# Track C — Districts & Consolidation Chains (single-worker)

You are the sole researcher for Track C of the RECA yearbook registry
project (repo: `soileaut/reca-yearbook-registry`). Clone from `main`,
work on a `track-c/research` branch, and open a PR when done — do not
merge it yourself.

## Required reading, in order

1. `schema.md` — the data contract. Do NOT modify it; school rows must
   stay schema-shaped.
2. `DATA_PIPELINE.md` — project history and rules (web search/browsing
   ONLY; never contact any institution or person; no fabrication;
   cite-or-mark-`unknown`; prefer keeping questionable rows flagged over
   deleting them).
3. `NEXT_STEPS.md` §1 — includes the two Track-C-relevant backlog items
   (dead-end successor links; unestablished successors).
4. `schools_master.json` — the 340-school dataset you'll be annotating.

## The three questions

1. **Which district owned each school, and when?** Verify `district_operator`
   for every school. Where a school transferred between districts over
   time, keep `district_operator` as the final/primary operator and
   record the transfer history in the school's `notes` field
   (schema-allowed free text).
2. **What was each closed school consolidated into?** Fill
   `successor_school_id` gaps — 193 schools have `closed_year` +
   `successor: none`, 66 have `unknown`, and ~7 point at school_ids that
   don't exist (dead ends: `ALL-343`, `ALL-465`, `ALL-382`, `ALL-486`,
   `ALL-314`, `ALL-378`, `ALL-464`, `"ALL-013; ALL-014"`). Resolve what
   you can; leave genuinely-unverifiable ones as `unknown` with a note.
   If a dead-end target turns out to be a real missing school, mint a
   new `ALL-9xx` row (precedent: `schools_lutheran_hs.json`).
3. **Which districts absorbed which?** Build `districts_master.json` —
   a NEW entity table (districts are currently only strings in
   `district_operator`). One entry per district appearing in the master
   plus districts discovered through consolidation research, each:

   ```json
   {
     "district_id": "DIST-001",
     "name": "Ferguson-Florissant R-II School District",
     "type": "public | parish_system | private_operator | county_special",
     "formed_year": "1952 or null",
     "dissolved_year": "1975 or null (null = still operating)",
     "predecessor_districts": ["DIST-0xx"],
     "successor_district_id": "DIST-0xx | none | unknown",
     "confidence": "confirmed | probable | unknown",
     "citations": [{"url": "...", "note": "..."}],
     "notes": ""
   }
   ```

## Method — work district-by-district, not school-by-school

Pick a district, establish ITS consolidation history once (formation,
renames/reorganizations, mergers in and out), then apply it to every
school listing that district as operator. This is both faster and more
consistent than 340 independent school lookups. Useful source classes:
MO DESE records, district "history of" pages, newspaper coverage of
consolidation votes/dissolutions, the archive citations already in
`schools_master.json` rows.

## Output mechanics

- Emit changed/added school rows to `schools_track_c_updates.json` in
  schema shape; merge via `merge_schools.py` per repo process. Verify
  merge semantics first — never overwrite a `confirmed` value with a
  lower-confidence one; additive corrections only.
- Write `districts_master.json` per the shape above.
- Write `track_c_notes.md`: what you resolved, what stayed unknown and
  why, dead-end successor adjudications, and any district consolidations
  you found that change how the school list should be read.
- After merge, regenerate `flat_yearbook_registry.csv` and
  `publish/public_yearbook_registry.csv` (see existing scripts) so the
  `terminal_successor` column picks up resolved chains.

## Scope notes

- Many closed elementary/parish schools genuinely have no successor
  school — records went to the district/parish system. "No successor
  school, records to district X" IS a valid answer; record it in notes
  rather than forcing a successor.
- RECA scope (1949+) still applies for prioritization, but Track C is
  about lineage — a school's full history is relevant even if its
  yearbook range is limited.
