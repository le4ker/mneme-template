---
name: review
description:
  Audit the vault for inbox items, broken links, orphans, stale notes, and
  resource lifecycle candidates.
---

<!-- markdownlint-disable MD041 -->

Review the vault without changing files. Read `AGENTS.md` for the current Areas
and Resources lifecycle rules.

Check:

1. Whether `Inbox/` contains files.
2. Broken Obsidian `[[...]]` links across Markdown files.
3. Notes in `Areas/` and `Resources/` that are not linked from another note.
4. Notes unmodified for more than six months, based on `git log`.
5. Notes with fewer than five lines of content after the H1 title.
6. Every item in `Resources/`, applying the promotion, merge, retention, and
   deletion criteria in `AGENTS.md`.

Present one section per check. For each finding, give the path and a short
description. Finish by asking which findings the user wants to act on; make no
changes during the review.
