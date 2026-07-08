# Fibrosis and Immune Response Case Study Outline

This case-study outline connects fibrosis, immune response, and computational biology in beginner-friendly language.

BiS is an educational project. This document is not medical advice and does not make clinical claims.

## Learning Question

How can immune cells and fibroblasts contribute to fibrosis, and how might single-cell RNA-seq help students study that process?

## Biological Story

Fibrosis can occur when tissue repair becomes excessive. Instead of returning to normal structure, tissue can accumulate extracellular matrix and become stiff or scarred.

Important pieces:

- **Macrophages** can release inflammatory or repair-related signals.
- **Fibroblasts** help maintain and remodel extracellular matrix.
- **Myofibroblast-like states** are often linked to stronger matrix production.
- **Extracellular matrix remodeling** can change tissue structure.
- **TGF-beta signaling** is often discussed because it can promote fibroblast activation and matrix production.

## Computational Biology Angle

A beginner single-cell analysis might ask:

1. Which immune cells are present?
2. Are macrophage-related signals higher in one condition?
3. Are fibroblast clusters expanded or activated?
4. Which extracellular matrix genes are highly expressed?
5. Are patterns biological, technical, or both?

## BiS Example

See [examples/fibrosis_immune_response_note.md](../examples/fibrosis_immune_response_note.md) for a short note that can be summarized with:

```bash
bis-notes examples/fibrosis_immune_response_note.md --json
```

For a longer version, see [fibrosis_immune_response_case_study.md](fibrosis_immune_response_case_study.md).
