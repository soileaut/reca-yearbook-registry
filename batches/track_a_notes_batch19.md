# Track A Notes — Batch 19 (ZIPs 63304 / 63341, St. Charles County + Washington, MO)

Date of research: 2026-10-08. Output: `batches/schools_batch19.json` — 15 rows, count
unchanged (no merges or splits). `reca_scope_status` intentionally absent per prompt;
`entity_type` set on every row.

## Confirmed vs. unknown

**Confirmed open dates (opened + still open, or opened + renamed):**
- `ALL-569` Castlio Elementary — 1981 (FHSD history timeline + school handbook).
- `ALL-571` Independence Elementary — March 18, 1999 (school handbook; district's
  ninth elementary). The 1885–1941 one-room "Independent School" it was named for is
  a predecessor in name only, documented in notes.
- `ALL-572` Westwood Trail Academy — 2019 (FHSD timeline).
- `ALL-573` Early Childhood Family Education Center (Central School Rd) — 1993
  (FHSD timeline, "Central School Road Early Childhood Center").
- `ALL-577` Immaculate Conception (Dardenne) — 1881, per the school's own site.
  Oldest school in the batch and still operating.
- `ALL-587` Daniel Boone Elementary — 1955 (school handbook, National Blue Ribbon
  nomination page, FHSD timeline all agree).
- `ALL-590` Washington High School — 1900 (Washington Historical Society timeline;
  Wikipedia corroborates). Current building dates to 1955-56.
- `ALL-580` St. Charles Community College — district established by voters April 1,
  1986; first classes June 1987 (the seed's "1987" is the classes year, not founding).
- `ALL-578` Francis Howell School District — legal entity organized May 8, 1915 as
  Consolidated School District No. 2; renamed "Francis Howell School District"
  March 15, 1966 (district's own history page).
- `ALL-579` Fort Zumwalt School District — formed as Central School District R-II,
  approved by voters July 19, 1949 (district's own archived history page).
- `ALL-585` Consolidated School District No. 2 — organized May 8, 1915; renamed 1966.
  Successor recorded as `ALL-578` (confirmed — it's a rename, same entity).
- `ALL-592` School District of Washington — incorporated as a public entity in 1889
  (district's own Comprehensive Annual Financial Report).

**Probable:**
- `ALL-575` Messiah Lutheran School — 2001 (privateschoolreview "Year Founded 2001"
  quoting the school's own copy; not independently confirmed).
- `ALL-576` St. Cletus School — ~1967 (parish founded 1965, first school building —
  grades 7-8 only, shared with St. Peter — done within two years per the parish's
  official guide book). The current K-8 school at 2705 Zumbehl Rd opened fall 1983
  (dedicated April 17, 1983). School claims "over six decades," consistent with 1967.

**Left unknown:**
- `ALL-591` Washington Middle School — opened_year unknown. Renovation projects are
  documented (2022 library addition, earlier additions) but no founding/building year
  is findable online. Recommend human follow-up with the School District of
  Washington or the Washington Historical Society.

## Administrative district disambiguation

Four rows are `administrative_district_only` — genuine multi-school districts, never
single buildings: `ALL-578` Francis Howell (23 campuses), `ALL-579` Fort Zumwalt
(25 schools), `ALL-592` School District of Washington (11 schools + career center),
and `ALL-585` Consolidated District No. 2 (historical predecessor, member schools at
the time included Francis Howell HS, Central Elementary, Daniel Boone, Becky-David).
Member schools are named in each row's `notes`. No `individual_school`-style
one-school districts or `ambiguous_unresolved` rows in this batch.

## Data-quality flags

- **`ALL-590` and `ALL-591` have shifted seed columns**: `Location Confidence`
  contains the Status value, `Status` contains the Yearbook Priority value,
  `Yearbook Priority` contains the notes text, and `Notes` is empty. Values were
  interpreted by position.
- **Seed date error `ALL-585`**: seed says Consolidated District No. 2 opened 1950;
  it was actually organized May 8, 1915 and renamed (not closed) in 1966. The 1950
  likely conflates the statewide ~1949 reorganization era.
- **ZIP mismatches (kept for community coverage)**: `ALL-576` St. Cletus is actually
  63301 (seed 63304); `ALL-577` ICD is 63368 (seed 63304); `ALL-580` SCC is 63376;
  `ALL-590`/`ALL-591` Washington schools are 63090.
- **Address quirk `ALL-587`**: Daniel Boone is "New Melle 63365" in the seed but
  "Wentzville 63385" on federal pages — same building, mailing-city discrepancy.
- **Unverifiable seed note `ALL-587`**: "second elementary for Reorganized District
  No. 3" could not be confirmed; documented lineage runs through Consolidated
  District No. 2. Possibly a distinct Defiance-area predecessor — follow-up item.
- **`ALL-577` possible stale NCES address**: NCES lists 2089 Hanley Rd but the
  parish campus is now at 7701 Town Square Ave, Dardenne Prairie; the school may
  have moved with it.

## Useful sources for reuse

- **fhsdschools.org/about** — the FHSD history timeline is a goldmine: exact
  organization/rename dates for the district plus opening year for every school it
  has ever opened. Single most valuable page for this batch.
- **School handbooks on fhsdschools.org** — each elementary's parent handbook has a
  "School History" section with exact opening dates and predecessor one-room schools.
- **washmohistorical.org/timeline** — Washington Historical Society timeline covers
  Washington, MO schools (first grammar school 1872, private HS 1887, public HS 1900).
- **District CAFR / archived district history pages** — School District of
  Washington's CAFR gave its 1889 incorporation date; Wayback Machine capture of
  fzschools.org gave Fort Zumwalt's 1949 formation vote.
- **Parish guide books / school About pages** (saintcletus.org, icdschool.org) —
  Catholic school founding dates are best found in parish-published histories, not
  NCES.
- **nationalblueribbonschools.ed.gov** — nomination narratives often include founding
  years and building history for award-winning schools.
- **privateschoolreview.com** — useful for private-school founding years but treat as
  `probable`; reflects the school's self-report or NCES record.

## Process friction

- **`opened_year` for current small/private programs is thinly documented** —
  Messiah Lutheran's 2001 rests on a single profile page; Washington Middle School's
  founding isn't on the public web at all.
- **District rename dates vs. legal formation dates diverge** (Fort Zumwalt renamed
  from Central R-II around its 1960 first high school; FHSD renamed in 1966). The
  schema's "opened/closed" model maps awkwardly onto renames — handled as
  rename = successor to itself with `confirmed` where the entity continues.
- **Mailing-city vs. actual location** recurs throughout St. Charles County
  (Weldon Spring/St. Charles/New Melle/Wentzville all interchangeable in addresses).
  ZIP fields were corrected to the physically accurate value with the discrepancy
  noted.
