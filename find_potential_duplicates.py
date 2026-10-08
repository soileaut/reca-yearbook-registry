"""
Flags potential duplicate schools between a NEW seed file (for the next
ZIP/task you're about to run) and schools_master.json (everything already
researched). Run this BEFORE starting a new Track A session, so you can
tell that session which schools to treat as "already exists, just add this
ZIP to also_relevant_to_zips" instead of researching from scratch.

This does NOT auto-merge anything -- fuzzy name matching is too risky to
trust blindly (different schools can have very similar names). It only
flags candidates for a human (or the next Track A session, explicitly
told) to confirm.

Usage:
    python3 find_potential_duplicates.py <new_seed_file.json>
"""

import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MASTER_PATH = ROOT / "schools_master.json"
SIMILARITY_THRESHOLD = 0.90

# Generic type-words that make short names look falsely similar
# ("Duello Elementary School" vs "Baden Elementary School") -- stripped
# before comparing, so the comparison focuses on the distinctive part of
# the name (e.g. "Duello" vs "Baden").
STOPWORDS = {
    "school", "schools", "elementary", "high", "middle", "junior", "senior",
    "public", "private", "parochial", "academy", "district", "college",
    "university", "community", "center", "of", "the", "st", "saint",
}


def normalize(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def core_tokens(normalized_name):
    return {t for t in normalized_name.split() if t not in STOPWORDS}


def all_names(row, name_key, alias_key):
    names = [row.get(name_key, "")]
    aliases = row.get(alias_key, "")
    if isinstance(aliases, list):
        names.extend(aliases)
    elif isinstance(aliases, str):
        names.extend(re.split(r"[;,]", aliases))
    return [normalize(n) for n in names if n and n.strip()]


def row_label(row, name_key, id_keys):
    for key in id_keys:
        if row.get(key):
            return row[key]
    return "?"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 find_potential_duplicates.py <new_seed_file.json>")
        sys.exit(1)

    seed_path = Path(sys.argv[1])

    if not MASTER_PATH.exists():
        print(f"No {MASTER_PATH.name} found yet -- nothing to compare against. "
              f"Run merge_schools.py first if prior task output exists.")
        sys.exit(0)

    with open(MASTER_PATH, encoding="utf-8") as f:
        master_rows = json.load(f)
    with open(seed_path, encoding="utf-8") as f:
        seed_rows = json.load(f)

    master_lookup = [
        (row.get("school_id", "?"), row.get("name", "?"), all_names(row, "name", "historical_names"))
        for row in master_rows
    ]

    found_any = False
    for seed_row in seed_rows:
        seed_names = all_names(seed_row, "School Name", "Historical/Former Name")
        seed_label = seed_row.get("School Name", "?")
        seed_id = row_label(seed_row, "School Name", ["row_id", "pilot_row_id"])

        best_matches = []
        for master_id, master_name, master_names in master_lookup:
            best_ratio = 0.0
            for sn in seed_names:
                sn_tokens = core_tokens(sn)
                for mn in master_names:
                    mn_tokens = core_tokens(mn)
                    # Require the distinctive (non-generic) parts of the
                    # names to actually overlap -- otherwise two unrelated
                    # schools sharing a generic suffix ("X Elementary
                    # School" vs "Y Elementary School") will falsely match.
                    if not sn_tokens or not mn_tokens:
                        continue
                    token_overlap = sn_tokens & mn_tokens
                    if not token_overlap:
                        continue
                    ratio = difflib.SequenceMatcher(None, sn, mn).ratio()
                    best_ratio = max(best_ratio, ratio)
            if best_ratio >= SIMILARITY_THRESHOLD:
                best_matches.append((master_id, master_name, round(best_ratio, 2)))

        if best_matches:
            found_any = True
            print(f"\nSeed row {seed_id} ({seed_label!r}) may already exist:")
            for mid, mname, ratio in sorted(best_matches, key=lambda x: -x[2]):
                print(f"  -> {mid} ({mname!r})  similarity={ratio}")

    if not found_any:
        print("No potential duplicates found above threshold "
              f"{SIMILARITY_THRESHOLD}. All seed rows look like new schools.")
    else:
        print("\nReview the above before starting the Track A task. For any "
              "confirmed match, instruct that session to reuse the existing "
              "school_id and add the new ZIP to `also_relevant_to_zips` "
              "instead of creating a new row.")


if __name__ == "__main__":
    main()
