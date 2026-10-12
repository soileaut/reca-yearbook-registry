#!/usr/bin/env python3
"""
Pivot yearbook_registry_master.json (one row per school_id+year+institution,
per schema.md Table 2) into a flat human-review/publish CSV, AND perform the
cross-institution reconciliation described in schema.md's "Cross-institution
reconciliation" section:

    school_id, school_name, year, digital_sources, digital_location,
    physical_sources, physical_location, checked_not_found_at, scan_status

"digital_sources" / "physical_sources" are pipe-joined short, clean
institution labels (schema.md's `short_name`, e.g. "SLCL Digital Archives",
"Archdiocese of St. Louis Archives") intended as a filterable/groupable
column for downstream publishing (e.g. a Substack table). The matching
"_location" column keeps the full detail (link/call-number/citation) for
the same institutions, in the same order.

Multiple institutions for the same (school_id, year) are joined with " | ".
"digital_location" / "physical_location" cells contain
"<holding_institution>: <access_info or citation_url>" per hit, or are left
blank if nothing was found at that status for that cell.

`scan_status` is a rolled-up verdict across ALL institutions for that
(school_id, year), computed here (never by an individual child/session):
  - digitally_secured      -- a digitized copy exists at an authority_tier
                               1 or 2 archive (school/district-hosted or
                               institutional custody). No scan needed.
  - rescan_recommended     -- the only digitized copy(ies) found are from
                               a tier-3 (aggregator/weak-provenance)
                               archive. A properly-sourced scan is still
                               wanted.
  - physical_only_known    -- no digitized copy anywhere, but a physical
                               location is known -- a scan target, and we
                               know where to borrow/access the book.
  - needs_scan             -- nothing found anywhere (or only not_found /
                               unknown rows) -- open scan target with no
                               known lead yet.

Also writes `citation_collisions.json` if the same citation_url is cited
for two different school_ids -- a sign one child matched a decoy name and
needs human review.

Usage:
    python3 flatten_registry.py [registry_file] [schools_file] [archives_file] [output_csv]

Defaults: yearbook_registry_master.json, schools_master.json,
data/digital_archives.json, flat_yearbook_registry.csv
"""
import csv
import json
import sys
from collections import defaultdict

REGISTRY_FILE = sys.argv[1] if len(sys.argv) > 1 else "yearbook_registry_master.json"
SCHOOLS_FILE = sys.argv[2] if len(sys.argv) > 2 else "schools_master.json"
ARCHIVES_FILE = sys.argv[3] if len(sys.argv) > 3 else "data/digital_archives.json"
OUTPUT_FILE = sys.argv[4] if len(sys.argv) > 4 else "flat_yearbook_registry.csv"
COLLISIONS_FILE = "citation_collisions.json"


def school_name_map(schools):
    return {s["school_id"]: s.get("name", "") for s in schools}


def location_str(row):
    loc = row.get("access_info") or row.get("citation_url") or "link unavailable"
    inst = row.get("holding_institution", "unknown institution")
    return f"{inst}: {loc}"


def source_name(row, name_map):
    archive_id = row.get("source_archive_id")
    return name_map.get(archive_id) or row.get("holding_institution", "Unknown source")


def archive_lookup_maps(archives_file):
    try:
        with open(archives_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        return {}, {}
    archives = data.get("archives", [])
    tier_map = {a["archive_id"]: a.get("authority_tier") for a in archives}
    name_map = {a["archive_id"]: a.get("short_name", a.get("name")) for a in archives}
    return tier_map, name_map


def compute_scan_status(rows, tier_map):
    """rows: list of registry rows sharing one (school_id, year) key."""
    has_tier12_digitized = False
    has_tier3_digitized = False
    has_physical = False
    for row in rows:
        status = row.get("digitized_status")
        tier = tier_map.get(row.get("source_archive_id"))
        if status == "digitized":
            if tier in (1, 2):
                has_tier12_digitized = True
            elif tier == 3:
                has_tier3_digitized = True
            else:
                # unknown source_archive_id / not in inventory -- treat as
                # weak provenance until a child tags it properly.
                has_tier3_digitized = True
        elif status == "physical_only":
            has_physical = True

    if has_tier12_digitized:
        return "digitally_secured"
    if has_tier3_digitized:
        return "rescan_recommended"
    if has_physical:
        return "physical_only_known"
    return "needs_scan"


def main():
    with open(REGISTRY_FILE) as f:
        registry = json.load(f)
    with open(SCHOOLS_FILE) as f:
        schools = json.load(f)
    names = school_name_map(schools)
    tier_map, archive_name_map = archive_lookup_maps(ARCHIVES_FILE)

    grouped = defaultdict(list)
    for row in registry:
        grouped[(row["school_id"], row["year"])].append(row)

    # Only check citations on digitized/physical_only rows -- a citation_url
    # there is supposed to point to one specific item/record. not_found rows
    # legitimately and correctly cite the same general search/index page
    # across many schools (there's no item-specific URL for "nothing found"),
    # so including them here would just produce false-positive collisions.
    citation_map = defaultdict(set)
    for row in registry:
        if row.get("digitized_status") not in ("digitized", "physical_only"):
            continue
        url = row.get("citation_url")
        if url:
            citation_map[url].add(row["school_id"])
    collisions = {url: sorted(ids) for url, ids in citation_map.items() if len(ids) > 1}
    # Always (re)write this file so a stale result from a prior run/bug can
    # never linger silently -- an empty {} is itself a meaningful, current
    # "no collisions found" result.
    with open(COLLISIONS_FILE, "w") as f:
        json.dump(collisions, f, indent=2)
    if collisions:
        print(f"WARNING: {len(collisions)} citation_url(s) cited for multiple school_ids "
              f"-- see {COLLISIONS_FILE}, review before trusting those rows.")
    else:
        print(f"No citation collisions found (see {COLLISIONS_FILE}).")

    rows_out = []
    for (school_id, year), rows in sorted(grouped.items()):
        digitized_rows = [r for r in rows if r.get("digitized_status") == "digitized"]
        physical_rows = [r for r in rows if r.get("digitized_status") == "physical_only"]
        not_found = [r.get("holding_institution", "unknown institution")
                     for r in rows if r.get("digitized_status") == "not_found"]
        rows_out.append({
            "school_id": school_id,
            "school_name": names.get(school_id, "UNKNOWN_SCHOOL_ID"),
            "year": year,
            "digital_sources": " | ".join(source_name(r, archive_name_map) for r in digitized_rows),
            "digital_location": " | ".join(location_str(r) for r in digitized_rows),
            "physical_sources": " | ".join(source_name(r, archive_name_map) for r in physical_rows),
            "physical_location": " | ".join(location_str(r) for r in physical_rows),
            "checked_not_found_at": " | ".join(not_found),
            "scan_status": compute_scan_status(rows, tier_map),
        })

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "school_id", "school_name", "year",
            "digital_sources", "digital_location",
            "physical_sources", "physical_location",
            "checked_not_found_at", "scan_status",
        ])
        writer.writeheader()
        writer.writerows(rows_out)

    print(f"Wrote {len(rows_out)} school+year rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
