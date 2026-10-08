"""
Merges all per-task yearbook_registry_*.json files under pilot/ (and any
future task folders) into one master file: yearbook_registry_master.json.

This master file is what future archive-survey task prompts should check
BEFORE spending search effort on an institution, to avoid re-searching for
yearbooks that are already confirmed digitized elsewhere.

Run with:
    python3 merge_registry.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
MASTER_OUT = ROOT / "yearbook_registry_master.json"


def main():
    rows = []
    for path in sorted(ROOT.rglob("yearbook_registry_*.json")):
        if path.name == MASTER_OUT.name:
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        print(f"Merged {len(data)} rows from {path.relative_to(ROOT)}")
        rows.extend(data)

    MASTER_OUT.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"\nWrote {len(rows)} total rows to {MASTER_OUT}")

    digitized = [r for r in rows if r.get("digitized_status") == "digitized"]
    print(f"Of which {len(digitized)} are confirmed digitized "
          f"(these should be SKIPPED in future institution-survey searches).")


if __name__ == "__main__":
    main()
