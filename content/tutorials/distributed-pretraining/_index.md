---
title: Distributed LLM pretraining
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Distributed LLM pretraining

When training large models, infrastructure should not be the hardest part. The real work is in the model architecture, the data, and the hyperparameters. In practice, though, teams often spend weeks just trying to get distributed training to run reliably.

And when it breaks, it usually breaks in familiar ways: out-of-memory crashes, corrupted checkpoints, data loaders that silently fail, or runs that hang with no obvious explanation.

Most distributed training tutorials focus on PyTorch primitives. This one focuses on getting something that actually ships. We go into the technical details, such as how FSDP shards parameters, why gradient clipping behaves differently at scale, and how streaming datasets reduce memory pressure, but always with the goal of building a system that works in production.

Real training jobs need more than a training loop. They need checkpointing, fault tolerance, data streaming, visibility into what’s happening, and the ability to recover from failures. In this tutorial, we build all of that using Flyte, without having to stand up or manage any additional infrastructure.

> [!NOTE]
> Full code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/pretraining/train.py).

## Overview

We're going to pretrain a GPT-2 style language model from scratch. This involves training on raw text data starting from randomly initialized weights, rather than fine-tuning or adapting a pretrained model. This is the same process used to train the original GPT-2, LLaMA, and most other foundation models.

The model learns by predicting the next token. Given "The cat sat on the", it learns to predict "mat". Do this billions of times across terabytes of text, and the model develops surprisingly sophisticated language understanding. That's pretraining.

The challenge is scale. A 30B parameter model doesn't fit on a single GPU. The training dataset, [SlimPajama](https://huggingface.co/datasets/cerebras/SlimPajama-627B) in our case, is 627 billion tokens. Training runs last for days or even weeks. To make this work, you need:

- **Distributed training**: Split the model across multiple GPUs using [FSDP (Fully Sharded Data Parallel)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)
- **Data streaming**: Pull training data on-demand instead of downloading terabytes upfront
- **Checkpointing**: Save progress regularly so a failure doesn’t wipe out days of compute
- **Observability**: See what's happening inside a multi-day training run

We’ll build a Flyte pipeline that takes care of all of this, using three tasks with clearly defined responsibilities:

1. **Data preparation**: Tokenizes your dataset and converts it to MDS (MosaicML Data Shard) format for streaming. This Flyte task is cached, so it only needs to be run once and can be reused across runs.
2. **Distributed training**: Runs FSDP across 8 H200 GPUs. Flyte's `Elastic` plugin handles the distributed setup. Checkpoints upload to S3 automatically via Flyte's `File` abstraction.
3. **Real-time reporting**: Streams loss curves and training metrics to Flyte Reports, a live dashboard integrated into the Flyte UI.

Why three separate tasks? Flyte makes this separation efficient:

- **Caching**: The data preparation step runs once. On subsequent runs, Flyte skips it entirely.
- **Resource isolation**: Training uses expensive H200 GPUs only while actively training, while the driver runs on inexpensive CPU instances.
- **Fault boundaries**: If training fails, the data preparation step does not re-run. Training can resume directly from the most recent checkpoint.

## Implementation

Let's walk through the code. We'll start with the infrastructure setup, build the model, then wire everything together into a pipeline.

### Setting up the environment

Every distributed training job needs a consistent environment across all nodes. Flyte handles this with container images:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="imports" lang="python" >}}

The imports tell the story: `flyte` for orchestration, `flyte.report` for live dashboards, `lightning` for training loop management, and `Elastic` from Flyte's PyTorch plugin. This last one is key as it configures PyTorch's distributed launch without you writing any distributed setup code.

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="constants" lang="python" >}}

These constants define the distributed topology. We're using 1 node with 8 GPUs, but you can scale this up by changing `NUM_NODES`. The vocabulary size (50,257 tokens) and sequence length (2,048 tokens) match GPT-2's [Byte Pair Encoding (BPE) tokenizer](https://huggingface.co/learn/llm-course/en/chapter6/5).

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="image" lang="python" >}}

Flyte builds this container automatically when the pipeline is run. All dependencies required for distributed training, including PyTorch, Lightning, the streaming library, and NCCL for GPU communication, are baked in. There's no Dockerfile to maintain and no "works on my machine" debugging.

### Declaring resource requirements

Different parts of the pipeline need different resources. Data tokenization needs CPU and memory. Training needs GPUs. The driver just coordinates. Flyte's `TaskEnvironment` lets you declare exactly what each task needs:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="task-envs" lang="python" >}}

