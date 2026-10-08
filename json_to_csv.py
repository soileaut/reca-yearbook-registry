"""
Converts a JSON array of flat objects (e.g. schools_63147.json,
yearbook_registry_master.json) into a readable CSV for visual inspection.

Usage:
    python3 json_to_csv.py <input.json> [output.csv]

If output.csv is omitted, it writes next to the input file with a .csv
extension.
"""

import csv
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 json_to_csv.py <input.json> [output.csv]")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else in_path.with_suffix(".csv")

    with open(in_path, encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        print("Input JSON must be a non-empty array of objects.")
        sys.exit(1)

    # Union of all keys across all rows, preserving first-seen order.
    fieldnames = []
    for row in data:
        for k in row.keys():
            if k not in fieldnames:
                fieldnames.append(k)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            flat = {
                k: ("; ".join(v) if isinstance(v, list) else v)
                for k, v in row.items()
            }
            writer.writerow(flat)

    print(f"Wrote {len(data)} rows, {len(fieldnames)} columns -> {out_path}")


if __name__ == "__main__":
    main()
