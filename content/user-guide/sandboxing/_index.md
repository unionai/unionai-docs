---
title: Sandboxing
weight: 18
variants: +flyte +union
sidebar_expanded: false
llm_readable_bundle: true
---

# Sandboxing

{{< llm-bundle-note >}}

A **sandbox** is an isolated, secure environment where code can run without affecting the host system.
Sandboxes restrict what the executing code can do — limiting filesystem access, blocking network calls, and preventing arbitrary system operations — so that even malicious or buggy code cannot cause harm.

The exact restrictions depend on the sandboxing approach: some sandboxes eliminate dangerous operations entirely, while others provide full capabilities within an isolated, disposable container.

## Why sandboxing matters for AI

LLM-generated code is inherently untrusted.
The model may produce code that is correct and useful, but it can also produce code that is dangerous — and it does so without intent or awareness.

| Risk | Example |
|------|---------|
| Data destruction | `DELETE FROM orders WHERE 1=1` — wipes an entire table |
| Credential exfiltration | Reads environment variables and sends API keys to an external endpoint |
| Infinite loops | `while True: pass` — consumes CPU indefinitely |
| Resource abuse | Spawns thousands of threads or allocates unbounded memory |
| Filesystem damage | `rm -rf /` or overwrites critical configuration files |
| Network abuse | Makes unauthorized API calls, sends spam, or joins a botnet |

Running LLM-generated code without a sandbox means trusting the model to never make these mistakes.
Sandboxing eliminates this trust requirement by making dangerous operations structurally impossible.

## Types of sandboxes

There are three broad approaches to sandboxing LLM-generated code, each with different tradeoffs:

| Type | How it works | Tradeoffs | Examples |
|------|-------------|-----------|----------|
| **One-shot execution** | Code runs to completion in a disposable container, then the container is discarded. Stdout, stderr, and outputs are captured. | Simple, no state reuse. Good for single-turn tasks. | Container tasks, serverless functions |
| **Interactive sessions** | A persistent VM or container where you send commands incrementally and observe results between steps. Sessions last for the lifetime of the VM. | Flexible and multi-turn, but heavier to provision and manage. | E2B, Daytona, fly.io |
| **Programmatic tool calling** | The LLM generates orchestration code that calls a predefined set of tools. The orchestration code runs in a sandbox while the tools run in full containers. | Durable, observable, and secure. Tools are known ahead of time. | Flyte workflow sandboxing |

## What Flyte offers

Flyte provides two complementary sandboxing approaches:

### Workflow sandbox (Monty)

A **sandboxed orchestrator** built on [Monty](https://github.com/pydantic/pydantic-monty), a Rust-based sandboxed Python interpreter.
The sandbox starts in microseconds, runs pure Python control flow, and dispatches heavy work to full container tasks through the Flyte controller.

This enables the **programmatic tool calling** pattern (also known as code mode): LLMs generate Python orchestration code that invokes registered tools, and Flyte executes it safely with full durability, observability, and type checking.

### Code sandbox (container)

A **stateless code sandbox** that runs arbitrary Python scripts or shell commands inside an ephemeral Docker container.
The container is built on demand from declared dependencies, executed once, and discarded.

This is the right choice when you need full Python capabilities — third-party packages, file I/O, shell commands, or any computation that goes beyond pure control flow.

### When to use which

| | Workflow sandbox | Code sandbox |
|---|---|---|
| **Runtime** | Monty (Rust-based Python interpreter) | Ephemeral Docker container |
| **Startup** | Microseconds | Seconds (image build + container spin-up) |
| **Capabilities** | Pure Python control flow only — no imports, no I/O, no network | Full Python environment — any package, any library, full I/O |
| **Use case** | LLM-generated orchestration logic that calls registered tools | Arbitrary computation — data processing, test execution, ETL, shell pipelines |
| **State** | Runs within a worker container process | Stateless — fresh container per invocation |
| **Security model** | Dangerous operations are structurally impossible | Isolated container |

- Use the **workflow sandbox** when you need to run untrusted control flow (loops, conditionals, routing) that dispatches work to known tasks. It starts in microseconds and provides the strongest isolation guarantees.
- Use the **code sandbox** when you need full Python capabilities — third-party packages, file I/O, shell commands, or any computation that goes beyond pure control flow.

### Learn more

- [**Workflow sandboxing**](./workflow-sandboxing-flyte) — How the Monty-based sandboxed orchestrator works, with examples
- [**Programmatic tool calling for agents**](./code-mode) — The concept behind programmatic tool calling and how to build agents that use it
- [**Code sandboxing**](./code-sandboxing) — Running arbitrary code and commands in ephemeral containers with `flyte.sandbox.create()`
