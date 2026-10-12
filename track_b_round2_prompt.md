# Track B Round 2 — Remaining Archive Surfaces

## Context

You are the coordinator session for a research project supporting a
yearbook digitization effort for RECA (Radiation Exposure Compensation Act)
claimants in the St. Louis, Missouri area. Track A (school data cleanup) is
complete — `schools_master.json` has 340 researched schools (337 original +
3 LAHE Lutheran high schools added during round-1 reconciliation).
Track B round 1 is complete on branch `track-b/integration` (PR #4): 7
archive surfaces surveyed, `yearbook_registry_master.json` now has ~1,235
rows covering `slcl_digital`, `slcl_physical`, `shsmo`/`whmc_umsl`,
`scchs`, `archstl_archives`, `concordia_hist`,
`north_county_municipal_libs`.

Your job is **not** to do the research yourself. Spin up **one child Devin
session per surface below, running in parallel**, using Agent Fan-Out.

**Fork point:** if PR #4 (`track-b/integration` → `main`) is already merged,
children branch from `main`. If it is still open, children branch from
`track-b/integration` so they inherit the round-1 registry and the 340-row
schools master (including the new ALL-651/652/653 rows). Merge round-2
output into a new `track-b2/integration` branch.

## Step 1: Read the contract

Read these files first, in full:
- `schema.md` — the data schema and rules every child MUST follow
  (web-search-only, no fabrication, cite-or-mark-unverified,
  `reca_scope_status`, `entity_type`, `source_archive_id` tagging).
- `schools_master.json` — the full school list. Every child filters to its
  relevant subset and skips `reca_scope_status:
  out_of_scope_closed_before_1949` and `entity_type:
  administrative_district_only` rows.
- `data/digital_archives.json` — archive inventory: `policy` block
  (free+institutional-provenance rule, authority tiers, **the
  archive-surface note: every archive is a search surface for the FULL
  school list — never assume coverage is limited to the institution's own
  name**), per-archive `coverage_status`/`covered_schools` hints.
- `yearbook_registry_master.json` — for any `(school_id, year)` already
  `digitized` at a tier-1/2 archive, do not spend search effort re-finding
  it (incidental duplicate notes are fine but optional). `physical_only` /
  `not_found` rows should still be actively (re-)checked.
- `track_b_notes_*.md` from round 1 — skim the ones adjacent to your
  surface for known decoys/dead ends already documented.

## Step 2: The surfaces (one child each)

### Child 1 — Internet Archive (`archive_org`)
- URL: `https://archive.org/details/yearbooks` — enumerate via the
  advancedsearch API (e.g. `collection:(yearbooks OR yearbook-archive)` +
  St. Louis / Missouri / county-name queries; the Classmates mirror
  identifiers encode school+year, e.g.
  `classmates-yearbook-30903-1983-st-louis-university-high-school`).
- Relevant schools: all in-scope rows. Prior inventory hints 11 matched
  schools (`63147-08, 63147-10, ALL-064, ALL-115, ALL-287, ALL-328,
  ALL-334, ALL-441, ALL-546, ALL-651, ALL-652`) — verify, don't trust.
- **Per-item provenance is required:** check each item's
  contributor/collection metadata. Institution-contributed =
  provenance institutional (tier 2 behavior); Classmates-mirror or
  unknown-contributor = aggregator (tier 3 — still record
  `digitized_status: digitized` tagged `source_archive_id: archive_org`;
  `flatten_registry.py` applies `rescan_recommended` automatically where
  no tier-1/2 copy exists elsewhere). Note provenance in
  `existence_reasoning` or `notes`.

### Child 2 — Missouri History Museum (`mohistory`)
- URLs: `https://mohistory.org/collections/library` and the Genealogy &
  Local History Index at `genealogy.mohistory.org`.
- Physical-only surface. Only `spot_checked` so far (hints: ALL-328
  Normandy HS, ALL-376 University City HS, ALL-546 WashU). MoHM holds STL
  school records **including SLPS records transferred when the district
  archives closed in 2016** — this is the likeliest physical home for city
  school material. Enumerate the Schools Files / genealogy index first,
  then per-school search vs all in-scope schools.

### Child 3 — St. Louis Mercantile Library at UMSL (`mercantile_umsl`)
- URL: `https://www.umsl.edu/mercantile/`
- `unsearched`, but the M-423 SLPS collection is confirmed to hold
  district material — yearbooks unverified. Enumerate the catalog /
  finding aids vs all in-scope schools, emphasis on SLPS city schools.
  Do NOT search UMSL's own yearbook collection here (that's Child 8) or
  WHMC/SHSMO (already covered in round 1) — Mercantile is a distinct
  collection on the same campus.

