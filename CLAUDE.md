# CLAUDE.md

## Vault Overview

Personal Obsidian knowledge vault tracked with Git. Static markdown files — no
build system or package manager.

## Getting Started

If you just created this vault from the template, run `/setup` in Claude Code.
It will ask you which Areas you want to track and generate your personal vault
structure and skills.

## Structure

- `Areas/` — Long-term areas of focus
- `Resources/` — Reference material that doesn't yet belong to a specific Area
- `Inbox/` — Quick capture

## Resources Lifecycle

Notes land in `Resources/` when `/process-inbox` cannot confidently map them to
an existing Area. They are not permanent residents — treat `Resources/` as a
staging ground, not an archive.

**Promote a resource into an existing Area** when:

- It turns out to be an addendum or extension of a note already in an Area.

**Promote a resource into a new Area** when:

- Three or more related resources on the same topic have accumulated, signalling
  a recurring interest that warrants its own Area.
- A single resource has grown substantially through repeated edits and is now
  actively maintained rather than passively referenced.

**Leave a resource in `Resources/`** when:

- It is passive reference material you consult occasionally but do not maintain.

**Delete a resource** when:

- It is no longer relevant and unlikely to be referenced again.

The `/review` skill audits `Resources/` at each periodic review and surfaces
candidates for promotion, merging, or deletion.

## Formatting

Prettier and markdownlint are configured. The pre-commit hook
(`.githooks/pre-commit`) runs Prettier automatically on staged markdown files —
no need to manually format before committing.

Rules (`.markdownlint.yaml`, `.prettierrc.yaml`):

- Max line length: 100 characters (tables and code blocks exempt)
- Prose wrap: always
- Tab width: 2 spaces

## Note Conventions

- Use **markdown tables** for structured data (gear specs, supplement dosages,
  financial accounts, etc.)
- Use **Obsidian internal links** for cross-references: `[[Folder/Note Name]]`
- **Link liberally** — whenever a note mentions a concept, person, gear item, or
  topic that has its own note, link to it with `[[Note Name]]`
- New notes in `Areas/` should match the existing structure of that area
- Every note starts with a single **H1 title matching the filename**, followed
  by content — no preamble
- Use **H2 and H3 headings only** — never go deeper than H3
- **Dates**: use `YYYY-MM-DD` when the full date is known; year only (`2026`)
  when only the year is known
- **Logs are reverse chronological** — most recent entry first

## Content Areas

<!-- Populated by /setup. Run it once to configure your Areas. -->
