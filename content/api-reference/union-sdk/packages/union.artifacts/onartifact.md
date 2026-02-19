---
title: OnArtifact
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# OnArtifact

**Package:** `union.artifacts`

Event used to link upstream and downstream workflows together.



```python
class OnArtifact(
    trigger_on: typing.Union[flytekit.core.artifact.Artifact, flytekit.core.artifact.ArtifactQuery],
    inputs: typing.Optional[typing.Dict[str, typing.Union[typing.Any, flytekit.core.artifact.Artifact, flytekit.core.artifact.ArtifactQuery]]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `trigger_on` | `typing.Union[flytekit.core.artifact.Artifact, flytekit.core.artifact.ArtifactQuery]` | Artifact on which to trigger. |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Union[typing.Any, flytekit.core.artifact.Artifact, flytekit.core.artifact.ArtifactQuery]]]` | Dict of inputs.  Example usage::  OnArtifact( trigger_on=dailyArtifact, inputs={ # Use the matched Artifact "today_upstream": dailyArtifact, "yesterday_upstream": dailyArtifact.query( time_partition=dailyArtifact. time_partition - timedelta(days=1)), # Use the matched hourly Artifact "other_daily_upstream": hourlyArtifact.query( partitions={"region": "LAX"}), # Static value "SEA" that will be passed as input "region": "SEA", "other_artifact": UnrelatedArtifact.query( time_partition=dailyArtifact. time_partition - timedelta(days=1)), "other_artifact_2": UnrelatedArtifact.query( time_partition=hourlyArtifact.time_partition.truncate_to_day()), "other_artifact_3": UnrelatedArtifact.query( region=hourlyArtifact.time_partition.truncate_to_day()), }, ) |

## Methods

| Method | Description |
|-|-|
| [`get_parameter_map()`](#get_parameter_map) | This is the key function that enables triggers to work. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### get_parameter_map()

```python
def get_parameter_map(
    input_python_interface: typing.Dict[str, typing.Type],
    input_typed_interface: typing.Dict[str, flytekit.models.interface.Variable],
) -> flyteidl.core.interface_pb2.ParameterMap
```
This is the key function that enables triggers to work. When declaring a trigger, the user specifies an input
map in the form of artifacts, artifact time partitions, and artifact queries (possibly on unrelated artifacts).
When it comes time to create the trigger, we need to convert all of these into a parameter map (because we've
chosen Parameter as the method by which things like artifact queries are passed around). This function does
that, and converts constants to Literals.


| Parameter | Type | Description |
|-|-|-|
| `input_python_interface` | `typing.Dict[str, typing.Type]` | |
| `input_typed_interface` | `typing.Dict[str, flytekit.models.interface.Variable]` | |

### to_flyte_idl()

```python
def to_flyte_idl(
    args,
    kwargs,
) -> flyteidl.artifacts.artifacts_pb2.Trigger
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

