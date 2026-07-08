# Single-cell RNA-seq Starter Reading Guide

This guide is a beginner-friendly reading path for students who want to understand single-cell RNA-seq before running full analysis workflows.

## What Single-cell RNA-seq Is

Single-cell RNA-seq measures RNA abundance in individual cells. Instead of averaging a whole tissue sample, it lets learners ask which cell types are present and how cell states differ across conditions.

Beginner questions:

- Which cell populations are present?
- Which genes distinguish one cell group from another?
- Are immune cells activated in a disease sample?
- Do fibroblasts show extracellular matrix remodeling signals?

## Concepts to Learn First

1. **Gene expression matrix:** a table where rows are genes and columns are cells.
2. **Cell metadata:** information about each cell, such as sample, condition, batch, or cell type.
3. **AnnData:** a common Python object that stores the matrix, metadata, and analysis results.
4. **`.h5ad`:** a common file format for saving AnnData objects.
5. **Quality control:** filtering unreliable cells or genes before interpretation.
6. **Normalization:** adjusting counts so cells can be compared more fairly.
7. **Dimensionality reduction:** using methods such as PCA or UMAP to summarize high-dimensional data.
8. **Clustering:** grouping cells with similar expression patterns.
9. **Marker genes:** genes used as clues for cell type or cell state annotation.
10. **Differential expression:** comparing groups to find genes with changed expression.

## Next Topics

- Cell type annotation
- Batch effects
- Marker gene interpretation
- Fibrosis and immune response case studies
- Public `.h5ad` tutorial datasets

For a longer version, see [single_cell_rna_seq_starter.md](single_cell_rna_seq_starter.md).
