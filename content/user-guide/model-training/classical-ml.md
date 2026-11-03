---
title: Classical machine learning
description: Train scikit-learn, XGBoost, and other CPU models with cached data prep and hyperparameter sweeps that run every trial in parallel.
icon: diagram-2
weight: 3
variants: +flyte +union
---

# Classical machine learning

Classical models such as gradient-boosted trees, linear models, and random forests train on CPUs in seconds to minutes. The cost is in how many times you train them: one fit per hyperparameter setting, per fold, per feature set. Flyte turns each fit into a task, runs them all at once, and caches every result, so a sweep that took an afternoon on a laptop finishes, given enough cluster capacity, in the time of its slowest trial.

## Define the environments

Trials are small and CPU-only, so each gets two CPUs. The driver gets less, because it only launches trials and compares scores:

{{< code file="/unionai-examples/v2/user-guide/model-training/classical_ml.py" fragment="env" lang=python >}}

`Image.from_uv_script` builds the image from the dependencies in the script's header. `depends_on=[env]` deploys the trial environment with the driver.

## Cache the data

Load and clean the data in its own task, with `cache="auto"`:

{{< code file="/unionai-examples/v2/user-guide/model-training/classical_ml.py" fragment="data" lang=python >}}

The task returns a `pandas.DataFrame`, which Flyte stores as Parquet in your object store. Every trial receives a reference to the same stored data, and later runs skip the load entirely. See [DataFrames](../tasks/task-programming/dataframes).

## Score one setting per task

Each hyperparameter setting is one call to an evaluation task:

{{< code file="/unionai-examples/v2/user-guide/model-training/classical_ml.py" fragment="trial" lang=python >}}

- **Typed inputs and outputs.** `Params` and `TrialResult` are dataclasses, so the UI shows each trial's settings and score, and the driver gets real objects back. See [Data classes and structures](../tasks/task-programming/dataclasses-and-structures).
- **Caching per trial.** With `cache="auto"`, rerunning a sweep with one new value only runs the new trials.
- **Retries per trial.** One trial that fails on a bad node retries on its own instead of failing the sweep.

## Run the sweep in parallel

The final fit is one more task, which trains on all of the data and saves the model as a file:

{{< code file="/unionai-examples/v2/user-guide/model-training/classical_ml.py" fragment="fit" lang=python >}}

The driver builds the grid in plain Python and launches every trial at once with `asyncio.gather`:

{{< code file="/unionai-examples/v2/user-guide/model-training/classical_ml.py" fragment="pipeline" lang=python >}}

`flyte.group("sweep")` collects the trials under one node in the UI. The driver picks the winner with ordinary Python, publishes a results table to the run's report, and calls `fit` with the best settings. The model comes back as a `flyte.io.File`, ready to pass to an evaluation task or a serving app. To limit how many trials run at once, see [Controlling parallel execution](../tasks/task-programming/controlling-parallelism).

## Search adaptively with Optuna

A grid tries every combination. To let earlier trials decide which settings to try next, drive an Optuna study from the driver task. The study asks for a setting, and `self.objective` is a Flyte task that scores it, so each trial runs as its own action:

{{< code file="/unionai-examples/v2/tutorials/ml/optimizer.py" fragment="optimizer-spawn" lang=python >}}

A semaphore bounds the number of trials in flight, and a trial that raises `flyte.errors.RuntimeUserError` is recorded as failed instead of stopping the study. See the [Hyperparameter optimization](../../tutorials/model-training/hpo/_index) tutorial for the full optimizer.

{{< variant union >}}
{{< markdown >}}

## Keep containers warm for short trials

When each trial takes seconds, starting a container for each one costs more than the trial. [Reusable containers](../tasks/task-configuration/reusable-containers) keep a pool of replicas running and send each trial to a warm one.

{{< /markdown >}}
{{< /variant >}}

## Related

- [Mapping over inputs](../tasks/task-programming/map): `flyte.map` for sweeps over a list.
- [MLflow](../../integrations/mlflow/_index) and [Weights & Biases](../../integrations/wandb/_index): log each trial to an experiment tracker.
- [Deploy trained models](../inference/deploy-trained-models): serve the fitted model behind a FastAPI app.
