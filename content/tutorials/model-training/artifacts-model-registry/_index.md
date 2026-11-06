---
title: Artifacts as a model registry
icon: box-seam
description: Version, stage, promote, and roll out models with artifacts, partitions, and triggers, with every transition recorded as lineage.
weight: 11
variants: -flyte +union
---

# Artifacts as a model registry

> [!NOTE]
> Code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/artifacts_model_registry).
> Requires flyte 2.12.2 or later.

A model registry answers four questions: which versions of a model exist, what each one is, which one is production, and what happens when a new one arrives. Artifacts answer the first two directly. This tutorial uses partitions for the third and triggers for the fourth, so the whole registry is one artifact name and two tasks.

The pipeline:

1. A `sweep` task trains several candidates, renders a leaderboard, and publishes the winner as a `stage=candidate` version of `sentiment-model`.
2. A trigger scoped to `stage=candidate` runs `evaluate`. If the candidate beats production, `evaluate` publishes the same weights as a `stage=production` version with lineage back to the candidate.
3. A trigger scoped to `stage=production`, pinned to a released version of the `rollout` task, hands the promoted model to serving.

Two things make this work without a mutable "production" pointer:

- **Stages are partitions.** Both stages are string partitions on one artifact name. `flyte.remote.Artifact.get(MODEL, stage="production")` answers "what is production", and `flyte.OnArtifact(MODEL, stage=...)` scopes each trigger so the candidate trigger never fires on a promotion.
- **Promotion is a new version.** Artifact metadata is immutable once published. `evaluate` republishes the candidate's value into the production partition and names the candidate as its parent. No data is copied, and the lineage graph records what was promoted from what.

See [Partitioned artifacts](../../../user-guide/artifacts/partitions) and [Automatic lineage tracking](../../../user-guide/artifacts/lineage) for the underlying features.

## Define the environment

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=env lang=python >}}

`MODEL` is the artifact name the whole registry lives under. `DATASET` is the artifact the sweep trains on, so every model version can point at the exact dataset version it came from.

## Train one candidate

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=train lang=python >}}

Each `train` call is one tracked run. The platform records its inputs (the hyperparameters), its task version (the code), and the dataset artifact it read (the data). `cache="auto"` means a sweep that repeats a configuration reuses the earlier result instead of retraining.

The training itself is a stand-in. Replace the body with your framework's training loop and keep the shape: weights in a `flyte.io.Dir`, metrics as plain numbers.

## Run the sweep and publish the winner

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=sweep lang=python >}}

The sweep is the experiment. It holds every trial's result, so it renders the comparison with `flyte.report.log` and attaches the same table to the candidate as a `flyte.artifacts.Card`.

The call to `flyte.remote.Artifact.create` is what makes this a registry entry:

| Argument | What it records |
| --- | --- |
| `kind="model"` | What the artifact is. `Artifact.listall(kind="model")` lists only models. |
| `attrs` | Framework, architecture, and metrics as strings. Filterable by equality with `Artifact.listall(attrs={...})`. |
| `card` | The leaderboard, rendered in the UI next to the version. |
| `partitions={"stage": "candidate", "date": ...}` | The stage, plus a time partition for range queries. |
| `parents=[dataset.artifact_version_id]` | Lineage across names: this model version derives from that dataset version. |

Because the version is created from inside a running task, the producing run, action, and attempt are recorded as its source without any extra arguments.

## Evaluate every candidate

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=on-candidate lang=python >}}

`flyte.OnArtifact` fires on every new version of `sentiment-model` whose `stage` partition is `candidate`. The version itself arrives in the `candidate` input through `flyte.TriggeredArtifact`.

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=evaluate lang=python >}}

`Artifact.get(MODEL, stage="production")` returns the newest version in the production partition, or raises if nothing has been promoted yet. If the candidate wins, `evaluate` publishes it into the production partition. The value is the candidate's `Dir`, so the new version references the same storage; `parents=[candidate.artifact_version_id]` and the `promoted_from` attr make the promotion traceable from both the lineage graph and the attrs.

Because this version lands in `stage=production`, the candidate trigger ignores it. Without the partition filter, every promotion would fire another evaluation.

## Roll out a promoted model

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=on-production lang=python >}}

This trigger watches the production partition only. `task_version` pins it to a released version of `rollout`. Deploying newer versions of the environment updates the trigger's inputs and automation from code but leaves it running `v1.4.0`. To move production to a newer rollout, change the pin and redeploy; to roll back, change it back.

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=rollout lang=python >}}

The example smoke-tests the weights. In a serving pipeline, this task redeploys the app with `flyte.app.ArtifactValue(name=MODEL, version=model.version)` as a parameter, which pins the app to that version and records app-to-model lineage. See [Use artifacts in apps](../../../user-guide/artifacts/artifacts-in-apps).

## Run it

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=main lang=python >}}

`main` registers a small dataset with `external_ref` pointing at where it was imported from, runs one sweep, and returns the candidate's version. The triggers do the rest.

Deploy the environment first so both triggers exist. The rollout trigger needs its pinned task version to be deployed:

```bash
cd v2/tutorials/artifacts_model_registry
flyte deploy --version v1.4.0 main.py env
uv run --script main.py
```

An `evaluate` run appears shortly after `main` finishes, launched by the trigger. If the candidate was promoted, a `rollout` run follows.

## Query the registry

{{< code file="/unionai-examples/v2/tutorials/artifacts_model_registry/main.py" fragment=query lang=python >}}

Other queries the same data supports:

```python
# All versions of the model, newest first
Artifact.listall(MODEL)

# Candidates from a specific sweep run
Artifact.listall(MODEL, stage="candidate", source_run=run.name)

# Production versions promoted this month
Artifact.listall(MODEL, stage="production", date=(date(2026, 11, 1), date(2026, 11, 30)))

# One version per distinct partition, newest first
Artifact.listall(MODEL, latest_per_partition=True)
```

## Limitations

- **Metrics are strings.** `attrs` values are compared by equality. "Best candidate by accuracy" is a client-side sort over `Artifact.listall`, as `show_registry` does. Put metrics in `attrs`, not in partitions: partitions are identity, so a continuous value as a partition makes every version its own partition and defeats `latest_per_partition` and partition-scoped triggers.
- **Partition keys are fixed per artifact name** by the first partitioned version. To add a key, use a new name.
- **"Latest" is by creation time**, not by version string. `Artifact.get(MODEL)` with no partition returns the newest version in any stage. Query with `stage=` when the stage matters.
- **Deleting a version does not delete its data.** `Artifact.delete` removes the registry entry; the blob stays in storage.

## Related pages

- [Artifacts](../../../user-guide/artifacts/)
- [Partitioned artifacts](../../../user-guide/artifacts/partitions)
- [Partition triggers](../../../user-guide/triggers/partition-triggers)
- [Use artifacts in apps](../../../user-guide/artifacts/artifacts-in-apps)
- [Hyperparameter optimization](../hpo)
