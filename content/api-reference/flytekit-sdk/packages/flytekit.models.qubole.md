---
title: flytekit.models.qubole
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.qubole


This is a deprecated module. Model files for plugins should go alongside the microlib.
See ``plugins/flytekit-kf-pytorch/flytekitplugins/kfpytorch/models.py`` as an example.

## Directory

### Classes

| Class | Description |
|-|-|
| [`HiveQuery`](.././flytekit.models.qubole#flytekitmodelsqubolehivequery) |  |
| [`HiveQueryCollection`](.././flytekit.models.qubole#flytekitmodelsqubolehivequerycollection) |  |
| [`QuboleHiveJob`](.././flytekit.models.qubole#flytekitmodelsqubolequbolehivejob) |  |

## flytekit.models.qubole.HiveQuery

```python
class HiveQuery(
    query,
    timeout_sec,
    retry_count,
)
```
Initializes a new HiveQuery.



| Parameter | Type | Description |
|-|-|-|
| `query` |  | |
| `timeout_sec` |  | |
| `retry_count` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `query` | `None` | The query string. :rtype: str |
| `retry_count` | `None` | :rtype: int |
| `timeout_sec` | `None` | :rtype: int |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _qubole. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: _qubole.HiveQuery


## flytekit.models.qubole.HiveQueryCollection

```python
class HiveQueryCollection(
    queries,
)
```
Initializes a new HiveQueryCollection.



| Parameter | Type | Description |
|-|-|-|
| `queries` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `queries` | `None` | :rtype: list[HiveQuery] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _qubole. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: _qubole.HiveQueryCollection


## flytekit.models.qubole.QuboleHiveJob

```python
class QuboleHiveJob(
    query,
    cluster_label,
    tags,
    query_collection,
)
```
Initializes a HiveJob.



| Parameter | Type | Description |
|-|-|-|
| `query` |  | |
| `cluster_label` |  | |
| `tags` |  | |
| `query_collection` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_label` | `None` | The cluster label where the query should be executed :rtype: Text |
| `is_empty` | `None` |  |
| `query` | `None` | The query to be executed :rtype: HiveQuery |
| `query_collection` | `None` | The queries to be executed :rtype: HiveQueryCollection |
| `tags` | `None` | User tags for the queries :rtype: list[Text] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _qubole. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: _qubole.QuboleHiveJob


