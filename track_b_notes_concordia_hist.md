# Track B notes — Concordia Historical Institute (concordia_hist)

Date: 2026-10-12 · Worker: track-b-concordia_hist · Branch: track-b/concordia_hist

## Surface

- ArchivesSpace PUI at `https://concordiahistoricalinstitute.libraryhost.com/` (LCMS archives,
  804 Seminary Place, Saint Louis). Physical-use archive; **nothing is digitized** in this
  interface (no linked digital objects found for any relevant holding).
- `robots.txt` = `Allow: /` with `Crawl-delay: 10` — all requests paced ≥10 s.

## What worked (enumeration-first)

1. **Subject index `subjects/960` "School yearbooks"** — the authoritative enumeration of every
   yearbook-holding series in the repository: 7 series total, only 3 in Missouri (all under the
   Lutheran High School Association (LAHE) deposit inside `Library. Geographic Collection.
   Missouri. Saint Louis`):
   - `archival_objects/62754` — LHS (original/"Central"), **The Crusader** 1949–1964:
     1949, 1951–1957 (2 copies each), 1959, 1960, 1962, 1963, 1964
   - `archival_objects/62755` — **LHS North, The Crusader** 1965–1974: 1965, 1967, 1968, 1969,
     1970, 1972, 1974 (the coordinator-pre-confirmed holding; per-year rows written)
   - `archival_objects/62756` — LHS South, **The Lance** 1960–1989 (complete run per catalog)
   - Decoys (non-MO): Blue and Gold Annual 1918–1950 (Luther Institute, Chicago, ao 102586);
     The Shield 1954–1982 (Chicago LHS, ao 3175); The Citadel 1958–1973 (LHS, Racine WI, ao 9706);
     The Pioneer and The Concordian 1915–1956 (Concordia College, Fort Wayne IN, ao 5137).
2. **`/tree/root` JSON** for the two Missouri geographic collections pulled the full top-level
   node lists: `resources/3340` (Saint Louis, 97 nodes) and `resources/3339` (Missouri, 92 nodes).
   Relevant nodes found and recorded in `data/archive_indexes/concordia_hist.json`.
3. **Targeted keyword searches** per seed school (Salem, Hope/Grace, Messiah, Weldon, New Melle,
   River Roads, Atonement, Lutheran High) — all returned via server-rendered `/search` pages.

## What did NOT work

- `/tree/node` and `/tree/waypoint` endpoints return **HTTP 500** server-side — deeper series
  expansion is broken. `node_from_root` returns only stubs. Compensated with keyword searches.
- Resource PDF endpoints 406/404. Per-collection `/search` sub-pages return a bare redirect.
- Keyword search occasionally returns a 220-byte "You are being redirected" page (transient —
  retry after a longer pause worked).

## Findings per seed school (9 rows)

| school_id | result |
|---|---|
| ALL-651 (LHS North — see anomaly) | **FOUND**: 7 physical volumes 1965–1974 (AO 62755) |
| ALL-016 Atonement (Florissant, ELCA) | not_found — no deposit; Atonement AOs are non-MO decoys (Racine WI etc.) |
| ALL-051 / ALL-052 Salem (Black Jack) | not_found — congregational records only (coll. 2546) |
| ALL-295 Hope (St. Ann) | not_found — congregational items in Saint Ann geo node only |
| ALL-484 Grace Chapel (Bellefontaine Neighbors) | not_found — official acts/microfilm (coll. 3238) |
| ALL-575 Messiah (Weldon Spring) | not_found — no Weldon Spring deposit; "Messiah (Saint Louis)" coll. 4065 is a different city congregation |
| ALL-596 New Melle Parochial (ambiguous) | not_found — St. Paul New Melle geo node + unprocessed Sunday School maps accession only |
| ALL-598 St. Paul (New Melle) | not_found — same deposits as ALL-596 |
| 63147-04 River Roads (StL city) | not_found — school's own records coll. 2166 (1980-89 admin files) + 1994 brochure, no yearbook |

## ANOMALY — ALL-651 and the missing LHS seed rows

- `data/digital_archives.json` lists `concordia_hist` `covered_schools: ["ALL-651"]`, and the
  coordinator prompt maps that id to LHS North — **but schools_master.json has no ALL-651**
  (max ALL id = 650). Sibling worker (slcl_digital) hit the same stale reference
  (ALL-651..655). Registry rows here use school_id `ALL-651` per the coordinator's stated
  intent; merge tooling should treat it as a dangling reference to **LHS North** and either
  create the missing seed row or remap.
- **LHS Central, LHS North, and LHS South have no seed rows at all** — yet CHI holds ~50
  yearbook volumes for them (1949–1989), all three campuses in RECA-relevant geography
  (Spanish Lake 63138, Lemay/Affton 63123/63125, city). LHS St. Charles administrative records
  also exist (resources 477, 2394, 2906, 2907, 3335, 3975). Recommend the coordinator add seed
  rows for the three LAHE high schools; if added, the South (30 vols) and Central (15 vols)
  series listed in `data/archive_indexes/concordia_hist.json` become immediately row-able.
- All elementary seed schools check out as congregational-records-only at CHI; LCMS grade
  schools of this era rarely published yearbooks, so `not_found` here is expected, not a gap.

## Suggested data/digital_archives.json changes

- `coverage_status` → `"index_enumerated (School yearbooks subject index fully enumerated — 7 series, 3 Missouri; Missouri geographic collection top-level indexes pulled; deeper series expansion blocked by ArchivesSpace /tree 500s)"`
- `covered_schools` → `["ALL-651"]` is accurate ONLY as LHS North; recommend keeping it and
  flagging the missing seed row (see anomaly). No additional seed school has CHI holdings.
- Consider noting `access: physical_only` already correct; `enumeration_method: browse_index` correct.
