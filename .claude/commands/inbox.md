Capture a fleeting note to `Inbox/`.

Ask the user:

1. A short title for the note?
2. Any content or context? (optional)

Then:

- Create `Inbox/YYYY-MM-DD-<kebab-case-title>.md` with today's date.
- Structure:

  ```markdown
  # Title

  <content if provided>
  ```

- Run `make format` to ensure clean formatting.
- Report the file path created.
