import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SRC = Path(__file__).resolve().parents[1] / "check_task_manifest.py"
spec = importlib.util.spec_from_file_location("manifest_check", SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

SHA = "a" * 40


def task():
    return {"issue":"FW-025", "agent":"codex", "branch":"feat/FW-025-pfx",
            "base_sha":SHA, "allowed_paths":["services/credentials/","docs/en/credentials.md"]}


class ContractTests(unittest.TestCase):
    def test_valid_task(self):
        self.assertEqual([], m.validate_task(task(), ["services/credentials/Foo.java", "docs/en/credentials.md"]))

    def test_outside_path_rejected(self):
        self.assertTrue(any("undeclared" in e for e in m.validate_task(task(), ["services/other/Bad.java"])))

    def test_traversal_rejected(self):
        self.assertTrue(any("unsafe" in e for e in m.validate_task(task(), ["../secret.txt"])))

    def test_wrong_base_or_issue_rejected(self):
        t = task(); t["base_sha"] = "0"*40
        self.assertTrue(any("base_sha" in e for e in m.validate_task(t, [])))
        t = task(); t["branch"] = "feat/FW-027-other"
        self.assertTrue(any("not linked" in e for e in m.validate_task(t, [])))

    def test_duplicate_slashes_rejected(self):
        self.assertTrue(any("unsafe" in e for e in m.validate_task(task(), ["services//wrong/Path.java"])))
        bad = task()
        bad["allowed_paths"] = ["services//wrong/"]
        self.assertTrue(any("unsafe" in e for e in m.validate_task(bad, [])))

    def test_app_change_without_task_fails(self):
        self.assertTrue(m.check_paths(["apps/shell/src/App.tsx"], Path(".")))

    def test_docs_only_no_task_required(self):
        self.assertEqual([], m.check_paths(["README.md", "docs/es/roadmap.md"], Path(".")))

    def test_task_file_and_ownership(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            f = root/"coordination/tasks/FW-025.json"
            f.parent.mkdir(parents=True)
            f.write_text(json.dumps(task()), encoding="utf-8")
            self.assertEqual([], m.check_paths(["coordination/tasks/FW-025.json", "services/credentials/Foo.java"],root))
            self.assertTrue(m.check_paths(["coordination/tasks/FW-025.json","services/payments/Foo.java"],root))


if __name__ == "__main__":
    unittest.main()
