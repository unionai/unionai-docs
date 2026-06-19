---
title: BERT emotion classification
weight: 3
variants: +flyte +union
---

# BERT emotion classification

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/bert_fine_tuning_emotion).

This tutorial fine-tunes a BERT-style model (ModernBERT by default) on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) Twitter dataset for six-way emotion classification: sadness, joy, love, anger, fear, and surprise. The pipeline trains the classifier, evaluates with a confusion matrix and per-class F1, and explores inference with attention and token-importance visualizations in Flyte reports.

Flyte provides:

- **GPU fine-tuning** with live training loss charts.
- **Rich evaluation reports** including confusion matrices and confidence bars.
- **Cached dataset loading** for repeatable experiments.

## Define the task environments

{{< code file="/unionai-examples/v2/tutorials/bert_fine_tuning_emotion/bert_fine_tuning_emotion.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "torch>=2.1.0",
#    "transformers>=4.45.0",
#    "datasets>=3.0.0",
#    "scikit-learn",
#    ...
# ]
# ///
```

## Orchestrate the pipeline

{{< code file="/unionai-examples/v2/tutorials/bert_fine_tuning_emotion/bert_fine_tuning_emotion.py" fragment=pipeline lang=python >}}

## Run the workflow

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/bert_fine_tuning_emotion):

```
cd v2/tutorials/bert_fine_tuning_emotion
uv run --script bert_fine_tuning_emotion.py
```

Quick smoke test with a small sample:

```
flyte run bert_fine_tuning_emotion.py pipeline --max_train_samples 200 --max_eval_samples 50 --epochs 1
```

Open the **evaluate** and **explore_inference** task reports for confusion matrices and attention visualizations.
