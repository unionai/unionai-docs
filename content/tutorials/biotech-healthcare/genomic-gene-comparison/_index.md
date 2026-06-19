---
title: Cross-species gene comparison
weight: 2
variants: +flyte +union
---

# Cross-species gene comparison

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/genomic_gene_comparison).

This tutorial builds a bioinformatics pipeline that compares homologous genes across species. The workflow loads curated gene sequences (insulin, hemoglobin, or p53 by default), scores each sequence with the [Carbon](https://huggingface.co/HuggingFaceBio/Carbon-3B) genomic language model, aligns DNA and translated protein sequences, folds proteins with [ESMFold](https://github.com/facebookresearch/esm), and renders interactive HTML reports with identity heatmaps, phylogenetic trees, and 3D structure viewers.

Flyte makes the multi-stage GPU/CPU pipeline reliable:

- **Separate CPU and GPU `TaskEnvironment`s** so alignment runs on modest CPU boxes while Carbon scoring and ESMFold run on GPUs.
- **`report=True`** on every stage for live HTML progress and final summaries in the Flyte UI.
- **Cached data loading** and orchestrated fan-out across pipeline stages.

## Define the task environments

GPU tasks handle Carbon log-likelihood scoring and ESMFold structure prediction; CPU tasks load gene sets, run Needleman-Wunsch alignments, and generate the final summary.

{{< code file="/unionai-examples/v2/tutorials/genomic_gene_comparison/genomic_gene_comparison.py" fragment=env lang=python >}}

Dependencies are declared at the top of the file using the `uv` script style:

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "torch>=2.9.0",
#    "transformers>=4.49.0",
#    "accelerate>=0.34.0",
#    "numpy",
# ]
# ///
```

## Orchestrate the pipeline

The top-level `pipeline` task chains four stages: load genes, Carbon scoring, sequence alignment, ESMFold folding, and a cross-species summary report.

{{< code file="/unionai-examples/v2/tutorials/genomic_gene_comparison/genomic_gene_comparison.py" fragment=pipeline lang=python >}}

## Run the workflow

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/genomic_gene_comparison):

```
cd v2/tutorials/genomic_gene_comparison
uv run --script genomic_gene_comparison.py
```

Or submit a specific gene set with the Flyte CLI:

```
flyte run genomic_gene_comparison.py pipeline --gene_set hemoglobin
```

This example needs a GPU for Carbon and ESMFold. Open the run URL and check each task's report tab for heatmaps, dendrograms, and interactive 3D viewers.
