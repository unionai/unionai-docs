---
title: Fine-tuning a vision-language model with a frozen backbone
weight: 1
variants: +flyte +union
sidebar_expanded: true
---

# Fine-tuning a vision-language model with a frozen backbone

Large vision-language models like Qwen2.5-VL are remarkably capable out of the box. But adapting one to a specialized task raises an immediate question: do you really need to update 3 billion parameters?

Usually, no. The **frozen backbone pattern** is a practical alternative: keep all pretrained weights frozen and train only a small, task-specific adapter inserted before the vision encoder. The adapter learns to transform its input in a way that makes the frozen model perform well on your task without touching the underlying billions of parameters. The result is faster training, lower memory pressure, and a much smaller set of weights to store and version.

This tutorial makes that pattern concrete. We take a partially-occluded image classification task — CIFAR-10 images with random black rectangles covering 22–45% of the frame — and train a tiny Conv2d adapter to "see through" the occlusion before the frozen VLM processes it. The adapter has approximately **10,500 trainable parameters**. The backbone has 3 billion.

The machine learning is interesting, but the real focus here is on shipping a production-grade training pipeline:

- **Multi-node distributed training** across 2 nodes × 4 GPUs using PyTorch Elastic and DeepSpeed Stage 2
- **Automatic fault tolerance**: checkpoints upload to object storage after every validation epoch; if training fails, the pipeline returns the last known-good checkpoint instead of crashing
- **Live observability**: a streaming HTML dashboard in the Flyte UI updates in real-time as training runs, no separate monitoring infrastructure required
- **Cached data preparation**: dataset processing runs once and is reused across all reruns
- **Clean task isolation**: each stage runs with exactly the resources it needs, nothing more

> [!NOTE]
> Full code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/qwen_vl_frozen_backbone_finetuning).

## Overview

The pipeline has four tasks with clearly defined responsibilities:

1. **Dataset preparation** (`prepare_occlusion_dataset`): Downloads CIFAR-10, applies random occlusions, and writes image manifests as streaming JSONL files to object storage. Runs on CPU and is cached, so it only runs once regardless of how many times you rerun the pipeline with the same config.
2. **Multi-node training** (`train_qwen_adapter_multinode`): Runs PyTorch Lightning with DeepSpeed Stage 2 across 2 nodes × 4 L40s GPUs. Only the adapter trains; the 3B backbone stays frozen.
3. **Evaluation** (`evaluate_qwen_adapter`): Loads the saved adapter, runs inference on validation examples, and produces a predictions report. Runs on a single GPU.
4. **Driver** (`qwen_vl_multinode_deepspeed`): The pipeline entry point. Orchestrates the three tasks above, manages WandB initialization, handles recovery from training failures, and produces a final HTML report in the Flyte UI.

Why this separation? It mirrors how production pipelines should be structured. Data prep is cheap and deterministic so we cache it. Training is expensive and failure-prone so we isolate it with fault tolerance. Evaluation needs different hardware than training. The driver is pure coordination, so it gets minimal resources.

## Implementation

### Setting up the environment

Different tasks need different compute. Flyte's `TaskEnvironment` is how you declare exactly what each task needs.

First, define the container images. Training needs a full CUDA stack with ML libraries, driver compatibility, and DeepSpeed's build tools:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/config.py" fragment="gpu-image" lang="python" >}}

`from_base` starts from the official NVIDIA CUDA image, giving you NCCL, cuDNN, and the right driver headers out of the box. `with_apt_packages("build-essential")` is required because DeepSpeed compiles CUDA kernels at first use and without build tools, it silently falls back to slower CPU implementations. The non-GPU image for data preparation and orchestration is much lighter:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/config.py" fragment="non-gpu-image" lang="python" >}}

With images defined, each task gets its own resource declaration:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/config.py" fragment="task-environments" lang="python" >}}

A few things worth noting here:

- **`Elastic(nnodes=2, nproc_per_node=4)`**: Flyte's integration with PyTorch's elastic launch. It handles process spawning (one process per GPU), rank assignment, and distributed environment setup — master address, world size, rendezvous — without any shell scripting or manual `torchrun` invocations.
- **`shm="16Gi"`**: Shared memory is required for NCCL inter-GPU communication on the same node. Without it, you'll see cryptic errors from the communication library when training starts.
- **`cache="auto"`**: The dataset preparation task is cached by input hash. Running the pipeline twice with the same hyperparameters skips it entirely on the second run.
- **`depends_on`**: The driver task declares that each worker image must finish building before it starts, ensuring containers are ready before the driver begins orchestrating.
- **`secrets`**: The WandB API key is injected from Flyte's secret store as an environment variable. No credentials in code.

