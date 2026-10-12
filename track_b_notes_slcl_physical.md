# Track B notes — slcl_physical (St. Louis County Library physical holdings)

Worker: track-b-slcl_physical. Date: 2026-10-12. Branch: `track-b/slcl_physical`.

## Source / access

- The live page (`https://www.slcl.org/yearbooks-and-alumni-publications`, which
  301-redirects to `/research-learn/genealogy/yearbooks-and-alumni-publications`)
  returns HTTP 403 to automated fetches. Per the assignment, Wayback Machine
  snapshots were used instead. No contact made; robots/ToS respected.
- **Primary index enumerated:** the page's *current* holdings table, captured in
  Wayback snapshot 2025-10-17 (web.archive.org/web/20251017014256/…). The page
  footer says "Updated: April 23, 2025". **1,914 rows**, columns: Organization
  Name | Year | Title | Type | City | County | State. Saved verbatim to
  `data/archive_indexes/slcl_physical.json`.
- **Prior version:** the ~Aug-2015 list (1,149 rows) the project had previously
  recorded (Wayback 2025-03-22 snapshot). Also parsed; nearly all of its org
  names are renames/supersets of the 2025 list (e.g. "Ritenour High School" →
  "Ritenour Senior High School", "Soldan High School" → "Frank Louis Soldan
  High School"). No old-only org maps to an otherwise-uncovered seed school,
  so the 2025 list alone was used as the index.

## Index shape

422 distinct organizations. Row types: yearbook 1800, alumni directory 32,
anniversary 31, directory 25, plus bulletins/indexes/reunion booklets.
Geography: MO 1,436 rows, IL 148, other states the rest. Only `type ==
"yearbook"` rows produced registry rows; non-yearbook items are noted below.

## Method

1. Enumerated the full table once (no per-school search needed — complete index).
2. Built candidate seed subset: 288 schools_master rows (excluding
   `out_of_scope_closed_before_1949` and `administrative_district_only`).
3. Token-overlap candidate generation (difflib ratio + shared core tokens,
   following find_potential_duplicates.py) + geography columns for
   disambiguation; every match reviewed by hand. No silent fuzzy-merges.

## Matches (20 seed schools, 195 physical_only rows)

| school_id | SLCL org | series | years |
|---|---|---|---|
| 63147-08 | Beaumont High School | Caduceus | adds only **1968, 1971** — all other volumes already in master (digitized or pilot physical_only) |
| 63147-10 | Riverview Gardens Senior High School | Echoes | all 15 physical years already `digitized` in master — no new rows |
| ALL-022 | Hazelwood High School + Hazelwood Central High School | Torch | 1972-1975, 1978, 1979, 1981 |
| ALL-032 | McCluer North High School | Polaris | 1973-78, 80 |
| ALL-064 | Hazelwood East High School | Pegasus | 1984, 87, 90-92, 99 |
| ALL-065 | Kirby Junior High | — | 1998 (hist. name of Hazelwood East Middle) |
| ALL-111 | McCluer High School | Crest | 1964-68, 2001-04 |
| ALL-148 | Pattonville High School | The Echo | 1953, 54, 58 |
| ALL-150 | Pattonville Heights Junior High | Pirate Plank | 1979 |
| ALL-285 | Ritenour Senior High School | The Melaureus | 1952-54, 65, 66, 70, 72 |
| ALL-328 | Normandy High School | The Saga | 1924-28, 35-57, 59, 64, 71-75 |
| ALL-334 | Incarnate Word Academy | various | 1950, 66-68 |
| ALL-376 | University City High School | The Dial | 1924-70 (23 vols), 88 |
| ALL-416 | Ferguson High School | Crest | 1947 |
| ALL-441 | North County Technical School | Happening | 1977, 78 |
| ALL-449 | Trinity Catholic High School | Trinity | 2004-08 |
| ALL-544 | St. Louis University | Archive | 1920-2003 (33 vols) |
| ALL-546 | Washington University | Hatchet | 1903-1990 (44 vols; index holds 2 copies of 1932, deduped to 1 row) |
| ALL-547 | Lindenwood College | Linden Leaves | 1958, 69, 70 |
| ALL-567 | Hollenbeck Middle School | Talon | 2006 |
| ALL-603 | Wentzville High School | Pow Wow | 1959, 67 (hist. name of Emil E. Holt Sr. HS) |

259 additional candidate schools have `year: "all"` / `not_found` rows —
their absence from a fully-enumerated index is a confirmed search result.

## Decoys / near-misses examined and rejected

- **'Hancock High School'** (St. Louis County, 1958-1961): Hancock Place
  district school — NOT Berkeley High School's "Hancock Campus" (ALL-379).
- **'O'Fallon High School'**: O'Fallon, St. Clair Co., IL — not O'Fallon MO
  (ALL-642).
- **'Francis Howell North High School'** (St. Peters): different school from
  Francis Howell Union (ALL-629). 'Union High School' (Union, Franklin Co.) also
  rejected.
- **'Washington Junior High School'** (St. Louis County, 1971/72 'Eagle'):
  could not be resolved to ALL-346 (Washington School, Normandy) or
  ALL-590 (Washington HS, Franklin Co.); left unmatched, flagged for a human.
- **'McKinley High School'** (St. Louis City): SLPS school, not Normandy's
  McKinley (ALL-351). Same for city 'Central High School'/'North High School'.
- **'DeSmet Jesuit High School'** (Creve Coeur): different from DeSmet School
  (ALL-004).
- **'Academy of the Sacred Heart'** (St. Charles): different from Florissant's
  Sacred Heart parish schools (ALL-005/007/008).
- **'Villa Duchesne'** (Frontenac): different from St. Rose Philippine Duchesne
  (ALL-047/048/056/108).
- **'Hazelwood West High School'** (Hazelwood, 'Focus' 1976-82): a real Hazelwood
  District HS with NO seed row — possible missing school, flagged to coordinator.

## Non-yearbook items of note (not registry rows)

- Harrison Elementary School: 1947-92 reunion publication only (ALL-352 →
  not_found for yearbooks).
- Incarnate Word Academy 2002 Alumnae Directory; University City HS Class-of-1952
  reunion booklet; various alumni directories/indexes (Beaumont index 1961-64,
  WashU law alumni directories, SLU bulletins).

## Suggested updates to data/digital_archives.json (`slcl_physical`)

- `coverage_status` → "index_enumerated (1,914-row April 23, 2025 holdings table
  enumerated in full via Wayback; supersedes the 1,149-row Aug-2015 list; 20 seed
  schools matched to yearbook holdings; 259 candidate schools confirmed absent)"
