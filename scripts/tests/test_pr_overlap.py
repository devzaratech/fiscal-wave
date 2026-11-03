import importlib.util
from pathlib import Path
import unittest

source = Path(__file__).resolve().parents[1] / "check_pr_overlap.py"
spec = importlib.util.spec_from_file_location("overlap", source)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class OverlapTests(unittest.TestCase):
    def test_identical_file_detected(self):
        other = [(3,[{"filename":"services/api/Invoice.java"}])]
        self.assertEqual([(3,["services/api/Invoice.java"])],
                         m.collisions({"services/api/Invoice.java"}, other))

    def test_disjoint_files_do_not_conflict(self):
        self.assertEqual([], m.collisions({"apps/ui/App.tsx"},
                        [(3,[{"filename":"services/api/Foo.java"}])]))

    def test_rename_old_and_new_are_checked(self):
        files = [{"status":"renamed","previous_filename":"contracts/a.yaml","filename":"contracts/b.yaml"}]
        self.assertEqual({"contracts/a.yaml","contracts/b.yaml"},m.changed_paths(files))


if __name__ == "__main__":
    unittest.main()