### Child 4 — St. Charles City-County Library (`stcharles_lib`)
- URL: `https://www.stchlibrary.org/learn-discover/genealogy`
- `unsearched`. No digital yearbook collection found previously; re-check
  the **physical** catalog for St. Charles-area schools. Relevant subset:
  the ~40 St. Charles County rows (Francis Howell, Wentzville, Fort
  Zumwalt + predecessors, St. Charles city, Defiance, New Melle etc.) —
  SCCHS (round 1) found only ALL-647, so gaps here are real open
  questions, not confirmation.

### Child 5 — School/district self-hosted (`school_self_hosted`)
- **Authority tier 1** — the strongest provenance there is. Bounded
  surface: each in-scope school's own DISTRICT website (a Florissant
  school's materials live on the Ferguson-Florissant district site, not a
  municipal site), plus alumni associations and school-linked historical
  societies. Orientation finding: "district sites host purchase pages,
  not archives — expect low yield" — but no systematic sweep has ever
  been done.
- This is the largest surface. The coordinator may split it into 2–3
  parallel sub-children by district cluster (e.g. SLPS/city, north St.
  Louis County districts, St. Charles County + south county districts) —
  all sub-children tag `source_archive_id: school_self_hosted`.
- Known lead: `ALL-377` Normandy Area Historical Association is a
  school-linked archive org in the seed list itself (their records are
  what SHSMO collection S0420 holds — see whether the association itself
  also hosts anything).
- For any district-hosted scan found, `digitized_status: digitized` with
  tier-1 provenance fully suppresses the scan target at rollup — highest
  value hits in this round.

### Children 6–9 — University archives (FULL-index survey, one child each)

**Critical scoping correction:** these are search surfaces for the ENTIRE
school list, not just the university's own yearbook. Each child must
enumerate the archive's full collections index (CONTENTdm collections,
ArchivesSpace PUI, DigitalMobius/Digital Commons collection list —
whatever the platform exposes) and diff it against all in-scope
`schools_master.json` rows — university archives can hold other schools'
yearbooks via donated/deposited collections. The university's own
yearbook series produces registry rows because the university IS itself
a target school (ids below), but do not stop there.

- **Child 6 — SLU (`slu`)**: `http://digitalcollections.slu.edu/digital/collection/historicpub`
  — CONTENTdm (cdm17321). Own series "The Archive" 1913–2005 covers
  ALL-544 (Saint Louis University). Probe the full collections index for
  yearbook/school collections beyond SLU's own — Jesuit institutions
  collected other schools' publications.
- **Child 7 — WashU (`wustl`)**: `aspace.library.washu.edu` (ArchivesSpace)
  + `digitalcommons.wustl.edu`. Own series "The Hatchet" covers ALL-546
  (Washington University) — digital run ends 1928 (mostly pre-RECA;
  physical complete set at Olin/Becker — record what the catalog asserts
  for the RECA-era years too). The real job is the full index diff for
  other schools.
- **Child 8 — UMSL (`umsl`)**: `https://irl.umsl.edu/yearbook/` — own
  series covers 63147-12. Enumerate the IRL@UMSL collections index for
  other schools' materials. NOTE: `whmc_umsl` is covered by round-1
  `shsmo` (same catalog — dedupe, do not redo) and `mercantile_umsl` is
  Child 3 — this child covers UMSL's own archives/IRL only.
- **Child 9 — STLCC (`stlcc`)**: `https://stlcc.digitalmobius.org/` —
  DigitalMobius. Per-campus subcollections cover ALL-443/444/445
  (Florissant Valley cluster: 8 vols 1967–1977), plus Meramec and Forest
  Park series — check whether Meramec/Forest Park map to any other seed
  rows before writing them off. Enumerate the full collection index.
