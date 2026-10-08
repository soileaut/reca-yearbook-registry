# Track A Notes — Batch 08 (Pattonville / Bridgeton / St. Ann / Hazelwood edges)

Date of research: 2026-10-08. Output: `schools_batch08.json` — 15 rows, one per seed
row; count unchanged (no merges or splits). `reca_scope_status` intentionally absent
per schema (computed downstream by `compute_reca_scope.py`).

## Confirmed vs. unknown

**Fully confirmed (opened + closed/status with citations):**
- `ALL-180` Carrollton Elementary — opened 1960, 3936 Celburne, Bridgeton; closed
  with the Lambert runway buyout (see year discrepancy below); students went to
  Drummond Elementary (successor confirmed). Building demolished.
- `ALL-182` Maryland Heights School District (Rural District 24) — founded 1924,
  merged into Pattonville 1962; member schools enumerated (Maryland Heights
  School/HS at 115 Harding, Remington Elementary, Carver Elementary for Negroes).
  `administrative_district_only`; successor ALL-184.
- `ALL-183` Pattonville Consolidated School District R-3 — name era Oct. 27, 1951
  (special election; Junction + Mount Pleasant merged in) → 1958 rename.
  `administrative_district_only`; successor ALL-184.
- `ALL-184` Pattonville R-3 School District — renamed 1958, still operating.
  `administrative_district_only`; member schools listed in notes.
- `ALL-198` Pattonville High School (current campus) — opened 1971 at 2497 Creve
  Coeur Mill Rd (dedicated Jan. 7, 1973); the school entity dates to March 17, 1936
  at the original 11055 St. Charles Rock Rd site (now Holman Middle School). Open.
- `ALL-222` Airport Elementary — opened 1954 (City of Berkeley RFP; Szombathy v.
  Ferguson-Florissant appellate record corroborates), closed end of 2018-19 school
  year under the FFSD redistricting plan (STLPR); city bought it in 2023.
- `ALL-249` Old Elm Grove School — built 1852, closed 1952 on organization of the
  Hazelwood School District (City of Hazelwood marker via HMDB); moved to Brookes
  Park (1961 or 1966 — sources conflict), rebuilt to 1890s appearance.
- `ALL-261` Buder Elementary — opened September 1939, replacing the Ashby School
  portable; closed 1981-1986 then reopened; still open.
- `ALL-262` Hoech Middle School — opened January 1955 as Hoech Junior High
  (1953 bond; property bought 1952); still open.
- `ALL-264` Drummond Elementary — opened August 2002 (dedicated Aug. 29) on the
  former St. Ann Elementary / Hope Lutheran site, 3721 St. Bridget Lane; still open.
- `ALL-266` Pattonville Early Childhood Center — opened August 2018 in the former
  Briar Crest Elementary (1965-2013) building at 2900 Adie Rd; still open.

**Probable:**
- `ALL-181` Pattonville Grade School ("Original District School") — opened 1907
  confirmed; the seed's 1930 is the district's reorganization year. Closed 1978 is
  recorded as probable: the lineage ran Grade School (1907) → Pattonville
  Elementary (1954) → closed 1978, but the district history lists the two names in
  different sections and the exact rename/rebuild moment is murky.
- `ALL-253` Melrose School #57 — opened c.1859 probable (county rural-school
  inventory); closure unknown (see flags).

**Left unknown / unresolved:**
- `ALL-202` "St. Charles Rock Road School" — no school by that literal name. Best
  candidate is Junction School (opened 1869 at St. Charles Rock Rd & Natural
  Bridge, merged into Penn-Junction 1936); alternates: the original Pattonville HS
  building at 11055 St. Charles Rock Rd, or Penn School on Old St. Charles Rock Rd.
