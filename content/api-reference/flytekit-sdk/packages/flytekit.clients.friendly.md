---
title: flytekit.clients.friendly
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.friendly

## Directory

### Classes

| Class | Description |
|-|-|
| [`SynchronousFlyteClient`](.././flytekit.clients.friendly#flytekitclientsfriendlysynchronousflyteclient) | This is a low-level client that users can use to make direct gRPC service calls to the control plane. |

### Variables

| Property | Type | Description |
|-|-|-|
| `ARTIFACT_TYPE_DECK` | `int` |  |

## flytekit.clients.friendly.SynchronousFlyteClient

This is a low-level client that users can use to make direct gRPC service calls to the control plane. See the
:std:doc:`service spec <idl:protos/docs/service/index>`. This is more user-friendly interface than the
{{< py_class_ref flytekit.clients.raw.RawSynchronousFlyteClient >}} so users should try to use this class
first. Create a client by

```python
SynchronousFlyteClient("your.domain:port", insecure=True)
# insecure should be True if your flyteadmin deployment doesn't have SSL enabled
```


```python
class SynchronousFlyteClient(
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
| [`get_active_launch_plan()`](#get_active_launch_plan) | Retrieves the active launch plan entity given a named entity identifier (project, domain, name). |
| [`get_control_plane_version()`](#get_control_plane_version) | Retrieve the Control Plane version from Flyteadmin. |
| [`get_data()`](#get_data) |  |
| [`get_domains()`](#get_domains) | This returns a list of domains. |
| [`get_download_artifact_signed_url()`](#get_download_artifact_signed_url) | Get a signed url for an artifact. |
| [`get_download_signed_url()`](#get_download_signed_url) |  |
| [`get_execution()`](#get_execution) |  |
| [`get_execution_data()`](#get_execution_data) | Returns signed URLs to LiteralMap blobs for an execution's inputs and outputs (when available). |
| [`get_execution_metrics()`](#get_execution_metrics) | Returns metrics partitioning and categorizing the workflow execution time-series. |
| [`get_node_execution()`](#get_node_execution) |  |
| [`get_node_execution_data()`](#get_node_execution_data) | Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available). |
| [`get_project_domain_attributes()`](#get_project_domain_attributes) | Fetches the custom attributes set for a project and domain combination. |
| [`get_task_execution()`](#get_task_execution) |  |
| [`get_task_execution_data()`](#get_task_execution_data) | Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available). |
| [`get_upload_signed_url()`](#get_upload_signed_url) | Get a signed url to be used during fast registration. |
| [`get_workflow_attributes()`](#get_workflow_attributes) | Fetches the custom attributes set for a project, domain, and workflow combination. |
| [`list_active_launch_plans_paginated()`](#list_active_launch_plans_paginated) | This returns a page of currently active launch plan meta-information for launch plans in a given project and. |
| [`list_executions_paginated()`](#list_executions_paginated) | This returns a page of executions in a given project and domain. |
| [`list_launch_plan_ids_paginated()`](#list_launch_plan_ids_paginated) | This returns a page of identifiers for the launch plans for a given project and domain. |
| [`list_launch_plans_paginated()`](#list_launch_plans_paginated) | This returns a page of launch plan meta-information for launch plans in a given project and domain. |
| [`list_matchable_attributes()`](#list_matchable_attributes) | Fetches all custom attributes for a resource type. |
| [`list_node_executions()`](#list_node_executions) | Get node executions associated with a given workflow execution. |
| [`list_node_executions_for_task_paginated()`](#list_node_executions_for_task_paginated) | This returns nodes spawned by a specific task execution. |
| [`list_node_executions_paginated()`](#list_node_executions_paginated) |  |
| [`list_projects()`](#list_projects) | This will return a list of the projects registered with the Flyte Admin Service. |
| [`list_projects_paginated()`](#list_projects_paginated) | This returns a page of projects. |
| [`list_signals()`](#list_signals) | This lists signals. |
| [`list_task_executions_paginated()`](#list_task_executions_paginated) |  |
| [`list_task_ids_paginated()`](#list_task_ids_paginated) | This returns a page of identifiers for the tasks for a given project and domain. |
| [`list_tasks_paginated()`](#list_tasks_paginated) | This returns a page of task metadata for tasks in a given project and domain. |
| [`list_workflow_ids_paginated()`](#list_workflow_ids_paginated) | This returns a page of identifiers for the workflows for a given project and domain. |
| [`list_workflows_paginated()`](#list_workflows_paginated) | This returns a page of workflow meta-information for workflows in a given project and domain. |
| [`recover_execution()`](#recover_execution) | Recreates a previously-run workflow execution that will only start executing from the last known failure point. |
| [`register_project()`](#register_project) | Registers a project. |
| [`relaunch_execution()`](#relaunch_execution) |  |
| [`set_signal()`](#set_signal) | This sets a signal. |
| [`terminate_execution()`](#terminate_execution) |  |
| [`update_launch_plan()`](#update_launch_plan) | Updates a launch plan. |
| [`update_named_entity()`](#update_named_entity) | Updates the metadata associated with a named entity. |
| [`update_project()`](#update_project) | Update an existing project specified by id. |
| [`update_project_domain_attributes()`](#update_project_domain_attributes) | Sets custom attributes for a project and domain combination. |
| [`update_workflow_attributes()`](#update_workflow_attributes) | Sets custom attributes for a project, domain, and workflow combination. |
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
    project,
    domain,
    name,
    execution_spec,
    inputs,
) -> e: flytekit.models.core.identifier.WorkflowExecutionIdentifier
```
This will create an execution for the given execution spec.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |
| `execution_spec` |  |
| `inputs` |  |

#### create_launch_plan()

```python
def create_launch_plan(
    launch_plan_identifer,
    launch_plan_spec,
)
```
This will create a launch plan definition in the Admin database.  Once successful, the launch plan object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
    the database must match the existing definition exactly.  This also means that as long as the request
    remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `launch_plan_identifer` |  |
| `launch_plan_spec` |  |

#### create_task()

```python
def create_task(
    task_identifer,
    task_spec,
)
```
This will create a task definition in the Admin database. Once successful, the task object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
  the database must match the existing definition exactly. Furthermore, as long as the request
  remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `task_identifer` |  |
| `task_spec` |  |

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
    workflow_identifier,
    workflow_spec,
)
```
This will create a workflow definition in the Admin database. Once successful, the workflow object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
    the database must match the existing definition exactly. Furthermore, as long as the request
    remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `workflow_identifier` |  |
| `workflow_spec` |  |

#### get_active_launch_plan()

```python
def get_active_launch_plan(
    identifier,
) -> e: flytekit.models.launch_plan.LaunchPlan
```
Retrieves the active launch plan entity given a named entity identifier (project, domain, name).  Raises an
error if no active launch plan exists.



| Parameter | Type |
|-|-|
| `identifier` |  |

#### get_control_plane_version()

```python
def get_control_plane_version()
```
Retrieve the Control Plane version from Flyteadmin.

This method calls Flyteadmin's GetVersion API to obtain the current version information of the control plane.
The retrieved version can be used to enable or disable specific features based on the Flyteadmin version.

Returns:
    str: The version string of the control plane.


#### get_data()

```python
def get_data(
    flyte_uri: str,
) -> flyteidl.service.dataproxy_pb2.GetDataResponse
```
| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |

#### get_domains()

```python
def get_domains()
```
This returns a list of domains.

:rtype: list[flytekit.models.Domain]


#### get_download_artifact_signed_url()

```python
def get_download_artifact_signed_url(
    node_id: str,
    project: str,
    domain: str,
    name: str,
    artifact_type: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10775e250>,
    expires_in: datetime.timedelta,
) -> e: flyteidl.service.dataproxy_pb2.CreateDownloadLinkResponse
```
Get a signed url for an artifact.



| Parameter | Type |
|-|-|
| `node_id` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `artifact_type` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10775e250>` |
| `expires_in` | `datetime.timedelta` |

