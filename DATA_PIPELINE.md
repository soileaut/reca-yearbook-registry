# RECA Yearbook Registry — Data Pipeline

A research pipeline to identify every school impacted by RECA (Radiation
Exposure Compensation Act) in the St. Louis, Missouri area, verify their
history, and locate which of their yearbooks already exist — digitized or
physical — across libraries and archives. The output feeds a downstream
app (`homeroom-archive`) that lets people select undigitized yearbooks to
scan.

This document is a running history of how the project's workflow was
designed and what was learned along the way. See `NEXT_STEPS.md` for
what's planned going forward.

## The core problem

The starting point was a single spreadsheet, `RECA Schools DB.csv` (650
rows), covering schools across ~20 RECA-impacted ZIP codes. It was itself
produced by an earlier AI pass and was known to be messy: inconsistent
date formats, 43 distinct free-text values in a `Status` column, and (as
later confirmed) some outright hallucinated/phantom school entries.

The work has two independent tracks against a shared schema:

- **Track A — data cleanup.** Verify each school's identity, opened/closed
  dates, and consolidation/successor relationships, with real citations.
- **Track B — archive survey.** For a given institution (a library,
  university archive, etc.), determine which schools' yearbooks it holds,
  digitized or physical.

## Why a pilot first

Rather than scaling to all 650 rows immediately, a 12-school pilot (ZIP
63147) was run first as two parallel Devin sessions — one Track A, one
Track B — to validate the schema and guardrails before committing to the
full dataset. See `pilot/` for the original task prompts and output.

