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

        self.assertEqual(summarize_note(note, max_sentences=2), "Topic. Biology uses data.")

    def test_summarize_note_handles_markdown_lists_and_code_blocks(self):
        note = """
# Fibrosis note

## Immune response

- Macrophages signal to fibroblasts.
* TGF-beta can support extracellular matrix remodeling.
1. Single-cell RNA-seq can separate cell populations.
- [x] Quality control matters before interpretation.

```python
print("This code should not appear in the summary.")
```
"""

        self.assertEqual(
            summarize_note(note, max_sentences=4),
            (
                "Immune response. Macrophages signal to fibroblasts. "
                "TGF-beta can support extracellular matrix remodeling. "
                "Single-cell RNA-seq can separate cell populations."
            ),
        )

    def test_summarize_note_cleans_blockquotes_links_and_inline_code(self):
        note = (
            "> Read the [PBMC tutorial](https://example.com). "
            "`AnnData` stores matrices and metadata."
        )

        self.assertEqual(
            summarize_note(note, max_sentences=2),
            "Read the PBMC tutorial. AnnData stores matrices and metadata.",
        )

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
