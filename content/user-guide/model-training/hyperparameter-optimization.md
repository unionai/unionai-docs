---
title: Hyperparameter optimization
description: Run hyperparameter sweeps with every trial as its own task, stop weak trials early, search adaptively with Optuna, and drive sweeps from Weights & Biases or Hydra.
icon: sliders
weight: 4
variants: +flyte +union
---

# Hyperparameter optimization

A sweep trains the same model many times with different settings and keeps the best one. Most of its cost goes to trials that turn out to be bad. Flyte makes each trial a task, so trials run in parallel on their own hardware, retry on their own, and are cached. The driver that chooses which trials to run is ordinary Python, so you can stop weak trials early and give their budget to strong ones.

## Run every trial as a task

Put trials and the driver in separate environments. Each trial gets the hardware one training run needs, and the driver only chooses settings and compares scores:

{{< code file="/unionai-examples/v2/user-guide/model-training/hpo.py" fragment="env" lang=python >}}

The trial task trains one setting for a number of epochs and returns its validation score with a checkpoint. It can also continue from a checkpoint, which the next section uses:

{{< code file="/unionai-examples/v2/user-guide/model-training/hpo.py" fragment="trial" lang=python >}}

- **`cache="auto"`** stores every finished trial. Rerunning the sweep with more trials runs only the new ones, and a sweep that failed halfway resumes without retraining what finished.
- **`retries=2`** reruns a trial that hit a bad node, without failing the sweep.
- **Typed results.** `Params` and `Trial` are dataclasses, so the UI shows each trial's settings, score, and checkpoint.

## Sweep in parallel

A random search samples settings and launches every trial at once. A semaphore caps how many run at the same time, so a large sweep doesn't take the whole cluster:

{{< code file="/unionai-examples/v2/user-guide/model-training/hpo.py" fragment="random-search" lang=python >}}

Sample from a seeded `random.Random`, so a rerun proposes the same settings and gets every finished trial from the cache. Random search usually finds a good setting with fewer trials than a grid, because it doesn't spend trials on dimensions that don't matter. For a grid over a few values, see [Classical machine learning](./classical-ml#run-the-sweep-in-parallel).

## Stop weak trials early

Most trials are bad after a few epochs as well as at the end. Successive halving trains every trial on a small budget, keeps the best fraction, and continues only those from their checkpoints with a larger budget:

{{< code file="/unionai-examples/v2/user-guide/model-training/hpo.py" fragment="halving" lang=python >}}

With 16 trials and `eta=2`, the sweep trains 16 trials for 2 epochs, 8 for 4, 4 for 8, 2 for 16, and 1 for 32. Because survivors continue from their checkpoints, that is 96 epochs of training in total, against 512 to train all 16 for 32 epochs. Each rung is a group in the UI. A surviving trial passes its checkpoint to its next rung, so it continues training instead of starting over. Hyperband runs several of these brackets with different starting budgets, and the same driver loop covers it.

## Search adaptively with Optuna

To let earlier trials decide which settings to try next, drive an Optuna study from the driver task. The study asks for a setting, and `self.objective` is a Flyte task that scores it, so each trial runs as its own action:

{{< code file="/unionai-examples/v2/tutorials/ml/optimizer.py" fragment="optimizer-spawn" lang=python >}}

A semaphore bounds the trials in flight, and a trial that raises `flyte.errors.RuntimeUserError` is recorded as failed instead of stopping the study. Optuna's samplers, such as TPE, propose each new setting from the results so far, so the number of trials in flight trades speed against how much each proposal can learn. See the [Hyperparameter optimization](../../tutorials/model-training/hpo/_index) tutorial for the full optimizer.

## Use a sweep tool you already have

These integrations run their own search and use Flyte to execute the trials:

| Integration | How it sweeps | Each trial runs as |
|---|---|---|
| [Weights & Biases sweeps](../../integrations/wandb/sweeps) | `@wandb_sweep` creates a W&B sweep, and parallel agent tasks pull settings from it. W&B chooses the settings with grid, random, or Bayesian search, and plots every trial. | One call in a sweep agent task |
| [Hydra](../../integrations/hydra/_index) | `--multirun` expands config overrides into a grid, and `hydra/sweeper=optuna` runs an Optuna sweeper over your Hydra config. | A separate Flyte run |
| [Ray](../../integrations/ray/_index) | Ray Tune runs its schedulers, such as ASHA and PBT, on a Ray cluster that a task starts. | A Ray trial inside one task |

To record every trial's settings and metrics in an experiment tracker, log from the trial task with [Weights & Biases](../../integrations/wandb/experiments) or [MLflow](../../integrations/mlflow/_index).

## Size trials for the hardware

- **GPU trials.** Give each trial one GPU, and cap concurrency at the number of GPUs you want the sweep to use. A trial that runs out of memory raises `flyte.errors.OOMError` to the driver, which can record it as failed. See [Resilient training](./resilient-training#recover-from-out-of-memory-errors).
- **Multi-node trials.** Make the trial task a `flyte.clustered.ClusteredTaskEnvironment`. The driver doesn't change. See [Pretraining](./pretraining).
- **Preemptible capacity.** Trials are short and retry on their own, so they suit `interruptible=True`. Keep the driver on on-demand capacity. See [Use spot capacity](./resilient-training#use-spot-capacity).

{{< variant union >}}
{{< markdown >}}

- **Seconds-long trials.** When a trial takes less time than a container takes to start, use [reusable containers](../tasks/task-configuration/reusable-containers) to send trials to a warm pool of replicas.

{{< /markdown >}}
{{< /variant >}}

## Related

- [Hyperparameter optimization](../../tutorials/model-training/hpo/_index): a parallel Optuna study, end to end.
- [Controlling parallel execution](../tasks/task-programming/controlling-parallelism): limit concurrency for a whole run.
- [Evaluation](./evaluation): score the winning setting on a held-out set before you promote it.
