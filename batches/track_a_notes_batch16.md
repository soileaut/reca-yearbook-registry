# Track A Notes — Batch 16

Date of research: 2026-10-08. Output: `schools_batch16.json` — 15 rows
(one per seed row; count unchanged). `reca_scope_status` left absent per the
batch instructions; `entity_type` set on every row.

Batch composition: three administrative-district rows (Ferguson Public School
District, Florissant School District, FFSD), three Hazelwood high-school
campus-era rows, Twillman Elementary, Trinity Catholic HS, and six Missouri
Division of Youth Services residential units on the Fort Bellefontaine campus.

## Confirmed vs. unknown

**Fully confirmed:**
- `ALL-449` Trinity Catholic HS — established fall 2003 by merger of St. Thomas
  Aquinas-Mercy + Rosary; closed end of 2020-21 school year (announced Feb
  2021). **Seed's 1957 open / 2025 close are both wrong.** The 1720 Redman Rd
  building opened as Rosary HS in 1961 (built 1959).
- `ALL-450` Ferguson Public School District — first school board appointed
  1867, per the history page of the 1948 Ferguson HS "Crest" yearbook
  (e-yearbook.com scan — a nice primary source hiding in plain sight).
  Merged into Ferguson-Florissant R-2 via the Oct 1951 county reorganization
  vote (operational 1952).
- `ALL-453` Ferguson-Florissant SD — created by the Oct 1951 reorganization;
  still operating (fergflor.org). Also absorbed Berkeley and Kinloch
  districts by federal court order, June 7, 1975.
- `ALL-459` Hazelwood HS original campus — 1954 building at 1865 Dunn Rd;
  ceased being the high school in 1966 when the second Hazelwood HS opened;
  building persists as Hazelwood Opportunity Center.
- `ALL-460` Hazelwood Central (mislabeled "Dunn Road Campus") — second
  Hazelwood HS, opened 1966 at 15875 New Halls Ferry Rd, **still open**.
  Seed's "closed 1977" is wrong (1977 = East/West opened, ending split shifts).
- `ALL-467` Twillman 1928 building — "around 1928" three-room building at
  11831 Bellefontaine Rd per the school's own history page; still open as
  Twillman Elementary. School lineage goes back to a one-room 1850 schoolhouse.
- `ALL-469`-`ALL-475` Bellefontaine Rd cluster — all are **current NCES-listed
  schools under the statewide Missouri Division of Youth Services district**
  (CCD district 2900009, 2024-25), grades 6-12, tiny enrollments (0-22).

**Probable:**
- `ALL-457` Hazelwood East split-session era — East established 1974 with
  classes of '75-'76 attending split sessions in the existing Hazelwood HS
  building; own building at 11300 Dunn Rd opened fall 1976 (Wikipedia) — the
  district's Central history page says "1977" for East/West opening, hence
  probable on the close year.
- `ALL-450`/`ALL-454` closed 1952 — the reorganization vote was Oct 1951;
  1952 is the commonly cited merger/operational year.

**Left unknown:**
- `opened_year` for `ALL-454` Florissant School District (district formation
  date not findable online; Florissant public schooling dates to at least
  1876 per the Combs seed row).
- `opened_year` for all six DYS units (`ALL-469`-`ALL-475`) — program-unit
  start dates aren't published; the site itself has been a youth facility
  since a 1913 City of St. Louis boys' detention/training school, becoming a
  DYS campus ~1986 (secondary sources only).

## Data-quality flags

- **Seed date errors:** `ALL-449` (1957→2003, 2025→2021), `ALL-460`
  (closed 1977→never closed), `ALL-475`-era `ALL-075` Twillman
  ("closed 1950s?"→never closed; in another batch).
- **Seed address errors:** `ALL-457` and `ALL-460` both say 1865 Dunn Rd —
  that address belongs to the original campus (`ALL-459`). The split-session
  site and Central's real campus are 15875 New Halls Ferry Rd (Florissant
  63031, not 63138).
- **Seed operator errors:** `ALL-469`-`ALL-475` say "Hazelwood School
  District" — actually Missouri Division of Youth Services residential
  program units (DYS FY2019 budget book lists each as a 1-2 "treatment group"
  moderate-care facility at the Fort Bellefontaine campus).
- **Duplicate rows:** `ALL-470` "Fort Bellefontaine School" = `ALL-469`
  "Fort Bellefontaine Campus" (same address; NCES only lists the latter).
  Cross-batch: `ALL-459`≈`ALL-020` (Hazelwood HS original), `ALL-460`≈
  `ALL-021`/`ALL-022` (second building / Hazelwood Central), `ALL-467`≈
  `ALL-075` (Twillman), `ALL-457`→`ALL-064` (Hazelwood East proper). All kept
  separate per the no-silent-merge rule; flagged for the coordinator.
- **Administrative rows:** `ALL-450`, `ALL-453`, `ALL-454` are
  `administrative_district_only`; member schools named in each row's notes.
- **`ALL-470` successor** recorded as `ALL-469` on probable confidence.
- Discovery Hall and Spanish Lake Campus show 0 students in 2024-25 CCD —
  listed but possibly inactive units.

## Sources worth reusing

- **e-yearbook.com scans of school yearbooks** — the 1948 Ferguson HS "Crest"
  contains a full district history page (1867 board, 1903 incorporation).
  Yearbook "history" pages are primary sources worth checking early.
- **School "About Us" pages on Finalsite** (`*.hazelwoodschools.org/about-us/`)
  — Hazelwood schools publish real building histories (Central: 1954/1966/
  1970 split shifts/1977; Twillman: 1850/1928/1975-76 remodel).
- **SLU PRiME Center consolidation blog** — dates the 1949/1951/1954 St.
  Louis County reorganization votes (Ferguson-Florissant R-2 = Oct 1951).
- **NCES CCD school lists by district** — DistrictID `2900009` is the
  statewide Division of Youth Services district; good for checking whether a
  "school" at a residential campus is a real NCES entity.
- **Missouri DSS/DYS budget request books** (oa.mo.gov PDFs) — list every DYS
  residential unit with address and treatment-group count.

## Process friction

- **NCES/Web detail pages don't expose opening dates** for program-unit
  schools (DYS halls) — formation dates likely require DYS annual reports or
  state archives. Recommended human follow-up only.
- **Campus-era seed rows** ("- Split Session", "- Original Campus",
  "- Dunn Road Campus") mostly encode building-era boundaries, not separate
  schools; several carry wrong addresses copied from a sibling row. Expect to
  correct, not just verify.
- **Wikipedia↔district-page conflicts** on East/West opening year (1976 vs
  1977) suggest school-year vs calendar-year ambiguity in the source
  material; recorded both in notes.
