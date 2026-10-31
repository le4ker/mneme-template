---
name: sync-vault
description: Commit vault changes and push them to the configured Git remote.
---

<!-- markdownlint-disable MD041 -->

Check Git status. Stage all vault changes, including added, modified, renamed,
and deleted files. Exclude local settings and memory files. Write a concise
commit message that describes the structure of the change, not sensitive note
contents.

Examples:

| Change              | Commit message       |
| ------------------- | -------------------- |
| Log entry added     | `Add log entry`      |
| Note updated        | `Update note`        |
| New note in an Area | `Add note`           |
| Multiple Areas      | `Update vault notes` |

The pre-commit hook formats and lints staged Markdown. If it fails, fix all
reported issues and retry. Then push to the configured remote. If there is
nothing to commit, push any existing commits. Report the commit created, number
of commits pushed, and whether the remote is up to date.
