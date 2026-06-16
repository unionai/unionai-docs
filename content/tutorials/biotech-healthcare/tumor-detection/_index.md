---
title: Brain tumor MRI classification
weight: 2
variants: +flyte +union
---

# Brain tumor MRI classification

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/tumor_detection).

This tutorial builds a medical-imaging pipeline that classifies brain MRI scans into four categories — Glioma, Meningioma, No Tumor, and Pituitary — using a two-phase EfficientNet-B4 transfer-learning strategy. The pipeline downloads the dataset, trains on a GPU with fault-tolerant checkpointing, and renders training curves and a confusion matrix directly in the {{< key product_name >}} UI.

The example is split into focused modules:

- `config.py` — container image, task environments, and the `TrainingConfig` hyperparameters.
- `dataset.py` — downloads the Hugging Face dataset, builds class-balanced data loaders.
- `model.py` / `training.py` — the Lightning module and the two-phase training loop.
- `utils.py` — plotting helpers for the report.
- `run.py` — the three Flyte tasks and the pipeline driver.

Flyte handles the production concerns:

- **Per-task resources**: CPU for download/reporting, a GPU for training.
- **`cache="auto"`** on dataset download and training, so reruns with the same data and config are free.
- **`retries=3`** plus **Flyte checkpointing** on the training task so a preempted GPU job resumes from the last epoch.
- **Built-in reports** to visualize metrics without separate dashboard infrastructure.

## Define the container image

A single GPU-ready image is shared by all tasks. `with_source_folder` copies the local modules (`dataset.py`, `model.py`, etc.) into the image.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/config.py" fragment=image lang=python >}}

## Define the task environments

Each stage declares the resources it needs. The lightweight `pipeline_env` orchestrates the others via `depends_on`.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/config.py" fragment=envs lang=python >}}

## Configure training

Hyperparameters are gathered in a single `TrainingConfig`, serialized to JSON, and passed into the training task so the exact configuration is captured alongside the run.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/run.py" fragment=config lang=python >}}

## Load the dataset

The first task downloads the public [Brain Tumor MRI dataset](https://huggingface.co/datasets/AIOmarRehan/Brain_Tumor_MRI_Dataset) from Hugging Face (no auth required) and stores it as a `flyte.io.Dir`. It's cached, so subsequent runs reuse it.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/run.py" fragment=load_dataset lang=python >}}

## Train the model

The training task downloads the dataset `Dir`, runs two-phase training (frozen backbone, then full fine-tuning), and writes metrics and predictions to an output `Dir`. It sets `retries=3` so a preempted GPU node restarts the task.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/run.py" fragment=train_model lang=python >}}

### Resumable checkpointing

To make retries cheap, training mirrors its Lightning checkpoint directory to a `flyte.Checkpoint` after every epoch, and resumes from the latest checkpoint when the task restarts.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/training.py" fragment=flyte_checkpoint lang=python >}}

On startup, the training loop looks for a checkpoint from a previous attempt and resumes from it if present:

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/training.py" fragment=resume lang=python >}}

## Generate the report

The reporting task reads the metrics and predictions, then renders accuracy/loss curves, a confusion matrix, and a per-class F1 chart with Plotly. `report=True` surfaces the HTML directly in the run's report panel.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/run.py" fragment=create_report lang=python >}}

## Orchestrate the pipeline

The driver task wires the three steps together.

{{< code file="/unionai-examples/v2/tutorials/tumor_detection/run.py" fragment=pipeline lang=python >}}

## Run the pipeline

This example has no secrets — the dataset is public. Because the pipeline imports sibling modules and uses `with_source_folder`, run it from inside the example directory so the local files are picked up.

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/tumor_detection):

```
cd v2/tutorials/tumor_detection
python run.py
```

Or submit it with the Flyte CLI from the same directory:

```
flyte run run.py tumor_detection_pipeline
```

When the run completes, open the `create_report` task in the UI to view the training curves, confusion matrix, and per-class F1 scores.
