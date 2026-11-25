---
title: Rubric rewards and checkpoints on Harvey's LAB
icon: briefcase
description: Run Harvey's Legal Agent Benchmark through Flyte on US open-weight models, audit what a rubric reward pays for and how noisy its judge is, test whether padding buys rubric points, and pick a checkpoint with a cached eval matrix and a pairwise tournament.
weight: 8
variants: -flyte +union
---

# Rubric rewards and checkpoints on Harvey's LAB

Harvey's [Tenet recipe on US open-weight models](https://www.harvey.ai/blog/applying-the-harvey-tenet-training-recipe-to-us-open-weight-models) trains legal agents with reinforcement learning against an LLM judge that grades expert rubrics. The reward is `0.35 c + 0.35 h + 0.30 a`: the fraction of criteria passed, the fraction of issue groups passed in full, and an all-pass bonus, with zero for an episode cut off by its turn or context limit. The training tasks come from Harvey's [Legal Agent Benchmark](https://github.com/harveyai/harvey-labs) (LAB): 2,010 legal tasks with about 114,000 pass/fail criteria, an agent harness, and a grader, all MIT-licensed.

This tutorial runs LAB itself, through Flyte, with US open-weight models served by vLLM on the same GPU node, and asks four questions about that kind of reward:

1. Which term of the reward actually moves a GRPO advantage, and how much of it is judge noise?
2. Does the rubric pay for padding, and does a pairwise judge agree?
3. What changes across checkpoints when you train against it?
4. How many pairwise judgments does it take to call a preference result a null?

It is not a replication of Harvey's results. LAB publishes no hold-out split, so the tasks are a seeded sample; the judges are open-weight models; the policies are 20B–120B; and episodes are capped at a few dozen turns. The training run stopped after seven steps, so the checkpoint matrix below is shown with base policies.

> [!NOTE]
> Full code is available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/legal_agent_rl).
> The rollouts and training were run on one 8× AMD Instinct MI355X node from a GPU market, reached through a queue; grading and the probes ran on NVIDIA L4 and L40S GPUs.
> The calibration step uses LAB's standard hosted judges and needs secrets named `ANTHROPIC_API_KEY` and `OPENAI_API_KEY`.

