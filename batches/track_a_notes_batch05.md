# Track A Notes — Batch 05 (ZIPs 63033 / 63034 / 63042)

Date of research: 2026-10-08. Output: `batches/schools_batch05.json` (15 rows —
one per seed row, count unchanged; no merges or splits). `reca_scope_status`
left absent per schema — computed downstream.

## Confirmed vs. unknown

**Fully confirmed (opened + closed, or confirmed still-open):**
- `ALL-076` Lindenwood Florissant/North County Center — opened Jan 2006
  (Lindenwood site director quoted in Catholic Review/archbalt.org), gone from
  the 2022-23 catalog locations list → closed ~2022 (probable). Seed's "opened
  2019" was wrong by 13 years.
- `ALL-080` St. Angela Merici School — opened Sept 1965 (Ursuline Sisters,
  parish's own history page), closed end of 2016-17 school year (Archbishop
  Carlson approved closure May 2017).
- `ALL-091` Arrowpoint Elementary — opened 2004 (architect project page,
  "Completion Date 08/2004"; flovalleynews Dec 2006: "opened two years ago").
- `ALL-094` Jana Elementary — opened 1970 (Post-Dispatch correction note; AP),
  closed Oct 2022 after radioactive contamination found in the Coldwater Creek
  floodplain; permanent closure confirmed March 2023; building repurposed 2024
  as the HSD Logistics Center. This is the RECA-relevant closure of the batch.
- `ALL-108` All Saints Academy – St. Rose campus — opened 2018 (academy
  founding), closed for 2023-24 (St. Louis Review, June 2023; archstl.org
  marks the campus "CLOSED").
- `ALL-113` McCluer South-Berkeley — opened January 2004 (Wikipedia),
  still open as the STEAM Academy magnet since the 2018-19 redistricting.
  Seed's "Opened 1976" is wrong — that's the Berkeley/Kinloch merger era.
- `ALL-114` Berkeley High School — closed December 2003 (Lambert airport
  expansion), directly succeeded by `ALL-113` in January 2004. Opened 1937
  (probable): Berkeley district formed 1937 and renamed the just-opened
  Kinloch High School.

**Probable:**
- `ALL-073` Prigge/Larimore — rural district joined Hazelwood July 29, 1951
  (Franzwa 1977, quoted at pipes.family); lineage continues as Larimore
  Elementary (`ALL-464`). Founding year unknown (multiple Prigge schoolhouses
  on the 1927 district map); the Prigge→Larimore rename date is not online.
- `ALL-075` Twillman — school's own site claims lineage "Since 1927"
  (probable; matches `ALL-467` "Twillman School - 1928 Building"); never
  closed, continues as Twillman Elementary (`ALL-465`).
- `ALL-111` McCluer High — 1957 probable (Wikipedia infobox says 1957, article
  text says "opened in 1958"; became senior high 1962 when Ferguson High
  closed). Still open.
- `ALL-079` OLTC Institute — still operating (live site, Niche listing);
  no founding date found anywhere.

**Left unknown:**
- `opened_year` for `ALL-073` (pre-1910 rural district), `ALL-077` Barrington,
  `ALL-078` North Middle, `ALL-090` Southeast Middle (predecessor junior highs
  predate the 2007 buildings and 2002 junior-high→middle-school renames, but
  no dedication/opening dates surfaced), and `ALL-104` Oasis Institute.

## Data-quality flags (labeled)

- **PHANTOM:** `ALL-104` "Oasis Institute" — no K-12 school by that name exists
  in the Florissant area in any directory or search. Only hit is the senior
  lifelong-learning nonprofit in St. Ann (oasisnet.org). Recommend asking the
  seed compiler for this row's source. Set `entity_type: ambiguous_unresolved`.
- **SEED DATE ERRORS:** `ALL-076` opened 2006 not 2019; `ALL-113` opened
  Jan 2004 not 1976 (1976 ≈ the court-ordered Berkeley/Kinloch annexation).
