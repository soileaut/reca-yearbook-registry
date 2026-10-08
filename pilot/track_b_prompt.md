# Pilot Track B — Archive Survey: St. Louis County Library (ZIP 63147)

## Context

You are working on a research project supporting a yearbook digitization
effort for RECA (Radiation Exposure Compensation Act) claimants in the St.
Louis, Missouri area. We need to know, for a specific small set of schools,
whether the St. Louis County Library (SLCL) holds any yearbooks for them —
digitized or physical — as a pilot before scaling this survey to other
institutions and the full school list.

SLCL is known to have a yearbook collection of roughly 92 volumes total
(across all schools, not just these). Your job is to find out how many, if
any, apply to this specific list of 12 schools.

This is a pilot. Work carefully and document your process — the goal is to
validate whether this kind of survey is even feasible against SLCL's online
presence, not just to produce a fast answer.

## Input

The schools to check are the 12 rows in `pilot_seed_63147.json` (in the
parent directory). Use the `School Name` and `Historical/Former Name`
fields — search under all known names for each school, since yearbooks are
often cataloged under the name used at time of publication, not the current
name.

## Schema

Read `schema.md` (in the parent directory) carefully before starting. Your
output MUST conform to the `yearbook_registry` table schema defined there.

## Task

1. **Find SLCL's yearbook collection online.** Start with SLCL's website,
   digital collections portal, and online catalog. If SLCL has a
   dedicated "yearbook collection" finding aid or digital exhibit, use it
   as your primary source. If not, search their general catalog.

2. **For each of the 12 schools**, search by every known name variant and
   record what you find:
   - If SLCL holds any yearbook(s) for that school (digitized or physical),
     record one `yearbook_registry` row per year/volume found, with
     `digitized_status`, `holding_format`, and `access_info` (call number,
     direct link to the digital copy, or whatever is needed to act on it).
   - If you search and find nothing for that school, still record this —
     set `digitized_status` to `not_found` for that school with a note of
     what you searched. Absence of evidence should be visible, not silently
     dropped.

3. **Web search/browsing only — do not contact anyone.** Do not call, email,
   or otherwise directly contact SLCL or any staff member. If resolving
   something would require contacting a librarian (e.g. an item isn't in
   the online catalog but might exist in an unlisted physical collection),
   do not do this yourself — record it as a recommended follow-up action
   for a human in `notes`, and mark the item `unknown`/`unverified`.

4. **If SLCL's catalog is not practically searchable this way** (e.g. no
   online catalog, no search by school name, requires an in-person visit),
   say so explicitly and clearly in your output notes rather than guessing
   or giving up silently. This is itself a useful and expected pilot
   finding.

5. **Do not fabricate catalog entries, call numbers, or links.** If you are
   not confident a source is real and accurate, mark it `unverified` and
   explain why in `notes`, rather than presenting it as confirmed.

## Output

Produce `yearbook_registry_slcl_63147.json` — an array of
`yearbook_registry` rows conforming to the schema in `schema.md`, covering
all 12 schools (including explicit `not_found` rows for schools where
nothing turned up).

Also produce a short `track_b_notes.md` summarizing:
- How searchable SLCL's collection actually was (direct online catalog?
  requires contacting a librarian? no usable online presence at all?).
- Whether the ~92-volume figure seems plausible/consistent with what you
  found, if you can tell.
- Any process friction or recommendations for how this survey should be
  structured when scaled to other institutions (SLU, UMSL, WashU, Mizzou,
  etc.) in a later track.

## Out of scope

- Do not attempt data cleanup on the school records themselves (dates,
  successors) — that's Track A.
- Do not survey any institution other than St. Louis County Library.
- Do not modify `schema.md` or `pilot_seed_63147.json`.
