---
title: Evaluation
description: Run an inference pass over a held-out set, compute metrics from the stored predictions, compare against a baseline, and choose an evaluation framework for classifiers, detectors, and LLMs.
icon: clipboard-check
weight: 5
variants: +flyte +union
---

# Evaluation

Evaluation answers whether a trained model is good enough to use, and whether it is better than the one you have. It has two parts with different costs: an inference pass that runs the model over a held-out set, which needs the model's hardware, and the metrics computed from its predictions, which run on a CPU in seconds. Flyte runs them as separate tasks, so you can change a metric without running the model again.

## Separate inference from metrics

Give each part its own environment. The prediction tasks get the hardware the model needs, and the metrics task gets a CPU:

{{< code file="/unionai-examples/v2/user-guide/model-training/evaluation.py" fragment="env" lang=python >}}

## Run the inference pass

The prediction task runs the model over one shard of the held-out set and returns every prediction, not only a score:

{{< code file="/unionai-examples/v2/user-guide/model-training/evaluation.py" fragment="predict" lang=python >}}

- **Keep the predictions.** The task returns the labels, the predicted classes, and the scores as a DataFrame. You can compute new metrics from it, slice it by subgroup, or inspect the examples the model got wrong, without running the model again.
- **`cache="auto"`** stores the predictions under the model and the shard. Evaluating the same checkpoint again, for example from a later pipeline, reuses them.
- **Shards in parallel.** Each shard is its own task, so a large test set finishes in the time of one shard.

For an LLM or other large model, the inference pass is a batch inference job: load the model once per task, and send it as many examples at a time as the engine can batch. See [Batch inference](../inference/batch-inference) and [Stream model weights](../inference/stream-model-weights).

## Compute metrics from the predictions

The metrics task reads the stored predictions and returns typed metrics:

{{< code file="/unionai-examples/v2/user-guide/model-training/evaluation.py" fragment="metrics" lang=python >}}

It has no cache, because it is cheap. To add a metric, edit this task and rerun: the predictions come from the cache, and only the metrics run again.

## Compare against a baseline

A metric means little on its own. Evaluate the candidate and the model it would replace on the same held-out set, and decide from the difference:

{{< code file="/unionai-examples/v2/user-guide/model-training/evaluation.py" fragment="evaluate" lang=python >}}

The driver evaluates both models with the same code, publishes a side-by-side table to the run's report, and returns whether the candidate should be promoted. With a small test set or a noisy metric, a difference can be chance. To compare with repeated samples and a margin, see [Evaluation gates](../project-patterns/software-development-lifecycle/evaluation-gates).

## Choose an evaluation framework

The framework runs inside the metrics task, or, for LLM harnesses that call the model themselves, inside the prediction task:

| Model | Framework | What it computes |
|---|---|---|
| Classical ML | [scikit-learn metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) | Accuracy, F1, ROC AUC, calibration, regression errors |
| Deep learning | [TorchMetrics](https://lightning.ai/docs/torchmetrics/) | Metrics that accumulate over batches, including across ranks |
| Hugging Face models | [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/) | Task metrics such as BLEU, ROUGE, and seqeval |
| Object detection | [pycocotools](https://github.com/cocodataset/cocoapi) or TorchMetrics `MeanAveragePrecision` | COCO mAP |
| LLMs on standard benchmarks | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) or [lighteval](https://github.com/huggingface/lighteval) | Benchmark accuracy, with a vLLM backend for throughput |
| LLM agents and open-ended output | [Inspect](https://inspect.aisi.org.uk/) or an LLM judge | Multi-turn and tool-use tasks, and rubric scores |

Run each benchmark as its own task, so benchmarks run in parallel and are cached separately. When the judge is a paid model API, wrap the call in `@flyte.trace`, so a retried task replays the recorded result instead of paying again. See [Call a judge without paying for it twice](../reinforcement-learning/reward-setup#call-a-judge-without-paying-for-it-twice).

## Evaluate checkpoints while training runs

To see how quality changes during a long run, evaluate checkpoints as they are saved. Have the training task return checkpoints at intervals, or split training into stages, and launch an evaluation for each checkpoint with `asyncio.create_task` while the next stage trains. The evaluations run on their own hardware and never hold up the trainer. The last checkpoint isn't always the best, so keep each checkpoint's metrics in the run's [report](../tasks/task-programming/reports) and promote the one that scores highest.

## Show results in the UI

`report=True` on the driver lets it publish tables and charts, such as a confusion matrix or a precision-recall curve, to the run's report. To keep results across runs, log them from the metrics task to [Weights & Biases](../../integrations/wandb/_index) or [MLflow](../../integrations/mlflow/_index).

{{< variant union >}}
{{< markdown >}}

On {{< key product_name >}}, publish the metrics alongside the model as an [artifact](../artifacts/_index), so the model registry shows the evaluation that each version passed.

{{< /markdown >}}
{{< /variant >}}

## Related

- [BERT emotion classification](../../tutorials/model-training/bert-fine-tuning-emotion/_index): a confusion matrix and attention visualizations in the report.
- [RT-DETR object detection](../../tutorials/computer-vision/detr-object-detection/_index): COCO mAP evaluation and side-by-side bounding boxes.
- [Multimodal retrieval evaluation](../../tutorials/computer-vision/multimodal-retrieval-evaluation/_index): benchmarking three retrieval models on GPUs.
- [RL evaluation](../reinforcement-learning/evaluation): how evaluating an RL policy differs.
- [Deploy trained models](../inference/deploy-trained-models): serve the model that passed.
