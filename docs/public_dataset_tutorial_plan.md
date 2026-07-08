# Public Dataset Tutorial Plan

This document outlines a future beginner-friendly public dataset tutorial for BiS.

The tutorial should use only public, educational datasets and should avoid clinical claims. The goal is to teach students how to connect a biological question with a small, reproducible analysis workflow.

## Suggested Dataset

### 10x Genomics PBMC 3k

The first tutorial can use the public PBMC 3k single-cell RNA-seq dataset from 10x Genomics.

Why this dataset is a good starting point:

- It is widely used in beginner single-cell tutorials.
- It is small enough for a starter workflow.
- It has clear biological relevance because peripheral blood mononuclear cells include immune cell populations.
- It connects well with BiS topics such as single-cell RNA-seq, immune response, cell type annotation, marker genes, and reproducible scientific learning.

## Learning Goals

Students should learn how to:

- Understand what a public single-cell dataset contains.
- Explain the difference between a gene expression matrix and cell metadata.
- Recognize why quality control matters before interpretation.
- Describe AnnData and `.h5ad` files at a high level.
- Identify basic immune cell populations using marker genes.
- Read simple outputs without making unsupported clinical claims.
- Write a short study note and summarize it with `bis-notes`.

## Tutorial Scope

The first version should stay small and readable.

Included:

- Dataset background
- Setup instructions
- Download or loading instructions
- Basic data object explanation
- Quality-control concept overview
- Cell type and marker-gene reading exercise
- Expected outputs
- Reflection questions

Not included in the first version:

- Clinical prediction
- Disease diagnosis
- Heavy model training
- Large-scale benchmarking
- Claims about patient outcomes

## Suggested Setup

The tutorial can start with a lightweight environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install scanpy pandas matplotlib
```

If the first implementation should avoid heavy dependencies, it can begin as a reading-only tutorial using exported CSV or Markdown notes, then later add a notebook.

## Expected Outputs

The finished tutorial should produce:

- A short explanation of the dataset.
- A small table describing cells, genes, and metadata.
- A quality-control checklist.
- A marker-gene table for beginner immune cell annotation.
- A short Markdown study note that can be passed to `bis-notes`.
- Optional figures such as a UMAP plot or marker-gene expression plot in a later notebook version.

## BiS Integration

Students can write a note like:

```text
PBMC 3k is a public single-cell RNA-seq dataset for learning immune cell analysis.
Marker genes can help annotate cell types such as T cells, B cells, and monocytes.
Quality control and metadata interpretation are important before biological conclusions.
```

Then run:

```bash
bis-notes pbmc3k_note.md --json
```

This connects public dataset reading with the current BiS CLI.

## Next Implementation Steps

1. Add `docs/tutorials/pbmc3k_beginner.md`.
2. Add a tiny example note under `examples/`.
3. Add a public dataset glossary section for PBMC, UMI, marker gene, and QC.
4. Add an optional notebook only if dependencies remain manageable.
5. Keep the tutorial educational and avoid clinical interpretation.
