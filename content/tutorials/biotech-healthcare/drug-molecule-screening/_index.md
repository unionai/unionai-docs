---
title: Drug molecule screening
weight: 5
variants: +flyte +union
---

# Drug molecule screening

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/drug_molecule_screening).

This tutorial builds a virtual drug-screening pipeline on Flyte. The workflow loads a library of drug SMILES strings, computes physicochemical properties with [RDKit](https://www.rdkit.org/), applies Lipinski's Rule of Five and custom target-profile filters, and ranks candidates by drug-likeness score — with rich HTML reports streamed into the Flyte UI.

Flyte provides:

- **Cached molecule loading** so repeated runs skip re-parsing SMILES
- **Report-enabled stage tasks** that stream property charts, similarity matrices, and candidate spotlights as each step completes
- **Lightweight orchestration** — the top-level `pipeline` task chains stages without its own report surface

## Define the task environment

The pipeline runs on CPU with RDKit and system libraries for 2D structure rendering.

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "rdkit",
#    "numpy",
#    "scikit-learn",
#    "pillow",
# ]
# ///
```

## Orchestrate the pipeline

The `pipeline` task is a lightweight orchestrator: it calls four stage tasks in sequence and returns a JSON summary.

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=pipeline lang=python >}}

Each stage task (`load_molecules`, `compute_properties`, `screen_candidates`, `generate_report`) owns its own `report=True` surface and updates the Flyte UI as it runs.

## Run the workflow

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/drug_molecule_screening):

```
cd v2/tutorials/drug_molecule_screening
uv run --script drug_molecule_screening.py
```

Pass a custom target profile:

```
flyte run drug_molecule_screening.py pipeline \
  --target_profile '{"mw": [100, 400], "logp": [-0.5, 4.0]}'
```

Open the run URL and follow the report panel for funnel charts, property distributions, and top-candidate spotlights.
