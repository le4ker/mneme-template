Bootstrap this vault for a new user. This skill runs **once** and deletes itself
when complete. Do not run it on a vault that has already been configured.

## Step 1 — Gather information

Ask the following questions **one at a time**, waiting for answers before moving
on. Be conversational — suggest options to help the user think, but accept
whatever they choose.

### 1a. Areas

Ask: "What long-term areas of your life do you want to track in this vault?"

Suggest these common starting points:

- 📖 Books — reading log and book notes
- 💰 Finance — accounts, budget, transactions
- 🏋️ Fitness — workouts, training log
- ✈️ Travel — trips, places, itineraries
- 🍳 Recipes — cooking recipes
- 💼 Work — projects, notes, goals
- 🌿 Wellness — health protocols, session logs
- 🎵 Music — practice log, gear, listening notes
- 🧠 Learning — courses, concepts, insights

For each area the user confirms, record:

- **Name** (e.g. "Books", "Fitness")
- **Emoji** — suggest one based on the name, let them override
- **One-line description** of what goes there (you can draft one and let them
  approve)

Keep asking "Any more areas?" until the user says they're done.

### 1b. Journalled areas

Ask: "Which of your areas have recurring log entries — things you log regularly,
like workouts, dives, or sessions?"

For each journalled area, ask:

- **Log file name** (e.g. "Workout Log", "Session Log", "Reading Log")
- **Fields** — what does each entry track? List column names
  (e.g. "Date, Exercise, Duration, Notes"). Date is always included automatically.

### 1c. Vault name

Ask: "What do you want to call your vault?" (e.g. "My Mind Palace", "Atlas",
"Second Brain"). Default: "My Vault" if they skip.

## Step 2 — Generate files

Perform the following without further prompting once you have all the information.

### 2a. Folder structure

For each area, create `Areas/{emoji} {name}/.gitkeep`.

### 2b. Update CLAUDE.md

Replace the `<!-- Populated by /setup ... -->` comment in the `## Content Areas`
section with a populated markdown table:

```markdown
| Area                    | Contents      |
| ----------------------- | ------------- |
| `Areas/{emoji} {name}/` | {description} |
```

One row per area, preserving the column alignment style.

### 2c. Log skills

For each journalled area, create `.claude/commands/log-{kebab-name}.md`.

The skill file should instruct Claude to:

1. Ask the user for each field (except Date, which is always today's date).
2. Open `Areas/{emoji} {name}/{Log File Name}.md`.
3. If the file does not exist, create it with an H1 title and an empty table
   with the correct header and separator rows.
4. Insert a new row at the **top** of the table (below the header and separator)
   — reverse chronological order.
5. Run `make format`.
6. Report what was logged without asking for confirmation.

Write the skill as a natural-language prompt (the same style as other skills in
`.claude/commands/`), not as a script or pseudocode.

### 2d. Clean up

Delete `.claude/commands/setup.md` (this file) once all other files are written.

### 2e. Format

Run `make format` to normalise all generated markdown.

## Step 3 — Report

Tell the user:

- The vault name and list of areas created
- Which areas have log skills, and the skill name for each (e.g. `/log-fitness`)
- Next steps: open the vault in Obsidian, try `/inbox` to capture a first note,
  `/sync-vault` to commit
