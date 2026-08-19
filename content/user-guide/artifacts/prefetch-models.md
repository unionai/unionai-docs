---
title: Prefetch Hugging Face models
weight: 3
variants: -flyte +union
---

# Prefetch Hugging Face models

`flyte.prefetch.hf_model()` downloads a model from the Hugging Face Hub into your own object storage and registers the result as a model artifact. It is the third way an artifact is created, alongside [task outputs](./task-outputs) and [publishing your own](./publish-artifacts).

```python
import flyte
import flyte.prefetch

flyte.init_from_config()

run = flyte.prefetch.hf_model(repo="HuggingFaceTB/SmolLM2-135M-Instruct")
run.wait()
```

For the full how-to, including sharding for multi-GPU inference, resources, tokens for gated repos, CLI usage, and serving the result from a vLLM or SGLang app, see [Prefetching models](../apps/serve-and-deploy-apps/prefetching-models). This page covers what a prefetch means for the artifact registry.

## What gets registered

On success the platform records a model artifact for the stored weights:

* The artifact name defaults to the last segment of the repo id, with `.` replaced by `-`, or set it with `artifact_name`. The example above registers `SmolLM2-135M-Instruct`.
* The version is the Hugging Face commit id.
* The searchable metadata carries the model facts (framework, architecture, task, modality, serialization format) plus the source repo and commit.
* The repo's README, if it has one, is attached as the model card.

Because the version is the upstream commit, a prefetch is idempotent. Re-running it for a model that has not moved republishes the same version instead of filling the registry with duplicates, and a genuine upstream change arrives as a new version you can [trigger on](./artifact-triggers).

## Finding a prefetched model

Retrieve it by name:

```python
from flyte.remote import Artifact

model = Artifact.get("SmolLM2-135M-Instruct")
```

Or find it by where it came from. The `hf://` source reference is recorded automatically:

```bash
flyte get artifact --source-external-ref hf://HuggingFaceTB/SmolLM2-135M-Instruct
```

That same reference is what makes a prefetched model traceable back to its Hub repo and commit in the [lineage view](./lineage).

Once prefetched, mount the model into a serving app with an artifact parameter. See [Use artifacts in apps](./artifacts-in-apps).
