---
title: Prefetching models
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Prefetching models

Prefetching allows you to download and prepare HuggingFace models (including sharding for multi-GPU inference) before deploying vLLM or SGLang apps. This speeds up deployment and ensures models are ready when your app starts.

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

Make sure you have a Flyte secret named `HF_TOKEN` containing your HuggingFace token.

### With resources

Specify resources for the prefetch task:

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
    accelerator="L40s:4",  # Use 4 GPUs
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

### SGLang sharding

Shard a model for SGLang:

```python
from flyte.prefetch import ShardConfig, SGLangShardArgs

run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    accelerator="L40s:4",
    shard_config=ShardConfig(
        engine="sglang",
        args=SGLangShardArgs(
            tp=4,  # Tensor parallelism size
            trust_remote_code=True,
        ),
    ),
    hf_token_key="HF_TOKEN",
)

run.wait()
```

### Using shard config file

You can also use a YAML file for sharding configuration:

```yaml
# shard_config.yaml
engine: vllm
args:
  tensor_parallel_size: 8
  dtype: auto
  trust_remote_code: true
```

Then use it:

```python
from pathlib import Path

run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    accelerator="L40s:8",
    shard_config=Path("shard_config.yaml"),
    hf_token_key="HF_TOKEN",
)
```

Or with CLI:

```bash
flyte prefetch hf-model meta-llama/Llama-2-70b-hf \
    --shard-config shard_config.yaml \
    --accelerator L40s:8 \
    --hf-token-key HF_TOKEN
```

## Using prefetched sharded models

After prefetching and sharding, use the model in your app:

```python
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

# Use in vLLM app
vllm_app = VLLMAppEnvironment(
    name="multi-gpu-llm-app",
    model_path=flyte.app.RunOutput(
        type="directory",
        run_name=run.name,
    ),
    model_id="llama-2-70b",
    resources=flyte.Resources(
        cpu="8",
        memory="32Gi",
        gpu="L40s:4",  # Match the number of GPUs used for sharding
    ),
    extra_args=[
        "--tensor-parallel-size", "4",  # Match sharding config
    ],
    stream_model=True,
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

# Step 1: Prefetch the model
print("Prefetching model...")
run = flyte.prefetch.hf_model(
    repo="Qwen/Qwen3-0.6B",
    artifact_name="qwen-0.6b",
    cpu="4",
    mem="16Gi",
    ephemeral_storage="50Gi",
)

# Wait for completion
print("Waiting for prefetch to complete...")
run.wait()
print(f"Model prefetched: {run.outputs()[0].path}")

# Step 2: Use the prefetched model in vLLM app
vllm_app = VLLMAppEnvironment(
    name="qwen-serving-app",
    model_path=flyte.app.RunOutput(
        type="directory",
        run_name=run.name,
    ),
    model_id="qwen3-0.6b",
    resources=flyte.Resources(
        cpu="4",
        memory="16Gi",
        gpu="L40s:1",
        disk="10Gi",
    ),
    stream_model=True,
    scaling=flyte.app.Scaling(
        replicas=(0, 1),
        scaledown_after=600,
    ),
    requires_auth=False,
)

# Step 3: Deploy the app
print("Deploying app...")
flyte.init_from_config()
app = flyte.serve(vllm_app)
print(f"App deployed: {app.url}")
```

## Best practices

1. **Prefetch before deployment**: Prefetch models before deploying apps for faster startup
2. **Version models**: Use meaningful artifact names to track model versions
3. **Shard appropriately**: Shard models for the GPU configuration you'll use
4. **Use secrets**: Store HuggingFace tokens in Flyte secrets
5. **Monitor prefetch**: Check prefetch status and logs
6. **Reuse prefetched models**: Once prefetched, reuse the same model path for multiple apps

## Troubleshooting

**Prefetch fails:**
- Check HuggingFace token (if required)
- Verify model repo exists and is accessible
- Check resource availability
- Review prefetch task logs

**Sharding fails:**
- Ensure accelerator matches shard config
- Check GPU memory is sufficient
- Verify tensor_parallel_size matches GPU count
- Review sharding logs for errors

**Model not found in app:**
- Verify RunOutput references correct run name
- Check that prefetch completed successfully
- Ensure model_path is set correctly
- Review app startup logs

