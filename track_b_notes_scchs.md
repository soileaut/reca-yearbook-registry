# Track B — SCCHS (St. Charles County Historical Society, PastPerfect): Process Notes

Date: 2026-10-12 · Session: `track-b-scchs` · Branch: `track-b/scchs`
Output: `yearbook_registry_scchs.json` (55 rows), `data/archive_indexes/scchs.json` (227 records)

## Surface mechanics

- `https://scchs.pastperfectonline.com/` — standard PastPerfect Online portal
  (~15,000 records across Object / Photo / Archive / Library / Container List).
- **Bot filtering:** plain `curl` gets a bare 403; adding a full UA string +
  `Accept`/`Accept-Language` headers gets HTTP 200. No login needed anywhere.
- **Search URLs:** `GET /Search?search_criteria=<q>&page=N` (global, all
  catalogs) or `/<catalog>?search_criteria=<q>` per catalog
  (`/archive`, `/library`, `/photo`, `/object`). 20 results/page, paginated
  `?page=N`. Results are server-rendered `<li class="card">` blocks — no JS
  rendering needed; parseable with regex. Detail pages live at
  `/<catalog>/<GUID>` with a small Metadata table.
- **Wildcard/AND/OR/quotes supported**; default connector is OR, so multi-word
  names (`community college`, `St. Paul`, `Orchard Farm`) return very noisy
  sets — the distinctive-token per-school query is the useful one.
- **Advanced Search gotcha:** field-specific queries
  (`/AdvancedSearch?searchcat_2|5|12=...` for Title / Object Name /
  Description) return "No results" via plain GET even with session cookies and
  `actionType=Search`. The form likely needs the site's JS flow. Not a
  blocker — the keyword index proved more useful anyway.
- **Keyword-index caveat (important):** the global `yearbook` search does NOT
  index all Scope&Content text — archive record **2021.05.16 (Assumption HS
  "The Clarion" yearbooks 1950–53)** never appears in the `yearbook` result
  set; it surfaced only via the per-school `Assumption` query. The 82-record
  `yearbook` enumeration is therefore a floor, not a ceiling — the ~60
  per-school queries are what make coverage trustworthy.

## Method applied

1. Global `yearbook` keyword enumeration → 82 records, all fetched and saved
   (`data/archive_indexes/scchs.json`).
2. Cross-cutting supplements: `classbook` (8), `annual` (89→60 fetched),
   `Charlemo` (24), `Charmelo` (1).
3. ~60 per-school/per-place queries, one distinctive token each, covering all
   52 in-scope seed rows (60 fetched max per noisy term).
4. Detail pages pulled for ambiguous records (2024.21.018, 2007.041.01,
   2021.18.01, 900.0002.199, Lincoln/Franklin/Military College items).

## What SCCHS actually holds — mostly NON-seed schools

SCCHS's yearbook holdings cluster on St. Charles **city** schools that are
absent from `schools_master.json` entirely:

- **St. Charles High School "The Charlemo"** — the society's flagship
  yearbook run: 1921, 1922, 1923, 1927, 1934 ("Charmelo"), 1951, 1952, 1953,
  1954, 1955, 1972, 1973, 1981, 1982, 1983, 1986, 1989, 1990, 1991, 1996,
  1998, 2008, 2009, plus one undated volume (2021.18.01). ~23 volumes.
- **Lincoln School, St. Charles** — classbook/yearbook run 1966-67, 1969,
  1970-71, 1971-72, 1972-73, 1973-74, 1974-75, 1976, 1976-77, 1977-78
  (collection 2024.21). **DECOY WARNING: this is the St. Charles city
  Lincoln elementary — NOT ALL-349 "Lincoln School" (Normandy, 63121).**
