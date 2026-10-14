# RECA Yearbook Registry — Data Pipeline

> Working history of how this project was built — written for contributors
> and the curious. For the searchable public registry itself, see the
> project's GitHub Pages site. Spot an error in the data? Please report it
> via the site's form — corrections are the point of publishing it.

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
- The seed data itself contains entries no independent source confirms —
  e.g. `Baden High School` has no evidence it ever existed, and
  `North High School` doesn't match any real SLPS school. These stay
  flagged as unverified rather than silently dropped.
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
   claimants. This was removed once it was confirmed the research schema
   didn't need it — schools are simply a flat list of "impacted schools."
   (The public site does still offer ZIP search for visitors, but that
   reads the school's own ZIP field rather than a served-ZIP mapping.)
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
- **Track B round-1 fan-out complete and merged to `main` (PR #4, 2026-10-12):**
  `track_b_fanout_prompt.md` partitioned the archive survey into 7 named
  surfaces (Archdiocese of St. Louis, Concordia Historical Institute,
  SHSMO/WHMC, St. Charles Co. Historical Society, SLCL Digital full
  scale-up, SLCL Physical full scale-up, north county municipal
  libraries), run via Agent Fan-Out, same pattern as Track A.
  `yearbook_registry_master.json` now has **1,235 rows** across 8
  sources; `flat_yearbook_registry.csv` covers 779 school-years (319
  `digitally_secured`, 137 `physical_only_known`, 280 `needs_scan`, rest
  unverdicted). Per-surface notes are in `track_b_notes_*.md`; raw
  enumerated indexes in `data/archive_indexes/`.
- **Round-1 reconciliation fix (same PR):** the fan-out prompt and
  `concordia_hist` rows referenced a phantom `ALL-651` (LHS North — no
  seed row ever existed). Resolved additively: `schools_lutheran_hs.json`
  minted real cited rows for ALL-651/652/653 (LHS North/South/Central),
  +43 registry rows for the Central and South CHI holdings.
  `schools_master.json` now covers **340 schools**.
- **Track C — Districts & Consolidation Chains complete and merged
  (PRs #5, #6, 2026-10-14):** a single-researcher pass per
  `track_c_prompt.md` (plus two in-flight addenda) that (1) canonicalized
  `district_operator` across all schools — 127 rows normalized, original
  lineage strings preserved in notes; (2) filled `successor_school_id`
  gaps — every dead-end reference resolved (repointed to surviving
  dedupe ids or to six newly-minted receiver schools, ALL-901–905),
  `schools_master.json` now covers **346 schools** with zero dangling
  successors; (3) built `districts_master.json` — **70 district/operator
  entities** with formed/dissolved years, predecessor/successor links,
  and `records_office` contact blocks; and (4) addendum 2 — a
  `reca_request` block on every district recording whether a
  **documented RECA-specific request path** exists (46 documented /
  22 generic-only / 2 unknown), with plain-language `display_text`
  written for verbatim display to claimants. `merge_schools.py` was
  patched to dedupe on `school_id` so update files apply as corrections.
- **Public site gained the lineage strip (2026-10-14):**
  `build_lineage.py` emits `publish/school_lineage.json` — per-school
  successor-chain trees with records-office payloads resolved onto
  terminal nodes via a normalized `district_operator`→district join
  (parish strings resolve through their "/ Archdiocese" custodian half).
  The site renders an inline boxes-and-arrows chain on school select
  (closed-year labels on arrows, weak-confidence edges marked
  "likely"/"unverified"), plus a records box showing the terminal
  district's office link, instructions, as-of date, and a
  RECA-process badge when `reca_request.documented`.
- **Track B round-2 fan-out designed and ready to run (not yet executed):**
  `track_b_round2_prompt.md` covers the remaining surfaces —
  `archive_org`, `mohistory`, `mercantile_umsl`, `stcharles_lib`,
  `school_self_hosted` (tier 1, splittable by district), plus full-index
  surveys of `slu`/`wustl`/`umsl`/`stlcc` (+optional `lindenwood`).
- **Publication layer built:** `build_public_registry.py` generates
  `publish/public_yearbook_registry.csv` — an expanded claimant-facing
  grid of **14,406 rows** (every in-scope school × every school-year it
  operated from 1949 on, including unsearched years, so missing years are
  visible rather than omitted; 291 schools, 49 excluded as
  closed-pre-1949/admin-district-only). Rows roll up the same
  `scan_status` semantics as the flat file plus `where_located`,
  `view_online`, `digital_in_library`, `physical_location`, and
  `also_known_as` (historical names for alias search). A "digitized but
  in-library-only" access phrase does **not** mark a year secured — it
  gets `digital_in_library_only` and remains a scan target.
- **Public site built (`docs/`, GitHub Pages source):** a self-contained
  static page serving the public CSV with combobox pickers (school name
  with historical-name matching, or ZIP code — one or the other), a year
  selector, a live-computed status summary line, paginated results with
  clickable source links, CSV download, and calls-to-action to two
  Google Forms: a report form (yearbook leads + corrections) and a
  testimonials form (consent-checked stories for the planned Substack
  article). Enabling Pages is a repo Settings toggle; the live URL will
  be `soileaut.github.io/reca-yearbook-registry`.
- **Not yet started:** enabling GitHub Pages, resolving the flagged
  ambiguous-duplicate/phantom rows surfaced by the scale-up (see
  `NEXT_STEPS.md`), and actually running the Track B round-2 fan-out above.

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
  digital_archives.json          -- Track B archive inventory: authority tiers, short display
                                     names, per-archive coverage_status/covered_schools
  archive_indexes/               -- raw enumerated per-archive listings (Track B fan-out output)

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

track_b_fanout_prompt.md       -- task spec for the Track B round-1 fan-out (completed)
track_b_round2_prompt.md       -- task spec for the Track B round-2 fan-out (ready to run)
track_b_notes_*.md             -- per-surface process notes from Track B workers

track_c_prompt.md              -- task spec for Track C districts/consolidation (completed, PRs #5-6)
track_c_notes.md               -- Track C adjudication write-up + addendum notes
schools_track_c_updates.json   -- Track C school-row updates (merged via merge_schools.py)
districts_master.json          -- district/operator entities: lineage + records_office
                                    + reca_request (display-ready claimant instructions)

schools_lutheran_hs.json       -- seed-style rows minted during round-1 reconciliation
                                    (ALL-651/652/653 Lutheran HS North/South/Central)
schools_master.json             -- merged schools table across all completed work
yearbook_registry_master.json   -- merged yearbook registry across all completed work
flat_yearbook_registry.csv      -- pivoted, human/publish-ready view (one row per school+year,
                                    with scan_status rollup) -- regenerate via flatten_registry.py
citation_collisions.json        -- flatten_registry.py output: citation_urls reused across
                                    different school_ids, needs human review if non-empty

publish/
  public_yearbook_registry.csv -- expanded public grid: every in-scope school x year (1949+),
                                    incl. unsearched years -- regenerate via build_public_registry.py
  school_lineage.json          -- per-school successor trees + records payloads --
                                    regenerate via build_lineage.py
docs/                          -- GitHub Pages site (static, no dependencies)
  index.html                   -- combobox search UI + lineage strip + records box + form links
  public_yearbook_registry.csv -- copy of publish/ output; copy again whenever it regenerates
  school_lineage.json          -- copy of publish/ output; copy again whenever it regenerates

merge_schools.py                -- regenerates schools_master.json
merge_registry.py               -- regenerates yearbook_registry_master.json
flatten_registry.py             -- regenerates flat_yearbook_registry.csv + citation_collisions.json
build_public_registry.py        -- regenerates publish/public_yearbook_registry.csv
build_lineage.py                -- regenerates publish/school_lineage.json
find_potential_duplicates.py    -- flags new rows that match already-researched schools
dedupe_seed.py                  -- self-deduplicates raw seed rows (exact-match only, safe)
compute_reca_scope.py           -- deterministically computes reca_scope_status
json_to_csv.py                  -- converts any schema JSON file to CSV for visual inspection
```

See `NEXT_STEPS.md` for what's planned going forward.
