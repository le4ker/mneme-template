Check git status to see what changed. Stage all modified and untracked vault
files (never stage .claude/settings.local.json or memory files). Write a concise
commit message that summarises what actually changed, then commit.

## Commit message rules

Commit messages are stored in plaintext and are visible to anyone with repo
access. Never include personal details in them — no names, dates, locations,
health information, financial figures, or any other sensitive content.

Describe the _structure_ of the change, not its content:

| Changed             | Write                | Never write                          |
| ------------------- | -------------------- | ------------------------------------ |
| Log entry added     | `Add log entry`      | `Add log: went to gym with Sarah`    |
| Note updated        | `Update note`        | `Update note: discussed anxiety`     |
| New note in an area | `Add note`           | `Add note on $500 medical expense`   |
| New recipe          | `Add recipe`         | `Add shakshuka recipe`               |
| Multiple areas      | `Update vault notes` | `Update notes on anxiety and budget` |

The pre-commit hook formats and lints automatically — if it fails, fix every
error before retrying and then push to origin.

If there is nothing to commit, just push (there may be unpushed commits from
previous sessions). Report how many commits were pushed and confirm the remote
is up to date.
