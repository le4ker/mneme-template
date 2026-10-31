import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINK_CHECKER = REPO_ROOT / ".githooks" / "check-links"


class CheckLinksTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.vault = Path(self.temp_dir.name)
        subprocess.run(["git", "init", "-q"], cwd=self.vault, check=True)
        for folder in ("Areas", "Resources", "Inbox"):
            (self.vault / folder).mkdir()

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_note(self, relative_path, content):
        path = self.vault / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def run_checker(self, *args):
        return subprocess.run(
            ["sh", str(LINK_CHECKER), *args],
            cwd=self.vault,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_allows_name_path_heading_alias_and_relative_links(self):
        self.write_note("Areas/Books/Reading.md", "# Reading\n")
        self.write_note(
            "Inbox/Capture.md",
            "[[Reading]] [[Areas/Books/Reading#Notes|book]] "
            "[[../Areas/Books/Reading]]\n",
        )

        result = self.run_checker("--all")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_reports_broken_links_with_source_path(self):
        self.write_note("Inbox/Capture.md", "# Capture\n\nSee [[Missing Note]].\n")

        result = self.run_checker("--all")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Inbox/Capture.md: [[Missing Note]]", result.stdout)

    def test_ignores_broken_links_outside_vault_note_folders(self):
        self.write_note("Areas/Books/Reading.md", "# Reading\n")
        self.write_note("README.md", "A non-vault link: [[Missing Note]].\n")
        self.write_note("Inbox/Capture.md", "See [[Reading]].\n")

        result = self.run_checker("--all")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_staged_mode_checks_index_content(self):
        self.write_note("Areas/Books/Reading.md", "# Reading\n")
        source = self.write_note("Inbox/Capture.md", "See [[Reading]].\n")
        subprocess.run(["git", "add", "Inbox/Capture.md"], cwd=self.vault, check=True)
        source.write_text("See [[Missing Note]].\n", encoding="utf-8")

        result = self.run_checker()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
