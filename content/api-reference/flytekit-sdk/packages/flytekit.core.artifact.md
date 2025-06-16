---
title: flytekit.core.artifact
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.artifact

## Directory

### Classes

| Class | Description |
|-|-|
| [`Artifact`](.././flytekit.core.artifact#flytekitcoreartifactartifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`ArtifactIDSpecification`](.././flytekit.core.artifact#flytekitcoreartifactartifactidspecification) | This is a special object that helps specify how Artifacts are to be created. |
| [`ArtifactQuery`](.././flytekit.core.artifact#flytekitcoreartifactartifactquery) |  |
| [`ArtifactSerializationHandler`](.././flytekit.core.artifact#flytekitcoreartifactartifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`DefaultArtifactSerializationHandler`](.././flytekit.core.artifact#flytekitcoreartifactdefaultartifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`InputsBase`](.././flytekit.core.artifact#flytekitcoreartifactinputsbase) | A class to provide better partition semantics. |
| [`Partition`](.././flytekit.core.artifact#flytekitcoreartifactpartition) |  |
| [`Partitions`](.././flytekit.core.artifact#flytekitcoreartifactpartitions) |  |
| [`Serializer`](.././flytekit.core.artifact#flytekitcoreartifactserializer) |  |
| [`TimePartition`](.././flytekit.core.artifact#flytekitcoreartifacttimepartition) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `Inputs` | `InputsBase` |  |
| `MAX_PARTITIONS` | `int` |  |
| `O` | `TypeVar` |  |
| `TIME_PARTITION_KWARG` | `str` |  |

## flytekit.core.artifact.Artifact

An Artifact is effectively just a metadata layer on top of data that exists in Flyte. Most data of interest
will be the output of tasks and workflows. The other category is user uploads.

This Python class has limited purpose, as a way for users to specify that tasks/workflows create Artifacts
and the manner (i.e. name, partitions) in which they are created.

Control creation parameters at task/workflow execution time ::

    @task
    def t1() -> Annotated[nn.Module, Artifact(name="my.artifact.name")]:
        ...


```python
class Artifact(
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
)
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `name` | `Optional[str]` |
| `version` | `Optional[str]` |
| `time_partitioned` | `bool` |
| `time_partition` | `Optional[TimePartition]` |
| `time_partition_granularity` | `Optional[Granularity]` |
| `partition_keys` | `Optional[typing.List[str]]` |
| `partitions` | `Optional[Union[Partitions, typing.Dict[str, str]]]` |

### Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task. |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger. |
| [`query()`](#query) |  |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation. |


#### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: `*args`,
    kwargs,
) -> O
```
This function allows users to declare partition values dynamically from the body of a task. Note that you'll
still need to annotate your task function output with the relevant Artifact object. Below, one of the partition
values is bound to an input, and the other is set at runtime. Note that since tasks are not run at compile
time, flytekit cannot check that you've bound all the partition values. It's up to you to ensure that you've
done so.

    Pricing = Artifact(name="pricing", partition_keys=["region"])
    EstError = Artifact(name="estimation_error", partition_keys=["dataset"], time_partitioned=True)

    @task
    def t1() -> Annotated[pd.DataFrame, Pricing], Annotated[float, EstError]:
        df = get_pricing_results()
        dt = get_time()
        return Pricing.create_from(df, region="dubai"),             EstError.create_from(msq_error, dataset="train", time_partition=dt)

You can mix and match with the input syntax as well.

    @task
    def my_task() -> Annotated[pd.DataFrame, RideCountData(region=Inputs.region)]:
        ...
        return RideCountData.create_from(df, time_partition=datetime.datetime.now())


| Parameter | Type |
|-|-|
| `o` | `O` |
| `card` | `Optional[SerializableToString]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### embed_as_query()

```python
def embed_as_query(
    partition: Optional[str],
    bind_to_time_partition: Optional[bool],
    expr: Optional[str],
    op: Optional[Op],
) -> art_id.ArtifactQuery
```
This should only be called in the context of a Trigger. The type of query this returns is different from the
query() function. This type of query is used to reference the triggering artifact, rather than running a query.


| Parameter | Type |
|-|-|
| `partition` | `Optional[str]` |
| `bind_to_time_partition` | `Optional[bool]` |
| `expr` | `Optional[str]` |
| `op` | `Optional[Op]` |

#### query()

```python
def query(
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]],
    partitions: Optional[Union[typing.Dict[str, str], Partitions]],
    kwargs,
) -> ArtifactQuery
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `time_partition` | `Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]]` |
| `partitions` | `Optional[Union[typing.Dict[str, str], Partitions]]` |
| `kwargs` | ``**kwargs`` |

#### to_id_idl()

```python
def to_id_idl()
```
Converts this object to the IDL representation.
This is here instead of translator because it's in the interface, a relatively simple proto object
that's exposed to the user.


### Properties

| Property | Type | Description |
|-|-|-|
| `concrete_artifact_id` |  |  |
| `partitions` |  |  |
| `time_partition` |  |  |

## flytekit.core.artifact.ArtifactIDSpecification

This is a special object that helps specify how Artifacts are to be created. See the comment in the
call function of the main Artifact class. Also see the handling code in transform_variable_map for more
information. There's a limited set of information that we ultimately need in a TypedInterface, so it
doesn't make sense to carry the full Artifact object around. This object should be sufficient, despite
having a pointer to the main artifact.


```python
class ArtifactIDSpecification(
    a: Artifact,
)
```
| Parameter | Type |
|-|-|
| `a` | `Artifact` |

### Methods

| Method | Description |
|-|-|
| [`bind_partitions()`](#bind_partitions) |  |
| [`to_partial_artifact_id()`](#to_partial_artifact_id) |  |


#### bind_partitions()

```python
def bind_partitions(
    args,
    kwargs,
) -> ArtifactIDSpecification
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### to_partial_artifact_id()

```python
def to_partial_artifact_id()
```
## flytekit.core.artifact.ArtifactQuery

```python
class ArtifactQuery(
    artifact: Artifact,
    name: str,
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[TimePartition],
    partitions: Optional[Partitions],
    tag: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `artifact` | `Artifact` |
| `name` | `str` |
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `time_partition` | `Optional[TimePartition]` |
| `partitions` | `Optional[Partitions]` |
| `tag` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`get_partition_str()`](#get_partition_str) |  |
| [`get_str()`](#get_str) |  |
| [`get_time_partition_str()`](#get_time_partition_str) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### get_partition_str()

```python
def get_partition_str(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_str()

```python
def get_str(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_time_partition_str()

```python
def get_time_partition_str(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `bound` |  |  |

## flytekit.core.artifact.ArtifactSerializationHandler

This protocol defines the interface for serializing artifact-related entities down to Flyte IDL.


```python
class ArtifactSerializationHandler(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`artifact_query_to_idl()`](#artifact_query_to_idl) |  |
| [`partitions_to_idl()`](#partitions_to_idl) |  |
| [`time_partition_to_idl()`](#time_partition_to_idl) |  |


#### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type |
|-|-|
| `aq` | `ArtifactQuery` |
| `kwargs` | ``**kwargs`` |

#### partitions_to_idl()

```python
def partitions_to_idl(
    p: Optional[Partitions],
    kwargs,
) -> Optional[art_id.Partitions]
```
| Parameter | Type |
|-|-|
| `p` | `Optional[Partitions]` |
| `kwargs` | ``**kwargs`` |

#### time_partition_to_idl()

```python
def time_partition_to_idl(
    tp: Optional[TimePartition],
    kwargs,
) -> Optional[art_id.TimePartition]
```
| Parameter | Type |
|-|-|
| `tp` | `Optional[TimePartition]` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.artifact.DefaultArtifactSerializationHandler

This protocol defines the interface for serializing artifact-related entities down to Flyte IDL.


### Methods

| Method | Description |
|-|-|
| [`artifact_query_to_idl()`](#artifact_query_to_idl) |  |
| [`partitions_to_idl()`](#partitions_to_idl) |  |
| [`time_partition_to_idl()`](#time_partition_to_idl) |  |


#### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type |
|-|-|
| `aq` | `ArtifactQuery` |
| `kwargs` | ``**kwargs`` |

#### partitions_to_idl()

```python
def partitions_to_idl(
    p: Optional[Partitions],
    kwargs,
) -> Optional[art_id.Partitions]
```
| Parameter | Type |
|-|-|
| `p` | `Optional[Partitions]` |
| `kwargs` | ``**kwargs`` |

#### time_partition_to_idl()

```python
def time_partition_to_idl(
    tp: Optional[TimePartition],
    kwargs,
) -> Optional[art_id.TimePartition]
```
| Parameter | Type |
|-|-|
| `tp` | `Optional[TimePartition]` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.artifact.InputsBase

A class to provide better partition semantics
Used for invoking an Artifact to bind partition keys to input values.
If there's a good reason to use a metaclass in the future we can, but a simple instance suffices for now


## flytekit.core.artifact.Partition

```python
class Partition(
    value: Optional[art_id.LabelValue],
    name: str,
)
```
| Parameter | Type |
|-|-|
| `value` | `Optional[art_id.LabelValue]` |
| `name` | `str` |

## flytekit.core.artifact.Partitions

```python
class Partitions(
    partitions: Optional[typing.Mapping[str, Union[str, art_id.InputBindingData, Partition]]],
)
```
| Parameter | Type |
|-|-|
| `partitions` | `Optional[typing.Mapping[str, Union[str, art_id.InputBindingData, Partition]]]` |

### Methods

| Method | Description |
|-|-|
| [`set_reference_artifact()`](#set_reference_artifact) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### set_reference_artifact()

```python
def set_reference_artifact(
    artifact: Artifact,
)
```
| Parameter | Type |
|-|-|
| `artifact` | `Artifact` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> Optional[art_id.Partitions]
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `partitions` |  |  |

## flytekit.core.artifact.Serializer

### Methods

| Method | Description |
|-|-|
| [`artifact_query_to_idl()`](#artifact_query_to_idl) |  |
| [`partitions_to_idl()`](#partitions_to_idl) |  |
| [`register_serializer()`](#register_serializer) |  |
| [`time_partition_to_idl()`](#time_partition_to_idl) |  |


#### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type |
|-|-|
| `aq` | `ArtifactQuery` |
| `kwargs` | ``**kwargs`` |

#### partitions_to_idl()

```python
def partitions_to_idl(
    p: Optional[Partitions],
    kwargs,
) -> Optional[art_id.Partitions]
```
| Parameter | Type |
|-|-|
| `p` | `Optional[Partitions]` |
| `kwargs` | ``**kwargs`` |

#### register_serializer()

```python
def register_serializer(
    serializer: ArtifactSerializationHandler,
)
```
| Parameter | Type |
|-|-|
| `serializer` | `ArtifactSerializationHandler` |

#### time_partition_to_idl()

```python
def time_partition_to_idl(
    tp: TimePartition,
    kwargs,
) -> Optional[art_id.TimePartition]
```
| Parameter | Type |
|-|-|
| `tp` | `TimePartition` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.artifact.TimePartition

```python
class TimePartition(
    value: Union[art_id.LabelValue, art_id.InputBindingData, str, datetime.datetime, None],
    op: Optional[Op],
    other: Optional[timedelta],
    granularity: Granularity,
)
```
| Parameter | Type |
|-|-|
| `value` | `Union[art_id.LabelValue, art_id.InputBindingData, str, datetime.datetime, None]` |
| `op` | `Optional[Op]` |
| `other` | `Optional[timedelta]` |
| `granularity` | `Granularity` |

### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> Optional[art_id.TimePartition]
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

