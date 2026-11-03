"""Deterministic PlantUML + SVG documentation checks."""
import re
import unittest

from scripts.diagrams import GALLERY, SOURCE, gallery


class DiagramDocumentationTest(unittest.TestCase):
    def test_gallery_lists_each_plantuml_source_and_svg_once(self):
        stems = sorted(p.stem for p in SOURCE.glob("*.puml"))
        self.assertGreaterEqual(len(stems), 6)
        text = gallery(stems)
        for stem in stems:
            with self.subTest(stem=stem):
                self.assertEqual(text.count(f"]({stem}.puml)"), 1)
                self.assertEqual(text.count(f"![") >= len(stems), True)
                self.assertIn(f"(rendered/{stem}.svg)", text)
        self.assertEqual(GALLERY.read_text(encoding="utf-8"), text)
        self.assertNotIn("mermaid", text.lower())

    def test_svg_has_real_opaque_white_canvas(self):
        for source in SOURCE.glob("*.puml"):
            with self.subTest(source=source.name):
                svg_file = SOURCE / "rendered" / f"{source.stem}.svg"
                self.assertTrue(svg_file.is_file(), f"Missing {svg_file}")
                svg = svg_file.read_text(encoding="utf-8")
                self.assertRegex(
                    svg,
                    r'<svg\b[^>]*><rect x="0" y="0" width="100%" height="100%" fill="#FFFFFF"/>',
                )

    def test_sources_declare_white_background_and_dark_text(self):
        for source in SOURCE.glob("*.puml"):
            with self.subTest(source=source.name):
                text = source.read_text(encoding="utf-8")
                self.assertIn("skinparam backgroundColor #FFFFFF", text)
                self.assertIn("skinparam defaultFontColor #111111", text)
                self.assertEqual(text.count("@startuml"), 1)
                self.assertEqual(text.count("@enduml"), 1)

    def test_no_mermaid_conversion_assets(self):
        self.assertFalse(list((SOURCE / "mermaid").glob("*.mmd")))


if __name__ == "__main__":
    unittest.main()
