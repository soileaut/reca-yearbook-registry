# Track A Notes — Batch 18 (`schools_seed_batch18.json`)

Date of research: 2026-10-08. Output: `batches/schools_batch18.json` — 15 rows, one
per seed row; no rows merged or split.

This batch is really three sub-batches: six Kinloch/Lambert-airport-area rows
(63140/63145), three metro universities folded in under the "served community"
rule, and six Francis Howell R-III schools (63304).

## Confirmed vs. unknown

**Fully confirmed (opened + closed/open status with citations):**
- `ALL-544` Saint Louis University — 1818 (official SLU timeline; founded as Saint
  Louis Academy, chartered as university 1832). Still open.
- `ALL-546` Washington University in St. Louis — charter signed Feb 22, 1853 as
  "Eliot Seminary" (WashU official history). Still open.
- `ALL-547` Lindenwood University — **1832, not the seed's 1827.** Lindenwood's
  Board of Trustees officially revised the founding year in Feb 2023 after
  primary-source review (Sibley correspondence; Mary Sibley's 1833 diary).
  Recorded at the corrected 1832. Still open.
- `ALL-522` Special School District of St. Louis County — formed December 1957
  by voter referendum (SSD's own history page). Still operating. Classified
  `administrative_district_only` — it's a countywide district with seven member
  schools (Ackerman, Litzsinger, Neuwoehner HS, Northview HS, Southview,
  North Tech, South Tech), not a yearbook-producing building.
- `ALL-513` St. John the Baptist School — elementary opened September 1914,
  grade school closed May 2014 — **but see the location flag below.**
- All six Francis Howell rows — the district's own About page
  (`fhsdschools.org/about`) carries a complete opening-year timeline, so every
  row resolved cleanly:
  - `ALL-562` Francis Howell HS — 1881 (Francis Howell Institute; renamed and
    continued as FHHS from Sept 6, 1915). Still open.
  - `ALL-564` Francis Howell Central HS — **1997, not the seed's 1987**
    (opening day Aug 21, 1997, per FHC's own anniversary issue).
  - `ALL-565` Francis Howell MS — 1992 (district timeline).
  - `ALL-566` Bryan MS — 1998 (district timeline).
  - `ALL-567` Hollenbeck MS — 1970 (district timeline; oldest FHSD middle school).
  - `ALL-568` Saeger MS — 1996 (district timeline, which spells it "Seager").

**Probable:**
- `ALL-510` Kinloch School — almost certainly **Dunbar Elementary School**
  (Paul Laurence Dunbar Elementary), the only Kinloch school that closed in
  1975. Opened 1913 per St. Louis REALTORS/St. Louis Black Heritage Network
  histories (SHSMO finding aid S0638 says 1914 — kept `probable`). Closing is
  `confirmed`: 1975 in the SHSMO finding aid, and the closure mechanism is
  documented in federal court records — *United States v. State of Missouri*,
  388 F. Supp. 1058 (E.D. Mo. 1975) ordered Kinloch SD annexed to
  Ferguson-Florissant R-2 effective Feb 1, 1975 (affirmed, 515 F.2d 1365).
  Successor is Ferguson-Florissant SD at the district level (no matching
  school_id in the dataset).

**Left unknown / unresolved:**
- `ALL-527` Lambert-St. Louis International Airport Schools — `ambiguous_unresolved`,
  all fields `unknown`. No evidence any such conventional school existed. Likely
  a phantom lead gesturing at the Kinloch Park / Berkeley-area schools absorbed
  by airport expansion.
- `ALL-548` and `ALL-549` — non-entity placeholders (`administrative_district_only`).
  The seeds themselves say "do not treat this as a school" / "placeholder";
  years left `unknown` by design. `notes` lists the concrete member schools the
  placeholders cover so Track B can redirect.

## Data-quality flags

- **`ALL-513` probable location error.** No St. John the Baptist parish or school
  ever existed in the Kinloch/Florissant area. The Archdiocese of St. Louis
  school by that name is in Bevo Mill, south city (5021 Adkins Ave, 63116) —
  elementary 1914–2014. The school the seed likely *intended* for north county
  is **Our Lady of the Angels Elementary** (Holy Angels/Our Lady of the Angels
  Parish, 8122 Scott St., Kinloch, parish 1931–2002 per the St. Louis
  Genealogical Society closed-churches list). Recommend a human decide whether
  `ALL-513` should be relabeled to that school or a new row added.
- **`ALL-527` likely phantom.** Flagged in row notes; recommend collapsing into
  `ALL-549` rather than researching it as a school.
- **`ALL-548`/`ALL-549` are placeholders, not entities** — marked
  `administrative_district_only` so no yearbook search is ever aimed at them.
- **Seed date errors corrected:** `ALL-564` (1987 → 1997) and `ALL-547`
  (1827 → 1832, per the university's own official correction).
- **Unverified "Junior High" aliases** in the four FHSD middle-school seeds —
  no source confirms any of them was ever named "Junior High"; the district's
  timeline uses "Middle School" at founding for all four. Kept as search aliases
  only, marked unverified in `notes`.
- **ZIP metadata:** SLU (63103/63108), WashU (63130), and Lindenwood (St. Charles
  63301) are all outside their seed ZIPs — included under the "served community"
  rule. Kinloch High School and Vernon School are other dataset rows, not
  covered here.

## Useful sources for reuse

- **fhsdschools.org/about** — official FHSD history timeline with opening years
  for every district school. Single-page resolution for an entire district.
- **files.shsmo.org** (State Historical Society of Missouri manuscript finding
  aids) — Kinloch collections S0151, S0638, S0707 carry concrete school dates.
- **law.justia.com** — the 1975 Kinloch desegregation decisions (388 F. Supp.
  1058; 515 F.2d 1365) give exact annexation dates and successor districts.
- **stlrealtors.com Kinloch history / stlblackheritage.com** — clean
  secondary-source school chronology for Kinloch (Dunbar 1913, Vernon 1927,
  Kinloch HS 1936, Our Lady of the Angels 1952/1931).
- **stlgs.org/closed-catholic-churches** — closed-parish table with date ranges;
  good for verifying parochial schools near closed parishes.
- **School official sites** (`*.fhsdschools.org`, `slu.edu`, `washu.edu`,
  `lindenwood.edu`, `ssdmo.org`) — authoritative founding years; the
  subdomain-per-school pattern made "still open" trivially verifiable.

## Process friction

- **Placeholder rows consume real research time.** `ALL-548`/`ALL-549` (and
  `ALL-527`) required verification that they *aren't* schools — recommend a
  preprocessing flag for seed rows whose `Notes` say "do not treat as a school"
  so they're routed past Track A.
- **Location hints in seeds are unreliable.** `ALL-513`'s "Kinloch/Florissant"
  placement appears to be a wrong-community attribution; Archdiocese parish
  geography (stlgs.org table) was the fastest way to prove a negative.
- **`successor_school_id` doesn't accommodate district-level successors.** For
  `ALL-510` the documented successor is a district (Ferguson-Florissant), not a
  school_id — recorded as `unknown` with the district named in `notes`.
- **Recommended human follow-up:** Archdiocese of St. Louis Archives has a
  dedicated RECA parish-records request path (archstl.org/archives) — the
  authoritative route for confirming dates of closed north-county parish
  schools like Our Lady of the Angels. Not contacted per scope rules.
