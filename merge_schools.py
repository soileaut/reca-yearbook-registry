"""
Merges all per-task schools_<scope>.json files into one master file:
schools_master.json. This is a naive concatenation — actual duplicate
resolution happens via find_potential_duplicates.py, run BEFORE starting a
new Track A task, not after.

Run with:
    python3 merge_schools.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
MASTER_OUT = ROOT / "schools_master.json"


def main():
    rows = []
    for path in sorted(ROOT.rglob("schools_*.json")):
        if path.name == MASTER_OUT.name:
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        print(f"Merged {len(data)} rows from {path.relative_to(ROOT)}")
        rows.extend(data)

    MASTER_OUT.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"\nWrote {len(rows)} total rows to {MASTER_OUT}")


if __name__ == "__main__":
    main()
