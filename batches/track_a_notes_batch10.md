# Track A Notes — Batch 10 (ZIP 63114)

Date of research: 2026-10-08. Output: `batches/schools_batch10.json` — 15 rows
from `batches/schools_seed_batch10.json`, count unchanged (no merges or splits;
two lineage overlaps flagged but kept separate per the no-silent-merge rule).
No row in this batch is named like an administrative district, so every row is
`entity_type: individual_school`.

## Confirmed vs. unknown

**Fully confirmed (opened + closed/open status with real citations):**
- `ALL-307` Marion Elementary — opened 1925 (district history), still open.
- `ALL-310` Home Heights School — opened 1907, closed 1976 (district history);
  demolished 1998 for the Ritenour HS North Campus athletic field.
- `ALL-311` Midland School — opened 1925, closed 1976 (district history);
  leased to Special School District, demolished 1991.
- `ALL-312` Marvin Elementary — opened 1928 (302 pupils, 6 teachers), still open.
- `ALL-315` Ashby School — closed 1939 confirmed, replaced by Buder School
  (opened Sept 1939; portable sold to St. Luke's AME Church for $400).
- `ALL-321` Ritenour School — opened 1867 probable; superseded/renamed 1907
  (same continuous entity as ALL-309).
- `ALL-309` Overland School — opened 1907 confirmed; closed 1958 confirmed
  (replaced by Wyland Elementary; building is now the Ritenour Administrative
  Center). **Seed's 1924 closure is wrong** — 1924 was the year the high-school
  classes moved into the new RHS building.
- `ALL-328` Normandy High School — resolved seed's "1920s": opened for the
  1923-24 school year on the former Eden Seminary campus (school's own site +
  SHSMO S0326 finding aid). Still open.
- `ALL-331` Bel-Nor School — opened 1927 (City of Bel-Nor official history).
  Closed Dec. 2013/Jan. 2014, later repurposed and reopened; currently the
  district's only grades 1-5 school (~300 students). Recorded `n/a` + notes.
- `ALL-333` Christian Academy of Greater St. Louis — founded 1976 (own site +
  NCES-derived profile). Still open.
- `ALL-334` Incarnate Word Academy — opened Sept. 6, 1932 (school's own
  history page; 35 students first year). Still open.

**Probable (real evidence, some conflict or secondary-only sourcing):**
- `ALL-308` New Overland School — opened 1929 confirmed (bond Feb. 12, 1929).
  Closure year conflicts inside the district's own material: the 100-facts page
  says 1975 (matches seed), but the narrative history's March 25, 1976
  reorganization plan designated it for closure and Vo-Prep moved in during
  summer 1976 — and Elmwood students were reassigned TO New Overland for
  1975-76. Recorded **1976**; flag in row notes.
- `ALL-315` opening: recorded **1933** (portable moved to Ashby Rd in Sept.
  1933 per the narrative history) vs. the district fact list's "housed grades
  1-4 from 1936 to 1939" (which the seed echoes). Conflict documented.
- `ALL-329` Normandy HS - Historical Campus — interpreted as the pre-1923
  predecessor: high-school classes in the old Washington School building
  1907-spring 1912 (SHSMO finding aid; Wikipedia says closed 1911 — one-year
  conflict). Successor = ALL-328 (1923 reopening; 11-year gap).
- `ALL-330` Normandy Junior High School — standalone junior high opened ~1949
  on the Natural Bridge Rd site bought from the Sisters of the Cenacle in 1947
  (construction began 1948; Wikipedia building-year list: 1949). Junior-high
  instruction itself dates to 1923 (combined jr/sr) with an on-campus JH
  building from 1934. Later names: "Normandy Junior High/Middle" and "7th-8th
  Grade Center." **closed_year left `unknown`** — no source pins down when the
  NJH name/building ended; middle-grades function continues today as Normandy
  Middle School at Lucas Crossing (ALL-343, recorded as probable successor).
- `ALL-332` Bel-Ridge School — opened 1953 probable (Wikipedia building-year
  list; no stronger source found); closed 2011 probable (Wikipedia; NCES
  enrollment data ends in 2011; STLPR in Oct. 2013 calls it unused district
  property).

**Successor fields:** most genuinely `none` (still open) or `unknown`
(closure announcements never name receiving schools). Two successor links
across batches: ALL-315 → ALL-314 (Buder Elementary, per district history) and
ALL-321 → ALL-309 (same-site lineage). ALL-330 → ALL-343 is functional
continuation (probable). **Wyland Elementary School** — the documented 1958
replacement for Overland School — has NO row anywhere in the seed dataset;
recorded as `unknown` + named in notes. Recommend adding it.

## Useful sources for reuse

- **ritenourschools.org/community/history-of-ritenour** and its
  **100 Interesting Ritenour Facts** page — building years, closure years and
  demolition dates for nearly every Ritenour school, all in one page.
- **"Ritenour: Our First 132 Years" (1978 district history, PDF on the
  district site)** — board-minutes-derived narrative 1846-1978 with exact bond
  elections, opening dates and reorganization details. Single best source for
  this district; covers batches beyond this one.
- **files.shsmo.org/manuscripts/saint-louis/S0326.pdf** — State Historical
  Society of Missouri finding aid for the Normandy School District Collection;
  a solid condensed district history (1894 formation, 1907-1912 first high
  school, 1923 Eden Seminary purchase, 1934/1949 junior-high milestones).
- **normandyhighschool.normandysc.org** and **normandysc.org/about-nsc** —
  school's own 1923-24 opening claim and current configuration.
- **cityofbelnor.org/about** — municipal page with Bel-Nor School's 1927
  opening and building details.
- **iwacademy.org/about-iwa/history** — IWA's exact 1932 opening date.
- **STLPR (stlpr.org)** — October 2013 reporting on the Bel-Nor closure vote;
  useful for Normandy-district closures generally.
- **The school's own site worked repeatedly** (Marion, Marvin, Bel-Nor, CA,
  IWA) as the "still open" citation.