All training hyperparameters flow through a single typed dataclass:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/config.py" fragment="config-dataclass" lang="python" >}}

Using a dataclass rather than scattered constants or argparse arguments means the full config is serializable, can be stored in artifact metadata alongside the model checkpoint, and flows cleanly as a typed input between tasks. The `to_dict()` method serializes it for WandB logging.

### Preparing the dataset

The dataset task handles everything: downloading CIFAR-10, generating occlusions, and writing the manifests.

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/data.py" fragment="prepare-dataset-task" lang="python" >}}

Each image gets a randomly-placed black rectangle. The occlusion covers 22–42% of the image area during training and 28–45% during evaluation. The occlusion is deliberately harder at eval time to test how robust the adapter is. The bounding box coordinates are written into each manifest record alongside the image path and ground-truth label, so the training task can reconstruct the binary occlusion mask as the adapter's fourth input channel.

Two Flyte primitives handle data persistence without any manual storage management:

- **`JsonlFile.new_remote()`** opens a streaming writer that writes directly to remote object storage. The training task reads records back via `jf.iter_records_sync()`, so no local file paths and S3 credentials to manage.
- **`Dir.from_local()`** uploads the local images directory to object storage and returns a typed handle. The training task downloads it to a local path via `Dir.download_sync()`.

Because `cache="auto"` is set on this task, dataset preparation runs once. Subsequent reruns with the same config skip it entirely.

### The adapter

Here's the entire trainable component of the model with `~10,500` parameters:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/model.py" fragment="residual-adapter" lang="python" >}}

The adapter takes the occluded image (3 channels) concatenated with the binary occlusion mask (1 channel) as a 4-channel input. It predicts a residual correction through a small convolutional network, then adds that correction back to the original pixels. The learnable `gate` scalar, initialized to `0.10`, controls how strongly the adapter modifies the image. It starts as a near-identity transformation and gradually grows during training as the adapter gains confidence.

The adapter is plugged into Qwen2.5-VL via a Lightning module:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/model.py" fragment="adapter-module-init" lang="python" >}}

The key line is `self.backbone.requires_grad_(False)`. This freezes all 3 billion backbone parameters which means only the adapter's ~10,500 weights receive gradients. `gradient_checkpointing_enable()` trades compute for memory: instead of keeping the frozen backbone's intermediate activations in GPU memory during the backward pass, they're recomputed on the fly. This is critical when a 3B model is sitting in GPU memory alongside your optimizer state.

`strict_loading = False` handles an important DeepSpeed checkpoint detail. When `exclude_frozen_parameters=True` is set on the strategy, DeepSpeed only saves the adapter weights in checkpoints, not the 3B frozen backbone. On resume, the checkpoint won't contain backbone weights, so loading must be non-strict. The `on_load_checkpoint` hook fills in the missing backbone weights from the freshly-loaded HuggingFace model, combining the best of both worlds: small checkpoints and a fully initialized model.

The training loss combines two objectives:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/model.py" fragment="forward-losses" lang="python" >}}

The **language modeling loss** (cross-entropy on the predicted class label tokens) drives the model to produce correct answers. The **reconstruction loss** (mean absolute error between the adapter's output and the clean image, computed only in the occluded region) pushes the adapter to actually restore the missing pixels rather than finding a representation shortcut. Without it, the adapter could overfit the frozen backbone's quirks and produce correct tokens while generating noise in the masked region. The `reconstruction_loss_weight` (default `0.35`) balances these two objectives.

Because Qwen2.5-VL's preprocessor packs image patches into a flat `(num_patches, patch_dim)` tensor, the adapter must unpack this into a spatial `(B, C, H, W)` tensor, apply the convolutions, then repack. The `packed_pixels_to_dense_images` and `dense_images_to_packed_pixels` utilities in `model.py` handle this format conversion transparently.

### Multi-node training with DeepSpeed

The training task is a standard PyTorch Lightning training loop with distributed infrastructure handled by Flyte and DeepSpeed:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="training-task-signature" lang="python" >}}

