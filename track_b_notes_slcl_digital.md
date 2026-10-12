# Track B — SLCL Digital Archives: Process Notes (full scale-up)

Date: 2026-10-12 · Session: `track-b-slcl_digital` · Branch: `track-b/slcl_digital`
Output: `yearbook_registry_slcl_digital.json` (527 rows) + `data/archive_indexes/slcl_digital.json`

## Method — full enumeration (no per-school keyword searching needed)

The Recollect browse endpoint is server-rendered and paginates 24/page with
`&page=N`, so the whole school index was pulled without a browser:

- `https://slcl.recollectcms.com/nodes/search?bid=1267&orderby=node_title&order=asc&page=1..4`
  → **92** school-level subcollections ("St. Louis Yearbooks"; site reports count 92)
- `bid=1268` ("Other Missouri Yearbooks") → **22** subcollections
- `bid=1266` ("Other State Yearbooks") → **23** subcollections, but these are one
  *state-level* collection per US state (Illinois, Kansas, etc.) — not school-level.
  No `schools_master.json` row is located outside Missouri, so per-school items
  inside state collections were not enumerated.
- Bonus find: `bid=8232` — SLCL itself curates a **"RECA Impacted High Schools"**
  subject grouping of 18 subcollections (stored in the index file). Useful
  cross-check; it lists Hazelwood West, Lutheran HS, Rosary, St. Louis Prep
  Seminary, St. Thomas Aquinas and St. Thomas Aquinas-Mercy which are NOT in
  `schools_master.json`, and omits Ferguson/Normandy/U. City/Wentzville which
  we do match.

Per-school volume enumeration uses the same endpoint with
`bid=<subcollection_node_id>` — it returns the subcollection's items
(cross-links to sibling subcollections, titled "… Yearbooks", appear in the
listing and must be filtered out; non-yearbook items like directories also
appear).

## Matches — 17 school_ids with holdings

| school_id | school | subcollection (node) | volumes found |
|---|---|---|---|
| ALL-020 | Hazelwood HS (Dunn Rd era) | Hazelwood HS (4849) | 7 (1957–1964) |
| ALL-021 | Hazelwood HS (New Halls Ferry era) | Hazelwood HS (4849) | 8 (1967–1974) |
| ALL-022 | Hazelwood Central HS | Hazelwood Central (3308) | 11 (1975–1993) |
| ALL-064 | Hazelwood East HS | Hazelwood East (1924) | 12 (1977–1999) |
| ALL-032 | McCluer North HS | McCluer North (1400) | 23 (1973–2004) |
| ALL-044 | North Technical HS (North Tech) | North County Technical School (3309) | 4 (1975–1978) |
| ALL-111 | McCluer HS | McCluer (1393) | 21 (1964–1991) |
| ALL-114 | Berkeley HS | Berkeley (7594) | 17 (1954–1980) |
| ALL-148 | Pattonville HS | Pattonville (1547) | 46 (1939–1999) |
| ALL-285 | Ritenour HS | Ritenour Senior HS (1559) | 47 (1951–1999) |
| ALL-328 | Normandy HS | Normandy (1507) | 40 (1924–1975) |
| ALL-334 | Incarnate Word Academy | Incarnate Word (1244) | 8 (1950–1996) |
| ALL-376 | University City HS | University City (1275) | 24 (1924–1988) |
| ALL-416 | Ferguson HS | Ferguson (1182) | 1 (1947) |
| ALL-449 | Trinity Catholic HS | Trinity Catholic (1811) | held but in-library only |
| ALL-562 | Francis Howell HS | Francis Howell (7764, Other MO) | 4 (1987–1993) |
| ALL-603 | Emil E. Holt Sr. HS (fka Wentzville HS) | Wentzville (1973, Other MO) | 2 (1959, 1967) |

All other 249 in-scope target schools get `year: "all"` `not_found` rows —
the enumeration is the exhaustive check.

## Judgment calls / edge cases

