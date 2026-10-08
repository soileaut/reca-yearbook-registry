# Track A Coordinator — Scale-Up Data Cleanup (All Remaining Schools)

## Context

You are the coordinator session for a research project supporting a
yearbook digitization effort for RECA (Radiation Exposure Compensation Act)
claimants in the St. Louis, Missouri area. A pilot already validated this
process on 12 schools (ZIP 63147) — see `pilot/schools_63147.json` and
`pilot/track_a_notes.md` for what "good output" looks like.

Your job is **not** to do the research yourself. Your job is to **partition
the remaining work and spin up a managed Devin session (child) for each
batch**, using the "Agent Fan-Out" capability — one child per batch,
running in parallel, each following the same task contract.

## Step 1: Read the contract

Read these files first, in full:
- `schema.md` — the data schema and rules every child MUST follow
  (web-search-only, no fabrication, cite-or-mark-unverified, RECA date
  scope, `reca_scope_status`).
- `pilot/track_a_prompt.md` — the original pilot task spec. Each child's
  task is the same kind of work, just scoped to a different batch of
  schools instead of ZIP 63147.
- `pilot/schools_63147.json` — a worked example of correct output format.

## Step 2: Read the pre-built, deduplicated work list

Deduplication has already been done and committed — do NOT re-derive it,
just read the results:

- `data/all_schools_seed.json` — the full 650-row raw source (reference
  only, you shouldn't need to touch this directly).
- `schools_master.json` (repo root) — 12 schools already researched (the
  ZIP 63147 pilot).
- `data/schools_seed_deduped.json` — **this is your actual work list.**
  325 unique schools (already excludes the 12 pilot schools and 12 more
  repeat appearances of already-researched schools like STLCC-Florissant
  Valley/UMSL, and already self-deduplicated against internal repeats in
  the raw data). Each entry is `{"representative": <row>,
  "duplicate_row_ids": [...]}` — use `representative` as the school to
  research.
- `data/schools_seed_deduped_review_needed.json` — 63 rows flagged as
  fuzzy/campus-variant near-matches that were deliberately NOT
  auto-merged (e.g. "Pattonville Heights Middle School" vs "Pattonville
  High School" — similar text, different schools; or "Hazelwood High
  School - Original Campus" vs a same-named-but-different campus). These
  are already included as their own separate entries in
  `schools_seed_deduped.json` — this file is purely informational, so
  children researching them can see WHY a similarly-named school exists
  nearby and avoid confusing the two. Do not merge any of these yourself.

## Step 3: Partition into batches

- Split the 325 representative schools in `data/schools_seed_deduped.json`
  into batches of **approximately 15 schools each** (the pilot's
  12-school batch was a good, manageable size for one session to do
  careful, well-cited research on — don't go much bigger).
- You do not need to partition by ZIP or geography — these are just
  "impacted schools" with no ZIP-specific logic downstream. Arbitrary
  sequential batches are fine.
- Write each batch's rows to its own seed file, e.g.
  `batches/schools_seed_batch01.json`, `batches/schools_seed_batch02.json`,
  etc. (create the `batches/` directory). Use the `representative` row's
  fields as the seed data for that batch (same shape as the pilot's
  `pilot_seed_63147.json`).

## Step 4: Spin up one managed child Devin per batch

For each batch, create a child session with a task prompt that:
- Points it at `schema.md` and its own `batches/schools_seed_batchNN.json`.
- Is otherwise the same task as `pilot/track_a_prompt.md` (verify
  opened/closed years, resolve successor/consolidation relationships, flag
  phantom/unresolved entities, web-search-only, no fabrication).
- **Explicitly calls out the "Administrative district disambiguation"
  rule in `schema.md`.** Several rows are named like a governing body
  ("X School District," "Y R-3 School District") rather than a single
  school — the child must investigate and set `entity_type` for every
  such row rather than treating the name at face value. Don't let this
  get missed just because it's buried in the schema doc — mention it
  directly in the child's task prompt.
- Instructs it to output `batches/schools_batchNN.json` (schools table
  rows) and `batches/track_a_notes_batchNN.md` (process notes), matching
  the pilot's output pattern.
- Tells it to commit its output to a new branch
  (`track-a/batchNN`) and report back when done — do not have children
  merge to `main` directly.

Run batches in parallel where the tooling allows it.

## Step 5: After children finish

- Do not do this until ALL child sessions report completion.
- For each batch's output branch, run `python3 compute_reca_scope.py
  batches/schools_batchNN.json` to add the `reca_scope_status` field
  (this is deterministic — do not let children compute it themselves).
- Merge all batch branches into a single integration branch.
- Run `python3 merge_schools.py` to regenerate `schools_master.json` across
  everything (pilot + all new batches).
- Run `python3 json_to_csv.py schools_master.json` so the result can be
  visually spot-checked.
- Produce a short summary: total schools processed, how many ended up
  `in_scope` vs `out_of_scope_closed_before_1949` vs
  `unknown_insufficient_data`, and any notable data-quality flags any child
  raised (phantom schools, unresolved identities, etc. — aggregate these
  into one list, don't just leave them scattered across batch notes).
- Push the integration branch and open a PR to `main`. Do not merge it
  yourself — a human will review.

## Guardrails (apply to you AND every child you spin up)

- **Web search/browsing only.** No calling, emailing, or otherwise
  contacting any person or institution, ever.
- **No fabrication.** Every child must cite real sources or mark fields
  `unknown`/`unverified`. If you notice a child's output looks fabricated
  (suspiciously clean, no real citations, implausibly complete), flag it
  in your final summary rather than passing it through silently.
- **Do not modify `schema.md`, `pilot/`, or anything under `data/`.** Only
  create new files under `batches/` (plus the merge outputs in Step 5).
