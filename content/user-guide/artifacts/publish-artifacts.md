---
title: Publish your own artifacts
description: Upload existing datasets and model weights from anywhere with `Artifact.create` or `flyte create artifact`, recording where they came from.
icon: cloud-upload
weight: 2
variants: -flyte +union
---

# Publish your own artifacts

Not every dataset or model is produced by a task. You can publish an existing asset as an artifact from anywhere: a laptop, a notebook, a CI job, or an external pipeline. This is how you bootstrap a registry from assets you already have.

## From Python

Use `flyte.remote.Artifact.create()`. It uploads the value and registers a version in one call:

```python
import flyte
from flyte.io import File
from flyte.remote import Artifact

flyte.init_from_config()

published = Artifact.create(
    File.from_local_sync("data/2026-08-18.csv"),
    name="incoming_dataset",
    description="Dataset dropped off by a partner",
    external_ref="s3://partner-bucket/drop/2026-08-18.csv",
)
print(published.name, published.version)
```

If you do not pass a `version`, one is generated for you. Pass `attrs`, `kind`, and `card` the same way as in task-produced [metadata](./task-outputs#metadata). The call is synchronous by default; use `Artifact.create.aio(...)` from async code.

The `external_ref` records where the data came from. When `Artifact.create()` runs inside a task, the producing run is stamped on the artifact automatically; outside a task, `external_ref` is the provenance you can attach.

## From the CLI

`flyte create artifact` publishes a file directly:

```bash
flyte create artifact my-model --from-file model.pt --kind model --attr framework=torch
flyte create artifact llama3 --from-file weights.bin --external-ref hf://meta-llama/Meta-Llama-3-8B
flyte create artifact my-model --from-file model.pt --card model_card.html --card-type model
```

`--attr` is repeatable, `--kind` is one of `model`, `data`, or `generic`, and the card format is inferred from the file extension.

## Finding artifacts

`flyte get artifact` browses the registry:

```bash
flyte get artifact                        # all artifact names, with latest version info
flyte get artifact my-model               # every version of my-model, newest first
flyte get artifact my-model 1.0           # details of one version
flyte get artifact --search model         # names containing "model"
flyte get artifact --source-run my_run    # versions produced by a run
flyte get artifact --kind model --attr framework=torch
```

The same queries are available in Python. `Artifact.get(name)` returns the latest version by default, `Artifact.listall()` iterates versions newest first with server-side filtering, and `Artifact.list_names()` lists distinct names with their version counts.

Artifacts are scoped to a project and domain. All of these calls accept `project` and `domain` arguments, and default to the ones in your config.
