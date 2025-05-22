---
title: flytekit.clients.raw
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.raw

## Directory

### Classes

| Class | Description |
|-|-|
| [`RawSynchronousFlyteClient`](.././flytekit.clients.raw#flytekitclientsrawrawsynchronousflyteclient) | This is a thin synchronous wrapper around the auto-generated GRPC stubs for communicating with the admin service. |

## flytekit.clients.raw.RawSynchronousFlyteClient

This is a thin synchronous wrapper around the auto-generated GRPC stubs for communicating with the admin service.

This client should be usable regardless of environment in which this is used. In other words, configurations should
be explicit as opposed to inferred from the environment or a configuration file. To create a client,

```python
from flytekit.configuration import PlatformConfig
RawSynchronousFlyteClient(PlatformConfig(endpoint="a.b.com", insecure=True))  # or
SynchronousFlyteClient(PlatformConfig(endpoint="a.b.com", insecure=True))
```


```python
class RawSynchronousFlyteClient(
    cfg: PlatformConfig,
    kwargs,
)
```
Initializes a gRPC channel to the given Flyte Admin service.



| Parameter | Type |
|-|-|
| `cfg` | `PlatformConfig` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`create_download_link()`](#create_download_link) |  |
| [`create_download_location()`](#create_download_location) |  |
| [`create_execution()`](#create_execution) | This will create an execution for the given execution spec. |
| [`create_launch_plan()`](#create_launch_plan) | This will create a launch plan definition in the Admin database. |
| [`create_task()`](#create_task) | This will create a task definition in the Admin database. |
| [`create_upload_location()`](#create_upload_location) | Get a signed url to be used during fast registration. |
| [`create_workflow()`](#create_workflow) | This will create a workflow definition in the Admin database. |
| [`get_active_launch_plan()`](#get_active_launch_plan) | Retrieves a launch plan entity. |
| [`get_domains()`](#get_domains) | This will return a list of domains registered with the Flyte Admin Service. |
| [`get_execution()`](#get_execution) | Returns an execution of a workflow entity. |
| [`get_execution_data()`](#get_execution_data) | Returns signed URLs to LiteralMap blobs for an execution's inputs and outputs (when available). |
| [`get_execution_metrics()`](#get_execution_metrics) | Returns metrics partitioning and categorizing the workflow execution time-series. |
| [`get_launch_plan()`](#get_launch_plan) | Retrieves a launch plan entity. |
| [`get_node_execution()`](#get_node_execution) |  |
| [`get_node_execution_data()`](#get_node_execution_data) | Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available). |
| [`get_project_domain_attributes()`](#get_project_domain_attributes) | This fetches the attributes for a project and domain registered with the Flyte Admin Service. |
| [`get_task()`](#get_task) | This returns a single task for a given identifier. |
| [`get_task_execution()`](#get_task_execution) |  |
| [`get_task_execution_data()`](#get_task_execution_data) | Returns signed URLs to LiteralMap blobs for a task execution's inputs and outputs (when available). |
| [`get_workflow()`](#get_workflow) | This returns a single workflow for a given identifier. |
| [`get_workflow_attributes()`](#get_workflow_attributes) | This fetches the attributes for a project, domain, and workflow registered with the Flyte Admin Service. |
| [`list_active_launch_plans_paginated()`](#list_active_launch_plans_paginated) | Lists Active Launch Plans for a given (project, domain). |
| [`list_executions_paginated()`](#list_executions_paginated) | Lists the executions for a given identifier. |
| [`list_launch_plan_ids_paginated()`](#list_launch_plan_ids_paginated) | Lists launch plan named identifiers for a given project and domain. |
| [`list_launch_plans_paginated()`](#list_launch_plans_paginated) | Lists Launch Plans for a given Identifier (project, domain, name). |
| [`list_matchable_attributes()`](#list_matchable_attributes) | This fetches the attributes for a specific resource type registered with the Flyte Admin Service. |
| [`list_node_executions_for_task_paginated()`](#list_node_executions_for_task_paginated) |  |
| [`list_node_executions_paginated()`](#list_node_executions_paginated) |  |
| [`list_projects()`](#list_projects) | This will return a list of the projects registered with the Flyte Admin Service. |
| [`list_signals()`](#list_signals) | This lists signals. |
| [`list_task_executions_paginated()`](#list_task_executions_paginated) |  |
| [`list_task_ids_paginated()`](#list_task_ids_paginated) | This returns a page of identifiers for the tasks for a given project and domain. |
| [`list_tasks_paginated()`](#list_tasks_paginated) | This returns a page of task metadata for tasks in a given project and domain. |
| [`list_workflow_ids_paginated()`](#list_workflow_ids_paginated) | This returns a page of identifiers for the workflows for a given project and domain. |
| [`list_workflows_paginated()`](#list_workflows_paginated) | This returns a page of workflow meta-information for workflows in a given project and domain. |
| [`recover_execution()`](#recover_execution) | This will recreate an execution with the same spec as the one belonging to the given execution identifier. |
| [`register_project()`](#register_project) | Registers a project along with a set of domains. |
| [`relaunch_execution()`](#relaunch_execution) |  |
| [`set_signal()`](#set_signal) | This sets a signal. |
| [`terminate_execution()`](#terminate_execution) |  |
| [`update_launch_plan()`](#update_launch_plan) | Allows updates to a launch plan at a given identifier. |
| [`update_named_entity()`](#update_named_entity) |  |
| [`update_project()`](#update_project) | Update an existing project specified by id. |
| [`update_project_domain_attributes()`](#update_project_domain_attributes) | This updates the attributes for a project and domain registered with the Flyte Admin Service. |
| [`update_workflow_attributes()`](#update_workflow_attributes) | This updates the attributes for a project, domain, and workflow registered with the Flyte Admin Service. |
| [`with_root_certificate()`](#with_root_certificate) |  |


#### create_download_link()

```python
def create_download_link(
    create_download_link_request: _dataproxy_pb2.CreateDownloadLinkRequest,
) -> _dataproxy_pb2.CreateDownloadLinkResponse
```
| Parameter | Type |
|-|-|
| `create_download_link_request` | `_dataproxy_pb2.CreateDownloadLinkRequest` |

#### create_download_location()

```python
def create_download_location(
    create_download_location_request: _dataproxy_pb2.CreateDownloadLocationRequest,
) -> _dataproxy_pb2.CreateDownloadLocationResponse
```
| Parameter | Type |
|-|-|
| `create_download_location_request` | `_dataproxy_pb2.CreateDownloadLocationRequest` |

#### create_execution()

```python
def create_execution(
    create_execution_request,
) -> e: flyteidl.admin.execution_pb2.ExecutionCreateResponse
```
This will create an execution for the given execution spec.


| Parameter | Type |
|-|-|
| `create_execution_request` |  |

#### create_launch_plan()

```python
def create_launch_plan(
    launch_plan_create_request,
) -> e: flyteidl.admin.launch_plan_pb2.LaunchPlanCreateResponse
```
This will create a launch plan definition in the Admin database.  Once successful, the launch plan object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
    the database must match the existing definition exactly.  This also means that as long as the request
    remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `launch_plan_create_request` |  |

#### create_task()

```python
def create_task(
    task_create_request,
) -> e: flyteidl.admin.task_pb2.TaskCreateResponse
```
This will create a task definition in the Admin database. Once successful, the task object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
    the database must match the existing definition exactly. This also means that as long as the request
    remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `task_create_request` |  |

#### create_upload_location()

```python
def create_upload_location(
    create_upload_location_request: _dataproxy_pb2.CreateUploadLocationRequest,
) -> e: flyteidl.service.dataproxy_pb2.CreateUploadLocationResponse
```
Get a signed url to be used during fast registration


| Parameter | Type |
|-|-|
| `create_upload_location_request` | `_dataproxy_pb2.CreateUploadLocationRequest` |

#### create_workflow()

```python
def create_workflow(
    workflow_create_request,
) -> e: flyteidl.admin.workflow_pb2.WorkflowCreateResponse
```
This will create a workflow definition in the Admin database.  Once successful, the workflow object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
    the database must match the existing definition exactly.  This also means that as long as the request
    remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `workflow_create_request` |  |

#### get_active_launch_plan()

```python
def get_active_launch_plan(
    active_launch_plan_request,
) -> e: flyteidl.admin.launch_plan_pb2.LaunchPlan
```
Retrieves a launch plan entity.



| Parameter | Type |
|-|-|
| `active_launch_plan_request` |  |

#### get_domains()

```python
def get_domains()
```
This will return a list of domains registered with the Flyte Admin Service


#### get_execution()

```python
def get_execution(
    get_object_request,
) -> e: flyteidl.admin.execution_pb2.Execution
```
Returns an execution of a workflow entity.



| Parameter | Type |
|-|-|
| `get_object_request` |  |

#### get_execution_data()

```python
def get_execution_data(
    get_execution_data_request,
) -> e: flyteidl.admin.execution_pb2.WorkflowExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for an execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `get_execution_data_request` |  |

#### get_execution_metrics()

```python
def get_execution_metrics(
    get_execution_metrics_request,
) -> e: flyteidl.admin.execution_pb2.WorkflowExecutionGetMetricsResponse
```
Returns metrics partitioning and categorizing the workflow execution time-series.



| Parameter | Type |
|-|-|
| `get_execution_metrics_request` |  |

#### get_launch_plan()

```python
def get_launch_plan(
    object_get_request,
) -> e: flyteidl.admin.launch_plan_pb2.LaunchPlan
```
Retrieves a launch plan entity.



| Parameter | Type |
|-|-|
| `object_get_request` |  |

#### get_node_execution()

```python
def get_node_execution(
    node_execution_request,
) -> e: flyteidl.admin.node_execution_pb2.NodeExecution
```
| Parameter | Type |
|-|-|
| `node_execution_request` |  |

#### get_node_execution_data()

```python
def get_node_execution_data(
    get_node_execution_data_request,
) -> e: flyteidl.admin.node_execution_pb2.NodeExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `get_node_execution_data_request` |  |

#### get_project_domain_attributes()

```python
def get_project_domain_attributes(
    project_domain_attributes_get_request,
) -> e: flyteidl.admin.ProjectDomainAttributesGetResponse
```
This fetches the attributes for a project and domain registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `project_domain_attributes_get_request` |  |

#### get_task()

```python
def get_task(
    get_object_request,
) -> e: flyteidl.admin.task_pb2.Task
```
This returns a single task for a given identifier.



| Parameter | Type |
|-|-|
| `get_object_request` |  |

#### get_task_execution()

```python
def get_task_execution(
    task_execution_request,
) -> e: flyteidl.admin.task_execution_pb2.TaskExecution
```
| Parameter | Type |
|-|-|
| `task_execution_request` |  |

#### get_task_execution_data()

```python
def get_task_execution_data(
    get_task_execution_data_request,
) -> e: flyteidl.admin.task_execution_pb2.TaskExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for a task execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `get_task_execution_data_request` |  |

#### get_workflow()

```python
def get_workflow(
    get_object_request,
) -> e: flyteidl.admin.workflow_pb2.Workflow
```
This returns a single workflow for a given identifier.



| Parameter | Type |
|-|-|
| `get_object_request` |  |

#### get_workflow_attributes()

```python
def get_workflow_attributes(
    workflow_attributes_get_request,
) -> e: flyteidl.admin.WorkflowAttributesGetResponse
```
This fetches the attributes for a project, domain, and workflow registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `workflow_attributes_get_request` |  |

#### list_active_launch_plans_paginated()

```python
def list_active_launch_plans_paginated(
    active_launch_plan_list_request,
) -> e: flyteidl.admin.launch_plan_pb2.LaunchPlanList
```
Lists Active Launch Plans for a given (project, domain)



| Parameter | Type |
|-|-|
| `active_launch_plan_list_request` |  |

#### list_executions_paginated()

```python
def list_executions_paginated(
    resource_list_request,
) -> e: flyteidl.admin.execution_pb2.ExecutionList
```
Lists the executions for a given identifier.



| Parameter | Type |
|-|-|
| `resource_list_request` |  |

#### list_launch_plan_ids_paginated()

```python
def list_launch_plan_ids_paginated(
    identifier_list_request,
) -> e: flyteidl.admin.common_pb2.NamedEntityIdentifierList
```
Lists launch plan named identifiers for a given project and domain.



| Parameter | Type |
|-|-|
| `identifier_list_request` |  |

#### list_launch_plans_paginated()

```python
def list_launch_plans_paginated(
    resource_list_request,
) -> e: flyteidl.admin.launch_plan_pb2.LaunchPlanList
```
Lists Launch Plans for a given Identifier (project, domain, name)



| Parameter | Type |
|-|-|
| `resource_list_request` |  |

#### list_matchable_attributes()

```python
def list_matchable_attributes(
    matchable_attributes_list_request,
) -> e: flyteidl.admin.ListMatchableAttributesResponse
```
This fetches the attributes for a specific resource type registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `matchable_attributes_list_request` |  |

#### list_node_executions_for_task_paginated()

```python
def list_node_executions_for_task_paginated(
    node_execution_for_task_list_request,
) -> e: flyteidl.admin.node_execution_pb2.NodeExecutionList
```
| Parameter | Type |
|-|-|
| `node_execution_for_task_list_request` |  |

#### list_node_executions_paginated()

```python
def list_node_executions_paginated(
    node_execution_list_request,
) -> e: flyteidl.admin.node_execution_pb2.NodeExecutionList
```
| Parameter | Type |
|-|-|
| `node_execution_list_request` |  |

#### list_projects()

```python
def list_projects(
    project_list_request: typing.Optional[ProjectListRequest],
) -> e: flyteidl.admin.project_pb2.Projects
```
This will return a list of the projects registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `project_list_request` | `typing.Optional[ProjectListRequest]` |

#### list_signals()

```python
def list_signals(
    signal_list_request: SignalListRequest,
) -> SignalList
```
This lists signals


| Parameter | Type |
|-|-|
| `signal_list_request` | `SignalListRequest` |

#### list_task_executions_paginated()

```python
def list_task_executions_paginated(
    task_execution_list_request,
) -> e: flyteidl.admin.task_execution_pb2.TaskExecutionList
```
| Parameter | Type |
|-|-|
| `task_execution_list_request` |  |

#### list_task_ids_paginated()

```python
def list_task_ids_paginated(
    identifier_list_request,
) -> e: flyteidl.admin.common_pb2.NamedEntityIdentifierList
```
This returns a page of identifiers for the tasks for a given project and domain. Filters can also be
specified.

> [!NOTE]
> The name field in the TaskListRequest is ignored.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `identifier_list_request` |  |

#### list_tasks_paginated()

```python
def list_tasks_paginated(
    resource_list_request,
) -> e: flyteidl.admin.task_pb2.TaskList
```
This returns a page of task metadata for tasks in a given project and domain.  Optionally,
specifying a name will limit the results to only tasks with that name in the given project and domain.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `resource_list_request` |  |

#### list_workflow_ids_paginated()

```python
def list_workflow_ids_paginated(
    identifier_list_request,
) -> e: flyteidl.admin.common_pb2.NamedEntityIdentifierList
```
This returns a page of identifiers for the workflows for a given project and domain. Filters can also be
specified.

> [!NOTE]
> The name field in the WorkflowListRequest is ignored.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `identifier_list_request` |  |

#### list_workflows_paginated()

```python
def list_workflows_paginated(
    resource_list_request,
) -> e: flyteidl.admin.workflow_pb2.WorkflowList
```
This returns a page of workflow meta-information for workflows in a given project and domain.  Optionally,
specifying a name will limit the results to only workflows with that name in the given project and domain.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `resource_list_request` |  |

#### recover_execution()

```python
def recover_execution(
    recover_execution_request,
) -> e: flyteidl.admin.execution_pb2.ExecutionRecoverResponse
```
This will recreate an execution with the same spec as the one belonging to the given execution identifier.


| Parameter | Type |
|-|-|
| `recover_execution_request` |  |

#### register_project()

```python
def register_project(
    project_register_request,
) -> e: flyteidl.admin.project_pb2.ProjectRegisterResponse
```
Registers a project along with a set of domains.


| Parameter | Type |
|-|-|
| `project_register_request` |  |

#### relaunch_execution()

```python
def relaunch_execution(
    relaunch_execution_request,
) -> e: flyteidl.admin.execution_pb2.ExecutionCreateResponse
```
| Parameter | Type |
|-|-|
| `relaunch_execution_request` |  |

#### set_signal()

```python
def set_signal(
    signal_set_request: SignalSetRequest,
) -> SignalSetResponse
```
This sets a signal


| Parameter | Type |
|-|-|
| `signal_set_request` | `SignalSetRequest` |

#### terminate_execution()

```python
def terminate_execution(
    terminate_execution_request,
) -> e: flyteidl.admin.execution_pb2.TerminateExecutionResponse
```
| Parameter | Type |
|-|-|
| `terminate_execution_request` |  |

#### update_launch_plan()

```python
def update_launch_plan(
    update_request,
) -> e: flyteidl.admin.launch_plan_pb2.LaunchPlanUpdateResponse
```
Allows updates to a launch plan at a given identifier.  Currently, a launch plan may only have it's state
switched between ACTIVE and INACTIVE.



| Parameter | Type |
|-|-|
| `update_request` |  |

#### update_named_entity()

```python
def update_named_entity(
    update_named_entity_request,
) -> e: flyteidl.admin.common_pb2.NamedEntityUpdateResponse
```
| Parameter | Type |
|-|-|
| `update_named_entity_request` |  |

#### update_project()

```python
def update_project(
    project,
) -> e: flyteidl.admin.project_pb2.ProjectUpdateResponse
```
Update an existing project specified by id.


| Parameter | Type |
|-|-|
| `project` |  |

#### update_project_domain_attributes()

```python
def update_project_domain_attributes(
    project_domain_attributes_update_request,
) -> e: flyteidl.admin.ProjectDomainAttributesUpdateResponse
```
This updates the attributes for a project and domain registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `project_domain_attributes_update_request` |  |

#### update_workflow_attributes()

```python
def update_workflow_attributes(
    workflow_attributes_update_request,
) -> e: flyteidl.admin.WorkflowAttributesUpdateResponse
```
This updates the attributes for a project, domain, and workflow registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `workflow_attributes_update_request` |  |

#### with_root_certificate()

```python
def with_root_certificate(
    cfg: PlatformConfig,
    root_cert_file: str,
) -> RawSynchronousFlyteClient
```
| Parameter | Type |
|-|-|
| `cfg` | `PlatformConfig` |
| `root_cert_file` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `url` |  |  |

