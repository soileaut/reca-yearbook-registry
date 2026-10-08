# Track A Notes — Batch 20 (ZIPs 63341 Defiance/New Melle + 63367 Lake St. Louis/Wentzville)

Date of research: 2026-10-08. Output: `schools_batch20.json` — 15 rows, count unchanged
(no rows merged or split). One row per seed `row_id` (ALL-593…ALL-610 as seeded).

## Confirmed vs. unknown

**Strongly resolved:**
- `ALL-593` Defiance School — resolved to a real, documented entity: the SHSMO Ramsay
  place-names thesis (1943) states plainly "Defiance School: See Walnut Grove School" —
  it was the *popular* name of Walnut Grove School, District No. 68, whose building was
  moved to Defiance ~1944. Opened/closed years remain `unknown` (documented before 1875
  at its original Darst Bottom site; still operating 1948-49 in Defiance; closure
  undated but almost certainly in the 1949–1955 consolidation wave — neighboring Bacon
  School closed June 2, 1950 and Daniel Boone Elementary opened 1955).
- `ALL-594` Defiance School District — administrative-disambiguation verdict:
  `individual_school`. No multi-school "Defiance School District" ever existed; the
  area had numbered one-school common districts, and the district governing the
  Defiance building was No. 68 (Walnut Grove). Almost certainly a duplicate of
  ALL-582/583/584 (batch 19) — flagged for merge review, not merged.
- `ALL-595` New Melle Public School — opened 1860 (probable; New Melle historical
  marker + Boone-Duden Historical Society history both say the district/first log
  school dates to 1860; 1898 "modern" frame building). Closed 1955 probable —
  consolidated into Francis Howell SD in 1949 and replaced by Daniel Boone Elementary
  (dedicated 1955), which is recorded as probable successor (seed row `ALL-587`).
- `ALL-601` Liberty High — 2013 confirmed by the school's own site ("Established:
  2013") plus FOX 2 / Post-Dispatch ribbon-cutting coverage. Still open.
- `ALL-602` Timberland High — seed's 1991 was wrong: opened Aug 28, 2000 as a Holt
  annex; independent four-year high school 2002. Still open.
- `ALL-603` Emil E. Holt Sr. High — seed's 1969 was the *rename* year; the school is
  Wentzville High School, established 1896 (probable — Wikipedia's own line is
  citation-flagged, but the school paper's history page repeats it; 1939
  reorganization to a four-year high school is corroborating structure). Still open.

