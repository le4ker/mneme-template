Process all notes in `Inbox/` and integrate them into the appropriate Areas.

First, read `CLAUDE.md` to understand the current Areas and what each one contains.

For each file in `Inbox/`:

1. Read its title and content.
2. Determine the best target area based on the content and the Areas defined in
   CLAUDE.md.
3. Decide whether to:
   - **Move** it as a standalone note into the area (if it's self-contained).
   - **Merge** its content into an existing note in the area (if it's an
     addendum to something already there).
   - **Park** it in `Resources/` if it is reference material or does not fit any
     existing Area — do not ask, just move it there and note it in the summary.
4. Apply the action: create or update the target note, add Obsidian internal
   links where relevant, and run `make format`.
5. Delete the processed file from `Inbox/`.

After processing all files, report a summary: what was moved/merged/parked
where, and confirm `Inbox/` is empty.