## Process friction

- **The district's own sources conflict on New Overland's closure (1975 vs.
  1976) and Ashby's opening (1933 vs. 1936).** Where the fact-list and the
  board-minutes narrative disagree I took the narrative and documented the
  conflict rather than silently picking one.
- **Bel-Ridge has almost no online footprint** beyond Wikipedia mirrors and an
  NCES-derived profile. Building year (1953) rests on Wikipedia alone —
  flagged probable. A Normandy district centennial book ("Normandy School
  District: The First One Hundred Years," 1994, held in SHSMO collection
  S0326) likely has exact dates; recommended human follow-up.
- **Normandy Junior High's end-of-life is undocumented online.** The building
  likely became the Early Learning Center at 7855 Natural Bridge Rd, but I
  could not confirm that or the rename date without contacting the district —
  left `unknown` with a recommended follow-up.
- **Seed ZIPs are aspirational, not literal.** Several rows list 63114 but the
  schools sit in 63121 (Bel-Nor, IWA), 63133 (Normandy HS) or 63074 — actual
  ZIPs noted per row. `zip` field kept at 63114 as descriptive seed metadata.
- **Schools migrate between buildings under one name** (Marion/Marvin both
  demolished and rebuilt on-site in the 1990s). Building-date vs.
  institution-date divergence is recorded in `notes` where relevant.

## Data-quality flags

- **`ALL-309` seed closure (1924) is wrong** — school ran to 1958; 1924 was the
  high school's move-out year. Corrected.
- **`ALL-308` seed closure (1975) likely off by a year** — best evidence is 1976.
- **`ALL-315` seed opening (1936) likely late by 3 years** — portable placed on
  Ashby Rd Sept. 1933.
- **Lineage overlaps (kept, not merged):** `ALL-321` + `ALL-309` are one
  continuous school (Ritenour→Overland, 1846/1867-1958, same site);
  `ALL-329` is a predecessor-phase row of `ALL-328` (1907-1912 vs. 1923-).
- **`ALL-333` seed address wrong** — real address is 11050 N. Warson Rd,
  63114, not "11050 St. Charles Rock Rd, St. Ann 63074."
- **Missing row:** Wyland Elementary (opened 1958, still open, replaced
  Overland School) is absent from the seed dataset entirely.
- **Cross-batch duplicate to watch:** `ALL-314` Buder Elementary (63114) says
  "Closed/Successor 1939-1981," but Buder closed 1981 AND reopened 1986 — it is
  operating today. `ALL-261` (63074) is likely the same school.
- **Recommended human follow-ups:** (1) SHSMO's "Normandy: The First One
  Hundred Years" (1994) for Bel-Ridge/NJH exact dates; (2) Normandy Schools
  Collaborative records for the NJH building's disposition; (3) New Overland's
  official closure year via Ritenour board minutes for 1975-76.
