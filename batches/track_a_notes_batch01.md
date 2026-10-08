# Track A Notes — Batch 01 (ZIP 63031, Florissant)

Date of research: 2026-10-08. Output: `batches/schools_batch01.json` (15 rows — count
unchanged; no rows merged or split). Seed file: `batches/schools_seed_batch01.json`.
All rows are `entity_type: individual_school` — no administrative-district rows in
this batch. `reca_scope_status` left absent per schema instructions (computed later).

## Confirmed vs. unknown

**Fully confirmed (opened + closed/open status with citations):**
- `ALL-005/006/007/008` Sacred Heart Catholic School + its three building rows —
  parish/school history pages give the complete lineage: first school Sept. 1866
  (Jefferson & St. Louis); replacement dedicated Nov. 28, 1889 (St. Denis &
  Jefferson); current building cornerstone Mar. 23, 1952 (501 St. Louis St). Still
  open. See nuance below on the 1889 building.
- `ALL-009` St. Ferdinand School — seed's "Unknown" resolved: parochial school
  opened Sept. 5, 1887 (Garraghan 1923 via Jesuit Archives + Florissant Valley
  Quarterly July 2024); moved to Charbonier Rd campus 1955; merged into All Saints
  Academy in 2018 → successor `ALL-014` (confirmed, St. Louis Review).
- `ALL-011` St. Sabina School — opened 1961, closed 2010, both verbatim on the
  St. Ferdinand parish history page (St. Sabina parish merged into St. Ferdinand
  in 2023). See successor nuance below.
- `ALL-012` St. Norbert School — opened Sept. 1988 (K-3), first class graduated
  1995, parish history page; merged into All Saints Academy 2018 → `ALL-013`.
- `ALL-013/014` All Saints Academy campuses — partnership announced Jan. 25, 2018,
  operating from 2018-19 (St. Louis Review). Both campuses still open; the third
  founding campus (St. Rose Philippine Duchesne) closed after 2022-23.
- `ALL-015` North County Christian School — seed's "1994" is WRONG: founded 1962
  as North County Day School at Ferguson Church of the Nazarene; at 845 Dunn Rd
  since 2004-05. Still open.
