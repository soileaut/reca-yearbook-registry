# Track A Scale-Up — Coordinator Summary

Scope: all 325 deduplicated seed rows in `data/schools_seed_deduped.json`,
researched by 22 parallel batch workers (~15 rows each, branches
`track-a/batch01`–`track-a/batch22`), merged into this integration branch.
Pilot output (`pilot/schools_63147.json`, 12 rows) is unchanged and included
in the regenerated master.

## Totals

- **337 rows** in `schools_master.json` (325 new + 12 pilot). All 325 seed
  `row_id`s are covered exactly once — no missing, no duplicates, no splits.
- `reca_scope_status` (computed by `compute_reca_scope.py`):
  - **in_scope: 282** (274 new + 8 pilot)
  - **out_of_scope_closed_before_1949: 22** (20 new + 2 pilot)
  - **unknown_insufficient_data: 33** (31 new + 2 pilot)
- `entity_type` (new rows): 287 `individual_school`, 27
  `administrative_district_only`, 11 `ambiguous_unresolved`.
- All rows have every required schema field; all confidence values are
  valid; ~640 citations, all but 2 are URLs.

## Data-quality flags (aggregated from all batch notes)

### Likely phantom / non-school seed rows
- ALL-004 "DeSmet School" — no independent verification (batch01).
- ALL-061 "Central Middle predecessor" — no Hazelwood Central JH ever existed (batch04).
- ALL-104 "Oasis Institute" — only a senior-ed nonprofit found (batch05).
- ALL-118 "McCluer South-Berkley feeder schools" — aggregate placeholder (batch06).
- ALL-164 — a gym facility of ALL-163, not a school (batch07).
- ALL-220 "Bridgeton Senior High School" — no evidence it existed (batch08).
- ALL-299 "St. Ann School District" — St. Ann was always Ritenour/Pattonville (batch09).
- ALL-335 "Loretto Academy" — seed ZIP unsupported; two candidate referents, needs adjudication (batch11).
- ALL-377 "Normandy Area Historical Association" — a historical society, not a school; useful as a Track B archive lead (batch12).
- ALL-448 "St. Peter School" — no such Catholic school in Ferguson (batch15).
- ALL-527 "Lambert Airport Schools" — likely phantom (batch18).
- ALL-253 "Melrose School #57" — real school but located in Wildwood 63038, ~25 mi outside the study area; recommend coordinator review (batch08).
- ALL-401, ALL-548, ALL-549 — aggregate/boundary placeholders → `administrative_district_only` (batches14/18).

### Cross-batch duplicates / same-school pairs (kept separate per the no-silent-merge rule; candidates for a future dedupe pass)
- Hazelwood Central chain: ALL-459/460/467 vs ALL-020/021/022/075; ALL-021/022 is a rename pair.
- STLCC–Florissant Valley: ALL-443/444/445 (batch15) — note ALL-444's "closed 1965" is the bond-issue year.
- Pattonville HS lineage: ALL-148/149/198.
- Airport Elementary: ALL-222 ≈ ALL-390 ≈ ALL-408.
- Kinloch HS: ALL-393 ≈ ALL-497; successor ALL-032 McCluer North.
- Normandy cluster: ALL-328/329/330 ≈ ALL-339/340/342; ALL-394/395 same building.
- Ferguson cluster: ALL-416/417; ALL-418/419; ALL-420 Vogt chain.
- Walnut Grove/Defiance: ALL-593/594 = ALL-582/583/584 (batches19/20).
- Holt/Wentzville HS: ALL-603 = ALL-604 (rename).
- Others: ALL-048=ALL-108, ALL-053=ALL-059, ALL-055≈ALL-143, ALL-065=ALL-088/127,
  ALL-249≈ALL-027, ALL-261≈ALL-314, ALL-321/ALL-309, ALL-470=ALL-469,
  ALL-491=ALL-492, ALL-596/597/598 (three rows, two real parochial schools).

### Seed data errors found
- **ZIPs are served-community, not physical** — systemic; many rows' real
  campus ZIP differs from seed (e.g. Bellefontaine Neighbors schools are
  63137 not 63138; Ritenour rows are 63114 not 63074; FZ/Wentzville rows
  63366/63376/63385 not 63367/63368).
- Date errors: FFSD opened 1951 not 1938; Consolidated District No. 2
  organized 1915 not 1950; Holt opened 1896 (1969 was the rename);
  Timberland HS 2000 not 1991; Overland School closed 1958 not 1924;
  Bridgeton 1978 not "1960s"; Berkeley SD 1937 / Kinloch SD 1902 (district
  dates corrected from seed).
- "Closed" fields often recorded *district* events, not school events
  (Penn-Junction, Mount Pleasant, ALL-073/075, ALL-293, ALL-444).
- Wrong operators: ALL-469–475 are Missouri DYS residential units, not
  Hazelwood SD schools; ALL-441 North Tech is Special School District;
  ALL-045 is Hazelwood's "ECE East," not FFSD.
- Address errors/placeholders on several rows; ALL-356/379 address swap;
  ALL-337 is the district admin center.
- Shifted columns on ALL-590/591 (batch19).
- Scudder narrative backwards — it was the *Black* school after 1903; the
  Scudder School District survived to ~1960 (batch13).
- "Stormin Academy" is a misspelling of **Storman Academy** — the typo
  originates in the City of Bellefontaine Neighbors' own history doc (batch17).

### Schema/process friction for a future pass
- Aggregate "X Rural/Area Schools" rows don't fit `entity_type` cleanly —
  workers used `administrative_district_only` for the correct Track B skip
  behavior; consider a `school_set_aggregate` enum (batch21).
- "Not a school" rows (historical society, placeholder) forced into
  `ambiguous_unresolved` — consider a `not_a_school` enum (batch12).
- Real successors with no seed row (e.g. Wyland Elementary, Lucas Crossing
  ES, Nerinx Hall, Drummond Elementary) got `successor_school_id: unknown`
  with the name in notes — a name-based fallback convention would help.
- Wyland Elementary (opened 1958, Overland School's documented successor)
  is missing from the seed entirely; also absent: Assumption HS (closed
  1962) and Our Lady of the Angels, Kinloch (1931–2002).
- Undigitized local histories would resolve remaining unknowns: Franzwa's
  1977 Hazelwood district history, Crank (1990), Ferguson's 1975 history —
  recommended as human follow-ups.

### Coordinator note
`merge_schools.py` was patched (one line) to skip files with `seed` in the
name — its `schools_*.json` glob also matched the 24 seed-input files in
`data/` and `batches/`, which would have corrupted `schools_master.json`.
