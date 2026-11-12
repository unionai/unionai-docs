---
title: Can a LoRA screen pick the right RL ablation?
icon: sliders
description: Train the same GRPO loss-aggregation arms as LoRA adapters and at full weight, one durable action per arm, and check whether the two rankings agree.
weight: 7
variants: -flyte +union
---

# Can a LoRA screen pick the right RL ablation?

An RL ablation table is expensive when every row is a full-weight run. A cheaper screen, such as LoRA arms on a small model, is only useful if it ranks the rows the same way the full-weight runs do. This tutorial runs that check for one ablation: how the GRPO policy loss is averaged over a batch.

- **`token_mean`** pools every token in the batch, so long completions carry more of the gradient.
- **`sequence_mean`** weights every completion equally, whatever its length (original GRPO).
- **`prompt_mean`** weights every prompt group equally and pools tokens within a group (DAPO-style).

Mercor's 397B SkyRL guide picked `prompt_mean` from 13 full-weight ablations on a 35B model, where trajectories ran from 2k to 128k tokens. This tutorial runs the same three choices on Qwen3-0.6B and GSM8K, once with LoRA and once at full weight, and reports whether the rankings match. It tests the method on a cheap proxy. A 0.6B model on single-turn math says nothing about long-horizon agentic RL.

> [!NOTE]
> Full code is available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/lora_ablation_screen).
> The default screen runs 12 arms (3 aggregations, 2 modes, 2 seeds), each on one `L4` GPU. Set `SCREEN_GPU_TYPE` to use another GPU type.
> You need a Hugging Face token stored as a secret named `HF_TOKEN`.

## Run it

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/lora_ablation_screen
python lora_screen.py
```

## An arm is a row of the ablation table

Everything that defines an arm is a field on `Arm`, so the arm is its own cache key. LoRA and full weight differ only in `mode` and learning rate.

{{< code file="/unionai-examples/v2/tutorials/lora_ablation_screen/lora_screen.py" fragment="arms" lang="python" >}}

LoRA arms use a learning rate 10 times the full-weight rate, following Thinking Machines' "LoRA Without Regret." LoRA targets every linear layer, attention and MLP.

## The loss aggregations

The three arms differ only in the per-sequence weight applied to the policy-gradient term. Each weighting keeps the loss on the same scale, so the arms share a learning rate within a mode.

{{< code file="/unionai-examples/v2/tutorials/lora_ablation_screen/lora_screen.py" fragment="aggregation" lang="python" >}}

## One arm, one durable action

`train_arm` runs a whole arm on one GPU: sample, score, take one GRPO step with the arm's aggregation, repeat, then evaluate greedily on held-out questions.

{{< code file="/unionai-examples/v2/tutorials/lora_ablation_screen/lora_screen.py" fragment="train_arm" lang="python" >}}

Three details matter for a fair comparison:

- **Token-in, token-out.** vLLM returns the prompt and completion token IDs it sampled, and the trainer computes log-probabilities over exactly those IDs. Nothing is re-tokenized.
- **vLLM runs in a subprocess.** Each step starts vLLM, samples, and exits, so the sampler releases its GPU memory before training. A LoRA arm loads the base model plus the adapter. A full-weight arm loads the whole updated model. The report shows the per-step cost of each.
- **fp32 master weights for full-weight arms.** A full-weight update at a learning rate of `2e-6` is too small to represent in bf16. LoRA arms keep the frozen base in bf16 and train fp32 adapters.

The task has `cache="auto"` and `retries=2`. A failed arm retries on its own without touching the other arms. A finished arm comes back from the cache when you rerun the screen.

## The screen

`screen` fans out the arms in parallel, evaluates the base model once, and computes the ranking under each mode and Kendall's τ between them.

{{< code file="/unionai-examples/v2/tutorials/lora_ablation_screen/lora_screen.py" fragment="screen" lang="python" >}}

A failed arm leaves a gap in the table instead of failing the screen. Add an arm to the list and rerun, and only the new arm trains.

## Results

Qwen3-0.6B on `L4` GPUs, 20 GRPO steps of 16 prompts × 8 samples, greedy evaluation on 300 held-out GSM8K questions. The standard error is about 2.9 points per arm. The base model scores 37.7%.

| Aggregation | Full weight, seed 0 / 1 → mean | LoRA, seed 0 / 1 → mean |
| --- | --- | --- |
| `prompt_mean` | 61.7% / 59.0% → 60.3% | 45.3% / 56.0% → 50.7% |
| `token_mean` | 54.3% / 58.3% → 56.3% | 49.3% / 51.0% → 50.2% |
| `sequence_mean` | 52.3% / 56.7% → 54.5% | 49.3% / 53.7% → 51.5% |

- **Full weight ranks `prompt_mean` first.** Both of its seeds beat every seed of the other two arms.
- **LoRA doesn't pick the same winner.** Its three arms are within 1.3 points of each other, and its two seeds of `prompt_mean` differ by 10.7 points. Kendall's τ between the two rankings is −0.33.
- **LoRA arms learn less in the same step budget**: 50.8% mean held-out accuracy against 57.0%. The LoRA learning rate isn't tuned here.

Per arm, a full-weight step averages 18 seconds of engine start, 17 seconds of sampling, and 26 seconds of training, and writes 2.4 GB of policy. A LoRA step averages 19, 30, and 34 seconds and writes 40 MB. At this model size, LoRA saves memory and bytes moved, not wall-clock time.

### Measure the noise floor first

If every completion reaches `max_tokens`, every sequence has the same length and the three aggregations compute the same loss. Without stop strings, Qwen3-0.6B writes the answer and keeps generating until the limit. A screen run that way is an A/A test. In one such run, full-weight arms with an identical loss still spread from 49.0% to 58.0% held-out accuracy. Run the screen with identical arms before you trust a ranking from it.

`ScreenConfig.stop` ends each completion after the answer. Because `stop` is a field on an input, changing it invalidates the cached arms. A change inside `vllm_generate.py` alone wouldn't.

## Related

- [RL for LLMs with GRPO and LoRA](../grpo-lora/_index) builds a single-arm GRPO loop with a warm vLLM pool.
- [Harness evals and trace audits for agentic RL](../agentic-rl-evals/_index) covers the eval side of the same campaign.
