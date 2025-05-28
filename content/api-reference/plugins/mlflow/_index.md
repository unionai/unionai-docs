---
title: MLflow
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: MLflow
  title_expanded: Flytekit MLflow Plugin
  name: flytekitplugins-mlflow
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package enables seamless use of MLFlow within Flyte
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.mlflow
  install_requires:
  - flytekit>=1.1.0,<2.0.0
  - plotly
  - mlflow>=2.10.0
  - pandas
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  folder: flytekit-mlflow
---


MLflow enables us to log parameters, code, and results in machine learning experiments and compare them using an interactive UI.
This MLflow plugin enables seamless use of MLFlow within Flyte, and render the metrics and parameters on Flyte Deck.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-mlflow
```

Example
```python
from flytekit import task, workflow
from flytekitplugins.mlflow import mlflow_autolog
import mlflow

@task(enable_deck=True)
@mlflow_autolog(framework=mlflow.keras)
def train_model():
    ...
```
