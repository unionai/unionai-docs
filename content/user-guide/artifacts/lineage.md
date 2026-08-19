---
title: Automatic lineage tracking
weight: 6
variants: -flyte +union
---

# Automatic lineage tracking

Every artifact version carries its history with it. Union records who produced it and everything that depends on it, without any configuration on your part. The result is a graph you can walk in either direction: from a deployed model back to the run and dataset that produced it, or from a dataset forward to every model, trigger, and app that consumes it.

## What gets recorded

On the producer side, each version records how it came to exist:

* A task output records the run and task that produced it, with a link to that execution and its inputs and logs.
* An upload through `flyte.remote.Artifact.create()` or `flyte create artifact` records who published it, and the `external_ref` if one was given, pointing at the original location of the data.
* A Hugging Face prefetch records the source repo and commit.

On the consumer side, Union records each place a version is bound to compute:

* Apps whose deployment resolved the artifact as a parameter, down to the exact pinned version.
* Triggers watching the artifact name, and the runs they started.

## The lineage view

Each artifact in the UI has a **Lineage** tab that draws this graph. The source action that produced the artifact sits on the left, and the dependents fan out on the right: the triggers watching the artifact name, and the apps pinning the selected version. App and run nodes link to their own pages, so you can jump from the graph to a consuming app's deployment or the producing run's logs. Trigger rows expand in place to reveal the runs they started.

The neighboring tabs break out the same relationships as lists: **Versions** shows the full version history, **Triggers** and **Apps** list what depends on the artifact, and **Artifact card** renders the attached model or data card.

Before deleting or reworking a dataset, you can see every model trained on it and every app serving those models. When a served model misbehaves, you can walk back to the training run and the exact dataset version it consumed.

You can query the same relationships from the CLI:

```bash
flyte get artifact --source-run my_run          # what a run produced
flyte get artifact --source-external-ref s3://partner-bucket/drop/2026-08-18.csv
```

In Python, `flyte.remote.Artifact` exposes `source`, `created_by`, and `url`, which links to the artifact's page in the UI.

## What is not recorded

Calling `Artifact.get()` in your own code and reading the data is a plain fetch, and does not create a consumer edge in the graph. Passing an artifact as a task input does not record a consumer edge yet either. Today the tracked dependencies are apps that declare the artifact as a parameter and the runs started by artifact triggers.