The `@wandb_init` decorator integrates with the `wandb_config` context created in the driver task. It retrieves the initialized WandB run and attaches a `WandbLogger` to the trainer. The `report=True` flag on the task decorator enables Flyte Reports for live dashboard streaming from this task.

![Live Training](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/qwen-vl-finetuning/live_training_graph.png)
![Live Training Contd](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/qwen-vl-finetuning/losses.png)

DeepSpeed Stage 2 shards optimizer states and gradients across GPUs, reducing per-GPU memory usage significantly. The critical configuration flag here is `exclude_frozen_parameters=True`:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="deepspeed-strategy" lang="python" >}}

Without `exclude_frozen_parameters=True`, DeepSpeed would shard and checkpoint the frozen backbone weights too, producing enormous checkpoint files, slow checkpoint saves, and unnecessary communication overhead. With it, only the adapter participates in sharding and checkpointing. The backbone is loaded independently on each worker from HuggingFace.

Gradient accumulation is computed automatically to hit the target global batch size regardless of how many GPUs are actually running:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="grad-accum" lang="python" >}}

With 2 nodes × 4 GPUs × per-device batch size 1, the effective per-step batch is 8. To reach the default target of 16, the trainer accumulates over 2 steps. Change `NUM_NODES` or `per_device_batch_size` and the calculation adjusts automatically.

The trainer brings everything together:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="trainer-setup" lang="python" >}}

`precision="bf16-mixed"` uses BFloat16, which matches FP32's dynamic range (unlike FP16), so you don't need loss scaling. This is the standard choice for modern VLM training. `benchmark=True` runs cuDNN autotuning on the first batch to select the fastest kernels for your specific input sizes.

### Fault tolerance and recovery

Multi-node GPU jobs fail. Hardware hiccups, spot instance preemptions, NCCL timeouts, memory spikes, etc. and the question is when, not if. This pipeline handles it with a two-part system.

After every validation epoch, the `RecoveryArtifactCallback` calls `trainer.save_checkpoint()` to write a DeepSpeed checkpoint directory, then uploads all shard files to the recovery URI. Each node's local rank 0 uploads its own shards; global rank 0 uploads the metadata files (`metrics.json`, `summary.json`). A distributed barrier between save and upload ensures all workers finish before training continues.

If training fails, the driver task catches the error and returns the last recovery artifact instead of propagating the failure:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="recovery-handler" lang="python" >}}

A failed run still produces useful output: the best checkpoint reached before the failure, along with a partial training report. To resume from that point, pass the recovery artifact as `resume_training_artifacts` on the next run. The training task downloads it, finds the most recent `.ckpt` file, and passes it to `trainer.fit()` as `ckpt_path`. Training picks up at the last saved epoch with optimizer state and metrics history intact.

The recovery URI is constructed from the configurable base path and the run name:

```
s3://your-bucket/qwen-vl-multinode-deepspeed/<run-name>/qwen_vl_training_recovery/
```

This means each run gets its own recovery location, so you can identify exactly which run a checkpoint came from.

### Live observability

`flyte.report` lets you push HTML content directly into the Flyte UI during task execution, with no separate monitoring infrastructure. The `LiveTrainingReportCallback` uses this to stream training metrics in real-time:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/callbacks.py" fragment="live-report-push" lang="python" >}}

`on_train_start` (see the full code) initializes the dashboard with an SVG loss chart and an HTML metrics table. Every `report_every_n_steps` training steps, `_push_update` serializes the latest metrics into a `<script>` block and calls `flyte.report.log()` to append it to the live page. The JavaScript `updateQwenLiveReport()` function then updates the chart polylines and appends a new table row for each step.

For resumed runs, the prior metrics history is seeded into the table on `on_train_start`, so the metrics view is continuous across runs rather than restarting from zero.

![Recovery](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/qwen-vl-finetuning/recovery.png)

WandB metrics are logged in parallel by `AdapterMetricsCallback` after each validation epoch, including per-epoch train and validation losses, the LM loss component, the reconstruction loss component, and the current adapter gate value.

![WandB](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/qwen-vl-finetuning/wandb.png)

### Evaluation

After training completes, a separate task runs inference on a single GPU:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="evaluation-task-header" lang="python" >}}

