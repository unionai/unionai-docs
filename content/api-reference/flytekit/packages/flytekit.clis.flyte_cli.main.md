---
title: flytekit.clis.flyte_cli.main
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.flyte_cli.main

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteContextManager`](.././flytekit.clis.flyte_cli.main#flytekitclisflyte_climainflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |

### Methods

| Method | Description |
|-|-|
| [`MessageToJson()`](#messagetojson) | Converts protobuf message to JSON format. |
| [`_assumable_iam_role_option()`](#_assumable_iam_role_option) |  |
| [`_cause_option()`](#_cause_option) |  |
| [`_detect_default_config_file()`](#_detect_default_config_file) |  |
| [`_domain_option()`](#_domain_option) |  |
| [`_extract_and_register()`](#_extract_and_register) |  |
| [`_extract_files()`](#_extract_files) | . |
| [`_extract_pair()`](#_extract_pair) | . |
| [`_fetch_and_stringify_literal_map()`](#_fetch_and_stringify_literal_map) | . |
| [`_filename_option()`](#_filename_option) |  |
| [`_files_argument()`](#_files_argument) |  |
| [`_filter_option()`](#_filter_option) |  |
| [`_get_additional_distribution_loc()`](#_get_additional_distribution_loc) | . |
| [`_get_all_node_executions()`](#_get_all_node_executions) |  |
| [`_get_all_task_executions_for_node()`](#_get_all_task_executions_for_node) |  |
| [`_get_client()`](#_get_client) |  |
| [`_get_config_file_path()`](#_get_config_file_path) |  |
| [`_get_io()`](#_get_io) |  |
| [`_get_io_string()`](#_get_io_string) | . |
| [`_get_patch_launch_plan_fn()`](#_get_patch_launch_plan_fn) |  |
| [`_get_user_filepath_home()`](#_get_user_filepath_home) |  |
| [`_host_option()`](#_host_option) |  |
| [`_idl_class_option()`](#_idl_class_option) |  |
| [`_insecure_option()`](#_insecure_option) |  |
| [`_kubernetes_service_acct_option()`](#_kubernetes_service_acct_option) |  |
| [`_limit_option()`](#_limit_option) |  |
| [`_name_option()`](#_name_option) |  |
| [`_named_entity_description_option()`](#_named_entity_description_option) |  |
| [`_named_entity_state_choice()`](#_named_entity_state_choice) |  |
| [`_optional_domain_option()`](#_optional_domain_option) |  |
| [`_optional_name_option()`](#_optional_name_option) |  |
| [`_optional_principal_option()`](#_optional_principal_option) |  |
| [`_optional_project_option()`](#_optional_project_option) |  |
| [`_optional_urn_option()`](#_optional_urn_option) |  |
| [`_optional_urns_only_option()`](#_optional_urns_only_option) |  |
| [`_output_location_prefix_option()`](#_output_location_prefix_option) |  |
| [`_prefix_lines()`](#_prefix_lines) | . |
| [`_principal_option()`](#_principal_option) |  |
| [`_project_description_option()`](#_project_description_option) |  |
| [`_project_identifier_option()`](#_project_identifier_option) |  |
| [`_project_name_option()`](#_project_name_option) |  |
| [`_project_option()`](#_project_option) |  |
| [`_render_error()`](#_render_error) |  |
| [`_render_node_executions()`](#_render_node_executions) |  |
| [`_render_schedule_expr()`](#_render_schedule_expr) |  |
| [`_render_workflow_execution()`](#_render_workflow_execution) |  |
| [`_secho_node_execution_status()`](#_secho_node_execution_status) |  |
| [`_secho_one_execution()`](#_secho_one_execution) |  |
| [`_secho_task_execution_status()`](#_secho_task_execution_status) |  |
| [`_secho_workflow_status()`](#_secho_workflow_status) |  |
| [`_show_all_option()`](#_show_all_option) |  |
| [`_show_io_option()`](#_show_io_option) |  |
| [`_sort_by_option()`](#_sort_by_option) |  |
| [`_state_choice()`](#_state_choice) |  |
| [`_substitute_fast_register_task_args()`](#_substitute_fast_register_task_args) |  |
| [`_terminate_one_execution()`](#_terminate_one_execution) |  |
| [`_token_option()`](#_token_option) |  |
| [`_update_one_launch_plan()`](#_update_one_launch_plan) |  |
| [`_urn_option()`](#_urn_option) |  |
| [`_verbose_option()`](#_verbose_option) |  |
| [`_watch_option()`](#_watch_option) |  |
| [`_welcome_message()`](#_welcome_message) |  |
| [`hydrate_registration_parameters()`](#hydrate_registration_parameters) | This is called at registration time to fill out identifier fields (e. |
| [`replace()`](#replace) | Return a new object replacing specified fields with new values. |


## Methods

#### MessageToJson()

```python
def MessageToJson(
    message,
    preserving_proto_field_name,
    indent,
    sort_keys,
    use_integers_for_enums,
    descriptor_pool,
    float_precision,
    ensure_ascii,
    always_print_fields_with_no_presence,
)
```
Converts protobuf message to JSON format.



| Parameter | Type |
|-|-|
| `message` |  |
| `preserving_proto_field_name` |  |
| `indent` |  |
| `sort_keys` |  |
| `use_integers_for_enums` |  |
| `descriptor_pool` |  |
| `float_precision` |  |
| `ensure_ascii` |  |
| `always_print_fields_with_no_presence` |  |

#### _assumable_iam_role_option()

```python
def _assumable_iam_role_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _cause_option()

