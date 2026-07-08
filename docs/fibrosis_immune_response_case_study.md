# Fibrosis and Immune Response Case Study Outline

This case study outline explains fibrosis as a beginner-friendly example of how cell biology, immune response, and computational biology can connect.

BiS is an educational project. This document is not medical advice and does not make clinical claims.

## Learning Question

How can immune cells and fibroblasts contribute to fibrosis, and how might single-cell RNA-seq help students explore that process?

## Biological Background

Fibrosis is a process where tissue repair becomes excessive. Instead of returning to normal structure after injury or inflammation, tissue can accumulate extracellular matrix and become stiff or scarred.

Important biological ideas:

- Tissue injury can trigger inflammation and repair.
- Immune cells can release signals that influence fibroblast behavior.
- Fibroblasts can become activated and produce extracellular matrix.
- Myofibroblast-like states are often associated with stronger matrix production.
- TGF-beta signaling is often discussed in fibrosis because it can promote fibroblast activation and matrix remodeling.

## Main Cell Types

### Macrophages

Macrophages are immune cells involved in inflammation, cleanup, and repair. In fibrosis learning materials, they are useful because they can connect immune signaling with tissue remodeling.

Possible beginner questions:

- Are macrophage-related genes enriched in a disease sample?
- Do macrophages show inflammatory or repair-associated states?
- Which signals might connect macrophages to fibroblasts?

### Fibroblasts

Fibroblasts help maintain and remodel extracellular matrix. In fibrosis, activated fibroblast states can become central to tissue stiffening and scar formation.

Possible beginner questions:

- Are fibroblast clusters expanded in disease samples?
- Which extracellular matrix genes are highly expressed?
- Are activation markers higher in one condition?

### Other Cells

Depending on the tissue, endothelial cells, epithelial cells, T cells, neutrophils, or other stromal cells may also matter. A good beginner analysis should avoid assuming only one cell type explains the disease process.

## Data Thinking

A single-cell dataset might include:

- A gene-by-cell count matrix
- Cell metadata such as sample, condition, and batch
- Cluster labels
- Cell type annotations
- Disease and control groups

Useful analysis questions:

1. What cell types are present?
2. Which cell populations differ between conditions?
3. Which genes mark activated fibroblast states?
4. Which immune signals may be related to matrix remodeling?
5. Are observed patterns biological, technical, or both?

## Example Note for BiS

See [examples/fibrosis_immune_response_note.md](../examples/fibrosis_immune_response_note.md) for a short study note that can be summarized with the BiS CLI.

Example command:

```bash
bis-notes examples/fibrosis_immune_response_note.md --json
```

## Beginner Interpretation Template

Use this template when reading a fibrosis single-cell paper or dataset:

```text
Tissue or disease context:
Main cell types:
Immune cell signal:
Fibroblast state:
Extracellular matrix genes:
Possible pathway:
Technical limitation:
One cautious biological interpretation:
```

## Caution

Computational results do not automatically prove mechanism. A single-cell pattern may suggest a hypothesis, but stronger biological claims usually need experimental validation, careful controls, and domain expertise.

