---
title: Train a DSpark drafter
icon: stars
description: Train a DSpark drafter for Qwen3-8B from scratch, which adds a Markov head and a confidence head to DFlash's block drafting.
weight: 3
variants: +flyte +union
---

# Train a DSpark drafter

**DSpark** builds on DFlash's block drafting with two extra heads:

- **A Markov head.** DFlash predicts every position in a block independently, so position 5
  cannot see what was drafted at position 4. The Markov head adds a low-rank dependency
  between neighboring tokens in the block, which raises accuracy at later positions, where
  DFlash is weakest.
- **A confidence head.** It predicts, for each position, whether the target will accept it.
  The serving engine can use that to stop verifying a block at the first position that is
  likely to be rejected.

This tutorial trains a DSpark drafter for Qwen3-8B from scratch, on the same dataset as
[Train an EAGLE-3 draft head](./eagle3-train).

> [!NOTE] Why from scratch
> Public DSpark checkpoints for Qwen3-8B exist, but none carries a license that permits reuse,
> so this recipe starts from random weights. A drafter trained from scratch needs far more
> data than a fine-tune to catch up with a public head. Treat this tutorial's DSpark numbers as
> what a few thousand examples buy, not as DSpark's ceiling.

## The DSpark recipe

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/recipes.py" fragment="dspark" lang="python" >}}

- **Three draft layers and the DFlash target layers.** With no head to load, the recipe sets
  the architecture: three decoder layers reading target layers 2, 10, 18, 26, and 34. Trained
  from scratch, every draft weight carries fp32 optimizer state, so three layers and 256 anchors
  per sequence fit next to the hidden-state server on one 48 GB GPU. On a 4-GPU node, use five
  layers and more anchors.
- **A block of 8.** Shorter blocks than DFlash's 16 suit a drafter trained on little data,
  because accuracy at late positions is the last thing it learns. vLLM serves it with
  `num_speculative_tokens=7`.
- **A reduced draft vocabulary.** The draft head predicts over the 32,000 most frequent
  target tokens in the training data, which shrinks its output layer by about 5x.
  `prepare-data` computes the token frequencies.
- **A mixed loss.** Cross-entropy plus total variation distance, weighted 0.1 and 0.9.
  Total variation tracks acceptance more directly than cross-entropy does.
- **A higher learning rate and more epochs.** `3e-4` for 5 epochs, as for any model trained
  from random weights.

## Train

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/dspark.py" fragment="main" lang="python" >}}

The dataset is the same cached one as for EAGLE-3 and DFlash.

```bash
python dspark.py --smoke   # 20 training steps
python dspark.py           # the full run
```

[Benchmark draft models](./benchmark) compares the DSpark drafter with the public and
fine-tuned EAGLE-3 and DFlash drafters.

## Serve the DSpark drafter

`serve.py` builds the app for every family from its recipe:

```bash
python serve.py --method dspark
```

[Serve and retrain draft models](./serve-and-retrain) covers the app, the agent that sends it
traffic, and nightly retraining. Every step there takes `--method dspark`.

## Choose a draft model family

- **Start with EAGLE-3.** It has the most mature tooling, a public head for most popular
  targets, and holds its speedup best as concurrency rises.
- **Try DFlash for long accepted runs.** Code, JSON, and low-concurrency serving reward block
  drafting. Fine-tune a public DFlash head where one exists.
- **Train DSpark when you have the data.** Its Markov and confidence heads improve on DFlash
  at later block positions, but a head trained from scratch needs far more data than a
  fine-tune to beat a public head.
- **Measure on your own traffic.** The benchmark in these tutorials runs every family on the
  same held-out prompts and GPUs. Rank them by acceptance length and speedup on your
  workload, not on a paper's.
