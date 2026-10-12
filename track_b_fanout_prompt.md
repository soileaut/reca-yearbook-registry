# Track B Fan-Out — Seven Named Archive Surfaces

## Context

You are the coordinator session for a research project supporting a
yearbook digitization effort for RECA (Radiation Exposure Compensation Act)
claimants in the St. Louis, Missouri area. Track A (school data cleanup) is
complete — `schools_master.json` (repo root) has 337 researched schools.
Track B (archive holdings survey) has only been piloted against St. Louis
County Library so far (see `pilot/track_b_notes.md`,
`pilot/yearbook_registry_slcl_63147.json`).

Your job is **not** to do the research yourself. Spin up **one child Devin
session per surface below, running in parallel**, using Agent Fan-Out.

## Step 1: Read the contract

Read these files first, in full:
- `schema.md` — the data schema and rules every child MUST follow
  (web-search-only, no fabrication, cite-or-mark-unverified,
  `reca_scope_status`, `entity_type`).
- `schools_master.json` — the full researched school list. Every child
  filters this down to its own relevant subset (see per-surface scoping
  below) and skips any row with `reca_scope_status:
  out_of_scope_closed_before_1949` or `entity_type:
  administrative_district_only`.
- `data/digital_archives.json` — existing archive inventory, including a
  `policy` block (free+institutional-provenance rule, authority tiers) and
  per-archive `coverage_status`/`covered_schools` for context. Six of the
  seven surfaces below already have entries in this file (`archstl_archives`,
  `concordia_hist`, `shsmo`/`whmc_umsl`, `scchs`, `slcl_digital`,
  `slcl_physical`) — note their recorded `coverage_status` is NOT reflected
  in `yearbook_registry_master.json` yet (verify independently, don't trust
  it blindly). North county municipal libraries does not yet have a
  resolved entry.
- `pilot/track_b_notes.md` and `pilot/yearbook_registry_slcl_63147.json` —
  the only SLCL work that's actually verified and merged so far (12 pilot
  schools). Read before starting Child 5/6 below so you don't repeat it.
- `yearbook_registry_master.json` (repo root) — for any `(school_id, year)`
  already marked `digitized_status: digitized` here, do not spend search
  effort re-finding it. `physical_only`/`not_found` rows should still be
  actively (re-)checked.

## Step 2: The seven surfaces (one child each)

### Child 1 — Archdiocese of St. Louis Archives
- URL: `https://archstl.capacity.com/article/929015/schools-and-seminaries`
- Relevant schools: rows in `schools_master.json` that are Catholic/parish
  elementary or high schools (check `school_type`/`district_operator` for
  "Catholic," "Archdiocese," parish names, or religious order names). Roughly
  ~30 rows.

### Child 2 — Concordia Historical Institute (LCMS Archives)
- URL: `https://concordiahistoricalinstitute.libraryhost.com/`
- Relevant schools: rows affiliated with the Lutheran Church–Missouri Synod
  (district_operator/name containing "Lutheran," "Concordia," "LCMS," or a
  named Lutheran congregation). Roughly ~8 rows. Already confirmed: Lutheran
  High School North / "The Crusader" (`archival_objects/62755`) — do not
  re-research this one, just pull the full per-year volume list for it into
  the registry.

### Child 3 — State Historical Society of Missouri / St. Louis Research Center
- URL: `https://collections.shsmo.org/` (this is also the current home of the
  Western Historical Manuscript Collection–St. Louis, i.e. `whmc_umsl` in
  `data/digital_archives.json` — same catalog, treat as one search, don't
  duplicate effort across both archive_ids).
- Relevant schools: all rows not yet `out_of_scope`/`administrative_district_only`
  (this archive collects broadly — St. Louis-area organizational and school
  records generally, not one denomination/sector). Already spot-checked:
  Webster Groves HS (S1203), Hosmer Hall "Ivy" 1909 (S1082) — don't
  re-research these, just confirm/extend.

### Child 4 — St. Charles County Historical Society (PastPerfect)
- URL: `https://scchs.pastperfectonline.com/`
- Relevant schools: rows in St. Charles County ZIPs/district_operators
  (Francis Howell, Wentzville, Fort Zumwalt and their historical
  predecessors, St. Charles city schools, Defiance, New Melle, etc.).
  Roughly ~40 rows.

