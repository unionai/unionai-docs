---
title: flytekit.models.qubole
version: 1.16.10
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


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `query` |  | {{< multiline >}}The query string.
:rtype: str
{{< /multiline >}} |
| `retry_count` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `timeout_sec` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `queries` |  | {{< multiline >}}:rtype: list[HiveQuery]
{{< /multiline >}} |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_label` |  | {{< multiline >}}The cluster label where the query should be executed
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `query` |  | {{< multiline >}}The query to be executed
:rtype: HiveQuery
{{< /multiline >}} |
| `query_collection` |  | {{< multiline >}}The queries to be executed
:rtype: HiveQueryCollection
{{< /multiline >}} |
| `tags` |  | {{< multiline >}}User tags for the queries
:rtype: list[Text]
{{< /multiline >}} |

