#!/usr/bin/env python3
"""
Builds the public, claimant-facing yearbook registry CSV by enumerating the
FULL grid of school-years (not just the years that were researched) and
left-joining the cross-institution verdicts from yearbook_registry_master.json.

Why: a person holding a physical yearbook needs a row for their school+year
even if we never researched it -- "absent from the list" must never be
confused with "doesn't exist". Unresearched years get their own status
(not_yet_checked), distinct from needs_scan (searched, nothing found).

Grid rules:
- One row per school per school-year, from max(1949, opened_year) through
  closed_year, or through CURRENT_YEAR if the school is still open or its
  closed_year is unknown (keep-everything bias: a false not_yet_checked row
  is cheaper than a missing real year).
- Pre-1949 years excluded entirely (RECA coverage starts Jan 1, 1949).
- Schools with reca_scope_status out_of_scope_closed_before_1949 or
  entity_type administrative_district_only are excluded.
- Registry rows with year "all" (exhaustive per-institution sweeps) apply
  to every enumerated year of that school.
- Registry years like "1972-1973" are normalized to the title (spring)
  year for joining to the single-year grid.

scan_status values reuse flatten_registry.py's verdicts
(digitally_secured / rescan_recommended / physical_only_known /
needs_scan), plus not_yet_checked for grid cells with no registry rows.

Usage:
    python3 build_public_registry.py [schools] [registry] [archives] [out.csv]

Defaults: schools_master.json, yearbook_registry_master.json,
data/digital_archives.json, publish/public_yearbook_registry.csv
"""
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

SCHOOLS_FILE = sys.argv[1] if len(sys.argv) > 1 else "schools_master.json"
REGISTRY_FILE = sys.argv[2] if len(sys.argv) > 2 else "yearbook_registry_master.json"
ARCHIVES_FILE = sys.argv[3] if len(sys.argv) > 3 else "data/digital_archives.json"
OUTPUT_FILE = sys.argv[4] if len(sys.argv) > 4 else "publish/public_yearbook_registry.csv"

RECA_START_YEAR = 1949
# Latest yearbook year plausibly published. Today is Oct 2026 -- the
# 2025-26 school yearbook (title year 2026) exists; 2026-27 doesn't yet.
CURRENT_YEAR = 2026

YEAR_RANGE_4 = re.compile(r"^(\d{4})\s*-\s*(\d{4})$")
YEAR_RANGE_2 = re.compile(r"^(\d{4})\s*-\s*(\d{2})$")
YEAR_SINGLE = re.compile(r"^\s*(\d{4})\s*$")


def parse_year(value):
    """Best-effort int year from free-text seed fields; None if unparseable."""
    if not value:
        return None
    m = YEAR_SINGLE.match(str(value))
    return int(m.group(1)) if m else None


def normalize_registry_year(value):
    """Map a registry `year` string to a grid year int, 'all', or None."""
    v = str(value).strip()
    if v.lower() == "all":
        return "all"
    m = YEAR_RANGE_4.match(v)
    if m:
        return int(m.group(2))
    m = YEAR_RANGE_2.match(v)
    if m:
        return int(m.group(1)[:2] + m.group(2))
    m = YEAR_SINGLE.match(v)
    return int(m.group(1)) if m else None


def compute_scan_status(rows, tier_map):
    """Mirror of flatten_registry.compute_scan_status -- keep in sync."""
    has_tier12 = has_tier3 = has_physical = False
    for row in rows:
        status = row.get("digitized_status")
        tier = tier_map.get(row.get("source_archive_id"))
        if status == "digitized":
            if tier in (1, 2):
                has_tier12 = True
            else:
                has_tier3 = True
        elif status == "physical_only":
            has_physical = True
    if has_tier12:
        return "digitally_secured"
    if has_tier3:
        return "rescan_recommended"
    if has_physical:
        return "physical_only_known"
    return "needs_scan"


def archive_maps(archives_file):
    data = json.load(open(archives_file))
    archives = data.get("archives", [])
    tier_map = {a["archive_id"]: a.get("authority_tier") for a in archives}
    name_map = {a["archive_id"]: a.get("short_name", a.get("name")) for a in archives}
    return tier_map, name_map


def source_name(row, name_map):
    archive_id = row.get("source_archive_id")
    return name_map.get(archive_id) or row.get("holding_institution", "Unknown source")


def location_str(row):
    loc = row.get("access_info") or row.get("citation_url") or "link unavailable"
    inst = row.get("holding_institution", "unknown institution")
    return f"{inst}: {loc}"


def main():
    schools = json.load(open(SCHOOLS_FILE))
    registry = json.load(open(REGISTRY_FILE))
    tier_map, name_map = archive_maps(ARCHIVES_FILE)

    # group registry rows by (school_id, normalized year); "all" kept aside
    per_year = defaultdict(list)
    all_years = defaultdict(list)
    for row in registry:
        ny = normalize_registry_year(row.get("year", ""))
        if ny == "all":
            all_years[row["school_id"]].append(row)
        elif ny is not None:
            per_year[(row["school_id"], ny)].append(row)

    rows_out = []
    skipped_schools = []
    for s in schools:
        sid = s["school_id"]
        if s.get("entity_type") == "administrative_district_only":
            skipped_schools.append((sid, "administrative_district_only"))
            continue
        if s.get("reca_scope_status") == "out_of_scope_closed_before_1949":
            skipped_schools.append((sid, "out_of_scope_closed_before_1949"))
            continue

        opened = parse_year(s.get("opened_year")) or RECA_START_YEAR
        closed = parse_year(s.get("closed_year")) or CURRENT_YEAR
        start = max(RECA_START_YEAR, opened)
        end = min(CURRENT_YEAR, closed)
        if end < start:
            skipped_schools.append((sid, f"unparseable span {s.get('opened_year')}-{s.get('closed_year')}"))
            continue

        for year in range(start, end + 1):
            rows = per_year.get((sid, year), []) + all_years.get(sid, [])
            if not rows:
                status, where, dloc, ploc, checked = "not_yet_checked", "", "", "", ""
            else:
                status = compute_scan_status(rows, tier_map)
                digitized = [r for r in rows if r.get("digitized_status") == "digitized"]
                physical = [r for r in rows if r.get("digitized_status") == "physical_only"]
                holders = []
                for r in digitized + physical:
                    n = source_name(r, name_map)
                    if n not in holders:
                        holders.append(n)
                checked_list = []
                for r in rows:
                    n = source_name(r, name_map)
                    if n not in checked_list:
                        checked_list.append(n)
                where = "; ".join(holders)
                dloc = " | ".join(location_str(r) for r in digitized)
                ploc = " | ".join(location_str(r) for r in physical)
                checked = "; ".join(checked_list)
            rows_out.append({
                "school_name": s.get("name", ""),
                "school_id": sid,
                "zip": s.get("zip", ""),
                "district_operator": s.get("district_operator", ""),
                "year": year,
                "scan_status": status,
                "where_located": where,
                "view_online": dloc,
                "physical_location": ploc,
                "checked_at": checked,
            })

    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "school_name", "school_id", "zip", "district_operator", "year",
            "scan_status", "where_located", "view_online",
            "physical_location", "checked_at",
        ])
        writer.writeheader()
        writer.writerows(rows_out)

    from collections import Counter
    print(f"Wrote {len(rows_out)} school-year rows to {OUTPUT_FILE}")
    print("scan_status counts:", dict(Counter(r["scan_status"] for r in rows_out)))
    if skipped_schools:
        print(f"Skipped {len(skipped_schools)} schools:", skipped_schools[:20])


if __name__ == "__main__":
    main()
