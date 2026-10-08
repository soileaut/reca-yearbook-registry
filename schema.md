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

---

## Table 1: `schools`

One row per school entity (one row per `pilot_row_id` in the seed data,
though `school_id` is the permanent identifier going forward).

| Field | Type | Notes |
|---|---|---|
| `school_id` | string | Stable ID, e.g. `63147-01`. Carried over from seed `pilot_row_id` for the pilot. |
| `name` | string | Current/primary name. |
| `historical_names` | string[] | All known former names. |
| `zip` | string | |
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
