---
title: flytekitplugins.airflow.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.airflow.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`AirflowAgent`](.././flytekitplugins.airflow.agent#flytekitpluginsairflowagentairflowagent) | It is used to run Airflow tasks. |
| [`AirflowMetadata`](.././flytekitplugins.airflow.agent#flytekitpluginsairflowagentairflowmetadata) | This class is used to store the Airflow task configuration. |

### Methods

| Method | Description |
|-|-|
| [`get_log_links()`](#get_log_links) |  |


## Methods

#### get_log_links()

```python
def get_log_links(
    airflow_operator: airflow.models.baseoperator.BaseOperator,
    airflow_trigger: typing.Optional[airflow.triggers.base.BaseTrigger],
) -> typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]]
```
| Parameter | Type |
|-|-|
| `airflow_operator` | `airflow.models.baseoperator.BaseOperator` |
| `airflow_trigger` | `typing.Optional[airflow.triggers.base.BaseTrigger]` |

## flytekitplugins.airflow.agent.AirflowAgent

It is used to run Airflow tasks. It is registered as an agent in the AgentRegistry.
There are three kinds of Airflow tasks: AirflowOperator, AirflowSensor, and AirflowHook.

Sensor is always invoked in get method. Calling get method to check if the certain condition is met.
For example, FileSensor is used to check if the file exists. If file doesn't exist, agent returns
RUNNING status, otherwise, it returns SUCCEEDED status.

Hook is a high-level interface to an external platform that lets you quickly and easily talk to
 them without having to write low-level code that hits their API or uses special libraries. For example,
 SlackHook is used to send messages to Slack. Therefore, Hooks are also invoked in get method.
Note: There is no running state for Hook. It is either successful or failed.

Operator is invoked in create method. Flytekit will always set deferrable to True for Operator. Therefore,
`operator.execute` will always raise TaskDeferred exception after job is submitted. In the get method,
we create a trigger to check if the job is finished.
Note: some of the operators are not deferrable. For example, BeamRunJavaPipelineOperator, BeamRunPythonPipelineOperator.
 In this case, those operators will be converted to AirflowContainerTask and executed in the pod.


```python
def AirflowAgent()
```
### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases. |


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekitplugins.airflow.agent.AirflowMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.airflow.agent.AirflowMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.airflow.agent.AirflowMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.airflow.agent.AirflowMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.airflow.agent.AirflowMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.airflow.agent.AirflowMetadata

This class is used to store the Airflow task configuration. It is serialized and returned to FlytePropeller.


```python
class AirflowMetadata(
    airflow_operator: flytekitplugins.airflow.task.AirflowObj,
    airflow_trigger: flytekitplugins.airflow.task.AirflowObj,
    airflow_trigger_callback: str,
    job_id: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `airflow_operator` | `flytekitplugins.airflow.task.AirflowObj` |
| `airflow_trigger` | `flytekitplugins.airflow.task.AirflowObj` |
| `airflow_trigger_callback` | `str` |
| `job_id` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


#### decode()

```python
def decode(
    data: bytes,
) -> AirflowMetadata
```
Decode the resource meta from bytes.


| Parameter | Type |
|-|-|
| `data` | `bytes` |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


