---
title: Artifact
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Artifact

**Package:** `flytekit.core.artifact`

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
| Parameter | Type | Description |
|-|-|-|
| `project` | `Optional[str]` | Should not be directly user provided, the project/domain will come from the project/domain of the execution that produced the output. These values will be filled in automatically when retrieving however. |
| `domain` | `Optional[str]` | See above. |
| `name` | `Optional[str]` | The name of the Artifact. This should be user provided. |
| `version` | `Optional[str]` | Version of the Artifact, typically the execution ID, plus some additional entropy. Not user provided. |
| `time_partitioned` | `bool` | Whether or not this Artifact will have a time partition. |
| `time_partition` | `Optional[TimePartition]` | If you want to manually pass in the full TimePartition object |
| `time_partition_granularity` | `Optional[Granularity]` | If you don't want to manually pass in the full TimePartition object, but want to control the granularity when one is automatically created for you. Note that consistency checking is limited while in alpha. |
| `partition_keys` | `Optional[typing.List[str]]` | This is a list of keys that will be used to partition the Artifact. These are not the values. Values are set via a () on the artifact and will end up in the partition_values field. |
| `partitions` | `Optional[Union[Partitions, typing.Dict[str, str]]]` | This is a dictionary of partition keys to values. |

## Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task. |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger. |
| [`query()`](#query) |  |
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
    def t1() -> Annotated[pd.DataFrame, Pricing], Annotated[float, EstError]:
        df = get_pricing_results()
        dt = get_time()
        return Pricing.create_from(df, region="dubai"),             EstError.create_from(msq_error, dataset="train", time_partition=dt)

You can mix and match with the input syntax as well.

    @task
    def my_task() -> Annotated[pd.DataFrame, RideCountData(region=Inputs.region)]:
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

### to_id_idl()

```python
def to_id_idl()
```
Converts this object to the IDL representation.
This is here instead of translator because it's in the interface, a relatively simple proto object
that's exposed to the user.


## Properties

| Property | Type | Description |
|-|-|-|
| `concrete_artifact_id` |  |  |
| `partitions` |  |  |
| `time_partition` |  |  |

