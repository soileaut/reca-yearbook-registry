# Track A Notes — Batch 04 (ZIP 63033 / Florissant–Black Jack–Spanish Lake area)

Date of research: 2026-10-08. Output: `schools_batch04.json` — 15 rows, one per seed row
(no merges or splits). `reca_scope_status` left absent per schema (computed by
`compute_reca_scope.py`).

This batch skews heavily toward Catholic parish schools swept up in the Archdiocese of
St. Louis's **2005 Northeast Deanery consolidation** and the 2023 "All Things New"
restructuring — that context resolved most of the rows.

## Confirmed vs. unknown

**Confirmed (opened or closed with citations):**
- `ALL-048` All Saints Academy – St. Rose Philippine Duchesne — formed 2018 as a
  three-campus partnership school (with St. Ferdinand and St. Norbert); the St. Rose
  campus closed for 2023-24 (enrollment 238→131, ~$878k deferred maintenance).
  Students offered transfers to the other two campuses — `ALL-013` and `ALL-014`
  (both in batch01), recorded as a dual successor.
- `ALL-049` St. Thomas the Apostle School — closed 2005; successor `ALL-047`
  (St. Rose Philippine Duchesne School, batch03), confirmed by STLPR: the new merged
  parish's school went into the St. Thomas building at 3500 St. Catherine St.
- `ALL-052` Salem Lutheran original schoolhouse — built 1895, used as a classroom
  until 1950 (congregation's own history + St. Louis County Historic Buildings
  Inventory). Building-variant row of `ALL-051`.
- `ALL-060` Hazelwood Central Middle School — new construction, dedicated April 18,
  2007; still open. One of four middle schools opened 2007-08 when the district
  pulled 6th grade out of elementaries.
- `ALL-064` Hazelwood East High School — established 1974 (seed's 1965 is wrong —
  that's the second Hazelwood High/Central building). Dunn Rd campus opened fall
  1976; still open.
- `ALL-051` Salem Lutheran School — still open (2026-27 re-enrollment). Opened
  "1868" is probable, not confirmed: first regular teacher called 1868, but the
  congregation's history says school was organized soon after the church's 1849
  founding. Seed's 1895 is the schoolhouse building date.

**Probable:**
- `ALL-050` St. Christopher School — real parish school at 11755 Mehl Ave
  (NCES-derived listings); parish 1967–2005, school presumed closed with it.
  Territory split: north of I-270 → St. Angela Merici (`ALL-080`, batch05), south →
  Holy Name of Jesus → Christ, Light of the Nations School (closed 2020, not in
  dataset). Opening year not found.
- `ALL-053` Children's Village Christian School — still listed as operating
  (PK-3, ~4 students); no founding date exists anywhere online.
- `ALL-054` Gateway Legacy Christian Academy — founded 2005; still operating at
  seed's 1360 Grandview Dr plus the ex-St. Stanislaus Seminary campus (700
  Howdershell Rd, acquired 2019). Survived a Dec 2022 city-ordered shutdown over
  fire/safety codes.