#### get_download_signed_url()

```python
def get_download_signed_url(
    native_url: str,
    expires_in: datetime.timedelta,
) -> flyteidl.service.dataproxy_pb2.CreateDownloadLocationResponse
```
| Parameter | Type |
|-|-|
| `native_url` | `str` |
| `expires_in` | `datetime.timedelta` |

#### get_execution()

```python
def get_execution(
    id,
) -> e: flytekit.models.execution.Execution
```
| Parameter | Type |
|-|-|
| `id` |  |

#### get_execution_data()

```python
def get_execution_data(
    id,
) -> e: flytekit.models.execution.WorkflowExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for an execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `id` |  |

#### get_execution_metrics()

```python
def get_execution_metrics(
    id,
    depth,
) -> e: flyteidl.admin.execution_pb2.WorkflowExecutionGetMetricsResponse
```
Returns metrics partitioning and categorizing the workflow execution time-series.



| Parameter | Type |
|-|-|
| `id` |  |
| `depth` |  |

#### get_node_execution()

```python
def get_node_execution(
    node_execution_identifier,
) -> e: flytekit.models.node_execution.NodeExecution
```
| Parameter | Type |
|-|-|
| `node_execution_identifier` |  |

#### get_node_execution_data()

```python
def get_node_execution_data(
    node_execution_identifier,
) -> flytekit.models.execution.NodeExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `node_execution_identifier` |  |

