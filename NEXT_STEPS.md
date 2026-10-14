# Next Steps

> Working roadmap for project contributors. If you came here from the
> public registry site and found a mistake in the data — please tell us
> via the site's report form. Corrections are the point of publishing it.

See `DATA_PIPELINE.md` for full background and how we got here.

**Done:** Pilot (12 schools), Track A scale-up (325 more, PR #3),
Track B round-1 fan-out (7 archive surfaces, PR #4), and Track C
districts/consolidation research (PRs #5–6) are all complete and merged
to `main`. `schools_master.json`/`.csv` now cover 346 schools
(337 + 3 LAHE Lutheran high schools + 6 Track-C-minted receivers) and
`districts_master.json` covers 70 district/operator entities;
`yearbook_registry_master.json` has 1,235 rows across 8 sources;
`flat_yearbook_registry.csv` covers 779 school-years (319
digitally_secured / 180 physical_only_known / 280 needs_scan).
`track_b_round2_prompt.md` is written and ready to run (not yet
executed) — see item 2 below.

Also done: the **publication layer** — `build_public_registry.py`
produces `publish/public_yearbook_registry.csv`, the expanded
claimant-facing grid (14,406 rows: every in-scope school × every
school-year 1949+, incl. unsearched years; 291 schools, 49 excluded as
closed-pre-1949/admin-only). A static site in `docs/` (GitHub Pages
source, live at soileaut.github.io/reca-yearbook-registry) provides
school-name/ZIP combobox search, year filter, live status counts, an
inline successor-chain strip + records-instructions box per selected
school (from `build_lineage.py`/`school_lineage.json`), CSV download,
and links to two live Google Forms — a report form (yearbook leads +
corrections) and a testimonials form (stories for the planned Substack
article).

## 1. Resolve flagged ambiguous/phantom rows

The scale-up surfaced real ambiguities that need a human (or a dedicated
follow-up research pass) to resolve, now with real data in hand instead
of just names:

- **Unverified rows** (~13, listed in
  `batches/track_a_scaleup_summary.md`) — schools the source data claims
  but no independent source has yet confirmed. They stay in the registry
  as `unknown_insufficient_data` rather than being dropped — if you know
  one of these schools existed, that's exactly what the report form is
  for.
- **Known possible-duplicate pairs** (~20, same file) — pairs of rows that
  may describe the same real school under different names (e.g. a school
  and its renamed successor: Hazelwood Central chain, Pattonville HS
  lineage, Kinloch HS successor chain). They were deliberately kept
  separate rather than auto-merged — merging wrongly loses a real school,
  keeping both only costs a redundant row. Each needs a judgment call
  informed by the opened/closed/successor data now on file.
- **The original 63 rows** in `data/schools_seed_deduped_review_needed.json`
  (fuzzy-similar or same-name-different-campus) — cross-reference against
  the above now that real research exists for most of them.
- **Seed data errors found** (ZIP served-vs-physical confusion, wrong
  operators, shifted columns, date errors) — already corrected in
  `schools_master.json` by the batch workers; no action needed unless
  auditing.
- ~~Dead-end successor links~~ — **resolved by Track C (PR #5)**: all
  dead ends traced to dedupe-folded seed rows and repointed, six missing
  receiver schools minted (ALL-901–905). Zero dangling successors.
- ~~Unestablished successor links~~ — **resolved by Track C**: the
  closed+`none`/`unknown` population was adjudicated — real successor
  links filled where they exist, "records stayed with the district"
  recorded in notes where they don't. `districts_master.json` now
  carries the district-level answer (records_office + reca_request)
  for the common "no successor school" case.

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

## 3. Community intake — interim forms live, automation future

The `docs/` site now links two Google Forms: a **report form**
(yearbook leads + registry corrections; school / ZIP / free-text
year-ranges / conditional sections by report type) and a **testimonials
form** (stories for the Substack article, with publish/anonymous/private
consent choices). Interim workflow is manual triage of form responses
into data fixes. Remaining ideas, cheapest first:

- **Prefilled GitHub issue links** embedded per-row/per-school in the
  Pages site (`issues/new?title=...&labels=claim-report`) — zero backend,
  but requires the reporter to have a GitHub account.
- **Issue forms** (`yaml` templates) for structured intake: school_id,
  year, report type (have-book / wrong-location / other).
- **GitHub Actions on issue-open**: label triage; a light validation job
  could re-check the cited URL's liveness or re-run `flatten_registry.py`
  for the flagged school. Full agentic re-research would need a session
  trigger — the same constraint that pushed scale-ups to manual fan-out.
- If GitHub-account friction is too much for the audience: a static form
  → a free serverless shim (e.g. Cloudflare Worker + Turnstile, ~20
  lines, holds a GitHub token server-side — tokens can never live in the
  page itself) → creates the issue via the GitHub API → an Actions
  workflow on issue-open does triage/re-verification. Actions can't
  receive inbound HTTP, so something thin must hold the credential —
  that's the only non-GitHub piece.

## 4. Repo housekeeping (optional, low priority)

- The remote branches `track-a/batch01`–`22`, `track-a/integration`, and
  `track-a/seeds` are fully merged into `main` and safe to delete — all
  their commits remain reachable via the merge commit's history.
- Same for `track-b/archstl_archives`, `concordia_hist`,
  `north_county_municipal_libs`, `scchs`, `shsmo`, `slcl_digital`,
  `slcl_physical`, and `track-b/integration` — all merged into `main` via
  PR #4.

