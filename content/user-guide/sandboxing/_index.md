---
title: Sandboxing
weight: 21
variants: +flyte +union
llm_readable_bundle: true
---

# Sandboxing

{{< llm-bundle-note >}}

A sandbox is an isolated, secure environment where code can run without affecting the host system.
Sandboxes restrict what the executing code can do — limiting filesystem access, blocking network calls, and preventing arbitrary system operations — so that even malicious or buggy code cannot cause harm.

The exact restrictions depend on the sandboxing approach: some sandboxes eliminate dangerous operations entirely, while others provide full capabilities within an isolated, disposable container.

## Why sandboxing matters for AI

LLM-generated code is inherently untrusted.
The model may produce code that is correct and useful, but it can also produce code that is dangerous, and it does so without intent or awareness.

| Risk | Example |
|------|---------|
| Data destruction | `DELETE FROM orders WHERE 1=1` wipes an entire table |
| Credential exfiltration | Reads environment variables and sends API keys to an external endpoint |
| Infinite loops | `while True: pass` consumes CPU indefinitely |
| Resource abuse | Spawns thousands of threads or allocates unbounded memory |
| Filesystem damage | `rm -rf /` or overwrites critical configuration files |
| Network abuse | Makes unauthorized API calls, sends spam or joins a botnet |

Running LLM-generated code without a sandbox means trusting the model to never make these mistakes.
Sandboxing eliminates this trust requirement by making dangerous operations structurally impossible.

## Types of sandboxes

There are three broad approaches to sandboxing LLM-generated code, each with different tradeoffs:

| Type | How it works | Tradeoffs | Examples |
|------|-------------|-----------|----------|
| **One-shot execution** | Code runs to completion in a disposable container, then the container is discarded. Stdout, stderr, and outputs are captured. | Simple, no state reuse. Good for single-turn tasks. | Container tasks, serverless functions |
| **Interactive sessions** | A persistent VM or container where you send commands incrementally and observe results between steps. Sessions last for the lifetime of the VM. | Flexible and multi-turn, but heavier to provision and manage. | E2B, Daytona, fly.io |
| **Programmatic tool calling** | The LLM generates orchestration code that calls a predefined set of tools. The orchestration code runs in a sandbox while the tools run in full containers. | Durable, observable, and secure. Tools are known ahead of time. | Flyte workflow sandboxing |

## What {{< key product_name >}} offers

{{< key product_name >}} ship sandboxes for each of the patterns above, so the right choice is rarely "default to the heaviest option". Pick by the *shape* of the workload first, then harden if the threat model demands it.

### Workflow sandbox (Monty)

A **sandboxed orchestrator** built on [Monty](https://github.com/pydantic/monty), a Rust-based sandboxed Python interpreter.
The sandbox starts in microseconds, runs pure Python control flow, and dispatches heavy work to full container tasks through the Flyte controller.

This is how you safely run the **programmatic tool calling** (a.k.a. code mode) pattern: an LLM generates Python that calls a known set of tools, and Flyte executes the orchestration with full durability, observability and type checking. Use it when the thing you need to sandbox is the control flow.

### Code sandbox (container)

A **stateless code sandbox** that runs arbitrary Python or shell inside an ephemeral container. The container is built on demand from declared dependencies, executed once and discarded. Each invocation starts from a clean slate.

Use this when full Python capabilities are required, including third-party packages, file I/O or shell commands, and when each invocation can run independently without state reuse or a persistent live session.

{{< variant union >}}
{{< markdown >}}
### Interactive sandbox (session)

A **live, multi-turn sandbox** via `unionai-sandbox` (`union.sandbox`). You open a session, send it many commands, watch state evolve on its work dir, then close it. The session is like a long-lived machine: the work dir and a venv persist across calls, so `uv pip install` in one call is importable in the next. Network and filesystem posture are set per call, so the same session can isolate a tool call, then allow-list an install, then drop back to blocked.

Use it for agent loops, REPL-style apps, and any workflow that runs a sequence of related commands rather than a single one-shot invocation. See [Interactive sandboxes](./interactive-sandboxes/_index) for the full guide.
{{< /markdown >}}
{{< /variant >}}

### Decision matrix

{{< variant flyte >}}
{{< markdown >}}
| | Workflow sandbox (Monty) | Code sandbox (`flyte.sandbox.create()`) |
|---|---|---|
| **Shape** | One sandboxed orchestration run that fans out to tools | One sandboxed invocation, typed inputs and outputs |
| **Startup** | Microseconds | Seconds (image build, container spin-up) |
| **State** | None across runs | None across runs |
| **Capabilities** | Pure Python control flow, no imports, no I/O, no network | Full Python and shell, declared dependencies |
| **Isolation** | Structural (dangerous operations are impossible) | Container |
| **Typical use** | LLM-generated orchestration calling known tools | ETL, test runs, data processing, shell pipelines |
{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}
| | Workflow sandbox (Monty) | Code sandbox (`flyte.sandbox.create()`) | Interactive sandbox (`union.sandbox`) |
|---|---|---|---|
| **Shape** | One sandboxed orchestration run that fans out to tools | One sandboxed invocation, typed inputs and outputs | Many commands against one live session, shared filesystem |
| **Startup** | Microseconds | Seconds (image build, container spin-up) | Milliseconds (local), seconds (remote pod) |
| **State** | None across runs | None across runs | Persists on the sandbox FS across calls |
| **Capabilities** | Pure Python control flow, no imports, no I/O, no network | Full Python and shell, declared dependencies | Full Python and shell, network and FS posture set per call |
| **Isolation** | Structural (dangerous operations are impossible) | Container | bubblewrap / userns by default; gVisor on remote pods |
| **Typical use** | LLM-generated orchestration calling known tools | ETL, test runs, data processing, shell pipelines | Coding agents, multi-turn assistants, REPL-style apps |
{{< /markdown >}}
{{< /variant >}}

A short version of the same decision:

- When workload is **orchestration that fans out to tools**, use the workflow sandbox.
- When workload is **one self-contained invocation** with declared inputs and outputs, use the code sandbox.
{{< variant union >}}
{{< markdown >}}
- When workload is a **sequence of commands** that share state, stream output or need per-call security flips, use the interactive sandbox.
{{< /markdown >}}
{{< /variant >}}

Reach for the heavier isolation (dedicated pod, gVisor runtime) only when the trust level or multi-tenancy demands it. The defaults are deliberately lightweight so the common case stays fast.

### Learn more

- [Workflow sandboxing](./workflow-sandboxing-flyte). How the Monty-based sandboxed orchestrator works, with examples.
- [Programmatic tool calling for agents](./code-mode). The pattern behind code mode, and how to build agents that use it.
- [Code sandboxing](./code-sandboxing). Running arbitrary code and commands in ephemeral containers with `flyte.sandbox.create()`.
{{< variant union >}}
{{< markdown >}}
- [Interactive sandboxes](./interactive-sandboxes/_index). Live, multi-command sessions with `unionai-sandbox`.
{{< /markdown >}}
{{< /variant >}}
