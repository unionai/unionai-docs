---
title: flytekit.clis.helpers
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.helpers

## Directory

### Classes

| Class | Description |
|-|-|
| [`LaunchPlan`](.././flytekit.clis.helpers#flytekitclishelperslaunchplan) | A ProtocolMessage. |
| [`TaskSpec`](.././flytekit.clis.helpers#flytekitclishelperstaskspec) | A ProtocolMessage. |
| [`WorkflowSpec`](.././flytekit.clis.helpers#flytekitclishelpersworkflowspec) | A ProtocolMessage. |

### Methods

| Method | Description |
|-|-|
| [`_hydrate_identifier()`](#_hydrate_identifier) |  |
| [`_hydrate_node()`](#_hydrate_node) |  |
| [`_hydrate_workflow_template_nodes()`](#_hydrate_workflow_template_nodes) |  |
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

#### _hydrate_identifier()

```python
def _hydrate_identifier(
    project: str,
    domain: str,
    version: str,
    identifier: flyteidl.core.identifier_pb2.Identifier,
) -> flyteidl.core.identifier_pb2.Identifier
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `identifier` | `flyteidl.core.identifier_pb2.Identifier` |

#### _hydrate_node()

```python
def _hydrate_node(
    project: str,
    domain: str,
    version: str,
    node: flyteidl.core.workflow_pb2.Node,
) -> flyteidl.core.workflow_pb2.Node
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `node` | `flyteidl.core.workflow_pb2.Node` |

#### _hydrate_workflow_template_nodes()

```python
def _hydrate_workflow_template_nodes(
    project: str,
    domain: str,
    version: str,
    template: flyteidl.core.workflow_pb2.WorkflowTemplate,
) -> flyteidl.core.workflow_pb2.WorkflowTemplate
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `template` | `flyteidl.core.workflow_pb2.WorkflowTemplate` |

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
) -> dict[Text, Text]
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
) -> bool
```
bool('False') is True in Python, so we need to do some string parsing.  Use the same words in ConfigParser


| Parameter | Type |
|-|-|
| `str` |  |

## flytekit.clis.helpers.LaunchPlan

A ProtocolMessage


## flytekit.clis.helpers.TaskSpec

A ProtocolMessage


## flytekit.clis.helpers.WorkflowSpec

A ProtocolMessage