```python
def _cause_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _detect_default_config_file()

```python
def _detect_default_config_file()
```
#### _domain_option()

```python
def _domain_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _extract_and_register()

```python
def _extract_and_register(
    client: flytekit.clients.friendly.SynchronousFlyteClient,
    project: str,
    domain: str,
    version: str,
    file_paths: typing.List[str],
    patches: typing.Dict[int, typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]],
)
```
| Parameter | Type |
|-|-|
| `client` | `flytekit.clients.friendly.SynchronousFlyteClient` |
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `file_paths` | `typing.List[str]` |
| `patches` | `typing.Dict[int, typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]]` |

#### _extract_files()

```python
def _extract_files(
    project: str,
    domain: str,
    version: str,
    file_paths: typing.List[str],
    patches: typing.Dict[int, typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]],
) -> List[(flyteidl.core.identifier_pb2.Identifier, T)]
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `file_paths` | `typing.List[str]` |
| `patches` | `typing.Dict[int, typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]]` |

#### _extract_pair()

```python
def _extract_pair(
    object_file: str,
    resource_type: int,
    project: str,
    domain: str,
    version: str,
    patches: typing.Dict[int, typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]],
) -> (flyteidl.core.identifier_pb2.Identifier, T)
```
| Parameter | Type |
|-|-|
| `object_file` | `str` |
| `resource_type` | `int` |
| `project` | `str` |
| `domain` | `str` |
| `version` | `str` |
| `patches` | `typing.Dict[int, typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]]` |

#### _fetch_and_stringify_literal_map()

```python
def _fetch_and_stringify_literal_map(
    path,
    verbose,
) -> Text
```
| Parameter | Type |
|-|-|
| `path` |  |
| `verbose` |  |

#### _filename_option()

```python
def _filename_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _files_argument()

```python
def _files_argument(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _filter_option()

```python
def _filter_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _get_additional_distribution_loc()

```python
def _get_additional_distribution_loc(
    remote_location: str,
    identifier: str,
) -> str
```
| Parameter | Type |
|-|-|
| `remote_location` | `str` |
| `identifier` | `str` |

#### _get_all_node_executions()

```python
def _get_all_node_executions(
    client,
    workflow_execution_identifier,
    task_execution_identifier,
)
```
| Parameter | Type |
|-|-|
| `client` |  |
| `workflow_execution_identifier` |  |
| `task_execution_identifier` |  |

#### _get_all_task_executions_for_node()

```python
def _get_all_task_executions_for_node(
    client,
    node_execution_identifier,
)
```
| Parameter | Type |
|-|-|
| `client` |  |
| `node_execution_identifier` |  |

#### _get_client()

```python
def _get_client(
    host: str,
    insecure: bool,
) -> flytekit.clients.friendly.SynchronousFlyteClient
```
| Parameter | Type |
|-|-|
| `host` | `str` |
| `insecure` | `bool` |

#### _get_config_file_path()

```python
def _get_config_file_path()
```
#### _get_io()

```python
def _get_io(
    node_executions,
    wf_execution,
    show_io,
    verbose,
)
```
| Parameter | Type |
|-|-|
| `node_executions` |  |
| `wf_execution` |  |
| `show_io` |  |
| `verbose` |  |

#### _get_io_string()

```python
def _get_io_string(
    literal_map,
    verbose,
) -> Text
```
| Parameter | Type |
|-|-|
| `literal_map` |  |
| `verbose` |  |

#### _get_patch_launch_plan_fn()

```python
def _get_patch_launch_plan_fn(
    assumable_iam_role: str,
    kubernetes_service_account: str,
    output_location_prefix: str,
) -> typing.Callable[[google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType], google.protobuf.pyext.cpp_message.GeneratedProtocolMessageType]
```
| Parameter | Type |
|-|-|
| `assumable_iam_role` | `str` |
| `kubernetes_service_account` | `str` |
| `output_location_prefix` | `str` |

#### _get_user_filepath_home()

```python
def _get_user_filepath_home()
```
#### _host_option()

