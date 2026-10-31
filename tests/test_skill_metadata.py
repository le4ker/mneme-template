import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / ".agents" / "skills"


class SkillMetadataTests(unittest.TestCase):
    def test_each_skill_has_matching_name_and_description(self):
        skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        self.assertTrue(skill_files, "No repo-local skills found")

        for skill_file in skill_files:
            with self.subTest(skill=skill_file.parent.name):
                content = skill_file.read_text(encoding="utf-8")
                frontmatter = content.split("---", 2)
                self.assertEqual(frontmatter[0].strip(), "")
                self.assertEqual(len(frontmatter), 3)

                metadata = frontmatter[1]
                name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", metadata)
                description = re.search(r"(?m)^description:\s*\S", metadata)

                self.assertIsNotNone(name, "Missing skill name")
                self.assertIsNotNone(description, "Missing skill description")
                self.assertEqual(name.group(1), skill_file.parent.name)


if __name__ == "__main__":
    unittest.main()
