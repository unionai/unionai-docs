---
title: Genomic variant effect prediction
weight: 3
variants: +flyte +union
---

# Genomic variant effect prediction

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/genomic_variant_effect).

This tutorial demonstrates zero-shot variant effect prediction (VEP) with HuggingFace [Carbon](https://huggingface.co/HuggingFaceBio/Carbon-3B). The pipeline loads clinically relevant variants across genes such as BRCA2, TP53, CFTR, KRAS, and HBB, scores each mutation with a log-likelihood ratio, and produces rich HTML reports with DNA tracks, lollipop plots, confusion matrices, and ranked pathogenicity tables.

Flyte provides:

- **GPU-backed inference** for Carbon scoring with live progress reports.
- **CPU analysis tasks** for visualization and accuracy metrics without holding a GPU.
- **End-to-end orchestration** from variant loading through summary reporting.

## Define the task environments

{{< code file="/unionai-examples/v2/tutorials/genomic_variant_effect/genomic_variant_effect.py" fragment=env lang=python >}}

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

The `pipeline` task loads variants, scores them with Carbon, analyzes classification accuracy against known labels, and generates a summary report.

{{< code file="/unionai-examples/v2/tutorials/genomic_variant_effect/genomic_variant_effect.py" fragment=pipeline lang=python >}}

## Run the workflow

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/genomic_variant_effect):

```
cd v2/tutorials/genomic_variant_effect
uv run --script genomic_variant_effect.py
```

Use a smaller Carbon model for faster iteration:

```
flyte run genomic_variant_effect.py pipeline --model_name HuggingFaceBio/Carbon-500M
```

Negative VEP scores indicate the model prefers the reference allele over the alternate, a signal correlated with pathogenicity in this zero-shot setup.