**What the pilot caught, that justified doing it this way:**
- The seed data itself contains phantom entities (`Baden High School`
  appears to never have existed) and unresolved identities (`North High
  School` doesn't match any real SLPS school).
- The "~92 yearbooks" figure initially assumed for St. Louis County
  Library was wrong — SLCL's actual digitized collection is ~90
  school-level collections totaling ~1,400 volumes.
- Several schools' real ZIP codes didn't match the ZIP they were listed
  under (e.g. Beaumont High School is actually in 63107, not 63147) —
  they were included because they *served* that community, a distinction
  the raw data's `ZIP Inclusion` column already captured.

## Key design decisions, in the order they came up

1. **Schema-first.** `schema.md` is the single shared contract every
   research task (pilot or scaled) must output to, so independent agent
   sessions produce mergeable results without a manual reconciliation
   pass.
2. **Web-search/browsing only, ever.** No session may call, email, or
   otherwise contact an institution or person. Anything requiring human
   outreach gets flagged as a recommended follow-up, never acted on.
3. **Cite-or-mark-unverified, always.** No confidence field may be left
   blank; no factual claim may be stated without a real citation.
4. **RECA date scope: 1949 onward.** RECA coverage for St. Louis begins
   January 1, 1949 (open-ended, no end date) — so school year 1948-1949
   is the first real yearbook-search target. Pre-1949 history still
   matters for Track A (establishing identity/successor chains), just not
   as a yearbook search target for Track B.
5. **ZIP tracking was dropped from the schema entirely.** Initially the
   schema tracked which ZIP(s) each school was relevant to
   (`also_relevant_to_zips`), to support ZIP-based ZIP-matching for
   claimants. This was removed once it was confirmed the downstream app
   doesn't match claimants to schools by ZIP at all — it just offers
   whichever yearbooks are undigitized, regardless of ZIP. Schools are
   simply a flat list of "impacted schools."
6. **Two separate dedup problems, two separate tools:**
   - `yearbook_registry_master.json` + `merge_registry.py` — once a
     yearbook is confirmed digitized at one institution, future
     institution surveys (Track B) skip actively re-searching for it.
   - `schools_master.json` + `find_potential_duplicates.py` +
     `dedupe_seed.py` — the raw seed data lists the same real-world
     school many times (once per ZIP it served); a school should only
     ever be researched once.
7. **Deduplication must never risk silently dropping a real school.**
   An early version of `dedupe_seed.py` used fuzzy string-similarity
   matching and nearly merged real, distinct schools together purely on
   coincidental character overlap (e.g. "Pattonville Heights Middle
   School" vs "Pattonville High School" scored 0.94 similarity despite
   being different buildings, because "Heights" and "High" share
   characters). The fix: **only exact name/alias matches are
   auto-collapsed.** Anything merely similar is flagged in a
   `*_review_needed.json` file and left as a separate row by default —
   redundant research is an acceptable cost; a silently-dropped real
   school is not.
8. **Different campuses are never auto-merged**, even with an identical
   name/alias, since a relocated or multi-campus school can be a
   functionally distinct entity (different building, possibly a separate
   yearbook series). Detected via campus/building/site keywords in the
   name and handled as a special case in `dedupe_seed.py`.
9. **"School District"-named rows need explicit disambiguation.** A row
   like "Baden School District" could be a pure administrative body (no
   yearbook of its own — the real targets are its member schools) or a
   small one-school district where the district name and the school are
   effectively the same thing. This can't be assumed either way; it's
   now a required research step (`entity_type` field) before any
   yearbook search is attempted on such a row.
10. **Scaling via Devin's "Agent Fan-Out," not an external API.** Devin's
    session API requires a paid/team tier not available here. Instead,
    a single coordinator Devin session (`track_a_coordinator_prompt.md`)
    is given the job of partitioning the remaining work and spinning up
    managed child sessions itself, rather than a human opening many tabs
    or a script calling an external API.

## Current status (as of this writing)

- **Pilot complete and merged to `main`:** 12 schools (ZIP 63147) fully
  researched (Track A) and surveyed against St. Louis County Library
  (Track B). See `pilot/`.
- **Track A scale-up complete and merged to `main` (PR #3):** the
  remaining 325 deduplicated schools were researched via a coordinator
  Devin session that partitioned the work into 22 batches and ran them
  through Agent Fan-Out. `schools_master.json`/`.csv` now cover all
  **337 schools** (12 pilot + 325 scale-up). See
  `batches/track_a_scaleup_summary.md` for the aggregated data-quality
  findings (phantom-row flags, cross-batch duplicate candidates, seed
  data errors) carried forward from all 22 batches.
- **Not yet started:** resolving the flagged ambiguous-duplicate/phantom
  rows surfaced by the scale-up (see `NEXT_STEPS.md`), and any Track B
  survey beyond St. Louis County Library.

## Repo map

```
schema.md                      -- the shared data contract (read this first)
DATA_PIPELINE.md               -- this file
NEXT_STEPS.md                   -- what's planned going forward

data/
  RECA_Schools_DB.csv           -- original raw source spreadsheet
  all_schools_seed.json          -- same data, JSON with stable row_ids
  remaining_schools_seed.json    -- all_schools_seed minus already-researched rows
  schools_seed_deduped.json      -- deduplicated work list (325 unique schools)
  schools_seed_deduped_review_needed.json -- ambiguous dedup cases, flagged not resolved

pilot/                          -- the ZIP 63147 pilot (Track A + Track B), completed
  pilot_seed_63147.json/.csv
  track_a_prompt.md / track_b_prompt.md
  schools_63147.json / .csv      -- Track A output
  track_a_notes.md
  yearbook_registry_slcl_63147.json -- Track B output (SLCL survey)
  track_b_notes.md

batches/                        -- Track A scale-up output (22 batches), completed
  schools_seed_batchNN.json      -- per-batch input (subset of schools_seed_deduped.json)
  schools_batchNN.json           -- per-batch Track A output
  track_a_notes_batchNN.md       -- per-batch process notes
  track_a_scaleup_summary.md    -- coordinator's aggregated findings across all 22 batches

track_a_coordinator_prompt.md   -- task spec used for the Track A scale-up (completed; kept as a reusable template)

schools_master.json             -- merged schools table across all completed work
yearbook_registry_master.json   -- merged yearbook registry across all completed work

merge_schools.py                -- regenerates schools_master.json
merge_registry.py               -- regenerates yearbook_registry_master.json
find_potential_duplicates.py    -- flags new rows that match already-researched schools
dedupe_seed.py                  -- self-deduplicates raw seed rows (exact-match only, safe)
compute_reca_scope.py           -- deterministically computes reca_scope_status
json_to_csv.py                  -- converts any schema JSON file to CSV for visual inspection
```

See `NEXT_STEPS.md` for what's planned going forward.
