---
title: flytekitplugins.mlflow.tracking
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.mlflow.tracking

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_run_metrics()`](#get_run_metrics) | Extracts all metrics and returns a dictionary of metric name to the list of metric for the given run_id. |
| [`get_run_params()`](#get_run_params) | Extracts all parameters and returns a dictionary of metric name to the list of metric for the given run_id. |
| [`metric_to_df()`](#metric_to_df) | Converts mlflow Metric object to a dataframe of 2 columns ['timestamp', 'value']. |
| [`mlflow_autolog()`](#mlflow_autolog) | MLFlow decorator to enable autologging of training metrics. |
| [`plot_metrics()`](#plot_metrics) |  |


## Methods

#### get_run_metrics()

```python
def get_run_metrics(
    c: mlflow.tracking.client.MlflowClient,
    run_id: str,
) -> typing.Dict[str, pandas.core.frame.DataFrame]
```
Extracts all metrics and returns a dictionary of metric name to the list of metric for the given run_id


| Parameter | Type |
|-|-|
| `c` | `mlflow.tracking.client.MlflowClient` |
| `run_id` | `str` |

#### get_run_params()

```python
def get_run_params(
    c: mlflow.tracking.client.MlflowClient,
    run_id: str,
) -> typing.Optional[pandas.core.frame.DataFrame]
```
Extracts all parameters and returns a dictionary of metric name to the list of metric for the given run_id


| Parameter | Type |
|-|-|
| `c` | `mlflow.tracking.client.MlflowClient` |
| `run_id` | `str` |

#### metric_to_df()

```python
def metric_to_df(
    metrics: typing.List[mlflow.entities.metric.Metric],
) -> pandas.core.frame.DataFrame
```
Converts mlflow Metric object to a dataframe of 2 columns ['timestamp', 'value']


| Parameter | Type |
|-|-|
| `metrics` | `typing.List[mlflow.entities.metric.Metric]` |

#### mlflow_autolog()

```python
def mlflow_autolog(
    fn,
    framework,
    experiment_name: typing.Optional[str],
)
```
MLFlow decorator to enable autologging of training metrics.

This decorator can be used as a nested decorator for a ``@task`` and it will automatically enable mlflow autologging,
for the given ``framework``. By default autologging is enabled for ``sklearn``.

.. code-block:: python

    @task
    @mlflow_autolog(framework=mlflow.tensorflow)
    def my_tensorflow_trainer():
        ...

One benefit of doing so is that the mlflow metrics are then rendered inline using FlyteDecks and can be viewed
in jupyter notebook, as well as in hosted Flyte environment:

.. code-block:: python

    # jupyter notebook cell
    with flytekit.new_context() as ctx:
        my_tensorflow_trainer()
        ctx.get_deck()  # IPython.display

When the task is called in a Flyte backend, the decorator starts a new MLFlow run using the Flyte execution name
by default, or a user-provided ``experiment_name`` in the decorator.



| Parameter | Type |
|-|-|
| `fn` |  |
| `framework` |  |
| `experiment_name` | `typing.Optional[str]` |

#### plot_metrics()

```python
def plot_metrics(
    metrics: typing.Dict[str, pandas.core.frame.DataFrame],
) -> typing.Optional[plotly.graph_objs._figure.Figure]
```
| Parameter | Type |
|-|-|
| `metrics` | `typing.Dict[str, pandas.core.frame.DataFrame]` |