```python
def _host_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _idl_class_option()

```python
def _idl_class_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _insecure_option()

```python
def _insecure_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _kubernetes_service_acct_option()

```python
def _kubernetes_service_acct_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _limit_option()

```python
def _limit_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _name_option()

```python
def _name_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _named_entity_description_option()

```python
def _named_entity_description_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _named_entity_state_choice()

```python
def _named_entity_state_choice(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _optional_domain_option()

```python
def _optional_domain_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _optional_name_option()

```python
def _optional_name_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _optional_principal_option()

```python
def _optional_principal_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _optional_project_option()

```python
def _optional_project_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _optional_urn_option()

```python
def _optional_urn_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _optional_urns_only_option()

```python
def _optional_urns_only_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _output_location_prefix_option()

```python
def _output_location_prefix_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _prefix_lines()

```python
def _prefix_lines(
    prefix,
    txt,
) -> Text
```
| Parameter | Type |
|-|-|
| `prefix` |  |
| `txt` |  |

#### _principal_option()

```python
def _principal_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _project_description_option()

```python
def _project_description_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _project_identifier_option()

```python
def _project_identifier_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _project_name_option()

```python
def _project_name_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _project_option()

```python
def _project_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _render_error()

```python
def _render_error(
    error,
)
```
| Parameter | Type |
|-|-|
| `error` |  |

#### _render_node_executions()

```python
def _render_node_executions(
    client,
    node_execs,
    show_io,
    verbose,
    host,
    insecure,
    wf_execution,
)
```
| Parameter | Type |
|-|-|
| `client` |  |
| `node_execs` |  |
| `show_io` |  |
| `verbose` |  |
| `host` |  |
| `insecure` |  |
| `wf_execution` |  |

#### _render_schedule_expr()

```python
def _render_schedule_expr(
    lp,
)
```
| Parameter | Type |
|-|-|
| `lp` |  |

#### _render_workflow_execution()

```python
def _render_workflow_execution(
    wf_execution,
    uri_to_message_map,
    show_io,
    verbose,
)
```
| Parameter | Type |
|-|-|
| `wf_execution` |  |
| `uri_to_message_map` |  |
| `show_io` |  |
| `verbose` |  |

#### _secho_node_execution_status()

```python
def _secho_node_execution_status(
    status,
    nl,
)
```
| Parameter | Type |
|-|-|
| `status` |  |
| `nl` |  |

#### _secho_one_execution()

```python
def _secho_one_execution(
    ex,
    urns_only,
)
```
| Parameter | Type |
|-|-|
| `ex` |  |
| `urns_only` |  |

#### _secho_task_execution_status()

```python
def _secho_task_execution_status(
    status,
    nl,
)
```
| Parameter | Type |
|-|-|
| `status` |  |
| `nl` |  |

#### _secho_workflow_status()

```python
def _secho_workflow_status(
    status,
    nl,
)
```
| Parameter | Type |
|-|-|
| `status` |  |
| `nl` |  |

#### _show_all_option()

```python
def _show_all_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _show_io_option()

```python
def _show_io_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _sort_by_option()

```python
def _sort_by_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _state_choice()

```python
def _state_choice(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _substitute_fast_register_task_args()

```python
def _substitute_fast_register_task_args(
    args: `*args`,
    full_remote_path: str,
    dest_dir: str,
) -> typing.List[str]
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `full_remote_path` | `str` |
| `dest_dir` | `str` |

#### _terminate_one_execution()

```python
def _terminate_one_execution(
    client,
    urn,
    cause,
    shouldPrint,
)
```
| Parameter | Type |
|-|-|
| `client` |  |
| `urn` |  |
| `cause` |  |
| `shouldPrint` |  |

#### _token_option()

```python
def _token_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _update_one_launch_plan()

```python
def _update_one_launch_plan(
    client: flytekit.clients.friendly.SynchronousFlyteClient,
    urn,
    state,
)
```
| Parameter | Type |
|-|-|
| `client` | `flytekit.clients.friendly.SynchronousFlyteClient` |
| `urn` |  |
| `state` |  |

#### _urn_option()

```python
def _urn_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _verbose_option()

```python
def _verbose_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _watch_option()

```python
def _watch_option(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### _welcome_message()

```python
def _welcome_message()
```
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

#### replace()

```python
def replace(
    obj,
    changes,
)
```
Return a new object replacing specified fields with new values.

This is especially useful for frozen classes.  Example usage::

@dataclass(frozen=True)
class C:
x: int
y: int

c = C(1, 2)
c1 = replace(c, x=3)
assert c1.x == 3 and c1.y == 2


| Parameter | Type |
|-|-|
| `obj` |  |
| `changes` |  |

## flytekit.clis.flyte_cli.main.FlyteContextManager

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
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
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
) -> traceback.FrameSummary
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
) -> FlyteContext
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
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

