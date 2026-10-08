"""
Self-deduplicates the raw seed dataset (data/all_schools_seed.json) BEFORE
partitioning into research batches. The raw CSV lists the same real-world
school many times (once per ZIP whose community it serves). This collapses
those into one representative row per distinct school, so each school is
only ever assigned to exactly one batch/child session.

Reuses the same core-token-overlap + similarity-ratio matching logic as
find_potential_duplicates.py (kept as a separate, simpler script here
since the comparison set and output shape differ).

Usage:
    python3 dedupe_seed.py <input_seed.json> [output.json]

Output: a JSON array where each element is:
{
  "representative": <the first-seen row for this school>,
  "duplicate_row_ids": [<row_id>, ...]   # other row_ids that matched it
}

This output is what should actually be partitioned into batches -- use
`representative` for research, and record `duplicate_row_ids` in that
school's eventual schools_master.json entry for provenance (optional).
"""

import difflib
import json
import re
import sys
from pathlib import Path

SIMILARITY_THRESHOLD = 0.90

STOPWORDS = {
    "school", "schools", "elementary", "high", "middle", "junior", "senior",
    "public", "private", "parochial", "academy", "district", "college",
    "university", "community", "center", "of", "the", "st", "saint",
}

# A different campus/building/site is a potentially distinct functional
# school (different location, possibly a separate yearbook series) even if
# it shares an identical name/alias with another row. Never auto-collapse
# these -- always flag for human review instead.
CAMPUS_KEYWORDS = {"campus", "building", "site", "location", "annex"}


def mentions_campus_distinction(row_name):
    return bool(core_tokens_raw(row_name) & CAMPUS_KEYWORDS)


def core_tokens_raw(name):
    return set(normalize(name).split())


def normalize(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def core_tokens(normalized_name):
    return {t for t in normalized_name.split() if t not in STOPWORDS}


def all_names(row):
    names = [row.get("School Name", "")]
    aliases = row.get("Historical/Former Name", "")
    if isinstance(aliases, list):
        names.extend(aliases)
    elif isinstance(aliases, str):
        names.extend(re.split(r"[;,]", aliases))
    return [normalize(n) for n in names if n and n.strip()]


def exact_match(names_a, names_b):
    """Only an EXACT normalized name/alias match is safe to auto-collapse.
    e.g. 'Pattonville High School - Original Campus' whose alias field is
    literally 'Pattonville High School' -- a real, unambiguous signal.
    Fuzzy-but-not-exact similarity (e.g. 'Pattonville Heights School' vs
    'Pattonville High School' at 0.94) is NOT safe: 'Heights' and 'High'
    are different words that happen to share characters. Auto-merging on
    fuzzy similarity risks silently dropping a real, distinct school from
    research entirely -- a worse failure than some redundant research."""
    return bool(set(names_a) & set(names_b))


def fuzzy_match(names_a, names_b):
    for a in names_a:
        a_tokens = core_tokens(a)
        if not a_tokens:
            continue
        for b in names_b:
            b_tokens = core_tokens(b)
            if not b_tokens or not (a_tokens & b_tokens):
                continue
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            if ratio >= SIMILARITY_THRESHOLD:
                return True
    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dedupe_seed.py <input_seed.json> [output.json]")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else in_path.with_name(
        in_path.stem + "_deduped.json"
    )

    with open(in_path, encoding="utf-8") as f:
        rows = json.load(f)

    clusters = []  # list of {"representative": row, "names": [...], "duplicate_row_ids": [...]}
    fuzzy_flags = []  # [(row_id, row_name, cluster_rep_id, cluster_rep_name, ratio-ish note)]

    for row in rows:
        names = all_names(row)
        row_id = row.get("row_id", row.get("pilot_row_id", "?"))
        row_name = row.get("School Name", "?")

        row_is_campus_variant = mentions_campus_distinction(row_name)

        matched_cluster = None
        for cluster in clusters:
            rep_name = cluster["representative"].get("School Name", "")
            rep_is_campus_variant = mentions_campus_distinction(rep_name)
            if row_is_campus_variant != rep_is_campus_variant:
                continue  # never cross-merge a campus-variant with a non-campus-variant
            if row_is_campus_variant:
                # Two campus-variant rows (e.g. both "- Original Campus")
                # may share the SAME alias as each other despite being
                # DIFFERENT campuses ("Original" vs "Current"). Require the
                # literal School Name itself to match -- alias overlap
                # alone isn't enough here.
                if normalize(row_name) == normalize(rep_name):
                    matched_cluster = cluster
                    break
            elif exact_match(names, cluster["names"]):
                matched_cluster = cluster
                break

        if matched_cluster:
            matched_cluster["duplicate_row_ids"].append(row_id)
            matched_cluster["names"].extend(names)
        else:
            # Not auto-collapsed (either no exact match, or it's a campus
            # variant) -- check if it's at least a FUZZY/exact-but-campus
            # near-miss worth flagging for human review.
            for cluster in clusters:
                rep = cluster["representative"]
                same_entity_text = exact_match(names, cluster["names"])
                if same_entity_text or fuzzy_match(names, cluster["names"]):
                    reason = "same name/alias but different campus" if (row_is_campus_variant or mentions_campus_distinction(rep.get("School Name",""))) and same_entity_text else "fuzzy similarity"
                    fuzzy_flags.append((
                        row_id, row_name,
                        rep.get("row_id", rep.get("pilot_row_id", "?")),
                        rep.get("School Name", "?"),
                        reason,
                    ))
            clusters.append({
                "representative": row,
                "names": names,
                "duplicate_row_ids": [],
            })

    output = [
        {
            "representative": c["representative"],
            "duplicate_row_ids": c["duplicate_row_ids"],
        }
        for c in clusters
    ]

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    dupes_collapsed = sum(len(c["duplicate_row_ids"]) for c in clusters)
    print(f"Input: {len(rows)} raw rows")
    print(f"Output: {len(clusters)} unique schools -> {out_path}")
    print(f"Auto-collapsed {dupes_collapsed} EXACT-match duplicate rows (safe, unambiguous).")

    if fuzzy_flags:
        flags_path = out_path.with_name(out_path.stem + "_review_needed.json")
        with open(flags_path, "w", encoding="utf-8") as f:
            json.dump([
                {"row_id": rid, "row_name": rname, "possible_match_id": mid,
                 "possible_match_name": mname, "reason": reason}
                for rid, rname, mid, mname, reason in fuzzy_flags
            ], f, indent=2)
        print(f"\n{len(fuzzy_flags)} rows are FUZZY near-matches to an existing cluster "
              f"but were NOT auto-collapsed -- they remain as separate schools pending "
              f"human review. See {flags_path}.")
        print("These are kept as separate (safer default) until a human confirms a merge.")


if __name__ == "__main__":
    main()
