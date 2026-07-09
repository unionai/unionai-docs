---
title: Intra-task checkpoints
weight: 15
variants: +flyte +union
---

# Intra-task checkpoints

Long-running tasks — model training especially — can fail partway through: a spot
instance is reclaimed, a pod is evicted, an out-of-memory error kills the process.
When the task is retried, it normally starts over from the beginning.

Intra-task checkpoints let a task save in-progress state to object storage as it
runs and load that state at the start of the next attempt, so a retry resumes from
where the previous attempt left off instead of repeating completed work.

## The checkpoint object

Inside a running task, `flyte.ctx().checkpoint` returns a `flyte.Checkpoint` (or `None`
when checkpointing isn't configured) bound to the action's checkpoint location in object storage:

- **Save**: `await checkpoint.save(...)` (async tasks) or `checkpoint.save_sync(...)`
  (sync tasks and synchronous framework callbacks). Accepts raw `bytes`, a file path,
  or a directory path — a directory is stored as a single compressed archive.
- **Load**: `await checkpoint.load()` or `checkpoint.load_sync()`. Returns a local
  `pathlib.Path` to the restored file or directory tree, or `None` when there is no
  previous checkpoint (i.e. on the first attempt).
- `flyte.latest_checkpoint(root)` finds the newest checkpoint file under a restored
  directory tree — useful for frameworks like PyTorch Lightning that write
  `last.ckpt` files into a directory.

Checkpoints only matter when the task can run more than once, so give the task
retries with `@env.task(retries=...)`. Each retry attempt sees the checkpoint saved
by the attempt before it.

> [!NOTE] Checkpoints vs. caching vs. traces
> - **Task caching** skips an entire task when it has already run with the same inputs.
> - **[Traces](./traces)** checkpoint at the boundaries of helper functions called by a task.
> - **Intra-task checkpoints** save state *within* a single task body — mid-loop,
>   mid-epoch — across retry attempts of the same action.

## Basic usage

The simplest checkpoint is a raw byte payload. This task counts up to
`n_iterations`, saving its progress on every iteration. A simulated failure kills
it partway through; the retry loads the saved counter and continues rather than
restarting from zero:

{{< tabs "generic-checkpoint" >}}
{{< tab "Async" >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/generic_checkpoint.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< tab "Sync" >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/generic_checkpoint_sync.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

Running this with `n_iterations=10` produces three failed attempts and one
successful one. Each attempt fails later than the last, because each one starts
from the checkpoint its predecessor saved.

## Checkpointing ML training frameworks

The same pattern applies to real training loops, whatever the framework:

1. **Load** the previous attempt's checkpoint at the start of the task; if one
   exists, restore the model/optimizer state and work out where to resume.
2. **Save** a checkpoint at a regular interval — every epoch or every N steps —
   as training progresses.

Frameworks with their own checkpoint files (PyTorch Lightning, Hugging Face
`Trainer`) already write them to a local directory; there you hook their callback
system and mirror that directory to the Flyte checkpoint, then feed the restored
directory back to the framework's native resume mechanism.

{{< tabs "ml-framework-checkpoints" >}}

{{< tab "PyTorch" >}}
{{< markdown >}}
Save the model state dict, optimizer state, and epoch counter with `torch.save`
after each epoch, and restore all three with `torch.load` on retry:
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/pytorch_checkpoint.py" fragment="task" lang="python" >}}
{{< /tab >}}

{{< tab "PyTorch Lightning" >}}
{{< markdown >}}
Lightning already writes `last.ckpt` through its `ModelCheckpoint` callback.
Subclass it to mirror the checkpoint directory to Flyte after each epoch
(Lightning callbacks are synchronous, so use `flyte.Checkpoint.save_sync`):
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/pytorch_lightning_checkpoint.py" fragment="callback" lang="python" >}}
{{< markdown >}}
In the task, restore the previous tree, pick the newest `last.ckpt` with
`flyte.latest_checkpoint`, and hand it to `Trainer.fit(ckpt_path=...)` — Lightning
restores the model, optimizer, and epoch from there:
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/pytorch_lightning_checkpoint.py" fragment="task" lang="python" >}}
{{< /tab >}}

{{< tab "Hugging Face Trainer" >}}
{{< markdown >}}
`transformers.Trainer` writes `checkpoint-<step>` directories under its
`output_dir` (here, every epoch via `save_strategy="epoch"`). A `TrainerCallback`
mirrors that directory to Flyte after each save:
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/huggingface_trainer_checkpoint.py" fragment="callback" lang="python" >}}
{{< markdown >}}
On retry, restore the tree, locate the last Hugging Face checkpoint with
`get_last_checkpoint`, and pass it to `trainer.train(resume_from_checkpoint=...)`:
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/huggingface_trainer_checkpoint.py" fragment="task" lang="python" >}}
{{< /tab >}}

{{< tab "scikit-learn" >}}
{{< markdown >}}
For estimators that support incremental training with `partial_fit`, pickle the
estimator together with a progress counter after each training chunk. A retry
unpickles the bundle and continues from the next chunk:
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/sklearn_partial_checkpoint.py" fragment="task" lang="python" >}}
{{< /tab >}}

{{< tab "Unsloth" >}}
{{< markdown >}}
LoRA fine-tuning with [Unsloth](https://unsloth.ai/) and `trl.SFTTrainer` uses the
same callback-and-resume pattern as the Hugging Face `Trainer`, since `SFTTrainer`
is built on it. Unsloth requires an NVIDIA, AMD, or Intel GPU, so the task
environment requests one:
{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/unsloth_sft_checkpoint.py" fragment="task" lang="python" >}}
{{< /tab >}}

{{< /tabs >}}

> [!NOTE] Simulated failures in the runnable examples
> The full example files for the basic, PyTorch, and scikit-learn cases inject a
> failure at a regular interval (`failure_interval`) so you can watch the retries
> resume from the checkpoint. In production code you would drop those lines — real
> failures (preemptions, OOMs, crashes) trigger the same resume path.

## How checkpoints are stored

Each action attempt gets a checkpoint prefix in the object store configured for
your cluster. `flyte.Checkpoint.save` uploads a file as-is, stores a directory as
a gzip-compressed tarball, and accepts raw `bytes` as a single blob.
`flyte.Checkpoint.load` downloads the previous attempt's object into a local
temporary workspace and returns the path — a restored directory tree, or the path
to the single restored file.

Saving repeatedly overwrites the same checkpoint object, so the cost of frequent
checkpointing is upload bandwidth, not unbounded storage growth. Checkpoint how
often you can afford to lose work: every epoch is typical for training loops.
