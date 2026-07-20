---
title: LLM fine-tuning with LoRA and QLoRA
weight: 2
variants: +flyte +union
---

# LLM fine-tuning with LoRA and QLoRA

> [!NOTE]
> Code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/llm_fine_tuning_lora_qlora).

This tutorial fine-tunes a language model for SQL generation using three methods in one workflow: **full** fine-tuning, **LoRA** adapters, and **QLoRA** (4-bit quantized base + LoRA). The pipeline prepares an instruction dataset from HuggingFace, trains with [TRL](https://huggingface.co/docs/trl) `SFTTrainer`, evaluates against a base-model baseline, and streams training charts into Flyte reports.

Flyte provides:

- **GPU training** with live loss and learning-rate charts via `report=True`.
- **Method switching** through a single `method` parameter (`full`, `lora`, or `qlora`).
- **Cached dataset preparation** for fast iteration on hyperparameters.

## Define the task environments

The GPU environment declares a HuggingFace token secret for gated models.

{{< code file="/unionai-examples/v2/tutorials/llm_fine_tuning_lora_qlora/llm_fine_tuning_lora_qlora.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "torch>=2.1.0",
#    "transformers>=4.45.0",
#    "peft>=0.13.0",
#    "trl>=0.12.0",
#    "bitsandbytes>=0.44.0",
#    ...
# ]
# ///
```

## Orchestrate the pipeline

{{< code file="/unionai-examples/v2/tutorials/llm_fine_tuning_lora_qlora/llm_fine_tuning_lora_qlora.py" fragment=pipeline lang=python >}}

## Run the workflow

Create a HuggingFace token secret if you use a gated base model:

```
flyte create secret huggingface-token <YOUR_HF_TOKEN>
```

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/llm_fine_tuning_lora_qlora):

```
cd v2/tutorials/llm_fine_tuning_lora_qlora
uv run --script llm_fine_tuning_lora_qlora.py
```

Try QLoRA on a GPU:

```
flyte run llm_fine_tuning_lora_qlora.py pipeline --method qlora --epochs 3
```

QLoRA requires CUDA; LoRA and full fine-tuning follow the same entry point with different memory requirements.
