# Next Steps

See `DATA_PIPELINE.md` for full background and how we got here.

**Done:** Pilot (12 schools) and the Track A scale-up (325 more schools,
PR #3) are both complete and merged to `main`. `schools_master.json`/`.csv`
now cover all 337 schools.

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

## 2. Scale Track B (archive surveys)

Repeat the Track B pattern (see `pilot/track_b_prompt.md`) against
additional institutions — SLU, WashU, UMSL, Mizzou, Missouri History
Museum, etc. Each survey must check `yearbook_registry_master.json` first
and skip re-searching for yearbooks already confirmed digitized
elsewhere. Given the scale (337 schools x N institutions), this is
likely its own coordinator + Agent Fan-Out pass, following the same
pattern as `track_a_coordinator_prompt.md`.

## 3. Repo housekeeping (optional, low priority)

- The remote branches `track-a/batch01`–`22`, `track-a/integration`, and
  `track-a/seeds` are fully merged into `main` and safe to delete — all
  their commits remain reachable via the merge commit's history.

