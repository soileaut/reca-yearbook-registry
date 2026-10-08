# Track A Notes — Batch 11 (Normandy cluster + two outliers)

Date of research: 2026-10-08. Output: `batches/schools_batch11.json` (15 rows —
count unchanged; no rows merged or split). `reca_scope_status` intentionally absent.

## Confirmed vs. unknown

**Confirmed (opened + closed/n-a both cited):**
- `ALL-340` Normandy HS original classes at old Washington School — opened 1907,
  closed spring 1912 (SHSMO S0326 district finding aid). This is the entity
  Wikipedia's NSC school list calls "Washington High School - 1907."
- `ALL-346` Washington School (1930 building) — opened 1930, still open as
  Washington Elementary, 1730 N Hanley Rd (current NSC enrollment list).
- `ALL-354` Jefferson School — opened 1929, still open as Jefferson Elementary,
  4315 Cardwell Dr (same NSC list).
- `ALL-337` Ritenour Adult Education — still operating (RSD relocation notice,
  July 2025); opened_year left `unknown`.

**Probable (real evidence, minor conflicts):**
- `ALL-335` Loretto Academy — identified as the city Loretto Academy, 3407
  Lafayette Ave (NRHP NRIS 92000079; opened 1907 per Post-Dispatch/UrbanReview;
  closed 1952 per Nerinx Hall's own LibGuide). Successor: Nerinx Hall HS.
  Identity and ZIP flagged — see flags below.
- `ALL-339` Normandy HS Eden Seminary campus — opened 1923-24 school year
  (district site + SHSMO; bond year given as 1922 or 1924 in different sources,
  Wikipedia school list says 1925). "Closed 1958" = demolition of the original
  seminary building only; the school never closed.
- `ALL-342` Normandy Junior High, Natural Bridge — opened 1949 (construction
  began 1948; split sessions during 1949-50). Closed as a school program in 2019
  when the "Normandy 7th-8th Grade Center" was eliminated in the EleMiddle
  reorg; building is now the Normandy Early Learning Center, and the
  middle-school program moved to Normandy MS at Lucas Crossing (7837 Natural
  Bridge).
- `ALL-344`/`ALL-345`/`ALL-346` — one continuous Washington School across three
  buildings (1894 → 1895 → 1930). 344's close (1895) is the weakest claim —
  SHSMO says the new building was built 1895 but doesn't say the old one stopped
  being used.
- `ALL-347`/`ALL-348` Normandy School / Roosevelt School — same 1897 building at
  7629 Natural Bridge Rd. Sources conflict on the rename date (seed's historic
  survey implies ~1930; Wikipedia's district-history school list gives Roosevelt
  the whole 1897-1938 span). Closed 1938 is consistent across sources.
- `ALL-349` Lincoln, `ALL-351` McKinley, `ALL-352` Harrison — established
  ~1900/1907/1907; all three closed ~2001 when their students moved to the new
  Lucas Crossing Elementary.
- `ALL-350` Garfield — est. 1906; consolidated into Barack Obama Elementary
  (batch12 `ALL-357`) when it began operations in 2011 (the naming vote was
  2010, so the consolidation year is 2010-2011 depending on convention).

**Left unknown:**
- `opened_year` for `ALL-337` (program start date not published online).
- `closed_year`/`successor` detail for `ALL-348` beyond the 1938 endpoint —
  no online source documents where Roosevelt's students went.
- Founding year of `ALL-347` Normandy School — it predates the 1894 district;
  the 1897 figure is the building date.

## Data-quality flags (for the coordinator)

1. **ZIP/identity uncertainty, `ALL-335` Loretto Academy:** recorded as the St.
   Louis city academy (3407 Lafayette Ave, 63104) which closed 1952 into Nerinx
   Hall. Seed's "63114 / St Louis County" is unsupported; a plausible alternative
   referent is the Florissant Loretto Academy (built 1882, burned 1919,
   florissantmo.com marker). Needs human adjudication.
2. **Wrong address, `ALL-337`:** 2420 Woodson Rd is the Ritenour district admin
   center, not the adult-ed classroom site (8672 St. Charles Rock Rd until 2025,
   now inside Hoech Middle School).
3. **Cross-batch overlap — Normandy HS:** `ALL-339` and `ALL-340` (this batch)
   overlap batch10's `ALL-328` ("Normandy High School") and `ALL-329`
   ("Normandy High School - Historical Campus"). `ALL-339` is the same school/
   campus as `ALL-329`. Recommend coordinator de-dup before Track B.
4. **Cross-batch overlap — Normandy JH:** `ALL-342` likely equals batch10's
   `ALL-330` ("Normandy Junior High School").
5. **Same-school pairs kept separate per rules:** `ALL-344`/`ALL-345`/`ALL-346`
   (Washington School buildings); `ALL-347`/`ALL-348` (Normandy → Roosevelt
   rename in one building). Both deserve a merge decision at aggregation time.
6. **Building vs. school conflation in seed "closed" dates:** `ALL-339` closed
   1958 is a demolition date, not a school closure — the campus still operates.
   Same pattern as the pilot's building-date caveat.
7. **1897 building likely gone:** builtstlouis.net describes the church now at
   7629 Natural Bridge as 1960s vintage — the "historic 1897 Normandy School"
   probably no longer stands despite seed implying it survives as the church.
8. **ZIP metadata vs. actual addresses:** ALL-339 is really 63133 (Wellston);
   ALL-346 is really 63114 (Vinita Park). Seed ZIPs kept as descriptive
   metadata per schema.
9. **No administrative-district rows in this batch** — every row is
   `individual_school`.
10. **McKinley opened year discrepancy:** seed 1906 vs. NSC school list 1907 —
    recorded 1907.
11. **Successor rows with no school_id:** Lucas Crossing Elementary (successor
    for ALL-349/351/352), Normandy MS at Lucas Crossing (successor for ALL-342),
    and Nerinx Hall HS (successor for ALL-335) have no seed rows anywhere in
    `batches/` — `successor_school_id` left `unknown` with names in notes.
    ALL-357 (batch12) is usable for Garfield and was used.

## Useful sources for reuse

- **SHSMO S0326 finding aid** (Normandy School District Collection):
  single best source for the district's founding (July 12, 1894), the 1895/1897
  buildings, the 1907-1912 high school, the 1922 bond/Eden Seminary purchase,
  the 1949 fire, and the 1958 demolition. cites its own internal district
  histories — good enough for `confirmed` on the old dates.
- **Wikipedia: "Normandy Schools Collaborative"** — contains a full school list
  with open dates drawn from a district history (fn. 5), plus a former-schools
  section naming which school absorbed which (Harrison/Lincoln/McKinley →
  Lucas Crossing; Garfield+Pine Lawn → Barack Obama; Bel-Ridge closed 2011).
  Use it as an index, then cite it directly for probable-level claims.
- **normandysc.org current enrollment list + Code of Student Conduct PDF** —
  authoritative current school/address roster (proved ALL-346 and ALL-354 still
  open, and that 7855 Natural Bridge is now the Early Learning Center).
- **NSC fall 2018 newsletter PDF** (resources.finalsite.net) — documents the
  7th-8th Grade Center closing and EleMiddle reconfiguration (2019).
- **npgallery.nps.gov (NRHP NRIS)** + **urbanreviewstl.com** for the Loretto
  Academy building; **nerinxhall.libguides.com** Loretto Project Packets give
  closure years for Loretto schools.
- **ritenourschools.org district news posts** — program relocations are posted
  there; useful for adult-ed/alternative rows.

## Process friction

- **Successor rows outside the batch have no IDs.** Schema's
  `successor_school_id` assumes the successor is in the registry; when it lives
  in another batch (or nowhere in the seed data), the only honest value is
  `unknown` + a note. Coordinator should add a name-based fallback convention.
- **Conflicting official-ish sources within the same district:** the district's
  own HS page says the Eden bond passed April 1924 while SHSMO's finding aid
  says voters authorized it in 1922 and Wikipedia's list says the school opened
  1925. All describe the same school; the open year is a range (1922-25) no
  online source fully resolves — school board minutes at SHSMO/Mercantile would.
- **Rename-vs-new-entity ambiguity:** the Normandy→Roosevelt rename date is not
  determinable online; two credible sources give different spans (1930-1938 vs.
  1897-1938). Both rows recorded probable with the conflict stated.
- **Missouri "historic survey" cited by seed notes was not found online** — the
  seed repeatedly references a survey identifying buildings under dual names
  (Wheaton/Harrison, Normandy/Roosevelt). Could not locate the document; treated
  its claims as seed assertions, not independently verified.
- **Recommended human follow-ups:** (a) SHSMO S0326's folder "A History of
  Public Schools in the Normandy School District" (f.13) would resolve the
  Roosevelt rename date and the ALL-344 close date; (b) Nerinx Hall/Sisters of
  Loretto archives could confirm whether the seed's Loretto Academy is the city
  or Florissant school.
