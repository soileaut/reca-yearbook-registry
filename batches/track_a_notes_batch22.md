# Track A Notes — Batch 22 (ZIP 63368: O'Fallon / Dardenne Prairie, St. Charles County)

Date of research: 2026-10-08. Output: `batches/schools_batch22.json` (10 rows —
count unchanged; no rows merged or split). All seed rows were real schools; no
phantoms found in this batch.

## Confirmed vs. unknown

**Opened year confirmed (primary/institutional citations):**
- `ALL-628` Emge Elementary — opened 2002-03 school year (Fort Zumwalt district
  history page: "two new elementary schools, Ostmann and Emge, opened"). The
  school's ~2022 "20th Anniversary" spirit week corroborates 2002.
- `ALL-629` Francis Howell Union High School — opened 1997 (school's own student
  handbook: "Since opening our doors in 1997"; corroborated by the FHSD history
  timeline). Relocated into the renovated 801 Corporate Centre Drive building in
  2022 (Prop S) — the seed's address is the current building, not the original
  site (the former Francis Howell Senior HS "C" building on the FHHS campus).
- `ALL-632` John Weldon Elementary — opened 1991 (FHSD official history timeline).
- `ALL-642` O'Fallon Public School System — organized/school built 1869 per the
  Fort Zumwalt district history; consolidated into Central School District R-II
  (today's Fort Zumwalt R-II) by voter approval July 19, 1949 — that is its
  closure/absorption date. Public high school department ran only until 1918.
- `ALL-646` Woodlawn Seminary — properly "Woodlawn Female Seminary," erected and
  opened 1878 by Prof. Richard H. Pitman (1895 Portrait and Biographical Record
  of St. Charles, Lincoln and Warren Counties). Closed ~1900 (probable — a Hodge
  Lodge cornerstone history says "it continued until 1900"); the building was
  "the former Woodlawn Seminary" when sold after the 1915 cyclone.
- `ALL-647` Assumption School — refined "1870s" to 1871 (school's own history:
  church + log schoolhouse dedicated Sept 17, 1871, school opened a week later).
  Still operating K-8. Sisters of the Most Precious Blood ran it 1873–1991.
- `ALL-650` SCC Dardenne Creek Campus — seed's 2017 confirmed ("established in
  2017," SCC Fast Facts; property purchase closed Feb 24, 2017; dedicated
  May 2, 2018). Nuance: SCC leased space for nursing there since August 2013
  under the Lindenwood partnership, so SCC programming on the site predates the
  campus itself.

**Opened year probable (secondary/informal sources only):**
- `ALL-637` Barfield Early Childhood Center — 2004, from an unlabeled "2004"
  stat on the school's own homepage; a contractor page confirms the ~30,000 SF
  facility existed before an August 2020 addition. Probable because the stat
  label wasn't captured.
- `ALL-640` OakHaven Montessori — 2008 per its LinkedIn company profile; a
  founding teacher's blog confirms it was operating by late 2009.
- `ALL-641` Future Apostle Academy — ~2021 (nonprofit "Est. 2021" on
  GivingFountain; first NCES PSS appearance 2021-22; DHSS child-care license
  application June 2022 at the Springhurst Pkwy address).

**Left unknown:** none — every seed row resolved to a real, identifiable school
with at least a probable opening year.

## entity_type determinations

- `ALL-642` "O'Fallon Public School System" was the only administrative-sounding
  row. Classified `individual_school`: it was a small pre-consolidation town
  district effectively coextensive with "the O'Fallon school" — one campus
  (Convent Park 1869 building, then two buildings on the Virgil Street/Hope High
  School site from 1910) with no separately-named member schools. Judgment call
  flagged for coordinator review; if treated as a district row, its successor is
  `ALL-579` (Fort Zumwalt School District, batch 19).
- All other rows: `individual_school`.

## Data-quality flags

- **Cross-batch successor reference:** `ALL-642`'s successor is `ALL-579`
  ("Fort Zumwalt School District," a district-level row in batch 19). If the
  coordinator prefers successor links only to physical schools, the physical
  continuation is the Fort Zumwalt school building on Virgil Street (later
  Hope High / North Middle School site).
- **Minor ZIP mismatches (systemic for O'Fallon proper):** `ALL-646` Woodlawn
  Seminary, `ALL-647` Assumption School, and `ALL-642` O'Fallon Public School
  System were/are actually in the O'Fallon 63366 area (per the seed's own
  "Current Address" fields); included under 63368 community coverage. Same
  pattern the pilot hit with Beaumont.
- **`ALL-641` Future Apostle Academy is tiny and new** (est. ~2021, ~11 students,
  PK-9). Real school, but near-zero yearbook relevance; keep for completeness.
- **`ALL-637` Barfield is PK-only** early-childhood special education — no
  yearbook relevance, per seed's own "Low" priority.
- **`ALL-647` related entities not in seed:** Assumption High School (building
  dedicated 1955, closed 1962 into the new St. Dominic High School) and the
  Precious Blood Sisters' girls' academy/college (the "St. Mary's Academy" at
  Convent Park, on whose grounds the 1869 public school was built — buildings
  are now O'Fallon City Hall and the police station). Neither is a seed row;
  flagging in case a later pass wants them added.
- **Woodlawn Seminary school type:** seed's "classical education for young
  women" verified — it was a female seminary — but at least one male alumnus
  (Dr. Caleb S. Stone) is documented; possibly admitted boys in some periods or
  the bio is loose. Noted, not blocking.
- **Name drift:** Emge's district site URL is `lce.fz.k12.mo.us` (a shared
  template host), not a dedicated `emge.` subdomain — cosmetic only.

## Useful sources for reuse

- **Fort Zumwalt district history page** (Wayback capture of fzschools.org,
  2007) — covers the whole district lineage from 1807/1869 through ~2007 with
  per-school opening years (Ostmann, Emge, Dardenne, Twin Chimneys, etc.) and the
  1949 Central R-II consolidation. Single best source for 63368-area FZ schools.
- **fhsdschools.org/about** — official FHSD timeline with opening years for
  every district school (John Weldon 1991, FHU 1997, etc.). Ideal pattern:
  district-published history pages give per-building years at scale.
- **School/parish "Our History" pages** — assumptionbvmschool.org resolved an
  "1870s" seed value down to 1871 with a dedication date.
- **Genealogy Trails transcriptions of 19th-century county histories** — the
  1895 Portrait and Biographical Record entry on Pitman gave an exact 1878
  opening for Woodlawn Seminary. Useful for pre-1900 schools that hit dead ends
  elsewhere.
- **NCES CCD/PSS lookups** — reliable for current open status (used for FHU,
  Weldon, OakHaven, Future Apostle).
- **hodgelodge.com Cornerstone History** — a local lodge timeline that happened
  to record Woodlawn Seminary's ~1900 closure; obscure but on-point.
- **District capital/bond pages** (FHSD Prop S, Wright Construction project
  pages, WSD board docs) — good for relocations, additions, and building years.

## Process friction

- Small private schools barely leave a web footprint: OakHaven (founded 2008)
  and Future Apostle (est. ~2021) only resolved via LinkedIn/IRS-adjacent
  nonprofit records and state child-care licensing files — all "probable" tier.
  Expect this pattern wherever seed rows list tiny private schools.
- Unlabeled stat blocks on school websites (Barfield's bare "2004") are a common
  Finalsite template pattern and are *probably* founding years, but they can't be
  read as confirmed without the label — flagged rather than upgraded.
- No recommended human follow-ups needed for this batch; everything resolvable
  by web search.
