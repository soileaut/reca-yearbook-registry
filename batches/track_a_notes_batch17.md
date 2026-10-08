# Track A Notes — Batch 17 (ZIP 63138 Bellefontaine Neighbors/Spanish Lake + 63140 Kinloch)

Date of research: 2026-10-08. Output: `batches/schools_batch17.json` — 15 rows,
one per seed row; no rows merged, split, added, or deleted.

## Confirmed vs. unknown

**Fully or mostly confirmed:**
- `ALL-484` Grace Lutheran School — opened September 1955 (congregation's own history
  page: site purchased March 1953, day school opened in the chapel ground floor with two
  teachers covering K-4). Still open as Grace Chapel Lutheran School, 10015 Lance Dr.
- `ALL-483` St. Jerome School — opened November 1954 with 511 students (St. Louis
  County Council resolution honoring the parish; parish founded March 17, 1952, church
  building on Ashbrook Dr opened May 21, 1961). Parish suppressed in the 2005
  archdiocesan merger into Holy Name of Jesus Parish — school closing recorded as
  probable 2005.
- `ALL-485` Stormin Academy — **seed name is a misspelling**: the real school is
  Storman Academy (Storman-Stufflin / now Storman Lions Leadership Academy), opened
  September 7, 1981 by Jacqueline Storman Turnage — Missouri's first Black-owned,
  non-sectarian independent private school (St. Louis American, county council
  resolution). Still operating per NCES PSS (~45 PK-8 students, 10014 Diamond Dr).
- `ALL-489` Hazelwood School District — founded December 10, 1949 (district
  anniversary materials); federal court stipulation confirms it formed from thirteen
  rural districts between 1949 and 1951 (US v. Hazelwood SD, 392 F.Supp. 1276).
  Still operating. `administrative_district_only`.
- `ALL-494` Danforth Elementary — closure confirmed: RGSD board voted June 24, 2025
  to close it after the 2025-26 school year; farewell tour June 4, 2026; building being
  repurposed as a community center. Opened ~1956 (probable — Post-Dispatch describes a
  70-year-old building).

**Probable (real but informal or inferred evidence):**
- `ALL-493` Gibson Elementary — opened fall 1953 (alumni-written district history);
  still open (9926 Fonda Dr).
- `ALL-482` Our Lady of Good Counsel School — parish relocated from St. Louis City
  (1114 Destrehan) to Bellefontaine Neighbors in 1951; school operating by 1954;
  parish suppressed 2005 into Holy Name of Jesus Parish.
- `ALL-488` Riverview Gardens School District — grew out of Science Hill District #20;
  the "Riverview Gardens" name dates to ~1926-27 when the 1926 brick building at 805
  Chambers Rd went up and the high school was founded (1927); modern boundaries fixed by
  the 1949 annexation of Moline District #19. Still operating under a state-appointed
  Special Administrative Board. `administrative_district_only`.
- `ALL-490` Hazelwood SD - Spanish Lake Schools — umbrella grouping, not a legal
  entity; `administrative_district_only` with member schools named in notes.
- `ALL-491` "Bellefontaine Neighbors School" — identity resolved as the district school
  at 805 Chambers Rd (1926 Science Hill building housing RGHS/Junior High), the only
  public school inside city limits at incorporation per the RGSD alumni history.
- `ALL-495` Fort Bellefontaine Military Reservation School — see flags below; recorded
  opened 1913 (probable) for the boys' training school the City of St. Louis built on
  the former reservation.
