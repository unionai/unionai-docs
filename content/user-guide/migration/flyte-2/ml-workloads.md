---
title: ML workloads
weight: 9
variants: +flyte +union
---

# ML workloads

The core patterns compose into the workloads data scientists and ML engineers run every day. Each of these is a complete v1→v2 pair in the [examples repo](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/migration/flyte-2). See [Migration](./migration) for the overall approach.

## Small model training (scikit-learn / XGBoost)

Train a model, persist it as a `File`, and evaluate it. Image, resources, and caching move to the `TaskEnvironment`; `FlyteFile` becomes `flyte.io.File`.

{{< tabs "migration-train-xgboost" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/train_xgboost_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/train_xgboost_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Hyperparameter optimization

Fan out one training run per hyperparameter, then pick the best. In Flyte 1 the grid search runs through `map_task` and the "pick the best" step must itself be a task. In Flyte 2 you `gather` the runs and select the winner in plain Python.

{{< tabs "migration-hpo" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/hpo_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/hpo_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Large model training (deep learning)

GPU configuration moves to the `TaskEnvironment`: the Flyte 1 `Resources(gpu="1")` plus a separate `accelerator=T4` become a single `gpu="T4:1"` string on `flyte.Resources`.

{{< tabs "migration-deep-learning" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/train_deep_learning_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/train_deep_learning_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

For multi-node distributed training (PyTorch elastic, etc.), see [Resources](../../task-configuration/resources) and the plugin integrations.

## Batch inference

Load a trained model once and score many batches in parallel. `map_task` with a `partial`-bound model becomes `asyncio.gather` over the batches, reusing the same model reference.

{{< tabs "migration-batch-inference" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/batch_inference_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/batch_inference_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## A complete example: end-to-end ML pipeline

Putting it together — a load / train / evaluate pipeline shows the image, resources, caching, file I/O, and orchestration changes in one place.

{{< tabs "migration-ml-pipeline" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/ml_pipeline_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/ml_pipeline_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Next

- [New in Flyte 2](./new-in-flyte-2) — real-time serving, apps, and sandboxing
- [Considerations](./considerations) — caveats of the new execution model
