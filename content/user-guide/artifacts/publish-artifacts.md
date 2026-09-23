---
title: Publish your own artifacts
description: Upload existing datasets and model weights from anywhere with `Artifact.create` or `flyte create artifact`, recording where they came from.
icon: cloud-upload
weight: 2
variants: -flyte +union
---

# Publish your own artifacts

Not every dataset or model is produced by a task. You can publish an existing asset as an artifact from anywhere: a laptop, a notebook, a CI job, or an external pipeline. This is how you bootstrap a registry from assets you already have.

## Publish an artifact

{{< tabs "publish-artifact" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

`flyte.remote.Artifact.create()` uploads the value and registers a version in one call:

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

The call is synchronous by default; use `Artifact.create.aio(...)` from async code.

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

`flyte create artifact` publishes a file directly:

```bash
flyte create artifact incoming_dataset --from-file data/2026-08-18.csv \
    --external-ref s3://partner-bucket/drop/2026-08-18.csv
flyte create artifact my-model --from-file model.pt --kind model --attr framework=torch
flyte create artifact my-model --from-file model.pt --card model_card.html --card-type model
```

`--attr` is repeatable, `--kind` is one of `model`, `data`, or `generic`, and the card format is inferred from the file extension.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

If you do not pass a version, one is generated for you. Set attrs, kind, and a card the same way as in task-produced [metadata](./task-outputs#metadata).

The external ref records where the data came from. When `Artifact.create()` runs inside a task, the producing run is stamped on the artifact automatically; outside a task, the external ref is the provenance you can attach.

## Finding artifacts

{{< tabs "find-artifacts" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyte.remote import Artifact

Artifact.list_names()                                   # all artifact names, with latest version info
Artifact.listall("my-model")                            # every version of my-model, newest first
Artifact.get("my-model", version="1.0")                 # one version
Artifact.list_names(search="model")                     # names containing "model"
Artifact.listall(source_run="my_run")                   # versions produced by a run
Artifact.listall(kind="model", attrs={"framework": "torch"})
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact                        # all artifact names, with latest version info
flyte get artifact my-model               # every version of my-model, newest first
flyte get artifact my-model 1.0           # details of one version
flyte get artifact --search model         # names containing "model"
flyte get artifact --source-run my_run    # versions produced by a run
flyte get artifact --kind model --attr framework=torch
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`Artifact.get(name)` returns the latest version by default, and `listall` and `list_names` return iterators. For partitions, ranges, and more filters, see [Find and retrieve artifacts](./retrieving-artifacts).

Artifacts are scoped to a project and domain. All of these calls accept `project` and `domain` arguments, and default to the ones in your config.
