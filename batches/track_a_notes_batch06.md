# Track A Notes — Batch 06 (ZIPs 63042/63043: Ferguson–Florissant north, Maryland Heights/Pattonville)

Date of research: 2026-10-08. Output: `schools_batch06.json` — 15 rows for 15 seed rows
(count unchanged; no merges or splits). `reca_scope_status` intentionally absent per
schema (computed later by `compute_reca_scope.py`).

## Confirmed vs. unknown

**Strong confirmations via the Pattonville district's own history pages**
(`psdr3.org/about/history`, `psdr3.org/about/history/by-the-years`, and
`sites.google.com/psdr3.org/pattonvillehistory`) — this source is exceptionally
detailed (exact open/dedication dates, first principals, building costs) and resolved
7 of 15 rows:

- `ALL-148` Pattonville High School — students moved in March 17, 1936 at 11055
  St. Charles Rock Rd; moved to current Creve Coeur Mill Rd campus 1971 (dedicated
  Jan. 7, 1973). Still open. Yearbook: *Echo*.
- `ALL-149` PHS Original Campus — same dates; the institution's relocation is the
  "closure." Recorded successor as ALL-148 (same school, new building).
- `ALL-150` Pattonville Heights MS — opened October 1966 as a 7/8 center;
  planetarium Jan. 1967 (first in a Missouri school); junior high 1971; middle
  school 1982. Still open.
- `ALL-151` Remington (now Academy of Innovation at Remington) — opened 1955 under
  Maryland Heights School District; Traditional School 1982; renamed 2024-25.
  Still open, same lineage.
- `ALL-154` Parkwood Elementary — opened 1965, dedicated Nov. 8, 1965. Open.
- `ALL-155` Rose Acres Elementary — opened 1967, dedicated Jan. 15, 1968. Open.
- `ALL-161` POSITIVE School — opened 1981-82 (124 students); moved to the closed
  Penn-Junction building 1982; now a wing of PHS. Still open.
- `ALL-162` Maryland Heights School — dedicated September 1924; became the
  district's high school; closed as a school when the Maryland Heights district
  merged into Pattonville in 1962 (students → PHS/Remington; building became the
  Pattonville Administration Building until 1995).

**Ferguson-Florissant rows resolved via St. Louis County Landmarks + NRHP + STLPR:**

- `ALL-115` "Central High School" — best read as the high-school program of
  Central School, 201 Wesley Ave, Ferguson. Two-year HS program began 1896,
  expanded to a 4-year accredited program when the school was renamed Central
  School in 1903; students transferred to the new Vogt High School in 1930
  (Central reverted to elementary in 1931). Seed's "Closed: 1950s" is wrong —
  the HS program ended ~1930-31. Successor: Vogt HS (seed row ALL-420).
- `ALL-117` Central Elementary → now **Central Primary School**, still operating
  at 201 Wesley Ave, Ferguson 63135 (PK-2). Opened 1880 in the 1877-80 Ferguson
  School building (NRHP 1984). **Announced closure for the 2027-28 restructuring**
  per FFSD board post — flagged in notes for whoever re-verifies later.

**Other rows:**

- `ALL-156` Holy Spirit Catholic School — open (NCES PSS, PK-8). Seed's 1964 is
  kept as *probable*: the site was St. Blaise Parish (founded 1961, church built
  1962), which merged with St. Lawrence + St. Mary's into Holy Spirit Parish in
  May 2004. School likely operated as St. Blaise School before 2004 — direct
  founding-year citation not found online.
- `ALL-157` DaySpring Arts & Education — founded September 1993 per its own About
  page; nonprofit 1998; current Metro Blvd building since 2015. Open.
- `ALL-158` McKelvey Elementary — opened ~1966 (probable: GBIG building record +
  district 50th-anniversary booklet). "Closed" ~2021 only as a rename: Parkway
  split it into McKelvey Primary (new building, 12657 Fee Fee Rd) and McKelvey
  Intermediate (existing building). Successor = ALL-159.
- `ALL-159` McKelvey Intermediate — began 2021-22 (probable: first appears in
  Parkway's 2021 records after the Dec. 2019 groundbreaking announcement). Open.
- `ALL-118` "McCluer South-Berkley feeder schools" — **not a school**; an
  aggregate placeholder the seed author meant to break out later. Marked
  `ambiguous_unresolved`; real Berkeley-area feeder rows already exist elsewhere
  in the dataset (ALL-385, 386, 387/388, 408, 431). See row notes.

## Data-quality flags

1. **ALL-115 wrong era + wrong location.** Seed "1950s" closure is off by ~20
   years (documented end ~1930-31), and the school is in Ferguson 63135, not the
   63042/Florissant area the seed suggests. Overlaps ALL-423/ALL-424 in other
   batches — same Central School lineage.
2. **ALL-117 wrong address/ZIP.** "12300 Old Halls Ferry Road" is not this
   school; actual is 201 Wesley Ave, Ferguson 63135.
3. **ALL-118 is a non-school aggregate row** (`ambiguous_unresolved`) — keep for
   coverage tracking, don't yearbook-search it.
4. **ALL-149 vs. ALL-148 vs. ALL-198**: three rows for one institution (original
   building, institution, current building). Kept separate per schema's
   campus-row rule; successor links recorded accordingly. Yearbook searchers
   should treat all PHS yearbooks as one series ("Echo").
5. **ALL-158/159 are a rename pair**, not two schools — McKelvey Elementary
   became McKelvey Intermediate in the same building (~2021) when McKelvey
   Primary opened nearby. McKelvey Primary itself is not in this batch's seed.
6. **ALL-156 name chronology**: "Holy Spirit" branding only dates to the 2004
   parish merger; the pre-2004 school at this site was most likely St. Blaise
   School (not independently confirmed).

## Useful sources for reuse

- **psdr3.org/about/history + sites.google.com/psdr3.org/pattonvillehistory** —
  district-authored school-by-school history with exact dates, principals,
  dedications, and closures. Should be the first stop for any Pattonville batch.
- **lv.stlouiscountymo.gov ... /st-louis-county-landmarks/ferguson/** — St. Louis
  County Landmarks entries with NR-level detail for Ferguson school buildings.
- **NRHP nominations via nara-media.s3.amazonaws.com** (NPS MO scans) — primary
  documentation incl. construction dates and school-use history.
- **stlpr.org** — 2017 FFSD historic-buildings story gives open dates for
  Central (1880) and Vogt (1930) elementaries.
- **NCES CCD/PSS lookups** — current operating status, grade bands, addresses.
- **stlgs.org/closed-catholic-churches** — St. Louis Genealogical Society table
  of closed/merged parishes; key for archdiocesan school lineage.
- **gbig.org** — building records with "year constructed"; useful corroboration
  when district history is missing (McKelvey).

## Process friction

- **Parkway School District publishes no comparable school-history page** — the
  McKelvey open/split dates needed triangulation across a building database, a
  salary listing, and a news article. Expect the same for other Parkway rows.
- **Private-school founding years** depend on NCES PSS self-reporting; Holy
  Spirit's "1964" can't be confirmed against the parish's own page, which covers
  only the 2004-merger entity.
- **Successor granularity**: seed rows for "X School" vs. "X - Original Campus"
  vs. "X - Current Campus" blur school-vs-building. I recorded building rows as
  `individual_school` with successors pointing at the institution row, and
  documented that choice in notes — coordinator may want a consistent convention.
