---
title: Train a DFlash block drafter
icon: grid-3x3-gap
description: Fine-tune a DFlash block-diffusion drafter for Qwen3-8B that drafts 15 tokens in one pass, on the same data as EAGLE-3.
weight: 2
variants: +flyte +union
---

# Train a DFlash block drafter

EAGLE-3 drafts one token per forward pass of its draft layer, so a draft of 3 tokens costs 3
passes. **DFlash** drafts a whole block in one pass. It is a small block-diffusion model:
starting from the last accepted token and the target's hidden states, it predicts every
position in a block of 16 in parallel. The target then verifies the block in one pass, as it
does any draft.

When the target accepts long runs, a block drafter pays for one draft pass where EAGLE-3 pays
for several. That favors code, structured output, and low-concurrency serving. When the target
rejects early in the block, the extra positions are wasted work.

This tutorial fine-tunes Red Hat's public DFlash head for Qwen3-8B, on the same dataset as
[Train an EAGLE-3 draft head](./eagle3-train).

## The DFlash recipe

Each drafter family is a recipe: the head to start from, the target layers it reads, the draft
length to serve with, and its training flags.

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/recipes.py" fragment="recipe" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/recipes.py" fragment="dflash" lang="python" >}}

- **Five target layers, not three.** DFlash reads layers 2, 10, 18, 26, and 34 of Qwen3-8B.
  The hidden-state server captures exactly the recipe's layers, and the trainer reads the
  same list, so the two can never disagree.
- **15 draft tokens.** A block of 16 positions starts with the token the target already
  produced, so vLLM serves it with `num_speculative_tokens=15`.
- **D-PACE loss weighting.** Later positions in a block are accepted only when every earlier
  one was, so they matter less. D-PACE weights each position's loss by how often it can be
  accepted.
- **Sized for one 48 GB GPU.** The hidden-state server takes 45% of the GPU, so the trainer
  gets the rest. The public head predicts over Qwen3's full 151,936-token vocabulary, and the
  logits for one 4,096-token sequence alone take 2.3 GB in fp32. The recipe trains on 2,048-token
  sequences, uses 512 anchors per sequence (positions a training block is drafted from), and
  checkpoints activations. On a 4-GPU node, raise all three.

## Train

`train_drafter` is the same task as for EAGLE-3. The `method` argument selects the recipe:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/dflash.py" fragment="main" lang="python" >}}

`build_dataset` has the same inputs as in the EAGLE-3 pipeline, so if you ran that first, every
data shard is a cache hit and this pipeline starts at training.

```bash
python dflash.py --smoke   # 20 training steps
python dflash.py           # the full run
```

The training report charts draft accuracy at each block position. Expect position 0 to be
close to EAGLE-3's first token, and accuracy to fall steadily across the block.
[Benchmark draft models](./benchmark) compares the fine-tuned drafter with the public DFlash
head and with every other family.

## Serve the DFlash drafter

`serve.py` builds the app for every family from its recipe:

```bash
python serve.py --method dflash
```

[Serve and retrain draft models](./serve-and-retrain) covers the app, the agent that sends it
traffic, and nightly retraining. Every step there takes `--method dflash`.
