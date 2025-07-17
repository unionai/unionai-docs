---
title: Cache a Huggingface Model as an Artifact
weight: 3
variants: -flyte +serverless +byoc +selfmanaged
---

# Cache a HuggingFace Model as an Artifact

The `union cache model-from-hf` command allows you to automatically download and cache models from HuggingFace Hub as Union Artifacts. This is particularly useful for serving large language models (LLMs) and other AI models efficiently in production environments.

## Why Cache Models from HuggingFace?

Caching models from HuggingFace Hub as Union Artifacts provides several key benefits:

- **Faster Model Loading**: Once cached, models load much faster since they're stored in Union's optimized blob storage
- **Reliability**: Eliminates dependency on HuggingFace Hub availability during model serving
- **Cost Efficiency**: Reduces repeated downloads and bandwidth costs
- **Version Control**: Each cached model gets a unique artifact ID for reproducible deployments
- **Sharding Support**: Large models can be automatically sharded for distributed inference
- **Streaming**: Models can be streamed directly from blob storage to GPU memory

## Prerequisites

Before using the `union cache model-from-hf` command, you need to set up authentication:

1. **Create a HuggingFace API Token**:
   - Go to [HuggingFace Settings](https://huggingface.co/settings/tokens)
   - Create a new token with read access
   - Store it as a Union secret:
   ```bash
   union create secret --name HUGGINGFACE_TOKEN
   ```

2. **Create a Union API Key** (for admin permissions):
   ```bash
   union create api-key admin --name EAGER_API_KEY
   union create secret --name EAGER_API_KEY
   ```

## Basic Example: Cache a Model As-Is

The simplest way to cache a model is to download it directly from HuggingFace without any modifications:

```bash
union cache model-from-hf Qwen/Qwen2.5-0.5B-Instruct \
    --hf-token-key HUGGINGFACE_TOKEN \
    --union-api-key EAGER_API_KEY \
    --artifact-name qwen2-5-0-5b-instruct \
    --cpu 2 \
    --mem 8Gi \
    --ephemeral-storage 10Gi \
    --wait
```

### Command Breakdown

- `Qwen/Qwen2.5-0.5B-Instruct`: The HuggingFace model repository
- `--hf-token-key HUGGINGFACE_TOKEN`: Union secret containing your HuggingFace API token
- `--union-api-key EAGER_API_KEY`: Union secret with admin permissions
- `--artifact-name qwen2-5-0-5b-instruct`: Custom name for the cached artifact
- `--cpu 2 --mem 8Gi`: Compute resources for downloading and caching
- `--ephemeral-storage 10Gi`: Temporary storage for the download process
- `--wait`: Wait for the caching process to complete

### Output

When the command completes, you'll see output like:

```
✅ Model cached successfully!
Cached model at: s3://union-serving-mvp-us-west-2-serving-mvp/model-loading-test/.cache/huggingface/hub/models--Qwen--Qwen2.5-0.5B-Instruct/snapshots/8123ea2e9354afb7ffcc6c8641d1b2f5ecf18301
Model Artifact ID: flyte://av0.2/dogfood-gcp/thomasjpfan/development/qwen2-5-0-5b-instruct@f4d7a98b650ce14367b5f6ba77e70144

To deploy this model run:
union deploy model --project dogfood-gcp --domain thomasjpfan/development flyte://av0.2/dogfood-gcp/thomasjpfan/development/qwen2-5-0-5b-instruct@f4d7a98b650ce14367b5f6ba77e70144
```

## Advanced Example: Sharding a Model with vLLM Engine

For large models that require distributed inference, you can use the `--shard-config` option to automatically shard the model using vLLM's tensor parallelism.

### Step 1: Create a Shard Configuration File

Create a YAML file (e.g., `shard_config.yaml`) with the sharding parameters:

```yaml
engine: vllm
args:
  model: unsloth/Llama-3.3-70B-Instruct
  tensor_parallel_size: 4
  gpu_memory_utilization: 0.9
  extra_args:
    max_model_len: 16384
```

### Step 2: Cache the Sharded Model

```bash
union cache model-from-hf unsloth/Llama-3.3-70B-Instruct \
    --hf-token-key HUGGINGFACE_TOKEN \
    --union-api-key EAGER_API_KEY \
    --artifact-name llama-3-3-70b-instruct-sharded \
    --cpu 36 \
    --gpu 4 \
    --mem 300Gi \
    --ephemeral-storage 300Gi \
    --accelerator nvidia-l40s \
    --shard-config shard_config.yaml \
    --project flytesnacks \
    --domain development \
    --wait
```

### Shard Configuration Options

The `VLLMShardArgs` class supports the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | str | Required | HuggingFace model identifier |
| `tensor_parallel_size` | int | Required | Number of GPUs for tensor parallelism |
| `trust_remote_code` | bool | False | Whether to trust remote code from HuggingFace |
| `revision` | str | None | Specific model revision/commit |
| `file_pattern` | str | None | Pattern for saved filenames |
| `max_file_size` | int | 5GB | Max size of each safetensors file |
| `gpu_memory_utilization` | float | 0.9 | GPU memory utilization ratio |
| `extra_args` | dict | {} | Additional vLLM engine arguments |

## Using Cached Models in Applications

Once you have cached a model, you can use it in your Union applications:

### VLLM App Example

```python
import os
from union import Artifact, Resources
from union.app.llm import VLLMApp
from flytekit.extras.accelerators import L4

# Use the cached model artifact
Model = Artifact(name="qwen2-5-0-5b-instruct")

vllm_app = VLLMApp(
    name="vllm-app-3",
    requests=Resources(cpu="12", mem="24Gi", gpu="1"),
    accelerator=L4,
    model=Model.query(),  # Query the cached artifact
    model_id="qwen2",
    scaledown_after=300,
    stream_model=True,
    port=8084,
)
```

### SGLang App Example

```python
import os
from union import Artifact, Resources
from union.app.llm import SGLangApp
from flytekit.extras.accelerators import L4

# Use the cached model artifact
Model = Artifact(name="qwen2-5-0-5b-instruct")

sglang_app = SGLangApp(
    name="sglang-app-3",
    requests=Resources(cpu="12", mem="24Gi", gpu="1"),
    accelerator=L4,
    model=Model.query(),  # Query the cached artifact
    model_id="qwen2",
    scaledown_after=300,
    stream_model=True,
    port=8000,
)
```

## Command Options Reference

The `union cache model-from-hf` command supports the following options:

### Required Arguments
- `repo`: HuggingFace repository identifier (e.g., `Qwen/Qwen2.5-0.5B-Instruct`)

### Optional Arguments

#### Artifact Configuration
- `--artifact-name`: Custom name for the cached artifact (alphanumeric, underscores, hyphens only)
- `--architecture`: Model architecture from HuggingFace config.json
- `--task`: Model task type (`generate`, `classify`, `embed`, `score`, or `auto`)
- `--modality`: Model modalities (`text`, `image`, `audio`, `video`) - can be specified multiple times
- `--format`: Model serialization format (`safetensors`, `onnx`, `torchscript`, `joblib`, etc.)
- `--model-type`: Model type (`transformer`, `xgboost`, `custom`, etc.)
- `--short-description`: Brief description of the model

#### Authentication
- `--hf-token-key`: Union secret key containing HuggingFace token (default: `HF_TOKEN`)
- `--union-api-key`: Union secret key with admin permissions (default: `UNION_API_KEY`)

#### Compute Resources
- `--cpu`: CPU resources for downloading and caching
- `--gpu`: GPU resources for downloading and caching
- `--mem`: Memory resources for downloading and caching
- `--ephemeral-storage`: Ephemeral storage for downloading and caching
- `--accelerator`: GPU accelerator type (e.g., `nvidia-l40s`, `nvidia-a100`, etc.)

#### Sharding Configuration
- `--shard-config`: Path to YAML file with sharding configuration

#### Execution Control
- `--force`: Force caching with retry number (1, 2, 3, etc.)
- `--wait`: Wait for caching to complete before returning

## Best Practices

1. **Resource Sizing**: Allocate sufficient resources for the model size:
   - Small models (< 1B): 2-4 CPU, 4-8Gi memory
   - Medium models (1-7B): 4-8 CPU, 8-16Gi memory
   - Large models (7B+): 8+ CPU, 16Gi+ memory

2. **Sharding for Large Models**: Use tensor parallelism for models > 7B parameters:
   - 7-13B models: 2-4 GPUs
   - 13-70B models: 4-8 GPUs
   - 70B+ models: 8+ GPUs

3. **Storage Considerations**: Ensure sufficient ephemeral storage for the download process

4. **Authentication**: Always use secrets for API tokens and never hardcode them

5. **Monitoring**: Use the `--wait` flag to monitor the caching process, or check the execution URL for progress

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Ensure your HuggingFace token has read access to the repository
2. **Insufficient Resources**: Increase CPU, memory, or ephemeral storage allocation
3. **Model Not Found**: Verify the repository name and ensure it's publicly accessible
4. **Sharding Failures**: Check that the shard configuration matches your available GPU resources

### Debugging

- Use the execution URL to monitor progress and view logs
- Check the Union console for detailed error messages
- Verify that all required secrets are properly configured

