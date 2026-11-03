"""Converter safety and structural equivalence tests."""
import hashlib
import re
import tempfile
import unittest
from pathlib import Path

from scripts.diagrams import DiagramError, SOURCE, convert, gallery


class DiagramConversionTest(unittest.TestCase):
    def test_existing_diagrams_convert_without_dropping_arrows(self):
        sources = sorted(SOURCE.glob("*.puml"))
        self.assertGreaterEqual(len(sources), 6, "Six baseline PlantUML diagrams expected")
        for source in sources:
            with self.subTest(source=source.name):
                raw = source.read_text(encoding="utf-8")
                rendered = convert(source)
                arrows = len(re.findall(r"(?m)^\s*\w+\s+(?:-->|->|\.\.)\s+\w+(?:\s|$)", raw))
                if "sequenceDiagram" in rendered:
                    converted = len(re.findall(r"(?m)^\s*\w+(?:->>|-->>)\w+:", rendered))
                else:
                    converted = len(re.findall(r"(?m)^\s*\w+\s+(?:-->|-\.-)\s*(?:\|[^|]*\|\s*)?\w+", rendered))
                self.assertEqual(arrows, converted)
                self.assertIn(f"from {source.name}", rendered)

    def test_diagrams_have_accessible_light_svg_palette(self):
        for source in sorted(SOURCE.glob("*.puml")):
            with self.subTest(source=source.name):
                text = source.read_text(encoding="utf-8")
                self.assertIn("skinparam backgroundColor #FFFFFF", text)
                self.assertIn("skinparam defaultFontColor #111111", text)

    def test_generated_svg_has_solid_white_canvas(self):
        for source in sorted(SOURCE.glob("*.puml")):
            with self.subTest(source=source.name):
                svg_file = SOURCE / "rendered" / f"{source.stem}.svg"
                self.assertTrue(svg_file.is_file(), f"Missing {svg_file}")
                svg = svg_file.read_text(encoding="utf-8")
                self.assertRegex(
                    svg,
                    r'<svg\b[^>]*><rect x="0" y="0" width="100%" height="100%" fill="#FFFFFF"/>',
                )

    def test_mermaid_light_theme_and_escaped_sequence_semicolons(self):
        for source in sorted(SOURCE.glob("*.puml")):
            with self.subTest(source=source.name):
                output = convert(source)
                self.assertIn('%%{init: {"theme":"base"', output)
                self.assertIn('"background":"#FFFFFF"', output)
                self.assertIn('"themeCSS":"svg { background-color: #FFFFFF', output)
        # Two diagrams previously broke the real Mermaid parser on raw semicolons.
        idempotency = convert(SOURCE / "idempotency-sequence.puml")
        signing = convert(SOURCE / "sii-signing-and-pdf.puml")
        self.assertIn("Authenticate tenant#59; reserve", idempotency)
        self.assertIn("folio#59; store intent", signing)
        self.assertIn("key != PFX", signing)

    def test_mermaid_svg_previews_have_white_canvas_and_current_source_digest(self):
        for source in sorted(SOURCE.glob("*.puml")):
            with self.subTest(source=source.name):
                mmd = SOURCE / "mermaid" / f"{source.stem}.mmd"
                svg_file = SOURCE / "rendered" / "mermaid" / f"{source.stem}.svg"
                self.assertTrue(svg_file.is_file(), f"Missing {svg_file}")
                digest = hashlib.sha256(mmd.read_bytes()).hexdigest()
                svg = svg_file.read_text(encoding="utf-8")
                self.assertIn(
                    '<rect x="0" y="0" width="100%" height="100%" fill="#FFFFFF"/>',
                    svg,
                )
                self.assertIn(f"<!-- fiscalwave-mermaid-sha256:{digest} -->", svg)

    def test_unknown_syntax_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "unknown.puml"
            source.write_text("@startuml\n!include external.puml\n@enduml\n", encoding="utf-8")
            with self.assertRaisesRegex(DiagramError, "unsupported PlantUML"):
                convert(source)

    def test_sequence_branches_and_notes_preserved(self):
        output = convert(SOURCE / "dte-lifecycle.puml")
        for token in ["alt accepted", "else rejected", "else timeout", "Note right of Connector", "end"]:
            self.assertIn(token, output)

    def test_gallery_discloses_proposed_design(self):
        result = gallery({"system-map": convert(SOURCE / "system-map.puml")})
        self.assertIn("no servicios implementados", result)
        self.assertIn("```mermaid", result)
        self.assertIn("rendered/system-map.svg", result)


if __name__ == "__main__":
    unittest.main()
