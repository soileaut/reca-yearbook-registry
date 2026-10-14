# Track C notes — district lineage + successor research

Track C researcher pass over `schools_master.json` (340 schools). Deliverables:

- `schools_track_c_updates.json` — 166 schema-shaped rows (normalized `district_operator` + `successor_school_id` fills + appended notes + 6 minted rows). Merged via `merge_schools.py` (now dedupes on `school_id`; updates win; never downgrades a `confirmed` value).
- `districts_master.json` — 70 district/operator entries with formation/dissolution years and predecessor→successor chains.
- Regenerated `docs/flat_yearbook_registry.csv`, `publish/public_yearbook_registry.csv`, and `docs/public_yearbook_registry.csv`.

## Q1 — district_operator verification

**Convention applied (per track_c_prompt.md):** `district_operator` is the **final/primary operator of the school during its own life** — the entity running it at closure, or the current operator for open schools. Transfer history that previously lived inside the `district_operator` string is preserved verbatim in each row's notes ("District lineage (Track C): ...").

**Method:** the 170 raw `district_operator` strings were canonicalized era-aware: multi-segment strings like "Berkeley School District (1937-1975) / Ferguson-Florissant R-II (1975-2003)" were resolved by the school's own `closed_year` against the annotated eras. 127 rows were normalized; parish/archdiocese operator strings ("X Parish / Archdiocese of St. Louis") and unique private operators were left as-is (they are single-operator records, not transfer chains).

**District histories established (applied district-by-district, not school-by-school):**

| District | Formation | Fate | Source |
|---|---|---|---|
| Hazelwood SD (R-1) | 1949–51 annexation of **thirteen** rural districts | operating | 392 F.Supp. 1276; hazelwoodschools.org; PRiME/SLU |
| Ferguson-Florissant R-2 | Oct 1951 reorg vote → 1952 merger of Ferguson Public + Florissant SDs; annexed Berkeley+Kinloch eff. Feb 1, 1975 (388 F.Supp. 1058 / 515 F.2d 1365) | operating | McCluer HS Wikipedia; law.resource.org; PRiME |
| Pattonville R-III | Oct 1951 reorg over the pre-existing School District of Pattonville; absorbed Bridgeton (~1950), Mount Pleasant + Penn-Junction (~1951), Fee Fee No.16 (1930), St. Ann, Maryland Heights SD (1962) | operating | Pattonville district history; PRiME |
| Normandy SD → Normandy Schools Collaborative | NSD renamed NSC July 2014 under state supervision; absorbed Wellston 2010 | operating | Wikipedia NSC; normandysc.org |
| Kinloch SD No. 18 | split 1937 → Berkeley SD (white) + new Kinloch SD (Black) | dissolved | 515 F.2d 1365 |
| Berkeley SD | 1937 (from No. 18); absorbed Scudder 1960, Robertson ~1964 | dissolved 1975 → FFSD | 515 F.2d 1365 |
| Ritenour SD | rural district lineage from 1867 | operating | ritenourschools.org 100-facts |
| Riverview Gardens SD | ~1950 from Science Hill #20 + Moline | operating | riverviewgardens1969.myevent.com |
| Parkway C-2 | 1954 from Fern Ridge + Mason Ridge C-2 + Weber | operating | PRiME/SLU |
| Central School District R-II → Fort Zumwalt R-II | formed July 19, 1949 from 12 small districts (1947 reorganization law); later renamed Fort Zumwalt | operating | fzschools.org history (Wayback) |
| Consolidated SD No. 2 (St. Charles Co.) → Francis Howell R-III | organized May 8, 1915; named Francis Howell SD March 15, 1966 | operating | fhsdschools.org/about |
| Wentzville R-IV | current district (Holt HS est. 1896); formation year not documented online | operating | Wikipedia |
| Special School District of St. Louis County | 1957 | operating | ssdmo.org |
| School District of University City | predates 1949 wave | operating | ucityschools.org |
| School District of Washington | Washington MO | operating | washington.k12.mo.us |
| Baden local district | — | absorbed into SLPS 1876 | Wikipedia (Baden, St. Louis) |
| Junior College District of St. Louis–St. Louis County | 1962 → STLCC | operating | Wikipedia |
| Wellston SD | — | dissolved 2010 → Normandy | PRiME/SLU |

Rows whose `district_operator` was already correct were verified against the district-level history without edits (no change recorded for them). District entity rows (e.g. "Kinloch School District") carry their own name as operator.

