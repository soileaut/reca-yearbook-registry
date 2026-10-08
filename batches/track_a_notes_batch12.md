# Track A Notes — Batch 12 (ZIPs 63121, 63134)

Date of research: 2026-10-08. Output: `schools_batch12.json` — 16 rows, one per seed
row (no merges or splits; every row kept, with flags where the seed entity is wrong,
phantom, or not a school).

Batch scope: mostly the City of Normandy / Normandy School District cluster (63121),
plus one Berkeley High School campus row in 63134.

## Confirmed vs. unknown

**Confirmed (opened + status with real citations):**
- `ALL-357` Barack Obama Elementary — opened 2011 as a new 65,000 sq ft building in
  Pine Lawn consolidating Garfield + Pine Lawn elementaries (STLPR, Kwame Building
  Group, district history). Still open (NCES/district site).
- `ALL-370` Unnamed African American School — in operation at district formation
  (July 12, 1894), closed 1895 when students moved to the new Washington School
  building (SHSMO S0326 finding aid). Seed's "1894" opening actually marks the
  district's formation, not the school's founding — opened_year left `unknown`.
- `ALL-371` Washington School African American Department — opened 1895 confirmed
  (same finding aid). End date unknown (see unknowns).
- `ALL-372` Normandy School District — formed July 12, 1894 confirmed (S0326);
  still operating as the legally-continuing Normandy Schools Collaborative
  (dissolved/reconstituted by the state effective June 30/July 1, 2014; local elected
  board fully restored June 30, 2024; the 2023 state action did NOT change the name).
- `ALL-376` University City High School — opened 1930 confirmed (district's own
  history page; NRHP nomination: designed 1928 by Trueblood & Graf). Still open.
- `ALL-377` Normandy Area Historical Association — est. 1974 confirmed (MoHistory
  ArchivesSpace). NOT A SCHOOL — see flags.
- `ALL-375` Bermuda Elementary — confirmed currently open at 5835 Bermuda Dr
  (NCES, now "Bermuda Primary School" PK-2 under FFSD reconfiguration); opened year
  unknown.

**Probable:**
- `ALL-356` Pine Lawn School — opened 1971 per district chronology; closed January
  2011 confirmed (STLPR), students to ALL-357 (successor confirmed).
- `ALL-358` Normandy Middle School at Lucas Crossing — opened 2001 probable
  (complex opened 2001 per Normandy city article; district chronology separately
  lists "Lucas Crossing School Complex - 2004"). The SEED'S NAME is wrong — see flags.
- `ALL-361` Normandy Early Learning Center — opened 2019 probable (district
  chronology). Address unresolved (see flags).
- `ALL-366` St. Vincent Home for Children — founded 1850-51 in the City of St.
  Louis; moved to the Normandy campus 1914 (RFT) or 1916 (archdiocesan facilities
  history). Still operating as a residential treatment / special-ed facility.
