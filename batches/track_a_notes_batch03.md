# Track A Notes — Batch 03 (ZIP 63033, Florissant)

Date of research: 2026-10-08. Output: `batches/schools_batch03.json` (15 rows,
ALL-033 through ALL-047 — count unchanged; no rows merged or split).

## Confirmed vs. unknown

**Fully confirmed (opened + closed-status with citations):**
- `ALL-042` Ackerman School (SSD) — opened 1961, SSD's first special-education
  school (ssdmo.org "Our Story"). Still open.
- `ALL-044` North Technical High School (SSD) — opened 1968, the year after
  South Tech (appliedtech.edu official history). Still open.
- `ALL-046` Our Lady of Fatima School — closed 2004 (privateschoolreview.com),
  one year before its parish dissolved in 2005. Probable successor: ALL-047.
- `ALL-047` St. Rose Philippine Duchesne School — closed 2018 when it joined the
  All Saints Academy partnership (St. Louis Review); successor ALL-048.

**Probable (real evidence, not exact):**
- `ALL-033` Cross Keys Middle — 1960s. FFSD acquired the site during the
  Wedgwood subdivision build (1963-67); alumni evidence from 1968-69 and a 1971
  junior-high yearbook ("The Padlock", grades 6-9).
- `ALL-034` Wedgwood 6th Grade Center — 1960s on the same land-acquisition
  evidence. Formerly Wedgwood Elementary (K-6).
- `ALL-046` Our Lady of Fatima — 1950s (parish founded 1950; church and school
  shared one building).
- `ALL-047` opened 1967 — seed's NCES-derived value, consistent with the site
  being St. Thomas the Apostle School on a 1960-founded parish site; not
  independently verified.
- `ALL-046` successor → ALL-047 — probable (institutional succession via the
  2005 merger; students actually dispersed before the parish closed).

**Left unknown (genuine search, nothing found):**
- `opened_year` for all seven remaining current schools: ALL-035 Commons Lane,
  ALL-036 Halls Ferry, ALL-037 Jury, ALL-038 Jamestown, ALL-039 Parker Road,
  ALL-040 Robinwood, ALL-041 Townsend, plus ALL-043 Northview High and ALL-045
  East ECC. No free web source publishes opening dates for post-1950 suburban
  elementaries; exact years likely live in district facilities records or the
  Franzwa (1977) / "Reflections of the Florissant Valley" (1990) local-history
  books, neither of which is digitized.
- Northview's original founding year (its building was demolished and replaced
  in 2015 — the rebuild is documented, the original is not).

## Data-quality flags

- **Seed error — ALL-045 East Early Childhood Center:** seed lists district as
  "Special School District/Ferguson-Florissant" but NCES (ID 291383003208) and
  Hazelwood's own school map list it as Hazelwood SD's "ECE East" at 12555
  Partridge Run. Corrected `district_operator` to Hazelwood School District.
- **Cross-batch duplicates of my successor rows:** ALL-047's successor All
  Saints Academy - St. Rose campus appears as ALL-048 (batch04, ZIP 63033) AND
  ALL-108 (batch05, ZIP 63034 "served ZIP") — same institution. I linked to
  ALL-048. Similarly ALL-046's building reuse is ALL-076 "Our Lady of Fatima
  School - Lindenwood campus" (batch05), already kept separate by design.
- **Name/format drift in FFSD schools:** after the district's ~2019-2021 grade
  reconfiguration, several seed names are stale — Commons Lane, Parker Road are
  now "Primary" (PreK-2) and Halls Ferry, Robinwood are now "Intermediate"
  (3-5). Recorded both names in `historical_names` and `notes`.
- **Spelling variant:** NCES uses "Wedgwood"; Wikipedia/FFSD materials use
  "Wedgewood" for ALL-034.
- **Possible deeper lineage not verified:** a rural "Cross Keys School" existed
  at New Halls Ferry Rd just north of Parker Rd (MoHistory genealogy index,
  "Reflections of the Florissant Valley") — a different site ~1 mi from the
  current Cross Keys Middle. Likely the predecessor rural school but unproven.
- **Hazelwood school names:** Jamestown, Jury, and Townsend are NOT among the
  13 schoolhouses that formed Hazelwood SD in 1949-51 (verified list from the
  district's 150th-anniversary Coldwater article) — they are post-consolidation
  buildings, though their names may continue older rural district names.
- **No administrative-district rows** in this batch; all 15 rows are
  `individual_school`.

## Useful sources for reuse

- **ssdmo.org/our-story + appliedtech.edu/our-history** — official SSD timeline:
  district 1957/58, Ackerman 1961, tech ed 1966, South Tech 1967, North Tech 1968.
- **flovalleynews.com (Florissant Valley news)** — school renovation/reopening
  stories, SSD construction news, and the canonical list of Hazelwood's 13
  original schoolhouses.
- **Official district directories as open-status proof** — FFSD annual building
  directory PDF (fergflor.k12.mo.us) and the City of Hazelwood's HSD school map
  (hazelwoodmo.org DocumentCenter/View/756), which enumerates every Hazelwood
  school with address.
- **stlouis.closedparishes.com** — archdiocesan closed-parish records (founding
  and closure years, merger details, property sales). Combined with
  **stlgs.org** parish tables for the same data.
- **STLPR's May 2005 consolidation article** — names exactly which buildings
  the merged parishes' schools would occupy.
- **St. Louis Review (stlouisreview.com)** — authoritative on All Saints
  Academy formation (2018) and the St. Rose campus closure (2023).
- **wedgwoodsubdivision.com** — HOA-written history dating school-site
  acquisition to the 1963-67 subdivision build; a decent way to bound
  1960s-era school openings by surrounding-development dates.
- **United States v. Hazelwood School District (1975)** — court stipulation
  documenting the district's formation from 13 rural districts 1949-51.

## Process friction for the scale-up decision

- **Opening dates for post-1950 suburban elementaries are essentially
  unpublished online.** County property records would give building years but
  are behind an interactive lookup; district facilities master plans and local
  history books (Franzwa 1977; Crank 1990) are not digitized. Expect most
  "current suburban elementary" rows to come out `unknown` unless a batch
  includes a district-published history.
- **District name drift breaks naive matching:** FFSD renamed half its
  elementaries (Primary/Intermediate split) and Hazelwood runs buildings under
  names different from the historic rural districts it absorbed. Search both
  current and former names.
- **Catholic schools are far better documented than public ones** — the
  archdiocese's merger/closure history is fully online; parish school lineage
  can be reconstructed almost completely from closedparishes.com + St. Louis
  Review + STLPR.
- **Recommended human follow-up:** Hazelwood SD or FFSD facilities offices (or
  the St. Louis County Library local-history collection, which holds the
  Franzwa and Florissant Valley books) could supply exact opening dates for
  the eight `unknown` elementaries. Not contacted per scope rules.
