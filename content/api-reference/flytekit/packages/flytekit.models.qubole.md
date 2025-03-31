---
title: flytekit.models.qubole
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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



| Parameter | Type |
|-|-|
| `query` |  |
| `timeout_sec` |  |
| `retry_count` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `query` |  | {{< multiline >}}The query string.
{{< /multiline >}} |
| `retry_count` |  |  |
| `timeout_sec` |  |  |

## flytekit.models.qubole.HiveQueryCollection

```python
class HiveQueryCollection(
    queries,
)
```
Initializes a new HiveQueryCollection.



| Parameter | Type |
|-|-|
| `queries` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> HiveQueryCollection
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `queries` |  |  |

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



| Parameter | Type |
|-|-|
| `query` |  |
| `cluster_label` |  |
| `tags` |  |
| `query_collection` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> QuboleHiveJob
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_label` |  | {{< multiline >}}The cluster label where the query should be executed
{{< /multiline >}} |
| `is_empty` |  |  |
| `query` |  | {{< multiline >}}The query to be executed
{{< /multiline >}} |
| `query_collection` |  | {{< multiline >}}The queries to be executed
{{< /multiline >}} |
| `tags` |  | {{< multiline >}}User tags for the queries
{{< /multiline >}} |

