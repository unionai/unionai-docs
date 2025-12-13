---
title: SGLang app
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# SGLang app

SGLang is a fast structured generation library for large language models (LLMs). Flyte provides `SGLangAppEnvironment` for deploying SGLang model servers.

## Installation

First, install the SGLang plugin:

```bash
pip install --pre flyteplugins-sglang
```

## Basic SGLang app

Here's a simple example serving a HuggingFace model:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/sglang/basic_sglang.py" lang=python >}}

## Using prefetched models

You can use models prefetched with `flyte.prefetch`:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/sglang/sglang_with_prefetch.py" lang=python >}}

## Model streaming

SGLang supports streaming models directly from blob storage to GPU memory:

```python
sglang_app = SGLangAppEnvironment(
    name="streaming-sglang-app",
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="qwen3-0.6b",
    stream_model=True,  # Enable streaming
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1"),
    # ...
)
```

When `stream_model=True`:
- Model weights stream directly from storage to GPU
- Faster startup time (no full download required)
- Lower disk space requirements

## Custom SGLang arguments

Use `extra_args` to pass additional arguments to SGLang:

```python
sglang_app = SGLangAppEnvironment(
    name="custom-sglang-app",
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="qwen3-0.6b",
    extra_args=[
        "--max-model-len", "8192",  # Maximum context length
        "--mem-fraction-static", "0.8",  # Memory fraction for static allocation
        "--trust-remote-code",  # Trust remote code in models
    ],
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1"),
    # ...
)
```

See the [SGLang server arguments documentation](https://docs.sglang.ai/backend/server_arguments.html) for all available options.

## Using the OpenAI-compatible API

Once deployed, your SGLang app exposes an OpenAI-compatible API:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://your-app-url/v1",  # SGLang endpoint
    api_key="your-api-key",  # If requires_auth=True
)

response = client.chat.completions.create(
    model="qwen3-0.6b",  # Your model_id
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ],
)

print(response.choices[0].message.content)
```

## Multi-GPU inference (Tensor Parallelism)

For larger models, use multiple GPUs with tensor parallelism:

```python
sglang_app = SGLangAppEnvironment(
    name="multi-gpu-sglang-app",
    model_hf_path="meta-llama/Llama-2-70b-hf",
    model_id="llama-2-70b",
    resources=flyte.Resources(
        cpu="8",
        memory="32Gi",
        gpu="L40s:4",  # 4 GPUs for tensor parallelism
        disk="100Gi",
    ),
    extra_args=[
        "--tp", "4",  # Tensor parallelism size (4 GPUs)
        "--max-model-len", "4096",
        "--mem-fraction-static", "0.9",
    ],
    requires_auth=False,
)
```

The tensor parallelism size (`--tp`) should match the number of GPUs specified in resources.

## Model sharding with prefetch

You can prefetch and shard models for multi-GPU inference using SGLang's sharding:

```python
# Prefetch with sharding configuration
run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    accelerator="L40s:4",
    shard_config=flyte.prefetch.ShardConfig(
        engine="sglang",  # Use SGLang for sharding
        args=flyte.prefetch.SGLangShardArgs(
            tp=4,  # Tensor parallelism
            trust_remote_code=True,
        ),
    ),
)
run.wait()

# Use the sharded model
sglang_app = SGLangAppEnvironment(
    name="sharded-sglang-app",
    model_path=flyte.app.RunOutput(type="directory", run_name=run.name),
    model_id="llama-2-70b",
    resources=flyte.Resources(cpu="8", memory="32Gi", gpu="L40s:4", disk="100Gi"),
    extra_args=["--tp", "4"],
    stream_model=True,
)
```

See [Prefetching models](../serve-and-deploy-apps/prefetching-models) for more details on sharding.

## Autoscaling

SGLang apps work well with autoscaling:

```python
sglang_app = SGLangAppEnvironment(
    name="autoscaling-sglang-app",
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="qwen3-0.6b",
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1"),
    scaling=flyte.app.Scaling(
        replicas=(0, 1),  # Scale to zero when idle
        scaledown_after=600,  # 10 minutes idle before scaling down
    ),
    # ...
)
```

## Structured generation

SGLang is particularly well-suited for structured generation tasks. The deployed app supports standard OpenAI API calls, and you can use SGLang's advanced features through the API.

## Best practices

1. **Use prefetching**: Prefetch models for faster deployment and better reproducibility
2. **Enable streaming**: Use `stream_model=True` to reduce startup time and disk usage
3. **Right-size GPUs**: Match GPU memory to model size
4. **Use tensor parallelism**: For large models, use multiple GPUs with `--tp`
5. **Set autoscaling**: Use appropriate idle TTL to balance cost and performance
6. **Configure memory**: Use `--mem-fraction-static` to control memory allocation
7. **Limit context length**: Use `--max-model-len` for smaller models to reduce memory usage

## Troubleshooting

**Model loading fails:**
- Verify GPU memory is sufficient for the model
- Check that the model path or HuggingFace path is correct
- Review container logs for detailed error messages

**Out of memory errors:**
- Reduce `--max-model-len`
- Lower `--mem-fraction-static`
- Use a smaller model or more GPUs

**Slow startup:**
- Enable `stream_model=True` for faster loading
- Prefetch models before deployment
- Use faster storage backends

