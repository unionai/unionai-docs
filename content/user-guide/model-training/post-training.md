---
title: Post-training and fine-tuning
description: Adapt a pretrained model with supervised fine-tuning, LoRA, or preference tuning, then evaluate it and hand it to serving.
icon: sliders
weight: 2
variants: +flyte +union
---

# Post-training and fine-tuning

Post-training starts from a pretrained model and adapts it with your data: supervised fine-tuning (SFT), parameter-efficient methods such as LoRA and QLoRA, or preference tuning such as DPO. The training code is usually a library call, such as TRL's `SFTTrainer` or the Hugging Face `Trainer`. Flyte runs the stages around it: getting the base model and data onto the GPU, keeping the run recoverable, comparing the result with the base model, and handing the weights to serving.

## Define the environments

Fine-tuning needs one GPU environment for training and evaluation, and a CPU environment for data prep and the driver:

{{< code file="/unionai-examples/v2/tutorials/llm_fine_tuning_lora_qlora/llm_fine_tuning_lora_qlora.py" fragment="env" lang=python >}}

- `flyte.Image.from_uv_script` builds the image from the script's own PEP 723 dependency header, so the image and your local environment use the same pins.
- The Hugging Face token comes from a [secret](../tasks/task-configuration/secrets) and is set as `HF_TOKEN`, which `transformers` and `datasets` read automatically.
- `depends_on=[gpu_env]` lets a driver in the CPU environment call the GPU tasks.

A single GPU is enough for LoRA on models of a few billion parameters. For full fine-tuning of a larger model, or fine-tuning with DeepSpeed, use a [clustered environment](./pretraining#run-torchrun-across-nodes).

## Structure the pipeline

A fine-tuning pipeline has the same stages whatever the method:

1. **Prepare the data** in a CPU task with `cache="auto"`, and return it as a `flyte.io.Dir`. Later runs with a different learning rate or LoRA rank skip this step.
2. **Train** in a GPU task with `report=True`, and return the adapter or model as a `flyte.io.Dir`. The directory goes to your object store, and the next task gets a reference to it.
3. **Evaluate** the base model and the fine-tuned model on the same held-out set, and report both scores. A fine-tuning run that doesn't beat the base model is a result too.
4. **Serve or publish** the model directory.

Because each step is a task, switching methods is a change to one task's arguments, not to the pipeline. Comparing LoRA with full fine-tuning is two calls to the same pipeline, run side by side with `asyncio.gather`.

## Avoid downloading the base model every run

A large base model takes minutes to download from Hugging Face, on every GPU task that loads it. Copy it into your object store once and pass the stored copy to each task. See [Prefetching models](../inference/prefetching-models).

## Resume from the last checkpoint

GPU nodes get preempted, and a fine-tuning run that restarts from step 0 wastes the hours before the failure. Connect the trainer's checkpoints to `flyte.Checkpoint` with a callback:

{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/huggingface_trainer_checkpoint.py" fragment="callback" lang=python >}}

Then load the previous attempt's checkpoint at the start of the task and pass it to `trainer.train`:

{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/huggingface_trainer_checkpoint.py" fragment="task" lang=python >}}

With `retries` set on the task, a failed attempt restarts from the last saved epoch. The same pattern works for PyTorch Lightning, plain PyTorch loops, and Unsloth. See [Intra-task checkpoints](../tasks/task-programming/intra-task-checkpoints).

## Watch training while it runs

`report=True` gives the task a report tab in the UI. Publish loss curves, learning-rate schedules, and sample generations with `flyte.report.replace.aio(..., do_flush=True)`, and the tab updates while the task runs. See [Reports](../tasks/task-programming/reports). To log to an experiment tracker instead, see the [Weights & Biases](../../integrations/wandb/_index) and [MLflow](../../integrations/mlflow/_index) integrations.

## Hand the model to serving

{{< variant union >}}
{{< markdown >}}

Publish the trained model as an [artifact](../artifacts/_index). A vLLM or FastAPI app can then serve the latest version by name, and each version records the run that produced it. See [Deploy trained models](../inference/deploy-trained-models).

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

Return the trained model as a `flyte.io.Dir`. A vLLM or FastAPI app can then load it from the run that produced it. See [Deploy trained models](../inference/deploy-trained-models).

{{< /markdown >}}
{{< /variant >}}

## Related

- [LLM fine-tuning with LoRA and QLoRA](../../tutorials/model-training/llm-fine-tuning-lora-qlora/_index): the full pipeline on this page, with live reports.
- [Fine-tuning a VLM](../../tutorials/computer-vision/qwen-vl-finetuning/_index): multi-node fine-tuning with DeepSpeed and Lightning.
- [BERT emotion classification](../../tutorials/model-training/bert-fine-tuning-emotion/_index): fine-tuning an encoder with the Hugging Face `Trainer`.
- [Reinforcement learning](../reinforcement-learning/_index): post-training with rewards instead of labels.
