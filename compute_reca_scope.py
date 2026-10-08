"""
Computes `reca_scope_status` for every row in a schools_<scope>.json file,
based on the deterministic rule: a school is out of RECA scope only if its
ENTIRE operating lifespan ended before 1949 (RECA St. Louis coverage starts
Jan 1, 1949 -> first relevant school year is 1948-1949).

Rule:
- closed_year is a confirmed/probable year strictly before 1949
    -> out_of_scope_closed_before_1949
- closed_year is "n/a" (still open) or a confirmed/probable year >= 1949
    -> in_scope
- anything else (closed_year is "unknown", or confidence is "unknown",
  or the year string can't be parsed) -> unknown_insufficient_data
  (kept in scope for research purposes until clarified -- do NOT discard)

Usage:
    python3 compute_reca_scope.py <schools_file.json> [output.json]

If output.json is omitted, overwrites the input file in place.
"""

import json
import re
import sys
from pathlib import Path

CUTOFF_YEAR = 1949


def parse_year(value):
    """Extract a 4-digit year from a string like '1908', '1950s', '1908-1910'."""
    if not value:
        return None
    match = re.search(r"\b(1[7-9]\d{2}|20\d{2})\b", str(value))
    return int(match.group(1)) if match else None


def compute_status(row):
    closed_year_raw = (row.get("closed_year") or "").strip().lower()
    closed_confidence = (row.get("closed_confidence") or "").strip().lower()

    if closed_year_raw == "n/a":
        return "in_scope"

    if closed_confidence in ("confirmed", "probable"):
        year = parse_year(closed_year_raw)
        if year is not None:
            return "in_scope" if year >= CUTOFF_YEAR else "out_of_scope_closed_before_1949"

    return "unknown_insufficient_data"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 compute_reca_scope.py <schools_file.json> [output.json]")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else in_path

    with open(in_path, encoding="utf-8") as f:
        rows = json.load(f)

    counts = {"in_scope": 0, "out_of_scope_closed_before_1949": 0, "unknown_insufficient_data": 0}
    for row in rows:
        status = compute_status(row)
        row["reca_scope_status"] = status
        counts[status] += 1

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    print(f"Wrote {len(rows)} rows -> {out_path}")
    for status, count in counts.items():
        print(f"  {status}: {count}")


if __name__ == "__main__":
    main()