### Child 5 — St. Louis County Library Digital Archives (full scale-up)
- URL: `https://slcl.recollectcms.com/pages/yearbooks`
- This institution was already piloted on 12 schools (ZIP 63147) — see
  `pilot/track_b_notes.md` and `pilot/yearbook_registry_slcl_63147.json`
  for what good output looks like and how the collection is structured
  (Recollect CMS, St. Louis Yearbooks collection node 1267, ~90
  school-level subcollections, ~1,400 items, browsable via
  `https://slcl.recollectcms.com/nodes/search?bid=1267&orderby=node_title&order=asc`).
  **Read these pilot files first and do not re-research the 12 pilot
  schools** (`yearbook_registry_master.json` already has their rows,
  `verified_by: pilot-track-b-slcl`).
- Your job: enumerate the full ~90-subcollection index (if not already
  captured from the pilot, re-pull it — don't trust undocumented claims
  elsewhere in this repo about this being already done at full scale; it
  has not been merged into `yearbook_registry_master.json`), diff against
  **all** of `schools_master.json` (not just ZIP 63147), and extract
  per-year volumes for every newly-matched school the pilot didn't cover.

### Child 6 — St. Louis County Library physical holdings list
- URL: `https://www.slcl.org/yearbooks-and-alumni-publications` (the live
  page may block bots with a 403 — use a Wayback Machine snapshot if so,
  e.g. via `web.archive.org/web/*/https://www.slcl.org/yearbooks-and-alumni-publications`).
- This is a flat alphabetical table of ~1,149 physical holdings (list
  dated ~Aug 2015), separate from the digital collection in Child 5 — a
  school can appear in one, both, or neither. Pull the full table once,
  diff against all of `schools_master.json`.
- Also already partially piloted for the 12 ZIP 63147 schools — don't
  duplicate rows already in `yearbook_registry_master.json` from the
  pilot, just extend to the rest.

### Child 7 — North St. Louis County municipal libraries
- No single URL — this one starts with an **orientation question, not a
  search**: most St. Louis County municipalities are served by the
  county-wide St. Louis County Library (SLCL) system, already
  index-enumerated (`slcl_digital`/`slcl_physical` in
  `data/digital_archives.json`) — not every incorporated city runs its own
  library.
  - First, determine which of these north county municipalities/areas
    actually operate an **independent library system separate from SLCL**
    (the way Kirkwood, Maplewood, Richmond Heights, University City, and
    Webster Groves do in other parts of the county): Ferguson, Florissant,
    Berkeley, Jennings, Normandy, Bellefontaine Neighbors, Black Jack,
    Spanish Lake, Kinloch, Wellston, Pine Lawn, Moline Acres, Riverview.
  - `data/digital_archives.json`'s `municipal_libs_unverified` entry
    already has partial findings (Ferguson/University City/Brentwood
    notes) — read it first so you don't repeat that work.
  - If a municipality has no independent library (served by SLCL), note
    that and move on — do NOT brute-force search SLCL's catalog again
    under a different name, it's already covered.
  - Only for any municipality that DOES have its own independent library,
    apply the enumerate-first method (Step 3 below) to that library's
    catalog/collection.
  - If, after this orientation pass, zero independent north-county
    libraries are found, that is a complete and useful result — write it
    up as such in your notes file, you do not need to force a positive
    finding.

## Step 3: The enumeration-first method (applies to every child)

For your assigned surface, in this order:

1. **Try to find a full listing first.** Look for a collection index,
   finding-aid list, "browse by school/collection" page, sitemap, or any
   other mechanism that lets you see ALL of an institution's holdings (or
   all of its school-related holdings) in one or a few page loads —
   without a plain per-school keyword search.
2. **If a full listing exists:** pull it once, in full. Save the raw
   listing to `data/archive_indexes/<surface_id>.json` (array of whatever
   names/titles/identifiers you found, plus the source URL and date) so
   this enumeration never has to be repeated. Then diff it locally against
   your relevant school subset from `schools_master.json` (use the
   core-token/geography matching approach in
   `find_potential_duplicates.py` as a reference for how this project
   disambiguates similar names — do not silently fuzzy-merge a decoy).
