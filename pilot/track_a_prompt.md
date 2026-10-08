# Pilot Track A — Data Cleanup & Consolidation Research (ZIP 63147)

## Context

You are working on a research project supporting a yearbook digitization
effort for RECA (Radiation Exposure Compensation Act) claimants in the St.
Louis, Missouri area. A prior AI pass produced a messy spreadsheet of
schools believed to have existed in RECA-impacted ZIP codes. Your job is to
clean up and verify the data for ONE small ZIP code (63147) as a pilot, so
the approach can be validated before scaling to the full ~650-row dataset.

This is a pilot of 12 schools. Work carefully and show your reasoning — the
goal right now is to validate the *process*, not just produce output fast.

## Input

The seed data is at `pilot_seed_63147.json` (attached/provided alongside this
prompt) — 12 rows, each with a `pilot_row_id` (e.g. `63147-01`) that you
should use as the `school_id` going forward.

## Schema

Read `schema.md` (in the parent directory) carefully before starting. Your
output MUST conform to the `schools` table schema defined there. Do not
invent new fields or skip required confidence/citation fields.

## Task

For each of the 12 schools in the seed data:

1. **Verify or correct `opened_year` and `closed_year`.** The seed data has
   many `Unknown` values and some vague ones (`"1900s"`, `"1950s"`). Try to
   narrow these down using: Missouri DESE historical records, St. Louis
   Public Schools board records/history pages, local historical societies,
   newspapers.com or other historical newspaper archives, city directories,
   Wikipedia (as a lead only — always find a primary/secondary source to
   back up anything Wikipedia claims), and the school's own "About/History"
   page if it still exists.

2. **Resolve consolidation/successor relationships.** Several of these rows
   are explicitly flagged as predecessor/successor candidates in their
   `Notes` field (e.g. `Baden School District` → `Baden Public School` →
   `Baden High School`; `North High School` and `Riverview Gardens High
   School` marked `Current/Successor`). For each closed/historical school,
   determine: did it merge into another school in this list, a school
   outside this list, or simply close with no clear successor? Record your
   confidence honestly — "probable" based on circumstantial evidence
   (geographic proximity, timing, district history) is fine and expected;
   just don't call something "confirmed" without a real citation.

3. **Do not fabricate.** If after a genuine search you cannot find
   something, set the field to `unknown` and briefly note what you tried in
   `notes`. A well-documented "I couldn't find this, here's what I checked"
   is a successful outcome, not a failure.

4. **Flag anything surprising.** If you discover the seed data is simply
   wrong (e.g. a school name doesn't exist, or two seed rows are actually
   the same school under different names), note this explicitly — don't
   silently merge or delete rows.

5. **Web search/browsing only — do not contact anyone.** Do not call,
   email, or otherwise directly contact any school, district, library,
   archive, or individual. If something can only be resolved by contacting
   a person, do not do this yourself — record it as a recommended
   follow-up action for a human in `notes`, and leave the field `unknown`.

## Output

Produce `schools_63147.json` — an array of 12 (or more, if you split a
row that was actually two conflated schools, or fewer if you merge two rows
that are the same school — explain any count change) objects conforming to
the `schools` table schema in `schema.md`.

Also produce a short `track_a_notes.md` summarizing:
- What you were able to confirm vs. leave as `unknown`, and roughly why some
  were harder than others.
- Any sources that were particularly useful (for future tracks to reuse).
- Any process friction — e.g. "DESE historical records don't go back far
  enough," "no good online source exists for closure dates before 1960" —
  so we can adjust the approach before scaling to the full dataset.

## Out of scope

- Do not attempt the archive/holdings survey (whether yearbooks exist or
  are digitized) — that's a separate track.
- Do not touch rows outside ZIP 63147.
- Do not modify `schema.md`.
