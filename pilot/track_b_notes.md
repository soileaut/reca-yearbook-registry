# Track B — SLCL Archive Survey: Process Notes (ZIP 63147)

Date: 2026-10-07 · Session: `pilot-track-b-slcl` · Output: `yearbook_registry_slcl_63147.json` (61 rows)

## How searchable is SLCL's yearbook collection?

**Searchable online — two complementary sources, no login or contact required.**

1. **SLCL Digital Archives** (Recollect CMS) — https://slcl.recollectcms.com
   - Dedicated "Yearbooks" hub: https://slcl.recollectcms.com/pages/yearbooks
   - "St. Louis Yearbooks" collection (node 1267) contains **90 school-level subcollections** of digitized yearbooks (~1,404 individual items site-wide per the homepage facet count). Each item page exposes metadata plus a PDF download.
   - The subcollection index is effectively an authoritative inventory of *which schools* SLCL has digitized — browseable alphabetically, so "is school X present?" is answerable in one pass.
   - Caveat: the subcollection list and per-school volume lists are JS-rendered and not visible in raw page fetches or naive scraping. They are retrievable via the Recollect browse endpoint: `https://slcl.recollectcms.com/nodes/search?bid=<collection-node-id>&orderby=node_title&order=asc`. A browser session (or scripted fetch of that endpoint) is needed to enumerate volumes; do not rely on `?q=` — it is not a keyword filter.
   - Note per collection page for some schools (e.g. Affton): volumes **from 2000 onward may require in-branch access** even though item records appear online. All volumes found for this pilot predate 2000 and show open PDF downloads.

2. **Physical holdings list** — https://www.slcl.org/yearbooks-and-alumni-publications
   - A flat alphabetical table ("Yearbooks and alumni publications", updated August 2015) of yearbooks, alumni directories, reunion booklets, and indexes held in the History & Genealogy Dept.'s **closed stacks** — viewing requires asking a librarian in person. ~1,149 rows including non-Missouri items.
   - **Process note:** the live page returned HTTP 403 to automated fetches; the table was parsed from the 2025-03-22 Wayback Machine snapshot. Recommend a human re-check the live page periodically, since the 2015 list is likely stale relative to the digital archive (digitized additions like Beaumont 1929/1936/1949 and Riverview 1967/1970/1971/1973/1979 are absent from it).

3. **General catalog** (slcl.org) — not needed and not systematically searched; the two sources above are SLCL's authoritative yearbook surfaces. The physical list also includes entries for the digitized schools, so it functions as a physical-holdings inventory rather than a complement of undigitized-only items.

## Findings vs. the 12 pilot schools

- **Beaumont High School (63147-08)** — strong holdings: **24 digitized volumes** (1926–1952 incl. Jan./June split issues) + **10 physical-only volumes** (1953–1964), plus a 1926–1936 anniversary volume and a 1961–1964 index in the physical list (not recorded as registry rows since they aren't yearbook volumes).
- **Riverview Gardens Senior High School (63147-10)** — **17 digitized volumes** (1967–1992, gaps). Physical list also shows a *Riverview Gardens Central Junior High* 1971 "Saber" — a feeder school, recorded here only as a mention.
- **All other 10 schools** — explicit `not_found` rows. Highlights:
  - The four "Baden" entities (elementary, district, public school, high school lead) return nothing — SLCL does not appear to hold any Baden-specific yearbook.
  - "North High School" (63147-09) has no SLCL match; several decoy "North" collections exist (North Side Catholic, North County Tech, McCluer North, Parkway North) — name-similarity checking matters.
  - Florissant Valley CC is absent even though the physical list carries two other STLCC campuses (Forest Park, Meramec). UMSL is absent (UMC Savitars only).
  - Elementary schools (Baden, Nance, Herzog) unsurprisingly have nothing — elementary yearbooks barely exist in the collection at all.

## On the "~92 volumes" figure

The figure in the prompt does not match what was found — but the discrepancy is informative: SLCL's digitized St. Louis yearbook collection is organized as **~90 school-level collections** (possibly the origin of "~92"), comprising **~1,400 individual volumes**; the separate physical closed-stack list contains ~1,149 line items statewide. SLCL's yearbook holdings are far larger than ~92 volumes in aggregate — any scaled survey should cite per-school volumes, not a single institutional total.

## Recommendations for scaling (SLU, UMSL, WashU, Mizzou, etc.)

- **Two-pass method worked well:** enumerate the institution's collection index first (authoritative school list), then diff against the seed's name variants — rather than one keyword search per school name. Only feasible where a browseable collection/finding aid exists; for institutions with only a general catalog, per-name keyword search is unavoidable.
- **Record the browse-endpoint trick per platform** — each digital-archive vendor (Recollect, CONTENTdm, Digital Commons) renders holdings differently; a short "how to enumerate" note per institution type will save every future session trial-and-error time.
- **Expect decoy name collisions** ("North High School", "Lutheran High School"); registry rows should always record the distinguishing geography in reasoning.
- **Physical finding aids lag digital collections** — treat a dated holdings page as a lower bound, and always cross-check the digital portal separately.
- **University archives** (UMSL, WashU, Mizzou) typically self-host their yearbook archives rather than depositing at public libraries — expect their collections to live on the universities' own digital platforms, a different search surface than SLCL-style public-library catalogs.