- **Hazelwood High School (4849) era-split.** `schools_master.json` has no
  plain "Hazelwood High School" row — only building-era rows. Volumes
  1957–1964 → ALL-020 (Dunn Rd building), 1967–1974 → ALL-021 (New Halls
  Ferry). The 1975 volume (node 3334, titled "Hazelwood High School") is
  filed by SLCL in BOTH the Hazelwood HS and Hazelwood Central collections
  → recorded once under ALL-022 (the institution had been renamed Hazelwood
  Central ~1974). Cross-batch duplicate rows ALL-459 (=ALL-020) and ALL-460
  (Dunn Rd building's later campus role) were NOT given rows; they're the
  same institution/building.
- **Cross-links inside collections.** Hazelwood Central/East/West listings
  embed each other's *subcollection* links (title ends in "Yearbooks");
  filtered out so they don't count as volumes.
- **Non-yearbook items excluded** (mentioned, not given registry rows):
  Berkeley SD Staff Directory 1974–75 (node 8209), McCluer HS Student
  Directory 1973 (8634), McCluer HS Who's Who 1972–73 (8633).
- **Trinity Catholic (ALL-449):** collection node 1811 returns **0 public
  items** — its description says it holds post-1990 yearbooks for
  **in-library use only** (Trinity operated 2003–2021). Recorded as
  `digitized` + `year: "all"` with the restriction documented; no per-year
  enumeration possible without a branch visit.
- **McCluer North 2001–2004:** item records are public, but the collection
  note says post-2000 volumes may be in-branch only — flagged in
  `access_info`.
- **Decoys checked and rejected:** "Central High School" (node 475) is the
  SLPS Central HS (descended from St. Louis High School, 1853) — NOT
  Ferguson's Central School (ALL-115, also out-of-scope anyway); "Central
  High School (Cape Girardeau)" (1282) is unrelated; "Hancock High School"
  (4854) is Hancock Place SD (south county) — NOT Berkeley's Hancock Campus
  (ALL-379); "McKinley High School" is SLPS — NOT Normandy's McKinley
  elementary (ALL-351); "De Smet Jesuit" is the Creve Coeur prep school —
  NOT Florissant's DeSmet elementary (ALL-004); "St. Louis University High
  School" is SLUH — NOT the university row ALL-544; bid-1266 state
  collections (Washington, West Virginia…) are geography decoys.
- **Duplicate/campus rows covered by anchors** — deliberately given NO
  `not_found` row because the institution's volumes are recorded under the
  anchor school_id: ALL-149/ALL-198 (→ALL-148), ALL-303 (→ALL-285),
  ALL-339 (→ALL-328), ALL-379/380/381 (→ALL-114), ALL-417 (→ALL-416),
  ALL-441 (→ALL-044), ALL-457 (→ALL-064), ALL-459/460 (→ALL-020/022).
- **ALL-113 McCluer South-Berkeley** DOES get a `not_found` row: the
  Berkeley collection is entirely pre-2003 (MSB only existed 2004–2019).

## Probable seed gaps (schools with SLCL collections but NO master row)

These have real SLCL subcollections yet no `schools_master.json` row exists
to attach them to — coordinator may want a seed follow-up:

- **Hazelwood West High School** (1923; 6 vols, Hazelwood SD, opened ~1977)
- **Rosary High School** (1584; Spanish Lake girls' school, →Trinity 2003)
- **St. Thomas Aquinas HS** (1797) and **St. Thomas Aquinas-Mercy HS** (7585)
  — Florissant Catholic lineage →Trinity
- **Mercy High School** (1463) — St. Thomas Aquinas-Mercy predecessor
- **Lutheran High School** (1325) and **Lutheran High School South** (1322)
- **Labouré High School** (1286) — North County Catholic
- **Wellston High School** (9544; closed 1962), **Fairview High School**
  (5377; Jennings), **W. F. Gaunt High School** (3315; Affton),
  **St. Charles High School** (3311), **St. Francis Borgia HS** (1722;
  Washington MO — ALL-590/591 are the public schools, Borgia is separate),
  **St. Louis Preparatory Seminary** (3312), plus the rest of the ~92 which
  are mostly SLPS/south-county schools outside the seed's scope.

## Suggested `data/digital_archives.json` update for `slcl_digital`

- `coverage_status`: `index_enumerated` — but REPLACE the existing text:
  it claims "113 school collections; 25 unique seed schools matched" and
  lists school_ids **ALL-651…ALL-655 that do not exist in
  `schools_master.json`** (max is ALL-650). Verified enumeration found
  **114 school-level subcollections** (92 St. Louis + 22 Other Missouri)
  matching **17 school_ids** (+2 pilot: 63147-08, 63147-10).
- `covered_schools`: `["63147-08","63147-10","ALL-020","ALL-021","ALL-022",
  "ALL-032","ALL-044","ALL-064","ALL-111","ALL-114","ALL-148","ALL-285",
  "ALL-328","ALL-334","ALL-376","ALL-416","ALL-449","ALL-562","ALL-603"]`
- `enumeration_notes` addition: subcollection items enumerable via
  `bid=<subcollection_node_id>&page=N`; filter "… Yearbooks"-titled
  cross-links; Trinity Catholic items are in-library-only (0 public items);
  "RECA Impacted High Schools" curated grouping = node 8232.

## Dead ends / notes for future workers

- `?q=` on nodes/search is NOT a keyword filter (per pilot notes) — always
  enumerate via `bid`.
- Collection item counts shown on `/nodes/view/<nid>` pages ("Yearbook
  Items (N)") include items hidden from the anonymous browse listing —
  Trinity Catholic's in-library-only volumes are invisible to `bid=`
  enumeration. If a school is high-value, have a human check in-branch.
- robots.txt does not disallow `/nodes/search`; requests were paced ~2s.
