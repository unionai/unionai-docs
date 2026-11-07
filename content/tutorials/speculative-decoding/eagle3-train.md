---
title: Train an EAGLE-3 draft head
icon: cpu
description: Generate training data with the target model itself, then fine-tune the public EAGLE-3 head for Qwen3-8B in online mode.
weight: 1
variants: +flyte +union
---

# Train an EAGLE-3 draft head

A draft head learns to predict what the **target** model will say next. Its training data
must therefore be the target's own output, not human-written responses. This page builds
that data, chat and agent traces, with Qwen3-8B itself, then fine-tunes the public EAGLE-3
head on it.

## Configure models and hardware

Everything that changes between clusters lives in `config.py`.

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/config.py" fragment="models" lang="python" >}}

The pipeline starts from `RedHatAI/Qwen3-8B-speculator.eagle3`, a general-purpose EAGLE-3
head trained by Red Hat. Fine-tuning it on your traffic is cheaper than training a head from
scratch and keeps its general drafting ability. Set `init_from=""` on `train_drafter` to
train from scratch instead. The same task trains the [DFlash](./dflash) and [DSpark](./dspark)
drafters with a different `method`.

One GPU image runs vLLM for data generation, serving, and benchmarks, and `speculators` for
training:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/config.py" fragment="images" lang="python" >}}

vLLM 0.33 and `speculators` 0.9 can share one environment because they agree on torch 2.14
and transformers 5.16 to 5.19. Pin all three. A newer transformers release can break that
overlap.

Resource requests are sized to the nodes they land on. A request above a node's
allocatable CPU or memory never schedules, even when the GPU is free:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/config.py" fragment="resources" lang="python" >}}

`TRAIN_NUM_GPUS` picks the training layout. With `1`, the hidden-state server and the
trainer share one 48 GB GPU, which fits any cluster that can serve the model. With `4`, the
task takes a whole 4-GPU node: two GPUs serve hidden states and two train, which is several
times faster.

Each stage gets an environment sized for its work:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/config.py" fragment="envs" lang="python" >}}

`generate_env` is a reusable environment. Up to four replicas stay alive between tasks, so
the vLLM server a replica starts for its first shard serves every later shard too. Loading
Qwen3-8B and capturing CUDA graphs takes several minutes, which would otherwise repeat for
every shard.

## Collect target-generated data

### Sample prompts

`prepare_prompts` samples UltraChat conversations for general chat and ToolACE tasks for
agent traffic, and splits each into shards:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/data.py" fragment="prepare-prompts" lang="python" >}}

ToolACE is split three ways in `workloads.py`. The first 60% is initial training data, the
next 20% stands in for production traffic in the retraining loop, and the last 20% is held
out for benchmarks. No benchmark prompt is ever trained on.

### Regenerate chat responses

`speculators regenerate-responses` sends each conversation to Qwen3-8B and writes the
response in tokenized form, with a loss mask over the assistant tokens:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/data.py" fragment="regenerate" lang="python" >}}

The sampling temperature is 0.7, not 0. A head trained only on greedy outputs drafts poorly
for requests served with sampling. Thinking is disabled because this tutorial's traffic
runs without it. If your application uses Qwen3's thinking mode, regenerate with it on so
the head learns to draft reasoning too.

### Record agent traces

ToolACE rows carry tool schemas, a user request, and recorded tool results. The agent sends
the request and the tools to Qwen3-8B, and when the model calls a tool, replays the recorded
result:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/workloads.py" fragment="agent" lang="python" >}}

Each episode becomes one trace: the full conversation in OpenAI chat format plus the tool
schemas. Every assistant turn in it is target output, including the JSON tool-call
arguments.

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/data.py" fragment="agent-traces" lang="python" >}}

### Report what each shard produced

Each generation task returns a `Shard`: the data file plus counts the later stages and
reports use, so nothing downstream has to re-read the file to know what is in it:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/data.py" fragment="shard" lang="python" >}}

Every data task also renders a report:

- `prepare_prompts` shows the sampled prompts: counts, prompt lengths, and tools per agent
  task.
