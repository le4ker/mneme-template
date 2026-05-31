Run a periodic review of the vault and surface anything worth acting on.

## Steps

1. **Inbox check** — list any files remaining in `Inbox/`. Flag if non-empty.

2. **Broken internal links** — scan all `.md` files for `[[...]]` links. For
   each link, check whether a corresponding file exists anywhere in the vault
   (match on filename without extension, case-insensitive). Report all broken
   links grouped by source file.

3. **Orphaned notes** — find notes in `Areas/` and `Resources/` that are not
   linked from any other note. These may be worth connecting or archiving.

4. **Stale notes** — using `git log`, find notes that have not been modified in
   over 6 months. List them as candidates for review or archival.

5. **Empty or stub notes** — find notes with fewer than 5 lines of content
   (excluding the H1 title). Flag them as potentially incomplete.

6. **Resources audit** — list everything currently in `Resources/` and evaluate
   each item against the promotion criteria from CLAUDE.md:
   - Promote into an existing Area if it is an addendum to a note there.
   - Propose a new Area if three or more related resources on the same topic
     exist, or a single resource has grown into something actively maintained.
   - Flag for deletion if no longer relevant.
   - Leave in place if it is passive reference material.

## Output

Present findings as a structured report with one section per check above. For
each finding, state the file path and a one-line description of the issue.

At the end, ask the user which items they want to act on now and which to skip.
Do not make any changes without confirmation.
