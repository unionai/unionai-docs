---
title: Distributed LLM pretraining
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Distributed LLM pretraining

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/pretraining/train.py).

This tutorial demonstrates how to pretrain large language models (LLMs) at scale using Flyte, PyTorch Lightning, and NVIDIA H200 GPUs. You'll learn how to build a complete distributed training pipeline that handles data preparation, multi-GPU training with FSDP, checkpoint management, and real-time metrics visualization.

## Use case

In this tutorial, you'll learn how to:

- Build a GPT-2 style language model from scratch with PyTorch
- Use PyTorch Lightning for training orchestration with FSDP for distributed training
- Stream data efficiently using MosaicML's Streaming library (MDS format)
- Get real-time training metrics visualization using Flyte Reports
- Handle checkpoint resumption and fault-tolerant training

## Why Flyte for LLM pretraining?

Training large language models presents unique challenges:

1. **Resource management**: LLMs require substantial GPU memory and compute. Flyte handles dynamic resource allocation across multiple nodes.

2. **Data streaming**: Training datasets can be terabytes in size. Flyte integrates with streaming datasets for efficient data loading without downloading entire datasets upfront.

3. **Fault tolerance**: Long-running training jobs need checkpoint management and recovery. Flyte provides built-in caching and resumption.

4. **Observability**: Training runs can last days or weeks. Flyte Reports provide real-time visibility into progress.

## Architecture overview

The training pipeline consists of three main components:

1. **Data preparation**: Tokenize and convert datasets to MDS (MosaicML Data Shard) format for efficient streaming
2. **Distributed training**: Multi-GPU training with FSDP (Fully Sharded Data Parallel)
3. **Real-time reporting**: Live training metrics visualization in the Flyte UI

## Define dependencies and imports

Start by importing the necessary modules:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="imports" lang="python" >}}

Key imports:
- `flyte` and `flyte.report` for orchestration and reporting
- `lightning` for training loop management
- `torch` and `torch.nn` for model definition
- `flyteplugins.pytorch.task.Elastic` for distributed training

## Configure training constants

Define the model and training configuration constants:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="constants" lang="python" >}}

These constants define the distributed training setup (nodes and devices) and model vocabulary parameters.

## Define the container image

Create a container image with all required dependencies:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="image" lang="python" >}}

This image includes:
- Transformers and tokenizers for data processing
- MosaicML Streaming for efficient data loading
- PyTorch and Lightning for training
- The Flyte PyTorch plugin for distributed training

## Configure task environments

Define specialized environments for different pipeline stages:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="task-envs" lang="python" >}}

Three environments handle different workloads:

1. **`data_loading_env`**: Moderate resources for tokenization and data preparation
2. **`distributed_llm_training_env`**: H200 GPUs with shared memory for NCCL and the Elastic plugin for distributed training
3. **`driver_env`**: Lightweight environment for pipeline orchestration

The `Elastic` plugin specifies the distributed topology: `nnodes` (number of nodes) and `nproc_per_node` (GPUs per node).

## Define model configurations

Support multiple model sizes with preset hyperparameters:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="model-configs" lang="python" >}}

Each model size includes optimized settings for batch size, learning rate, checkpointing frequency, and validation intervals.

## Implement the GPT model

Build a GPT-2 style transformer from scratch:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="gpt-model" lang="python" >}}

The model consists of:
- **GPTConfig**: Model hyperparameters
- **GPTBlock**: Transformer block with causal self-attention and MLP
- **GPTModel**: Full language model with embeddings, transformer blocks, and LM head

Key features:
- Causal masking for autoregressive generation
- Weight tying between input embeddings and output projection
- Efficient caching for position IDs and causal masks

## Create the Lightning training module

Wrap the model in a PyTorch Lightning module:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="lightning-module" lang="python" >}}

The Lightning module handles:
- **Training step**: Causal language modeling loss with label shifting
- **Validation step**: Evaluation metrics including perplexity
- **Optimizer**: AdamW with weight decay separation and cosine LR schedule with warmup

## Implement custom callbacks

### S3 checkpoint callback

Periodically upload checkpoints to S3 for durability:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="checkpoint-callback" lang="python" >}}

This callback ensures checkpoints are safely stored in remote storage even if the training job is interrupted.

### Flyte reporting callback

Stream training metrics to the Flyte UI in real-time:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="reporting-callback" lang="python" >}}

This callback creates an interactive dashboard with:
- Training and validation loss curves
- Learning rate schedule visualization
- Real-time metrics updates

## Prepare streaming datasets

Convert datasets to MDS format for efficient streaming:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="data-loading-task" lang="python" >}}

This task:
- Loads datasets in streaming mode for memory efficiency
- Concatenates documents into fixed-length sequences
- Writes sharded output for parallel data loading

## Implement distributed training

The main training task orchestrates multi-GPU training:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="training-task" lang="python" >}}

This task:
- Configures FSDP for memory-efficient distributed training
- Sets up streaming data loaders that auto-shard across GPUs
- Initializes the Lightning trainer with callbacks and strategies
- Supports checkpoint resumption for fault tolerance

## Create the main pipeline

Orchestrate the complete training workflow:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="main-pipeline" lang="python" >}}

The pipeline:
1. Loads model configuration based on the specified size
2. Prepares streaming datasets with tokenization
3. Calculates gradient accumulation for target global batch size
4. Launches distributed training with all configurations

## Run the training pipeline

Execute the pipeline with your desired configuration:

{{< code file="/external/unionai-examples/v2/tutorials/pretraining/train.py" fragment="main" lang="python" >}}

To run the training:

```bash
flyte create config --endpoint <FLYTE_OR_UNION_ENDPOINT> --project <PROJECT_NAME> --domain <DOMAIN_NAME> --builder remote
uv run train.py
```

## Key features

### FSDP for large models

FSDP (Fully Sharded Data Parallel) enables training models that exceed single-GPU memory by:
- Sharding parameters, optimizer states, and gradients across GPUs
- All-gathering parameters only when needed for computation

### Streaming data loading

MosaicML Streaming provides:
- Efficient loading without downloading entire datasets upfront
- Automatic sharding across distributed workers
- Resumable iteration for fault tolerance

### Real-time reporting

Flyte Reports provide:
- Live training metrics visualization
- Interactive loss and learning rate charts
- No external monitoring infrastructure required

## Next steps

- Experiment with different model sizes (1.5B, 30B, 65B)
- Try different datasets (SlimPajama, The Pile, etc.)
- Add evaluation on downstream tasks
- Implement model parallelism for even larger models