- `covered_schools` → the 20 matched ids:
  ["63147-08","63147-10","ALL-022","ALL-032","ALL-064","ALL-065","ALL-111",
  "ALL-148","ALL-150","ALL-285","ALL-328","ALL-334","ALL-376","ALL-416",
  "ALL-441","ALL-449","ALL-544","ALL-546","ALL-547","ALL-567","ALL-603"]
- **The recorded covered_schools list was stale and partially wrong:** it
  included ALL-651 and ALL-652, which do not exist in schools_master.json
  (renumbering drift); ALL-115 (out_of_scope, pre-1949); ALL-352 (reunion
  booklet only, not a yearbook); and it omitted ALL-022, ALL-065, ALL-111,
  ALL-148, ALL-150, ALL-328, ALL-376, ALL-416, ALL-441, ALL-449, ALL-544,
  ALL-546, ALL-547, ALL-567, ALL-603 which are all present in the current list.
- `source_url` should be updated to the new path
  `/research-learn/genealogy/yearbooks-and-alumni-publications`.
- Note for coordinator: live page 403s bots — enumeration must go via Wayback.

## Not pursued / limits

- No contact, login, or per-school catalog search was used (index was complete).
- Pre-1949 volumes included where listed (trivially found alongside RECA-era ones).
- Hazelwood West: holdings exist but no seed row — coordinator may want a new
  schools_master entry.