- `ALL-057` Tendercare Learning Center — licensed child-care center (DHSS
  #000566534) at 13775 New Halls Ferry; still operating, possibly rebranded as
  "Visionary Academy Prep."
- `ALL-065` Hazelwood East Middle School — lineage: 1954 first Hazelwood High
  building (1865 Dunn Rd) → Kirby Junior High (~1966) → Kirby Middle (2000) →
  East Middle (2007) → moved into East HS as the 8th Grade Center ~2017-18;
  old building now Hazelwood Opportunity Center (`ALL-476`, batch17). Still open.
  Opened_year 1966 is probable (inferred from Central HS's 1966 opening).

**Left unknown (documented dead ends):**
- `ALL-049` opened_year — school probably dates to the early-mid 1960s (parish
  1960, church 1966) but no dated source found.
- `ALL-050` opened_year.
- `ALL-055` Faith Christian School — only stale business-directory listings at
  2300 Parker Rd (principal Warren Stump). Can't confirm operating period or even
  that it survives — likely a small church school, possibly defunct.
- `ALL-056` Academy at St. Rose Philippine Duchesne — resolved the identity (an
  Archdiocese Dept. of Special Education academy at 1220 Paddock Dr, NCES
  00752221, ~33 students), but no open/close dates. Absent from the 2017-18
  accredited-schools list while The Academy at St. Sabina (Florissant) is listed —
  probably consolidated into St. Sabina sometime between ~2012 and 2017.
- `ALL-058` Alphabet Soup Learning Center — LinkedIn-attested Florissant daycare
  (director 1999–2005, owner from 2002); no address or current status findable.
- `ALL-061` "Hazelwood Central Middle School predecessor" — LIKELY PHANTOM; no
  Central Junior High/Intermediate ever existed in Hazelwood (see flags below).

## Data-quality flags

1. **Phantom row — `ALL-061`.** No "Central Junior High/Intermediate School" is
   documented in Hazelwood history. Hazelwood's pre-2007 junior highs were Kirby
   JH and Hazelwood JH; Central Middle was greenfield construction in 2007.
   Recommend deletion or folding into `ALL-060`'s notes at coordination time.
2. **Seed address errors:**
   - `ALL-049`: "5300 Derby Lane" — no Derby Lane exists in Florissant; the school
     was at 3500 St. Catherine St.
   - `ALL-064`/`ALL-065`: physical address is 11300 Dunn Rd, **ZIP 63138**
     (Spanish Lake), not 63033 — seed itself notes this; ZIP is attendance-zone
     metadata.
3. **Duplicate/conflated rows across batches:**
   - `ALL-048` = `ALL-108` "All Saints Academy - St. Rose Campus" (batch05) — same
     entity.
   - `ALL-053` = `ALL-059` "Children's Village Christian School - Historical."
   - `ALL-055` ≈ `ALL-143` (same school under ZIP 63042).
   - `ALL-065` = `ALL-088`/`ALL-127` (East Middle under 63034/63042).
   - `ALL-052` is a deliberately kept building-variant of `ALL-051` (1895
     schoolhouse vs. the continuous school).
4. **Name-collision caution:** `ALL-056` (archdiocesan special-ed "Academy at
   St. Rose Philippine Duchesne," 1220 Paddock Dr) is *not* the All Saints Academy
   campus (`ALL-048`, 3500 St. Catherine) and *not* the private "Academy of St.
   Louis" in Manchester — three easily-confused names.
5. **Early-childhood rows** (`ALL-057`, `ALL-058`, and nearly `ALL-053`) are
   daycares; almost certainly no yearbooks — candidates for low-effort handling.

## Useful sources for reuse

- **stlouisreview.com** (archdiocesan paper) — closure/merger announcements,
  campus-level detail (2005 deanery consolidation, 2018 All Saints formation,
  2023 campus closure).
- **stlouis.closedparishes.com** and the **Archdiocese closed-parishes list**
  (capacity.com PDF) — parish founding/closure years and territory disposition.
- **stlgs.org** closed-churches tables — parish dates/addresses.
- **flovalleynews.com** (North County community paper) — school dedications,
  district rename history (Kirby JH → East Middle), parish school consolidations.
- **Schools' own history pages** (salembjmo.org, saintangelamerici.org) — best
  primary sources for parish school lineage.
- **en-academic.com Wikipedia mirrors** — the deleted "Hazelwood East Middle
  School" article survives there; useful when school articles get merged/redirected.
- **MO DHSS child-care license search** (webapp01.dhss.mo.gov/childcaresearch) —
  current-status check for daycare rows.
- **privateschoolreview.com / educationbug.org** — NCES-derived; good for
  existence/address, "Year Founded" usable only as probable.

## Process friction

- **No Derby Lane in Florissant** — seed addresses should be sanity-checked
  against a map; at least one per batch has been garbled.
- **Special-education academies and daycares** have almost no archival footprint;
  `unknown` is the honest outcome.
- **Pre-1970 parish school opening dates** are rarely online — parish founding
  year is the best available anchor; noted as such.
- **Recommended human follow-up:** Archdiocese of St. Louis Catholic Education
  Office records / parish sacramental-records guides could date St. Thomas and
  St. Christopher school openings; Secretary of State filings could pin
  Alphabet Soup and Faith Christian.
