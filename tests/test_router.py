import importlib.util
import json
import unittest
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("route", PACKAGE / "super-global-skill/scripts/route.py")
route = importlib.util.module_from_spec(spec)
spec.loader.exec_module(route)


class RouterTests(unittest.TestCase):
    def test_vietnamese_debug_route(self):
        self.assertEqual(route.search("soi lỗi PR và tìm nguyên nhân API chập chờn")[0]["skill"], "rune-debug")

    def test_ui_alias_route(self):
        self.assertEqual(route.search("làm lại UI cho đẹp và rõ hơn")[0]["skill"], "ui-ux-pro-max")

    def test_reuseforge_route(self):
        self.assertIn(route.search("tìm repository và đánh giá khả năng tái sử dụng")[0]["skill"], {"reuseforge-asset-scout", "reuseforge-orchestrator"})

    def test_bounded_empty_and_catalog(self):
        self.assertEqual(route.search("zzznomatchingword"), [])
        self.assertLessEqual(len(route.search("API testing code", 99)), 5)
        entries = json.loads((PACKAGE / "super-global-skill/references/skill-index.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(entries), 400)