Let's break down the training environment, since this is where most of the complexity lives:

- **`gpu=f"H200:{DEVICES_PER_NODE}"`**: Flyte provisions exactly 8 H200 GPUs. These have 141GB of memory each, enough to train 30B+ parameter models with FSDP.
- **`shm="16Gi"`**: This allocates explicit shared memory. NCCL (NVIDIA's communication library) uses shared memory for inter-GPU communication on the same node. Without this, you'll see cryptic errors like "NCCL error: unhandled system error", which can be difficult to debug.
- **`Elastic(nnodes=NUM_NODES, nproc_per_node=DEVICES_PER_NODE)`**: This is Flyte's integration with PyTorch's elastic launch. It handles process spawning (one process per GPU), rank assignment (each process knows its ID), and environment setup (master address, world size). This replaces the boilerplate typically written in shell scripts.

The `driver_env` is intentionally lightweight, using 2 CPUs and 4 GB of memory. Its role is limited to orchestrating tasks and passing data between them, so allocating GPUs here would be unnecessary.

### Model configurations

Training a 1.5B model uses different hyperparameters than training a 65B model. Rather than hardcoding values, we define presets:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="model-configs" lang="python" >}}

A few things to notice:

- **Batch size decreases with model size**: For a fixed GPU memory budget, larger models consume more memory for parameters, optimizer state, and activations, leaving less room for per-GPU batch size. For example, a 1.5B parameter model may fit a batch size of 8 per GPU, while a 65B model may only fit a batch size of 1. This is typically compensated for using gradient accumulation to maintain a larger effective batch size.
- **Learning rate decreases with model size**: Larger models are more sensitive to optimization instability and typically require lower learning rates. The values here follow empirical best practices used in large-scale language model training, informed by work such as the [Chinchilla study](https://arxiv.org/pdf/2203.15556) on compute-optimal scaling.
- **Checkpoint frequency increases with model size**: Checkpointing a 65B model is expensive (the checkpoint is huge). We do it less often but make sure we don't lose too much progress if something fails.

The 1.5B config is good for testing your setup before committing to a serious training run.

### Building the GPT model

Now for the model itself. We're building a GPT-2 style decoder-only transformer from scratch.

First, the configuration class:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="gpt-config" lang="python" >}}

The key architectural parameters:

- **`n_embd`**: The hidden (embedding) dimension. Larger values increase model capacity but also increase memory and compute requirements.
- **`n_layer`**: The number of transformer blocks. Model depth strongly influences expressiveness and performance.
- **`n_head`**: The number of attention heads. Each head can attend to different patterns or relationships in the input.
- **`n_inner`**: The hidden dimension of the feed-forward network (MLP), typically set to 4x the embedding dimension.

Next, we define a single transformer block:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="gpt-block" lang="python" >}}

Each block has two sub-layers: causal self-attention and a feed-forward MLP. The causal mask ensures the model can only attend to previous tokens in the sequence, so it can't "cheat" by looking at the answer. This is what makes it *autoregressive*.

The full `GPTModel` class (see the complete code) stacks these blocks and adds token and positional embeddings. One important detail is that the input token embedding matrix is shared with the output projection layer (often called [weight tying](https://mbrenndoerfer.com/writing/weight-tying-shared-embeddings-transformers)). This reduces the number of parameters by roughly 50 million for typical vocabulary sizes and often leads to better generalization and more stable training.

### The Lightning training module

PyTorch Lightning handles the training loop boilerplate. We wrap our model in a `LightningModule` that defines how to train it:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="lightning-module-init" lang="python" >}}

The `save_hyperparameters()` call is important because it stores all constructor arguments in the checkpoint. This allows the model to be reloaded later without having to manually reconstruct the original configuration.

The training and validation steps implement standard causal language modeling, where the model is trained to predict the next token given all previous tokens in the sequence.

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="lightning-module-training" lang="python" >}}

The model performs a forward pass with a causal (autoregressive) mask created internally, ensuring each token can only attend to earlier positions. To align predictions with targets, the logits and labels are shifted so that the representation at position `i` is used to predict token `i + 1`.

Loss is computed using cross-entropy over the shifted logits and labels. Training loss and perplexity are logged during execution, with metrics synchronized across distributed workers.

The optimizer setup is where a lot of training stability comes from:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="lightning-module-optimizer" lang="python" >}}

Two important choices here:

1. **Separate weight decay groups**: We only apply weight decay to the weight matrices, not to biases or LayerNorm parameters. This follows the original BERT paper and is now standard practice, as regularizing biases and normalization parameters does not improve performance and can be harmful.
2. **Cosine learning rate schedule with warmup**: We start with a low learning rate, ramp up linearly during warmup (helps stabilize early training when gradients are noisy), then decay following a cosine curve. This schedule outperforms constant or step decay for transformer training.

### Checkpointing for fault tolerance

Training a 30B-parameter model for 15,000 steps can take days. Hardware failures and spot instance preemptions are inevitable, which makes checkpointing essential.

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="checkpoint-callback" lang="python" >}}

This callback runs every `N` training steps and uploads the checkpoint to durable storage. The key line is `File.from_local_sync()` which is a Flyte abstraction for uploading files. There are no blob store credentials to manage and no bucket paths to hardcode. Flyte automatically uses the storage backend configured for your cluster.

The callback only runs on rank 0. In distributed training, all 8 GPUs have identical model states (that's the point of data parallelism). Having all of them upload the same checkpoint would be wasteful and could cause race conditions.

When you restart a failed run, pass the checkpoint via `resume_checkpoint` so training resumes exactly where it left off, including the same step count, optimizer state, and learning rate schedule position.

### Real-time metrics with Flyte Reports

Multi-day training runs need observability. Is the loss decreasing? Did training diverge? Is the learning rate schedule behaving correctly? Flyte Reports let you build live dashboards directly in the UI:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="reporting-callback" lang="python" >}}

The `_initialize_report` method (see complete code) creates an HTML/JavaScript dashboard with interactive charts. The callback then calls `flyte.report.log()` every `N` steps to push new metrics. The charts update in real-time so you can watch your loss curve descend while training runs.

There is no need to deploy Grafana, configure Prometheus, or keep a TensorBoard server running. Using `flyte.report.log()` is sufficient to get live training metrics directly in the Flyte UI.

![Metrics viz](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/distributed-llm-pretraining/metrics.png)

### Streaming data at scale

Training datasets are massive. SlimPajama contains 627 billion tokens and spans hundreds of gigabytes even when compressed. Downloading the entire dataset to each training node before starting would take hours and waste storage.

Instead, we convert the data to MDS (MosaicML Data Shard) format and stream it during training:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="data-loading-task" lang="python" >}}

This task does three things:

1. **Tokenizes the text** using GPT-2's BPE tokenizer
2. **Concatenates documents** into fixed-length sequences (no padding waste)
3. **Writes shards** to storage in a format optimized for streaming

The task returns a Flyte `Dir` object, which is a reference to the output location. It's not the data itself, just a pointer. When the training task receives this `Dir`, it streams shards on-demand rather than downloading everything upfront.

Flyte caches this task automatically. Run the pipeline twice with the same dataset config, and Flyte skips tokenization entirely on the second run. Change the dataset or sequence length, and it re-runs.

### Distributed training with FSDP

Now we get to the core: actually training the model across multiple GPUs. FSDP is what makes this possible for large models.

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="training-task-signature" lang="python" >}}

Notice `report=True` on the task decorator. It enables Flyte Reports for this specific task.

The training task receives the prepared dataset as a `Dir` and streams data directly from storage:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="training-task-streaming" lang="python" >}}

`prepared_dataset.path` provides the remote storage path for the dataset. MosaicML's `StreamingDataset` automatically shards data across GPUs so that each rank sees different samples, without requiring a manual distributed sampler. The credentials are already in the environment because Flyte set them up.

FSDP is where the memory magic happens. Instead of each GPU holding a full copy of the model (like Distributed Data Parallel (DDP)), FSDP shards the parameters, gradients, and optimizer states across all GPUs. Each GPU only holds 1/8th of the model. When a layer needs to run, FSDP all-gathers the full parameters, runs the computation, then discards them.

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="training-task-fsdp" lang="python" >}}

We wrap at the `GPTBlock` level because each transformer block becomes an FSDP unit. This balances communication overhead (more units = more all-gathers) against memory savings (smaller units = more granular sharding).

One subtle detail: gradient clipping. With FSDP, gradients are sharded across ranks, so computing a global gradient norm would require an expensive all-reduce operation. Instead of norm-based clipping, we use value-based gradient clipping, which clamps each individual gradient element to a fixed range. This can be done independently on each rank with no coordination overhead and is commonly used for large-scale FSDP training.

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="training-task-trainer" lang="python" >}}

The trainer configuration brings together all the pieces we've discussed:

- **`precision="bf16-mixed"`**: BFloat16 mixed precision training. BF16 has the same dynamic range as FP32 (unlike FP16), so you don't need loss scaling. This is the standard choice for modern GPU training.
- **`gradient_clip_val=1.0`**: Clips gradients to prevent exploding gradients during training. Combined with value-based clipping for FSDP compatibility.
- **`accumulate_grad_batches`**: Accumulates gradients over multiple forward passes before updating weights. This lets us hit a larger effective batch size than what fits in GPU memory.
- **`val_check_interval`**: How often to run validation. For long training runs, you don't want to validate every epoch — that would be too infrequent. Instead, validate every `N` training steps.
- **`use_distributed_sampler=False`**: We disable Lightning's built-in distributed sampler because `StreamingDataset` handles data sharding internally. Using both would cause conflicts.
- **`benchmark=True`**: Enables cuDNN autotuning. PyTorch will benchmark different convolution algorithms on the first batch and pick the fastest one for your specific input sizes.

The trainer then calls `fit()` with the model, data loaders, and optionally a checkpoint path to resume from.

### Tying it together

The pipeline task orchestrates everything:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="main-pipeline" lang="python" >}}

The flow is straightforward: load the configuration, prepare the data, and run training. Flyte automatically manages the execution graph so data preparation runs first and training waits until it completes. If data preparation is cached from a previous run, training starts immediately.

The gradient accumulation calculation is worth noting. We want a global batch size of 256 (this affects training dynamics), but each GPU can only fit a small batch. With 8 GPUs and batch size 1 each, we need 32 accumulation steps to hit 256.

## Running the pipeline

With everything defined, running is simple:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="main" lang="python" >}}

This configuration is designed for testing and demonstration. Notice `max_train_samples=5_000_000` — that's 5 million samples from a dataset with 627 billion tokens. A tiny fraction, enough to verify everything works without burning through compute.

For a real pretraining run, you would remove this limit by setting `max_train_samples=None`, or increase it significantly. You would also increase `max_steps` to match your compute budget, likely scale to multiple nodes by setting `NUM_NODES=4` or higher, and allocate more resources. The rest of the pipeline remains unchanged.

```bash
flyte create config --endpoint <FLYTE_OR_UNION_ENDPOINT> --project <PROJECT_NAME> --domain <DOMAIN_NAME> --builder remote
uv run train.py
```

When you run this, Flyte:

1. **Builds the container** (cached after first run)
2. **Schedules data prep** on CPU nodes
3. **Waits for data prep** (or skips if cached)
4. **Provisions H200 nodes** and launches distributed training
5. **Streams logs and metrics** to the UI in real-time

Open the Flyte UI to observe the workflow execution. The data preparation task completes first, followed by the training task spinning up. As training begins, the Flyte Reports dashboard starts plotting loss curves. If anything goes wrong, the logs are immediately available in the UI.

![Training Log](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/distributed-llm-pretraining/logs.png)

If training fails due to an out-of-memory error, a GPU driver error, or a hardware issue, check the logs, fix the problem, and restart the run with `resume_checkpoint` pointing to the most recent checkpoint. Training resumes from where it left off. Flyte tracks the full execution history, so it is easy to see exactly what happened.

## Going further

If you've run through this tutorial, here's where to go next depending on what you're trying to do:

**You want to train on your own data.** The data prep task accepts any HuggingFace dataset with a `text` column. If your data isn't on HuggingFace, you can modify `load_and_prepare_streaming_dataset` to read from S3, local files, or any other source. The key is getting your data into MDS format. Once it's there, the streaming and sharding just works. For production training, look at SlimPajama, [RedPajama](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T), or [The Pile](https://huggingface.co/datasets/EleutherAI/pile) as starting points.

**You want to scale to more GPUs.** Bump `NUM_NODES` and Flyte handles the rest. The main thing to watch is the effective batch size. As you add more GPUs, you may want to reduce gradient accumulation steps to keep the same global batch size, or increase them if you want to experiment with larger batches.

**Your training keeps failing.** Add `retries=3` to your task decorator for automatic retry on transient failures. This handles spot instance preemption, temporary network issues, and the occasional GPU that decides to stop working. Combined with checkpointing, you get fault-tolerant training that can survive most infrastructure hiccups. For persistent failures, the Flyte UI logs are your friend as they capture stdout/stderr from all ranks.

**You want better visibility into what's happening.** We're actively working on surfacing GPU driver logs (xid/sxid errors), memory utilization breakdowns, and NCCL communication metrics directly in the Flyte UI. If you're hitting issues that the current logs don't explain, reach out. Your feedback helps us prioritize what observability features to build next!
