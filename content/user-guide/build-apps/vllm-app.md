---
title: vLLM app
weight: 11
variants: +flyte +serverless +byoc +selfmanaged
---

# vLLM app

vLLM is a high-performance library for serving large language models (LLMs). Flyte provides `VLLMAppEnvironment` for deploying vLLM model servers.

## Installation

First, install the vLLM plugin:

```bash
pip install --pre flyteplugins-vllm
```

## Basic vLLM app

Here's a simple example serving a HuggingFace model:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/vllm/basic_vllm.py" lang=python >}}

## Using prefetched models

You can use models prefetched with `flyte.prefetch`:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/vllm/vllm_with_prefetch.py" lang=python >}}

## Model streaming

vLLM supports streaming models directly from blob storage to GPU memory, reducing startup time:

```python
vllm_app = VLLMAppEnvironment(
    name="streaming-llm-app",
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

## Custom vLLM arguments

Use `extra_args` to pass additional arguments to vLLM:

```python
vllm_app = VLLMAppEnvironment(
    name="custom-vllm-app",
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="qwen3-0.6b",
    extra_args=[
        "--max-model-len", "8192",  # Maximum context length
        "--gpu-memory-utilization", "0.8",  # GPU memory utilization
        "--trust-remote-code",  # Trust remote code in models
    ],
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1"),
    # ...
)
```

See the [vLLM documentation](https://docs.vllm.ai/en/stable/configuration/engine_args.html) for all available arguments.

## Using the OpenAI-compatible API

Once deployed, your vLLM app exposes an OpenAI-compatible API:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://your-app-url/v1",  # vLLM endpoint
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

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/vllm/vllm_multi_gpu.py" lang=python >}}

The `tensor-parallel-size` should match the number of GPUs specified in resources.

## Model sharding with prefetch

You can prefetch and shard models for multi-GPU inference:

```python
# Prefetch with sharding configuration
run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    accelerator="L40s:4",
    shard_config=flyte.prefetch.ShardConfig(
        engine="vllm",
        args=flyte.prefetch.VLLMShardArgs(
            tensor_parallel_size=4,
            dtype="auto",
            trust_remote_code=True,
        ),
    ),
)
run.wait()

# Use the sharded model
vllm_app = VLLMAppEnvironment(
    name="sharded-llm-app",
    model_path=flyte.app.RunOutput(type="directory", run_name=run.name),
    model_id="llama-2-70b",
    resources=flyte.Resources(cpu="8", memory="32Gi", gpu="L40s:4", disk="100Gi"),
    extra_args=["--tensor-parallel-size", "4"],
    stream_model=True,
)
```

See [Prefetching models](../serve-and-deploy-apps/prefetching-models) for more details on sharding.

## Autoscaling

vLLM apps work well with autoscaling:

```python
vllm_app = VLLMAppEnvironment(
    name="autoscaling-llm-app",
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

## Best practices

1. **Use prefetching**: Prefetch models for faster deployment and better reproducibility
2. **Enable streaming**: Use `stream_model=True` to reduce startup time and disk usage
3. **Right-size GPUs**: Match GPU memory to model size
4. **Configure memory utilization**: Use `--gpu-memory-utilization` to control memory usage
5. **Use tensor parallelism**: For large models, use multiple GPUs with `tensor-parallel-size`
6. **Set autoscaling**: Use appropriate idle TTL to balance cost and performance
7. **Limit context length**: Use `--max-model-len` for smaller models to reduce memory usage

## Troubleshooting

**Model loading fails:**
- Verify GPU memory is sufficient for the model
- Check that the model path or HuggingFace path is correct
- Review container logs for detailed error messages

**Out of memory errors:**
- Reduce `--max-model-len`
- Lower `--gpu-memory-utilization`
- Use a smaller model or more GPUs

**Slow startup:**
- Enable `stream_model=True` for faster loading
- Prefetch models before deployment
- Use faster storage backends

