---
name: setup
description:
  Configure a fresh Mneme vault by creating the user's Areas and journal skills.
---

<!-- markdownlint-disable MD041 -->

Run once in a fresh vault. Do not run again after the Areas have been
configured.

## Gather details

Ask one question at a time and wait for the answer:

1. Which long-term Areas should the vault track? Offer Books, Finance, Fitness,
   Travel, Recipes, Work, Wellness, Music, and Learning as examples. For each,
   record its name, an emoji, and a one-line description. Draft the emoji and
   description for the user to approve. Ask whether they want to add more Areas
   until they are done.
2. Which Areas need recurring logs? For each, record the log filename and the
   fields to track. Date is included automatically.
3. What should the vault be called? Use “My Vault” if they skip this answer.

## Generate the vault

After gathering the details, make these changes without additional prompts:

1. Create `Areas/{emoji} {name}/.gitkeep` for each Area.
2. Replace the setup comment under `## Content Areas` in `AGENTS.md` with a
   Markdown table listing each Area path and description.
3. For each journalled Area, create `.agents/skills/log-{kebab-name}/SKILL.md`.
   Include `name` and a concise `description` in YAML front matter. In the skill
   instructions, ask for each field except Date (use today's date), open
   `Areas/{emoji} {name}/{Log File Name}.md`, create it with an H1 and an empty
   table if needed, insert each new row directly below the table header, run
   `make format`, and report the logged entry.
4. Delete this setup skill after creating the other files.
5. Run `make format`.

Report the vault name, Areas created, generated log skills, and next steps: open
the vault in Obsidian, invoke `$inbox` to capture a first note, and invoke
`$sync-vault` to commit and push.