- `ALL-220` "Bridgeton Senior High School" — likely phantom. No evidence a
  Bridgeton public high school ever operated; the Bridgeton School District
  (inc. 1864) ran elementary-level schools and was annexed into Pattonville in the
  1949-50 school year (matching the seed's 1950 close). Bridgeton teens would have
  attended Pattonville HS (post-1936) or tuition high schools (Ritenour, Normandy,
  University City).

## Data-quality flags (for the coordinator)

1. **`ALL-220` Bridgeton Senior High School is a likely phantom row** — same
   category as the pilot's "Baden High School."
2. **`ALL-222` Airport Elementary has a wrong district and wrong community in the
   seed.** It is a Ferguson-Florissant school at 8249/8429 Airport Rd, Berkeley
   63134 — not Pattonville, not Bridgeton/Earth City 63045. Also a probable
   cross-batch duplicate of `ALL-390` "Airport Elementary School - Historical
   Campus" (flagged pair in `schools_seed_deduped_review_needed.json`).
3. **`ALL-253` Melrose School #57 has a wrong location in the seed.** The real
   building is at 18820 Melrose Rd, Wildwood 63038 (west county, ~25 mi from
   Hazelwood) — NOT "Hazelwood predecessor" / "Florissant 63031." This row may be
   out of the target region entirely; recommend coordinator review.
4. **`ALL-249` Old Elm Grove School** is a probable duplicate of `ALL-027`
   "Elm Grove School" in another batch (flagged pair in the review file).
5. **`ALL-198` / `ALL-148` / `ALL-149`** are one continuous Pattonville High School
   across two campuses (1936 site → 1971 site). Kept separate per batching; single
   yearbook series.
6. **`ALL-180` Carrollton vs `ALL-179` Carrollton Oaks** — different buildings,
   both closed in the Lambert buyout and both succeeded by Drummond; don't merge.
7. **Administrative-district rows `ALL-182`, `ALL-183`, `ALL-184`** are
   `administrative_district_only` — redirect yearbook effort to member schools.
   `ALL-181` is `individual_school` despite the "School District" in its seed name.
8. **Closure-year discrepancy for Carrollton:** district school-profile list says
   "closed in 2001," the district timeline and Wikipedia put the effective closure
   at the 2002-03 boundary change (matching the seed's 2002). Recorded 2002.
9. **Elm Grove move year conflict:** 1966 (HMDB marker, seed) vs 1961 (Hamilton
   inventory, Flo Valley News). Operating dates unaffected.
10. **St. Ann Elementary** (not in batch) occupied 3721 St. Bridget Lane until
    1982 — the exact address later reused by Drummond. Worth noting if a
    St. Ann Elementary row exists elsewhere in the dataset.

## Useful sources for reuse

- **psdr3.org/about/history and /about/history/by-the-years** — the Pattonville
  district's own history pages are exceptionally detailed: building open dates,
  addresses, first principals, closures, consolidations, and the full
  district-name chronology (1930 formation, Oct. 27 1951 R-3 reorganization, 1958
  rename, 1962 Maryland Heights merger, 1949-50 Penn/Bridgeton annexations).
  Single most useful source for any batch touching Pattonville, Bridgeton,
  Maryland Heights, or St. Ann.
- **sites.google.com/psdr3.org/pattonvillehistory** — the district's deeper
  history site (same content, plus "Evolution of Pattonville" narrative with the
  Rural District 24 and merger details).
- **ritenourschools.org/community/history-of-ritenour/100-facts** — per-school
  open dates for Ritenour buildings (Buder, Hoech, Ashby, etc.).
- **HMDB.org** — historical-marker text for one-room schools (Elm Grove).
- **stlouisarchitecture.org Spring 2013 newsletter** — Esley Hamilton's
  "Surviving Rural Schools in St. Louis County" is a county-wide inventory of
  numbered rural districts (#1-#78) with addresses, dates, and current status —
  the definitive lead for any "District #NN" or one-room-school seed row.
- **Municipal document archives** — the City of Berkeley's eGov document portal
  contained the Airport Elementary construction/closure history (RFP + purchase
  agreement); city PDFs are worth grepping for other schools.
- **Court opinions** — Szombathy v. Ferguson-Florissant (Mo. App. 1984) gave the
  1954 Airport Elementary construction date; State ex rel. School Dist. No. 24 v.
  Neaf (Mo. 1939) corroborates Maryland Heights' district number.

## Process friction

- **Seed ZIP/community attributions are unreliable for borderline rows** — two of
  15 rows (Airport Elementary, Melrose #57) were materially mis-attributed, and
  one (Pattonville HS) had a borderline ZIP (63044 vs actual 63043). At scale,
  verify the named school's actual address before trusting the seed's geography.
- **Pattonville Grade School vs Pattonville Elementary naming** in the district's
  own history is inconsistent (listed in different sections with different
  "opened" years for what appears to be one continuous site). Resolved as a
  single lineage; flagged for the coordinator.
- **"School District" seed names conflate district and school** — the batch
  contained three pure district-name eras (Rural District 24, Consolidated R-3,
  R-3) plus one row ("Original District School") that was really a school. The
  `entity_type` disambiguation requirement worked well here.
- **One-room/rural schools close via district consolidation, not school
  closure** — the closing event is usually the 1947-54 merger wave, and the
  receiving *school* is rarely documented online; expect `successor: unknown`
  with a district-level explanation for most of these.
- **Recommended human follow-up:** Wildwood Historical Society (Melrose School
  records/photos), St. Louis County Library Bridgeton local-history index
  (resolves whether any Bridgeton public high school existed — the index cites a
  Bridgeton history book, p. 73 for the district).
