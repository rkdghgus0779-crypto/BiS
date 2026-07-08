# Beginner Bioinformatics Glossary

This glossary defines common terms that appear in bioinformatics, computational biology, and biomedical AI learning materials. The explanations are intentionally short and beginner-friendly.

BiS is an educational project. These definitions are not medical advice and should not be used for diagnosis or treatment decisions.

## Core Terms

### Bioinformatics

Bioinformatics is the use of computation to store, process, analyze, and interpret biological data. Examples include DNA sequences, RNA expression measurements, protein data, and single-cell datasets.

### Computational Biology

Computational biology uses mathematical, statistical, and computational methods to understand biological systems. It often asks questions about mechanisms, patterns, and models, not only data storage or processing.

### Biomedical AI

Biomedical AI applies machine learning and artificial intelligence to biomedical questions. In an educational project, this may include learning how models are trained, how data quality affects results, and why biological interpretation matters.

### Reproducible Analysis

A reproducible analysis can be rerun by another person and produce the same or similar results. It usually includes clear code, documented inputs, fixed software versions, and transparent assumptions.

### Dataset

A dataset is a structured collection of observations. In biology, a dataset might contain gene expression counts, sample metadata, cell annotations, imaging measurements, or clinical variables.

### Metadata

Metadata describes the dataset. For example, in a single-cell experiment, metadata may include sample ID, tissue source, disease condition, batch, cell type, or sequencing platform.

### Feature

A feature is a measurable variable used in analysis. In gene expression analysis, genes are often treated as features. In clinical prediction, features may include lab values or demographic variables.

### Sample

A sample is a biological or experimental unit. Depending on context, a sample may mean a patient sample, tissue sample, sequencing library, or experimental condition.

### Batch Effect

A batch effect is unwanted variation caused by technical differences rather than biological differences. For example, samples processed on different days may look different even if the biology is similar.

### Normalization

Normalization adjusts data so samples can be compared more fairly. In RNA-seq, normalization helps account for differences such as sequencing depth.

## Gene Expression Terms

### Gene Expression

Gene expression describes how active a gene is in a cell or sample. RNA measurements are often used as a proxy for gene activity.

### RNA-seq

RNA-seq is a sequencing method used to measure RNA abundance. It can help identify which genes are active in a tissue, condition, or cell population.

### Single-cell RNA-seq

Single-cell RNA-seq measures gene expression in individual cells. This helps researchers study cell types, cell states, and differences between cells that would be hidden in bulk measurements.

### Bulk RNA-seq

Bulk RNA-seq measures gene expression from a mixture of many cells. It gives an average signal across the sample, which can be useful but may hide rare cell populations.

### Count Matrix

A count matrix stores gene expression counts. Rows often represent genes, columns often represent cells or samples, and each value represents how many reads or molecules were detected.

### Differential Expression

Differential expression analysis looks for genes that have different expression levels between groups, such as disease versus control or one cell type versus another.

## Single-cell Terms

### Cell Type

A cell type is a category of cells with shared biological identity and function, such as T cells, macrophages, fibroblasts, or endothelial cells.

### Cell State

A cell state is a temporary or context-dependent condition of a cell. For example, immune cells can become activated, exhausted, inflammatory, or repair-associated.

### Clustering

Clustering groups cells with similar expression profiles. It is often used in single-cell analysis to find possible cell types or states.

### Dimensionality Reduction

Dimensionality reduction turns high-dimensional data into fewer dimensions for visualization or analysis. PCA, UMAP, and t-SNE are common examples.

### Marker Gene

A marker gene is a gene commonly associated with a cell type or cell state. Marker genes help annotate clusters, but they should be interpreted carefully.

### Cell Type Annotation

Cell type annotation assigns biological labels to clusters or cells. It usually combines marker genes, reference datasets, and domain knowledge.

## Interpretation Terms

### Pathway

A pathway is a set of biological molecules and interactions involved in a process, such as inflammation, cell cycle, or extracellular matrix remodeling.

### Enrichment Analysis

Enrichment analysis asks whether a group of genes is overrepresented in known pathways, processes, or gene sets.

### Biomarker

A biomarker is a measurable biological signal associated with a condition, process, or response. A candidate biomarker needs careful validation before clinical use.

### Model

A model is a simplified representation used to make predictions or explain patterns. Models can be statistical, machine learning-based, or conceptual.

### Overfitting

Overfitting happens when a model learns noise or dataset-specific details instead of general patterns. An overfit model may perform well on training data but poorly on new data.

### Validation

Validation checks whether a result or model holds up in independent data, experiments, or settings.

## Learning Advice

When learning bioinformatics, try to connect each technical step to a biological question:

- What biological system is being studied?
- What is one row and one column in the data?
- What does each feature mean biologically?
- What assumptions does the method make?
- What would count as a strong or weak interpretation?

