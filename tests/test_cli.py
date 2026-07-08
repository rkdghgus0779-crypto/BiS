import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from bis_notes.cli import main


class CliTests(unittest.TestCase):
    def test_json_output_contains_summary_and_keywords(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            note_path = Path(temp_dir) / "note.md"
            note_path.write_text(
                "Biology uses data. Single-cell RNA-seq can study fibrosis.",
                encoding="utf-8",
            )

            output = StringIO()
            with redirect_stdout(output):
                exit_code = main([str(note_path), "--json"])

        payload = json.loads(output.getvalue())

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            payload["summary"],
            "Biology uses data. Single-cell RNA-seq can study fibrosis.",
        )
        self.assertEqual(
            payload["keywords"],
            ["biology", "data", "single-cell", "single-cell rna-seq", "fibrosis"],
        )


if __name__ == "__main__":
    unittest.main()