## Q2 — successor_school_id gap adjudication

65 rows entered the queue (closed+`none`, closed+`unknown`, dead-end references). Resolved/confirmed **22 fills**:

**Dead-end successor IDs (8):** all traced to seed rows that dedupe folded into other representatives — i.e., the targets were real but the dedupe pass remapped them. Adjudications:

- `ALL-315` → `ALL-261` Buder Elementary (seed ALL-314 folded into ALL-261; documented 1939 Ashby replacement).
- `ALL-330` → `ALL-358` Normandy Middle School at Lucas Crossing (seed ALL-343 folded into ALL-358).
- `ALL-381` → `ALL-113` McCluer South-Berkeley HS (seed ALL-382 folded into ALL-113).
- `ALL-491` → `63147-10` Riverview Gardens HS (seed ALL-486 = same school as pilot row).
- `ALL-075` → `ALL-467` Twillman School - 1928 Building (seed ALL-465 was a duplicate of the continuing school).
- `ALL-073` → `ALL-464` — **the dead end was a real missing school**: Larimore Elementary (1025 Trampe Ln, still open) minted as its own row.
- `ALL-497` → `ALL-393` Kinloch HS (institution row; seed ALL-378 folded into ALL-114 Berkeley HS; per campus-row convention the Kinloch HS identity row is the right target).
- `ALL-048` "ALL-013; ALL-014" — **valid multi-value successor** (documented split to All Saints Academy's St. Norbert + St. Ferdinand campuses); kept as-is.

**New confirmed/probable fills:** ALL-023→ALL-905 (Brown Elementary, minted), ALL-025→ALL-464 (Larimore), ALL-108→"ALL-013; ALL-014" (ASA campuses), ALL-179→ALL-264 (Drummond), ALL-181→ALL-154 (Parkwood, documented replacement), ALL-292→"ALL-289; ALL-308; ALL-901" (Iveland; New Overland; Wyland — documented triple receivership), ALL-309→ALL-901 (Wyland), ALL-335→ALL-904 (Nerinx Hall), ALL-342→ALL-358 (Normandy Middle), ALL-349/351/352→ALL-902 (Lucas Crossing Elementary — documented receivers of Lincoln/McKinley/Harrison students, 2001), ALL-482/483→ALL-903 (Christ, Light of the Nations — the 2005 inter-parish receivership documented by STLPR), 63147-01→63147-02 (Nance Elementary, probable geographic receiver).

**Minted rows (per ALL-9xx convention):** ALL-464 Larimore Elementary, ALL-901 Wyland Elementary, ALL-902 Lucas Crossing Elementary, ALL-903 Christ, Light of the Nations School, ALL-904 Nerinx Hall, ALL-905 Brown Elementary.

**"No successor, records to district" adjudications** (successor kept `none` + note): ALL-076, ALL-094 (Jana → dispersed across Hazelwood elementaries), ALL-164, ALL-170–174, ALL-178, ALL-222, ALL-249, ALL-288, ALL-293, ALL-308, ALL-310, ALL-311 (1976 Ritenour reorganization receivers unnamed), ALL-390, ALL-396, ALL-397, ALL-398, ALL-408, ALL-428, ALL-449, ALL-494 (RGSD redistricting documented), ALL-508, ALL-510 (district-level successor = FFSD), ALL-646, 63147-08 (Beaumont → CTE building conversion).

**Kept `unknown` with adjudication notes:** ALL-011 (site tenant was a different institution), ALL-080 (multiple Deanery receivers), ALL-165/ALL-167 (Carver → integrated Pattonville elementaries; Remington is the unverified geographic candidate), ALL-220 (likely phantom row — no Bridgeton Senior HS documented), ALL-295 (Hope Lutheran receiver undetermined), ALL-332 (Bel-Ridge receivers not documented — Obama took Garfield/Pine Lawn, not Bel-Ridge), ALL-348 (Roosevelt 1938 receiver undocumented), ALL-362 (PAL Center — probable rename into CASA branding), ALL-395 (Dunbar closure year itself conflicting), ALL-513 (seed location likely erroneous; south-city St. John the Baptist dispersed).

## Q3 — districts_master.json

70 entries: all canonical operators present in `district_operator` (normalized set) plus predecessor districts discovered through the consolidation research (13 Hazelwood rural districts incl. Rosary/Garrett/Bonfils which never had school rows; Penn + Junction behind Penn-Junction; Scudder/Robertson/Wellston behind Berkeley/Normandy; the Parkway and FHSD/Central R-II predecessor formations).

**Known limitations:** Wentzville R-IV's own formation year, the Central R-II → Fort Zumwalt rename year, RGSD's exact formation year, and the Penn/Junction → Penn-Junction merger year are not documented online — recorded `unknown`/`probable` per cite-or-unknown rules. Melrose District No. 57's receiving district is undocumented.

## Merge semantics

`merge_schools.py` was naive concatenation — it would have duplicated all 166 update rows into the master. Patched to dedupe by `school_id` (later files win per rglob ordering; the updates file sorts after `schools_master.json`). Regenerated downstream artifacts afterward so `terminal_successor` picks up the resolved chains.

---

## Addendum — Q4: who holds the records today?

Every `districts_master.json` entry now carries a `records_office` block:
`{"name","address","phone","url","confidence","citation","notes"}`. Result:
**25 confirmed, 42 probable, 3 unknown** — the actionable endpoint for a
dissolved district is always its successor's office.

### Method

- **Operating districts/operators (confirmed):** registrar/records/custodian-of-records
  contacts taken from each organization's public site (per-school research was out of
  scope; the district office is the endpoint a records request actually reaches).