#### get_project_domain_attributes()

```python
def get_project_domain_attributes(
    project,
    domain,
    resource_type,
) -> n:
```
Fetches the custom attributes set for a project and domain combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `resource_type` |  |

#### get_task_execution()

```python
def get_task_execution(
    id,
) -> e: flytekit.models.admin.task_execution.TaskExecution
```
| Parameter | Type |
|-|-|
| `id` |  |

#### get_task_execution_data()

```python
def get_task_execution_data(
    task_execution_identifier,
) -> e: flytekit.models.execution.NodeExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `task_execution_identifier` |  |

#### get_upload_signed_url()

```python
def get_upload_signed_url(
    project: str,
    domain: str,
    content_md5: typing.Optional[bytes],
    filename: typing.Optional[str],
    expires_in: typing.Optional[datetime.timedelta],
    filename_root: typing.Optional[str],
    add_content_md5_metadata: bool,
) -> e: flyteidl.service.dataproxy_pb2.CreateUploadLocationResponse
```
Get a signed url to be used during fast registration



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `content_md5` | `typing.Optional[bytes]` |
| `filename` | `typing.Optional[str]` |
| `expires_in` | `typing.Optional[datetime.timedelta]` |
| `filename_root` | `typing.Optional[str]` |
| `add_content_md5_metadata` | `bool` |

#### get_workflow_attributes()

```python
def get_workflow_attributes(
    project,
    domain,
    workflow,
    resource_type,
) -> n:
```
Fetches the custom attributes set for a project, domain, and workflow combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `workflow` |  |
| `resource_type` |  |

#### list_active_launch_plans_paginated()

```python
def list_active_launch_plans_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> e: list[flytekit.models.launch_plan.LaunchPlan], str
```
This returns a page of currently active launch plan meta-information for launch plans in a given project and
domain.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_executions_paginated()

```python
def list_executions_paginated(
    project,
    domain,
    limit,
    token,
    filters,
    sort_by,
) -> e: (list[flytekit.models.execution.Execution], Text)
```
This returns a page of executions in a given project and domain.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_launch_plan_ids_paginated()

```python
def list_launch_plan_ids_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> e: list[flytekit.models.common.NamedEntityIdentifier], Text
```
This returns a page of identifiers for the launch plans for a given project and domain. Filters can also be
specified.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_launch_plans_paginated()

```python
def list_launch_plans_paginated(
    identifier,
    limit,
    token,
    filters,
    sort_by,
) -> e: list[flytekit.models.launch_plan.LaunchPlan], str
```
This returns a page of launch plan meta-information for launch plans in a given project and domain.  Optionally,
specifying a name will limit the results to only workflows with that name in the given project and domain.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_matchable_attributes()

```python
def list_matchable_attributes(
    resource_type,
) -> n:
```
Fetches all custom attributes for a resource type.


| Parameter | Type |
|-|-|
| `resource_type` |  |

#### list_node_executions()

```python
def list_node_executions(
    workflow_execution_identifier,
    limit: int,
    token: typing.Optional[str],
    filters: typing.List[flytekit.models.filters.Filter],
    sort_by: flytekit.models.admin.common.Sort,
    unique_parent_id: str,
) -> e: list[flytekit.models.node_execution.NodeExecution], Text
```
Get node executions associated with a given workflow execution.



| Parameter | Type |
|-|-|
| `workflow_execution_identifier` |  |
| `limit` | `int` |
| `token` | `typing.Optional[str]` |
| `filters` | `typing.List[flytekit.models.filters.Filter]` |
| `sort_by` | `flytekit.models.admin.common.Sort` |
| `unique_parent_id` | `str` |

#### list_node_executions_for_task_paginated()

```python
def list_node_executions_for_task_paginated(
    task_execution_identifier,
    limit,
    token,
    filters,
    sort_by,
) -> e: list[flytekit.models.node_execution.NodeExecution], Text
```
This returns nodes spawned by a specific task execution.  This is generally from things like dynamic tasks.


| Parameter | Type |
|-|-|
| `task_execution_identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

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

