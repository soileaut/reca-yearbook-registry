# Next Steps

See `DATA_PIPELINE.md` for full background and how we got here.

1. **Launch `track_a_coordinator_prompt.md`** as a Devin session to
   research the 325 remaining schools in `data/schools_seed_deduped.json`
   via Agent Fan-Out.
2. **Review the resulting PR** — spot-check citations, confirm no
   fabrication, spot-check the `entity_type`/administrative-district
   calls for rows named like a governing body.
3. **Decide on the 63 flagged review cases** in
   `data/schools_seed_deduped_review_needed.json` — likely easier to
   resolve once the Track A research above provides real context (dates,
   addresses, successor info) than from names alone.
4. **Scale Track B** to additional institutions (SLU, WashU, UMSL,
   Mizzou, etc.), each checking `yearbook_registry_master.json` first to
   skip re-searching for yearbooks already confirmed digitized elsewhere.
