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

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=basic-prefetch lang=python >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=using-prefetched-models lang=python >}}

> [!TIP]
> You can also use prefetched models as parameters to your generic `[[AppEnvironment]]`s or `FastAPIAppEnvironment`s.

## Prefetch options

### Custom artifact name

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=custom-artifact-name lang=python >}}

### With HuggingFace token

If the model requires authentication:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=hf-token lang=python >}}

The default value for `hf_token_key` is `HF_TOKEN`, where `HF_TOKEN` is the name of the Flyte secret containing your
HuggingFace token. If this secret doesn't exist, you can create a secret using the [flyte create secret CLI](../task-configuration/secrets).

### With resources

By default, the prefetch task uses minimal resources (2 CPUs, 8GB of memory, 50Gi of disk storage), using
filestreaming logic to move the model weights from HuggingFace to your storage backend directly.

In some cases, the HuggingFace model may not support filestreaming, in which case the prefetch task will fallback to
downloading the model weights to the task pod's disk storage first, then uploading them to your storage backend. In this
case, you can specify custom resources for the prefetch task to override the default resources.

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=with-resources lang=python >}}

## Sharding models for multi-GPU

### vLLM sharding

Shard a model for tensor parallelism:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=vllm-sharding lang=python >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=using-sharded-models lang=python >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/prefetch_examples.py" fragment=complete-example lang=python >}}

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

