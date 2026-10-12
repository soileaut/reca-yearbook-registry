# Track B — SHSMO / St. Louis Research Center: Process Notes

Date: 2026-10-12 · Session: `track-b-shsmo` · Branch: `track-b/shsmo`
Output: `yearbook_registry_shsmo.json` (26 rows) · Index: `data/archive_indexes/shsmo.json` (1,126 collections)

## How searchable is collections.shsmo.org?

**Fully enumerable — one paginated table per research center, plus PDF finding aids.**

1. **Manuscript index** — `https://collections.shsmo.org/manuscripts/saint-louis`
   is a flat table of every St. Louis Research Center collection (S#### series,
   which includes the former Western Historical Manuscript Collection–St. Louis
   holdings — same catalog, treated as one surface per the coordinator brief).
   Paginated `?page=0..11` at ~100 rows/page → **1,126 collections**, each row
   carrying number, title, collection dates, a prose description, and a
   finding-aid link. Saved in full to `data/archive_indexes/shsmo.json`.
2. **Finding aids are PDFs** at a stable pattern:
   `https://files.shsmo.org/manuscripts/saint-louis/S####.pdf` — the real
   container lists (folder-level detail). 61 were fetched for school-adjacent
   collections; per-year volumes come from these, not the index page.
3. The site search (`shsmo.org/search`) is org-wide, not a collections
   filter; the manuscripts index IS the collection-level enumeration.
   `/search/` is robots-disallowed — enumeration only touched index pages and
   public PDFs, human-paced.
4. `digital.shsmo.org` (CONTENTdm) has a JSON API
   (`/digital/api/search/searchterm/...`) — probed for yearbooks: 191 hits are
   publications/photos, **no STL-area school yearbook scans**. Everything found
   here is `physical_only`.

## Method

Enumerated all 1,126 St. Louis collections → keyworded titles+descriptions for
school/yearbook terms and diffed against all 288 in-scope seed rows
(`out_of_scope_closed_before_1949` and `administrative_district_only` skipped) →
fetched finding-aid PDFs for every plausible collection → per-year volumes from
container lists. Most famous holdings (Sumner, Vashon, Webster Groves, Clayton,
Southwest, Jennings HS, Douglass, Hosmer Hall, Fontbonne, St. Charles HS,
Wellston) are **not seed schools** — the seed is scoped to the north-county /
St. Charles impacted areas; those are noted here but can't produce registry rows
(`school_id` must exist in `schools_master.json`).

## Yearbook holdings mapped to seed schools

| school_id | school | volumes | collection |
|---|---|---|---|
| ALL-328 | Normandy High School | 1943, 1944 | S0420 Normandy Area Historical Assoc. |
| ALL-366 | St. Vincent Home for Children | 1956–1965 (run) | S0420 (same) |
| 63147-12 | UMSL | 1960-1962 (Residence Center), 1967 "Young Years" | S0533 |
| 63147-08 | Beaumont High School | 1971, 1972 — NEW pairs, master only had ≤1964 | S1114 John Buckner Papers |
| ALL-562 | Francis Howell High School | 1943, 1945, 1946 | S0039 Medlock-Luecke |
| ALL-393 | Kinloch High School | 1948 (photo items 201.25-33) | S0201 Black History Project |

Confirmed absences (`year: "all"`, collections checked hold no yearbooks):
ALL-372 Normandy School District (S1146/S0326/S0951/district folders of S0420),
ALL-444 & ALL-445 Junior College predecessors (S0692), ALL-009 St. Ferdinand
School (S0432 parish records), ALL-292 Elmwood Park (S0584 photos), ALL-416
Ferguson HS (S1163 AAUW org-yearbooks only + S1214).

## Notable holdings for NON-seed schools (context — worth recording)

All `physical_only`, St. Louis Research Center: Sumner HS 1929-1950 scattered
(S0468); Vashon HS 1945/1947 (S0468); Stowe Teachers College 1949 (S0468);
Douglass HS "Oracle" 1935 + "Trojan" 1947-48 (S0698); Clayton HS "Clamo"
1945-1951 (S0716); Southwest HS 1948 (S0506) + 1953-1957 (S0791); Wellston HS
"Welhisco" 1952-1955 (S0766); St. Charles HS "Charlemo" 1975-1977 (S0039 — also
at SCCHS); Hardin Middle St. Charles 1997-2000 (S0039); Taylor School "Sartor"
1947-1952 (S1180); Mo. Baptist School of Nursing "Caduceus" 1946-1960 (S1180);
McKinley HS "Nugget" 1939/1942 (S0790 — DECOY vs ALL-351 McKinley School, a
Normandy elementary); Fontbonne yearbooks 1929-1962 (S0680, the closed
university's archives); Jennings HS "Jen-Echo" 1948-1950 (S0336); Western
Military Academy 1943-1948 (S0341, Alton IL); Hosmer Hall "Ivy" 1909 (S1082);
Webster Groves HS "The Eco" 1960/1962 (S1203 — the previously spot-checked
items, confirmed plus per-year detail).

## Dead ends

- `digital.shsmo.org` — 191 "yearbook" hits are Missouri Historical Review /
  Missouri Press News issues and out-of-area schools (Charleston, Caruthersville
  "Booker T. Washington"). No STL-area school yearbook scans.
- Other research centers (Columbia, KC, Cape Girardeau, Rolla, Springfield) —
  page-0 probe: few yearbook mentions, all out-of-area (SE Missouri). St. Louis
  schools live in the St. Louis center; the S-index is the exhaustive surface.
- S0477 Soldan HS Collection and S0650 Ruth Cherrick Class Book — newspapers,
  certificates, and a personal class book, no yearbook volumes. S0815 Southwest
  HS — photos/newsletters/drives only. S0895 Kirkwood — scrapbooks only.

## Recommended `data/digital_archives.json` update for `shsmo`

- `coverage_status`: `index_enumerated (1,126 St. Louis Research Center
  collections enumerated + 61 finding aids checked; physical-only surface —
  digital.shsmo.org holds no STL school yearbook scans)`
- `covered_schools`: `["ALL-328","ALL-366","ALL-393","ALL-562","63147-08",
  "63147-12"]` — note ALL-372 keeps school/district *material* but no yearbooks;
  the earlier entry's coverage was material-level, not volume-level.
- `enumeration_method`: `browse_index` → `api`-equivalent (flat paginated index
  + per-collection PDF finding aids at stable URLs).
- `whmc_umsl`: mark `index_enumerated` and point `covered_schools` at the same
  list — same catalog, one search (per coordinator dedupe rule).
