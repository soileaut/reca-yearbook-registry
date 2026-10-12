# Track B notes — north_county_municipal_libs

Surveyed 2026-10-12 by `track-b-north_county_municipal_libs`.

## Orientation verdict: per-municipality

The assigned municipalities were checked against the Municipal Library
Consortium (MLC) of St. Louis County roster — the only independent municipal
library districts in the county are Brentwood, Ferguson, Kirkwood, Maplewood,
Richmond Heights, Rock Hill, University City, Valley Park, Webster Groves
(<https://mlc-stl.org/find-your-library/>) — and against the SLCL branch map.

| Municipality | Independent library? | Notes |
|---|---|---|
| **Ferguson** | **YES** | Ferguson Municipal Public Library District, 35 N. Florissant Rd. — own taxing district, MLC member ("MLC-FE"), catalog on shared MLC Aspen Discovery (`mlc-fe.modiscovery.org`). Surveyed — see below. |
| Florissant | no | SLCL Florissant Valley / Jamestown Bluffs branches |
| Berkeley | no | SLCL (Natural Bridge / Florissant Valley nearest) |
| Jennings | no | SLCL Jennings branch |
| Normandy | no | SLCL Natural Bridge branch |
| Bellefontaine Neighbors | no | SLCL (Jamestown Bluffs / Lewis & Clark) |
| Black Jack | no | SLCL Jamestown Bluffs |
| Spanish Lake | no | unincorporated; SLCL Prairie Commons / Jamestown Bluffs |
| Kinloch | no | no library in city; SLCL county service |
| Wellston | no | 0 libraries per SLCL homefacts; nominal SLCL county service |
| Pine Lawn | no | no library in city; SLCL county service |
| Moline Acres | no | SLCL Lewis & Clark |
| Riverview | no | SLCL Lewis & Clark |

So exactly **one** north-county municipality operates an independent library:
Ferguson.

## Ferguson Municipal Public Library District — enumeration

The catalog is a shared Aspen Discovery union catalog for all 9 MLC libraries;
Ferguson-held copies were isolated with the `available_at` facet
`"MLC - Ferguson Municipal Public Library District"` (raw query results saved in
`data/archive_indexes/north_county_municipal_libs.json`).

Exhaustive yearbook probes, all scoped to Ferguson holdings:

- **Subject "yearbooks"** → 1 item, the Allyson Condie novel *Yearbook*.
- **Keyword "yearbook"** → 16 items, all fiction/graphic novels/media
  (*Gotham Academy: Yearbook*, *Bakuman*, *African American yearbook*, etc.).
  The only local-history-adjacent hit is *Let's go cruizin' again: remembering
  more North County "happy days" 1950s–1970s* — a memoir/photo book, not a
  yearbook.
- **Local call-number "yearbook"** → same 16 items.
- **Keyword "McCluer OR Ferguson yearbook"** → same 16 items.
- **Subject "Ferguson (Mo.)"** → 27 items of genuine Ferguson local history
  (city histories, charters, budgets, *Ferguson: a city remembered*) — **no
  school yearbooks or school-district publications**.
- **School-name searches** (McCluer High School, Ferguson High School,
  Ferguson Middle/Junior High, Vogt Junior High, Normandy High School) → zero
  yearbook holdings.
- **Library website** (`ferguson.lib.mo.us` / Aspen site pages `/fedigital`,
  `/feresearch`, `/feservices`, `/ferc`, `/feabout`) → no local-history room
  page, no digital collections, no yearbook collection; only cardholder
  genealogy databases (Ancestry in-library, etc.) which are out of scope per
  the project policy block.

**Conclusion:** Ferguson PL holds no school yearbooks — not digitized, and no
cataloged physical yearbook holdings. A small uncataloged local-history shelf
cannot be ruled out from web evidence alone, but nothing on the website or in
the catalog indicates one; if the library accepts donations, yearbooks would
be worth an in-person ask later (out of scope for this web-only survey).

### Registry rows written

`yearbook_registry_north_county_municipal_libs.json`: 19 rows, `year: "all"`,
`digitized_status: "not_found"` — one per schools_master row physically in
Ferguson city (ZIP 63135), since the exhaustive catalog probes cover every
school yearbook the library could hold. High schools and the Florissant
Valley college rows get `existence_status: likely_exists` /
`existence_confidence: probable` (standard-era yearbook programs, inferred);
elementary/junior-high rows get `unknown`/`unknown`.

### Dead ends / decoys

- `mcl-fe.modiscovery.org` (as spelled in a search-result snippet) is an
  invalid host — correct host is `mlc-fe.modiscovery.org`.
- Both `ferguson.lib.mo.us` and `mlc-fe.modiscovery.org` sit behind **Anubis
  proof-of-work anti-bot**: plain curl/HTTP is rejected; enumeration was done
  by driving the session's real Chrome over the CDP endpoint.
- "The crest: 1930" appears in unscoped MLC yearbook searches — it is a
  Galena Consolidated Schools (Stone County, MO) volume held elsewhere in the
  consortium, **not** a Ferguson school; do not fuzzy-match it.
- Wayback Machine was rate-limiting this VM's IP during the survey, so
  archived copies of the Ferguson PL site were not checked.

## Suggested `data/digital_archives.json` update for `north_county_municipal_libs`

- `coverage_status`: `"verified_no_holdings"` (or equivalent negative-complete
  status) — 12 of 13 assigned municipalities have no independent library (SLCL
  territory, already covered by slcl_digital/slcl_physical); the one
  independent library, Ferguson Municipal Public Library District, was
  exhaustively searched and holds **zero** school yearbooks in catalog or
  digital collections.
- `covered_schools`: the 19 Ferguson-ZIP-63135 school_ids in the registry file
  (all `not_found` at this surface).
- The prior `municipal_libs_unverified` note listing "Ferguson" among
  "remaining unverified" can now be marked verified-negative for Ferguson.
