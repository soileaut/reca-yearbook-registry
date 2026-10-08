# Track A Notes — Batch 02 (ZIP 63031/63033: Florissant / Hazelwood / Black Jack)

Date of research: 2026-10-08. Output: `batches/schools_batch02.json` (15 rows —
count unchanged; no merges or splits, but several rows are rename-lineage
siblings of each other as flagged below).

## The big picture that unlocked this batch

Nine of the 15 rows (ALL-023 through ALL-031) are one-room rural schoolhouses
of old St. Ferdinand Township that were consolidated to form the Hazelwood
School District in **1949-1951**. Once that context was found, all nine became
one story instead of nine separate mysteries:

- **United States v. Hazelwood School District, 392 F. Supp. 1276
  (E.D. Mo. 1975)** — the stipulated history states the district "was formed
  from thirteen rural school districts between 1949 and 1951 by process of
  annexation," maintained eight schools at formation, and initiated its first
  high-school grade in 1954-55. Stable, authoritative citation for the whole
  cluster.
- **Hazelwood district press release (flovalleynews.com, Oct. 2009)** — names
  all 13 schoolhouses: Brown, Coldwater, Vossenkemper, Pea Ridge, Columbia
  Bottom, Prigge, Twillman, Black Jack, Elm Grove, Hyatt, Rosary, Garrett,
  Bonfils. All nine batch-02 rural rows are on this list.
- **Gregory Franzwa, "History of the Hazelwood School District" (1977)** —
  the district's official published history; not itself online, but quoted at
  length by the Old Jamestown Association (Brown School chapter excerpts) and
  the Pipes Family Foundation (Prigge/Larimore chapter). Where I rely on it
  secondhand, confidence is `probable`.

## Confirmed vs. unknown

**Fully confirmed (opened + status/closed with citations):**
- ALL-020 Hazelwood HS - Original — completed 1954 at 1865 Dunn Rd (school's
  own history page). Ceased to be the district high school when the second
  building opened 1966; building never closed — it's now the Hazelwood
  Opportunity Center.
- ALL-021 Hazelwood HS - Second Building — opened 1966 at 15875 New Halls
  Ferry Rd (school's own page).
- ALL-022 Hazelwood Central HS — the same building/institution as ALL-021,
  renamed ~1974 when East and West opened (opened 1977). Still open.
- ALL-024 Cold Water School — closed spring 1954 per the St. Louis County
  landmarks page and the district's 2009 press release. 1859 brick building
  survives as a museum on the HSD Learning Center grounds.
- ALL-027 Elm Grove School — district established 1852, closed 1952, moved to
  Brookes Park as "The Little Red Schoolhouse" (City of Hazelwood marker,
  HMDB).
- ALL-032 McCluer North HS — founded 1971 (Wikipedia/Wikidata), still open
  (mnhs.fergflor.org).

**Probable:**
- ALL-018 Marygrove — Florissant campus established 1969 when the Sisters of
  the Good Shepherd moved from Gravois Ave; institution traces to the
  sisters' 1849 arrival in St. Louis. Now a Catholic Charities ministry;
  residential program shrank after ~2021 but the organization (and its
  on-campus special-ed school listing in NCES PSS through 2021-22) persists.
- ALL-023 Brown School — founded by a Dec. 9, 1859 land deed (Franzwa ch. 1
  via Old Jamestown Association); originally "James School," then "Douglas
  and James," finally Brown. Taken over by Hazelwood in 1950; building became
  a residence/parsonage and still stands.
- ALL-025 Prigge/Larimore — "Prigge is the predecessor name for the Larimore
  district," which voted to join Hazelwood July 29, 1951 (Franzwa ch. 6 via
  Pipes Family Foundation).
- ALL-026 Hyatt, ALL-028 Pea Ridge, ALL-029 Columbia Bottom, ALL-030
  Vossenkemper, ALL-031 Black Jack — `closed_year` 1951 is recorded as
  `probable`, meaning end of operation as an independent school/district at
  the close of the 1949-1951 annexation window. Exact per-school closure
  dates are not online; buildings may have operated under Hazelwood past
  that. Black Jack's 1928 building survives as City Hall (4655 Parker Rd).

**Left unknown:**
- `opened_year` for ALL-019 Oak Bridge (in NCES PSS by 2017-18; site © 2018 —
  a recent small school, founding date not published).