**Probable (district-site year tiles):**
- `ALL-605` Wentzville Middle — `1964` per the school's homepage year tile
  (probable: tile is unlabeled; the current building is the 1962 former high school
  and only became a middle school in the late 1980s, so 1964 is the entity's
  organization year, not the building's).
- `ALL-607` Frontier Middle — `2005` (homepage tile).
- `ALL-608` Green Tree Elementary — `1997` (homepage tile).
- `ALL-609` Duello Elementary — `2007` (homepage tile); publicschoolreview says 2004 —
  conflict noted in row notes.
- `ALL-610` Prairie View Elementary — `2005` (homepage tile).

**Left unknown (documented dead ends):**
- `ALL-596` New Melle Parochial School 1 — `ambiguous_unresolved`: a generic
  placeholder that resolves to one of two documented parochial schools (St. Paul's
  Lutheran school = probable duplicate of ALL-598, or the Methodist school south of
  town). Which one can't be determined without the seed compiler; ALL-597 presumably
  holds the other. Church archives are the follow-up.
- `ALL-598` St. Paul Lutheran School — opened `1844` probable ("German school soon
  after" the 1844 congregation, per Boone-Duden; new school building dedicated 1919).
  Closure unknown: the church is still active but runs no school today; NRHP lists
  the church as "...Church and Day School" with a significant year of 1965 that may
  mark the school's end — not confirmed, noted only.
- `ALL-606` South Middle — operating by Dec 2006 (Suburban Journals honor roll);
  likely an early-2000s build next to Timberland but no source gives the year. Left
  `unknown`.
- `ALL-599` Defiance Area Rural Schools — `ambiguous_unresolved`: an aggregate
  placeholder for multiple one-room schools, not a single entity. Documented members
  (Bacon #64, Calamus Springs #65, Walnut Grove #68, Hickory Hill #69, Richmond #70,
  Mount Hope ~1837–1940s) are listed in the row's notes for a future split.

## Data-quality flags

- **Cross-batch duplicate cluster:** `ALL-593`/`ALL-594` (batch 20) and `ALL-582`
  Walnut Grove School / `ALL-583` Sycamore School / `ALL-584` Walnut Grove District
  No. 68 (batch 19) all resolve to the same one-room school lineage (District No.
  68). Recommend coordinator merge review — kept separate per the no-silent-merge
  rule.
- **`ALL-596` / `ALL-597` / `ALL-598` overlap:** three seed rows cover New Melle's
  two documented parochial schools (St. Paul Lutheran + Methodist). `ALL-598` is the
  real St. Paul's; `ALL-596`/`ALL-597` are unnamed placeholders that need
  reconciliation.
- **`ALL-603` vs `ALL-604`:** "Emil E. Holt Sr. High School" and "Wentzville High
  School" (different batch) are the same school — Holt is just the 1969+ name.
- **Seed year errors:** Timberland `1991` → actually 2000; Holt `1969` → actually
  1896 (1969 was the renaming).
- **ZIP accuracy:** New Melle rows (`ALL-595`, `ALL-596`, `ALL-598`) sit in ZIP
  63365, not the seed's 63341; Timberland/Holt/WMS/SMS are in 63385, Frontier in
  63368 — all were seeded under 63367 on "served community" grounds. Kept seed ZIP
  in the `zip` field (descriptive only) with actuals noted.
- **Aggregate row:** `ALL-599` covers ~7 distinct one-room schools — should be split
  into per-school rows if those schools are to be searched individually.

## Useful sources for reuse

- **Boone-Duden Historical Society** — `heritage.freese.net/Family/Welge/ArnOlPA/NewMelle.pdf`
  ("New Melle Thru the Years," 2022): school-by-school dates for New Melle (1860
  district, 1898 building, 1949 consolidation, 1955 Daniel Boone dedication, 1919
  Lutheran school dedication). Covers SW St. Charles + SE Warren County.
- **"Just a Walk Down the Road" blog (Bob Brail)** — the "One-Room Schools of
  Township 45, Range 2" post gives founding/closure dates and locations for the
  Defiance-area one-room schools, sourced from Boone-Duden archives.
- **SHSMO Ramsay Place Names File** (`collections.shsmo.org/manuscripts/columbia/C2366/`)
  — per-county entries that resolve rural-school aliases (this is what proved
  "Defiance School" = Walnut Grove School).
- **fhsdschools.org/about** — FHSD's own decade-by-decade history; authoritative
  opening years for every FHSD school (Daniel Boone Elementary 1955 etc.).
- **Wentzville school-site homepages** (`*.wentzville.k12.mo.us`) — each school's
  homepage carries an unlabeled founding-year tile; consistent with known dates
  (Liberty 2013, Timberland 2000), used as `probable` for the middles/elementaries.
- **hmdb.org historical markers** — the New Melle marker independently confirms the
  1860 first public school.

## Process friction

- **Rural common-school closures are mostly undocumented online.** One-room schools
  stopped without news coverage; the best sources are local-historical-society writeups
  that give approximate eras, not exact dates. Expect `unknown`/`probable` on most
  rural closure years.
- **Wentzville district's founding-year tiles are unlabeled**, so they support
  `probable`, not `confirmed`, confidence — and in one case (Duello) conflict with
  NCES-derived sites by 3 years.
- **Rename-vs-open confusion in the seed** is a pattern worth watching: both Holt
  (1969 rename) and Timberland (1991 vs 2000) had seed years that came from events
  other than the school's actual opening.
- **Recommended human follow-up:** St. Paul's Lutheran Church office and the
  Boone-Duden Historical Society archives (Kamphoefner House, New Melle) could supply
  exact dates for the Lutheran and Methodist parochial schools and the Defiance/
  Walnut Grove closure year. Not contacted per scope rules.
