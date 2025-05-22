---
title: Weights & Biases
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Weights & Biases
  title_expanded: Flytekit Weights and Biases Plugin
  name: flytekitplugins-wandb
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package enables seamless use of Weights & Biases within Flyte
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.wandb
  install_requires:
  - flytekit>=1.12.0
  - wandb>=0.17.0
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Programming Language :: Python :: 3.12'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  folder: flytekit-wandb
---


The Weights and Biases MLOps platform helps AI developers streamline their ML workflow from end-to-end. This plugin
enables seamless use of Weights and Biases within Flyte by configuring links between the two platforms.

To install the plugin, run:

```bash
pip install flytekitplugins-wandb
```

Here is an example of running W&B with XGBoost using W&B for tracking:

```python
from flytekit import task, Secret, ImageSpec, workflow

from flytekitplugins.wandb import wandb_init

WANDB_PROJECT = "flytekit-wandb-plugin"
WANDB_ENTITY = "github-username"
WANDB_SECRET_KEY = "wandb-api-key"
WANDB_SECRET_GROUP = "wandb-api-group"
REGISTRY = "localhost:30000"

image = ImageSpec(
    name="wandb_example",
    python_version="3.11",
    packages=["flytekitplugins-wandb", "xgboost", "scikit-learn"],
    registry=REGISTRY,
)
wandb_secret = Secret(key=WANDB_SECRET_KEY, group=WANDB_SECRET_GROUP)


@task(
    container_image=image,
    secret_requests=[wandb_secret],
)
@wandb_init(
    project=WANDB_PROJECT,
    entity=WANDB_ENTITY,
    secret=wandb_secret,
)
def train() -> float:
    from xgboost import XGBClassifier
    from wandb.integration.xgboost import WandbCallback
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    import wandb

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    bst = XGBClassifier(
        n_estimators=100,
        objective="binary:logistic",
        callbacks=[WandbCallback(log_model=True)],
    )
    bst.fit(X_train, y_train)

    test_score = bst.score(X_test, y_test)

    # Log custom metrics
    wandb.run.log({"test_score": test_score})
    return test_score


@workflow
def main() -> float:
    return train()
```

Weights and Biases requires an API key to authenticate with their service. In the above example,
the secret is created using
[Flyte's Secrets manager](https://docs.flyte.org/en/latest/user_guide/productionizing/secrets.html).

To enable linking from the Flyte side panel to Weights and Biases, add the following to Flyte's
configuration

```yaml
plugins:
  logs:
    dynamic-log-links:
      - wandb-execution-id:
          displayName: Weights & Biases
          templateUris: '{{ .taskConfig.host }}/{{ .taskConfig.entity }}/{{ .taskConfig.project }}/runs/{{ .executionName }}-{{ .nodeId }}-{{ .taskRetryAttempt }}'
      - wandb-custom-id:
          displayName: Weights & Biases
          templateUris: '{{ .taskConfig.host }}/{{ .taskConfig.entity }}/{{ .taskConfig.project }}/runs/{{ .taskConfig.id }}'
```
