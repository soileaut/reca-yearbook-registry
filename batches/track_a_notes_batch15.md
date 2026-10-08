# Track A Notes — Batch 15 (ZIP 63135, Ferguson)

Date of research: 2026-10-08. Output: `batches/schools_batch15.json` — 15 rows,
count unchanged (no rows merged or split; two likely duplicates flagged for the
coordinator — see below).

Batch 15 is all-Ferguson (63135). The single richest source turned out to be a
pair of documents about the older schools: the 1984 **National Register
nomination for Ferguson School–Central School** (NPS 84002706, hosted on
nara-media.s3.amazonaws.com) and the **1948 Ferguson High School "Crest"
yearbook history page on e-yearbook.com**, plus an STLPR feature drawing on the
Ferguson Historical Society's 1976 *Ferguson: A City and Its People*.

## Confirmed vs. unknown

**Fully confirmed (opened + closed/status with citations):**
- `ALL-420` Vogt High School — opened **1930** (1948 Crest yearbook text +
  AS&U + STLPR all say 1930; seed's "Sept. 9, 1931" is likely the dedication or
  the Ittner building's completion date — the first Crest yearbook is 1931).
  Closed 1939 when students moved to the new Ferguson High at 701 January Ave.
- `ALL-421` Vogt Junior High — opened 1939 (same building, converted when
  Ferguson High opened).
- `ALL-424` Central School — opened **1880** (NRHP nom, STLPR, PD Journal);
  still open as Central Primary. Oldest school in north St. Louis County;
  NRHP-listed 1984.
- `ALL-428` Vernon School (Ferguson) — built **1885** for Black children,
  grades 1-8; new brick Vernon built 1927 at the district's western edge;
  remained all-Black until it **closed in 1967** (STLPR/Ferguson Historical
  Society). Distinct from Kinloch's Vernon School (ALL-396/397, batch 13) —
  already paired in `schools_seed_deduped_review_needed.json`.
- `ALL-430` Lee-Hamilton Intermediate — established **1950**, named for Arthur
  Lee and Sarah Hamilton (official FFSD family handbook). Still open, grades 3-5.
- `ALL-438` McCluer Junior High — opened **1957** (probable: Wikipedia is
  internally inconsistent, "1957" in infobox/history vs. "1958" in pre-history
  line); converted to McCluer Senior High in **1962** when Ferguson High closed.
  Same building still open as McCluer HS (ALL-111, batch 5) — successor
  confirmed.
- `ALL-440` STEAM Academy at McCluer South-Berkeley — opened **Aug 15, 2019**
  (Flo Valley News), per the Oct 10, 2018 board vote converting MSB to a STEAM
  magnet. Same building (est. Jan 2004) as ALL-113 (batch 5).
- `ALL-441` North County Technical High School — refined seed's "1960s" to
  **1968** (SSD official history at appliedtech.edu; also "North County
  Technical High School" in the Liddell desegregation opinions). Still open as
  North Tech, 1700 Derhake Rd, Florissant 63033.
- `ALL-443/444/445` STLCC-Florissant Valley lineage — district established by
  April 1962 referendum (ERIC case study ED021558); classes Jan 1963; permanent
  Pershall Rd campus built 1966 / opened 1967-68. Still open.
- `ALL-419` Ferguson Middle School — currently open. See below for the date
  nuance.
- `ALL-425` Griffith — still open (grades 3-5). See below for the date nuance.
- `ALL-432` Johnson-Wabash 6th Grade Center — opened ~**2019** (probable) under
  the 2018 restructuring; still open.

**Left unknown:**
- `ALL-421` Vogt JH closed_year — seed says 1981 (conversion to Vogt
  Elementary); no online source confirms the year. The building's lineage
  continued until Vogt Elementary closed at the end of 2018-19 (Oct 2018 board
  vote — confirmed).
- `ALL-425` Griffith opened_year — kept seed's 1927 at `probable`: it traces to
  the district-compiled *History of Ferguson* (1975), not available online;
  existence confirmed by a Jan 1967 Post-Dispatch tornado photo. Likely named
  for superintendent W. W. Griffith (1902-1930) — inference only.
- `ALL-419` Ferguson Middle — set opened 1962 `probable` (the year the 1939
  building converted from high school to junior high); the exact year it was
  renamed "Ferguson Middle School" is undocumented online but is ≤1989 (a 1989
  yearbook exists under that name; the school rebuilt after a 1988 fire).
- `ALL-444/445` closed_year — set `unknown` because the premise is wrong: the
  Junior College District never closed; it continues today as STLCC (seed's
  "1965" is the bond-issue year for the permanent campuses).
- `ALL-448` St. Peter School — everything unknown; unresolved row (below).

## Data-quality flags

- **`ALL-444` ≈ `ALL-445` are the same entity** — "St. Louis County Junior
  College - Florissant Valley" and "STLCC-FV - Former St. Louis County Junior
  College" both describe the Junior College District of St. Louis-St. Louis
  County era (1962/63 → STLCC). And **`ALL-443` is a publications-search alias
  for the same campus** already researched in the pilot as `63147-11`. All
  three kept per the no-silent-merge rule; recommend collapsing at aggregation.
- **`ALL-448` "St. Peter School" appears misattributed.** No Catholic school by
  that name exists in Ferguson in NCES PSS or archdiocesan directories.
  Ferguson's actual Catholic schools were Our Lady of Guadalupe (~1955-2025)
  and Blessed Teresa of Calcutta (school closed ~2010). Possible intended
  referents: St. Peter's Catholic School, Kirkwood (63122), or St. Peter's UCC
  in Ferguson — a Protestant congregation (1425 Stein Rd) that historically ran
  a school at its *city* location (St. Louis Ave & Warne, 1906), not in 63135.
  `entity_type: ambiguous_unresolved`.
- **`ALL-441` seed operator is wrong**: North County Tech was a Special School
  District of St. Louis County school, not FFSD — corrected in output.
- **`ALL-420` Vogt seed date**: "Opened Sept. 9, 1931" conflicts with multiple
  sources saying 1930 (a 1948 primary-source yearbook included). Recorded 1930
  `confirmed`; the 1931 date noted as probable dedication/building-completion.
- **`ALL-424` conflates two buildings**: the seed's "1867 open / 1880 close"
  splices the first one-room school (1867, Wesley & N. Florissant — later moved
  to 110 S. Clark, survives as a residence) onto the 1880 Central School
  building, which is still operating. Both halves documented in notes.
- **Cross-batch dedup pointers found in this batch**: Vogt/Ferguson/McCluer
  predecessors relate to batch 14 rows (ALL-416 Ferguson HS, ALL-417 January
  Ave campus, ALL-418 Ferguson JH, ALL-406 Johnson-Wabash Elementary, ALL-404
  FFSD district, ALL-450/ALL-453 district rows in batch 16); MSB relates to
  ALL-113 (batch 5); McCluer HS is ALL-111 (batch 5); Kinloch Vernon is
  ALL-396/397 (batch 13). Successor links recorded where determinable.
- **Lineage vs. entity dates**: several rows describe one physical building
  under successive names (Vogt: HS→JH→Elementary, 1930-2019; 701 January:
  HS→JH→Middle, 1939-present; 1896 S. New Florissant: JH→HS, 1957-present).
  `opened_year` records when the named entity/phase began; building dates are
  in `notes`. A future cleanup pass may want building-level records.

## Useful sources for reuse (Ferguson/North County)

- **NARA-hosted NRHP nominations** (`nara-media.s3.amazonaws.com/electronic-records/rg-079/NPS_MO/`)
  — the Central School nomination has construction dates, board minutes
  citations, and county-directory evidence. Other NRHP-listed SLPS/FFSD
  schools likely have equally rich nominations.
- **e-yearbook.com "history" pages** — the 1948 Ferguson HS Crest yearbook's
  institutional history gave superintendent names/dates that explain school
  namesakes (Griffith, McCluer, Vogt) and settled the Vogt 1930-vs-1931 question.
- **STLPR (stlpr.org)** — Mary Delach Leonard's 2015 Ferguson history feature
  documents Vernon School end-to-end (1885 → 1927 brick → closed 1967).
- **Living New Deal** — building-level dates for WPA schools (Ferguson
  Middle/High, 1939).
- **FFSD board restructuring coverage** — STLPR Oct 2018 vote + AS&U May 2019
  closure story pin Vogt/Airport/Mark Twain closures, the 6th-grade-center
  conversions, and the MSB→STEAM conversion; fergflor.org's April 2025 post
  documents the coming 2027-28 K-5/6-8/9-12 restructuring.
- **Official school handbooks on finalsite resources** — FFSD family handbooks
  carry "established in YYYY" statements (Lee-Hamilton 1950).
- **ERIC** — ED021558 documents the junior college district's 1962 formation.
- **Special School District history** (appliedtech.edu/our-history) — North
  Tech 1968, South Tech 1967.

## Process friction

- **Junior-high/middle-school rename dates are invisible online.** Both Vogt
  JH→Elementary (~1981?) and Ferguson JH→Middle (≤1989) are undocumented via
  web search; they live in FFSD board minutes and the print *History of
  Ferguson* (1975) held at Ferguson Public Library — a recommended human
  follow-up / archive visit.
- **Parochial-school data is thin.** For ALL-448 there is no authoritative
  online list of defunct Archdiocese parish schools; resolution needs the
  archdiocesan archives or the seed author's intent.
- **NCES-derived closure years skew** (same as pilot): publicschoolreview shows
  Vogt "Closed 2020" for the actual 2019 closure.
- **STLCC naming**: campuses were renamed to the "STLCC-Campus" format in 1976,
  which makes pre-1976 campus records appear under different names — worth a
  note for Track B when searching yearbook catalogs.
- **Recommended human follow-ups**: FFSD Records/History of Ferguson for the
  Vogt JH conversion year and Griffith 1927 verification; Archdiocese archives
  for St. Peter; seed author clarification for ALL-443/444/445 (one entity,
  three rows) and ALL-448.
