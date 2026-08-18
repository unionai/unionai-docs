---
title: Use artifacts in apps
weight: 5
variants: -flyte +union
---

# Use artifacts in apps

A serving app usually needs model weights or reference data on disk before it starts. Instead of baking them into the image or downloading them in startup code, declare an artifact as an app parameter and Union mounts it for you.

`flyte.app.ArtifactValue` names the artifact, and the parameter's `mount` says where its contents appear in the container:

```python
import flyte
import flyte.app

env = flyte.AppEnvironment(
    name="classifier-api",
    resources=flyte.Resources(cpu="2", memory="8Gi"),
    parameters=[
        flyte.app.Parameter(
            name="model",
            value=flyte.app.ArtifactValue(name="trained-model", type="directory"),
            mount="/tmp/model",
        )
    ],
)
```

The app code reads `/tmp/model` like any local directory. Only `flyte.io.File` and `flyte.io.Dir` artifacts can be app parameters; set `type` to `"file"` or `"directory"` to match.

The prebuilt serving environments accept an `ArtifactValue` directly. For example, the vLLM and SGLang app environments take one as `model_path`, which pairs naturally with [prefetched Hugging Face models](./prefetch-models).

## Versions are pinned at deploy time

The artifact is resolved when the app is deployed. If you leave out `version`, the latest version at deploy time is chosen and pinned, so a new version published later does not swap weights under a running app. Redeploy to move to the newer version, or pass an explicit `version=` to stay on a known one.

Union records exactly which artifact version each app deployment resolved, so the artifact's [lineage view](./lineage) shows every app serving it.

## Apps can publish artifacts too

An app endpoint can call `flyte.remote.Artifact.create()` to register a new version from inside the app, for example to snapshot state it has built up. That version behaves like any other: it shows up in the registry and can fire [artifact triggers](./artifact-triggers).