- `ALL-368` St. Ann Catholic School — opened 1858 probable (parish history page;
  the school's own page says classes began 1856 in the frame church). Still open.
- `ALL-379` Berkeley HS Hancock Campus — "1937" marks the Berkeley identity/district
  formation; the Hancock building itself is 1902-03 and housed HS classes by 1932.
  closed_year deliberately left `unknown`: the seed's 1947 conflicts with the alumni
  site's "BHS Reunion 1938-1960" framing (HS classes at Hancock through ~1960);
  the HS did move to a purpose-built campus, but the exact year is unfound.

**Left unknown:**
- `ALL-362` PAL Center — real program at 6834 Normandale Dr (existed by May 2010,
  STLPR); founding year and whether the PAL name is still used (current branding is
  C.A.S.A.) both unknown.
- `ALL-371` closed year — when the segregated department at Washington ended.
- `ALL-375` opened year — Bermuda Elementary's build date isn't online.
- `ALL-374` opened year — district grouping row; FFSD formation date not needed/found
  (existed before 1975).

## Data-quality flags (the important part)

1. **SEED ADDRESS SWAP (ALL-356):** "6506 Wright Way" belongs to **Garfield School**,
   not Pine Lawn School — the archived June 2003 district list gives Pine Lawn School
   at **2505 Kienlen Ave**. The seed's note "may occupy/relate to former Garfield
   site" reflects this mix-up.
2. **PHANTOM NAME (ALL-358):** there is no "Barack Obama Middle School." The school
   at the seed's address is **Normandy Middle School at Lucas Crossing**
   (7837/7855 Natural Bridge Rd — both numbers appear in district/NCES records for
   the same complex). Row renamed to the real entity; seed name kept as an alias.
3. **NOT A SCHOOL (ALL-377):** Normandy Area Historical Association is a historical
   society (est. 1974), not a school — but it's the single most valuable archive lead
   in this batch (its MoHistory + SHSMO S0420 deposits include school histories and
   yearbooks). Recommend excluding from the schools table and routing to Track B.
   `entity_type: ambiguous_unresolved` used only because the enum lacks a "not an
   institution" value.
4. **ADMINISTRATIVE ROWS:** ALL-372 (Normandy School District) and ALL-374
   (Ferguson-Florissant schools in Normandy) are `administrative_district_only` —
   yearbook work should target their member schools (members named in each row's
   notes). ALL-374 isn't even a district per se — it's "the wedge of Normandy inside
   FFSD."
5. **DEPARTMENT, NOT A BUILDING (ALL-371):** the AA "department" at Washington
   School was a segregated enrollment stream inside a shared building, not a
   standalone school — records/yearbooks may be filed under Washington School
   proper (related building rows ALL-344/345/346 are in other batches).
6. **SEED OPERATOR ERROR (ALL-366):** St. Vincent's was run by the Sisters of St.
   Joseph of Carondelet (until 1888) and Sisters of Christian Charity (until lay
   administration in 1996) — NOT the Daughters of Charity.
7. **SEED ADDRESS ERRORS:** ALL-366's "7301 St Charles Rock Rd" doesn't match the
   campus (7401 Florissant Rd; a related community center was at 7335 St. Charles
   Rock Rd in Pagedale). ALL-375's "11600 Old Halls Ferry Road?" is in Jennings
   territory — actual address 5835 Bermuda Dr. ALL-361: seed's 3417 St Thomas More
   Ln was the Kindergarten Center; the district's current enrollment page lists the
   ELC at 7855 Natural Bridge Rd and NCES shows 3101 Nordic Dr — unresolved move.
8. **ZIP NOTE (ALL-376):** U City HS is physically in University City 63130, not
   63121 — included for the pre-1922 Normandy attendance relationship.
9. **ALL-368 identification is probable:** "Normandy Catholic School" → St. Ann
   Catholic School is the best-supported reading (the parish elementary school of
   Normandy), but Incarnate Word Academy (girls' HS, est. 1932, in the Normandy
   area) is a possible alternate referent if the seed meant a secondary school.

## Sources that carried this batch

- **SHSMO finding aid S0326 (Normandy School District Collection)** — the single
  best source: district formation, 1894/1895 schools, the unnamed AA school, the
  1907-1912 high-school experiment, Eden Seminary purchase (1922), junior-high
  construction (1947-49), and the Normandy Residence Center → UMSL timeline.
- **Archived 2003 Normandy district school list** (surfaced via Wikipedia footnotes
  on Normandy, MO / Pine Lawn, MO / Normandy Schools Collaborative) — resolved the
  Garfield/Pine Lawn address swap, the Kindergarten Center at St. Thomas More Ln,
  and the Lucas Crossing opening chronology.
- **STLPR** — Garfield/Pine Lawn January 2011 closure + PAL Center existence (2010).
- **Kwame Building Group project page** — Obama Elementary completed 2011.
- **United States v. Missouri, 388 F. Supp. 1058 (1975)** — the court order that
  merged Berkeley + Kinloch into FFSD; explains the Berkeley/Kinloch campus rows.
- **Barker Reunion blogspot** (BHS Reunion 1938-1960) + **City of Berkeley history
  page** — Hancock School (Little Red Schoolhouse) built 1902, housed elementary +
  HS in 1932/1935.
- **Archdiocese of St. Louis Catholic orphanage history** (capacity.com PDF) +
  **Riverfront Times "Castles of Normandy and Bel-Nor"** — St. Vincent's timeline.
- **MoHistory ArchivesSpace** — NAHA history/collections (est. 1974).
- **NRHP nomination, University City Education District** (mostateparks.com PDF) —
  U City HS designed 1928, opened 1930.
- **NCES CCD/PSS** — current open status + corrected addresses (Bermuda, Obama,
  St. Ann, FFSD school list).
- **Normandy SC enrollment page + Code of Student Conduct PDF** — current school
  directory (names, addresses, grades).

## Process friction

- **Normandy school history is unusually well covered** thanks to SHSMO S0326 +
  NAHA deposits — but the same can't be assumed for other districts; the district
  finding aid essentially is the Normandy school gazetteer.
- **Building vs. program dates keep conflating** in seeds: Pine Lawn's "1971" is a
  building date; U City HS's "1930" is a building date (institution older); Berkeley
  HS Hancock's "1937" is the district/name date while the building is 1902.
- **Segregated-school records are thin online.** The 1895 AA department's end date,
  and whether Lincoln School (Pagedale) was Normandy's designated Black school, need
  the S0326/NAHA collections or Normandy board minutes — recommended human follow-up.
- **The PAL Center's current identity** (vs. the C.A.S.A. branding) and **the ELC's
  address history** are only resolvable via district records — recommended human
  follow-up with Normandy SC.
- **Archived district pages are load-bearing.** The 2003-era normandy.k12.mo.us
  school list (via Wayback) resolved multiple seed errors; future batches in other
  districts should check for similarly cached district directories early.
