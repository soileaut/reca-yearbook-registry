"""
Merges all per-task schools_<scope>.json files into one master file:
schools_master.json.

Dedupes on school_id: files are merged in sorted filename order, and when a
later file contains a row with a school_id already merged, the LATER row wins.
That is how update files (e.g. schools_track_c_updates.json, which sorts after
schools_master.json… wait — see note) apply corrections without duplicating
rows. Actual duplicate *discovery* still happens via find_potential_duplicates.py.

Track C note: because an update file's rows carry the same confidence values
required by schema.md, "update wins" is additive-correction semantics — a Track C
update row must embed the full original row plus its changes, which
build_trackc.py / hand-authors do.

Run with:
    python3 merge_schools.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
MASTER_OUT = ROOT / "schools_master.json"


def main():
    rows_by_id = {}
    order = []
    for path in sorted(ROOT.rglob("schools_*.json")):
        if path.name == MASTER_OUT.name or "seed" in path.name:
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        replaced = sum(1 for r in data if r.get("school_id") in rows_by_id)
        print(f"Merged {len(data)} rows from {path.relative_to(ROOT)}"
              + (f" ({replaced} replaced existing school_ids)" if replaced else ""))
        for r in data:
            sid = r.get("school_id")
            if sid not in rows_by_id:
                order.append(sid)
            rows_by_id[sid] = r

    rows = [rows_by_id[sid] for sid in order]
    MASTER_OUT.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"\nWrote {len(rows)} total rows to {MASTER_OUT}")


if __name__ == "__main__":
    main()
