---
title: Artifact
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Artifact

**Package:** `union.artifacts`

This is a wrapper around the Flytekit Artifact class.

This Python class has two purposes - as a Python representation of a materialized Artifact,
and as a way for users to specify that tasks/workflows create Artifacts and the manner
in which they are created.

Use one as input to workflow (only workflow for now)
df_artifact = Artifact.get("flyte://a1")
remote.execute(wf, inputs={"a": df_artifact})

Note that Python fields will be missing when retrieved from the service.



```python
class Artifact(
    args,
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
    python_val: Optional[typing.Any],
    python_type: Optional[typing.Type],
    literal: Optional[Literal],
    literal_type: Optional[LiteralType],
    short_description: Optional[str],
    source: Optional[artifacts_pb2.ArtifactSource],
    card: Optional[Card],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `project` | `Optional[str]` | Should not be directly user provided, the project/domain will come from the project/domain of the execution that produced the output. These values will be filled in automatically when retrieving however. |
| `domain` | `Optional[str]` | See above. |
| `name` | `Optional[str]` | The name of the Artifact. This should be user provided. |
| `version` | `Optional[str]` | Version of the Artifact, typically the execution ID, plus some additional entropy. Not user provided. |
| `time_partitioned` | `bool` | Whether or not this Artifact will have a time partition. |
| `time_partition` | `Optional[TimePartition]` | If you want to manually pass in the full TimePartition object |
| `time_partition_granularity` | `Optional[Granularity]` | If you don't want to manually pass in the full TimePartition object, but want to control the granularity when one is automatically created for you. Note that consistency checking is limited while in alpha. |
| `partition_keys` | `Optional[typing.List[str]]` | This is a list of keys that will be used to partition the Artifact. These are not the values. Values are set via a () on the artifact and will end up in the partition_values field. |
| `partitions` | `Optional[Union[Partitions, typing.Dict[str, str]]]` | This is a dictionary of partition keys to values. |
| `python_val` | `Optional[typing.Any]` | The Python value. |
| `python_type` | `Optional[typing.Type]` | The Python type. |
| `literal` | `Optional[Literal]` | |
| `literal_type` | `Optional[LiteralType]` | |
| `short_description` | `Optional[str]` | |
| `source` | `Optional[artifacts_pb2.ArtifactSource]` | |
| `card` | `Optional[Card]` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `concrete_artifact_id` | `None` |  |
| `partitions` | `None` |  |
| `time_partition` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task. |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger. |
| [`from_flyte_idl()`](#from_flyte_idl) | Converts the IDL representation to this object. |
| [`get()`](#get) | This function is supposed to mimic the get() behavior inputs/outputs as returned by FlyteRemote for an. |
| [`initialize()`](#initialize) | Use this for when you have a Python value you want to get an Artifact object out of. |
| [`metadata()`](#metadata) |  |
| [`query()`](#query) |  |
| [`set_resolver()`](#set_resolver) |  |
| [`set_source()`](#set_source) |  |
| [`to_create_request()`](#to_create_request) |  |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation. |


### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: *args,
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
    def t1() -&gt; Annotated[pd.DataFrame, Pricing], Annotated[float, EstError]:
        df = get_pricing_results()
        dt = get_time()
        return Pricing.create_from(df, region="dubai"),             EstError.create_from(msq_error, dataset="train", time_partition=dt)

You can mix and match with the input syntax as well.

    @task
    def my_task() -&gt; Annotated[pd.DataFrame, RideCountData(region=Inputs.region)]:
        ...
        return RideCountData.create_from(df, time_partition=datetime.datetime.now())


| Parameter | Type | Description |
|-|-|-|
| `o` | `O` | |
| `card` | `Optional[SerializableToString]` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### embed_as_query()

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


| Parameter | Type | Description |
|-|-|-|
| `partition` | `Optional[str]` | Can embed a time partition |
| `bind_to_time_partition` | `Optional[bool]` | Set to true if you want to bind to a time partition |
| `expr` | `Optional[str]` | Only valid if there's a time partition. |
| `op` | `Optional[Op]` | If expr is given, then op is what to do with it. |

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: artifacts_pb2.Artifact,
) -> Artifact
```
Converts the IDL representation to this object.


| Parameter | Type | Description |
|-|-|-|
| `pb2` | `artifacts_pb2.Artifact` | |

### get()

```python
def get(
    as_type: Optional[typing.Type],
) -> Optional[typing.Any]
```
This function is supposed to mimic the get() behavior inputs/outputs as returned by FlyteRemote for an
execution, leveraging the LiteralsResolver (and underneath that the TypeEngine) to turn the literal into a
Python value.


| Parameter | Type | Description |
|-|-|-|
| `as_type` | `Optional[typing.Type]` | |

### initialize()

```python
def initialize(
    python_val: typing.Any,
    python_type: typing.Type,
    name: Optional[str],
    literal_type: Optional[LiteralType],
    version: Optional[str],
    tags: Optional[typing.List[str]],
) -> Artifact
```
Use this for when you have a Python value you want to get an Artifact object out of.

This function readies an Artifact for creation, it doesn't actually create it just yet since this is a
network-less call. You will need to persist it with a FlyteRemote instance:
    remote.create_artifact(Artifact.initialize(...))

Artifact.initialize("/path/to/file", tags={"tag1": "val1"})
Artifact.initialize("/path/to/parquet", type=pd.DataFrame, tags=["0.1.0"])

What's set here is everything that isn't set by the server. What is set by the server?
- name, version, if not set by user.
- uri
Set by remote
- project, domain


| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `python_type` | `typing.Type` | |
| `name` | `Optional[str]` | |
| `literal_type` | `Optional[LiteralType]` | |
| `version` | `Optional[str]` | |
| `tags` | `Optional[typing.List[str]]` | |

### metadata()

```python
def metadata()
```
### query()

```python
def query(
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]],
    partitions: Optional[Union[typing.Dict[str, str], Partitions]],
    kwargs,
) -> ArtifactQuery
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `time_partition` | `Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]]` | |
| `partitions` | `Optional[Union[typing.Dict[str, str], Partitions]]` | |
| `kwargs` | `**kwargs` | |

### set_resolver()

```python
def set_resolver(
    resolver: LiteralsResolver,
)
```
| Parameter | Type | Description |
|-|-|-|
| `resolver` | `LiteralsResolver` | |

### set_source()

```python
def set_source(
    source: artifacts_pb2.ArtifactSource,
)
```
| Parameter | Type | Description |
|-|-|-|
| `source` | `artifacts_pb2.ArtifactSource` | |

### to_create_request()

```python
def to_create_request(
    a: Artifact,
) -> artifacts_pb2.CreateArtifactRequest
```
| Parameter | Type | Description |
|-|-|-|
| `a` | `Artifact` | |

### to_id_idl()

```python
def to_id_idl()
```
Converts this object to the IDL representation.
This is here instead of translator because it's in the interface, a relatively simple proto object
that's exposed to the user.


