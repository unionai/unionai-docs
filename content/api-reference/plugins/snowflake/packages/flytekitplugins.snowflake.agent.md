---
title: flytekitplugins.snowflake.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.snowflake.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`SnowflakeAgent`](.././flytekitplugins.snowflake.agent#flytekitpluginssnowflakeagentsnowflakeagent) | This is the base class for all async agents. |
| [`SnowflakeJobMetadata`](.././flytekitplugins.snowflake.agent#flytekitpluginssnowflakeagentsnowflakejobmetadata) |  |

### Methods

| Method | Description |
|-|-|
| [`construct_query_link()`](#construct_query_link) |  |
| [`get_connection()`](#get_connection) |  |
| [`get_private_key()`](#get_private_key) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `SNOWFLAKE_PRIVATE_KEY` | `str` |  |
| `TASK_TYPE` | `str` |  |

## Methods

#### construct_query_link()

```python
def construct_query_link(
    resource_meta: flytekitplugins.snowflake.agent.SnowflakeJobMetadata,
) -> str
```
| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.snowflake.agent.SnowflakeJobMetadata` |

#### get_connection()

```python
def get_connection(
    metadata: flytekitplugins.snowflake.agent.SnowflakeJobMetadata,
) -> <module 'snowflake.connector' from '/Users/nelson/src/flyteorg/flytekit/.venv/lib/python3.12/site-packages/snowflake/connector/__init__.py'>
```
| Parameter | Type |
|-|-|
| `metadata` | `flytekitplugins.snowflake.agent.SnowflakeJobMetadata` |

#### get_private_key()

```python
def get_private_key()
```
## flytekitplugins.snowflake.agent.SnowflakeAgent

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def SnowflakeAgent()
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
) -> flytekitplugins.snowflake.agent.SnowflakeJobMetadata
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
    resource_meta: flytekitplugins.snowflake.agent.SnowflakeJobMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.snowflake.agent.SnowflakeJobMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.snowflake.agent.SnowflakeJobMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.snowflake.agent.SnowflakeJobMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.snowflake.agent.SnowflakeJobMetadata

```python
class SnowflakeJobMetadata(
    user: str,
    account: str,
    database: str,
    schema: str,
    warehouse: str,
    query_id: str,
    has_output: bool,
)
```
| Parameter | Type |
|-|-|
| `user` | `str` |
| `account` | `str` |
| `database` | `str` |
| `schema` | `str` |
| `warehouse` | `str` |
| `query_id` | `str` |
| `has_output` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


#### decode()

```python
def decode(
    data: bytes,
) -> ResourceMeta
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