- `ALL-017` Grace Christian Academy — opened Aug. 31, 1981 as Grace Christian
  School (school's own history page); at 2890 Patterson Rd only since 2018; now
  branded "Foundation Christian Academy." Still open (NCES PSS 2023-24).

**Probable (real but weaker evidence):**
- `ALL-001` Combs Intermediate — 1876 St. Ferdinand Public School at the Combs
  site: confirmed that the school existed at Washington between St. Jacques &
  St. Jean (MoHistory index); the 1876 build year rests on the seed plus an
  AI-aggregated district history, so `probable`. Still open.
- `ALL-004` DeSmet School — kept 1953 `probable` on seed + aggregated district
  history, but NOT independently verified (see flags).
- `ALL-007` Sacred Heart 1889 building — closed 1952 `probable` because the
  building still houses PreK/K today (it ceased being the *main* school in 1952).
- `ALL-016` Atonement Lutheran — opened 1956 `probable` (privateschoolreview
  profile; church founded 1951). Still open.

**Left unknown:**
- `ALL-003` Cross Keys School — verified real (MoHistory index locates it on New
  Halls Ferry Rd just north of Parker Rd; FVHS Quarterly Oct. 2022 shows an 8th
  grade class there in 1942), but no source for open or close dates. Seed's
  "before 1951"/"1950s?" are unverifiable; 1952 R-II consolidation is plausible
  context only. Successor unknown — modern Cross Keys Middle School (14205 Cougar
  Dr, 63033) shares the name but continuity is unproven.
- `ALL-004` closed_year/successor — see flags.
- Minor: founding detail behind the "Combs" name; Sacred Heart's 1872 second
  classroom building (folded into ALL-005 notes, no separate seed row).

## Data-quality flags (for the coordinator)

1. **`ALL-004` DeSmet School — partially unverified / possible phantom-or-rename.**
   No "DeSmet" school appears on current FFSD rosters, Wikipedia's former-schools
   list, or the MoHistory index of historic Florissant schools. The only web
   attestations are the seed itself and an AI-generated district-history page.
   Likely a real FFSD school that was renamed or closed, but it needs an
   archival/district-records check before Track B. Do NOT confuse with De Smet
   Jesuit HS (Creve Coeur, est. 1967, unrelated).
2. **`ALL-015` seed opened-year wrong:** 1994 → actually 1962.
3. **`ALL-016` seed operator wrong:** listed as LCMS; the school is ELCA
   (Lutheran Church of the Atonement).
4. **`ALL-011` successor nuance:** after the parish school closed in 2010, the
   same site hosted "The Academy at St. Sabina," an archdiocesan *special-education*
   school (~30 students), itself closed ~2019-20. Not a general-ed successor —
   recorded `successor: unknown`; noted so nobody assumes continuity.
5. **`ALL-007` not fully closed:** the 1889 Sacred Heart building still hosts
   PreK/K classes; "1952" means it stopped being the main school.
6. **Address discrepancy:** St. Norbert school/parish address is 16455 New Halls
   Ferry Rd (seed correct); All Saints Academy site prints 16475 — likely a typo.
7. **`ALL-017` location caveat:** the school lineage only arrived at 2890
   Patterson Rd in 2018; earlier years operated in Pattonville/Overland under
   the Grace Christian School name.
8. **`ALL-003` ZIP caution:** the historic Cross Keys site (New Halls Ferry just
   north of Parker) sits in today's 63033 area, not 63031 — seed already marked
   its location confidence "Borderline."

## Useful sources for reuse

- **sacredheartflorissant.org/history** and **shcs-flo.org/history** — complete
  parish school building lineage with exact dates (1866/1889/1952).
- **stferdinandstl.org/history** — covers St. Ferdinand school (Charbonier move
  1955), St. Sabina school (1961-2010), parish mergers (2023). Best single page
  for the French-parish side.
- **saintnorbert.com/history.html + school-history.html** — full parish/school
  chronology.
- **fcastl.org/about** — the 1981→present Grace Christian/Foundation Christian
  itinerary incl. all prior campuses.
- **florissantvalleyhs.com/newsletters/*.pdf** — FVHS Quarterly archive back to
  2017; the July 2024 issue documents St. Ferdinand's 1887 school opening and the
  Sisters of Loretto/public-school story; the Oct. 2022 issue verifies Cross Keys
  School operating in 1942. High-value local source; worth grepping per batch.
- **jesuitarchives.org** (Garraghan's parochial-ministry history) — scholarly
  source for 19th-c. parish school dates.
- **genealogy.mohistory.org** index of "Reflections of the Florissant Valley"
  (Crank, 1990) — lists historic rural schools with locations (Cross Keys,
  Coldwater, Elm Grove, Rosary, Twillman, Pea Ridge, Vossenkemper, St. Ferdinand
  Public). Useful existence+location check for one-room-school rows.
- **stlouisreview.com** — archdiocesan paper; merger/closure announcements are
  authoritative (All Saints 2018; campus closure 2023; canonical decrees).
- **NCES PSS** — private-school open status + enrollment (Grace Christian,
  Academy at St. Sabina).

## Process friction for the scale-up decision

- **Grokipedia is showing up in search results** and repeats seed/AI-generated
  claims (e.g., the DeSmet 1953 line). Treat it as a lead at most — never as the
  sole citation basis for `confirmed`.
- **Small closed public elementaries (Cross Keys, DeSmet) have almost no web
  footprint.** MoHistory's "Reflections of the Florissant Valley" index confirms
  existence/location but not dates. The 1950s-era township-district consolidation
  into R-II is probably where several of these disappeared; FVHS or FFSD board
  minutes would be the follow-up.
- **Parish-school "closed" dates mark merger, not cessation.** St. Ferdinand and
  St. Norbert "closed" in 2018 only as independent entities — instruction
  continued seamlessly as All Saints Academy campuses. For yearbook purposes the
  campus continuity matters more than the legal name change.
- **Seed data reused building years as school years** (e.g., Sacred Heart rows,
  North County Christian's unexplained 1994). Verify every seed year against a
  school-controlled source when one exists.
- **Private-school names drift:** NCES carries "Grace Christian Academy" while
  the school itself is "Foundation Christian Academy." Check address+phone to
  match identities rather than name strings.
