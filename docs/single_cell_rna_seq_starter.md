# Single-cell RNA-seq Starter Reading Guide

This guide is a beginner-friendly path for students who want to understand single-cell RNA-seq before running full analysis workflows.

The goal is not to memorize every tool. The goal is to understand what question each analysis step is trying to answer.

## What Single-cell RNA-seq Measures

Single-cell RNA-seq measures RNA abundance in individual cells. Instead of averaging signals across a whole tissue sample, it lets learners ask which cell types are present and how cell states differ across conditions.

Common biological questions include:

- Which cell populations are present in this tissue?
- Are immune cells activated in disease samples?
- Do fibroblasts show extracellular matrix remodeling signals?
- Are there rare cell states that bulk RNA-seq would hide?
- Which genes distinguish one cell group from another?

## Minimum Concepts to Learn First

### 1. Gene Expression Matrix

Most beginner workflows start from a matrix where rows are genes and columns are cells. The values represent detected RNA molecules or sequencing reads.

Ask:

- What does one row mean?
- What does one column mean?
- Are the values raw counts or normalized values?

### 2. Cell Metadata

Cell metadata stores information about each cell, such as sample ID, condition, batch, tissue, or predicted cell type.

Metadata matters because biological interpretation often depends on comparing groups.

### 3. Quality Control

Quality control removes cells or genes that may be technically unreliable. Common checks include total counts, number of detected genes, and mitochondrial gene percentage.

Biological meaning:

- A low-quality cell may look different because it was damaged, not because it represents a meaningful cell state.
- Filtering choices can affect downstream conclusions.

### 4. Normalization

Normalization makes cells more comparable by adjusting for technical differences such as sequencing depth.

Biological meaning:

- Without normalization, highly sequenced cells can appear more active simply because more RNA was measured.

### 5. Highly Variable Genes

Highly variable genes are genes that show strong differences across cells. They are often used to focus the analysis on informative signals.

Biological meaning:

- Variable genes may reflect cell identity, activation, stress, cell cycle, or technical effects.

### 6. Dimensionality Reduction

Methods such as PCA and UMAP help summarize high-dimensional gene expression into fewer dimensions.

Biological meaning:

- Nearby points may represent cells with similar expression profiles.
- A UMAP plot is a visualization, not proof of a biological mechanism.

### 7. Clustering

Clustering groups cells with similar expression patterns.

Biological meaning:

- A cluster may represent a cell type, a cell state, a technical artifact, or a mixture.
- Clusters need biological annotation.

### 8. Marker Genes

Marker genes help identify cell types or states.

Biological meaning:

- Marker genes are clues, not automatic labels.
- Good annotation combines multiple markers and biological context.

### 9. Differential Expression

Differential expression compares gene expression between groups.

Biological meaning:

- A differentially expressed gene may point to a pathway, cell state, or response.
- Results need context and validation.

## Beginner Reading Order

1. Learn what RNA-seq and gene expression mean.
2. Learn the difference between bulk RNA-seq and single-cell RNA-seq.
3. Study what a count matrix and cell metadata table look like.
4. Read about quality control and normalization.
5. Learn PCA and UMAP as visualization tools.
6. Learn clustering and marker gene annotation.
7. Read one simple case study about immune cells, fibrosis, cancer, or development.
8. Try a small public dataset tutorial only after the concepts make sense.

## Suggested Mini-project

Create a short Markdown note answering:

```text
Dataset question:
Cell types expected:
Condition comparison:
Possible marker genes:
Possible technical risks:
One biological interpretation:
```

Then run:

```bash
bis-notes your_note.md --json
```

This connects biological reading with the current BiS note summarization workflow.

## Terms to Know

See [Beginner Bioinformatics Glossary](bioinformatics_glossary.md) for short definitions of:

- Count matrix
- Metadata
- Batch effect
- Normalization
- Cell type
- Cell state
- Marker gene
- Differential expression
- Pathway

## Current Status

This guide is a starter reading track. Future BiS work may add a small public dataset tutorial using common Python tools such as pandas, Scanpy, or AnnData.