- `ALL-497` Kinloch High School - Original Campus — segregated Black high school;
  program began at Dunbar in 1936, dedicated building ~1937; closed 1976 after the
  federal-court annexation of Kinloch into Ferguson-Florissant R-II (US v. Missouri,
  388 F.Supp. 1058; aff'd 515 F.2d 1365). Successor: Berkeley High School (ALL-378).
- `ALL-508` Kinloch Elementary School — real distinct school, 5924 Hancock Ave, built
  1902-03 (St. Louis County Historic Buildings Inventory); closed probable 1975
  (annexation year; the court plan contemplated its continued use — final closure
  unverified).

**Left unknown:**
- `ALL-476` Hazelwood Opportunity Center — program founding year not published; site
  current (hoc.hazelwoodschools.org). The building is the 1954 original Hazelwood High
  (ALL-459/460 in other batches). Recommend asking HSD directly.
- `ALL-477` St. Louis County School for Handicapped Children — best-matched to the
  Special School District of St. Louis County (formally the "Special District for the
  Education and Training of Handicapped Children," est. December 1957, classes from
  1958, first own school = Frank Ackerman School, October 1961). Left
  `ambiguous_unresolved` because the name could denote either the district or a single
  building; if the district reading is right, treat as `administrative_district_only`
  and search Ackerman (ALL-478) and Northview (ALL-479).

## Data-quality flags

- **Phantom-ish name:** `ALL-485` "Stormin Academy" is a misspelling of Storman
  Academy — and the misspelling comes from the City of Bellefontaine Neighbors' own
  history document (the seed's likely source).
- **Duplicate seed rows:** `ALL-491` "Bellefontaine Neighbors School" and `ALL-492`
  "Bellefontaine Neighbors Public School" (in another batch) name the same unnamed
  referent — the district school at 805 Chambers Rd. Consider merging at coordination.
- **Conflated entities:** `ALL-495` "Fort Bellefontaine Military Reservation School"
  mixes the 1805-1826 army post (no school evidenced) with the boys' training school
  the City of St. Louis built on the site in 1913 — the lineage that becomes today's
  Fort Bellefontaine Campus (ALL-469/470, MO Division of Youth Services school).
- **Kinloch overlaps:** `ALL-497` (Kinloch HS - Original Campus) overlaps `ALL-393`
  and `ALL-496` (plain "Kinloch High School" rows for 63134/63140) — same school, kept
  separate per no-silent-merge rule. `ALL-508` "Kinloch Elementary" is **not** generic —
  it is the 5924 Hancock Ave building (1902-03); do not conflate with Dunbar School
  (ALL-395), the district's separate school for Black children.
- **ZIP caveat:** nearly all Bellefontaine Neighbors institutions in this batch
  (Gibson, Danforth, Grace Lutheran, Storman, the 805 Chambers Rd school) carry mailing
  ZIP 63137, not the seed's 63138 — seed ZIPs denote the community covered, not postal
  addresses.
- **Administrative rows resolved:** `ALL-488`, `ALL-489`, `ALL-490` are all
  `administrative_district_only`; `ALL-477` is `ambiguous_unresolved`.

## Useful sources for reuse

- **riverviewgardens1969.myevent.com "RGHStory"** — long, specific alumni-written
  history of Riverview Gardens SD: district lineage (Science Hill #20, Moline #19,
  1949 annexation), per-school opening dates (Gibson fall 1953, RGHS 1927, 805 Chambers
  Rd building 1926), Turner School as the district's Black school until 1955. Informal
  but detailed; cite as probable.
- **stlgs.org closed-churches list** and the Archdiocese closed-parishes PDF
  (capacity.com) — parish founded/suppressed dates for St. Louis archdiocese parishes;
  ideal for parochial schools.
- **St. Louis County Council resolutions** (stlouisco.civicweb.net) — surprisingly
  useful primary-ish source; produced exact dates for St. Jerome Parish/School.
- **ssdmo.org/our-story** — SSD founding (Dec 1957, classes 1958, Ackerman 1961).
- **SHSMO finding aids** (files.shsmo.org) — Frank Ackerman Papers (C3443) and
  LifeBridge Partnership records (S0280) document pre-SSD county special-ed provisions.
- **St. Louis County Historic Buildings Inventory** (ig.stlouiscountymo.gov) —
  building construction dates; gave Kinloch Elementary's 1902-03 build date.
- **Federal court opinions** (388 F.Supp. 1058; 515 F.2d 1365; 392 F.Supp. 1276) —
  gold for district formation/dissolution dates (Kinloch annexation, Hazelwood's
  13-district consolidation).

## Process friction

- **Parochial school dates ≠ parish dates.** Parishes have excellent founding/merger
  documentation (Archdiocese + StLGS), but the school attached to a parish often opened
  or closed on its own schedule (e.g., OLGC school confirmed operating 1954 via alumni
  comments, but no formal opening notice found). Parish merger year is a reasonable
  probable for school closure, not confirmation.
- **Small private/alternative programs publish no history.** Hazelwood Opportunity
  Center has an active site but no founding date; enrollment-driven closures (Danforth)
  are well covered only because the district published board actions.
- **postal ZIP vs. community ZIP.** Seed ZIPs systematically reflect community coverage;
  expect real mailing addresses to differ (63137 vs 63138 throughout Bellefontaine
  Neighbors).
- **Recommended human follow-up:** Missouri Baptist University / St. Louis County
  Library local history and the SLCL Kinloch files could pin down Kinloch Elementary's
  final year under Ferguson-Florissant and confirm whether a distinct "St. Louis County
  School for Handicapped Children" building existed before Ackerman (1958-61). Not
  contacted per scope rules.
