---
title: Benchmark draft models
icon: speedometer2
description: Benchmark EAGLE-3, DFlash, and DSpark drafters against no speculation and draft-free methods on identical GPUs, and verify that outputs and GSM8K accuracy are unchanged.
weight: 4
variants: +flyte +union
---

# Benchmark draft models

A speculative decoding claim needs two numbers: how much faster the target decodes, and
evidence that its outputs did not change. This page benchmarks eight ways of serving
Qwen3-8B on identical GPUs, covering every draft model family in these tutorials, and checks
both.

## Compare eight configurations

| Configuration | What drafts | Training |
| --- | --- | --- |
| `baseline` | Nothing. The target decodes one token per forward pass. | None |
| `ngram` | Matching n-grams copied from the prompt | None |
| `suffix` | A suffix tree over the prompt and earlier responses | None |
| `eagle3-public` | Red Hat's general-purpose EAGLE-3 head | Pretrained |
| `eagle3-finetuned` | The head from [Train an EAGLE-3 draft head](./eagle3-train) | Fine-tuned here |
| `dflash-public` | Red Hat's general-purpose DFlash head | Pretrained |
| `dflash-finetuned` | The drafter from [Train a DFlash block drafter](./dflash) | Fine-tuned here |
| `dspark-trained` | The drafter from [Train a DSpark drafter](./dspark) | From scratch here |

The two draft-free methods matter as baselines. On repetitive traffic, they can match or beat
a learned drafter without any training, so a learned drafter has to earn its place.

`compare` trains a drafter of every family, then benchmarks all eight configurations:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/compare.py" fragment="compare" lang="python" >}}

`train_drafter` is cached. If you already ran `pipeline.py`, `dflash.py`, and `dspark.py`,
`compare` calls it with the same data and arguments, reuses all three drafters, and goes
straight to the benchmarks. Otherwise it trains the three in parallel, each on its own GPU.

Each configuration is a `ServerConfig`. A drafter configuration takes its draft length from
its family's recipe:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/benchmark.py" fragment="configs" lang="python" >}}

## Measure on held-out prompts

`prepare_benchmark_prompts` draws three workloads that the training data never touched:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/benchmark.py" fragment="prompts" lang="python" >}}

- **chat**: first-turn MT-Bench prompts, the standard for reporting acceptance length.
- **agent**: held-out ToolACE requests with their tool schemas. The response is usually a
  JSON tool call.
- **math**: GSM8K test questions, which also have checkable answers.

## Run one configuration per GPU

`benchmark_server` starts vLLM with one configuration, warms it up, and replays every
workload at concurrency 1, 4, and 16:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/benchmark.py" fragment="benchmark" lang="python" >}}

Each request streams, so the task records time to first token (TTFT), time per output token
(TPOT), and decode speed per request. Before and after each pass, it reads vLLM's speculative
decoding counters and takes the difference:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/vllm_server.py" fragment="metrics" lang="python" >}}

**Mean acceptance length** is `1 + accepted / drafts`: the tokens each target forward pass
produces, counting the one token the target always contributes. It is the headline draft
quality metric because it does not depend on how many tokens the drafter proposes.
Acceptance rate, `accepted / proposed`, falls as you propose more tokens even when the
drafter improves.

> [!WARNING] Never replay a prompt a caching method has seen
> Suffix decoding caches earlier responses and drafts from them. Replaying the same prompts
> at each concurrency level lets it draft the exact greedy answer it already produced. In an
> early version of this benchmark, that inflated its acceptance length from about 1.5 to 8.5.
> Each concurrency level here gets its own slice of prompts, and warm-up uses a prompt
> outside every workload.

`run_benchmarks` runs all eight configurations at once, each on its own GPU, and compares
them in a report:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/compare.py" fragment="run-benchmarks" lang="python" >}}

```bash
python compare.py --smoke   # 20 training steps, 12 prompts per workload
python compare.py           # the full run
```

## Verify that outputs are unchanged

Speculative sampling is lossless in theory: every accepted token is one the target would
have produced. In practice, three checks confirm it:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/report.py" fragment="summarize" lang="python" >}}

- **Agreement with the baseline.** At temperature 0, each configuration's outputs are
  compared with the baseline's, prompt by prompt: whether they match exactly, and how much
  of each output matches before the first differing character.
- **The noise floor.** The baseline replays its own prompts at concurrency 16 and is compared
  with itself the same way. Batched GPU kernels are not bit-identical across batch sizes, and
  over a few hundred tokens one rounding difference flips a token and the texts diverge. A
  lossless configuration agrees with the baseline about as well as the baseline agrees with
  itself, which on most GPUs is well below 100%.
- **Task accuracy.** GSM8K accuracy should be the same within noise for every
  configuration. This is the check that matters most, because two greedy paths that diverge
  after a rounding difference are usually both correct, while a broken drafter or verifier
  costs accuracy.

> [!NOTE] Bit-exact comparisons need batch-invariant kernels
> vLLM's `VLLM_BATCH_INVARIANT=1` makes outputs independent of batch size on Hopper and newer
> GPUs, at a throughput cost. Without it, expect exact match well below 100% for every
> configuration, including the baseline against itself.

## Read the results

- **Speedup shrinks with concurrency.** At concurrency 1, the GPU is mostly idle while it
  waits on memory, so verifying draft tokens is nearly free. As concurrency rises, that idle
  compute fills with other requests and speculation's advantage narrows. Block drafters,
  which verify more tokens per step, lose their advantage first.
- **Agent traffic drafts best.** Tool calls repeat tool names and argument names from the
  schema, and JSON syntax is predictable, so drafters accept more tokens there.
- **Fine-tuning helps where traffic differs from a public head's training data.** The gap
  between each family's public and fine-tuned configuration is the value of training on your
  traffic. [Serve and retrain draft models](./serve-and-retrain) keeps that gap
  open as traffic changes.
- **Compare families at the same concurrency you serve.** A family that wins at
  concurrency 1 can lose at 16. Pick the one that wins where your traffic runs.
