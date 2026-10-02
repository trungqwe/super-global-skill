import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", PACKAGE / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class PackageTests(unittest.TestCase):
    def test_real_package_verifies(self):
        manifest = installer.verify_package(PACKAGE)
        self.assertEqual(manifest["name"], "super-global-skill")
        self.assertGreaterEqual(manifest["catalog_entries"], 400)


class FixtureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="sgs-")
        self.root = Path(self.tmp.name)
        self.home = self.root / "home"
        self.home.mkdir()
        self.pkg = self.root / "pkg"
        self.pkg.mkdir()
        skill = self.pkg / "super-global-skill"
        (skill / "references/platforms/antigravity/skills/demo").mkdir(parents=True)
        (skill / "references/platforms/antigravity/plugins/demo-plugin").mkdir(parents=True)
        (skill / "references/platforms/antigravity/rules").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            "---\nname: super-global-skill\ndescription: fixture\n---\nbody",
            encoding="utf-8",
        )
        (skill / "references/platforms/antigravity/skills/demo/SKILL.md").write_text(
            "---\nname: demo\ndescription: fixture demo\n---\ndemo", encoding="utf-8"
        )
        (skill / "references/platforms/antigravity/plugins/demo-plugin/plugin.json").write_text("{}")
        (skill / "references/platforms/antigravity/rules/AGENTS.md").write_text("rules")
        (skill / "references/platforms/antigravity/rules/SOUL.md").write_text("soul")
        files = installer.tree_hashes(self.pkg)
        (self.pkg / "package-manifest.json").write_text(
            json.dumps({"schema_version": 1, "name": "super-global-skill", "version": "test", "files": files})
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_dry_run_does_not_mutate(self):
        result = installer.install("generic", self.home, dry=True, package=self.pkg)
        self.assertEqual(result["status"], "planned")
        self.assertFalse((self.home / ".agents").exists())

    def test_install_and_rollback(self):
        result = installer.install("antigravity", self.home, package=self.pkg, install_rules=True)
        target = Path(result["target"])
        self.assertTrue((target / "SKILL.md").is_file())
        self.assertTrue((self.home / ".gemini/config/plugins/demo-plugin/plugin.json").is_file())
        self.assertEqual((self.home / ".gemini/AGENTS.md").read_text(), "rules")
        self.assertEqual(installer.rollback(Path(result["receipt"]))["status"], "rolled_back")
        self.assertFalse(target.exists())

    def test_unmanaged_destination_is_preserved(self):
        target = installer.roots(self.home, "generic")[0] / installer.NAME
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("owned")
        with self.assertRaises(ValueError):
            installer.install("generic", self.home, package=self.pkg)
        self.assertEqual((target / "SKILL.md").read_text(), "owned")
