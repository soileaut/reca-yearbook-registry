# Next Steps

See `DATA_PIPELINE.md` for full background and how we got here.

**Done:** Pilot (12 schools), Track A scale-up (325 more, PR #3), and
Track B round-1 fan-out (7 archive surfaces, PR #4) are all complete and
merged to `main`. `schools_master.json`/`.csv` now cover 340 schools
(337 + 3 LAHE Lutheran high schools added during round-1 reconciliation);
`yearbook_registry_master.json` has 1,235 rows across 8 sources;
`flat_yearbook_registry.csv` covers 779 school-years (319
digitally_secured / 137 physical_only_known / 280 needs_scan).
`track_b_round2_prompt.md` is written and ready to run (not yet
executed) — see item 2 below.

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

## 2. Run the Track B round-2 fan-out — ready, not yet started

Round 1 (PR #4) is done. `track_b_round2_prompt.md` is written and ready
to hand to a coordinator Devin session, covering the remaining surfaces:
`archive_org` (Internet Archive, tier 3 + per-item provenance),
`mohistory` (incl. the 2016 SLPS records transfer), `mercantile_umsl`
(M-423 SLPS collection lead), `stcharles_lib` (physical catalog,
~40 St. Charles rows), `school_self_hosted` (tier 1 district sites —
splittable into sub-children), and full-index surveys of `slu`, `wustl`,
`umsl`, `stlcc` (+ optional `lindenwood`) — where the university archive
is a search surface for the whole school list, not just its own yearbook.

Children branch from `main` (round-1 state is merged). Each tags rows
with `source_archive_id`; coordinator merges into `track-b2/integration`,
re-runs `merge_registry.py` + `flatten_registry.py`, checks
`citation_collisions.json`, opens a PR.

Surfaces already verified-empty or out of scope (no round-2 work needed):
`missouri_digital_heritage`, `webster_univ`, `mizzou`, `wgpl`,
`colleton_stl`, `fontbonne` (dead host), `whmc_umsl` (same catalog as
`shsmo`, done in round 1), `north_county_municipal_libs` (verified
negative).

## 3. Repo housekeeping (optional, low priority)

- The remote branches `track-a/batch01`–`22`, `track-a/integration`, and
  `track-a/seeds` are fully merged into `main` and safe to delete — all
  their commits remain reachable via the merge commit's history.
- Same for `track-b/archstl_archives`, `concordia_hist`,
  `north_county_municipal_libs`, `scchs`, `shsmo`, `slcl_digital`,
  `slcl_physical`, and `track-b/integration` — all merged into `main` via
  PR #4.

