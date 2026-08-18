---
title: Prefetch Hugging Face models
weight: 3
variants: -flyte +union
---

# Prefetch Hugging Face models

Serving apps and training tasks should not download model weights from the Hugging Face Hub on every cold start. Prefetching downloads the weights once, stores them in your own object storage close to your compute, and registers the result as a model artifact.

`flyte.prefetch.hf_model()` launches a run that does the download and registration:

```python
import flyte

flyte.init_from_config()

run = flyte.prefetch.hf_model(
    repo="HuggingFaceTB/SmolLM2-135M-Instruct",
    hf_token_key=None,  # public repo, no token needed
    resources=flyte.Resources(cpu="2", memory="4Gi", disk="10Gi"),
)
run.wait()
```

For gated repos, `hf_token_key` names the secret that holds your Hugging Face token (default `HF_TOKEN`). It is the name of the secret, not the token itself.

## What gets registered

On success the platform records a model artifact for the stored weights:

* The artifact name defaults to the repo name, or set it with `artifact_name`.
* The version is the Hugging Face commit id, so prefetching the same commit again republishes the same version instead of creating a duplicate.
* The searchable metadata carries the model facts (framework, architecture, task, modality, serialization format) plus the source repo and commit.
* The repo's README is attached as the model card.

Retrieve it later with `flyte.remote.Artifact.get(artifact_name)`, or find it by source:

```bash
flyte get artifact --source-external-ref hf://HuggingFaceTB/SmolLM2-135M-Instruct
```

## Sharding large models

For models that will be served with tensor parallelism, pre-shard the weights during prefetch so the serving app skips that work too:

```python
from flyte.prefetch import ShardConfig, VLLMShardArgs

run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    shard_config=ShardConfig(engine="vllm", args=VLLMShardArgs(tensor_parallel_size=8)),
    hf_token_key="HF_TOKEN",
)
```

## From the CLI

```bash
flyte prefetch hf-model meta-llama/Llama-2-7b-hf --artifact-name llama2-7b --gpu A100:1 --wait
```

The CLI accepts the same options as the Python API, including `--cpu`, `--mem`, `--disk`, `--modality`, `--format`, and `--shard-config` with a YAML file.

Once prefetched, mount the model into a serving app with an artifact parameter. See [Use artifacts in apps](artifacts-in-apps).
