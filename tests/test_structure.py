import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROOT_FILES = ["README.md", "CHANGELOG.md", "CITATION.cff", "CONTRIBUTING.md",
              "GOVERNANCE.md", "LICENSE", "SECURITY.md"]
DOCS = ["operating-model.md", "evidence-model.md", "assessment-method.md",
        "maturity-model.md", "limitations.md", "repository-architecture.md",
        "implementation-guide.md", "future-roadmap.md", "glossary.md",
        "portfolio-positioning.md"]
TEMPLATES = ["control-record-template.md", "decision-record-template.md",
             "dependency-review-template.md", "evidence-record-template.md",
             "finding-and-recommendation-template.md",
             "operationalization-plan-template.md",
             "regulatory-change-template.md", "review-record-template.md",
             "stakeholder-review-template.md"]
PLACEHOLDERS = ["TODO", "TBD", "FIXME"]
# Declared in the README/CHANGELOG as v0.2.0+ instantiation scope.
# These must NOT exist until that release is built.
PLANNED_DIRS = ["govern", "shared-registers", "evidence", "examples"]


def read(p):
    return p.read_text(encoding="utf-8")


class TestFilesExist(unittest.TestCase):
    def test_root_files(self):
        for name in ROOT_FILES:
            self.assertTrue((ROOT / name).is_file(), f"missing {name}")

    def test_docs(self):
        for name in DOCS:
            self.assertTrue((ROOT / "docs" / name).is_file(),
                            f"missing docs/{name}")

    def test_templates(self):
        for name in TEMPLATES:
            self.assertTrue((ROOT / "templates" / name).is_file(),
                            f"missing templates/{name}")


class TestVersionConsistency(unittest.TestCase):
    """One version, three files. CITATION.cff is canonical; README and
    CHANGELOG must agree. If this fails, the version story drifted."""

    def test_single_version_across_files(self):
        citation = read(ROOT / "CITATION.cff")
        m = re.search(r"^version:\s*([0-9]+\.[0-9]+\.[0-9]+)",
                      citation, re.MULTILINE)
        self.assertIsNotNone(m, "CITATION.cff has no version field")
        ver = m.group(1)
        self.assertIn(f"v{ver}", read(ROOT / "README.md"),
                      f"README missing v{ver}")
        self.assertIn(f"[{ver}]", read(ROOT / "CHANGELOG.md"),
                      f"CHANGELOG missing [{ver}] release section")


class TestClaimsAreCalibrated(unittest.TestCase):
    """Enforces the v0.1.0 calibration: this repo is documentation+templates.
    If these fail, a headline drifted back into overclaiming: fix the TEXT."""

    def test_readme_does_not_claim_gvoc_complete(self):
        self.assertNotIn("GV.OC complete", read(ROOT / "README.md"),
                         "README claims GV.OC complete again")

    def test_readme_does_not_claim_gvoc_org_context_complete(self):
        self.assertNotIn("GV.OC Organizational Context complete",
                         read(ROOT / "README.md"),
                         "README roadmap claims GV.OC complete (current)")

    def test_readme_states_release_scope(self):
        self.assertIn("framework documentation and template set",
                      read(ROOT / "README.md"))

    def test_readme_is_not_a_reference_implementation(self):
        self.assertNotIn("reference implementation", read(ROOT / "README.md"),
                         "README calls itself a reference implementation again")

    def test_changelog_plans_gvoc_for_later_release(self):
        self.assertIn("GV.OC", read(ROOT / "CHANGELOG.md"))

    def test_citation_abstract_not_a_reference_implementation(self):
        self.assertNotIn("reference implementation", read(ROOT / "CITATION.cff"),
                         "CITATION abstract overclaims again")


class TestStructureMatchesStatedScope(unittest.TestCase):
    """The README/CHANGELOG declare govern/, shared-registers/, evidence/,
    examples/ as v0.2.0+ additions. They may exist locally as empty
    scaffolding, but nothing under them may be tracked/published until
    that release ships."""

    def test_planned_dirs_have_no_tracked_content(self):
        import subprocess
        tracked = subprocess.run(
            ["git", "ls-files"], capture_output=True, text=True, cwd=ROOT
        ).stdout.split()
        for name in PLANNED_DIRS:
            hits = [p for p in tracked if p == name or p.startswith(name + "/")]
            self.assertFalse(hits,
                             f"{name}/ has tracked content but is planned for "
                             f"v0.2.0+ (release deliberately: update README, "
                             f"CHANGELOG, and this test)")


class TestLicense(unittest.TestCase):
    def test_apache_license(self):
        self.assertIn("Apache License", read(ROOT / "LICENSE"))


class TestNoPlaceholders(unittest.TestCase):
    def test_docs_and_templates_have_no_todos(self):
        for folder in ("docs", "templates"):
            for p in (ROOT / folder).glob("*.md"):
                text = read(p)
                for marker in PLACEHOLDERS:
                    self.assertNotIn(marker, text,
                                     f"{p.name}: unfinished marker '{marker}'")


class TestLinks(unittest.TestCase):
    LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

    def test_internal_links_resolve(self):
        for p in ROOT.rglob("*.md"):
            if ".git" in p.parts:
                continue
            for raw in self.LINK_RE.findall(read(p)):
                if "://" in raw or raw.startswith(("#", "mailto:")):
                    continue
                target = raw.split("#")[0].strip()
                if target:
                    self.assertTrue((p.parent / target).resolve().exists(),
                                    f"{p.name}: broken link -> {raw}")
