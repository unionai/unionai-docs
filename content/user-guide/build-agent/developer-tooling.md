---
title: Developer tooling
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
mermaid: true
---

# Developer tooling

## Migrating from V1 to V2

For teams already on Union V1, there's a migration context file that's been helping other customers convert workflows to V2 (often in a single pass with Claude). **See [`FLYTE_V1_TO_V2_MIGRATION_CONTEXT.md`](https://gist.github.com/LeonKolyang/2151397b78e30e7ea8f717a6702f47f1).**

Key V1 to V2 changes:
- V2 is **pure Python**, with no YAML and no separate workflow decorator
- Tasks call tasks directly (async/await)
- App serving is built-in with `flyte.serve()`
- Better local development and debugging experience

> [!TIP]
> See the migration guide: [From Flyte 1 to 2](https://www.union.ai/docs/v2/byoc/user-guide/flyte-2/).

## Claude Code agents and MCP

Union provides four specialist Claude Code agents that teams can drop into their workflow. Each agent is a markdown file with a system prompt that turns Claude into a domain expert. They're available at [`unionai/claude-agents-public`](https://github.com/unionai/claude-agents-public):

| Agent | What it does |
|-------|-------------|
| **Flyte Expert** | Designs and generates Flyte 2.0 workflows, tasks, and apps. Knows async patterns, container strategies, environment setup, app serving, and traces. Start here for any "how do I build X on Union?" question. |
| **Deep Learning Engineer** | PyTorch model development, training optimization, distributed training (Accelerate), HuggingFace integration, and inference serving. Useful for teams building ML pipelines on Union. |
| **GPU Optimization Expert** | CUDA/TPU/Trainium performance tuning, hardware selection, memory optimization, mixed precision, and profiling. Helps teams get the most out of Union's GPU resources. |
| **Distributed Systems Safety Auditor** | Rigorous safety/liveness analysis of distributed code, identifying race conditions, deadlocks, and failure cascades. Runs on Claude Opus for maximum reasoning depth. |

**Setup:** Clone the repo, then copy the agent `.md` files into your Claude Code project's `.claude/agents/` directory. Once installed, Claude Code can invoke them by name for specialized tasks (e.g., ask Claude to "use the flyte-expert agent to design a training pipeline").

**Context7 / MCP:** Flyte docs are already available on [Context7](https://context7.com) as an MCP service, which lets Claude fetch up-to-date docs without web searches. Union-specific docs aren't yet published there; this is on our TODO list. In the meantime, Claude is generally good at finding Union/Flyte documentation autonomously.
