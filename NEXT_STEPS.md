# Next Steps

See `DATA_PIPELINE.md` for full background and how we got here.

**Done:** Pilot (12 schools) and the Track A scale-up (325 more schools,
PR #3) are both complete and merged to `main`. `schools_master.json`/`.csv`
now cover all 337 schools. `track_b_fanout_prompt.md` is written and ready
to run (not yet executed) — see item 2 below.

## 1. Resolve flagged ambiguous/phantom rows

The scale-up surfaced real ambiguities that need a human (or a dedicated
follow-up research pass) to resolve, now with real data in hand instead
of just names:

- **Likely-phantom rows** (~13, listed in
  `batches/track_a_scaleup_summary.md`) — e.g. "DeSmet School," "Oasis
  Institute," "St. Peter School" — no independent verification found.
  Decide whether to drop, keep as `unknown_insufficient_data`, or research
  further.
- **Cross-batch duplicate candidates** (~20 pairs, same file) — same-school
  pairs that were deliberately kept separate per the no-silent-merge rule
  (e.g. Hazelwood Central chain, Pattonville HS lineage, Kinloch HS
  successor chain). Each needs a human judgment call informed by the
  actual opened/closed/successor data now available.
- **The original 63 rows** in `data/schools_seed_deduped_review_needed.json`
  (fuzzy-similar or same-name-different-campus) — cross-reference against
  the above now that real research exists for most of them.
- **Seed data errors found** (ZIP served-vs-physical confusion, wrong
  operators, shifted columns, date errors) — already corrected in
  `schools_master.json` by the batch workers; no action needed unless
  auditing.

## 2. Run the Track B fan-out (archive surveys) — ready, not yet started

`track_b_fanout_prompt.md` is written and ready to hand to a coordinator
Devin session: it partitions the remaining archive survey into 7 named
surfaces (Archdiocese of St. Louis, Concordia Historical Institute,
SHSMO/WHMC, St. Charles Co. Historical Society, SLCL Digital full
scale-up, SLCL Physical full scale-up, north county municipal libraries),
each run via Agent Fan-Out, same pattern as `track_a_coordinator_prompt.md`.
Each child tags its rows with `source_archive_id`; after merging,
`flatten_registry.py` rolls up a `scan_status` verdict per school/year
across every institution and flags any citation collisions for review
before the PR is opened.

Remaining institutions not yet covered by a named surface above (SLU,
WashU, UMSL, Mizzou, Missouri History Museum, etc. — see
`data/digital_archives.json` for the full inventory and `coverage_status`
per institution) would be a follow-up fan-out using the same pattern.

## 3. Repo housekeeping (optional, low priority)

- The remote branches `track-a/batch01`–`22`, `track-a/integration`, and
  `track-a/seeds` are fully merged into `main` and safe to delete — all
  their commits remain reachable via the merge commit's history.

