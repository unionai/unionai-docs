---
title: Prefetching models
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Prefetching models

Prefetching allows you to download and prepare HuggingFace models (including sharding for multi-GPU inference) before
deploying [vLLM](../build-apps/vllm-app) or [SGLang](../build-apps/sglang-app) apps. This speeds up deployment and ensures models are ready when your app starts.

## Why prefetch?

Prefetching models provides several benefits:

- **Faster deployment**: Models are pre-downloaded, so apps start faster
- **Reproducibility**: Models are versioned and stored in Flyte's object store
- **Sharding support**: Pre-shard models for multi-GPU tensor parallelism
- **Cost efficiency**: Download once, use many times
- **Offline support**: Models are cached in your storage backend

## Basic prefetch

### Using Python SDK

```python
import flyte

# Prefetch a HuggingFace model
run = flyte.prefetch.hf_model(repo="Qwen/Qwen3-0.6B")

# Wait for prefetch to complete
run.wait()

# Get the model path
model_path = run.outputs()[0].path
print(f"Model prefetched to: {model_path}")
```

### Using CLI

```bash
flyte prefetch hf-model Qwen/Qwen3-0.6B
```

Wait for completion:

```bash
flyte prefetch hf-model Qwen/Qwen3-0.6B --wait
```

## Using prefetched models

Use the prefetched model in your vLLM or SGLang app:

```python
from flyteplugins.vllm import VLLMAppEnvironment
import flyte

# Prefetch the model
run = flyte.prefetch.hf_model(repo="Qwen/Qwen3-0.6B")
run.wait()

# Use the prefetched model
vllm_app = VLLMAppEnvironment(
    name="my-llm-app",
    model_path=flyte.app.RunOutput(
        type="directory",
        run_name=run.name,
    ),
    model_id="qwen3-0.6b",
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1"),
    stream_model=True,
)

app = flyte.serve(vllm_app)
```

## Prefetch options

### Custom artifact name

```python
run = flyte.prefetch.hf_model(
    repo="Qwen/Qwen3-0.6B",
    artifact_name="qwen-0.6b-model",  # Custom name for the stored model
)
```

### With HuggingFace token

If the model requires authentication:

```python
run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-7b-hf",
    hf_token_key="HF_TOKEN",  # Name of Flyte secret containing HF token
)
```

The default value for `hf_token_key` is `HF_TOKEN`, where `HF_TOKEN` is the name of the Flyte secret containing your
HuggingFace token. If this secret doesn't exist, you can create a secret using the [flyte create secret CLI](../task-configuration/secrets).

### With resources

By default, the prefetch task uses minimal resources (2 CPUs, 8GB of memory, 50Gi of disk storage), using
filestreaming logic to move the model weights from HuggingFace to your storage backend directly.

In some cases, the HuggingFace model may not support filestreaming, in which case the prefetch task will fallback to
downloading the model weights to the task pod's disk storage first, then uploading them to your storage backend. In this
case, you can specify custom resources for the prefetch task to override the default resources.

```python
run = flyte.prefetch.hf_model(
    repo="Qwen/Qwen3-0.6B",
    cpu="4",
    mem="16Gi",
    ephemeral_storage="100Gi",
)
```

## Sharding models for multi-GPU

### vLLM sharding

Shard a model for tensor parallelism:

```python
from flyte.prefetch import ShardConfig, VLLMShardArgs

run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    resources=flyte.Resources(cpu="8", memory="32Gi", gpu="L40s:4"),
    shard_config=ShardConfig(
        engine="vllm",
        args=VLLMShardArgs(
            tensor_parallel_size=4,
            dtype="auto",
            trust_remote_code=True,
        ),
    ),
    hf_token_key="HF_TOKEN",
)

run.wait()
```

Currently, the `flyte.prefetch.hf_model` function only supports sharding models
using the `vllm` engine. Once sharded, these models can be loaded with other
frameworks such as `transformers`, `torch`, or `sglang`.

### Using shard config via CLI

You can also use a YAML file for sharding configuration to use with the
`flyte prefetch hf-model` CLI command:

```yaml
# shard_config.yaml
engine: vllm
args:
  tensor_parallel_size: 8
  dtype: auto
  trust_remote_code: true
```

Then run the CLI command:

