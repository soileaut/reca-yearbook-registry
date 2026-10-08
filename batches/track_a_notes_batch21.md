# Track A Notes — Batch 21 (St. Charles County: Wentzville R-IV + Fort Zumwalt R-II)

Date of research: 2026-10-08. Output: `batches/schools_batch21.json` — 15 rows,
count unchanged (no merges/splits). Batch covers ZIPs 63367/63368 (Lake St.
Louis, O'Fallon, Dardenne Prairie — St. Charles County exurbs, not the city).

## Confirmed vs. unknown

**Fully confirmed (12 rows, all `individual_school`, all still open):**
- ALL-611 Discovery Ridge Elementary — opened 2010 (school's own About page).
- ALL-612 Crossroads Elementary — 2002 (school About page).
- ALL-613 Lakeview Elementary — 2010 (Patch article on its first-ever school year).
- ALL-618 Fort Zumwalt West HS — 1998 (district history + Wikipedia).
- ALL-619 Fort Zumwalt West Middle — 2001 (district history: opened 2001-02).
- ALL-620 Fort Zumwalt North HS — 1960 as "Fort Zumwalt High School", renamed
  North in 1987 when South opened; building moved 1976.
- ALL-622 Fort Zumwalt South HS — 1987 (district history, 1987-88).
- ALL-623 Fort Zumwalt East HS — 2007 (opened Aug 20, 2007).
- ALL-624 Dardenne Elementary — 1987 (district history, 1987-88).
- ALL-625 Ostmann Elementary — 2002 (district history, 2002-03).
- ALL-626 Pheasant Point Elementary — 1998 (district history, 1998-99).
- ALL-627 Twin Chimneys Elementary — 1993 (district history, 1993-94).

Every single opening year in this batch came from ONE of two sources:
the Wentzville schools' own "About" pages (which literally print
"Year Opened: YYYY") and the archived Fort Zumwalt district history page —
which is a goldmine, covering every FZ building opening by school-year in
narrative form. Fastest batch possible for a reason: the sources were good.

**Left unknown (3 rows — all non-school entities, see below):**
- ALL-614 Lake St. Louis Rural Schools, ALL-615 Boone-Duden Area Schools,
  ALL-616 Wentzville School District — no single open/close year applies.
  Formation/consolidation dates for these entities are not reliably
  resolvable online; the rural rows' member schools can only be enumerated
  from county district maps (human follow-up recommended).

## Data-quality flags

- **3 rows are not schools at all** (`administrative_district_only`):
  - `ALL-614` "Lake St. Louis Rural Schools" — aggregate placeholder; member
    schools unenumerable online. Human follow-up needed for the roster.
  - `ALL-615` "Boone-Duden Area Schools" — aggregate; partial member list in
    row notes (Bacon #64, Calamus Springs #65, Hamburg).
  - `ALL-616` "Wentzville School District" — the district itself; full member
    list in row notes. Serves 63367 but is based in 63385.
- **Seed ZIP errors (community-level vs physical):**
  - `ALL-613` Lakeview Elementary is in **Wentzville 63385**, not 63367.
  - `ALL-618` West HS is 63366; `ALL-620` North HS is 63366; `ALL-622` South
    HS and `ALL-623` East HS are **63376 (St. Peters)** — all included only
    for attendance-area overlap with 63367/63368.
- **Address discrepancy**: `ALL-623` East HS seed address "6001 Highway 94"
  vs documented "600 1st Executive Ave" — same campus, wrong street in seed.
- **Fuzzy-match file misfires**: `data/schools_seed_deduped_review_needed.json`
  flags the four FZ high schools as possible matches of each other — they
  are four different physical schools, correctly kept separate.
- **`Length`/`#VALUE!` columns ignored** as before (derived junk).

## Useful sources for reuse

- **Wentzville school "About" pages** (`<abbr>.wentzville.k12.mo.us/about`)
  print `Year Opened: YYYY` verbatim — the single fastest possible citation.
  URL slug is the school's initials (dre, cre, lve, …).
- **Archived Fort Zumwalt district history**
  (`web.archive.org/.../fzschools.org/Html/fzsdhist.htm`) — narrates EVERY
  FZ building opening by school year, 1807 through 2003. One fetch resolved
  7 rows. Same pattern likely exists for other county districts.
- **School "About" pages generally** — districts on Finalsite-style CMS
  publish "Year Opened" in quick-facts; check the school's own site first.
- **Boone-Duden Historical Society / local history blogs** — the only
  source found that names individual rural one-room schools by district
  number. Human archival work needed for full rosters.

## Process friction

- **Collective/aggregate seed rows** ("X Rural Schools", "Y Area Schools")
  aren't covered cleanly by the schema's `entity_type` — they aren't
  administrative *districts*, they are sets of schools across several
  defunct districts. Used `administrative_district_only` as the closest fit
  (correct operational effect: skipped by Track B), but consider adding a
  `school_set_aggregate` enum value for these.
- **Rural one-room school rosters are not online.** For ZIPs built over
  rural territory, per-school enumeration needs county plat/district maps —
  outside web-search scope; flagged as human follow-up.
- **Community-ZIP seeds carry wrong physical ZIPs.** Several rows list ZIP
  63367/63368 while the actual campus sits in 63366/63376/63385. Kept the
  real ZIP in the row and flagged in notes — worth deciding whether `zip`
  should hold the seed's match-ZIP or the true campus ZIP going forward
  (I used the true campus ZIP).
