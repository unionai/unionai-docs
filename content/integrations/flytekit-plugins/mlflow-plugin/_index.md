---
title: MLflow
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: false
---

# MLflow

The MLflow Tracking component is an API and UI for logging parameters,
code versions, metrics, and output files when running your machine learning code and for later visualizing the results

First, install the Flyte MLflow plugin:

```shell
$  pip install flytekitplugins-mlflow
```

To log the metrics and parameters to Flyte deck, add `@mlflow_autolog` to the task. For example

```python
@task(enable_deck=True)
@mlflow_autolog(framework=mlflow.keras)
def train_model(epochs: int):
...
```

To log the metric and parameters to a remote MLflow server, add default environment variable [MLFLOW_TRACKING_URI](https://mlflow.org/docs/latest/tracking.html#logging-to-a-tracking-server) to the flytepropeller config map.

```shell
$  kubectl edit cm flyte-propeller-config
```

```yaml
plugins:
  k8s:
    default-cpus: 100m
    default-env-vars:
    - MLFLOW_TRACKING_URI: postgresql+psycopg2://postgres:@postgres.flyte.svc.cluster.local:5432/flyteadmin
```

![MLflow UI](../../../_static/images/integrations/flytekit-plugins/mlflow-plugin/mlflow-ui.png)