- **St. Charles Military College** — yearbooks 1904, 1905, 1906 (x2), 1907 (x2).
- **Franklin School/HS, St. Charles** (the city's Black school) — class
  photos 1952-53 & 1954-55, "yearbook photos" 1949, reunion programs
  (collection 2023.33), commencement-exercise file 1935–1955 (250.001.028).
  Photos/documents, not yearbook volumes.
- **St. Charles Borromeo School** — 8th-grade graduation photo 1942 only.
- **Central Wesleyan College "The Pulse"** (Warrenton) — several Library vols.
- **University library copies** — SLU "The Archive", WashU "The Hatchet",
  Central College "Ragout" — reference copies, not custody of those schools.
- **Non-school "yearbook" hits** — Missouri River Otters hockey, Liberty
  Grove/St. Charles Co. Extension Clubs (homemaker clubs), Dept. of
  Superintendence. Exclude all.
- **Unidentified:** 2007.041.01 "Yearbook" dated 1942 (no school named);
  2024.21.018 "Yearbook for the year 1980-1981" (in the Lincoln/Charlemo
  donor collection 2024.21 — probably a St. Charles city school, unverifiable);
  vertical file 900.0002.199 ("Schools" collection) lists "Original 1967
  yearbook" + a Thanksgiving-mass invitation — likely a Catholic parish
  school, school not named.

## Seed-row findings

- **ALL-647 Assumption School (O'Fallon)** — the ONLY seed match:
  "The Clarion" yearbooks of Assumption High School, O'Fallon — one catalog
  record (2021.05.16) holding four volumes, **1950, 1951, 1952, 1953** —
  written as four `physical_only` rows. The HS is this parish school's
  high-school department (Track A notes: parochial HS from ~1918, building
  dedicated 1955, closed 1962 → St. Dominic HS).
- **Adjacent materials, no yearbooks:** ALL-562 Francis Howell HS (graduation
  announcements, classes of 1925/1939–43/1946–49, acc. 2024.20.004–.015 —
  SCCHS demonstrably collects FHHS material but holds no FHHS yearbook);
  ALL-603 Holt/Wentzville (Wentzville vertical file 900.0001.102); ALL-566
  Bryan Middle (named in 900.0002.019); ALL-571 Independence (Library
  "Independence School Record" + schoolhouse photo — predecessor site);
  ALL-624/628 Dardenne-area Emge (O'Fallon history files 2023.06.x);
  ALL-547 Lindenwood (commencement programs 1938/1958 only).
- **All other 45 in-scope seed rows:** nothing school-specific — `not_found`
  with `year:"all"`. Most are suburban FHSD/WSD/FZSD elementaries and middle
  schools opened post-1990 (SCCHS's collecting is pre-1960s-weighted), plus
  the Defiance/New Melle one-room-school rows and small parochial/privates.
- Skipped per contract: 7 `administrative_district_only` rows
  (ALL-578/579/585/592/614/615/616) and ALL-646 Woodlawn Seminary
  (`out_of_scope_closed_before_1949`) — though SCCHS does hold a Woodlawn
  Institute "Annual Announcement" print (2023.06.146) for the record.

## Suggested `data/digital_archives.json` updates for `scchs`

- `coverage_status` → `"index_enumerated (yearbook-keyword enumeration across all four catalogs — 82 records — plus ~60 per-school queries covering all 52 in-scope St. Charles County seed rows; keyword index is NOT exhaustive of record text, so per-school sweep was required)"`
- `covered_schools` → `["ALL-647"]`
- `enumeration_notes` addition: server-rendered search at
  `/Search?search_criteria=<q>&page=N` works with curl+browser UA; Advanced
  Search fields don't execute via plain GET; per-school keyword search is
  REQUIRED (keyword index misses Scope&Content hits like the Assumption find).
- `digital_yearbooks` stays `none_found` — no scans; PastPerfect records are
  catalog entries for physical objects (access 101 S. Main St., St. Charles;
  contact@scchs.org listed on site — human follow-up for volume-level detail).

## Follow-ups for a human / coordinator

- The ~23-volume Charlemo run + 10-volume Lincoln classbook run + Assumption
  Clarion vols are physical-only in closed stacks — prime scan candidates if
  the project can partner with SCCHS directly.
- If St. Charles city schools matter to RECA claimants, `schools_master.json`
  has no rows for St. Charles HS, Lincoln School (St. Charles), Franklin
  School/HS, or St. Charles Military College — coordinator decision whether
  to add seed rows so these holdings get registry rows.
- ALL-592/590 Washington SD/HS (Franklin Co.) was left out of the 633xx
  subset; SCCHS does hold a "Washington, Missouri 1839-1989" history book but
  no yearbook — non-blocking.
