# Track A Notes — ZIP 63147 Pilot (Data Cleanup)

Date of research: 2026-10-08. Output: `schools_63147.json` (12 rows — count unchanged;
no rows merged or split, though 63147-06 should be reviewed for a future merge into
63147-01 and 63147-07 appears to be a phantom school).

## Confirmed vs. unknown

**Fully confirmed (opened + closed with citations):**
- `63147-02` Earl Nance Sr. Elementary — opened 2002 (SLPS structures table), still open.
- `63147-04` River Roads Lutheran — opened 1869 (St. Louis American), still open
  (NCES PSS 2023-24). Oldest school in the set.
- `63147-08` Beaumont High School — opened Jan/Feb 1926, final class May 14, 2014.
  Building persists as a CTE center, so no successor school.
- `63147-12` UMSL — dedicated Sept 15, 1963 (predecessor Normandy Residence Center,
  1960). Still open.
- `63147-03` Herzog Elementary — resolved seed's `Unknown`: Peter Herzog School,
  completed 1936 (City of St. Louis Wayman neighborhood history; MoHistory Museum
  P.W.A. Project No. 282 record corroborates). Still open.

**Probable (real evidence, some conflict or informality):**
- `63147-01` Baden Elementary — Ittner building at 8724 Halls Ferry Rd built 1907 /
  opened 1908. Closure year conflicts: 2009 (Preservation Research Office,
  Wikipedia/Wayman) vs. 2010 (publicschoolreview.com, which likely reflects the NCES
  record year — seed's 2010 probably came from the same source).
- `63147-05` Baden School District — formation date unfound; absorbed into St. Louis
  Public Schools when Baden was annexed to the city in 1876. Successor recorded as
  `63147-06` (its school continued under SLPS).
- `63147-06` Baden Public School — 1872 one-room schoolhouse → 1878 brick building →
  folded into the 1908 Halls Ferry building, i.e., the same lineage as 63147-01.
- `63147-10` Riverview Gardens High School — founded 1927 per a detailed
  alumni-written district history; the current Shepley Drive campus dates to Sept
  1957, which explains the seed's "1950s". Still open.
- `63147-11` STLCC Florissant Valley — district created 1962, classes 1963,
  permanent Pershall Rd campus opened ~1967 (earliest yearbook is 1967-68;
  May 1967 cornerstone documented). Seed's "1965" is the bond-issue year.

**Left unknown:**
- `63147-07` Baden High School — no evidence it ever existed; flagged as a likely
  phantom/search alias. Baden teens attended Yeatman (1904–1926), Beaumont
  (1926–2014), and Northwest (1964–1992).
- `63147-09` "North High School" — unresolved identity. No SLPS school by that exact
  name. Candidates: Northwest High School (opened Feb 1964, 5140 Riverview Blvd;
  later Northwest Academy of Law, closed 2022) or Yeatman High School
  (1904–1926). Needs clarification from whoever compiled the seed.
- `opened_year` for `63147-05` (district formation date not found online).

## Surprises / data-quality flags

- **Seed address error:** `63147-01` Baden Elementary is listed at "5814 Thekla
  Avenue" — that address is the Walnut Park School (opened 1909, closed 2003), per
  its National Register nomination. Baden Elementary's real historic home is 8724
  Halls Ferry Rd. publicschoolreview.com does list Baden Elementary at 5814 Thekla,
  so a late relocation into the vacated Walnut Park building is possible but
  unverified.
- **`63147-06` and `63147-01` are the same school lineage**, not two schools —
  kept as separate rows per the no-silent-merge rule.
- **`63147-07` "Baden High School" and `63147-09` "North High School"** both appear
  to be nonexistent/garbled entities. At scale, expect more phantom rows like this —
  worth adding a "verify the school ever existed" step early in each track.
- **Pre-1960 schools had several buildings under one name.** "Baden School" means
  three different buildings (1872, 1878, 1908). Building open-dates ≠ school
  open-dates; both were recorded in `notes` where they diverge.
- **`Length` and `#VALUE!` columns** in the seed are derived junk (length = years
  open); ignored.

## Useful sources for reuse

- **stlouis-mo.gov/archive/neighborhood-histories-norbury-wayman/** — Norbury
  Wayman's neighborhood histories have per-neighborhood "schools" pages with exact
  building years, architects, and closings. Single most useful source; covers the
  whole city.
- **SLPS "Table of Current SLPS Structures" PDF** (Proposition S, 2022) — year built
  for every current district building.
- **Landmarks Association archival page on SLPS closings** and
  **preservationresearch.com** — 2009-era closure lists.
- **NCES CCD/PSS lookups** — reliable current open/closed status for public and
  private schools.
- **Missouri History Museum ArchivesSpace** (SLPS Archives finding aid) — building
  records incl. PWA letting numbers.
- **builtstlouis.net** — good secondary source for Ittner/Milligan school buildings.
- **Wikipedia** — useful for Baden neighborhood + Beaumont, backed by the Wayman
  histories and NRHP docs; used only where a stronger citation wasn't available.
- **Publicschoolreview.com** — fast NCES-derived profiles, but its "Closed YYYY" can
  be a record-year, not a true closure year. Treat as a lead only.

## Process friction for the scale-up decision

- **No good online source for pre-1900 district/school dates.** The Baden district
  formation date (63147-05) isn't findable via web search; likely requires SLPS
  Board minutes at MoHistory or Mercantile Library. Recommend a human follow-up or
  a dedicated archive visit for the ~1870–1900 era.
- **publicschoolreview/NCES closure years are unreliable** — they reflect when a
  school stopped appearing in federal data (e.g., Baden "2010" vs. actual 2009
  board-approved closure). Expect ~1-year skew.
- **School renaming chains need manual disambiguation.** "North High School,"
  "Northwest," "Yeatman," and "Central" share territory and eras; automated
  matching will misfire.
- **Successors for closed schools are rarely documented.** Closure announcements
  name receiving schools inconsistently; most successor fields ended up
  `none`/`unknown` with reasoning in `notes`. This is probably the correct honest
  outcome rather than a process failure.
- **Recommended human follow-up:** SLPS Records Center / special collections desk
  could resolve Baden Elementary's exact closure year and successor-school
  assignment, and whether it ever occupied 5814 Thekla. Not contacted per scope
  rules.