- **Optional Child 10 — Lindenwood (`lindenwood`)**:
  `https://digitalcommons.lindenwood.edu/yearbooks/` — own series covers
  ALL-547 (multi-decade run + Belleville IL campus 2010–2014). Same
  full-index-diff rule applies (Digital Commons collections index). Skip
  this child only if the coordinator judges the single covered school not
  worth a session.

## Step 3: The enumeration-first method (applies to every child)

1. **Try to find a full listing first** — collection index, finding-aid
   list, "browse all," API, or sitemap — before per-school keyword search.
2. **If a full listing exists:** pull it once, in full. Save the raw
   listing to `data/archive_indexes/<surface_id>.json` (names/titles/
   identifiers + source URL + date). Then diff locally against your
   school subset (use the core-token/geography matching approach in
   `find_potential_duplicates.py` as the reference for disambiguation —
   do not silently fuzzy-merge a decoy).
3. **If no full listing exists:** only then fall back to targeted
   per-school searches, and only for schools enumeration didn't resolve.
4. **Be polite, not a bulk scraper:** respect `robots.txt`, human-paced
   requests, prefer official APIs over form submissions, never log in or
   submit contact/request forms (web browsing only per `schema.md`), stop
   and note it if blocked/rate-limited.

## Step 4: Output

Each child produces, on branch `track-b2/<surface_id>`:
- `data/archive_indexes/<surface_id>.json` — raw enumerated listing, if
  one was found.
- `yearbook_registry_<surface_id>.json` — `schema.md` Table 2 rows for
  every `(school_id, year)` actually investigated (`year: "all"` for an
  exhaustive not-found sweep). **Set `source_archive_id` on every row** —
  reconciliation is the coordinator's job, not yours; record what you
  found accurately.
- `track_b_notes_<surface_id>.md` — process notes: what was tried, dead
  ends, recommended `coverage_status`/`covered_schools` updates for this
  archive_id.
- Commit and report back. Do not merge to `main` yourself.

Use these `surface_id` values: `archive_org`, `mohistory`,
`mercantile_umsl`, `stcharles_lib`, `school_self_hosted`, `slu`, `wustl`,
`umsl`, `stlcc` (and `lindenwood` if Child 10 runs).

## Step 5: After children finish

- Wait until ALL children report.
- Merge all `track-b2/*` branches into `track-b2/integration`.
- Update `data/digital_archives.json` `coverage_status`/`covered_schools`
  for each surface from what was actually found.
- Run `python3 merge_registry.py` then `python3 flatten_registry.py`;
  check `citation_collisions.json` and resolve any collisions before the
  PR (same-citation-across-different-school_ids means a probable decoy
  match — except legitimate shared index URLs, which round 1 documented
  in its PR body).
- Produce a summary: rows per surface, newly `digitized`/`physical_only`
  schools, data-quality flags (especially any new dangling school_ids —
  round 1 hit one; if a child finds holdings for a school absent from
  `schools_master.json`, mint a `schools_lutheran_hs.json`-style
  additions file with cited rows rather than using a phantom id).
- Push and open a PR to `main`. Do not merge it — a human reviews.

## Guardrails (apply to you AND every child)

- **Web search/browsing only.** No calling, emailing, logging in, or
  contacting any person or institution. Human-outreach needs go in
  `notes` as recommended follow-ups.
- **Enumerate before you brute-force.**
- **Be a polite client.** `robots.txt`, pacing, stop-and-report if
  blocked.
- **No fabrication.** Real citations or `unknown`/`unverified`.
- **Do not modify `schema.md`, `pilot/`, `batches/`, or
  `schools_master.json`** (school additions go in a new
  `schools_<scope>.json` file per the Step 5 note — never edit the master
  directly). Only create new files under `data/archive_indexes/`, plus
  `yearbook_registry_<surface_id>.json`, `schools_<scope>.json` additions
  if needed, and notes files at the repo root, plus Step 5 merge outputs.
