---
name: process-inbox
description: Route notes from Inbox into Areas or Resources and clear the inbox.
---

<!-- markdownlint-disable MD041 -->

Process every note in `Inbox/`. Read `AGENTS.md` to understand the configured
Areas and their contents.

For each note, choose whether to move it as a standalone note into the best
matching Area, merge it into an existing note as an addendum, or park it in
`Resources/` when it is reference material or has no clear Area. Add relevant
Obsidian links, apply the chosen change, and remove the processed Inbox file.
Run `make format` after processing. Report what was moved, merged, or parked and
confirm whether `Inbox/` is empty.