- `opened_year` for ALL-024, 025, 026, 028, 029, 030, 031 — all predate the
  surviving online record (these are 19th-century rural districts; e.g. Cold
  Water's school existed by the 1840s, but only its 1859 *building* is dated).
- All successor fields for rural rows — the modern namesake elementaries
  (Brown Elem, Cold Water Elem, Larimore Elem) are noted per-row but no
  source ties the specific schoolhouse's students to them.

## Data-quality flags

1. **ALL-021 and ALL-022 are the same school.** "Hazelwood High School -
   Second Building" never closed — it was renamed Hazelwood Central ~1974.
   Kept as separate rows per the no-silent-merge rule; treat as one lineage.
2. **Cross-batch duplicates everywhere.** The same schools appear under
   neighboring ZIPs: Hazelwood HS/Central (ALL-062, 063, 084-086, 124-126,
   258-260, 458-460, 530-531); the rural schoolhouses (ALL-068-074, 096-103,
   249-254); McCluer North (ALL-112, 413, 518). `find_potential_duplicates`
   should have caught these — coordinator should merge at aggregation.
   Notably ALL-460 "Hazelwood Central High School - Dunn Road Campus" is
   **mislabeled** — Dunn Road is the *original* campus (today Hazelwood
   Opportunity Center, ALL-476); Central was never on Dunn Road.
3. **Seed ZIP errors:** ALL-020 (1865 Dunn Rd is 63138 Spanish Lake, not
   63031); ALL-027 (450 Brookes Dr, Hazelwood is 63042 — and it's the
   *relocated museum* site, not the school's historic location); ALL-031
   (Black Jack = 63033).
4. **ALL-025 name conflation:** "Prigge School/Larimore School" is one school
   renamed, not two — the seed's slash-joined name accidentally got it right.
5. **No `administrative_district_only` rows in this batch.** No seed row
   uses district-style naming; every row resolved to a single physical
   school → `individual_school`.
6. **Marygrove caveat:** the "school" is an on-campus special-ed program of a
   residential treatment center — unlikely to have produced traditional
   yearbooks; also verify its current operating status (residential program
   contracted after 2021).

## Useful sources for reuse

- **chs.hazelwoodschools.org/about-us/about-us** — Hazelwood Central's own
  history page resolves the whole 1954→1966→1974→1977 high-school sequence.
- **flovalleynews.com** — ran the district's 2009 Old Coldwater press release
  naming all 13 consolidation schoolhouses; also carried Florissant-area
  historic-preservation news.
- **oldjamestownassociation.org** — Franzwa chapter excerpts (Brown School).
- **pipes.family** (Pipes Family Foundation, 2025) — Franzwa ch. 6-7
  excerpts on Prigge/Larimore/Twillman districts.
- **St. Louis County landmarks pages** (de.stlouiscountymo.gov +
  ig.stlouiscountymo.gov inventory) — Coldwater 1954 closure, Black Jack
  1928 school → City Hall, Hyatt House.
- **hmdb.org** — Elm Grove/Little Red Schoolhouse marker (1852, closed 1952).
- **Esley Hamilton surveys** (stlouisarchitecture.org Spring 2013 "Surviving
  Rural Schools"; 1989 county inventory Phase II: Black Jack at
  mostateparks.com) — county rural-school numbers and building fates.
- **392 F. Supp. 1276 via Justia** — district formation window + enrollment.
- **theclio.com entry 149142** — Good Shepherd → Marygrove relocation, 1969.
- **ProPublica private-school-demographics** — NCES PSS history for tiny
  private schools (Oak Bridge, Marygrove Services) when no other record exists.

## Process friction

- **Franzwa's 1977 district history is the linchpin source and is not
  online.** Per-school annexation dates for Hyatt, Pea Ridge, Columbia
  Bottom, Vossenkemper, and Black Jack almost certainly live in it (it has
  per-district chapters). A library copy scan or HSD archivist request would
  resolve all five at once — recommended human follow-up (St. Louis County
  Library or the HSD Foundation's Art & History Park museum project).
- **hazelwoodschools.org "History of the District" page renders empty** to a
  text fetch (JS-driven); its content may hold the same history.
- **The mostateparks.com Black Jack inventory PDF now 404s** under its old
  encoded URL — the Google-indexed text is still retrievable but the file
  itself may need relocation for future batches.
- One-room schools moved between districts/buildings under one name —
  building dates vs. school-entity dates diverge (Cold Water: entity by
  1840s, building 1859; Elm Grove: district 1852, building rebuilt 1961/66).
  I recorded entity dates in the fields and building dates in `notes`.