- **"CLOSED 1950s?" MISREADS:** `ALL-073` and `ALL-075` were never closed —
  their *districts* merged into Hazelwood 1949-51 while the schools continued.
  Same pattern likely affects other rural-predecessor rows in other batches.
- **CROSS-BATCH DUPLICATES (same real-world entity, different row_ids):**
  `ALL-073` = `ALL-025`/`ALL-096`/`ALL-251`; `ALL-075` = `ALL-101`/`ALL-255`
  (and ALL-466/467 are its buildings); `ALL-108` = `ALL-048`/`ALL-135`;
  `ALL-080` = `ALL-110`/`ALL-137`/`ALL-214`/`ALL-447`; `ALL-094` = `ALL-121`;
  `ALL-077` = `ALL-122` (+`ALL-081` "predecessor"); `ALL-078` = `ALL-123`
  (+`ALL-082`); `ALL-090` = `ALL-463`; `ALL-091` = `ALL-468`;
  `ALL-111` = `ALL-412`/`ALL-437`/`ALL-516`/`ALL-541` (+`ALL-116` "Original");
  `ALL-113` = `ALL-382`/`ALL-414`/`ALL-439`/`ALL-517` (+`ALL-440` STEAM
  Academy); `ALL-114` = `ALL-378`/`ALL-529` (+ campus rows `ALL-379/380/381`).
  Kept separate per the no-silent-merge rule; the aggregator should collapse.
- **ADDRESS/ZIP SLIP:** `ALL-090` Southeast Middle — district map says 918
  Prigge Rd, NCES/seed say 9180 Riverview Dr 63137; same campus. `ALL-091`,
  `ALL-094`, `ALL-111`, `ALL-113` all physically sit outside the seed ZIP
  (borderline attendance-area rows, retained per instructions).

## Useful sources for reuse

- **pipes.family** (Pipes Family Foundation, 2025) — retells Franzwa's 1977
  *History of the Hazelwood School District* chapter by chapter; the only
  online source with rural-district merger dates (e.g. Larimore's 7/29/1951
  election). The book itself isn't digitized — recommended human follow-up:
  county library has copies.
- **United States v. Hazelwood School District, 392 F.Supp. 1276** — court
  stipulation fixing the 1949-51 formation-from-13-districts fact.
- **stlouisarchitecture.org** — Esley Hamilton's "Surviving Rural Schools in
  St. Louis County" (2013 PDF): the 1910 renumbering (districts 1-75) and the
  1947-54 merger wave; explains "#6"-style seed names.
- **flovalleynews.com** (Florissant Valley News-Reporter archive) — the best
  source for North County school dates: 2007 middle-school dedications,
  parochial closures, Arrowpoint's masonry award.
- **schooldesigns.com** — architect project pages give completion dates for
  new-build Hazelwood schools (Arrowpoint 2004).
- **stlouisreview.com + archstl.org** — authoritative for Archdiocese school
  openings/closures/consolidations (All Saints Academy campuses, St. Angela
  Merici).
- **lindenwood.smartcatalogiq.com** — catalog "Locations" pages let you date-
  bound satellite-campus closures (2021-22 lists it; 2022-23 doesn't).

## Process friction

- **Hazelwood predecessor junior highs have no online open dates.** The 2002
  rename and 2007 rebuild are documented, but the original 1950s-70s junior
  high dedications aren't in the news archive. DESE has no historical
  directory. Franzwa's book or board minutes would resolve them.
- **NCES/publicschoolreview "closed" years are record-year artifacts** — e.g.
  publicschoolreview says Fatima "closed 2004" (correct here) but these can
  lag reality; cross-check with parish/news sources.
- **Every non-city school is harder.** The pilot's Wayman neighborhood
  histories only cover the City of St. Louis; there is no equivalent for
  county schools — the St. Louis County landmarks survey and pipes.family
  partially fill the gap.
