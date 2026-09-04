---
title: Task outputs as artifacts
description: Wrap a task's return value with `flyte.artifacts.new()` to register it as a named, versioned artifact with metadata and a model or data card.
icon: box-seam
weight: 1
variants: -flyte +union
---

# Task outputs as artifacts

The most common way to create an artifact is to register a task output. Two things are required: the task must be declared with `produces_artifacts=True`, and the return value must be wrapped with `flyte.artifacts.new()`.

```python
import flyte
from flyte import artifacts
from flyte.io import File

env = flyte.TaskEnvironment(name="training")


@env.task(produces_artifacts=True)
async def train() -> File:
    weights = await File.from_local("model.pt")
    return artifacts.new(
        weights,
        artifacts.Metadata(
            name="trained-model",
            description="Classifier trained on the latest training set",
            attrs={"framework": "pytorch"},
        ),
    )
```

Every run of this task registers a new version of `trained-model`. Union records the producing run on the artifact, so you can always trace a version back to the execution that created it.

> [!WARNING] Both parts are required
> The wrapper is stripped from the output value either way. Without `produces_artifacts=True` the platform never extracts the metadata, so no artifact is registered, no trigger fires, and there is nothing for an app to bind to. Nothing warns you.

## What can be an artifact

An artifact must be an offloaded value: a `flyte.io.File`, a `flyte.io.Dir`, or a `flyte.io.DataFrame`. Primitives, dataclasses, and Pydantic models cannot be artifacts. Wrap a raw dataframe with `DataFrame.from_df()` first.

The wrapped value must also be a top-level task output. Nesting an artifact inside a list, a dictionary, or a model raises an error. In a multi-output task, only the wrapped slot becomes an artifact:

```python
@env.task(produces_artifacts=True)
async def train() -> tuple[File, float]:
    ...
    return artifacts.new(weights, metadata), accuracy
```

## Metadata

`flyte.artifacts.Metadata` carries the identity of the artifact. Only `name` is required. If you leave out `version`, the version comes from the producing run, so every execution registers a distinct version. You can also set a `description`, string-valued `attrs` for searching and filtering, a `kind` (`"model"`, `"data"`, or `"generic"`), and a card.

For models there is a helper that fills in the standard fields and records the artifact's kind as `model`:

```python
card = artifacts.Card.create_from(content=card_html, format="html", card_type="model")

metadata = artifacts.Metadata.create_model_metadata(
    name="trained-model",
    description="A toy classifier",
    framework="PyTorch",
    architecture="ResNet50",
    task="Image Classification",
    serial_format="pt",
    card=card,
)
```

A card is a document attached to the artifact and rendered in the UI. `flyte.artifacts.Card.create_from()` accepts inline content or a local file, in formats including HTML, Markdown, JSON, YAML, CSV, and PNG.

## Consuming artifacts in tasks

Downstream tasks take artifacts as ordinary typed inputs. Fetch a reference with `flyte.remote.Artifact.get()` and pass it to `flyte.run()`:

```python
from flyte.remote import Artifact

model = Artifact.get("trained-model")               # latest version
data = Artifact.get("training-set", version="v3")   # pinned version

run = flyte.run(evaluate, model=model, data=data)
```

The task body receives a plain `File`, `Dir`, or `DataFrame` and needs no artifact-specific code.

## Reading an artifact's value directly

Outside a task — in a notebook or a local script — materialize the value with `to_python()`, passing the type the artifact holds:

```python
import asyncio

from flyte.io import Dir
from flyte.remote import Artifact


async def load() -> str:
    artifact = Artifact.get("trained-model")
    weights = await artifact.to_python(Dir)  # File or DataFrame for other artifacts
    return await weights.download()


local = asyncio.run(load())
```

In a notebook, `await` the two calls directly instead of wrapping them in `asyncio.run()`.

The download runs wherever you call it, so that environment needs credentials for the object store. This is a plain fetch and records no [lineage](./lineage) edge.
