---
title: Frontier AI
icon: stars
description: "The everyday workloads of frontier AI labs: pretraining, data curation for text and video, evals on every checkpoint, interpretability, and AI-driven science."
weight: 4
variants: +flyte +union
sidebar_expanded: true
---

# Frontier AI

Tutorials for the workloads of frontier AI labs.

{{< variant union >}}
{{< markdown >}}

The headline training run is a small part of what a frontier AI lab does. Most of the work
around it falls into three kinds:

- **Data factories:** turning raw web text, video, audio, or lab measurements into training data,
  with every filter versioned and every document or clip traceable to the stage that kept it.
- **Decisions from many small runs:** which checkpoint to ship, which data to keep, which
  candidate to send to an expensive experiment.
- **Continuous measurement:** benchmarks on every checkpoint, and interpretability tools that
  look inside the model.

These tutorials follow those workloads at a scale that runs in minutes, each tested end to end
on a Union cluster. Each one names the labs and papers it is modeled on.

| Tutorial | Who does this | What makes it hard at scale |
| --- | --- | --- |
| [Distributed LLM pretraining](./distributed-pretraining/_index) | Every foundation model lab | Multi-GPU training that has to survive failures and stream data |
| [Refine a pretraining corpus](./pretraining-data-refinery/_index) | Pretraining data teams, as in FineWeb-Edu, Essential-Web, and Zyda-2 | Billions of documents, CPU and GPU stages, and LLM labels that cost too much to run on everything |
| [Evaluate every checkpoint](./checkpoint-evals/_index) | Post-training and evals teams, as in OLMo and OLMES | Evals that must keep up with training without slowing it, and never re-run when nothing changed |
| [Curate a video dataset for generative video](./video-data-curation/_index) | Generative video and world-model labs, as in Open-Sora and Stable Video Diffusion | Hours of footage through decoders, scoring models, and captioners on different hardware |
| [Find features in a language model with sparse autoencoders](./sparse-autoencoders/_index) | Interpretability teams, as in Scaling Monosemanticity and Gemma Scope | Terabytes of activations, a grid of training runs, and thousands of LLM calls to label features |
| [Closed-loop molecular discovery](./closed-loop-discovery/_index) | AI-for-science labs that run autonomous experiments | A slow, failure-prone oracle, a loop that runs for days, and a scientist who approves each batch |

{{< /markdown >}}
{{< /variant >}}

{{< grid >}}

{{< link-card target="distributed-pretraining" icon="cpu" title="Distributed LLM pretraining" >}}
Pretrain large language models at scale with PyTorch Lightning, FSDP, and H200 GPUs, featuring streaming data and real-time metrics.
{{< /link-card >}}

{{< variant union >}}
{{< link-card target="pretraining-data-refinery" icon="filter" title="Refine a pretraining corpus" >}}
Turn raw web text into pretraining data with heuristic filters, global deduplication, eval decontamination, and a quality classifier distilled from LLM labels.
{{< /link-card >}}
{{< /variant >}}

{{< variant union >}}
{{< link-card target="checkpoint-evals" icon="clipboard-check" title="Evaluate every checkpoint" >}}
Publish every checkpoint of a fine-tuning run as an artifact version, let an artifact trigger run a benchmark suite on each one while training continues, and promote the checkpoint that wins a ship rule.
{{< /link-card >}}
{{< /variant >}}

{{< variant union >}}
{{< link-card target="video-data-curation" icon="film" title="Curate a video dataset for generative video" >}}
Cut long-form films into shots, score every clip for exposure, blur, on-screen text, aesthetics and motion on pools of CPU and GPU workers, caption the keepers with a small vision-language model, and publish the result as a dataset artifact.
{{< /link-card >}}
{{< /variant >}}

{{< variant union >}}
{{< link-card target="sparse-autoencoders" icon="search" title="Find features in a language model with sparse autoencoders" >}}
Harvest a language model's activations once, train a grid of TopK sparse autoencoders in parallel on GPUs, and have Claude label and score the features they find.
{{< /link-card >}}
{{< /variant >}}

{{< variant union >}}
{{< link-card target="closed-loop-discovery" icon="eyedropper" title="Closed-loop molecular discovery" >}}
An active learning loop where a surrogate model proposes molecules, a quantum chemistry oracle measures them on a warm CPU pool, and a scientist approves each batch before it runs.
{{< /link-card >}}
{{< /variant >}}

{{< /grid >}}

## Related

- [Reinforcement learning](../reinforcement-learning/_index): RL for LLMs, agents, robots, and games, including durable agentic RL with SkyRL and Harbor.
- [Speculative decoding models](../speculative-decoding/_index): train and serve draft models that make an LLM generate faster.