#### list_projects_paginated()

```python
def list_projects_paginated(
    limit,
    token,
    filters,
    sort_by,
) -> e: (list[flytekit.models.Project], Text)
```
This returns a page of projects.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

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
    node_execution_identifier,
    limit,
    token,
    filters,
    sort_by,
) -> e: (list[flytekit.models.admin.task_execution.TaskExecution], Text)
```
| Parameter | Type |
|-|-|
| `node_execution_identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_task_ids_paginated()

```python
def list_task_ids_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> e: list[flytekit.models.common.NamedEntityIdentifier], Text
```
This returns a page of identifiers for the tasks for a given project and domain. Filters can also be
specified.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_tasks_paginated()

```python
def list_tasks_paginated(
    identifier,
    limit,
    token,
    filters,
    sort_by,
) -> e: list[flytekit.models.task.Task], Text
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
| `identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_workflow_ids_paginated()

```python
def list_workflow_ids_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> e: list[flytekit.models.common.NamedEntityIdentifier], Text
```
This returns a page of identifiers for the workflows for a given project and domain. Filters can also be
specified.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
    The user of the API is responsible for providing this token.

> [!NOTE]
> If entries are added to the database between requests for different pages, it is possible to receive
    entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_workflows_paginated()

```python
def list_workflows_paginated(
    identifier,
    limit,
    token,
    filters,
    sort_by,
) -> e: list[flytekit.models.admin.workflow.Workflow], Text
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
| `identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### recover_execution()

```python
def recover_execution(
    id,
    name: str,
) -> e: flytekit.models.core.identifier.WorkflowExecutionIdentifier
```
Recreates a previously-run workflow execution that will only start executing from the last known failure point.


| Parameter | Type |
|-|-|
| `id` |  |
| `name` | `str` |

#### register_project()

```python
def register_project(
    project,
) -> e: flyteidl.admin.project_pb2.ProjectRegisterResponse
```
Registers a project.


| Parameter | Type |
|-|-|
| `project` |  |

#### relaunch_execution()

```python
def relaunch_execution(
    id,
    name,
) -> e: flytekit.models.core.identifier.WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |

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
    id,
    cause,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `cause` |  |

#### update_launch_plan()

```python
def update_launch_plan(
    id,
    state,
)
```
Updates a launch plan.  Currently, this can only be used to update a given launch plan's state (ACTIVE v.
INACTIVE) for schedules.  If a launch plan with a given project, domain, and name is set to ACTIVE,
then any other launch plan with the same project, domain, and name that was set to ACTIVE will be switched to
INACTIVE in one transaction.



| Parameter | Type |
|-|-|
| `id` |  |
| `state` |  |

#### update_named_entity()

```python
def update_named_entity(
    resource_type,
    id,
    metadata,
)
```
Updates the metadata associated with a named entity.  A named entity is designated a resource, e.g. a workflow,
task or launch plan specified by {project, domain, name} across all versions of the resource.



| Parameter | Type |
|-|-|
| `resource_type` |  |
| `id` |  |
| `metadata` |  |

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
    project,
    domain,
    matching_attributes,
) -> n:
```
Sets custom attributes for a project and domain combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `matching_attributes` |  |

#### update_workflow_attributes()

```python
def update_workflow_attributes(
    project,
    domain,
    workflow,
    matching_attributes,
) -> n:
```
Sets custom attributes for a project, domain, and workflow combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `workflow` |  |
| `matching_attributes` |  |

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
| `raw` |  | {{< multiline >}}Gives access to the raw client
:rtype: flytekit.clients.raw.RawSynchronousFlyteClient
{{< /multiline >}} |
| `url` |  |  |

