---
title: Fraud detection with Feast
weight: 3
variants: +flyte +union
---

# Fraud detection with Feast

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/fraud_detection_feast).

This tutorial builds a credit-card fraud detection pipeline that combines [Feast](https://feast.dev/) feature store materialization with an XGBoost classifier on the Sparkov simulated transactions dataset. The workflow engineers transaction and user-level features, trains a model, registers features in Feast, and materializes online feature values for low-latency scoring.

Flyte provides:

- **Cached data preparation** for the Kaggle dataset download and feature engineering.
- **Report-backed training** with confusion matrix and ROC-style metrics in the UI.
- **Durable artifacts** — the trained model and Feast repo are returned as `flyte.io.File` and `flyte.io.Dir`.

## Define the task environment

{{< code file="/unionai-examples/v2/tutorials/fraud_detection_feast/fraud_detection_feast.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "feast==0.63.0",
#    "xgboost==3.2.0",
#    "scikit-learn==1.8.0",
#    "kagglehub==0.3.12",
#    ...
# ]
# ///
```

## Orchestrate the pipeline

The `fraud_detection_pipeline` task downloads data, trains XGBoost, applies Feast feature definitions, and materializes features.

{{< code file="/unionai-examples/v2/tutorials/fraud_detection_feast/fraud_detection_feast.py" fragment=pipeline lang=python >}}

## Run the workflow

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/fraud_detection_feast):

```
cd v2/tutorials/fraud_detection_feast
uv run --script fraud_detection_feast.py
```

The first run downloads the dataset via `kagglehub` (public dataset, no API key required). Open the run report to review the confusion matrix and feature-importance summary when training completes.
