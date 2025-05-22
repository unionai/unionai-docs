---
title: Packages
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Packages

| Package | Description |
|-|-|
| [`flytekit`](flytekit) | This package contains all of the most common abstractions you'll need to write Flyte workflows and extend Flytekit. |
| [`flytekit.bin.entrypoint`](flytekit.bin.entrypoint) |  |
| [`flytekit.clients.auth.auth_client`](flytekit.clients.auth.auth_client) |  |
| [`flytekit.clients.auth.authenticator`](flytekit.clients.auth.authenticator) |  |
| [`flytekit.clients.auth.default_html`](flytekit.clients.auth.default_html) |  |
| [`flytekit.clients.auth.exceptions`](flytekit.clients.auth.exceptions) |  |
| [`flytekit.clients.auth.keyring`](flytekit.clients.auth.keyring) |  |
| [`flytekit.clients.auth.token_client`](flytekit.clients.auth.token_client) |  |
| [`flytekit.clients.auth_helper`](flytekit.clients.auth_helper) |  |
| [`flytekit.clients.friendly`](flytekit.clients.friendly) |  |
| [`flytekit.clients.grpc_utils.auth_interceptor`](flytekit.clients.grpc_utils.auth_interceptor) |  |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor`](flytekit.clients.grpc_utils.default_metadata_interceptor) |  |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor`](flytekit.clients.grpc_utils.wrap_exception_interceptor) |  |
| [`flytekit.clients.helpers`](flytekit.clients.helpers) |  |
| [`flytekit.clients.raw`](flytekit.clients.raw) |  |
| [`flytekit.clis.helpers`](flytekit.clis.helpers) |  |
| [`flytekit.clis.sdk_in_container.backfill`](flytekit.clis.sdk_in_container.backfill) |  |
| [`flytekit.clis.sdk_in_container.constants`](flytekit.clis.sdk_in_container.constants) |  |
| [`flytekit.clis.sdk_in_container.executions`](flytekit.clis.sdk_in_container.executions) |  |
| [`flytekit.clis.sdk_in_container.helpers`](flytekit.clis.sdk_in_container.helpers) |  |
| [`flytekit.clis.sdk_in_container.metrics`](flytekit.clis.sdk_in_container.metrics) |  |
| [`flytekit.clis.sdk_in_container.package`](flytekit.clis.sdk_in_container.package) |  |
| [`flytekit.clis.sdk_in_container.serialize`](flytekit.clis.sdk_in_container.serialize) |  |
| [`flytekit.clis.sdk_in_container.serve`](flytekit.clis.sdk_in_container.serve) |  |
| [`flytekit.clis.sdk_in_container.utils`](flytekit.clis.sdk_in_container.utils) |  |
| [`flytekit.clis.version`](flytekit.clis.version) |  |
| [`flytekit.configuration`](flytekit.configuration) | # Configuration. |
| [`flytekit.configuration.default_images`](flytekit.configuration.default_images) |  |
| [`flytekit.configuration.feature_flags`](flytekit.configuration.feature_flags) |  |
| [`flytekit.configuration.file`](flytekit.configuration.file) |  |
| [`flytekit.configuration.internal`](flytekit.configuration.internal) |  |
| [`flytekit.configuration.plugin`](flytekit.configuration.plugin) | Defines a plugin API allowing other libraries to modify the behavior of flytekit. |
| [`flytekit.core.annotation`](flytekit.core.annotation) |  |
| [`flytekit.core.array_node`](flytekit.core.array_node) |  |
| [`flytekit.core.array_node_map_task`](flytekit.core.array_node_map_task) |  |
| [`flytekit.core.artifact`](flytekit.core.artifact) |  |
| [`flytekit.core.artifact_utils`](flytekit.core.artifact_utils) |  |
| [`flytekit.core.base_sql_task`](flytekit.core.base_sql_task) |  |
| [`flytekit.core.base_task`](flytekit.core.base_task) | # flytekit. |
| [`flytekit.core.cache`](flytekit.core.cache) |  |
| [`flytekit.core.checkpointer`](flytekit.core.checkpointer) |  |
| [`flytekit.core.class_based_resolver`](flytekit.core.class_based_resolver) |  |
| [`flytekit.core.condition`](flytekit.core.condition) |  |
| [`flytekit.core.constants`](flytekit.core.constants) |  |
| [`flytekit.core.container_task`](flytekit.core.container_task) |  |
| [`flytekit.core.context_manager`](flytekit.core.context_manager) |  |
| [`flytekit.core.data_persistence`](flytekit.core.data_persistence) | The Data persistence module is used by core flytekit and most of the core TypeTransformers to manage data fetch & store,. |
| [`flytekit.core.docstring`](flytekit.core.docstring) |  |
| [`flytekit.core.environment`](flytekit.core.environment) |  |
| [`flytekit.core.gate`](flytekit.core.gate) |  |
| [`flytekit.core.hash`](flytekit.core.hash) |  |
| [`flytekit.core.interface`](flytekit.core.interface) |  |
| [`flytekit.core.launch_plan`](flytekit.core.launch_plan) |  |
| [`flytekit.core.legacy_map_task`](flytekit.core.legacy_map_task) | Flytekit map tasks specify how to run a single task across a list of inputs. |
| [`flytekit.core.local_cache`](flytekit.core.local_cache) |  |
| [`flytekit.core.local_fsspec`](flytekit.core.local_fsspec) |  |
| [`flytekit.core.mock_stats`](flytekit.core.mock_stats) |  |
| [`flytekit.core.node`](flytekit.core.node) |  |
| [`flytekit.core.node_creation`](flytekit.core.node_creation) |  |
| [`flytekit.core.notification`](flytekit.core.notification) | Notifications are primarily used when defining Launch Plans (also can be used when launching executions) and will trigger. |
| [`flytekit.core.options`](flytekit.core.options) |  |
| [`flytekit.core.pod_template`](flytekit.core.pod_template) |  |
| [`flytekit.core.promise`](flytekit.core.promise) |  |
| [`flytekit.core.python_auto_container`](flytekit.core.python_auto_container) |  |
| [`flytekit.core.python_customized_container_task`](flytekit.core.python_customized_container_task) |  |
| [`flytekit.core.python_function_task`](flytekit.core.python_function_task) |  |
| [`flytekit.core.reference`](flytekit.core.reference) |  |
| [`flytekit.core.reference_entity`](flytekit.core.reference_entity) |  |
| [`flytekit.core.resources`](flytekit.core.resources) |  |
| [`flytekit.core.schedule`](flytekit.core.schedule) |  |
| [`flytekit.core.shim_task`](flytekit.core.shim_task) |  |
| [`flytekit.core.task`](flytekit.core.task) |  |
| [`flytekit.core.testing`](flytekit.core.testing) |  |
| [`flytekit.core.tracked_abc`](flytekit.core.tracked_abc) |  |
| [`flytekit.core.tracker`](flytekit.core.tracker) |  |
| [`flytekit.core.type_engine`](flytekit.core.type_engine) |  |
| [`flytekit.core.type_helpers`](flytekit.core.type_helpers) |  |
| [`flytekit.core.type_match_checking`](flytekit.core.type_match_checking) |  |
| [`flytekit.core.utils`](flytekit.core.utils) |  |
| [`flytekit.core.worker_queue`](flytekit.core.worker_queue) |  |
| [`flytekit.core.workflow`](flytekit.core.workflow) |  |
| [`flytekit.deck.deck`](flytekit.deck.deck) |  |
| [`flytekit.deck.renderer`](flytekit.deck.renderer) |  |
| [`flytekit.exceptions.base`](flytekit.exceptions.base) |  |
| [`flytekit.exceptions.eager`](flytekit.exceptions.eager) |  |
| [`flytekit.exceptions.scopes`](flytekit.exceptions.scopes) |  |
| [`flytekit.exceptions.system`](flytekit.exceptions.system) |  |
| [`flytekit.exceptions.user`](flytekit.exceptions.user) |  |
| [`flytekit.exceptions.utils`](flytekit.exceptions.utils) |  |
| [`flytekit.experimental.eager_function`](flytekit.experimental.eager_function) |  |
| [`flytekit.extend.backend.base_connector`](flytekit.extend.backend.base_connector) |  |
| [`flytekit.extend.backend.utils`](flytekit.extend.backend.utils) |  |
| [`flytekit.extras.accelerators`](flytekit.extras.accelerators) | ## Specifying Accelerators. |
| [`flytekit.extras.cloud_pickle_resolver`](flytekit.extras.cloud_pickle_resolver) |  |
| [`flytekit.extras.pydantic_transformer.decorator`](flytekit.extras.pydantic_transformer.decorator) |  |
| [`flytekit.extras.sqlite3.task`](flytekit.extras.sqlite3.task) |  |
| [`flytekit.extras.tasks.shell`](flytekit.extras.tasks.shell) |  |
| [`flytekit.image_spec.default_builder`](flytekit.image_spec.default_builder) |  |
| [`flytekit.image_spec.image_spec`](flytekit.image_spec.image_spec) |  |
| [`flytekit.interaction.click_types`](flytekit.interaction.click_types) |  |
| [`flytekit.interaction.parse_stdin`](flytekit.interaction.parse_stdin) |  |
| [`flytekit.interaction.rich_utils`](flytekit.interaction.rich_utils) |  |
| [`flytekit.interaction.string_literals`](flytekit.interaction.string_literals) |  |
| [`flytekit.interactive`](flytekit.interactive) |  |
| [`flytekit.interactive.constants`](flytekit.interactive.constants) |  |
| [`flytekit.interactive.utils`](flytekit.interactive.utils) |  |
| [`flytekit.interactive.vscode_lib.config`](flytekit.interactive.vscode_lib.config) |  |
| [`flytekit.interactive.vscode_lib.decorator`](flytekit.interactive.vscode_lib.decorator) |  |
| [`flytekit.interactive.vscode_lib.vscode_constants`](flytekit.interactive.vscode_lib.vscode_constants) |  |
| [`flytekit.interfaces.cli_identifiers`](flytekit.interfaces.cli_identifiers) |  |
| [`flytekit.interfaces.random`](flytekit.interfaces.random) |  |
| [`flytekit.interfaces.stats.client`](flytekit.interfaces.stats.client) |  |
| [`flytekit.interfaces.stats.taggable`](flytekit.interfaces.stats.taggable) |  |
| [`flytekit.lazy_import.lazy_module`](flytekit.lazy_import.lazy_module) |  |
| [`flytekit.loggers`](flytekit.loggers) |  |
| [`flytekit.models.admin.common`](flytekit.models.admin.common) |  |
| [`flytekit.models.admin.task_execution`](flytekit.models.admin.task_execution) |  |
| [`flytekit.models.admin.workflow`](flytekit.models.admin.workflow) |  |
| [`flytekit.models.annotation`](flytekit.models.annotation) |  |
| [`flytekit.models.array_job`](flytekit.models.array_job) |  |
| [`flytekit.models.common`](flytekit.models.common) |  |
| [`flytekit.models.core.catalog`](flytekit.models.core.catalog) |  |
| [`flytekit.models.core.compiler`](flytekit.models.core.compiler) |  |
| [`flytekit.models.core.condition`](flytekit.models.core.condition) |  |
| [`flytekit.models.core.errors`](flytekit.models.core.errors) |  |
| [`flytekit.models.core.execution`](flytekit.models.core.execution) |  |
| [`flytekit.models.core.identifier`](flytekit.models.core.identifier) |  |
| [`flytekit.models.core.types`](flytekit.models.core.types) |  |
| [`flytekit.models.core.workflow`](flytekit.models.core.workflow) |  |
| [`flytekit.models.documentation`](flytekit.models.documentation) |  |
| [`flytekit.models.domain`](flytekit.models.domain) |  |
| [`flytekit.models.dynamic_job`](flytekit.models.dynamic_job) |  |
| [`flytekit.models.event`](flytekit.models.event) |  |
| [`flytekit.models.execution`](flytekit.models.execution) |  |
| [`flytekit.models.filters`](flytekit.models.filters) |  |
| [`flytekit.models.interface`](flytekit.models.interface) |  |
| [`flytekit.models.launch_plan`](flytekit.models.launch_plan) |  |
| [`flytekit.models.literals`](flytekit.models.literals) |  |
| [`flytekit.models.matchable_resource`](flytekit.models.matchable_resource) |  |
| [`flytekit.models.named_entity`](flytekit.models.named_entity) |  |
| [`flytekit.models.node_execution`](flytekit.models.node_execution) |  |
| [`flytekit.models.presto`](flytekit.models.presto) | This is a deprecated module. |
| [`flytekit.models.project`](flytekit.models.project) |  |
| [`flytekit.models.qubole`](flytekit.models.qubole) | This is a deprecated module. |
| [`flytekit.models.schedule`](flytekit.models.schedule) |  |
| [`flytekit.models.security`](flytekit.models.security) |  |
| [`flytekit.models.task`](flytekit.models.task) |  |
| [`flytekit.models.types`](flytekit.models.types) |  |
| [`flytekit.models.workflow_closure`](flytekit.models.workflow_closure) |  |
| [`flytekit.remote.backfill`](flytekit.remote.backfill) |  |
| [`flytekit.remote.data`](flytekit.remote.data) |  |
| [`flytekit.remote.entities`](flytekit.remote.entities) | This module contains shadow entities for all Flyte entities as represented in Flyte Admin / Control Plane. |
| [`flytekit.remote.executions`](flytekit.remote.executions) |  |
| [`flytekit.remote.interface`](flytekit.remote.interface) |  |
| [`flytekit.remote.lazy_entity`](flytekit.remote.lazy_entity) |  |
| [`flytekit.remote.metrics`](flytekit.remote.metrics) |  |
| [`flytekit.remote.remote`](flytekit.remote.remote) | This module provides the ``FlyteRemote`` object, which is the end-user's main starting point for interacting. |
| [`flytekit.remote.remote_callable`](flytekit.remote.remote_callable) |  |
| [`flytekit.remote.remote_fs`](flytekit.remote.remote_fs) |  |
| [`flytekit.sensor.base_sensor`](flytekit.sensor.base_sensor) |  |
| [`flytekit.sensor.file_sensor`](flytekit.sensor.file_sensor) |  |
| [`flytekit.sensor.sensor_engine`](flytekit.sensor.sensor_engine) |  |
| [`flytekit.tools.fast_registration`](flytekit.tools.fast_registration) |  |
| [`flytekit.tools.ignore`](flytekit.tools.ignore) |  |
| [`flytekit.tools.interactive`](flytekit.tools.interactive) |  |
| [`flytekit.tools.module_loader`](flytekit.tools.module_loader) |  |
| [`flytekit.tools.repo`](flytekit.tools.repo) |  |
| [`flytekit.tools.script_mode`](flytekit.tools.script_mode) |  |
| [`flytekit.tools.serialize_helpers`](flytekit.tools.serialize_helpers) |  |
| [`flytekit.tools.subprocess`](flytekit.tools.subprocess) |  |
| [`flytekit.tools.translator`](flytekit.tools.translator) |  |
| [`flytekit.types.directory`](flytekit.types.directory) | Similar to {{< py_class_ref flytekit.types.file.FlyteFile >}} there are some 'preformatted' directory types. |
| [`flytekit.types.directory.types`](flytekit.types.directory.types) |  |
| [`flytekit.types.error.error`](flytekit.types.error.error) |  |
| [`flytekit.types.file`](flytekit.types.file) | Flytekit File Type. |
| [`flytekit.types.file.file`](flytekit.types.file.file) |  |
| [`flytekit.types.iterator.iterator`](flytekit.types.iterator.iterator) |  |
| [`flytekit.types.iterator.json_iterator`](flytekit.types.iterator.json_iterator) |  |
| [`flytekit.types.numpy.ndarray`](flytekit.types.numpy.ndarray) |  |
| [`flytekit.types.pickle.pickle`](flytekit.types.pickle.pickle) |  |
| [`flytekit.types.schema.types`](flytekit.types.schema.types) |  |
| [`flytekit.types.schema.types_pandas`](flytekit.types.schema.types_pandas) |  |
| [`flytekit.types.structured`](flytekit.types.structured) |  |
| [`flytekit.types.structured.basic_dfs`](flytekit.types.structured.basic_dfs) |  |
| [`flytekit.types.structured.structured_dataset`](flytekit.types.structured.structured_dataset) |  |
| [`flytekit.utils.asyn`](flytekit.utils.asyn) | Manages an async event loop on another thread. |
| [`flytekit.utils.dict_formatter`](flytekit.utils.dict_formatter) |  |
| [`flytekit.utils.pbhash`](flytekit.utils.pbhash) |  |
| [`flytekit.utils.rate_limiter`](flytekit.utils.rate_limiter) |  |