3. **If no full listing exists (or the index only covers *some* relevant
   schools, e.g. a partial browse page):** only then fall back to
   targeted per-school keyword searches, and only for the schools that
   enumeration didn't already resolve.
4. **Be polite, not a bulk scraper:**
   - Respect `robots.txt`.
   - Use normal human-paced browsing/search — no rapid-fire automated
     hammering of search endpoints. If an official API exists (e.g.
     ArchivesSpace/PastPerfect sometimes expose one), prefer it over
     repeated HTML form submissions.
   - Never create an account, log in, or submit a request/contact form.
     Web search/browsing only — no contacting the institution, per
     `schema.md`.
   - If a site actively blocks/rate-limits you, stop and note it rather
     than retrying aggressively.

## Step 4: Output

Each child produces, in its own working branch:
- `data/archive_indexes/<surface_id>.json` — the raw enumerated listing,
  if one was found (omit if the surface had no enumerable index at all).
- `yearbook_registry_<surface_id>.json` — rows matching `schema.md` Table 2
  for every `(school_id, year)` actually investigated (found, confirmed
  absent, or exhaustively searched with nothing found — use `year: "all"`
  per the schema for that last case). **Set `source_archive_id` to your
  surface_id on every row** — this is how the coordinator reconciles
  overlapping findings across surfaces after everyone reports back (see
  schema.md's "Cross-institution reconciliation" section). You do not need
  to decide whether your find is "good enough" relative to what another
  surface might hold — that's not visible to you and is not your call;
  just record what you found accurately and tag it with your
  `source_archive_id`.
- `track_b_notes_<surface_id>.md` — process notes: what was tried, dead
  ends, anything that should update `data/digital_archives.json`'s
  `coverage_status`/`covered_schools` for this archive_id.
- Commit to a new branch (`track-b/<surface_id>`) and report back. Do not
  merge to `main` yourself.

Use these `surface_id` values: `archstl_archives`, `concordia_hist`,
`shsmo`, `scchs`, `slcl_digital`, `slcl_physical`,
`north_county_municipal_libs`.

## Step 5: After children finish

- Do not do this until ALL child sessions report completion.
- Merge all branches into a single integration branch.
- Update `data/digital_archives.json`: for each of the seven archive_ids,
  update `coverage_status` and `covered_schools` to reflect what was
  actually found (e.g. `spot_checked` → `index_enumerated` if a full
  listing was pulled).
- Run `python3 merge_registry.py` to regenerate
  `yearbook_registry_master.json` across everything.
- Run `python3 flatten_registry.py` to produce
  `flat_yearbook_registry.csv` — one row per `(school_id, year)` with
  `digital_location` / `physical_location` columns (pivoted from the
  normalized per-institution rows) plus a rolled-up `scan_status` verdict
  computed across all institutions for that row. This is the primary
  review artifact going forward. It also writes `citation_collisions.json`
  if two children cited the same source URL for different `school_id`s —
  **check this file and resolve any collisions before opening the PR**,
  since it means one child likely matched a decoy.
- Produce a short summary: how many (school, year) rows each surface
  contributed, any schools now `digitized`/`physical_only` that weren't
  before, and any notable data-quality flags.
- Push the integration branch and open a PR to `main`. Do not merge it
  yourself — a human will review.

## Guardrails (apply to you AND every child you spin up)

- **Web search/browsing only.** No calling, emailing, logging in, or
  otherwise contacting any person or institution.
- **Enumerate before you brute-force.** Spending effort re-deriving a full
  index by keyword-searching one school at a time, when a browsable list
  already exists, wastes time and risks missing schools you didn't think
  to search for.
- **Be a polite client.** Respect `robots.txt` and reasonable request
  pacing; stop and report rather than retry aggressively if blocked.
- **No fabrication.** Cite real sources or mark fields
  `unknown`/`unverified`.
- **Do not modify `schema.md`, `pilot/`, `batches/`, or
  `schools_master.json`.** Only create new files under `data/`
  (archive_indexes), plus `yearbook_registry_<surface_id>.json` and notes
  files at the repo root, plus the merge outputs in Step 5.
