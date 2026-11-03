"""Converter safety and structural equivalence tests."""
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
