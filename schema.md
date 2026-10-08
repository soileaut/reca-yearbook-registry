# RECA Yearbook Registry — Data Schema (v0, pilot)

This is the shared contract that every research track (data cleanup, archive
survey) must output to, so results merge mechanically instead of requiring a
manual reconciliation pass. Any Devin session working on this project must
produce output in exactly this shape.

General rules for every field below:
- **Never leave a confidence/status field blank.** If something is not known,
  the value must explicitly be `unknown` — never inferred silently and never
  left empty.
- **Every non-obvious factual claim needs a citation** — a URL to the
  specific page/source found via web search. No citation = the claim must
  be marked `unverified`, not stated as fact.
- **Web search/browsing only.** Do not call, email, or otherwise directly
  contact any institution, library, archive, or individual. If something
  can only be resolved by contacting a person (e.g. "call the special
  collections desk"), do not do this yourself — instead record it as a
  recommended follow-up action for a human, in `notes`.
- **Do not fabricate sources.** If you cannot find a source, say so.

## RECA date scope

RECA coverage for the St. Louis area begins **January 1, 1949**, with no
defined end date (open-ended). This means:

- The first school year of real interest for residency evidence is
  **1948-1949** (the academic year spanning that start date). School years
  before this are not RECA-relevant on their own.
- For the `yearbook_registry` table, **prioritize and focus research effort
  on school years 1948-1949 and later.** A pre-1949 yearbook is not useless
  (it can still help confirm a school existed/had a program), but it is not
  the target deliverable — don't spend research budget chasing 1920s-1940s
  volumes unless they're trivially found alongside later ones in the same
  collection.
- This does **not** limit the `schools` table (Track A). A school's full
  history — including founding dates well before 1949 — remains relevant
  for establishing identity, consolidation, and successor relationships,
  since a pre-1949 founding date helps confirm which post-1949 entity is
  the right one to search for yearbooks.
- There is no upper-bound year — a 2020 yearbook is just as relevant as a
  1950 one.
- **Before starting an archive-survey (Track B-style) task, check each
  school's `reca_scope_status` in the relevant `schools_<scope>.json` file
  (see Table 1 below).** Skip any school marked
  `out_of_scope_closed_before_1949` entirely — do not search for its
  yearbooks at any institution. Schools marked `unknown_insufficient_data`
  should still be searched (benefit of the doubt until a human clarifies).

---

## Table 1: `schools`

One row per school entity (one row per `pilot_row_id` in the seed data,
though `school_id` is the permanent identifier going forward).

| Field | Type | Notes |
|---|---|---|
| `school_id` | string | Stable ID, e.g. `63147-01`. Carried over from seed `pilot_row_id` for the pilot. |
| `name` | string | Current/primary name. |
| `historical_names` | string[] | All known former names. |
| `zip` | string | The school's actual/home ZIP (where it's physically located). |
| `also_relevant_to_zips` | string[] | Other RECA-impacted ZIPs this school is relevant to because it served students from that community (even though it isn't physically located there) — e.g. a high school outside the ZIP that neighborhood kids attended. Empty list if none. |
| `district_operator` | string | |
| `school_type` | string | |
| `opened_year` | string | Year or `unknown`. |
| `opened_confidence` | enum | `confirmed` / `probable` / `unknown` |
| `opened_citation` | string | URL or source description. Required if confidence is not `unknown`. |
| `closed_year` | string | Year, `unknown`, or `n/a` (still open). |
| `closed_confidence` | enum | `confirmed` / `probable` / `unknown` |
| `closed_citation` | string | |
| `successor_school_id` | string | `school_id` of the school that absorbed this one's students/records, or `none`, or `unknown`. |
| `successor_confidence` | enum | `confirmed` / `probable` / `unknown` |
| `successor_citation` | string | |
| `notes` | string | Free text — research trail, ambiguities, dead ends. |
| `reca_scope_status` | enum | `in_scope` / `out_of_scope_closed_before_1949` / `unknown_insufficient_data`. **Do not set this field manually** — it is computed deterministically by `compute_reca_scope.py` from `closed_year`/`closed_confidence` after you produce your output. Leave it absent from your output; the script will add it. |

## Table 2: `yearbook_registry`

One row per `(school_id, year)` combination that was actually investigated.
**Do not generate a row for every year a school was open** — only create rows
where you did real work (found something, or made a genuine attempt and
concluded `not_found`). An empty/unresearched year should simply not appear
in this table yet, rather than appearing with hollow `unknown` values.

| Field | Type | Notes |
|---|---|---|
| `school_id` | string | FK to `schools`. |
| `year` | string | School year, e.g. `1973` or `1972-1973`. Use the literal value `all` for a row representing an exhaustive search of an institution's entire collection for a school with no per-year breakdown possible (e.g. a `not_found` result after checking all available indices) — do not use `all` if you found and are recording specific volumes; one row per actual year found in that case. |
| `existence_status` | enum | `likely_exists` / `likely_none_published` / `unknown` — whether a yearbook was plausibly ever produced for this school/year at all (independent of whether we've found a copy). |
| `existence_confidence` | enum | `confirmed` / `probable` / `unknown` |
| `existence_reasoning` | string | Why you believe this (e.g. "high school, operating that year, yearbook program confirmed in other years"). |
| `digitized_status` | enum | `digitized` / `physical_only` / `not_found` / `unknown` |
| `holding_institution` | string | e.g. "St. Louis County Library", or `none_found`. |
| `holding_format` | string | e.g. "PDF scan", "bound physical volume", "microfilm". |
| `access_info` | string | Call number, direct link, contact name/email, or similar — whatever is needed to actually act on this. |
| `citation_url` | string | Source for this specific row's claim. |
| `last_verified_date` | string | ISO date you did this research. |
| `verified_by` | string | Which task/session produced this row, e.g. `pilot-track-b-slcl`. |

---

## Output file format

Each Devin session should produce:
- `schools_<scope>.json` — array of `schools` rows (only the ones it touched).
- `yearbook_registry_<scope>.json` — array of `yearbook_registry` rows it
  produced (can be empty if a track doesn't touch this table).

Where `<scope>` identifies the task, e.g. `63147` for the ZIP 63147 pilot,
or `slcl` for the St. Louis County Library survey.

## Cross-ZIP school deduplication (`schools_master.json`)

A school that "serves" a community (e.g. the area high school) is often
included in multiple ZIP-scoped seed files — the same real-world school,
but potentially researched independently by separate Track A sessions,
creating duplicate `school_id`s for the same institution.

**Before starting any new Track A task, run:**
```
python3 merge_schools.py                              # refresh the master
python3 find_potential_duplicates.py <new_seed_file>   # check for overlaps
```

For any school the script flags as a likely match to an existing entry in
`schools_master.json`, tell the new Track A session explicitly in its task
prompt: *"School X already exists as `<school_id>` — do not create a new
entry. Instead, add this ZIP to its `also_relevant_to_zips` list, and only
research it further if the existing entry has unresolved
gaps (`unknown` fields) you can fill."*

This is a fuzzy-match tool, not an auto-merger — always have a human
confirm a flagged match is actually the same school before instructing an
agent to treat it as such, since similarly-named but distinct schools
exist (see the pilot's "Lutheran High School" / "North High School" decoy
collisions).

## Cross-institution deduplication (`yearbook_registry_master.json`)

`yearbook_registry_master.json` (repo root) is the running merge of every
`yearbook_registry_<scope>.json` produced so far — regenerate it with
`merge_registry.py` after merging a new task's output into `main`.

**Any archive-survey task (Track B-style, surveying a specific institution)
MUST read `yearbook_registry_master.json` before starting its search.**

Rule: for any `(school_id, year)` that already has a row in the master with
`digitized_status: digitized` — **do not actively spend search effort
re-finding it at the new institution.** Skip it and move to the next item.
This does NOT apply to `physical_only` or `not_found` rows; those should
still be actively searched at every institution, since a different
institution may succeed where another didn't, or hold a physical copy
worth knowing about even if a digital one already exists elsewhere.

If, while browsing an institution's collection for other purposes, you
incidentally notice it also holds something already marked `digitized`
elsewhere, it's fine (not required) to add a row noting the duplicate
holding — this can be useful for redundancy/preservation purposes — but it
should never come at the cost of time spent actively searching for it.
