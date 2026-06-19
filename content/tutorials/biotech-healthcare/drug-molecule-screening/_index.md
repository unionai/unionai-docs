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
- **Report tasks** that stream property charts, similarity matrices, and candidate spotlights as each stage completes
- **End-to-end orchestration** from library loading through final ranked recommendations

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

The `pipeline` task loads molecules, computes properties, screens against a target profile, and generates a final report.

{{< code file="/unionai-examples/v2/tutorials/drug_molecule_screening/drug_molecule_screening.py" fragment=pipeline lang=python >}}

Intermediate tasks (`load_molecules`, `compute_properties`, `screen_candidates`, `generate_report`) each update the Flyte report as they run.

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
