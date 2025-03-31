---
title: flytekit.core.artifact
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.artifact

## Directory

### Classes

| Class | Description |
|-|-|
| [`Artifact`](.././flytekit.core.artifact#flytekitcoreartifactartifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`ArtifactIDSpecification`](.././flytekit.core.artifact#flytekitcoreartifactartifactidspecification) | This is a special object that helps specify how Artifacts are to be created. |
| [`ArtifactQuery`](.././flytekit.core.artifact#flytekitcoreartifactartifactquery) | None. |
| [`ArtifactSerializationHandler`](.././flytekit.core.artifact#flytekitcoreartifactartifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`DefaultArtifactSerializationHandler`](.././flytekit.core.artifact#flytekitcoreartifactdefaultartifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`FlyteContextManager`](.././flytekit.core.artifact#flytekitcoreartifactflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`InputsBase`](.././flytekit.core.artifact#flytekitcoreartifactinputsbase) | A class to provide better partition semantics. |
| [`OutputMetadata`](.././flytekit.core.artifact#flytekitcoreartifactoutputmetadata) | None. |
| [`Partition`](.././flytekit.core.artifact#flytekitcoreartifactpartition) | None. |
| [`Partitions`](.././flytekit.core.artifact#flytekitcoreartifactpartitions) | None. |
| [`SerializableToString`](.././flytekit.core.artifact#flytekitcoreartifactserializabletostring) | This protocol is used by the Artifact create_from function. |
| [`Serializer`](.././flytekit.core.artifact#flytekitcoreartifactserializer) | None. |
| [`TimePartition`](.././flytekit.core.artifact#flytekitcoreartifacttimepartition) | None. |
| [`Timestamp`](.././flytekit.core.artifact#flytekitcoreartifacttimestamp) | A ProtocolMessage. |
| [`timedelta`](.././flytekit.core.artifact#flytekitcoreartifacttimedelta) | Difference between two datetime values. |

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
def Artifact(
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
):
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
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger |
| [`query()`](#query) | None |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation |


#### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: `*args`,
    kwargs,
):
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
):
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
):
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
| concrete_artifact_id |  |  |
| partitions |  |  |
| time_partition |  |  |

## flytekit.core.artifact.ArtifactIDSpecification

This is a special object that helps specify how Artifacts are to be created. See the comment in the
call function of the main Artifact class. Also see the handling code in transform_variable_map for more
information. There's a limited set of information that we ultimately need in a TypedInterface, so it
doesn't make sense to carry the full Artifact object around. This object should be sufficient, despite
having a pointer to the main artifact.


```python
def ArtifactIDSpecification(
    a: Artifact,
):
```
| Parameter | Type |
|-|-|
| `a` | `Artifact` |

### Methods

| Method | Description |
|-|-|
| [`bind_partitions()`](#bind_partitions) | None |
| [`to_partial_artifact_id()`](#to_partial_artifact_id) | None |


#### bind_partitions()

```python
def bind_partitions(
    args,
    kwargs,
):
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
def ArtifactQuery(
    artifact: Artifact,
    name: str,
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[TimePartition],
    partitions: Optional[Partitions],
    tag: Optional[str],
):
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
| [`get_partition_str()`](#get_partition_str) | None |
| [`get_str()`](#get_str) | None |
| [`get_time_partition_str()`](#get_time_partition_str) | None |
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### get_partition_str()

```python
def get_partition_str(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_str()

```python
def get_str(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_time_partition_str()

```python
def get_time_partition_str(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| bound |  |  |

## flytekit.core.artifact.ArtifactSerializationHandler

This protocol defines the interface for serializing artifact-related entities down to Flyte IDL.


```python
def ArtifactSerializationHandler(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`artifact_query_to_idl()`](#artifact_query_to_idl) | None |
| [`partitions_to_idl()`](#partitions_to_idl) | None |
| [`time_partition_to_idl()`](#time_partition_to_idl) | None |


#### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
):
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
):
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
):
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
| [`artifact_query_to_idl()`](#artifact_query_to_idl) | None |
| [`partitions_to_idl()`](#partitions_to_idl) | None |
| [`time_partition_to_idl()`](#time_partition_to_idl) | None |


#### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `tp` | `Optional[TimePartition]` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.artifact.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) | None |
| [`current_context()`](#current_context) | None |
| [`get_origin_stackframe()`](#get_origin_stackframe) | None |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context |
| [`pop_context()`](#pop_context) | None |
| [`push_context()`](#push_context) | None |
| [`size()`](#size) | None |
| [`with_context()`](#with_context) | None |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
):
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
):
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
):
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.core.artifact.InputsBase

A class to provide better partition semantics
Used for invoking an Artifact to bind partition keys to input values.
If there's a good reason to use a metaclass in the future we can, but a simple instance suffices for now


## flytekit.core.artifact.OutputMetadata

```python
def OutputMetadata(
    artifact: 'Artifact',
    dynamic_partitions: Optional[typing.Dict[str, str]],
    time_partition: Optional[datetime],
    additional_items: Optional[typing.List[SerializableToString]],
):
```
| Parameter | Type |
|-|-|
| `artifact` | `'Artifact'` |
| `dynamic_partitions` | `Optional[typing.Dict[str, str]]` |
| `time_partition` | `Optional[datetime]` |
| `additional_items` | `Optional[typing.List[SerializableToString]]` |

## flytekit.core.artifact.Partition

```python
def Partition(
    value: Optional[art_id.LabelValue],
    name: str,
):
```
| Parameter | Type |
|-|-|
| `value` | `Optional[art_id.LabelValue]` |
| `name` | `str` |

## flytekit.core.artifact.Partitions

```python
def Partitions(
    partitions: Optional[typing.Mapping[str, Union[str, art_id.InputBindingData, Partition]]],
):
```
| Parameter | Type |
|-|-|
| `partitions` | `Optional[typing.Mapping[str, Union[str, art_id.InputBindingData, Partition]]]` |

### Methods

| Method | Description |
|-|-|
| [`set_reference_artifact()`](#set_reference_artifact) | None |
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### set_reference_artifact()

```python
def set_reference_artifact(
    artifact: Artifact,
):
```
| Parameter | Type |
|-|-|
| `artifact` | `Artifact` |

#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| partitions |  |  |

## flytekit.core.artifact.SerializableToString

This protocol is used by the Artifact create_from function. Basically these objects are serialized when running,
and then added to a literal's metadata.


```python
def SerializableToString(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) | None |


#### serialize_to_string()

```python
def serialize_to_string(
    ctx: FlyteContext,
    variable_name: str,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `variable_name` | `str` |

## flytekit.core.artifact.Serializer

### Methods

| Method | Description |
|-|-|
| [`artifact_query_to_idl()`](#artifact_query_to_idl) | None |
| [`partitions_to_idl()`](#partitions_to_idl) | None |
| [`register_serializer()`](#register_serializer) | None |
| [`time_partition_to_idl()`](#time_partition_to_idl) | None |


#### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
):
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
):
```
| Parameter | Type |
|-|-|
| `p` | `Optional[Partitions]` |
| `kwargs` | ``**kwargs`` |

#### register_serializer()

```python
def register_serializer(
    serializer: ArtifactSerializationHandler,
):
```
| Parameter | Type |
|-|-|
| `serializer` | `ArtifactSerializationHandler` |

#### time_partition_to_idl()

```python
def time_partition_to_idl(
    tp: TimePartition,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `tp` | `TimePartition` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.artifact.TimePartition

```python
def TimePartition(
    value: Union[art_id.LabelValue, art_id.InputBindingData, str, datetime.datetime, None],
    op: Optional[Op],
    other: Optional[timedelta],
    granularity: Granularity,
):
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
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

## flytekit.core.artifact.Timestamp

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`FromDatetime()`](#fromdatetime) | Converts datetime to Timestamp |
| [`FromJsonString()`](#fromjsonstring) | Parse a RFC 3339 date string format to Timestamp |
| [`FromMicroseconds()`](#frommicroseconds) | Converts microseconds since epoch to Timestamp |
| [`FromMilliseconds()`](#frommilliseconds) | Converts milliseconds since epoch to Timestamp |
| [`FromNanoseconds()`](#fromnanoseconds) | Converts nanoseconds since epoch to Timestamp |
| [`FromSeconds()`](#fromseconds) | Converts seconds since epoch to Timestamp |
| [`GetCurrentTime()`](#getcurrenttime) | Get the current UTC into Timestamp |
| [`ToDatetime()`](#todatetime) | Converts Timestamp to a datetime |
| [`ToJsonString()`](#tojsonstring) | Converts Timestamp to RFC 3339 date string format |
| [`ToMicroseconds()`](#tomicroseconds) | Converts Timestamp to microseconds since epoch |
| [`ToMilliseconds()`](#tomilliseconds) | Converts Timestamp to milliseconds since epoch |
| [`ToNanoseconds()`](#tonanoseconds) | Converts Timestamp to nanoseconds since epoch |
| [`ToSeconds()`](#toseconds) | Converts Timestamp to seconds since epoch |


#### FromDatetime()

```python
def FromDatetime(
    dt,
):
```
Converts datetime to Timestamp.



| Parameter | Type |
|-|-|
| `dt` |  |

#### FromJsonString()

```python
def FromJsonString(
    value,
):
```
Parse a RFC 3339 date string format to Timestamp.



| Parameter | Type |
|-|-|
| `value` |  |

#### FromMicroseconds()

```python
def FromMicroseconds(
    micros,
):
```
Converts microseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `micros` |  |

#### FromMilliseconds()

```python
def FromMilliseconds(
    millis,
):
```
Converts milliseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `millis` |  |

#### FromNanoseconds()

```python
def FromNanoseconds(
    nanos,
):
```
Converts nanoseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `nanos` |  |

#### FromSeconds()

```python
def FromSeconds(
    seconds,
):
```
Converts seconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `seconds` |  |

#### GetCurrentTime()

```python
def GetCurrentTime()
```
Get the current UTC into Timestamp.


#### ToDatetime()

```python
def ToDatetime(
    tzinfo,
):
```
Converts Timestamp to a datetime.



| Parameter | Type |
|-|-|
| `tzinfo` |  |

#### ToJsonString()

```python
def ToJsonString()
```
Converts Timestamp to RFC 3339 date string format.

Returns:
A string converted from timestamp. The string is always Z-normalized
and uses 3, 6 or 9 fractional digits as required to represent the
exact time. Example of the return format: '1972-01-01T10:00:20.021Z'


#### ToMicroseconds()

```python
def ToMicroseconds()
```
Converts Timestamp to microseconds since epoch.


#### ToMilliseconds()

```python
def ToMilliseconds()
```
Converts Timestamp to milliseconds since epoch.


#### ToNanoseconds()

```python
def ToNanoseconds()
```
Converts Timestamp to nanoseconds since epoch.


#### ToSeconds()

```python
def ToSeconds()
```
Converts Timestamp to seconds since epoch.


## flytekit.core.artifact.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


