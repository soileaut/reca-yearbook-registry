# Track B — Archdiocese of St. Louis Archives: Process Notes

Date: 2026-10-12 · Session: `track-b-archstl_archives` · Branch: `track-b/archstl_archives`
Output: `yearbook_registry_archstl_archives.json` (34 rows) + `data/archive_indexes/archstl_archives.json`
Surface: https://archstl.capacity.com/article/929015/schools-and-seminaries (same content mirrored at resources.archstl.org)

## How searchable is this archive?

**Published finding aids only — no digitized holdings, no per-school public index.** The archives'
knowledge base (a "Capacity"-platform help site, robots.txt fully permissive) has nine articles in its
Archives folder; the "Archival Materials" article is explicit: *"Finding aids are posted online as they
are created. Please contact the office to discuss materials not listed here."* So the enumerated index
is complete as far as the public site goes — every published finding aid appears as a named item.

Two important scope facts from the articles themselves:

- **Schools:** the archives "holds the records from closed archdiocesan elementary and high schools,
  including transcripts, yearbooks, photographs, etc. The extent of materials varies widely for each
  school." Real per-school record groups exist but are NOT itemized online — a records request
  (transcript-request page / archivist contact) is the only way to learn a specific school's contents.
- **Parishes:** it "takes in the records of closed parishes, which include correspondence, photographs,
  bulletins, school information, and other record types" plus the per-parish "Chancery Parish Files"
  (bulk 1940s+). Same story: held, not published.

The site's search box is a client-side "concierge" JS widget (results fetched from an external
aisoftware.com service) — no sane static endpoint to query politely. The article index is authoritative
anyway, so per-school "searches" were done as diffs against the full index + the three relevant finding
aids rather than per-school form submissions. `site:archstl.capacity.com` Google searches confirmed no
unlisted per-school articles exist.

## What the index enumerates (data/archive_indexes/archstl_archives.json)

20 items total: 15 named school/seminary collections on the Schools and Seminaries article (5 high-
school alumni directories, McBride HS alumni-club records, an interactive Catholic-HS map, 6 seminary
record groups, St. Mary's College + St. Mary's Academy in O'Fallon) plus the OCE Records finding aid
and 4 school-adjacent items from the Parishes/Agencies articles (Chancery Parish Files, closed-parish
records + Closed Parish List, African American Parishes handout, orphanages handout).

## Diff vs. the ~34-school Catholic subset of schools_master.json

**Direct index match: 1 school.**

- **ALL-449 Trinity Catholic HS** → "Trinity Catholic High School 2004-2018" (alumni class directory
  PDF — per-year rosters, not yearbooks) + five OCE admin files (merger 2001-04, correspondence,
  clippings, real-estate file, "Trinity/Open House" pubs). Its predecessors Mercy / St. Thomas Aquinas /
  Aquinas-Mercy / Rosary also have alumni directories in the index — those predecessor schools have no
  seed rows of their own; recorded under ALL-449's lineage.

**Itemized files in the OCE Records finding aid (RG 05 B 01) touching 3 more seed schools** (admin
files only, never yearbooks):

- ALL-334 Incarnate Word Academy — correspondence w/ faculty assignments 1972-1973
- ALL-018 Marygrove — "MaryGrove High School" faculty assignments 1972-1973 (evidences an on-campus
  HS program; small residential school, yearbook publication unproven)
- ALL-513 St. John the Baptist — "St. John the Baptist High School" correspondence 1972-1997 (related
  parish HS of the south-city parish; our row is the elementary — flagged, not merged)

**Closed school/parish coverage (unpublished but policy-applies): 21 rows marked `unknown`.**
The archives' mandate covers exactly these, so record groups plausibly exist — digitized_status
`unknown` rather than `not_found` because a records request could well return yearbooks. 17 rows are
closed-school/closed-parish cases: ALL-009, ALL-011, ALL-046, ALL-047, ALL-048, ALL-049, ALL-050,
ALL-056, ALL-080, ALL-108, ALL-293, ALL-335, ALL-366, ALL-398, ALL-448, ALL-482, ALL-483 (the Closed
Parish List gives the per-parish closure evidence cited in each row). 4 more rows are `unknown` with
itemized admin files but no yearbooks: ALL-449, ALL-334, ALL-018, ALL-513.

**Clean `not_found`: 13 rows.** Operating schools whose records stay local (ALL-005, 007, 008, 012,
013, 014, 156, 368, 576, 577, 647) plus out-of-mandate entities (ALL-339 Normandy HS Eden campus —
Eden is a UCC seminary, not archdiocesan; ALL-544 SLU — Jesuit university with its own archives).

## Decoys / traps hit

- **"Loretto Academy"**: KC Public Library holds "Loretto Academy High School Yearbook" volumes —
  that's the Sisters-of-Loretto school in KANSAS CITY, not our 3407 Lafayette Ave St. Louis academy
  (closed ~1952). St. Louis identity confirmed via MoHistory class-of-1932 photo + Nerinx Hall's
  "Loretto Project Packets" (likely alternative custodian — Loretto records stayed with the order).
- **"St. Vincent High School"** in the OCE finding aid (1972-2008) is ambiguous vs. St. Vincent
  (DePaul) HS in Perryville MO — NOT assumed to be ALL-366 St. Vincent Home for Children (Normandy).
- **"Sacred Heart"**: the closed-parish list's "Sacred Heart of Jesus - St. Louis City, 1871-1978" is
  a different (suppressed) parish than ALL-005's Florissant school.
- **"Trinity"**: St. Vincent-related OCE files similarly kept separate; no silent merges anywhere.
- ALL-448 "St. Peter School" is an unresolved/misattributed seed row — searched, nothing anywhere.
- ALL-056 "Academy at St. Rose Philippine Duchesne" (archdiocesan special-ed school) is NOT the All
  Saints Academy campus (ALL-048/ALL-108) — kept distinct per schools_master.

## Recommended update for data/digital_archives.json (archstl_archives)

- `coverage_status`: `"index_enumerated (published finding aids fully enumerated — 20 school-relevant items across 3 KB articles; 1 direct seed match (Trinity Catholic alumni directory + OCE files). Real per-school record groups for closed archdiocesan schools exist but are NOT published online — remaining parish rows need a records request, not more web searching)"`
- `covered_schools`: `["ALL-018", "ALL-334", "ALL-449", "ALL-513"]` (schools with any itemized holding;
  the 17 `unknown` rows are "policy plausibly applies, contents unpublished" — coordinator's call whether
  to include them)
- `enumeration_method`: `"browse_index"`
- `digital_yearbooks`: stays `"none_found"` (alumni-directory PDFs exist online but no yearbooks)
- Worth adding to `notes`: "St. Mary's Academy in O'Fallon (1964-2013, full yearbook run per finding
  aid) and the five Trinity-lineage alumni directories cover non-seed schools; Sisters of Loretto /
  Nerinx Hall is the likelier custodian for ALL-335 Loretto Academy."

## Recommended human follow-ups

- One archives records request would settle 17 schools at once: ask which closed-school/closed-parish
  record groups contain yearbooks (St. Sabina, St. Ferdinand, OLF, St. Rose PD, St. Thomas Apostle,
  St. Christopher, St. Angela Merici, Holy Trinity St. Ann, OLotA Kinloch, OL Good Counsel, St. Jerome,
  Holy Spirit/St. Blaise, StJB elementary, Loretto Academy, Academy at SRPD, Trinity Catholic,
  St. Vincent Home). Per guardrails I did not submit the contact form myself.