## Run it

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/legal_agent_rl
export CLUSTER=amd GPU_QUEUE=<your GPU queue>   # or CLUSTER=demo for one NVIDIA GPU
python smoke.py                                  # one rollout per model, both judges, one LoRA step
python sweep.py --tasks 48 --samples 8           # base rollouts and grades
python audit.py --sweep-run <run>                # the reward and judge audit, on CPU
python grade_shards.py --rollouts sweep_rollouts.jsonl.gz   # grade existing rollouts anywhere, one GPU per shard
python grade_shards.py merge --rollouts sweep_rollouts.jsonl.gz --runs <run>   # merge shard verdicts, print the audit
python probes.py variants --rollouts sweep_rollouts.jsonl.gz # padding probe
python probes.py pairs --rollouts sweep_rollouts.jsonl.gz    # pairwise tournament and A/A test
python diag.py                                   # does the trainer agree with the sampler?
python train.py                                  # checkpoints
python checkpoints.py --train-run <run>          # checkpoint matrix and tournament
```

## LAB in a pod

LAB runs each agent in its own `--network=none` Podman container. A Kubernetes pod can't start containers, so the GPU image is built from LAB's own sandbox image, and `PodSandbox` implements LAB's sandbox interface over a private directory per rollout. The agent still sees LAB's canonical paths (`/workspace`, `/workspace/documents`, `/workspace/output`) and LAB's tools, system prompt, skills and agent loop, unchanged.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/lab_harness.py" fragment="pod_sandbox" lang="python" >}}

Two differences from LAB's own runs follow from this, and both are worth stating: the pod has a network, and several rollouts share one container.

The images start from that sandbox image and add vLLM. vLLM publishes ROCm wheels, so the AMD image comes from Flyte's builder like the CUDA one, without a `vllm serve` entrypoint to work around:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/images.py" fragment="images" lang="python" >}}

## One rollout

A rollout is one agent episode on one LAB task. The adapter is LAB's OpenAI-compatible one, extended to ask vLLM for the token IDs and log-probabilities it sampled, so the same rollout can be used for training without re-tokenizing.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/lab_harness.py" fragment="rollout" lang="python" >}}

Grading is LAB's `score_rubric`, unchanged. The only new piece is a judge that sends LAB's `rubric_criterion` prompt to an OpenAI-compatible server, so a rubric can be graded by an open-weight model on the same node. The reward terms follow Harvey's post:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/lab_harness.py" fragment="reward" lang="python" >}}

LAB's public rubrics have no issue-group field, so the sweep asks the judge model to group each task's criteria by legal issue, once per task. That grouping is a stand-in for Harvey's, not theirs.

## A sweep on a node that can be taken back

The GPU market grants whole nodes and can take one back at any time. The sweep is one task per node, and every rollout and every grade inside it is a `@flyte.trace`:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/sweep.py" fragment="traced" lang="python" >}}

When the task retries on a new node, finished rollouts and grades replay from the record and only the rest run. The task is cached on its config, so asking for the same sweep twice costs nothing.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/sweep.py" fragment="sweep" lang="python" >}}

On one 8× MI355X node, three US open-weight models (`gpt-oss-120b`, `gpt-oss-20b`, `Nemotron-3-Nano-30B-A3B`) ran 48 LAB tasks × 8 rollouts in 96 minutes: 1,152 episodes launched, 1,151 finished. The grading step ran separately, on NVIDIA L4 GPUs on another cluster, from the same rollouts.

| Policy | Criteria passed | All-pass | Cut off | No deliverable | Median turns |
| --- | --- | --- | --- | --- | --- |
| gpt-oss-120b | 31.0% | 0 of 384 | 0.3% | 5.5% | 12 |
| Nemotron 3 Nano 30B | 13.0% | 0 of 384 | 7.3% | 34.6% | 23 |
| gpt-oss-20b | 11.6% | 0 of 383 | 2.1% | 12.5% | 15 |

## What the reward pays for

The trainer never sees the reward's terms on their own. It sees each rollout's advantage: its reward minus its group's mean. So `reward_audit.py` asks, within each group of G rollouts of one task, how much of the reward's variance comes from each term. Each term's share is `Cov(part, R) / Var(R)`, and the shares sum to 1.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/reward_audit.py" fragment="term_shares" lang="python" >}}

Judge noise is measured the same way: re-grade the same rollouts and compare how much a rollout's reward moves between gradings with how much rewards differ within its group.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/reward_audit.py" fragment="judge_noise" lang="python" >}}

The audit is CPU work over verdicts that are already paid for, so changing the weights is a new run of `audit.py`, not a new sweep.

With `gpt-oss-20b` as the judge, no rollout passed every criterion, so the all-pass term was constant in all 144 groups and carried none of the advantage. Criteria carried 60–69% of within-group reward variance and issue groups 28–40%. Re-grading flipped 2.4–4.7% of criterion verdicts, a median of 1–4% of the group signal (7–14% at the 90th percentile). A second judge from another family, `Nemotron-3-Nano-4B`, agreed on 90% of 41,196 criterion verdicts (Cohen's kappa 0.70) and was more lenient (25% of criteria passed against 19%), and the gpt-oss judge showed no preference for its own family.

## Does the rubric pay for padding?

`padding.py` takes real deliverables and appends four plausible but non-responsive issues, either generic cautions or matter-specific speculation, then grades each variant with the rubric and compares it with the unpadded draft in both orders:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/preference.py" fragment="both_orders" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/padding.py" fragment="summarize" lang="python" >}}

On 94 deliverables from `gpt-oss-120b`, padding added 10–14% to each and raised criteria passed by about half a point (+0.52 generic, +0.51 speculative, on a 33.0% baseline), against a re-grading noise of 3.9 points. Pairwise, `gpt-oss-20b` picked whichever draft it saw first in more than 90% of judgments; `Nemotron-3-Nano-4B` split the speculative pairs 17–17.

## Training to make checkpoints

`train.py` uses the loss Harvey describes: rank-64 LoRA, CISPO's clipped, gradient-free importance weight, Dr. GRPO's advantage and constant normalizer (`T0 = 55,000`), G = 8, and only model-generated tokens in the loss.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/train.py" fragment="cispo" lang="python" >}}

Each turn's prompt is the conversation as the server rendered it, so a rollout becomes one training sequence per run of turns whose prompts extend each other:

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/train.py" fragment="merge" lang="python" >}}

Things that differ from the published recipe, and why:

- **Synchronous, not asynchronous.** Sample, grade, one optimizer step, repeat. The importance weight corrects train/inference numerics, not staleness.
- **A bf16 copy of gpt-oss-20b.** vLLM's LoRA path for gpt-oss's MXFP4 weights builds an emulation kernel at startup that a pip-installed ROCm stack can't compile, so the policy is dequantized once and served and trained in bf16.
- **LoRA on the attention projections.** Harvey's adapter covers the whole network, routed experts included. Expert LoRA only fits 16k-token sequences on this stack, and attention projections are the layers vLLM hot-loads for gpt-oss.
- **Four data-parallel trainer ranks** on the node's last four GPUs, with the adapter's gradients all-reduced.

The first run's importance ratio averaged 0.33 with 99% of tokens clipped: Transformers had silently re-initialized gpt-oss's expert weights when loading the dequantized copy. `diag.py` compares the trainer's log-probabilities with vLLM's on real turns; after loading the original checkpoint and dequantizing in memory, the two agreed (−0.3508 against −0.3500), and the ratio stayed at 0.997–1.001 over seven steps.

## A checkpoint matrix of cached cells

Picking a checkpoint is a matrix: checkpoints down one side, eval suites across the top. Every cell is its own cached task in a reusable environment, so the cells share one warm node, the policy server holds every checkpoint as a LoRA adapter, and a new checkpoint or a new suite runs only its new cells.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/checkpoints.py" fragment="reusable" lang="python" >}}

The tournament is cells too: one per pair of checkpoints, sample-matched, both orders, including an A/A pair of a checkpoint against itself.

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/checkpoints.py" fragment="pair_cell" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/legal_agent_rl/preference.py" fragment="bradley_terry" lang="python" >}}

Run on base policies rather than checkpoints, the tournament gave: the first-shown draft won 69% (`gpt-oss-20b` judge) and 60% (`Nemotron-3-Nano-4B` judge) of judgments; an A/A pair scored 0.54 (0.46–0.61) and 0.56 (0.48–0.64); and `gpt-oss-120b` beat the other two at 0.81–0.87 under both judges, with no preference for a judge's own model family. A sign test needs 783 decided pairs to tell a 55/45 preference from 50/50 (`preference.pairs_needed`).

## Things this example hit

- **aiter compiles at first use.** On a pip-installed ROCm stack, vLLM's aiter kernels fail their runtime build and the engine dies on the first request. `servers.py` sets `VLLM_ROCM_USE_AITER=0`.
- **Every model needs its tool-call parser.** `--enable-auto-tool-choice` without `--tool-call-parser` exits at startup; `servers.PARSERS` holds the ones used here.
- **A custom base image needs Flyte in its own interpreter.** Building from LAB's sandbox image put Flyte in a separate virtual environment the entrypoint couldn't find; installing into the image's Python fixes it and keeps `lab_core` next to the agent's document tools.
- **A dequantized MoE checkpoint can load with missing weights.** Saving gpt-oss's dequantized weights and reading them back with Transformers re-initialized the experts without an error. vLLM read the same files correctly.
- **Not every model is an agent in this harness.** Olmo 3 7B Instruct answered in prose instead of calling tools, and vLLM 0.34 doesn't support Inkling 2 Mini's architecture yet.
- **Whole-node GPU pools.** GPUs go in a pod template, every task in the run goes to the pool's queue, and images are built off-queue and pinned.
