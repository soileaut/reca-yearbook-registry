# Track A Notes — Batch 13 (Berkeley / Kinloch, ZIPs 63134 & 63140)

Date of research: 2026-10-08. Output: `batches/schools_batch13.json` — 15 rows, one per
seed row in `batches/schools_seed_batch13.json`; no rows merged, split, or dropped.

## Context: the 1937 Berkeley–Kinloch split (key to the whole batch)

Nearly every row in this batch traces to one event: **Kinloch School District No. 18**
(originally "No. 5", formed 1902) was split in 1937–38 when white residents of northern
Kinloch Park — the community briefly called **Nuroad** — incorporated as the city of
**Berkeley** (August 1937) and created their own district over the school for Black
students' location. The federal courts later forced Berkeley and Kinloch districts into
Ferguson-Florissant in 1975 (US v. Missouri, 388 F. Supp. 1058; June 7, 1975 order;
affirmed 515 F.2d 1365), and the Kinloch district's remaining facilities closed with the
1975-76 school year. Sources: Washington University history text (gateway_book_2.pdf),
the 8th Circuit opinion, the Kinloch and Berkeley Wikipedia articles, and the BHS alumni
site (barkerreunion.blogspot.com, which publishes John A. Wright Sr.'s school history).

## Confirmed vs. unknown

**Confirmed (both dates, or one date + still-open):**
- `ALL-390` Airport Elementary — built 1954, closed 2019, per the City of Berkeley's own
  RFP for converting it to a community center (the strongest kind of source: a municipal
  document). STLPR confirms the Oct 2018 board vote and the failed lawsuit to block it.
- `ALL-398` Our Lady of the Angels — opened 1931 (Wikipedia + St. Louis Black Heritage
  Trail agree); closed 2002 per Wikipedia.
- `ALL-394` Kinloch HS – Dunbar Campus (opened side) — the Black high-school program
  began inside Dunbar in 1936 (Wikipedia + WashU history agree).
- `ALL-381` Berkeley HS – Walter Ave (closed side) — school closed end of 2003/first
  semester 2004 for airport expansion; McCluer South-Berkeley opened Jan 2004 explicitly
  "replacing Berkeley High School" (confirmed successor).
- `ALL-385`/`ALL-386`/`ALL-387` — all confirmed still operating (NCES, district org
  chart, school's own sites).

**Probable (real evidence, some conflict or informality):**
- `ALL-380` Caroline Ave campus 1947–1955 — consistent with a Post-Dispatch listing
  showing 6033 Caroline as "Berkeley Junior High" while the senior high was at 8710
  Walter, but the exact 1947 opening could not be independently pinned; the building may
  actually be the "brand new 1937" WPA-era building alumni describe.
- `ALL-381` opened 1955 — building described as "over 40 years" old in 1998.
- `ALL-383` Berkeley Middle "closed 2020" — NCES-recorded end of the middle school as a
  6-8 entity in the 2019 reorganization; renamed/rebranded Berkeley Intermediate per the
  Mo. Dept. of Conservation roster ("Berkeley Middle (Now Berkley Intermediate)").
- `ALL-385`/`ALL-386` opened ~2019 — current 3-5 / intermediate schools date to the
  2018-19 grade reorganization, not to new construction.
- `ALL-391` Nuroad — closed (transferred to Berkeley district) 1937. Probable
  identification with the 5924 Hancock "Kinloch School"/"Little Red Schoolhouse"
  (1902-03, G.E. Reid, still standing per county inventory).
- `ALL-393` Kinloch High School — opened 1937-38, closed 1976 with the district
  dissolution; students to McCluer North.
- `ALL-395` Dunbar — opened 1913/14; closed 1975 (conflict with seed's 1967, see below).
- `ALL-396`/`ALL-397` Vernon — 1885 schoolhouse → 1927 building → closed 1967.

**Left unknown:**
- `ALL-392` Scudder Avenue School — both dates unknown; the seed's framing is likely
  wrong (see flags).
- `ALL-383`/`ALL-387` opened years (Frost Ave and Harold Dr building dates not found).
- Successors for Vernon, Dunbar, Scudder, and Airport Elementary (students dispersed;
  no documented single successor).

## Data-quality flags

1. **`ALL-392` Scudder Avenue School — seed narrative backwards.** Seed says "white
   Kinloch school after Kinloch District 18 formed in 1902," closing 1937. Per Wright's
   history and the St. Louis Black Heritage Trail, Scudder was the *pre-1902 white*
   school that was *handed to Black students* in 1903 and served as Kinloch's Black
   elementary; it disappeared before 1937 (WashU says the district then had only two
   schools, Nuroad and Dunbar — Scudder's real end was probably ~1913-14 when Dunbar
   opened). Seed's "1937" reflects the Berkeley split, not a school closure.
2. **Scudder district vs. school are different entities.** A "Scudder School District"
   (ALL-403, another batch) survived independently until annexed by the Berkeley
   district on Aug. 24, ~1959/60 — ~260 students, ~75% Black, no high school (Southern
   School News, via teva.contentdm). Whether that district ran a school also called
   "Scudder" after 1903 is unresolved — recommended human follow-up.
3. **`ALL-394` vs `ALL-395` — same building.** "Kinloch HS – Dunbar Campus" is just the
   1936-38 high-school program *inside* the Dunbar School building; kept separate per
   the no-silent-merge rule. ALL-499 (another batch) describes the same thing again.
4. **`ALL-396`/`ALL-397` Vernon — district attribution likely wrong in seed.** Vernon
   was a *Ferguson* School District school for Black children (stlblackheritage:
   "remained in use as an all-black school in the Ferguson District until it was closed
   in 1967"), not a Kinloch district school. Almost surely the same school as ALL-427/
   ALL-428/ALL-429 (Ferguson-district rows in other batches) — flagged in
   `schools_seed_deduped_review_needed.json`.
5. **`ALL-395` Dunbar closure-year conflict:** seed 1967 vs. Wikipedia 1975. Seed's 1967
   appears to be conflated with Vernon's well-attested 1967 closure; Wikipedia's 1975
   fits the district's 1975 dissolution. Recorded 1975/probable; a consolidated
   "Kinloch Elementary" (a.k.a. Smith School, per SLCL's Black Heritage Trail index)
   may have absorbed it earlier — unresolved.
6. **Kinloch High School name collision:** the "white" Kinloch High School building was
   renamed Berkeley High School in 1937 (Wikipedia/Bosenbecker) — sources that say
   "Kinloch High opened 1937" may mean either building. My rows separate them: ALL-393 =
   the Black high school; ALL-379/380/381 = the white→Berkeley lineage.
7. **`ALL-385`/`ALL-386` naming overlap:** "Berkeley Elementary" (NCES 4030, grades 3-5)
   and "Berkeley Intermediate" (bis.fergflor.org) share 8300 Frost Ave and the same phone
   number — one school with two names or two co-located schools is unclear; flagged for
   district follow-up. Also, an older pre-1975 Berkeley elementary lineage likely existed
   and was demolished for the airport — the current school is a 2019 regrade, not that
   lineage's direct continuation.
8. **Holman name collision:** `ALL-387` Holman Elementary (FFSD, Berkeley) is NOT the
   Pattonville district's Holman Middle School (ALL-177/187/231/263).
9. **Airport Elementary address typo:** city ordinance says "8249 Airport Rd"; RFP, seed,
   and NCES all say 8429.
10. **All rows are `entity_type: individual_school`** — no administrative-district-named
    rows appear in this batch (those live in other batches: ALL-400-406, etc.).

## Sources that were especially useful (for reuse)

- **history.wustl.edu gateway_book_2.pdf** — WashU history text with the most precise
  account of the 1937 Nuroad protest and the two-school Kinloch district.
- **barkerreunion.blogspot.com** — BHS alumni site publishing John A. Wright Sr.'s
  Hancock School/"Little Red Schoolhouse" history and a 1931 "Directory of Nuroad's
  Citizens"; explains that "Nuroad" was the pre-incorporation community name (~1930-37).
- **St. Louis County Historic Buildings Inventory** (ig.stlouiscountymo.gov) — dates and
  architects for standing school buildings (e.g. 5924 Hancock, 1902-03, G.E. Reid).
- **US v. State of Missouri, 388 F. Supp. 1058 (1975)** and **515 F.2d 1365 (8th Cir.)**
  — authoritative for the 1975 annexation order, effective 1975-76, and the pre-1937
  Kinloch No. 18 school configuration ("one high school and one elementary school for
  white children, and one elementary school for black children").
- **Southern School News** (segregation-era newsletter, via teva.contentdm.oclc.org) —
  the only source found documenting the ~1959-60 Scudder School District annexation.
- **berkeleymo.us RFP documents** — municipal primary sources; pin Airport Elementary's
  1954 construction and 2019 closure exactly.
- **stlblackheritage.com (St. Louis Black Heritage Trail)** — best consolidated account
  of Kinloch's Black schools (Vernon 1885/1927, Dunbar 1913, Kinloch High 1936-37,
  Our Lady of the Angels 1931); also the only source that correctly locates Vernon in
  the Ferguson district.
- **Federal court record (E.D. Mo. case, April 2019 TRO, via CourtListener/Recap)** —
  verbatim description of FFSD "Option 2": Berkeley Middle building → grades 3-5,
  Holman → PreK-2, Airport closed.
- **education.mdc.mo.gov school roster** — transitional names ("Berkeley Middle (Now
  Berkley Intermediate)"), useful for following renames that NCES records miss.
- **SHSMO manuscript collections** (files.shsmo.org) — S0151 (Kinloch History Committee,
  incl. a Kinloch Elementary remodel study and "Kinloch High 1940 annual" reference) and
  S0707 (Kinloch School Desegregation) — recommended for human follow-up.

## Process friction

- **Contested dates without primary records:** Dunbar 1967-vs-1975 and the Kinloch High
  1936/1937/1938 variants can't be settled online; Wright's book ("Kinloch: Missouri's
  First Black City," Arcadia 2000) is cited by nearly every secondary source but isn't
  fully accessible — a human with the physical book or SHSMO collections could resolve
  most of this batch's `probable`s quickly.
- **The seed conflates building lifespans with program lifespans** (ALL-394 vs 395;
  ALL-396 vs 397). Each "campus" row needed a judgment call on which dates it tracks;
  I recorded the program/school-function dates and explained the overlap in `notes`.
- **NCES closures lag reality** — "Berkeley Middle (Closed 2020)" is a rename/regrade,
  not a closure; same trap the pilot found with publicschoolreview-derived dates.
- **Pre-1940 Kinloch/Berkeley school geography** is only reconstructable from alumni
  and history books — exact building addresses for Nuroad, Scudder, Dunbar, and the
  Kinloch High building were not found online.
- **No district records online** for the Berkeley School District era (1937-1975):
  junior-high move dates, elementary building dates, and the Caroline Ave campus's
  construction year likely require Ferguson-Florissant district archives or Post-Dispatch
  microfilm — recommended human follow-up.
