---
title: flytekit.clis.helpers
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.helpers

## Directory

### Methods

| Method | Description |
|-|-|
| [`display_help_with_error()`](#display_help_with_error) |  |
| [`hydrate_registration_parameters()`](#hydrate_registration_parameters) | This is called at registration time to fill out identifier fields (e. |
| [`parse_args_into_dict()`](#parse_args_into_dict) | Takes a tuple like (u'input_b=mystr', u'input_c=18') and returns a dictionary of input name to the. |
| [`str2bool()`](#str2bool) | bool('False') is True in Python, so we need to do some string parsing. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DOMAIN_PLACEHOLDER` | `str` |  |
| `PROJECT_PLACEHOLDER` | `str` |  |
| `VERSION_PLACEHOLDER` | `str` |  |

## Methods

#### display_help_with_error()

```python
def display_help_with_error(
    ctx: click.core.Context,
    message: str,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `message` | `str` |

#### hydrate_registration_parameters()

```python
def hydrate_registration_parameters(
    resource_type: int,
    project: str,
    domain: str,
    version: str,
    entity: typing.Union[flyteidl.admin.launch_plan_pb2.LaunchPlan, flyteidl.admin.workflow_pb2.WorkflowSpec, flyteidl.admin.task_pb2.TaskSpec],
) -> typing.Tuple[flyteidl.core.identifier_pb2.Identifier, typing.Union[flyteidl.admin.launch_plan_pb2.LaunchPlan, flyteidl.admin.workflow_pb2.WorkflowSpec, flyteidl.admin.task_pb2.TaskSpec]]
```
This is called at registration time to fill out identifier fields (e.g. project, domain, version) that are mutable.


| Parameter | Type |
|-|-|
| `resource_type` | `int` |
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `entity` | `typing.Union[flyteidl.admin.launch_plan_pb2.LaunchPlan, flyteidl.admin.workflow_pb2.WorkflowSpec, flyteidl.admin.task_pb2.TaskSpec]` |

#### parse_args_into_dict()

```python
def parse_args_into_dict(
    input_arguments,
) -> e: dict[Text, Text]
```
Takes a tuple like (u'input_b=mystr', u'input_c=18') and returns a dictionary of input name to the
original string value



| Parameter | Type |
|-|-|
| `input_arguments` |  |

#### str2bool()

```python
def str2bool(
    str,
) -> e: bool
```
bool('False') is True in Python, so we need to do some string parsing.  Use the same words in ConfigParser


| Parameter | Type |
|-|-|
| `str` |  |