- `regenerate_chat` shows each shard's rows, target-written tokens, and response length
  distribution, with sample rows as the trainer sees them after the chat template.
- `collect_agent_traces` shows episodes, tool-call rate, turns per episode, and the most
  called tools, with a rendered example episode.
- `build_dataset` shows the final mix: chat against agent tokens, and per-shard totals.

Check these before you spend GPU hours on training. A shard with many failed episodes or a
response length distribution piled up at `--max-tokens` means the data, not the trainer,
needs fixing.

### Fan out the shards

`build_dataset` runs the chat and agent shards concurrently:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/data.py" fragment="build-dataset" lang="python" >}}

`prepare_prompts`, `regenerate_chat`, and `collect_agent_traces` all use `cache="auto"`. A
second pipeline run with the same data sizes reuses every shard and goes straight to
training.

## Fine-tune the head in online mode

EAGLE-3 trains on the target's hidden states from three layers. Precomputing them offline
costs about 32 KB per token for an 8B model, which is terabytes for a dataset of a few
hundred million tokens. In **online mode**, a vLLM server computes hidden states on demand
and the trainer consumes and discards them.

The hidden-state server is ordinary `vllm serve` with two extra flags. One tells vLLM which
of the target's layers to capture. The other attaches a connector that writes them to a
shared path for every request:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/vllm_server.py" fragment="hidden-states" lang="python" >}}

What to train is a recipe. The EAGLE-3 recipe names the public head to start from, the
three target layers it reads, its serving draft length, and its training flags:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/recipes.py" fragment="eagle3" lang="python" >}}

`train_drafter` starts that server, then runs the trainer with `torchrun` against it. On
`/dev/shm`, hidden states move between the two processes through memory and are deleted as
soon as the trainer reads them:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/train.py" fragment="train" lang="python" >}}

The trainer prints one metric line per optimizer step. `run_and_chart` streams those lines,
parses them, and refreshes the task's report every 20 seconds:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/train.py" fragment="stream" lang="python" >}}

The report charts training loss and draft accuracy at each position, tabulates validation
metrics per epoch, and records the configuration. Position 0 is the first drafted token.
Each later position counts only when every earlier one was accepted, so acceptance length
is roughly `1 + acc0 + acc0 × acc1 + …`. Watch position 0: if it does not rise above the
public head's starting point, more training will not help.

Things to know about the training settings:

- **Two kinds of training data, one dataset.** Regenerated chat files are already
  tokenized. Agent traces are raw conversations, which `prepare-data` renders through the
  vLLM server's chat template endpoint, tool schemas included. `prepare_data` prepares each
  kind separately and merges them, and the task fails if fewer rows come out than went in:

  {{< code file="/unionai-examples/v2/tutorials/speculative_decoding/train.py" fragment="prepare" lang="python" >}}

  Rendering conversations that carry tool schemas needs vLLM's tool-calling flags on the
  hidden-state server. Without them, every agent trace fails to render, and without the row
  check, training would silently run on chat data alone.
- **The training-time-test depth is 3.** The draft is unrolled on its own predictions
  for `--ttt-steps` steps. Match it to `num_speculative_tokens` at serving time, or raise it
  for math and code, where longer drafts get accepted.
- **The learning rate is low for fine-tuning.** `5e-5` adapts the public head without
  erasing it. Training from scratch uses about `1e-4` and several epochs.
- **Only the config and weights are uploaded.** The returned `Dir` is the format vLLM loads
  with `--speculative-config`, so the serving app and benchmarks consume it directly.

## Run the pipeline

`main` generates the dataset and fine-tunes the head:

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/pipeline.py" fragment="main" lang="python" >}}

{{< code file="/unionai-examples/v2/tutorials/speculative_decoding/pipeline.py" fragment="run" lang="python" >}}

Start with a smoke run, which uses 64 prompts per source and 20 training steps:

```bash
python pipeline.py --smoke
```

Then run the full pipeline:

```bash
python pipeline.py
```

`train_drafter` is cached along with the data, so rerunning with the same inputs returns the
trained head immediately. Changing a training argument reruns only training.
[Benchmark draft models](./benchmark) measures the head against the other families.