The task is async so the driver can `asyncio.gather` the downloads of training artifacts and images in parallel rather than sequentially, a simple speedup that matters when downloading hundreds of megabytes from object storage.

The evaluation task loads the adapter state dict from `adapter_artifact.pt`, rebuilds the frozen backbone fresh from HuggingFace (there's no need to checkpoint 3B weights, only the ~10,500 adapter weights travel with the artifact), and runs greedy decoding on each validation example. The metric is exact-match accuracy between the model's predicted class token and the ground-truth CIFAR-10 label.

### Putting it all together

The driver task is the pipeline entry point that all other tasks flow through:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/tasks.py" fragment="driver-task-signature" lang="python" >}}

The driver constructs the recovery URI from `checkpoint_base_uri` and the current run name, prepares the dataset (or retrieves it from cache), then executes training inside a `wandb_config` context. The `wandb_config` context manager creates and registers a WandB run; the `@wandb_init` decorator on the training task retrieves it, updates it with the full `Config` dataclass, and attaches a `WandbLogger`. Neither the training task nor the callbacks need any WandB initialization code of their own.

The recovery handler (shown in the previous section) wraps the training call. If training succeeds, evaluation runs next. The driver then downloads both the training and evaluation artifacts concurrently and assembles a final HTML report with training curves, evaluation summary, per-epoch metrics table, and sample prediction cards with the actual occluded images, which is pushed to Flyte Reports.

## Running the tutorial

Before running, update two placeholders in `config.py`:

- `DEFAULT_CHECKPOINT_BASE_URI`: your S3, GCS, or Azure Blob URI for checkpoint storage
- The `wandb_api_key` secret key name to match your cluster's secret store configuration

Then configure and launch:

{{< code file="/unionai-examples/v2/tutorials/qwen_vl_frozen_backbone_finetuning/train.py" fragment="main-run" lang="python" >}}

```bash
flyte create config --endpoint <YOUR_ENDPOINT> --project <PROJECT> --domain <DOMAIN> --builder remote
uv run train.py
```

When you run this, the pipeline:

1. **Builds containers** once and caches them for subsequent runs
2. **Prepares the dataset**: downloads CIFAR-10, generates occlusions, writes JSONL manifests; cached on subsequent runs with the same config
3. **Launches multi-node training**: provisions 2 × 4 L40s GPUs and starts the Elastic job
4. **Streams metrics to the live dashboard**: the Flyte Reports view starts updating as soon as the first step logs
5. **Runs evaluation**: a single-GPU task loads the adapter and runs inference, computing exact-match accuracy
6. **Generates the final report**: training curves, evaluation summary, and sample prediction cards appear in the Flyte UI

![Final Report](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/qwen-vl-finetuning/final_report.png)
![Predictions](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/qwen-vl-finetuning/predictions.png)

To resume a failed or interrupted run, uncomment the `resume_training_artifacts` line in `train.py` and point it to the recovery URI from the previous run. Training picks up from the last checkpoint with metrics history intact.

## Going further

**Adapting this to a different task.** The frozen backbone pattern transfers directly. Replace `QwenOcclusionDataset` and `prepare_occlusion_dataset` with your own data, update the prompt template, and adjust the dual loss if a pixel-level reconstruction term doesn't apply to your task. The multi-node Elastic setup, DeepSpeed Stage 2 config, recovery system, and live reporting are completely reusable.

**Using a larger Qwen model.** Change `DEFAULT_MODEL_NAME` to `Qwen/Qwen2.5-VL-7B-Instruct` or a larger variant. You may need to increase `memory` in `training_env` and reduce `per_device_batch_size`. The frozen backbone + adapter pattern becomes more valuable at larger scales where you're always training the same ~10,500-parameter adapter regardless of backbone size.

**Training keeps failing.** Add `retries=3` to the `@training_env.task` decorator. With the recovery callback uploading checkpoints after every validation epoch, Flyte automatically restarts training from the last checkpoint on transient failures. Spot instance preemptions and most hardware hiccups become non-events.

**Scaling to more nodes.** Increase `NUM_NODES` in `config.py`. The Elastic plugin, DeepSpeed strategy, and gradient accumulation calculation all adapt automatically. The recovery system is unchanged as each run still gets its own recovery URI.
