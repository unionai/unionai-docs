---
title: AutoSec researcher agent
weight: 3
variants: +flyte +union
---

# AutoSec researcher agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/autosec_research_agent).

This tutorial demonstrates an autonomous security-research agent on Flyte. The pipeline fans out across bundled C source files (each with a planted memory-corruption bug), runs static analysis, uses a `flyte.ai.agents.Agent` to hypothesize vulnerabilities, builds proof-of-concept payloads, and validates exploits inside an on-device [unionai-sandbox](https://www.union.ai/docs/v2/union/user-guide/sandboxing/interactive-sandboxes/) user-namespace session.

Flyte provides:

- **Parallel fan-out** across every target file with `asyncio.gather`
- **Self-healing tasks** — LLM timeouts, malformed JSON, and OOM during static analysis retry with bounded resources
- **Sandbox isolation** — PoC compilation and execution never runs on the orchestration node
- **Live HTML reports** with per-target detail tabs in the Flyte UI

> [!WARNING]
> This example analyzes deliberately vulnerable C code and runs generated exploit payloads in a sandbox. Use it only in controlled environments.

## Define the task environment

The agent needs an Anthropic API key and a container image with `gcc` for sandbox compilation.

{{< code file="/unionai-examples/v2/tutorials/autosec_research_agent/main.py" fragment=env lang=python >}}

The Python packages are declared at the top of the file using the `uv` script style:

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "unionai-sandbox",
#    "litellm",
# ]
# ///
```

## Run the security pipeline

Each target flows through four stages: static scan, LLM hypothesis, PoC construction, and sandbox validation. The `run_autosec_agent` driver task analyzes all bundled targets in parallel and streams a findings report.

{{< code file="/unionai-examples/v2/tutorials/autosec_research_agent/main.py" fragment=pipeline lang=python >}}

## Run the agent

### Create secrets

Get an Anthropic API key from the [Anthropic console](https://console.anthropic.com/) and register it as a Flyte secret:

```
flyte create secret internal-anthropic-api-key <YOUR_ANTHROPIC_API_KEY>
```

See [Secrets](../../../user-guide/task-configuration/secrets) for scoping and file-based secrets.

### Run remotely

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/autosec_research_agent):

```
cd v2/tutorials/autosec_research_agent
uv run --script main.py
```

Follow the printed run URL to watch each target progress through the pipeline and open the report panel for the findings table and per-target detail tabs.

Optional environment variables demonstrate self-healing behavior (`AUTOSEC_FORCE_LLM_TIMEOUT`, `AUTOSEC_FORCE_BAD_TOOL_CALL`, `AUTOSEC_FORCE_OOM`, or `AUTOSEC_FORCE_ALL=1`).