```bash
flyte prefetch hf-model meta-llama/Llama-2-70b-hf \
    --shard-config shard_config.yaml \
    --accelerator L40s:8 \
    --hf-token-key HF_TOKEN
```

## Using prefetched sharded models

After prefetching and sharding, serve the model in your app:

```python
# Use in vLLM app
vllm_app = VLLMAppEnvironment(
    name="multi-gpu-llm-app",
    # this will download the model from HuggingFace into the app container's filesystem
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="llama-2-70b",
    resources=flyte.Resources(
        cpu="8",
        memory="32Gi",
        gpu="L40s:4",  # Match the number of GPUs used for sharding
    ),
    extra_args=[
        "--tensor-parallel-size", "4",  # Match sharding config
    ],
)

if __name__ == "__main__":
    # Prefetch with sharding
    run = flyte.prefetch.hf_model(
        repo="meta-llama/Llama-2-70b-hf",
        accelerator="L40s:4",
        shard_config=ShardConfig(
            engine="vllm",
            args=VLLMShardArgs(tensor_parallel_size=4),
        ),
    )
    run.wait()

    flyte.serve(
        vllm_app.clone_with(
            name=vllm_app.name,
            # override the model path to use the prefetched model
            model_path=flyte.app.RunOutput(type="directory", run_name=run.name),
            # set the hf_model_path to None
            hf_model_path=None,
            # stream the model from flyte object store directly to the GPU
            stream_model=True,
        )
    )

```

## CLI options

Complete CLI usage:

```bash
flyte prefetch hf-model <repo> \
    --artifact-name <name> \
    --architecture <arch> \
    --task <task> \
    --modality text \
    --format safetensors \
    --model-type transformer \
    --short-description "Description" \
    --force 0 \
    --wait \
    --hf-token-key HF_TOKEN \
    --cpu 4 \
    --mem 16Gi \
    --ephemeral-storage 100Gi \
    --accelerator L40s:4 \
    --shard-config shard_config.yaml
```

## Complete example

Here's a complete example of prefetching and using a model:

```python
import flyte
from flyteplugins.vllm import VLLMAppEnvironment
from flyte.prefetch import ShardConfig, VLLMShardArgs


# define the app environment
vllm_app = VLLMAppEnvironment(
    name="qwen-serving-app",
    # this will download the model from HuggingFace into the app container's filesystem
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="qwen3-0.6b",
    resources=flyte.Resources(
        cpu="4",
        memory="16Gi",
        gpu="L40s:1",
        disk="10Gi",
    ),
    scaling=flyte.app.Scaling(
        replicas=(0, 1),
        scaledown_after=600,
    ),
    requires_auth=False,
)

if __name__ == "__main__":
    # prefetch the model
    print("Prefetching model...")
    run = flyte.prefetch.hf_model(
        repo="Qwen/Qwen3-0.6B",
        artifact_name="qwen-0.6b",
        cpu="4",
        mem="16Gi",
        ephemeral_storage="50Gi",
    )

    # wait for completion
    print("Waiting for prefetch to complete...")
    run.wait()
    print(f"Model prefetched: {run.outputs()[0].path}")

    # deploy the app
    print("Deploying app...")
    flyte.init_from_config()
    app = flyte.serve(
        vllm_app.clone_with(
            name=vllm_app.name,
            model_path=flyte.app.RunOutput(type="directory", run_name=run.name),
            hf_model_path=None,
            stream_model=True,
        )
    )
    print(f"App deployed: {app.url}")
```

## Best practices

1. **Prefetch before deployment**: Prefetch models before deploying apps for faster startup
2. **Version models**: Use meaningful artifact names to easily identify the model in object store paths
3. **Shard appropriately**: Shard models for the GPU configuration you'll use for inference
4. **Cache prefetched models**: Once prefetched, models are cached in your storage backend for faster serving

## Troubleshooting

**Prefetch fails:**
- Check HuggingFace token (if required)
- Verify model repo exists and is accessible
- Check resource availability
- Review prefetch task logs

**Sharding fails:**
- Ensure accelerator matches shard config
- Check GPU memory is sufficient
- Verify `tensor_parallel_size` matches GPU count
- Review prefetch task logs for sharding-related errors

**Model not found in app:**
- Verify RunOutput references correct run name
- Check that prefetch completed successfully
- Ensure model_path is set correctly
- Review app startup logs

