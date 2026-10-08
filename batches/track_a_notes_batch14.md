# Track A Notes — Batch 14 (Berkeley / Kinloch / Ferguson / Robertson, ZIPs 63134–63135)

Date of research: 2026-10-08. Output: `schools_batch14.json` (15 rows — count
unchanged; no rows merged or split. ALL-417 is flagged as the same entity as
ALL-416, and ALL-401 is flagged as a pseudo-entity; both kept per the
no-silent-merge rule).

This batch is unusually interconnected: nearly every row belongs to one
segregation-era story — the 1902 Kinloch split from Ferguson, the 1937–38
Berkeley secession, the 1960 Scudder annexation, the ~1964 Robertson
absorption, and the June 7, 1975 federal court order merging Berkeley and
Kinloch into Ferguson-Florissant R-II.

## Confirmed vs. unknown

**Fully confirmed (opened + closed with citations):**
- `ALL-400` Berkeley School District — established 1937 (Eighth Circuit,
  515 F.2d 1365) when Kinloch No. 18 was split white/Black; annexed to
  Ferguson-Florissant by court order June 7, 1975 (388 F. Supp. 1058,
  SHSMO S0707 collection).
- `ALL-402` Kinloch School District — formed 1902 by Board of Arbitration
  after white residents split from the Ferguson district (Wright-based
  history + urbanreviewstl.com); originally District No. 5, renumbered
  No. 18 in 1910. Annexed to FFSD June 7, 1975.
- `ALL-403` Scudder School District — closed/annexed: Berkeley district
  voted Aug 24, 1960 to annex it (Southern School News, Oct 1960, p. 14 —
  a scanned primary source; ~260 pupils, ~75% Black, no high school, HS
  students tuitioned to Soldan). Formation date NOT found — left `unknown`.
