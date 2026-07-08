# BiS

[![CI](https://github.com/rkdghgus0779-crypto/BiS/actions/workflows/ci.yml/badge.svg)](https://github.com/rkdghgus0779-crypto/BiS/actions/workflows/ci.yml)

BiS is an early-stage open-source toolkit and learning archive for students interested in bio and brain engineering, bioinformatics, neuroscience, computational biology, and AI-assisted scientific learning.

The project aims to provide simple, readable, and beginner-friendly materials that help connect biological knowledge with programming, data analysis, and computational thinking. Its long-term direction is biomedical AI education: helping learners move from biological questions to reproducible Python workflows.

## Overview

Many students in biology-related fields find it difficult to move from scientific concepts to practical coding and data analysis. BiS was created to reduce this gap by organizing study notes, example code, and small learning tools in one public repository.

This repository is currently in its early stage, but it is being shaped as a practical educational toolkit: small Python utilities, reproducible examples, and clear documentation for students who are learning how biology and computation connect.

BiS is especially interested in topics where cell biology meets clinical problems, such as single-cell RNA-seq, fibrosis, immune response, organoids, and medical data science.

## Features

* Organizes bio and brain engineering study notes
* Provides beginner-friendly Python examples
* Supports simple text-based note summarization
* Extracts basic keywords from scientific notes
* Documents biology, neuroscience, and computational biology concepts
* Explores AI-assisted workflows for scientific learning
* Builds toward reproducible examples for biomedical AI learning

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/rkdghgus0779-crypto/BiS.git
cd BiS
python -m pip install -e .
```

No external runtime dependencies are required for the current version.

## Usage

Run the example script:

```bash
python src/note_summarizer.py
```

Use the command line interface with a Markdown or text note:

```bash
bis-notes examples/example_notes.md
```

Export structured JSON:

```bash
bis-notes examples/example_notes.md --json
```

Use the package from Python:

```python
from bis_notes import extract_keywords, summarize_note

note = "Computational biology connects biology, data, and machine learning."

print(summarize_note(note))
print(extract_keywords(note))
```

## Project Structure

The repository is organized as follows:

```text
BiS/
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   `-- workflows/
|-- src/
|   |-- bis_notes/
|   `-- note_summarizer.py
|-- tests/
|-- examples/
|-- docs/
|-- pyproject.toml
|-- README.md
|-- LICENSE
`-- requirements.txt
```

## Testing

Run the test suite:

```bash
python -m unittest discover -s tests
```

## Example Use Case

A student can write a short study note about biology, neuroscience, or bioinformatics, then use BiS to generate a simple summary and extract related keywords.

This is a small first step toward building reproducible, code-based tools for scientific learning.

## Who This Helps

BiS is designed for:

* Biology and bioengineering students starting to learn Python
* Neuroscience students organizing concept notes and data-analysis examples
* Beginners who want readable examples before moving into larger scientific Python tools
* Contributors who want a friendly place to practice open-source documentation, testing, and educational examples

## Project Tracks

BiS is organized around a few learning tracks:

* **Scientific Python basics:** small utilities, tests, CLI examples, and readable code
* **Biomedical concept notes:** beginner-friendly notes on biology, neuroscience, and bioinformatics
* **Single-cell and fibrosis direction:** future tutorials connecting cell-level data to clinical questions
* **Open-source practice:** issues, documentation, and review habits for first-time contributors

See [docs/research_focus.md](docs/research_focus.md), [docs/project_ideas.md](docs/project_ideas.md), and [docs/open_source_growth.md](docs/open_source_growth.md) for the current direction.

## Areas of Interest

* Bio and Brain Engineering
* Bioinformatics
* Computational Biology
* Neuroscience
* Biological Data Analysis
* Machine Learning in Biology
* AI-assisted Scientific Learning
* Single-cell RNA-seq
* Fibrosis and immune response
* Biomedical AI

## Roadmap

* Add more example notes related to biology, neuroscience, and bioinformatics
* Add beginner-friendly examples for biological data analysis
* Add a small single-cell RNA-seq reading and tutorial track
* Add a fibrosis and immune response learning track
* Publish a small documentation site with tutorials
* Add notebooks using public scientific datasets
* Improve the CLI for note organization and keyword extraction
* Invite first-time contributors through labeled beginner issues

## Current Status

This project is under active development. Version 0.1 focuses on documentation, a small Python package, a CLI, basic tests, and learning materials.

See [docs/impact.md](docs/impact.md) for the project's current reach and impact goals.

## Contributing

Contributions are welcome, especially documentation fixes, beginner-friendly examples, tests, and small utilities for scientific learning.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License

This project is licensed under the MIT License.
