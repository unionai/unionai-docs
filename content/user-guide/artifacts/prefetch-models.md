---
title: Prefetch Hugging Face models
description: Pull model weights from the Hugging Face Hub into your own storage as a model artifact, versioned by commit, with the model card attached.
icon: download
weight: 3
variants: -flyte +union
---

# Prefetch Hugging Face models

`flyte.prefetch.hf_model()` downloads a model from the Hugging Face Hub into your own object storage and registers the result as a model artifact. It is the third way an artifact is created, alongside [task outputs](./task-outputs) and [publishing your own](./publish-artifacts).

{{< tabs "prefetch" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
import flyte
import flyte.prefetch

flyte.init_from_config()

run = flyte.prefetch.hf_model(repo="HuggingFaceTB/SmolLM2-135M-Instruct")
run.wait()
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte prefetch hf-model HuggingFaceTB/SmolLM2-135M-Instruct --wait
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

For the full how-to, including sharding for multi-GPU inference, resources, tokens for gated repos, CLI usage, and serving the result from a vLLM or SGLang endpoint, see [Prefetching models](../inference/prefetching-models). This page covers what a prefetch means for the artifact registry.

## What gets registered

On success the platform records a model artifact for the stored weights:

* The artifact name defaults to the last segment of the repo id, with `.` replaced by `-`, or set it with `artifact_name`. The example above registers `SmolLM2-135M-Instruct`.
* The version is the Hugging Face commit ID.
* The searchable metadata carries the model facts (framework, architecture, task, modality, serialization format) plus the source repo and commit.
* The repo's README, if it has one, is attached as the model card.

The prefetch task is cached on its inputs (the repo, `artifact_name`, the model metadata, `shard_config` and `raw_data_path`), not on the upstream commit. Re-running a prefetch with the same inputs reuses the cached result and doesn't pick up a newer upstream commit, even if you change `resources` or `hf_token_key`. To download the repo's latest commit again, increment `force` (`--force 1`, `--force 2`, and so on, on the CLI). If the commit has moved, it registers as a new version you can [trigger on](../triggers/artifact-triggers).

## Finding a prefetched model

Retrieve it by name, or find it by where it came from. The source repo and commit are recorded as searchable metadata:

{{< tabs "find-prefetched" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyte.remote import Artifact

model = Artifact.get("SmolLM2-135M-Instruct")
models = Artifact.listall(attrs={"source_repo": "HuggingFaceTB/SmolLM2-135M-Instruct"})
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact SmolLM2-135M-Instruct
flyte get artifact --attr source_repo=HuggingFaceTB/SmolLM2-135M-Instruct
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Those `source_repo` and `source_commit` attributes are what make a prefetched model traceable back to its Hub repo and commit.

To load the weights yourself rather than passing them to a task, see [reading an artifact's value directly](./task-outputs#reading-an-artifacts-value-directly).

Once prefetched, mount the model into a serving app with an artifact parameter. See [Use artifacts in apps](./artifacts-in-apps).
