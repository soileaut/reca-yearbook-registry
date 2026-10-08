# Track A Notes — Batch 07 (Pattonville / Maryland Heights area, ZIP 63043 seeds)

Date of research: 2026-10-08. Output: `batches/schools_batch07.json` — 15 rows,
one per seed row (`ALL-164`–`ALL-179`, no `ALL-177` in this batch). Count unchanged;
no rows merged or split, though several pairs are flagged as same-school relationships
(see flags below). No `reca_scope_status` set (computed downstream).

## Dominant source

This batch turned out to be unusually tractable because the **Pattonville R-III
School District's own published history** covers nearly every row in detail:

- `https://www.psdr3.org/about/history/by-the-years` — year-by-year district
  timeline (1806 → present), including the 1936 Penn/Junction merger, the 1949-50
  Penn-Junction and Bridgeton annexations, the 1951 Junction/Mount Pleasant merger
  that created the "R-3" district, the 1962 Maryland Heights merger, and exact
  opening years/principals for Willow Brook (1959), Bridgeway (1963), Briar Crest
  (1965), and Carrollton Oaks (1967).
- `https://sites.google.com/psdr3.org/pattonvillehistory/home` — per-school
  profiles including "Schools No Longer Operating" with closure years and
  building dispositions (1978 trio: Bridgeton, Mount Pleasant, Pattonville
  Elementary; 1982 reorganization: Penn-Junction and St. Ann; 2001 airport
  closures: Carrollton and Carrollton Oaks; 2013 Briar Crest).
- `https://www.psdr3.org/about/prop-s` — confirms the 1951 Maryland Heights
  gymnasium/printing facility at 115 Harding was slated for demolition (for
  Pattonville Heights parking) once printing moved to Holman Gym B in 2025.

Because the district itself published these dates, `confirmed` was used freely —
this is the strongest possible short-of-archival source for a school district's
own history.

## Confirmed vs. unknown

**Fully resolved (both dates cited):**
- `ALL-167` Carver Harding Ave campus — 1951 build ($15,000 two-room), discontinued 1962.
- `ALL-168` Penn School — ~1850 (probable; "about the same time" as Fee Fee 1850),
  merged 1936 → Penn-Junction.
- `ALL-169` Junction School — opened 1869, merged 1936 → Penn-Junction.
- `ALL-170` Penn-Junction — 1936 merger product, annexed May 1950 (seed correct),
  kept operating as a Pattonville elementary until closed in the 1982 reorganization.
- `ALL-171` Mount Pleasant — schoolhouse 1836 (probable), district merged 1951,
  school ran until the 1978 enrollment-decline closures; sold 1981.
- `ALL-173` Bridgeton Elementary — opened 1953 (Pattonville-era building),
  closed 1978, sold 1985 to First Korean Presbyterian Church. Seed's "1960s" was wrong.
- `ALL-174` St. Ann Elementary — opened unknown but closed 1982 confirmed.
- `ALL-175` Willow Brook — 1959, still open. `ALL-176` Bridgeway — 1963, still open.
- `ALL-178` Briar Crest — 1965–2013 (not 2018; 2018 is when the building reopened
  as the Pattonville Early Childhood Center).
- `ALL-179` Carrollton Oaks — 1967–2001 (not 2002); closed for the Lambert airport
  runway expansion and demolished; students went to Drummond Elementary, the
  airport-funded replacement school.
- `ALL-164` Maryland Heights HS gymnasium — built 1951 for $40,000; demolished
  ~2025 (probable on the exact date; district Prop S documents the plan and the
  seed says July 2025).

**Left unknown:**
- `ALL-165`/`ALL-166` Carver School for Negroes (umbrella + Adie Road campus)
  `opened_year` — founding date of the segregated Maryland Heights Black school
  is not online. SLCL's Black Heritage Trail index does reference "Carver
  Elementary School, Maryland Heights, Mo." (pp. 73-74 of an indexed volume) —
  recommended human follow-up, possibly at the Missouri History Museum or SLCL.
- `ALL-174` St. Ann Elementary `opened_year` — district itself records only
  "existed as early as 1956."

## Data-quality flags

- **`ALL-164` is a facility, not a school** — it's the gymnasium of Maryland
  Heights High School (`ALL-163`, a different batch). No yearbook research should
  attach here; keep as a footnote to `ALL-163`. `entity_type` left
  `individual_school` because it is neither a district nor unresolved, but it
  should never be a Track B search target.
- **`ALL-165`/`ALL-166`/`ALL-167` are one school at two sites** — Carver School
  for Negroes is the umbrella; Adie Road is the pre-1951 site, Harding Avenue the
  1951–1962 site. Rows kept separate per the no-silent-merge rule (and the
  review-needed file already flags them); a merge decision belongs to a human or
  the coordinator.
- **`ALL-172` Pattonville Grade School identity ambiguity** — the 1907 Fee Fee
  Road grade school coexists in district records with a "Pattonville Elementary
  School (opened 1954, closed 1978)." Most likely the grade school was renamed,
  but the district history never says so; recorded opened 1907 confirmed /
  closed 1978 probable. If another batch produces a Pattonville Elementary row,
  review for merge.
- **Seed `Closed` fields often record district events, not school events** —
  Penn-Junction "1950" was the annexation (school ran to 1982), Mount Pleasant
  "1951" was the district merger (school ran to 1978). Worth checking this
  pattern in other batches seeded from the same spreadsheet.
- **Successor targets missing from the dataset** — Drummond Elementary (the
  confirmed successor to `ALL-179`, built with airport funds) has no seed row;
  successor recorded as `unknown` id with the name documented in `notes`.
- **ZIP accuracy** — several rows carry ZIP 63043 but the physical addresses are
  63044 (Bridgeway, Carrollton Oaks, Bridgeton Elementary), 63074 (Briar Crest,
  St. Ann Elementary) or 63146 (Willow Brook). Seed `zip` values were preserved
  as descriptive metadata per schema; actual ZIPs noted per row.
- **Seed `Length`/`#VALUE!` columns** are derived junk (years-open arithmetic);
  ignored, consistent with the pilot.

## Process friction for scale-up

- When a single strong district-history source exists (like psdr3.org's),
  a whole batch collapses to ~an hour of work. Batches lacking one will need
  the slower per-school search path from the pilot.
- District histories record *district* events and *building* events with the
  same verbs ("closed," "merged," "sold") — care needed to keep the school
  entity's timeline straight (e.g. Penn-Junction's 1950 annexation vs. 1982
  closure vs. 1985 sale).
- Black/ segregated school records remain the thinnest online coverage: Carver's
  founding year is invisible on the open web despite being documented enough
  for the district to name it in its own history.
- `entity_type` required per schema: no batch row had an administrative-district
  name, so all are `individual_school`.
