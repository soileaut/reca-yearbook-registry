# Track A Notes — Batch 09 (ZIPs 63074 St. Ann / 63114 Overland)

Date of research: 2026-10-08. Output: `batches/schools_batch09.json` (15 rows — count
unchanged; no rows merged or split). Batch is dominated by the Ritenour School
District's history, so one authoritative source did most of the work.

## Confirmed vs. unknown

**Fully confirmed (opened + closed/current status with citations):**
- `ALL-285` Ritenour High School — four-year program began fall 1914 (district
  history; names of all ten freshmen are printed), still open at 9100 St. Charles
  Rock Rd (campus since the 1950-51 term). Seed's 1927 rejected.
- `ALL-287` Ritenour Middle School — opened 1950 as the district's first junior
  high in the former (1924) high-school building; became a middle school 1981.
  Still open (school's own history page).
- `ALL-288` DeHart School — opened 1945 (Mo. Court of Appeals record, DeHart v.
  Ritenour, 663 S.W.2d 332: classes 1945–1981); district's own 100-Facts page says
  "closed in 1980" — recorded 1980 probable for the one-year discrepancy.
- `ALL-289` Iveland Elementary — permanent four-room building 1936 (school's own
  history page), still open. Seed's "1940s" corrected.
- `ALL-290` Buck School — built/opened 1846; became Ritenour School in 1867 when
  the district formed (closed = rename, probable). Successor ALL-321 ("Ritenour
  School", in another batch) per the district's explicit lineage statement.
- `ALL-291` Lackland Avenue School — opened October 1888 (district history; seed's
  "1900s" corrected), closed late 1915 when consolidated into the new Elmwood
  building; successor ALL-292 confirmed.
- `ALL-293` Holy Trinity School — opened 2002 (parish/school consolidation),
  closed end of 2018-19 school year. Both dates confirmed by the St. Louis Review.
- `ALL-297` American Trade School — founded/incorporated 2003 (BBB), still open.
- `ALL-300` Ritenour Consolidated School District — rural district formed 1867
  (MoHistory + district history), still operating. Set
  `administrative_district_only`; member schools enumerated in notes.
- `ALL-303` Ritenour HS – Forest Avenue Campus — opened Sept 1924 (RMS history +
  district history), served as HS until 1950 (district 100 Facts), then junior
  high. Successor ALL-285.
- `ALL-304` Ritenour HS – Old Overland Campus — HS-level classes began 1910 in the
  1907 Overland/Ritenour grade-school building (Mo. Supreme Court, State ex rel.
  Bender v. Hackmann, 1922 — probable); program moved to Forest Ave Sept 1924.
  Successor ALL-303.

**Probable:**
- `ALL-292` Elmwood Park School — opened 1899 as rented "branch school" (permanent
  building 1915); closed ~1975 when an HEW integration plan dispersed students
  among Wyland, New Overland (ALL-308) and Iveland (ALL-289) — no single
  successor, so `none` with the dispersal documented in notes; building then
  housed Vo-Prep and was sold summer 1976.
- `ALL-295` Hope Lutheran School – St. Ann — operating since 1943, closed 2016
  (privateschoolreview only; single source, hence probable). Church still active.

**Left unknown:**
- `ALL-299` "St. Ann School District" — no evidence it ever existed (see flags).
- `successor` for ALL-288 DeHart (receiving school not identified in any source).
- `ALL-298` Olivet University St. Louis campus opened year is probable (2023 St.
  Ann special-use permit) rather than fully pinned.

## Data-quality flags

- **SEED ERROR (ALL-293):** "Closed 2024" is actually the August 2024 date Ritenour
  bought the property for its Center for Educational Excellence; the school closed
  in **2019**.
- **LIKELY PHANTOM (ALL-299):** no "St. Ann School District" appears to have ever
  existed — St. Ann was platted 1943/incorporated 1948 and has always been served
  by Ritenour and Pattonville. Set `entity_type: ambiguous_unresolved`; retained as
  a search alias per policy.
- **`ALL-300` is a district, not a school** — `administrative_district_only`. Seed's
  "organized as a consolidated district in 1910" is unverified: district formed
  1867 (rural), reorganized 1907 (village district, six-member board), and
  "Consolidated" is documented by 1921-22 court records. 1910 likely conflates the
  start of HS coursework that year.
- **Seed open-date corrections:** ALL-291 (1900s→1888), ALL-289 (1940s→1936),
  ALL-304 (1918→1910 — 1918 was the first *graduating* class), ALL-285 (1927→1914).
- **ZIP fields are served-community values**, not physical: Ritenour HS, Ritenour
  Middle, DeHart, Iveland, Lackland, Elmwood are all physically in 63114
  (Overland/Breckenridge Hills), not 63074.
- **Cross-batch successors:** Buck School → ALL-321 (Ritenour School); Elmwood
  dispersal included ALL-308 (New Overland); Overland School itself is ALL-309;
  Scudder Avenue School is ALL-392. Coordinators merging batches should link these.
- **DeHart deed reverter:** the 1944 sale required the building to be a school for
  "white children" named Lewis DeHart School — litigated through 1983 after
  closure; the site is now a bank.

## Useful sources for reuse

- **`our_first_132_years_ada.pdf`** (Patricia Lewis Williamson, 1978, on
  ritenourschools.org) — the district's commissioned history built from board
  minute books; answered nearly every Ritenour question in this batch.
- **ritenourschools.org "100 Interesting Ritenour Facts"** and per-school "History
  of …" pages (RMS, Iveland) — concise date confirmations.
- **State ex rel. Bender v. Hackmann (Mo. 1922)** and **DeHart v. Ritenour
  Consolidated School District (Mo. App. 1983)** — court opinions gave precise
  dates (HS classes from 1910; DeHart classes 1945-1981) unavailable elsewhere.
- **stlouisreview.com** — authoritative Archdiocese school closure/consolidation
  coverage (Holy Trinity).
- **City board/committee packets** (stannmo.org DocumentCenter) — useful for
  recent private-school campus changes (Olivet permit, 2023).

## Process friction

- **District-level formation taxonomy is murky:** "rural" (1867) → "village" (1907)
  → "consolidated" (by 1921) transitions for Ritenour are documented but the exact
  1910 consolidated-district organization the seed cites couldn't be verified;
  expect similar unverifiable formation claims in other district rows.
- **private school closure years lean on privateschoolreview.com**, which as the
  pilot noted can reflect a record year rather than a true closure — mitigated
  here by marking confidence `probable`.
- **Recommended human follow-up:** St. Louis County recorder/DESE historical
  district directories could definitively confirm no St. Ann district existed, and
  Ritenour board records could pin DeHart's exact final school year (1980 vs.
  1981) and Elmwood's last year as an elementary (1975 vs. 1976).
