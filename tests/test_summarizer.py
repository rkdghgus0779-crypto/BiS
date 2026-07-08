import unittest

from bis_notes import extract_keywords, summarize_note


class SummarizerTests(unittest.TestCase):
    def test_summarize_note_keeps_requested_sentence_count(self):
        note = "Biology uses data. Neuroscience studies the brain. Python helps analysis."

        self.assertEqual(
            summarize_note(note, max_sentences=2),
            "Biology uses data. Neuroscience studies the brain.",
        )

    def test_summarize_note_returns_empty_string_for_empty_note(self):
        self.assertEqual(summarize_note("   "), "")

    def test_summarize_note_ignores_markdown_headings(self):
        note = "# Example Note\n\n## Topic\n\nBiology uses data. Python helps analysis."

        self.assertEqual(summarize_note(note, max_sentences=1), "Biology uses data.")

    def test_summarize_note_rejects_invalid_sentence_count(self):
        with self.assertRaises(ValueError):
            summarize_note("Biology uses data.", max_sentences=0)

    def test_extract_keywords_preserves_default_order(self):
        note = "Computational biology connects biology, data, and machine learning."

        self.assertEqual(
            extract_keywords(note),
            ["biology", "data", "machine learning", "computational biology"],
        )

    def test_extract_keywords_finds_biomedical_focus_terms(self):
        note = "Single-cell RNA-seq can study fibrosis, macrophage, and fibroblast states."

        self.assertEqual(
            extract_keywords(note),
            ["single-cell", "single-cell rna-seq", "fibrosis", "macrophage", "fibroblast"],
        )


if __name__ == "__main__":
    unittest.main()
