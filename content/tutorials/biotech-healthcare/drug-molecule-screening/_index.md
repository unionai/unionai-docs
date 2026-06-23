---
title: Drug molecule screening agent
weight: 5
variants: +flyte +union
---

# Drug molecule screening agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/drug_molecule_screening).

This tutorial builds an **agentic** virtual drug-screening workflow on Flyte. A medicinal-chemistry agent interprets your therapeutic goal in plain language, derives screening criteria, and composes durable RDKit stage tasks — while the scientific core (property computation, Lipinski filters, Tanimoto similarity, ranking, and HTML reports) stays in trusted, deterministic tools.

The pattern follows how cheminformatics agents like ChemCrow and PharmAgents are built: **the LLM plans and reflects; RDKit computes.**

Flyte provides:

- **Flyte-native agent orchestration** via `flyte.ai.agents.Agent` — see [Flyte-native agents](../../../user-guide/build-agent/flyte-agents/)
- **Typed agent tool I/O** — Flyte 2.5.4+ passes `flyte.io.Dir`, `File`, and `DataFrame` between agent tool calls so the LLM can compose multi-step pipelines directly
- **Cached molecule loading** so repeated runs skip re-parsing SMILES
- **Report-enabled stage tasks** that stream property charts, similarity matrices, and candidate spotlights as each step completes
- **Hybrid iteration** — the agent re-runs `screen_candidates` and `generate_report` with adjusted criteria when the funnel is too narrow, reusing cached `molecule_dir` and `properties_json`

> [!NOTE] Prerequisites
> The agent requires an `internal-anthropic-api-key` secret on your cluster (same as other agent tutorials).

## Define the task environment

The pipeline runs on CPU with RDKit, LiteLLM, and system libraries for 2D structure rendering.

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.5.4",
#    "litellm",
#    "rdkit",
#    "numpy",
#    "scikit-learn",
#    "pillow",
# ]
# ///
```

## Define the screening agent

The agent receives a natural-language brief and composes four stage tools in order. Each tool is a durable Flyte task with its own `report=True` surface in the Flyte UI.

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=agent lang=python >}}

## Run the agentic pipeline

The `pipeline` task delegates to the screening agent:

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=pipeline lang=python >}}

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/drug_molecule_screening):

```
cd v2/tutorials/drug_molecule_screening
uv run --script drug_molecule_screening.py
```

Pass a natural-language brief (the agent derives the target profile):

```
flyte run drug_molecule_screening.py pipeline \
  --brief "Find oral kinase inhibitor candidates under 400 Da with moderate LogP"
```

Or pass an explicit target profile to skip agent-derived criteria:

```
flyte run drug_molecule_screening.py pipeline \
  --target_profile '{"mw": [100, 400], "logp": [-0.5, 4.0]}'
```

### Two-round rescreen demo (complex execution graph)

The `rescreen_demo` task always runs two screening rounds: a strict first pass (`load_molecules` → `compute_properties` → `screen_candidates` → `generate_report`), then a second `screen_candidates` → `generate_report` with a widened LogP window reusing the same `molecule_dir` and `properties_json`. The Flyte UI shows six stage tasks instead of four.

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=rescreen_demo lang=python >}}

```
flyte run drug_molecule_screening.py rescreen_demo
```

Or pass the same inputs to `pipeline` directly:

```
flyte run drug_molecule_screening.py pipeline \
  --brief "Screen the default library. If all_criteria_met is 0 after generate_report, re-run screen_candidates and generate_report with target_profile {\"mw\": [150, 200], \"logp\": [-0.5, 3.5], \"hbd\": [0, 1], \"hba\": [0, 3], \"tpsa\": [20, 45]}." \
  --target_profile '{"mw": [150, 200], "logp": [-0.5, 1.0], "hbd": [0, 1], "hba": [0, 3], "tpsa": [20, 45]}'
```

Open the run URL and follow the report panel for funnel charts, property distributions, top-candidate spotlights, and the agent's final screening summary. A successful rescreen demo shows two rounds of `screen_candidates` and `generate_report` in the action tree.