- `ALL-404` Ferguson-Florissant School District — **seed corrected**:
  formed by the October 1951 county reorganization vote (PRiME Center/SLU;
  Eighth Circuit: "in 1951 Ferguson, Florissant and St. Ferdinand School
  Districts reorganized"), effective 1952. Seed's 1938 is wrong. Still
  operating.
- `ALL-408` Airport Elementary — primary source: City of Berkeley RFP
  (Aug 2023) states the school and gym "were constructed on this site in
  1954... closed in 2019 due to declining enrollment, and the City
  purchased the property in 2023." Berkeley SD 1954–75 → FFSD 1975–2019 →
  community-center conversion.
- `ALL-416`/`ALL-417` Ferguson High School — opened 1939 (400 students
  transferred from John M. Vogt HS; WPA-built on the January Estate;
  Living New Deal + school's own 1948 Crest yearbook history), last
  graduating class 1962, students moved to McCluer High School (ALL-111).
  Yearbook: "The Crest."
- `ALL-418` Ferguson Junior High School — opened 1962 in the same building;
  still operating as Ferguson Middle School (fms.fergflor.org).

**Probable (real evidence, incomplete or informal):**
- `ALL-409` Robertson School District — dissolved ~1964 into Berkeley
  (probable): the Robertson HS closed 1964 and Berkeley bused the students
  (Wikipedia Berkeley HS); Robertson is absent from the 1975 court order
  yet sits inside the post-merger district per an FFSD geographical study,
  so the boundary change must have predated 1975.
- `ALL-410` Robertson High School — closed 1964 (probable, same source);
  students bused to Berkeley High School (ALL-114). No opening date or
  building location found.
- `ALL-411` Robertson Elementary School — seed's 1964 rejected in favor of
  ~1975 (probable): the FFSD study says "all the schools in the Kinloch
  and Robertson areas were closed" as a result of the court-ordered
  merger, implying an elementary-level school still ran in Robertson
  (under the Berkeley district) until 1975. Alternative reading noted in
  the row.
- `ALL-401` Berkeley SD Elementary System — opened follows district
  (probable); closed 1975 confirmed with the district.
- `ALL-405` Mark Twain School — still operating as the alternative-ed
  "Mark Twain Restoration & Wellness Center" (rwc.fergflor.org), but an
  FFSD board doc proposes closing/restructuring the Mark Twain location,
  so status is probable only.

**Left unknown:**
- `opened_year` for ALL-403 (Scudder district formation), ALL-405 (Mark
  Twain Elementary — alumni site covers "Classes of 1963–1981" but no
  founding year), ALL-406 (Johnson-Wabash building), ALL-407 (Walnut
  Grove — operating by 1973 per a Pacific Standard memoir, no founding
  year), ALL-409/410/411 (all Robertson dates before 1964), and the
  junior-high→middle rename year for ALL-418.

## Data-quality flags

- **`ALL-401` is a pseudo-entity** — "Berkeley School District Elementary
  System" was never a real entity; it aggregates the district's
  elementaries (Hancock School, Airport Elementary, later Berkeley
  Elementary/Intermediate, Holman Elementary). Marked
  `administrative_district_only`; do not Track-B it.
- **`ALL-417` duplicates `ALL-416`** — the January Avenue building was
  Ferguson High's only location, not one of several campuses. Flagged for
  the coordinator to consider merging (deliberately kept separate per
  dedup rules).
- **`ALL-418`/`ALL-419` cross-batch overlap** — this batch's "Ferguson
  Junior High School" and another batch's "Ferguson Middle School"
  (ALL-419) are one continuous school under era names.
- **`ALL-408`/`ALL-390`/`ALL-222` cross-batch overlap** — three seed rows
  describe the same Airport Elementary building (1954–2019).
- **Seed error:** `ALL-404` "opened 1938" → corrected to 1951.
- **Seed error:** `ALL-405` "Berkeley area" — Mark Twain is in
  Hazelwood/Florissant (now 8855 Dunn Rd, Hazelwood 63042; earlier campus
  possibly on Derhake Rd per a Florissant crosswalk ordinance). Not
  Berkeley.
- **Seed artifact:** `ALL-408` "Opened 2023" describes the community-center
  conversion date, not the school (1954–2019).
- **`ALL-403` marked `ambiguous_unresolved`** — the Scudder district had
  ~260 pupils and no high school, but whether it ran one or several
  school buildings could not be determined; the "Scudder Avenue School"
  (ALL-392) belongs to the Ferguson/Kinloch lineage and is likely a naming
  overlap, not a confirmed member.
- **ZIP corrections:** ALL-402 is Kinloch 63140 (not 63134); ALL-405 is
  Hazelwood 63042 (not 63134).

## Useful sources for reuse

- **Court opinions (primary, well-indexed):** 515 F.2d 1365 (8th Cir.,
  en banc, law.resource.org), 363 F. Supp. 739 (Justia), 388 F. Supp. 1058
  (hallapproved.com) — authoritative for the 1937 Berkeley/Kinloch split
  and the June 7, 1975 merger. Better than secondary sources for any
  north-county district row.
- **Southern School News (teva.contentdm.oclc.org)** — scanned 1954–1973
  desegregation-era reporting; the Oct 1960 issue documents the
  Scudder→Berkeley annexation verbatim. Worth checking for other district
  annexations.
- **PRiME Center (SLU) consolidation blog** — maps every St. Louis County
  district reorganization (1949, 1951, 1954, 1960s annexations, 1975
  court order, 2010 Wellston). Excellent district-level reference.
- **barkerreunion.blogspot.com** — "Red Schoolhouse / BHS Reunion" pages
  quoting John A. Wright Sr.'s Berkeley/Kinloch history (Wright is the
  authoritative Kinloch historian — the same Wright who chaired the
  Kinloch History Committee, SHSMO S0151). Informal but specific; treat as
  probable.
- **City of Berkeley eGov docs (berkeleymo.us)** — council bills and RFPs
  give primary-source dates for Airport Elementary and the community
  center conversion.
- **fergflor.org school pages + NCES** — current status/config of every
  FFSD school; the district's posted restructuring plans (2019, 2027-28)
  explain the primary/intermediate/6th-grade-center name churn.
- **Living New Deal + Wikipedia 'McCluer High School'** — the
  Vogt → Ferguson HS → McCluer lineage with dates.
- **Wikipedia 'Kinloch High School'** — the segregated-school story
  (Black HS program at Dunbar 1936 → dedicated building 1938 → closed
  ~1976, students to McCluer North).

## Process friction for the scale-up decision

- **District-level rows resolve cleanly; single-school founding dates do
  not.** Court opinions and the PRiME consolidation map settle district
  dates definitively, but construction dates for ordinary elementaries
  (Johnson-Wabash, Walnut Grove, Mark Twain, the Robertson schools) are
  simply not indexed online. FFSD building inventories or DESE facilities
  records would be needed — recommend a human follow-up or a dedicated
  lookup for those rather than repeated web searching.
- **The 1960s county-wide annexation wave is under-documented.** Scudder
  (1960) and Robertson (~1964) dissolved into Berkeley with only scattered
  coverage; the Scudder annexation is confirmed only because one scanned
  newsletter survived. Expect similar fuzzy 1960s mergers in other batches
  where no survivor exists.
- **Segregated dual systems double the effective school count.** Each
  pre-1954 district here ran parallel white/Black schools, and the seed
  conflates them (e.g., "Kinloch High School" = the white school that
  became Berkeley HS AND the Black school opened 1938). Track B workers
  should check which segregated entity a yearbook target actually was.
- **Renaming waves break naive name matching.** FFSD's 2019 grade-center
  restructure renamed most elementaries (elementary→primary/intermediate/
  6th-grade center); a 2027-28 restructure reverses some of it. School
  name matching against yearbook catalogs must tolerate these suffix
  changes.
- **Recommended human follow-ups:** (1) Robertson district/school
  records — nothing beyond the 1964 HS closure is online; try FFSD
  administrative records or St. Louis County boundary-change files;
  (2) Berkeley district member-school list for ALL-401; (3) Mark Twain
  Elementary's original campus and the Mark Twain center's current status
  (board proposed closing it).
