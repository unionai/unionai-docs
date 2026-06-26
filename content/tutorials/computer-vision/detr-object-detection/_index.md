---
title: RT-DETR object detection
weight: 3
variants: +flyte +union
---

# RT-DETR object detection

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/detr_object_detection).

This tutorial fine-tunes [RT-DETRv2](https://huggingface.co/PekingU/rtdetr_v2_r18vd) on a custom COCO-format dataset from HuggingFace. The pipeline downloads and splits the data, fine-tunes the detector with live training charts in Flyte reports, evaluates COCO mAP on a validation split, and renders a side-by-side inference demo with ground-truth and predicted bounding boxes.

Flyte highlights:

- **Cached dataset preparation** so re-runs skip the HuggingFace download.
- **Live training reports** with loss curves and optional periodic mAP checkpoints.
- **GPU evaluation and demo tasks** that stream annotated images into the UI.

## Define the task environments

{{< code file="/unionai-examples/v2/tutorials/detr_object_detection/detr_object_detection.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "torch>=2.9.0",
#    "transformers>=4.49.0",
#    "albumentations>=1.4.0",
#    "torchmetrics>=1.4.0",
#    ...
# ]
# ///
```

## Orchestrate the pipeline

The `pipeline` task prepares data, fine-tunes RT-DETR, evaluates mAP, and renders an inference demo.

{{< code file="/unionai-examples/v2/tutorials/detr_object_detection/detr_object_detection.py" fragment=pipeline lang=python >}}

## Run the workflow

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/detr_object_detection):

```
cd v2/tutorials/detr_object_detection
uv run --script detr_object_detection.py
```

Quick local smoke test with one epoch:

```
flyte run detr_object_detection.py pipeline --epochs 1 --batch_size 2
```

This workflow needs a GPU. Check the **train**, **evaluate**, and **inference_demo** task reports for charts and annotated images.