- **Dissolved districts (probable):** custodian derived from `successor_district_id`
  under Missouri DESE guidance — "if the school you attended is no longer open,
  contact the superintendent's office of the district that now serves the area"
  (https://dese.mo.gov/transcripts-and-diplomas). Successor office details are
  mirrored into the dissolved entry so each row is self-contained; chains of
  dissolved districts (e.g. Fee Fee → School District of Pattonville → Pattonville
  R-III) resolve to the final successor.
- **Never contacted anyone** — lookup only, per the standing rule.

### Key custodian findings

- **Archdiocese of St. Louis Archives** (Office of Archives and Records,
  20 Archbishop May Dr, 314-792-7020, archives@archstl.org) is the documented
  repository for **all closed archdiocesan schools and closed parishes** —
  transcripts, yearbooks, photos. Open Catholic schools keep their own records.
  It runs a transcript-request page ($10/copy, photo ID required) and a dedicated
  **RECA page** (archstl.org/reca). All parish schools in the registry route here
  via DIST-401; All Saints Academy (closed 2023) too (DIST-402).
- **SLPS Student Transcript Office** (801 N. 11th St, 314-645-2648) — records for
  every current/former city school incl. Baden-district schools annexed 1876;
  $3 transcripts, $10 genealogy searches.
- **Pattonville** maintains an explicit **RECA Record Requests** section on its
  Community page (student + staff forms) — the best-documented RECA endpoint in
  the region. Custodian for all 7 dissolved Pattonville-feeder districts.
- **SSD of St. Louis County** (Student Records Dept, 12110 Clayton Rd,
  e-records@ssdmo.org / fax 314-989-8170) — custodian of **special-education
  records for every St. Louis County public district**, not just its own schools.
- **Sisters of Loretto** records stayed with the order: Loretto Heritage Center
  Archives, Nerinx KY (270-431-0096, lorarchives@lorettocommunity.org) — NOT the
  Archdiocese. This is where Loretto Academy (closed ~1952) records live.
- **Missouri DYS** case records are confidential (13 CSR 110-2.140); formerly-
  committed youth 18+ may request their own records in writing w/ photo ID or
  notarized request (AskDYS@dss.mo.gov, 573-751-3324). Covers Fort Bellefontaine.
- **FHSD** guidance pages list a dedicated **"Transcript request for RRECA"**
  option for past graduates.

### Successor-school vs. original-district custody (per the ask)

For schools with a resolved `successor_school_id`: records follow the
**district**, not the building. A school that closed but whose district survives
(e.g. Ritenour elementaries) → that district's office. A school whose district
dissolved → the successor district's office (e.g. Kinloch No.18 → FFSD; Wellston
→ Normandy SC). The successor *school* inherits students/programs; it does NOT
inherit records — the district office does. Yearbooks specifically may also be
in school libraries/alumni hands, but the records office is the documented
custodian for transcripts and administrative files.

### Left unknown

- DIST-120 Melrose No.57 — receiving district at dissolution undocumented
  (same limitation flagged in the district research).
- DIST-208 St. Charles County common districts — pre-1949 consolidation records
  custody undocumented; SHSMO / St. Charles County Historical Society plausible.
- DIST-409 Olivet University — small private operator, no public records office
  found; MDHE closed-school repository is the fallback if defunct.
