#!/usr/bin/env python3
"""
Builds docs/school_lineage.json — the per-school successor-chain +
records-office payload the public site renders as the lineage strip and
the "how to request records" box.

Shape per school_id:

  {
    "name": "...", "opened": "...", "closed": "..."|"open",
    "conf":  link confidence from the PARENT edge ("confirmed"/...),
    "children": [ <node>, ... ],          -- splits become siblings
    "records": { ... } | null             -- present on terminal nodes
  }

records payloads come from districts_master.json via a normalized
name join on the terminal node's district_operator (parish strings like
"X Parish / Archdiocese of St. Louis" resolve via their second half —
the archdiocese IS the documented custodian). Unmatched/ambiguous
operators produce records: null and are reported at build time.
reca_request fields are read via .get so the file absorbs addendum-2
data without changes.
"""
import json
import re
import sys
from pathlib import Path

SCHOOLS_FILE = sys.argv[1] if len(sys.argv) > 1 else "schools_master.json"
DISTRICTS_FILE = sys.argv[2] if len(sys.argv) > 2 else "districts_master.json"
OUTPUT_FILE = sys.argv[3] if len(sys.argv) > 3 else "publish/school_lineage.json"

STOPWORDS = ("school district", "schools", "district", "sd", "r ii", "r 2",
             "r iii", "r 3", "r iv", "r 4", "r v", "r 5", "r vi", "r 6",
             "co", "county", "mo")


def norm(s):
    s = re.sub(r"\([^)]*\)", "", s or "")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    for w in STOPWORDS:
        s = re.sub(r"\b" + w + r"\b", "", s)
    return " ".join(s.split())


def find_district(operator, nmap):
    """Return district row or None. Tries full string, then each
    '/ '-separated part (parish strings name their custodian)."""
    if not operator:
        return None
    for part in [operator] + [p.strip() for p in operator.split("/")]:
        hits = nmap.get(norm(part))
        if hits and len(hits) == 1:
            return hits[0]
    return None


def records_payload(district):
    if not district:
        return None
    ro = district.get("records_office") or {}
    rr = district.get("reca_request") or {}
    payload = {
        "district_name": district.get("name", ""),
        "office_name": ro.get("name") or district.get("name", ""),
        "url": rr.get("url") or ro.get("url"),
        "display_text": rr.get("display_text") or ro.get("notes") or "",
        "as_of": rr.get("as_of") or ro.get("as_of"),
        "reca_documented": rr.get("documented"),
        "confidence": rr.get("confidence") or ro.get("confidence"),
    }
    return payload if (payload["url"] or payload["display_text"]) else None


def build_node(sid, by_id, nmap, seen, link_conf):
    """Recursive chain node; `seen` guards cycles."""
    s = by_id.get(sid)
    if s is None:
        return {"id": sid, "name": f"({sid} — not yet in registry)",
                "opened": "", "closed": "?", "conf": "unknown",
                "children": [], "records": None}
    node = {
        "id": sid,
        "name": s.get("name", sid),
        "opened": s.get("opened_year") or "",
        "closed": s.get("closed_year") or "open",
        "conf": link_conf,
        "children": [],
        "records": None,
    }
    if sid in seen:
        return node
    seen.add(sid)
    succ = str(s.get("successor_school_id") or "").strip()
    if succ.lower() in ("", "none", "unknown"):
        node["records"] = records_payload(
            find_district(s.get("district_operator"), nmap))
        return node
    for part in re.split(r"[;,]", succ):
        part = part.strip()
        if part.lower() in ("", "none", "unknown"):
            continue
        child = build_node(part, by_id, nmap, set(seen),
                           s.get("successor_confidence") or "unknown")
        node["children"].append(child)
    if not node["children"]:
        node["records"] = records_payload(
            find_district(s.get("district_operator"), nmap))
    return node


def main():
    schools = json.load(open(SCHOOLS_FILE))
    districts = json.load(open(DISTRICTS_FILE))["districts"]
    by_id = {s["school_id"]: s for s in schools}
    nmap = {}
    for d in districts:
        nmap.setdefault(norm(d["name"]), []).append(d)

    out = {}
    unmatched = set()
    for s in schools:
        node = build_node(s["school_id"], by_id, nmap, set(), None)
        out[s["school_id"]] = node
        # tally which terminals lacked a district join
        def terms(n):
            if n["children"]:
                for c in n["children"]:
                    yield from terms(c)
            else:
                yield n
        for t in terms(node):
            ts = by_id.get(t["id"])
            if ts and t["records"] is None and ts.get("district_operator"):
                unmatched.add(ts["district_operator"][:60])

    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_FILE).write_text(json.dumps(out, indent=1))
    print(f"Wrote {len(out)} lineage entries to {OUTPUT_FILE}")
    have_rec = sum(1 for n in out.values()
                   if any(t["records"] for t in terms(n)))
    print(f"entries with a records payload: {have_rec}")
    if unmatched:
        print(f"unmatched district_operator values ({len(unmatched)}):")
        for u in sorted(unmatched):
            print("  ", u)


if __name__ == "__main__":
    main()
