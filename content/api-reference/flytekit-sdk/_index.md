---
title: Flytekit SDK
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# Flytekit SDK

These are the Flytekit SDK API docs.

Flytekit is the core Python SDK for the Union and Flyte platforms.


## Developing on Flyte

For developing on the Flyte platform you need to add the `flytekit` package to your project:

```shell
$ uv add flytekit
```

This will install the Flytekit SDK and the `pyflyte` command-line tool.

When working with the FLytekit SDK you will be using the `pyflyte` CLI and the Flytekit SDK docs (not the Union SDK docs).


## Developing on Union

For developing on the Union platform you need to add the `union` package to your project:

```shell
$ uv add union
```

This will install the Union SDK, which is a superset of the Flytekit SDK.
It will also install the `union` command-line tool.

When working with the Union SDK you will be using the `union` CLI and both the Flytekit SDK and the Union SDK docs.


## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekit.clients.auth.auth_client.AuthorizationClient`](packages/flytekit.clients.auth.auth_client/authorizationclient) | Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`flytekit.clients.auth.auth_client.AuthorizationCode`](packages/flytekit.clients.auth.auth_client/authorizationcode) |  |
| [`flytekit.clients.auth.auth_client.EndpointMetadata`](packages/flytekit.clients.auth.auth_client/endpointmetadata) | This class can be used to control the rendering of the page on login successful or failure. |
| [`flytekit.clients.auth.auth_client.OAuthCallbackHandler`](packages/flytekit.clients.auth.auth_client/oauthcallbackhandler) | A simple wrapper around BaseHTTPServer. |
| [`flytekit.clients.auth.auth_client.OAuthHTTPServer`](packages/flytekit.clients.auth.auth_client/oauthhttpserver) | A simple wrapper around the BaseHTTPServer. |
| [`flytekit.clients.auth.authenticator.Authenticator`](packages/flytekit.clients.auth.authenticator/authenticator) | Base authenticator for all authentication flows. |
| [`flytekit.clients.auth.authenticator.ClientConfig`](packages/flytekit.clients.auth.authenticator/clientconfig) | Client Configuration that is needed by the authenticator. |
| [`flytekit.clients.auth.authenticator.ClientConfigStore`](packages/flytekit.clients.auth.authenticator/clientconfigstore) | Client Config store retrieve client config. |
| [`flytekit.clients.auth.authenticator.ClientCredentialsAuthenticator`](packages/flytekit.clients.auth.authenticator/clientcredentialsauthenticator) | This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`flytekit.clients.auth.authenticator.CommandAuthenticator`](packages/flytekit.clients.auth.authenticator/commandauthenticator) | This Authenticator retrieves access_token using the provided command. |
| [`flytekit.clients.auth.authenticator.DeviceCodeAuthenticator`](packages/flytekit.clients.auth.authenticator/devicecodeauthenticator) | This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`flytekit.clients.auth.authenticator.PKCEAuthenticator`](packages/flytekit.clients.auth.authenticator/pkceauthenticator) | This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`flytekit.clients.auth.authenticator.StaticClientConfigStore`](packages/flytekit.clients.auth.authenticator/staticclientconfigstore) |  |
| [`flytekit.clients.auth.exceptions.AccessTokenNotFoundError`](packages/flytekit.clients.auth.exceptions/accesstokennotfounderror) | This error is raised with Access token is not found or if Refreshing the token fails. |
| [`flytekit.clients.auth.exceptions.AuthenticationError`](packages/flytekit.clients.auth.exceptions/authenticationerror) | This is raised for any AuthenticationError. |
| [`flytekit.clients.auth.exceptions.AuthenticationPending`](packages/flytekit.clients.auth.exceptions/authenticationpending) | This is raised if the token endpoint returns authentication pending. |
| [`flytekit.clients.auth.keyring.Credentials`](packages/flytekit.clients.auth.keyring/credentials) | Stores the credentials together. |
| [`flytekit.clients.auth.keyring.KeyringStore`](packages/flytekit.clients.auth.keyring/keyringstore) | Methods to access Keyring Store. |
| [`flytekit.clients.auth.token_client.DeviceCodeResponse`](packages/flytekit.clients.auth.token_client/devicecoderesponse) | Response from device auth flow endpoint. |
| [`flytekit.clients.auth.token_client.GrantType`](packages/flytekit.clients.auth.token_client/granttype) |  |
| [`flytekit.clients.auth_helper.AuthenticationHTTPAdapter`](packages/flytekit.clients.auth_helper/authenticationhttpadapter) | A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`flytekit.clients.auth_helper.RemoteClientConfigStore`](packages/flytekit.clients.auth_helper/remoteclientconfigstore) | This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |
| [`flytekit.clients.friendly.SynchronousFlyteClient`](packages/flytekit.clients.friendly/synchronousflyteclient) | This is a low-level client that users can use to make direct gRPC service calls to the control plane. |
| [`flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor`](packages/flytekit.clients.grpc_utils.auth_interceptor/authunaryinterceptor) | This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`flytekit.clients.grpc_utils.deadline_interceptor.ScopedGrpcDeadlineInterceptor`](packages/flytekit.clients.grpc_utils.deadline_interceptor/scopedgrpcdeadlineinterceptor) | Applies the currently scoped gRPC timeout to unary-unary calls. |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor.DefaultMetadataInterceptor`](packages/flytekit.clients.grpc_utils.default_metadata_interceptor/defaultmetadatainterceptor) |  |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.RetryExceptionWrapperInterceptor`](packages/flytekit.clients.grpc_utils.wrap_exception_interceptor/retryexceptionwrapperinterceptor) |  |
| [`flytekit.clients.raw.RawSynchronousFlyteClient`](packages/flytekit.clients.raw/rawsynchronousflyteclient) | This is a thin synchronous wrapper around the auto-generated GRPC stubs for communicating with the admin service. |
| [`flytekit.clis.sdk_in_container.build.BuildCommand`](packages/flytekit.clis.sdk_in_container.build/buildcommand) | A click command group for building a image for flyte workflows & tasks in a file. |
| [`flytekit.clis.sdk_in_container.build.BuildParams`](packages/flytekit.clis.sdk_in_container.build/buildparams) |  |
| [`flytekit.clis.sdk_in_container.build.BuildWorkflowCommand`](packages/flytekit.clis.sdk_in_container.build/buildworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`flytekit.clis.sdk_in_container.run.DynamicEntityLaunchCommand`](packages/flytekit.clis.sdk_in_container.run/dynamicentitylaunchcommand) | This is a dynamic command that is created for each launch plan. |
| [`flytekit.clis.sdk_in_container.run.Entities`](packages/flytekit.clis.sdk_in_container.run/entities) | NamedTuple to group all entities in a file. |
| [`flytekit.clis.sdk_in_container.run.RemoteEntityGroup`](packages/flytekit.clis.sdk_in_container.run/remoteentitygroup) | click multicommand that retrieves launchplans from a remote flyte instance and executes them. |
| [`flytekit.clis.sdk_in_container.run.RunCommand`](packages/flytekit.clis.sdk_in_container.run/runcommand) | A click command group for registering and executing flyte workflows & tasks in a file. |
| [`flytekit.clis.sdk_in_container.run.RunLevelComputedParams`](packages/flytekit.clis.sdk_in_container.run/runlevelcomputedparams) | This class is used to store the computed parameters that are used to run a workflow / task / launchplan. |
| [`flytekit.clis.sdk_in_container.run.RunLevelParams`](packages/flytekit.clis.sdk_in_container.run/runlevelparams) | This class is used to store the parameters that are used to run a workflow / task / launchplan. |
| [`flytekit.clis.sdk_in_container.run.WorkflowCommand`](packages/flytekit.clis.sdk_in_container.run/workflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`flytekit.clis.sdk_in_container.run.YamlFileReadingCommand`](packages/flytekit.clis.sdk_in_container.run/yamlfilereadingcommand) |  |
| [`flytekit.clis.sdk_in_container.serialize.SerializationMode`](packages/flytekit.clis.sdk_in_container.serialize/serializationmode) |  |
| [`flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand`](packages/flytekit.clis.sdk_in_container.utils/errorhandlingcommand) | Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`flytekit.clis.sdk_in_container.utils.PyFlyteParams`](packages/flytekit.clis.sdk_in_container.utils/pyflyteparams) |  |
| [`flytekit.configuration.AuthType`](packages/flytekit.configuration/authtype) |  |
| [`flytekit.configuration.AzureBlobStorageConfig`](packages/flytekit.configuration/azureblobstorageconfig) | Any Azure Blob Storage specific configuration. |
| [`flytekit.configuration.Config`](packages/flytekit.configuration/config) | This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.configuration.DataConfig`](packages/flytekit.configuration/dataconfig) | Any data storage specific configuration. |
| [`flytekit.configuration.EntrypointSettings`](packages/flytekit.configuration/entrypointsettings) | This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`flytekit.configuration.FastSerializationSettings`](packages/flytekit.configuration/fastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.configuration.GCSConfig`](packages/flytekit.configuration/gcsconfig) | Any GCS specific configuration. |
| [`flytekit.configuration.GenericPersistenceConfig`](packages/flytekit.configuration/genericpersistenceconfig) | Data storage configuration that applies across any provider. |
| [`flytekit.configuration.Image`](packages/flytekit.configuration/image) | Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.configuration.ImageConfig`](packages/flytekit.configuration/imageconfig) | We recommend you to use ImageConfig. |
| [`flytekit.configuration.LocalConfig`](packages/flytekit.configuration/localconfig) | Any configuration specific to local runs. |
| [`flytekit.configuration.PlatformConfig`](packages/flytekit.configuration/platformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.configuration.S3Config`](packages/flytekit.configuration/s3config) | S3 specific configuration. |
| [`flytekit.configuration.SecretsConfig`](packages/flytekit.configuration/secretsconfig) | Configuration for secrets. |
| [`flytekit.configuration.SerializationSettings`](packages/flytekit.configuration/serializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.configuration.StatsConfig`](packages/flytekit.configuration/statsconfig) | Configuration for sending statsd. |
| [`flytekit.configuration.TaskConfig`](packages/flytekit.configuration/taskconfig) | Any Project/Domain/Org configuration. |
| [`flytekit.configuration.default_images.DefaultImages`](packages/flytekit.configuration.default_images/defaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`flytekit.configuration.default_images.PythonVersion`](packages/flytekit.configuration.default_images/pythonversion) |  |
| [`flytekit.configuration.feature_flags.FeatureFlags`](packages/flytekit.configuration.feature_flags/featureflags) |  |
| [`flytekit.configuration.file.ConfigEntry`](packages/flytekit.configuration.file/configentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`flytekit.configuration.file.ConfigFile`](packages/flytekit.configuration.file/configfile) |  |
| [`flytekit.configuration.file.LegacyConfigEntry`](packages/flytekit.configuration.file/legacyconfigentry) | Creates a record for the config entry. |
| [`flytekit.configuration.file.YamlConfigEntry`](packages/flytekit.configuration.file/yamlconfigentry) | Creates a record for the config entry. |
| [`flytekit.configuration.internal.AWS`](packages/flytekit.configuration.internal/aws) |  |
| [`flytekit.configuration.internal.AZURE`](packages/flytekit.configuration.internal/azure) |  |
| [`flytekit.configuration.internal.Credentials`](packages/flytekit.configuration.internal/credentials) |  |
| [`flytekit.configuration.internal.GCP`](packages/flytekit.configuration.internal/gcp) |  |
| [`flytekit.configuration.internal.Images`](packages/flytekit.configuration.internal/images) |  |
| [`flytekit.configuration.internal.Local`](packages/flytekit.configuration.internal/local) |  |
| [`flytekit.configuration.internal.LocalSDK`](packages/flytekit.configuration.internal/localsdk) |  |
| [`flytekit.configuration.internal.Persistence`](packages/flytekit.configuration.internal/persistence) |  |
| [`flytekit.configuration.internal.Platform`](packages/flytekit.configuration.internal/platform) |  |
| [`flytekit.configuration.internal.Secrets`](packages/flytekit.configuration.internal/secrets) |  |
| [`flytekit.configuration.internal.StatsD`](packages/flytekit.configuration.internal/statsd) |  |
| [`flytekit.configuration.plugin.FlytekitPlugin`](packages/flytekit.configuration.plugin/flytekitplugin) |  |
| [`flytekit.configuration.plugin.FlytekitPluginProtocol`](packages/flytekit.configuration.plugin/flytekitpluginprotocol) |  |
| [`flytekit.constants.CopyFileDetection`](packages/flytekit.constants/copyfiledetection) |  |
| [`flytekit.core.annotation.FlyteAnnotation`](packages/flytekit.core.annotation/flyteannotation) | A core object to add arbitrary annotations to flyte types. |
| [`flytekit.core.array_node.ArrayNode`](packages/flytekit.core.array_node/arraynode) |  |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTask`](packages/flytekit.core.array_node_map_task/arraynodemaptask) |  |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTaskResolver`](packages/flytekit.core.array_node_map_task/arraynodemaptaskresolver) | Special resolver that is used for ArrayNodeMapTasks. |
| [`flytekit.core.artifact.Artifact`](packages/flytekit.core.artifact/artifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.core.artifact.ArtifactIDSpecification`](packages/flytekit.core.artifact/artifactidspecification) | This is a special object that helps specify how Artifacts are to be created. |
| [`flytekit.core.artifact.ArtifactQuery`](packages/flytekit.core.artifact/artifactquery) |  |
| [`flytekit.core.artifact.ArtifactSerializationHandler`](packages/flytekit.core.artifact/artifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`flytekit.core.artifact.DefaultArtifactSerializationHandler`](packages/flytekit.core.artifact/defaultartifactserializationhandler) |  |
| [`flytekit.core.artifact.InputsBase`](packages/flytekit.core.artifact/inputsbase) | A class to provide better partition semantics. |
| [`flytekit.core.artifact.Partition`](packages/flytekit.core.artifact/partition) |  |
| [`flytekit.core.artifact.Partitions`](packages/flytekit.core.artifact/partitions) |  |
| [`flytekit.core.artifact.Serializer`](packages/flytekit.core.artifact/serializer) |  |
| [`flytekit.core.artifact.TimePartition`](packages/flytekit.core.artifact/timepartition) |  |
| [`flytekit.core.base_sql_task.SQLTask`](packages/flytekit.core.base_sql_task/sqltask) | Base task types for all SQL tasks. |
| [`flytekit.core.base_task.IgnoreOutputs`](packages/flytekit.core.base_task/ignoreoutputs) | This exception should be used to indicate that the outputs generated by this can be safely ignored. |
| [`flytekit.core.base_task.PythonTask`](packages/flytekit.core.base_task/pythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.base_task.Task`](packages/flytekit.core.base_task/task) | The base of all Tasks in flytekit. |
| [`flytekit.core.base_task.TaskMetadata`](packages/flytekit.core.base_task/taskmetadata) | Metadata for a Task. |
| [`flytekit.core.base_task.TaskResolverMixin`](packages/flytekit.core.base_task/taskresolvermixin) | Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.cache.Cache`](packages/flytekit.core.cache/cache) | Cache configuration for a task. |
| [`flytekit.core.cache.CachePolicy`](packages/flytekit.core.cache/cachepolicy) |  |
| [`flytekit.core.cache.VersionParameters`](packages/flytekit.core.cache/versionparameters) | Parameters used for version hash generation. |
| [`flytekit.core.checkpointer.Checkpoint`](packages/flytekit.core.checkpointer/checkpoint) | Base class for Checkpoint system. |
| [`flytekit.core.checkpointer.SyncCheckpoint`](packages/flytekit.core.checkpointer/synccheckpoint) | This class is NOT THREAD-SAFE!. |
| [`flytekit.core.class_based_resolver.ClassStorageTaskResolver`](packages/flytekit.core.class_based_resolver/classstoragetaskresolver) | Stores tasks inside a class variable. |
| [`flytekit.core.condition.BranchNode`](packages/flytekit.core.condition/branchnode) |  |
| [`flytekit.core.condition.Case`](packages/flytekit.core.condition/case) |  |
| [`flytekit.core.condition.Condition`](packages/flytekit.core.condition/condition) |  |
| [`flytekit.core.condition.ConditionalSection`](packages/flytekit.core.condition/conditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.condition.LocalExecutedConditionalSection`](packages/flytekit.core.condition/localexecutedconditionalsection) |  |
| [`flytekit.core.condition.SkippedConditionalSection`](packages/flytekit.core.condition/skippedconditionalsection) | This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |
| [`flytekit.core.container_task.ContainerTask`](packages/flytekit.core.container_task/containertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flytekit.core.context_manager.BranchEvalMode`](packages/flytekit.core.context_manager/branchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.core.context_manager.CompilationState`](packages/flytekit.core.context_manager/compilationstate) | Compilation state is used during the compilation of a workflow or task. |
| [`flytekit.core.context_manager.ExecutionParameters`](packages/flytekit.core.context_manager/executionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.context_manager.ExecutionState`](packages/flytekit.core.context_manager/executionstate) | This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.context_manager.FlyteContext`](packages/flytekit.core.context_manager/flytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.context_manager.FlyteContextManager`](packages/flytekit.core.context_manager/flytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.context_manager.FlyteEntities`](packages/flytekit.core.context_manager/flyteentities) | This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.context_manager.OutputMetadata`](packages/flytekit.core.context_manager/outputmetadata) |  |
| [`flytekit.core.context_manager.OutputMetadataTracker`](packages/flytekit.core.context_manager/outputmetadatatracker) | This class is for the users to set arbitrary metadata on output literals. |
| [`flytekit.core.context_manager.SecretsManager`](packages/flytekit.core.context_manager/secretsmanager) | This provides a secrets resolution logic at runtime. |
| [`flytekit.core.context_manager.SerializableToString`](packages/flytekit.core.context_manager/serializabletostring) | This protocol is used by the Artifact create_from function. |
| [`flytekit.core.data_persistence.FileAccessProvider`](packages/flytekit.core.data_persistence/fileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.core.docstring.Docstring`](packages/flytekit.core.docstring/docstring) |  |
| [`flytekit.core.environment.Environment`](packages/flytekit.core.environment/environment) |  |
| [`flytekit.core.gate.Gate`](packages/flytekit.core.gate/gate) | A node type that waits for user input before proceeding with a workflow. |
| [`flytekit.core.hash.HashMethod`](packages/flytekit.core.hash/hashmethod) | Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.core.hash.HashOnReferenceMixin`](packages/flytekit.core.hash/hashonreferencemixin) |  |
| [`flytekit.core.interface.Interface`](packages/flytekit.core.interface/interface) | A Python native interface object, like inspect. |
| [`flytekit.core.launch_plan.LaunchPlan`](packages/flytekit.core.launch_plan/launchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.launch_plan.ReferenceLaunchPlan`](packages/flytekit.core.launch_plan/referencelaunchplan) | A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.core.legacy_map_task.MapPythonTask`](packages/flytekit.core.legacy_map_task/mappythontask) | A MapPythonTask defines a {{< py_class_ref flytekit.PythonTask >}} which specifies how to run. |
| [`flytekit.core.legacy_map_task.MapTaskResolver`](packages/flytekit.core.legacy_map_task/maptaskresolver) | Special resolver that is used for MapTasks. |
| [`flytekit.core.local_cache.LocalTaskCache`](packages/flytekit.core.local_cache/localtaskcache) | This class implements a persistent store able to cache the result of local task executions. |
| [`flytekit.core.local_fsspec.FlyteLocalFileSystem`](packages/flytekit.core.local_fsspec/flytelocalfilesystem) | This class doesn't do anything except override the separator so that it works on windows. |
| [`flytekit.core.mock_stats.MockStats`](packages/flytekit.core.mock_stats/mockstats) |  |
| [`flytekit.core.node.Node`](packages/flytekit.core.node/node) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.notification.Email`](packages/flytekit.core.notification/email) | This notification should be used when sending regular emails to people. |
| [`flytekit.core.notification.Notification`](packages/flytekit.core.notification/notification) |  |
| [`flytekit.core.notification.PagerDuty`](packages/flytekit.core.notification/pagerduty) | This notification should be used when sending emails to the PagerDuty service. |
| [`flytekit.core.notification.Slack`](packages/flytekit.core.notification/slack) | This notification should be used when sending emails to the Slack. |
| [`flytekit.core.options.Options`](packages/flytekit.core.options/options) | These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.core.pod_template.PodTemplate`](packages/flytekit.core.pod_template/podtemplate) | Custom PodTemplate specification for a Task. |
| [`flytekit.core.promise.ComparisonExpression`](packages/flytekit.core.promise/comparisonexpression) | ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`flytekit.core.promise.ComparisonOps`](packages/flytekit.core.promise/comparisonops) |  |
| [`flytekit.core.promise.ConjunctionExpression`](packages/flytekit.core.promise/conjunctionexpression) | A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`flytekit.core.promise.ConjunctionOps`](packages/flytekit.core.promise/conjunctionops) |  |
| [`flytekit.core.promise.HasFlyteInterface`](packages/flytekit.core.promise/hasflyteinterface) |  |
| [`flytekit.core.promise.LocallyExecutable`](packages/flytekit.core.promise/locallyexecutable) |  |
| [`flytekit.core.promise.NodeOutput`](packages/flytekit.core.promise/nodeoutput) |  |
| [`flytekit.core.promise.Promise`](packages/flytekit.core.promise/promise) | This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.promise.SupportsNodeCreation`](packages/flytekit.core.promise/supportsnodecreation) |  |
| [`flytekit.core.promise.VoidPromise`](packages/flytekit.core.promise/voidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.python_auto_container.DefaultNotebookTaskResolver`](packages/flytekit.core.python_auto_container/defaultnotebooktaskresolver) | This resolved is used when the task is defined in a notebook. |
| [`flytekit.core.python_auto_container.DefaultTaskResolver`](packages/flytekit.core.python_auto_container/defaulttaskresolver) | Please see the notes in the TaskResolverMixin as it describes this default behavior. |
| [`flytekit.core.python_auto_container.PickledEntity`](packages/flytekit.core.python_auto_container/pickledentity) | Represents the structure of the pickled object stored in the. |
| [`flytekit.core.python_auto_container.PickledEntityMetadata`](packages/flytekit.core.python_auto_container/pickledentitymetadata) | Metadata for a pickled entity containing version information. |
| [`flytekit.core.python_auto_container.PythonAutoContainerTask`](packages/flytekit.core.python_auto_container/pythonautocontainertask) | A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_customized_container_task.PythonCustomizedContainerTask`](packages/flytekit.core.python_customized_container_task/pythoncustomizedcontainertask) | Please take a look at the comments for {{< py_class_ref flytekit.extend.ExecutableTemplateShimTask >}} as well. |
| [`flytekit.core.python_customized_container_task.TaskTemplateResolver`](packages/flytekit.core.python_customized_container_task/tasktemplateresolver) | This is a special resolver that resolves the task above at execution time, using only the ``TaskTemplate``,. |
| [`flytekit.core.python_function_task.AsyncPythonFunctionTask`](packages/flytekit.core.python_function_task/asyncpythonfunctiontask) | This is the base task for eager tasks, as well as normal async tasks. |
| [`flytekit.core.python_function_task.EagerAsyncPythonFunctionTask`](packages/flytekit.core.python_function_task/eagerasyncpythonfunctiontask) | This is the base eager task (aka eager workflow) type. |
| [`flytekit.core.python_function_task.EagerFailureHandlerTask`](packages/flytekit.core.python_function_task/eagerfailurehandlertask) |  |
| [`flytekit.core.python_function_task.EagerFailureTaskResolver`](packages/flytekit.core.python_function_task/eagerfailuretaskresolver) |  |
| [`flytekit.core.python_function_task.PythonFunctionTask`](packages/flytekit.core.python_function_task/pythonfunctiontask) | A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.python_function_task.PythonInstanceTask`](packages/flytekit.core.python_function_task/pythoninstancetask) | This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.core.reference_entity.LaunchPlanReference`](packages/flytekit.core.reference_entity/launchplanreference) | A reference object containing metadata that points to a remote launch plan. |
| [`flytekit.core.reference_entity.Reference`](packages/flytekit.core.reference_entity/reference) |  |
| [`flytekit.core.reference_entity.ReferenceEntity`](packages/flytekit.core.reference_entity/referenceentity) |  |
| [`flytekit.core.reference_entity.ReferenceSpec`](packages/flytekit.core.reference_entity/referencespec) |  |
| [`flytekit.core.reference_entity.ReferenceTemplate`](packages/flytekit.core.reference_entity/referencetemplate) |  |
| [`flytekit.core.reference_entity.TaskReference`](packages/flytekit.core.reference_entity/taskreference) | A reference object containing metadata that points to a remote task. |
| [`flytekit.core.reference_entity.WorkflowReference`](packages/flytekit.core.reference_entity/workflowreference) | A reference object containing metadata that points to a remote workflow. |
| [`flytekit.core.resources.ResourceSpec`](packages/flytekit.core.resources/resourcespec) |  |
| [`flytekit.core.resources.Resources`](packages/flytekit.core.resources/resources) | This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.schedule.CronSchedule`](packages/flytekit.core.schedule/cronschedule) | Use this when you have a launch plan that you want to run on a cron expression. |
| [`flytekit.core.schedule.FixedRate`](packages/flytekit.core.schedule/fixedrate) | Use this class to schedule a fixed-rate interval for a launch plan. |
| [`flytekit.core.schedule.LaunchPlanTriggerBase`](packages/flytekit.core.schedule/launchplantriggerbase) |  |
| [`flytekit.core.schedule.OnSchedule`](packages/flytekit.core.schedule/onschedule) |  |
| [`flytekit.core.shim_task.ExecutableTemplateShimTask`](packages/flytekit.core.shim_task/executabletemplateshimtask) | The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`flytekit.core.shim_task.ShimTaskExecutor`](packages/flytekit.core.shim_task/shimtaskexecutor) |  |
| [`flytekit.core.task.Echo`](packages/flytekit.core.task/echo) |  |
| [`flytekit.core.task.ReferenceTask`](packages/flytekit.core.task/referencetask) | This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.task.TaskPlugins`](packages/flytekit.core.task/taskplugins) | This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |
| [`flytekit.core.tracked_abc.FlyteTrackedABC`](packages/flytekit.core.tracked_abc/flytetrackedabc) | This class exists because if you try to inherit from abc. |
| [`flytekit.core.tracker.InstanceTrackingMeta`](packages/flytekit.core.tracker/instancetrackingmeta) | Please see the original class :flytekit. |
| [`flytekit.core.tracker.TrackedInstance`](packages/flytekit.core.tracker/trackedinstance) | Please see the notes for the metaclass above first. |
| [`flytekit.core.type_engine.AsyncTypeTransformer`](packages/flytekit.core.type_engine/asynctypetransformer) |  |
| [`flytekit.core.type_engine.BatchSize`](packages/flytekit.core.type_engine/batchsize) | This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`flytekit.core.type_engine.BinaryIOTransformer`](packages/flytekit.core.type_engine/binaryiotransformer) | Handler for BinaryIO. |
| [`flytekit.core.type_engine.DataclassTransformer`](packages/flytekit.core.type_engine/dataclasstransformer) | The Dataclass Transformer provides a type transformer for dataclasses. |
| [`flytekit.core.type_engine.DictTransformer`](packages/flytekit.core.type_engine/dicttransformer) | Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`flytekit.core.type_engine.EnumTransformer`](packages/flytekit.core.type_engine/enumtransformer) | Enables converting a python type enum. |
| [`flytekit.core.type_engine.ListTransformer`](packages/flytekit.core.type_engine/listtransformer) | Transformer that handles a univariate typing. |
| [`flytekit.core.type_engine.LiteralTypeTransformer`](packages/flytekit.core.type_engine/literaltypetransformer) |  |
| [`flytekit.core.type_engine.LiteralsResolver`](packages/flytekit.core.type_engine/literalsresolver) | LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.core.type_engine.ProtobufTransformer`](packages/flytekit.core.type_engine/protobuftransformer) |  |
| [`flytekit.core.type_engine.RestrictedTypeError`](packages/flytekit.core.type_engine/restrictedtypeerror) |  |
| [`flytekit.core.type_engine.RestrictedTypeTransformer`](packages/flytekit.core.type_engine/restrictedtypetransformer) | Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. |
| [`flytekit.core.type_engine.SimpleTransformer`](packages/flytekit.core.type_engine/simpletransformer) | A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate. |
| [`flytekit.core.type_engine.TextIOTransformer`](packages/flytekit.core.type_engine/textiotransformer) | Handler for TextIO. |
| [`flytekit.core.type_engine.TypeEngine`](packages/flytekit.core.type_engine/typeengine) | Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.type_engine.TypeTransformer`](packages/flytekit.core.type_engine/typetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.TypeTransformerFailedError`](packages/flytekit.core.type_engine/typetransformerfailederror) |  |
| [`flytekit.core.type_engine.UnionTransformer`](packages/flytekit.core.type_engine/uniontransformer) | Transformer that handles a typing. |
| [`flytekit.core.utils.AutoDeletingTempDir`](packages/flytekit.core.utils/autodeletingtempdir) | Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`flytekit.core.utils.ClassDecorator`](packages/flytekit.core.utils/classdecorator) | Abstract class for class decorators. |
| [`flytekit.core.utils.Directory`](packages/flytekit.core.utils/directory) |  |
| [`flytekit.core.utils.timeit`](packages/flytekit.core.utils/timeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.worker_queue.Controller`](packages/flytekit.core.worker_queue/controller) | This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint. |
| [`flytekit.core.worker_queue.ItemStatus`](packages/flytekit.core.worker_queue/itemstatus) |  |
| [`flytekit.core.worker_queue.Update`](packages/flytekit.core.worker_queue/update) |  |
| [`flytekit.core.worker_queue.WorkItem`](packages/flytekit.core.worker_queue/workitem) | This is a class to keep track of what the user requested. |
| [`flytekit.core.workflow.ImperativeWorkflow`](packages/flytekit.core.workflow/imperativeworkflow) | An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`flytekit.core.workflow.PythonFunctionWorkflow`](packages/flytekit.core.workflow/pythonfunctionworkflow) | Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`flytekit.core.workflow.ReferenceWorkflow`](packages/flytekit.core.workflow/referenceworkflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.core.workflow.WorkflowBase`](packages/flytekit.core.workflow/workflowbase) |  |
| [`flytekit.core.workflow.WorkflowFailurePolicy`](packages/flytekit.core.workflow/workflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.core.workflow.WorkflowMetadata`](packages/flytekit.core.workflow/workflowmetadata) |  |
| [`flytekit.core.workflow.WorkflowMetadataDefaults`](packages/flytekit.core.workflow/workflowmetadatadefaults) | This class is similarly named to the one above. |
| [`flytekit.deck.deck.Deck`](packages/flytekit.deck.deck/deck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.deck.deck.DeckField`](packages/flytekit.deck.deck/deckfield) | DeckField is used to specify the fields that will be rendered in the deck. |
| [`flytekit.deck.deck.TimeLineDeck`](packages/flytekit.deck.deck/timelinedeck) | The TimeLineDeck class is designed to render the execution time of each part of a task. |
| [`flytekit.deck.renderer.ArrowRenderer`](packages/flytekit.deck.renderer/arrowrenderer) | Render an Arrow dataframe as an HTML table. |
| [`flytekit.deck.renderer.MarkdownRenderer`](packages/flytekit.deck.renderer/markdownrenderer) | Convert a markdown string to HTML and return HTML as a unicode string. |
| [`flytekit.deck.renderer.PythonDependencyRenderer`](packages/flytekit.deck.renderer/pythondependencyrenderer) | PythonDependencyDeck is a deck that contains information about packages installed via pip. |
| [`flytekit.deck.renderer.Renderable`](packages/flytekit.deck.renderer/renderable) |  |
| [`flytekit.deck.renderer.SourceCodeRenderer`](packages/flytekit.deck.renderer/sourcecoderenderer) | Convert Python source code to HTML, and return HTML as a unicode string. |
| [`flytekit.deck.renderer.TopFrameRenderer`](packages/flytekit.deck.renderer/topframerenderer) | Render a DataFrame as an HTML table. |
| [`flytekit.exceptions.base.FlyteException`](packages/flytekit.exceptions.base/flyteexception) |  |
| [`flytekit.exceptions.base.FlyteRecoverableException`](packages/flytekit.exceptions.base/flyterecoverableexception) |  |
| [`flytekit.exceptions.eager.EagerException`](packages/flytekit.exceptions.eager/eagerexception) | Raised when a node in an eager workflow encounters an error. |
| [`flytekit.exceptions.scopes.FlyteScopedException`](packages/flytekit.exceptions.scopes/flytescopedexception) |  |
| [`flytekit.exceptions.scopes.FlyteScopedSystemException`](packages/flytekit.exceptions.scopes/flytescopedsystemexception) |  |
| [`flytekit.exceptions.scopes.FlyteScopedUserException`](packages/flytekit.exceptions.scopes/flytescopeduserexception) |  |
| [`flytekit.exceptions.system.FlyteAgentNotFound`](packages/flytekit.exceptions.system/flyteagentnotfound) |  |
| [`flytekit.exceptions.system.FlyteConnectorNotFound`](packages/flytekit.exceptions.system/flyteconnectornotfound) |  |
| [`flytekit.exceptions.system.FlyteDownloadDataException`](packages/flytekit.exceptions.system/flytedownloaddataexception) |  |
| [`flytekit.exceptions.system.FlyteEntrypointNotLoadable`](packages/flytekit.exceptions.system/flyteentrypointnotloadable) |  |
| [`flytekit.exceptions.system.FlyteNonRecoverableSystemException`](packages/flytekit.exceptions.system/flytenonrecoverablesystemexception) |  |
| [`flytekit.exceptions.system.FlyteNotImplementedException`](packages/flytekit.exceptions.system/flytenotimplementedexception) |  |
| [`flytekit.exceptions.system.FlyteSystemAssertion`](packages/flytekit.exceptions.system/flytesystemassertion) |  |
| [`flytekit.exceptions.system.FlyteSystemException`](packages/flytekit.exceptions.system/flytesystemexception) |  |
| [`flytekit.exceptions.system.FlyteSystemUnavailableException`](packages/flytekit.exceptions.system/flytesystemunavailableexception) |  |
| [`flytekit.exceptions.system.FlyteUploadDataException`](packages/flytekit.exceptions.system/flyteuploaddataexception) |  |
| [`flytekit.exceptions.user.FlyteAssertion`](packages/flytekit.exceptions.user/flyteassertion) |  |
| [`flytekit.exceptions.user.FlyteAuthenticationException`](packages/flytekit.exceptions.user/flyteauthenticationexception) |  |
| [`flytekit.exceptions.user.FlyteCompilationException`](packages/flytekit.exceptions.user/flytecompilationexception) |  |
| [`flytekit.exceptions.user.FlyteDataNotFoundException`](packages/flytekit.exceptions.user/flytedatanotfoundexception) |  |
| [`flytekit.exceptions.user.FlyteDisapprovalException`](packages/flytekit.exceptions.user/flytedisapprovalexception) |  |
| [`flytekit.exceptions.user.FlyteEntityAlreadyExistsException`](packages/flytekit.exceptions.user/flyteentityalreadyexistsexception) |  |
| [`flytekit.exceptions.user.FlyteEntityNotExistException`](packages/flytekit.exceptions.user/flyteentitynotexistexception) |  |
| [`flytekit.exceptions.user.FlyteEntityNotFoundException`](packages/flytekit.exceptions.user/flyteentitynotfoundexception) |  |
| [`flytekit.exceptions.user.FlyteFailureNodeInputMismatchException`](packages/flytekit.exceptions.user/flytefailurenodeinputmismatchexception) |  |
| [`flytekit.exceptions.user.FlyteInvalidInputException`](packages/flytekit.exceptions.user/flyteinvalidinputexception) |  |
| [`flytekit.exceptions.user.FlyteMissingReturnValueException`](packages/flytekit.exceptions.user/flytemissingreturnvalueexception) |  |
| [`flytekit.exceptions.user.FlyteMissingTypeException`](packages/flytekit.exceptions.user/flytemissingtypeexception) |  |
| [`flytekit.exceptions.user.FlytePromiseAttributeResolveException`](packages/flytekit.exceptions.user/flytepromiseattributeresolveexception) |  |
| [`flytekit.exceptions.user.FlyteRecoverableException`](packages/flytekit.exceptions.user/flyterecoverableexception) |  |
| [`flytekit.exceptions.user.FlyteTimeout`](packages/flytekit.exceptions.user/flytetimeout) |  |
| [`flytekit.exceptions.user.FlyteTypeException`](packages/flytekit.exceptions.user/flytetypeexception) |  |
| [`flytekit.exceptions.user.FlyteUserException`](packages/flytekit.exceptions.user/flyteuserexception) |  |
| [`flytekit.exceptions.user.FlyteUserRuntimeException`](packages/flytekit.exceptions.user/flyteuserruntimeexception) |  |
| [`flytekit.exceptions.user.FlyteValidationException`](packages/flytekit.exceptions.user/flytevalidationexception) |  |
| [`flytekit.exceptions.user.FlyteValueException`](packages/flytekit.exceptions.user/flytevalueexception) |  |
| [`flytekit.extend.backend.base_connector.AsyncConnectorBase`](packages/flytekit.extend.backend.base_connector/asyncconnectorbase) | This is the base class for all async connectors. |
| [`flytekit.extend.backend.base_connector.AsyncConnectorExecutorMixin`](packages/flytekit.extend.backend.base_connector/asyncconnectorexecutormixin) | This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.ConnectorBase`](packages/flytekit.extend.backend.base_connector/connectorbase) |  |
| [`flytekit.extend.backend.base_connector.ConnectorRegistry`](packages/flytekit.extend.backend.base_connector/connectorregistry) | This is the registry for all connectors. |
| [`flytekit.extend.backend.base_connector.Resource`](packages/flytekit.extend.backend.base_connector/resource) | This is the output resource of the job. |
| [`flytekit.extend.backend.base_connector.ResourceMeta`](packages/flytekit.extend.backend.base_connector/resourcemeta) | This is the metadata for the job. |
| [`flytekit.extend.backend.base_connector.SyncConnectorBase`](packages/flytekit.extend.backend.base_connector/syncconnectorbase) | This is the base class for all sync connectors. |
| [`flytekit.extend.backend.base_connector.SyncConnectorExecutorMixin`](packages/flytekit.extend.backend.base_connector/syncconnectorexecutormixin) | This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.TaskCategory`](packages/flytekit.extend.backend.base_connector/taskcategory) |  |
| [`flytekit.extend.backend.connector_service.AsyncConnectorService`](packages/flytekit.extend.backend.connector_service/asyncconnectorservice) |  |
| [`flytekit.extend.backend.connector_service.ConnectorMetadataService`](packages/flytekit.extend.backend.connector_service/connectormetadataservice) |  |
| [`flytekit.extend.backend.connector_service.SyncConnectorService`](packages/flytekit.extend.backend.connector_service/syncconnectorservice) |  |
| [`flytekit.extras.accelerators.BaseAccelerator`](packages/flytekit.extras.accelerators/baseaccelerator) | Base class for all accelerator types. |
| [`flytekit.extras.accelerators.GPUAccelerator`](packages/flytekit.extras.accelerators/gpuaccelerator) | Class that represents a GPU accelerator. |
| [`flytekit.extras.accelerators.MultiInstanceGPUAccelerator`](packages/flytekit.extras.accelerators/multiinstancegpuaccelerator) | Base class for all multi-instance GPU accelerator types. |
| [`flytekit.extras.cloud_pickle_resolver.ExperimentalNaiveCloudPickleResolver`](packages/flytekit.extras.cloud_pickle_resolver/experimentalnaivecloudpickleresolver) | Please do not use this resolver, basically ever. |
| [`flytekit.extras.pydantic_transformer.transformer.PydanticTransformer`](packages/flytekit.extras.pydantic_transformer.transformer/pydantictransformer) |  |
| [`flytekit.extras.sklearn.native.SklearnEstimatorTransformer`](packages/flytekit.extras.sklearn.native/sklearnestimatortransformer) |  |
| [`flytekit.extras.sklearn.native.SklearnTypeTransformer`](packages/flytekit.extras.sklearn.native/sklearntypetransformer) |  |
| [`flytekit.extras.sqlite3.task.SQLite3Config`](packages/flytekit.extras.sqlite3.task/sqlite3config) | Use this configuration to configure if sqlite3 files that should be loaded by the task. |
| [`flytekit.extras.sqlite3.task.SQLite3Task`](packages/flytekit.extras.sqlite3.task/sqlite3task) | Run client side SQLite3 queries that optionally return a FlyteSchema object. |
| [`flytekit.extras.sqlite3.task.SQLite3TaskExecutor`](packages/flytekit.extras.sqlite3.task/sqlite3taskexecutor) |  |
| [`flytekit.extras.tasks.shell.AttrDict`](packages/flytekit.extras.tasks.shell/attrdict) | Convert a dictionary to an attribute style lookup. |
| [`flytekit.extras.tasks.shell.OutputLocation`](packages/flytekit.extras.tasks.shell/outputlocation) |  |
| [`flytekit.extras.tasks.shell.ProcessResult`](packages/flytekit.extras.tasks.shell/processresult) | Stores a process return code, standard output and standard error. |
| [`flytekit.extras.tasks.shell.RawShellTask`](packages/flytekit.extras.tasks.shell/rawshelltask) |  |
| [`flytekit.extras.tasks.shell.ShellTask`](packages/flytekit.extras.tasks.shell/shelltask) |  |
| [`flytekit.extras.webhook.WebhookConnector`](packages/flytekit.extras.webhook/webhookconnector) | WebhookConnector is responsible for handling webhook tasks. |
| [`flytekit.extras.webhook.WebhookTask`](packages/flytekit.extras.webhook/webhooktask) | The WebhookTask is used to invoke a webhook. |
| [`flytekit.extras.webhook.connector.WebhookConnector`](packages/flytekit.extras.webhook.connector/webhookconnector) | WebhookConnector is responsible for handling webhook tasks. |
| [`flytekit.extras.webhook.task.WebhookTask`](packages/flytekit.extras.webhook.task/webhooktask) | The WebhookTask is used to invoke a webhook. |
| [`flytekit.image_spec.default_builder.DefaultImageBuilder`](packages/flytekit.image_spec.default_builder/defaultimagebuilder) | Image builder using Docker and buildkit. |
| [`flytekit.image_spec.image_spec.ImageBuildEngine`](packages/flytekit.image_spec.image_spec/imagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.image_spec.image_spec.ImageSpec`](packages/flytekit.image_spec.image_spec/imagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.image_spec.image_spec.ImageSpecBuilder`](packages/flytekit.image_spec.image_spec/imagespecbuilder) |  |
| [`flytekit.image_spec.noop_builder.NoOpBuilder`](packages/flytekit.image_spec.noop_builder/noopbuilder) | Noop image builder. |
| [`flytekit.interaction.click_types.DateTimeType`](packages/flytekit.interaction.click_types/datetimetype) |  |
| [`flytekit.interaction.click_types.DirParamType`](packages/flytekit.interaction.click_types/dirparamtype) |  |
| [`flytekit.interaction.click_types.DurationParamType`](packages/flytekit.interaction.click_types/durationparamtype) |  |
| [`flytekit.interaction.click_types.EnumParamType`](packages/flytekit.interaction.click_types/enumparamtype) |  |
| [`flytekit.interaction.click_types.FileParamType`](packages/flytekit.interaction.click_types/fileparamtype) |  |
| [`flytekit.interaction.click_types.FlyteLiteralConverter`](packages/flytekit.interaction.click_types/flyteliteralconverter) |  |
| [`flytekit.interaction.click_types.JSONIteratorParamType`](packages/flytekit.interaction.click_types/jsoniteratorparamtype) |  |
| [`flytekit.interaction.click_types.JsonParamType`](packages/flytekit.interaction.click_types/jsonparamtype) |  |
| [`flytekit.interaction.click_types.PickleParamType`](packages/flytekit.interaction.click_types/pickleparamtype) |  |
| [`flytekit.interaction.click_types.StructuredDatasetParamType`](packages/flytekit.interaction.click_types/structureddatasetparamtype) | TODO handle column types. |
| [`flytekit.interaction.click_types.UnionParamType`](packages/flytekit.interaction.click_types/unionparamtype) | A composite type that allows for multiple types to be specified. |
| [`flytekit.interaction.rich_utils.RichCallback`](packages/flytekit.interaction.rich_utils/richcallback) |  |
| [`flytekit.interactive.vscode_lib.config.VscodeConfig`](packages/flytekit.interactive.vscode_lib.config/vscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`flytekit.interactive.vscode_lib.decorator.vscode`](packages/flytekit.interactive.vscode_lib.decorator/vscode) |  |
| [`flytekit.interfaces.cli_identifiers.Identifier`](packages/flytekit.interfaces.cli_identifiers/identifier) |  |
| [`flytekit.interfaces.cli_identifiers.TaskExecutionIdentifier`](packages/flytekit.interfaces.cli_identifiers/taskexecutionidentifier) |  |
| [`flytekit.interfaces.cli_identifiers.WorkflowExecutionIdentifier`](packages/flytekit.interfaces.cli_identifiers/workflowexecutionidentifier) |  |
| [`flytekit.interfaces.stats.client.DummyStatsClient`](packages/flytekit.interfaces.stats.client/dummystatsclient) | A dummy client for statsd. |
| [`flytekit.interfaces.stats.client.ScopeableStatsProxy`](packages/flytekit.interfaces.stats.client/scopeablestatsproxy) | A Proxy object for an underlying statsd client. |
| [`flytekit.interfaces.stats.client.StatsClientProxy`](packages/flytekit.interfaces.stats.client/statsclientproxy) |  |
| [`flytekit.interfaces.stats.taggable.TaggableStats`](packages/flytekit.interfaces.stats.taggable/taggablestats) |  |
| [`flytekit.models.admin.common.Sort`](packages/flytekit.models.admin.common/sort) |  |
| [`flytekit.models.admin.task_execution.TaskExecution`](packages/flytekit.models.admin.task_execution/taskexecution) |  |
| [`flytekit.models.admin.task_execution.TaskExecutionClosure`](packages/flytekit.models.admin.task_execution/taskexecutionclosure) |  |
| [`flytekit.models.admin.workflow.Workflow`](packages/flytekit.models.admin.workflow/workflow) |  |
| [`flytekit.models.admin.workflow.WorkflowClosure`](packages/flytekit.models.admin.workflow/workflowclosure) |  |
| [`flytekit.models.admin.workflow.WorkflowSpec`](packages/flytekit.models.admin.workflow/workflowspec) |  |
| [`flytekit.models.annotation.TypeAnnotation`](packages/flytekit.models.annotation/typeannotation) | Python class representation of the flyteidl TypeAnnotation message. |
| [`flytekit.models.array_job.ArrayJob`](packages/flytekit.models.array_job/arrayjob) |  |
| [`flytekit.models.common.Annotations`](packages/flytekit.models.common/annotations) |  |
| [`flytekit.models.common.AuthRole`](packages/flytekit.models.common/authrole) |  |
| [`flytekit.models.common.EmailNotification`](packages/flytekit.models.common/emailnotification) |  |
| [`flytekit.models.common.Envs`](packages/flytekit.models.common/envs) |  |
| [`flytekit.models.common.FlyteABCMeta`](packages/flytekit.models.common/flyteabcmeta) |  |
| [`flytekit.models.common.FlyteCustomIdlEntity`](packages/flytekit.models.common/flytecustomidlentity) |  |
| [`flytekit.models.common.FlyteIdlEntity`](packages/flytekit.models.common/flyteidlentity) |  |
| [`flytekit.models.common.FlyteType`](packages/flytekit.models.common/flytetype) |  |
| [`flytekit.models.common.Labels`](packages/flytekit.models.common/labels) |  |
| [`flytekit.models.common.NamedEntityIdentifier`](packages/flytekit.models.common/namedentityidentifier) |  |
| [`flytekit.models.common.Notification`](packages/flytekit.models.common/notification) |  |
| [`flytekit.models.common.PagerDutyNotification`](packages/flytekit.models.common/pagerdutynotification) |  |
| [`flytekit.models.common.RawOutputDataConfig`](packages/flytekit.models.common/rawoutputdataconfig) |  |
| [`flytekit.models.common.SlackNotification`](packages/flytekit.models.common/slacknotification) |  |
| [`flytekit.models.common.UrlBlob`](packages/flytekit.models.common/urlblob) |  |
| [`flytekit.models.concurrency.ConcurrencyLimitBehavior`](packages/flytekit.models.concurrency/concurrencylimitbehavior) |  |
| [`flytekit.models.concurrency.ConcurrencyPolicy`](packages/flytekit.models.concurrency/concurrencypolicy) | Defines the concurrency policy for a launch plan. |
| [`flytekit.models.core.catalog.CatalogArtifactTag`](packages/flytekit.models.core.catalog/catalogartifacttag) |  |
| [`flytekit.models.core.catalog.CatalogMetadata`](packages/flytekit.models.core.catalog/catalogmetadata) |  |
| [`flytekit.models.core.compiler.CompiledTask`](packages/flytekit.models.core.compiler/compiledtask) |  |
| [`flytekit.models.core.compiler.CompiledWorkflow`](packages/flytekit.models.core.compiler/compiledworkflow) |  |
| [`flytekit.models.core.compiler.CompiledWorkflowClosure`](packages/flytekit.models.core.compiler/compiledworkflowclosure) |  |
| [`flytekit.models.core.compiler.ConnectionSet`](packages/flytekit.models.core.compiler/connectionset) |  |
| [`flytekit.models.core.condition.BooleanExpression`](packages/flytekit.models.core.condition/booleanexpression) |  |
| [`flytekit.models.core.condition.ComparisonExpression`](packages/flytekit.models.core.condition/comparisonexpression) |  |
| [`flytekit.models.core.condition.ConjunctionExpression`](packages/flytekit.models.core.condition/conjunctionexpression) |  |
| [`flytekit.models.core.condition.Operand`](packages/flytekit.models.core.condition/operand) |  |
| [`flytekit.models.core.errors.ContainerError`](packages/flytekit.models.core.errors/containererror) |  |
| [`flytekit.models.core.errors.ErrorDocument`](packages/flytekit.models.core.errors/errordocument) |  |
| [`flytekit.models.core.execution.ExecutionError`](packages/flytekit.models.core.execution/executionerror) |  |
| [`flytekit.models.core.execution.NodeExecutionPhase`](packages/flytekit.models.core.execution/nodeexecutionphase) |  |
| [`flytekit.models.core.execution.TaskExecutionPhase`](packages/flytekit.models.core.execution/taskexecutionphase) |  |
| [`flytekit.models.core.execution.TaskLog`](packages/flytekit.models.core.execution/tasklog) |  |
| [`flytekit.models.core.execution.WorkflowExecutionPhase`](packages/flytekit.models.core.execution/workflowexecutionphase) | This class holds enum values used for setting notifications. |
| [`flytekit.models.core.identifier.Identifier`](packages/flytekit.models.core.identifier/identifier) |  |
| [`flytekit.models.core.identifier.NodeExecutionIdentifier`](packages/flytekit.models.core.identifier/nodeexecutionidentifier) |  |
| [`flytekit.models.core.identifier.ResourceType`](packages/flytekit.models.core.identifier/resourcetype) |  |
| [`flytekit.models.core.identifier.SignalIdentifier`](packages/flytekit.models.core.identifier/signalidentifier) |  |
| [`flytekit.models.core.identifier.TaskExecutionIdentifier`](packages/flytekit.models.core.identifier/taskexecutionidentifier) |  |
| [`flytekit.models.core.identifier.WorkflowExecutionIdentifier`](packages/flytekit.models.core.identifier/workflowexecutionidentifier) |  |
| [`flytekit.models.core.types.BlobType`](packages/flytekit.models.core.types/blobtype) | This type represents offloaded data and is typically used for things like files. |
| [`flytekit.models.core.types.EnumType`](packages/flytekit.models.core.types/enumtype) | Models _types_pb2. |
| [`flytekit.models.core.workflow.Alias`](packages/flytekit.models.core.workflow/alias) |  |
| [`flytekit.models.core.workflow.ApproveCondition`](packages/flytekit.models.core.workflow/approvecondition) |  |
| [`flytekit.models.core.workflow.ArrayNode`](packages/flytekit.models.core.workflow/arraynode) |  |
| [`flytekit.models.core.workflow.BranchNode`](packages/flytekit.models.core.workflow/branchnode) |  |
| [`flytekit.models.core.workflow.GateNode`](packages/flytekit.models.core.workflow/gatenode) |  |
| [`flytekit.models.core.workflow.IfBlock`](packages/flytekit.models.core.workflow/ifblock) |  |
| [`flytekit.models.core.workflow.IfElseBlock`](packages/flytekit.models.core.workflow/ifelseblock) |  |
| [`flytekit.models.core.workflow.Node`](packages/flytekit.models.core.workflow/node) |  |
| [`flytekit.models.core.workflow.NodeMetadata`](packages/flytekit.models.core.workflow/nodemetadata) |  |
| [`flytekit.models.core.workflow.SignalCondition`](packages/flytekit.models.core.workflow/signalcondition) |  |
| [`flytekit.models.core.workflow.SleepCondition`](packages/flytekit.models.core.workflow/sleepcondition) |  |
| [`flytekit.models.core.workflow.TaskNode`](packages/flytekit.models.core.workflow/tasknode) |  |
| [`flytekit.models.core.workflow.TaskNodeOverrides`](packages/flytekit.models.core.workflow/tasknodeoverrides) |  |
| [`flytekit.models.core.workflow.WorkflowMetadata`](packages/flytekit.models.core.workflow/workflowmetadata) |  |
| [`flytekit.models.core.workflow.WorkflowMetadataDefaults`](packages/flytekit.models.core.workflow/workflowmetadatadefaults) |  |
| [`flytekit.models.core.workflow.WorkflowNode`](packages/flytekit.models.core.workflow/workflownode) |  |
| [`flytekit.models.core.workflow.WorkflowTemplate`](packages/flytekit.models.core.workflow/workflowtemplate) |  |
| [`flytekit.models.documentation.Description`](packages/flytekit.models.documentation/description) | Full user description with formatting preserved. |
| [`flytekit.models.documentation.Documentation`](packages/flytekit.models.documentation/documentation) | DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.models.documentation.SourceCode`](packages/flytekit.models.documentation/sourcecode) | Link to source code used to define this task or workflow. |
| [`flytekit.models.domain.Domain`](packages/flytekit.models.domain/domain) | Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |
| [`flytekit.models.dynamic_job.DynamicJobSpec`](packages/flytekit.models.dynamic_job/dynamicjobspec) |  |
| [`flytekit.models.event.TaskExecutionMetadata`](packages/flytekit.models.event/taskexecutionmetadata) |  |
| [`flytekit.models.execution.AbortMetadata`](packages/flytekit.models.execution/abortmetadata) |  |
| [`flytekit.models.execution.ClusterAssignment`](packages/flytekit.models.execution/clusterassignment) |  |
| [`flytekit.models.execution.Execution`](packages/flytekit.models.execution/execution) |  |
| [`flytekit.models.execution.ExecutionClosure`](packages/flytekit.models.execution/executionclosure) |  |
| [`flytekit.models.execution.ExecutionMetadata`](packages/flytekit.models.execution/executionmetadata) |  |
| [`flytekit.models.execution.ExecutionSpec`](packages/flytekit.models.execution/executionspec) |  |
| [`flytekit.models.execution.LiteralMapBlob`](packages/flytekit.models.execution/literalmapblob) |  |
| [`flytekit.models.execution.NodeExecutionGetDataResponse`](packages/flytekit.models.execution/nodeexecutiongetdataresponse) |  |
| [`flytekit.models.execution.NotificationList`](packages/flytekit.models.execution/notificationlist) |  |
| [`flytekit.models.execution.SystemMetadata`](packages/flytekit.models.execution/systemmetadata) |  |
| [`flytekit.models.execution.TaskExecutionGetDataResponse`](packages/flytekit.models.execution/taskexecutiongetdataresponse) |  |
| [`flytekit.models.execution.WorkflowExecutionGetDataResponse`](packages/flytekit.models.execution/workflowexecutiongetdataresponse) |  |
| [`flytekit.models.filters.Contains`](packages/flytekit.models.filters/contains) |  |
| [`flytekit.models.filters.Equal`](packages/flytekit.models.filters/equal) |  |
| [`flytekit.models.filters.Filter`](packages/flytekit.models.filters/filter) |  |
| [`flytekit.models.filters.FilterList`](packages/flytekit.models.filters/filterlist) |  |
| [`flytekit.models.filters.GreaterThan`](packages/flytekit.models.filters/greaterthan) |  |
| [`flytekit.models.filters.GreaterThanOrEqual`](packages/flytekit.models.filters/greaterthanorequal) |  |
| [`flytekit.models.filters.LessThan`](packages/flytekit.models.filters/lessthan) |  |
| [`flytekit.models.filters.LessThanOrEqual`](packages/flytekit.models.filters/lessthanorequal) |  |
| [`flytekit.models.filters.NotEqual`](packages/flytekit.models.filters/notequal) |  |
| [`flytekit.models.filters.SetFilter`](packages/flytekit.models.filters/setfilter) |  |
| [`flytekit.models.filters.ValueIn`](packages/flytekit.models.filters/valuein) |  |
| [`flytekit.models.filters.ValueNotIn`](packages/flytekit.models.filters/valuenotin) |  |
| [`flytekit.models.interface.Parameter`](packages/flytekit.models.interface/parameter) |  |
| [`flytekit.models.interface.ParameterMap`](packages/flytekit.models.interface/parametermap) |  |
| [`flytekit.models.interface.TypedInterface`](packages/flytekit.models.interface/typedinterface) |  |
| [`flytekit.models.interface.Variable`](packages/flytekit.models.interface/variable) |  |
| [`flytekit.models.interface.VariableMap`](packages/flytekit.models.interface/variablemap) |  |
| [`flytekit.models.launch_plan.Auth`](packages/flytekit.models.launch_plan/auth) |  |
| [`flytekit.models.launch_plan.LaunchPlan`](packages/flytekit.models.launch_plan/launchplan) |  |
| [`flytekit.models.launch_plan.LaunchPlanClosure`](packages/flytekit.models.launch_plan/launchplanclosure) |  |
| [`flytekit.models.launch_plan.LaunchPlanMetadata`](packages/flytekit.models.launch_plan/launchplanmetadata) |  |
| [`flytekit.models.launch_plan.LaunchPlanSpec`](packages/flytekit.models.launch_plan/launchplanspec) |  |
| [`flytekit.models.launch_plan.LaunchPlanState`](packages/flytekit.models.launch_plan/launchplanstate) |  |
| [`flytekit.models.literals.Binary`](packages/flytekit.models.literals/binary) |  |
| [`flytekit.models.literals.Binding`](packages/flytekit.models.literals/binding) |  |
| [`flytekit.models.literals.BindingData`](packages/flytekit.models.literals/bindingdata) |  |
| [`flytekit.models.literals.BindingDataCollection`](packages/flytekit.models.literals/bindingdatacollection) |  |
| [`flytekit.models.literals.BindingDataMap`](packages/flytekit.models.literals/bindingdatamap) |  |
| [`flytekit.models.literals.Blob`](packages/flytekit.models.literals/blob) |  |
| [`flytekit.models.literals.BlobMetadata`](packages/flytekit.models.literals/blobmetadata) | This is metadata for the Blob literal. |
| [`flytekit.models.literals.Literal`](packages/flytekit.models.literals/literal) |  |
| [`flytekit.models.literals.LiteralCollection`](packages/flytekit.models.literals/literalcollection) |  |
| [`flytekit.models.literals.LiteralMap`](packages/flytekit.models.literals/literalmap) |  |
| [`flytekit.models.literals.LiteralOffloadedMetadata`](packages/flytekit.models.literals/literaloffloadedmetadata) |  |
| [`flytekit.models.literals.Primitive`](packages/flytekit.models.literals/primitive) |  |
| [`flytekit.models.literals.RetryStrategy`](packages/flytekit.models.literals/retrystrategy) |  |
| [`flytekit.models.literals.Scalar`](packages/flytekit.models.literals/scalar) |  |
| [`flytekit.models.literals.Schema`](packages/flytekit.models.literals/schema) |  |
| [`flytekit.models.literals.StructuredDataset`](packages/flytekit.models.literals/structureddataset) |  |
| [`flytekit.models.literals.StructuredDatasetMetadata`](packages/flytekit.models.literals/structureddatasetmetadata) |  |
| [`flytekit.models.literals.Union`](packages/flytekit.models.literals/union) |  |
| [`flytekit.models.literals.Void`](packages/flytekit.models.literals/void) |  |
| [`flytekit.models.matchable_resource.ClusterResourceAttributes`](packages/flytekit.models.matchable_resource/clusterresourceattributes) |  |
| [`flytekit.models.matchable_resource.ExecutionClusterLabel`](packages/flytekit.models.matchable_resource/executionclusterlabel) |  |
| [`flytekit.models.matchable_resource.ExecutionQueueAttributes`](packages/flytekit.models.matchable_resource/executionqueueattributes) |  |
| [`flytekit.models.matchable_resource.MatchableResource`](packages/flytekit.models.matchable_resource/matchableresource) |  |
| [`flytekit.models.matchable_resource.MatchingAttributes`](packages/flytekit.models.matchable_resource/matchingattributes) |  |
| [`flytekit.models.matchable_resource.PluginOverride`](packages/flytekit.models.matchable_resource/pluginoverride) |  |
| [`flytekit.models.matchable_resource.PluginOverrides`](packages/flytekit.models.matchable_resource/pluginoverrides) |  |
| [`flytekit.models.named_entity.NamedEntityIdentifier`](packages/flytekit.models.named_entity/namedentityidentifier) |  |
| [`flytekit.models.named_entity.NamedEntityMetadata`](packages/flytekit.models.named_entity/namedentitymetadata) |  |
| [`flytekit.models.named_entity.NamedEntityState`](packages/flytekit.models.named_entity/namedentitystate) |  |
| [`flytekit.models.node_execution.DynamicWorkflowNodeMetadata`](packages/flytekit.models.node_execution/dynamicworkflownodemetadata) |  |
| [`flytekit.models.node_execution.NodeExecution`](packages/flytekit.models.node_execution/nodeexecution) |  |
| [`flytekit.models.node_execution.NodeExecutionClosure`](packages/flytekit.models.node_execution/nodeexecutionclosure) |  |
| [`flytekit.models.node_execution.TaskNodeMetadata`](packages/flytekit.models.node_execution/tasknodemetadata) |  |
| [`flytekit.models.node_execution.WorkflowNodeMetadata`](packages/flytekit.models.node_execution/workflownodemetadata) |  |
| [`flytekit.models.presto.PrestoQuery`](packages/flytekit.models.presto/prestoquery) |  |
| [`flytekit.models.project.Project`](packages/flytekit.models.project/project) |  |
| [`flytekit.models.qubole.HiveQuery`](packages/flytekit.models.qubole/hivequery) |  |
| [`flytekit.models.qubole.HiveQueryCollection`](packages/flytekit.models.qubole/hivequerycollection) |  |
| [`flytekit.models.qubole.QuboleHiveJob`](packages/flytekit.models.qubole/qubolehivejob) |  |
| [`flytekit.models.schedule.Schedule`](packages/flytekit.models.schedule/schedule) |  |
| [`flytekit.models.security.Identity`](packages/flytekit.models.security/identity) |  |
| [`flytekit.models.security.OAuth2Client`](packages/flytekit.models.security/oauth2client) |  |
| [`flytekit.models.security.OAuth2TokenRequest`](packages/flytekit.models.security/oauth2tokenrequest) |  |
| [`flytekit.models.security.Secret`](packages/flytekit.models.security/secret) | See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.models.security.SecurityContext`](packages/flytekit.models.security/securitycontext) | This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.models.task.CompiledTask`](packages/flytekit.models.task/compiledtask) |  |
| [`flytekit.models.task.Container`](packages/flytekit.models.task/container) |  |
| [`flytekit.models.task.DataLoadingConfig`](packages/flytekit.models.task/dataloadingconfig) |  |
| [`flytekit.models.task.IOStrategy`](packages/flytekit.models.task/iostrategy) | Provides methods to manage data in and out of the Raw container using Download Modes. |
| [`flytekit.models.task.K8sObjectMetadata`](packages/flytekit.models.task/k8sobjectmetadata) |  |
| [`flytekit.models.task.K8sPod`](packages/flytekit.models.task/k8spod) |  |
| [`flytekit.models.task.Resources`](packages/flytekit.models.task/resources) |  |
| [`flytekit.models.task.RuntimeMetadata`](packages/flytekit.models.task/runtimemetadata) |  |
| [`flytekit.models.task.Sql`](packages/flytekit.models.task/sql) |  |
| [`flytekit.models.task.Task`](packages/flytekit.models.task/task) |  |
| [`flytekit.models.task.TaskClosure`](packages/flytekit.models.task/taskclosure) |  |
| [`flytekit.models.task.TaskExecutionMetadata`](packages/flytekit.models.task/taskexecutionmetadata) |  |
| [`flytekit.models.task.TaskMetadata`](packages/flytekit.models.task/taskmetadata) |  |
| [`flytekit.models.task.TaskSpec`](packages/flytekit.models.task/taskspec) |  |
| [`flytekit.models.task.TaskTemplate`](packages/flytekit.models.task/tasktemplate) |  |
| [`flytekit.models.types.Error`](packages/flytekit.models.types/error) |  |
| [`flytekit.models.types.LiteralType`](packages/flytekit.models.types/literaltype) |  |
| [`flytekit.models.types.OutputReference`](packages/flytekit.models.types/outputreference) |  |
| [`flytekit.models.types.SchemaType`](packages/flytekit.models.types/schematype) |  |
| [`flytekit.models.types.SimpleType`](packages/flytekit.models.types/simpletype) |  |
| [`flytekit.models.types.StructuredDatasetType`](packages/flytekit.models.types/structureddatasettype) |  |
| [`flytekit.models.types.TypeStructure`](packages/flytekit.models.types/typestructure) | Models _types_pb2. |
| [`flytekit.models.types.UnionType`](packages/flytekit.models.types/uniontype) | Models _types_pb2. |
| [`flytekit.models.workflow_closure.WorkflowClosure`](packages/flytekit.models.workflow_closure/workflowclosure) |  |
| [`flytekit.remote.entities.FlyteArrayNode`](packages/flytekit.remote.entities/flytearraynode) |  |
| [`flytekit.remote.entities.FlyteBranchNode`](packages/flytekit.remote.entities/flytebranchnode) |  |
| [`flytekit.remote.entities.FlyteGateNode`](packages/flytekit.remote.entities/flytegatenode) |  |
| [`flytekit.remote.entities.FlyteLaunchPlan`](packages/flytekit.remote.entities/flytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.entities.FlyteNode`](packages/flytekit.remote.entities/flytenode) | A class encapsulating a remote Flyte node. |
| [`flytekit.remote.entities.FlyteTask`](packages/flytekit.remote.entities/flytetask) | A class encapsulating a remote Flyte task. |
| [`flytekit.remote.entities.FlyteTaskNode`](packages/flytekit.remote.entities/flytetasknode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`flytekit.remote.entities.FlyteWorkflow`](packages/flytekit.remote.entities/flyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.entities.FlyteWorkflowNode`](packages/flytekit.remote.entities/flyteworkflownode) | A class encapsulating a workflow that a Flyte node needs to execute. |
| [`flytekit.remote.executions.FlyteNodeExecution`](packages/flytekit.remote.executions/flytenodeexecution) | A class encapsulating a node execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteTaskExecution`](packages/flytekit.remote.executions/flytetaskexecution) | A class encapsulating a task execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteWorkflowExecution`](packages/flytekit.remote.executions/flyteworkflowexecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.RemoteExecutionBase`](packages/flytekit.remote.executions/remoteexecutionbase) |  |
| [`flytekit.remote.interface.TypedInterface`](packages/flytekit.remote.interface/typedinterface) |  |
| [`flytekit.remote.lazy_entity.LazyEntity`](packages/flytekit.remote.lazy_entity/lazyentity) | Fetches the entity when the entity is called or when the entity is retrieved. |
| [`flytekit.remote.metrics.FlyteExecutionSpan`](packages/flytekit.remote.metrics/flyteexecutionspan) |  |
| [`flytekit.remote.remote.FlyteRemote`](packages/flytekit.remote.remote/flyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.remote.remote.RegistrationSkipped`](packages/flytekit.remote.remote/registrationskipped) | RegistrationSkipped error is raised when trying to register an entity that is not registrable. |
| [`flytekit.remote.remote.ResolvedIdentifiers`](packages/flytekit.remote.remote/resolvedidentifiers) |  |
| [`flytekit.remote.remote_callable.RemoteEntity`](packages/flytekit.remote.remote_callable/remoteentity) |  |
| [`flytekit.remote.remote_fs.FlyteFS`](packages/flytekit.remote.remote_fs/flytefs) | Want this to behave mostly just like the HTTP file system. |
| [`flytekit.remote.remote_fs.FlytePathResolver`](packages/flytekit.remote.remote_fs/flytepathresolver) |  |
| [`flytekit.remote.remote_fs.HttpFileWriter`](packages/flytekit.remote.remote_fs/httpfilewriter) |  |
| [`flytekit.sensor.base_sensor.BaseSensor`](packages/flytekit.sensor.base_sensor/basesensor) | Base class for all sensors. |
| [`flytekit.sensor.base_sensor.SensorConfig`](packages/flytekit.sensor.base_sensor/sensorconfig) |  |
| [`flytekit.sensor.base_sensor.SensorMetadata`](packages/flytekit.sensor.base_sensor/sensormetadata) |  |
| [`flytekit.sensor.file_sensor.FileSensor`](packages/flytekit.sensor.file_sensor/filesensor) |  |
| [`flytekit.sensor.sensor_engine.SensorEngine`](packages/flytekit.sensor.sensor_engine/sensorengine) |  |
| [`flytekit.tools.fast_registration.FastPackageOptions`](packages/flytekit.tools.fast_registration/fastpackageoptions) | FastPackageOptions is used to set configuration options when packaging files. |
| [`flytekit.tools.ignore.DockerIgnore`](packages/flytekit.tools.ignore/dockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`flytekit.tools.ignore.FlyteIgnore`](packages/flytekit.tools.ignore/flyteignore) | Uses a. |
| [`flytekit.tools.ignore.GitIgnore`](packages/flytekit.tools.ignore/gitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`flytekit.tools.ignore.Ignore`](packages/flytekit.tools.ignore/ignore) | Base for Ignores, implements core logic. |
| [`flytekit.tools.ignore.IgnoreGroup`](packages/flytekit.tools.ignore/ignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`flytekit.tools.ignore.StandardIgnore`](packages/flytekit.tools.ignore/standardignore) | Retains the standard ignore functionality that previously existed. |
| [`flytekit.tools.repo.NoSerializableEntitiesError`](packages/flytekit.tools.repo/noserializableentitieserror) |  |
| [`flytekit.types.directory.types.FlyteDirToMultipartBlobTransformer`](packages/flytekit.types.directory.types/flytedirtomultipartblobtransformer) | This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`flytekit.types.directory.types.FlyteDirectory`](packages/flytekit.types.directory.types/flytedirectory) |  |
| [`flytekit.types.error.error.ErrorTransformer`](packages/flytekit.types.error.error/errortransformer) | Enables converting a python type FlyteError to LiteralType. |
| [`flytekit.types.error.error.FlyteError`](packages/flytekit.types.error.error/flyteerror) | Special Task type that will be used in the failure node. |
| [`flytekit.types.file.FileExt`](packages/flytekit.types.file/fileext) | Used for annotating file extension types of FlyteFile. |
| [`flytekit.types.file.file.FlyteFile`](packages/flytekit.types.file.file/flytefile) |  |
| [`flytekit.types.file.file.FlyteFilePathTransformer`](packages/flytekit.types.file.file/flytefilepathtransformer) |  |
| [`flytekit.types.file.image.PILImageTransformer`](packages/flytekit.types.file.image/pilimagetransformer) | TypeTransformer that supports PIL. |
| [`flytekit.types.iterator.iterator.FlyteIterator`](packages/flytekit.types.iterator.iterator/flyteiterator) |  |
| [`flytekit.types.iterator.iterator.IteratorTransformer`](packages/flytekit.types.iterator.iterator/iteratortransformer) |  |
| [`flytekit.types.iterator.json_iterator.JSONIterator`](packages/flytekit.types.iterator.json_iterator/jsoniterator) |  |
| [`flytekit.types.iterator.json_iterator.JSONIteratorTransformer`](packages/flytekit.types.iterator.json_iterator/jsoniteratortransformer) | A JSON iterator that handles conversion between an iterator/generator and a JSONL file. |
| [`flytekit.types.numpy.ndarray.NumpyArrayTransformer`](packages/flytekit.types.numpy.ndarray/numpyarraytransformer) | TypeTransformer that supports np. |
| [`flytekit.types.pickle.pickle.FlytePickle`](packages/flytekit.types.pickle.pickle/flytepickle) | This type is only used by flytekit internally. |
| [`flytekit.types.pickle.pickle.FlytePickleTransformer`](packages/flytekit.types.pickle.pickle/flytepickletransformer) |  |
| [`flytekit.types.schema.types.FlyteSchema`](packages/flytekit.types.schema.types/flyteschema) |  |
| [`flytekit.types.schema.types.FlyteSchemaTransformer`](packages/flytekit.types.schema.types/flyteschematransformer) |  |
| [`flytekit.types.schema.types.LocalIOSchemaReader`](packages/flytekit.types.schema.types/localioschemareader) |  |
| [`flytekit.types.schema.types.LocalIOSchemaWriter`](packages/flytekit.types.schema.types/localioschemawriter) |  |
| [`flytekit.types.schema.types.SchemaEngine`](packages/flytekit.types.schema.types/schemaengine) | This is the core Engine that handles all schema sub-systems. |
| [`flytekit.types.schema.types.SchemaFormat`](packages/flytekit.types.schema.types/schemaformat) | Represents the schema storage format (at rest). |
| [`flytekit.types.schema.types.SchemaHandler`](packages/flytekit.types.schema.types/schemahandler) |  |
| [`flytekit.types.schema.types.SchemaOpenMode`](packages/flytekit.types.schema.types/schemaopenmode) |  |
| [`flytekit.types.schema.types.SchemaReader`](packages/flytekit.types.schema.types/schemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types.SchemaWriter`](packages/flytekit.types.schema.types/schemawriter) |  |
| [`flytekit.types.schema.types_pandas.PandasDataFrameTransformer`](packages/flytekit.types.schema.types_pandas/pandasdataframetransformer) | Transforms a pd. |
| [`flytekit.types.schema.types_pandas.PandasSchemaReader`](packages/flytekit.types.schema.types_pandas/pandasschemareader) |  |
| [`flytekit.types.schema.types_pandas.PandasSchemaWriter`](packages/flytekit.types.schema.types_pandas/pandasschemawriter) |  |
| [`flytekit.types.schema.types_pandas.ParquetIO`](packages/flytekit.types.schema.types_pandas/parquetio) |  |
| [`flytekit.types.structured.basic_dfs.ArrowToParquetEncodingHandler`](packages/flytekit.types.structured.basic_dfs/arrowtoparquetencodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.CSVToPandasDecodingHandler`](packages/flytekit.types.structured.basic_dfs/csvtopandasdecodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.PandasToCSVEncodingHandler`](packages/flytekit.types.structured.basic_dfs/pandastocsvencodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.PandasToParquetEncodingHandler`](packages/flytekit.types.structured.basic_dfs/pandastoparquetencodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.ParquetToArrowDecodingHandler`](packages/flytekit.types.structured.basic_dfs/parquettoarrowdecodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.ParquetToPandasDecodingHandler`](packages/flytekit.types.structured.basic_dfs/parquettopandasdecodinghandler) |  |
| [`flytekit.types.structured.bigquery.ArrowToBQEncodingHandlers`](packages/flytekit.types.structured.bigquery/arrowtobqencodinghandlers) |  |
| [`flytekit.types.structured.bigquery.BQToArrowDecodingHandler`](packages/flytekit.types.structured.bigquery/bqtoarrowdecodinghandler) |  |
| [`flytekit.types.structured.bigquery.BQToPandasDecodingHandler`](packages/flytekit.types.structured.bigquery/bqtopandasdecodinghandler) |  |
| [`flytekit.types.structured.bigquery.PandasToBQEncodingHandlers`](packages/flytekit.types.structured.bigquery/pandastobqencodinghandlers) |  |
| [`flytekit.types.structured.snowflake.PandasToSnowflakeEncodingHandlers`](packages/flytekit.types.structured.snowflake/pandastosnowflakeencodinghandlers) |  |
| [`flytekit.types.structured.snowflake.SnowflakeToPandasDecodingHandler`](packages/flytekit.types.structured.snowflake/snowflaketopandasdecodinghandler) |  |
| [`flytekit.types.structured.structured_dataset.DuplicateHandlerError`](packages/flytekit.types.structured.structured_dataset/duplicatehandlererror) |  |
| [`flytekit.types.structured.structured_dataset.StructuredDataset`](packages/flytekit.types.structured.structured_dataset/structureddataset) | This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetDecoder`](packages/flytekit.types.structured.structured_dataset/structureddatasetdecoder) |  |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetEncoder`](packages/flytekit.types.structured.structured_dataset/structureddatasetencoder) |  |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetTransformerEngine`](packages/flytekit.types.structured.structured_dataset/structureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flytekit.utils.rate_limiter.RateLimiter`](packages/flytekit.utils.rate_limiter/ratelimiter) | Rate limiter that allows up to a certain number of requests per minute. |

### Packages

| Package | Description |
|-|-|
| [`flytekit`](packages/flytekit/_index) | This package contains all of the most common abstractions you'll need to write Flyte workflows and extend Flytekit. |
| [`flytekit.bin.entrypoint`](packages/flytekit.bin.entrypoint/_index) |  |
| [`flytekit.clients.auth.auth_client`](packages/flytekit.clients.auth.auth_client/_index) |  |
| [`flytekit.clients.auth.authenticator`](packages/flytekit.clients.auth.authenticator/_index) |  |
| [`flytekit.clients.auth.default_html`](packages/flytekit.clients.auth.default_html/_index) |  |
| [`flytekit.clients.auth.exceptions`](packages/flytekit.clients.auth.exceptions/_index) |  |
| [`flytekit.clients.auth.keyring`](packages/flytekit.clients.auth.keyring/_index) |  |
| [`flytekit.clients.auth.token_client`](packages/flytekit.clients.auth.token_client/_index) |  |
| [`flytekit.clients.auth_helper`](packages/flytekit.clients.auth_helper/_index) |  |
| [`flytekit.clients.friendly`](packages/flytekit.clients.friendly/_index) |  |
| [`flytekit.clients.grpc_utils.auth_interceptor`](packages/flytekit.clients.grpc_utils.auth_interceptor/_index) |  |
| [`flytekit.clients.grpc_utils.deadline_interceptor`](packages/flytekit.clients.grpc_utils.deadline_interceptor/_index) |  |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor`](packages/flytekit.clients.grpc_utils.default_metadata_interceptor/_index) |  |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor`](packages/flytekit.clients.grpc_utils.wrap_exception_interceptor/_index) |  |
| [`flytekit.clients.helpers`](packages/flytekit.clients.helpers/_index) |  |
| [`flytekit.clients.raw`](packages/flytekit.clients.raw/_index) |  |
| [`flytekit.clis.helpers`](packages/flytekit.clis.helpers/_index) |  |
| [`flytekit.clis.sdk_in_container.backfill`](packages/flytekit.clis.sdk_in_container.backfill/_index) |  |
| [`flytekit.clis.sdk_in_container.build`](packages/flytekit.clis.sdk_in_container.build/_index) |  |
| [`flytekit.clis.sdk_in_container.constants`](packages/flytekit.clis.sdk_in_container.constants/_index) |  |
| [`flytekit.clis.sdk_in_container.executions`](packages/flytekit.clis.sdk_in_container.executions/_index) |  |
| [`flytekit.clis.sdk_in_container.helpers`](packages/flytekit.clis.sdk_in_container.helpers/_index) |  |
| [`flytekit.clis.sdk_in_container.metrics`](packages/flytekit.clis.sdk_in_container.metrics/_index) |  |
| [`flytekit.clis.sdk_in_container.package`](packages/flytekit.clis.sdk_in_container.package/_index) |  |
| [`flytekit.clis.sdk_in_container.pyflyte`](packages/flytekit.clis.sdk_in_container.pyflyte/_index) |  |
| [`flytekit.clis.sdk_in_container.run`](packages/flytekit.clis.sdk_in_container.run/_index) |  |
| [`flytekit.clis.sdk_in_container.serialize`](packages/flytekit.clis.sdk_in_container.serialize/_index) |  |
| [`flytekit.clis.sdk_in_container.serve`](packages/flytekit.clis.sdk_in_container.serve/_index) |  |
| [`flytekit.clis.sdk_in_container.utils`](packages/flytekit.clis.sdk_in_container.utils/_index) |  |
| [`flytekit.clis.version`](packages/flytekit.clis.version/_index) |  |
| [`flytekit.configuration`](packages/flytekit.configuration/_index) | # Configuration. |
| [`flytekit.configuration.default_images`](packages/flytekit.configuration.default_images/_index) |  |
| [`flytekit.configuration.feature_flags`](packages/flytekit.configuration.feature_flags/_index) |  |
| [`flytekit.configuration.file`](packages/flytekit.configuration.file/_index) |  |
| [`flytekit.configuration.internal`](packages/flytekit.configuration.internal/_index) |  |
| [`flytekit.configuration.plugin`](packages/flytekit.configuration.plugin/_index) | Defines a plugin API allowing other libraries to modify the behavior of flytekit. |
| [`flytekit.constants`](packages/flytekit.constants/_index) |  |
| [`flytekit.core.annotation`](packages/flytekit.core.annotation/_index) |  |
| [`flytekit.core.array_node`](packages/flytekit.core.array_node/_index) |  |
| [`flytekit.core.array_node_map_task`](packages/flytekit.core.array_node_map_task/_index) |  |
| [`flytekit.core.artifact`](packages/flytekit.core.artifact/_index) |  |
| [`flytekit.core.artifact_utils`](packages/flytekit.core.artifact_utils/_index) |  |
| [`flytekit.core.base_sql_task`](packages/flytekit.core.base_sql_task/_index) |  |
| [`flytekit.core.base_task`](packages/flytekit.core.base_task/_index) | # flytekit. |
| [`flytekit.core.cache`](packages/flytekit.core.cache/_index) |  |
| [`flytekit.core.checkpointer`](packages/flytekit.core.checkpointer/_index) |  |
| [`flytekit.core.class_based_resolver`](packages/flytekit.core.class_based_resolver/_index) |  |
| [`flytekit.core.condition`](packages/flytekit.core.condition/_index) |  |
| [`flytekit.core.constants`](packages/flytekit.core.constants/_index) |  |
| [`flytekit.core.container_task`](packages/flytekit.core.container_task/_index) |  |
| [`flytekit.core.context_manager`](packages/flytekit.core.context_manager/_index) | These classes provide functionality related context management. |
| [`flytekit.core.data_persistence`](packages/flytekit.core.data_persistence/_index) | The Data persistence module is used by core flytekit and most of the core TypeTransformers to manage data fetch & store,. |
| [`flytekit.core.docstring`](packages/flytekit.core.docstring/_index) |  |
| [`flytekit.core.environment`](packages/flytekit.core.environment/_index) |  |
| [`flytekit.core.gate`](packages/flytekit.core.gate/_index) |  |
| [`flytekit.core.hash`](packages/flytekit.core.hash/_index) |  |
| [`flytekit.core.interface`](packages/flytekit.core.interface/_index) |  |
| [`flytekit.core.launch_plan`](packages/flytekit.core.launch_plan/_index) |  |
| [`flytekit.core.legacy_map_task`](packages/flytekit.core.legacy_map_task/_index) | Flytekit map tasks specify how to run a single task across a list of inputs. |
| [`flytekit.core.local_cache`](packages/flytekit.core.local_cache/_index) |  |
| [`flytekit.core.local_fsspec`](packages/flytekit.core.local_fsspec/_index) |  |
| [`flytekit.core.mock_stats`](packages/flytekit.core.mock_stats/_index) |  |
| [`flytekit.core.node`](packages/flytekit.core.node/_index) |  |
| [`flytekit.core.node_creation`](packages/flytekit.core.node_creation/_index) |  |
| [`flytekit.core.notification`](packages/flytekit.core.notification/_index) | Notifications are primarily used when defining Launch Plans (also can be used when launching executions) and will trigger. |
| [`flytekit.core.options`](packages/flytekit.core.options/_index) |  |
| [`flytekit.core.pod_template`](packages/flytekit.core.pod_template/_index) |  |
| [`flytekit.core.promise`](packages/flytekit.core.promise/_index) |  |
| [`flytekit.core.python_auto_container`](packages/flytekit.core.python_auto_container/_index) |  |
| [`flytekit.core.python_customized_container_task`](packages/flytekit.core.python_customized_container_task/_index) |  |
| [`flytekit.core.python_function_task`](packages/flytekit.core.python_function_task/_index) |  |
| [`flytekit.core.reference`](packages/flytekit.core.reference/_index) |  |
| [`flytekit.core.reference_entity`](packages/flytekit.core.reference_entity/_index) |  |
| [`flytekit.core.resources`](packages/flytekit.core.resources/_index) |  |
| [`flytekit.core.schedule`](packages/flytekit.core.schedule/_index) | These classes provide functionality related to schedules. |
| [`flytekit.core.shim_task`](packages/flytekit.core.shim_task/_index) |  |
| [`flytekit.core.task`](packages/flytekit.core.task/_index) |  |
| [`flytekit.core.testing`](packages/flytekit.core.testing/_index) |  |
| [`flytekit.core.tracked_abc`](packages/flytekit.core.tracked_abc/_index) |  |
| [`flytekit.core.tracker`](packages/flytekit.core.tracker/_index) |  |
| [`flytekit.core.type_engine`](packages/flytekit.core.type_engine/_index) |  |
| [`flytekit.core.type_helpers`](packages/flytekit.core.type_helpers/_index) |  |
| [`flytekit.core.type_match_checking`](packages/flytekit.core.type_match_checking/_index) |  |
| [`flytekit.core.utils`](packages/flytekit.core.utils/_index) |  |
| [`flytekit.core.worker_queue`](packages/flytekit.core.worker_queue/_index) |  |
| [`flytekit.core.workflow`](packages/flytekit.core.workflow/_index) |  |
| [`flytekit.deck.deck`](packages/flytekit.deck.deck/_index) |  |
| [`flytekit.deck.renderer`](packages/flytekit.deck.renderer/_index) |  |
| [`flytekit.exceptions.base`](packages/flytekit.exceptions.base/_index) |  |
| [`flytekit.exceptions.eager`](packages/flytekit.exceptions.eager/_index) |  |
| [`flytekit.exceptions.scopes`](packages/flytekit.exceptions.scopes/_index) |  |
| [`flytekit.exceptions.system`](packages/flytekit.exceptions.system/_index) |  |
| [`flytekit.exceptions.user`](packages/flytekit.exceptions.user/_index) |  |
| [`flytekit.exceptions.utils`](packages/flytekit.exceptions.utils/_index) |  |
| [`flytekit.experimental.eager_function`](packages/flytekit.experimental.eager_function/_index) |  |
| [`flytekit.extend.backend.base_connector`](packages/flytekit.extend.backend.base_connector/_index) |  |
| [`flytekit.extend.backend.connector_service`](packages/flytekit.extend.backend.connector_service/_index) |  |
| [`flytekit.extend.backend.utils`](packages/flytekit.extend.backend.utils/_index) |  |
| [`flytekit.extras.accelerators`](packages/flytekit.extras.accelerators/_index) | ## Specifying Accelerators. |
| [`flytekit.extras.cloud_pickle_resolver`](packages/flytekit.extras.cloud_pickle_resolver/_index) |  |
| [`flytekit.extras.pydantic_transformer.transformer`](packages/flytekit.extras.pydantic_transformer.transformer/_index) |  |
| [`flytekit.extras.sklearn.native`](packages/flytekit.extras.sklearn.native/_index) |  |
| [`flytekit.extras.sqlite3.task`](packages/flytekit.extras.sqlite3.task/_index) |  |
| [`flytekit.extras.tasks.shell`](packages/flytekit.extras.tasks.shell/_index) |  |
| [`flytekit.extras.webhook`](packages/flytekit.extras.webhook/_index) |  |
| [`flytekit.extras.webhook.connector`](packages/flytekit.extras.webhook.connector/_index) |  |
| [`flytekit.extras.webhook.constants`](packages/flytekit.extras.webhook.constants/_index) |  |
| [`flytekit.extras.webhook.task`](packages/flytekit.extras.webhook.task/_index) |  |
| [`flytekit.image_spec.default_builder`](packages/flytekit.image_spec.default_builder/_index) |  |
| [`flytekit.image_spec.image_spec`](packages/flytekit.image_spec.image_spec/_index) |  |
| [`flytekit.image_spec.noop_builder`](packages/flytekit.image_spec.noop_builder/_index) |  |
| [`flytekit.interaction.click_types`](packages/flytekit.interaction.click_types/_index) |  |
| [`flytekit.interaction.parse_stdin`](packages/flytekit.interaction.parse_stdin/_index) |  |
| [`flytekit.interaction.rich_utils`](packages/flytekit.interaction.rich_utils/_index) |  |
| [`flytekit.interaction.string_literals`](packages/flytekit.interaction.string_literals/_index) |  |
| [`flytekit.interactive`](packages/flytekit.interactive/_index) | This module provides functionality related to Flytekit Interactive. |
| [`flytekit.interactive.constants`](packages/flytekit.interactive.constants/_index) |  |
| [`flytekit.interactive.utils`](packages/flytekit.interactive.utils/_index) |  |
| [`flytekit.interactive.vscode_lib.config`](packages/flytekit.interactive.vscode_lib.config/_index) |  |
| [`flytekit.interactive.vscode_lib.decorator`](packages/flytekit.interactive.vscode_lib.decorator/_index) |  |
| [`flytekit.interactive.vscode_lib.vscode_constants`](packages/flytekit.interactive.vscode_lib.vscode_constants/_index) |  |
| [`flytekit.interfaces.cli_identifiers`](packages/flytekit.interfaces.cli_identifiers/_index) |  |
| [`flytekit.interfaces.random`](packages/flytekit.interfaces.random/_index) |  |
| [`flytekit.interfaces.stats.client`](packages/flytekit.interfaces.stats.client/_index) |  |
| [`flytekit.interfaces.stats.taggable`](packages/flytekit.interfaces.stats.taggable/_index) |  |
| [`flytekit.lazy_import.lazy_module`](packages/flytekit.lazy_import.lazy_module/_index) |  |
| [`flytekit.loggers`](packages/flytekit.loggers/_index) |  |
| [`flytekit.models.admin.common`](packages/flytekit.models.admin.common/_index) |  |
| [`flytekit.models.admin.task_execution`](packages/flytekit.models.admin.task_execution/_index) |  |
| [`flytekit.models.admin.workflow`](packages/flytekit.models.admin.workflow/_index) |  |
| [`flytekit.models.annotation`](packages/flytekit.models.annotation/_index) |  |
| [`flytekit.models.array_job`](packages/flytekit.models.array_job/_index) |  |
| [`flytekit.models.common`](packages/flytekit.models.common/_index) |  |
| [`flytekit.models.concurrency`](packages/flytekit.models.concurrency/_index) |  |
| [`flytekit.models.core.catalog`](packages/flytekit.models.core.catalog/_index) |  |
| [`flytekit.models.core.compiler`](packages/flytekit.models.core.compiler/_index) |  |
| [`flytekit.models.core.condition`](packages/flytekit.models.core.condition/_index) |  |
| [`flytekit.models.core.errors`](packages/flytekit.models.core.errors/_index) |  |
| [`flytekit.models.core.execution`](packages/flytekit.models.core.execution/_index) |  |
| [`flytekit.models.core.identifier`](packages/flytekit.models.core.identifier/_index) |  |
| [`flytekit.models.core.types`](packages/flytekit.models.core.types/_index) |  |
| [`flytekit.models.core.workflow`](packages/flytekit.models.core.workflow/_index) |  |
| [`flytekit.models.documentation`](packages/flytekit.models.documentation/_index) |  |
| [`flytekit.models.domain`](packages/flytekit.models.domain/_index) |  |
| [`flytekit.models.dynamic_job`](packages/flytekit.models.dynamic_job/_index) |  |
| [`flytekit.models.event`](packages/flytekit.models.event/_index) |  |
| [`flytekit.models.execution`](packages/flytekit.models.execution/_index) |  |
| [`flytekit.models.filters`](packages/flytekit.models.filters/_index) |  |
| [`flytekit.models.interface`](packages/flytekit.models.interface/_index) |  |
| [`flytekit.models.launch_plan`](packages/flytekit.models.launch_plan/_index) |  |
| [`flytekit.models.literals`](packages/flytekit.models.literals/_index) |  |
| [`flytekit.models.matchable_resource`](packages/flytekit.models.matchable_resource/_index) |  |
| [`flytekit.models.named_entity`](packages/flytekit.models.named_entity/_index) |  |
| [`flytekit.models.node_execution`](packages/flytekit.models.node_execution/_index) |  |
| [`flytekit.models.presto`](packages/flytekit.models.presto/_index) | This is a deprecated module. |
| [`flytekit.models.project`](packages/flytekit.models.project/_index) |  |
| [`flytekit.models.qubole`](packages/flytekit.models.qubole/_index) | This is a deprecated module. |
| [`flytekit.models.schedule`](packages/flytekit.models.schedule/_index) |  |
| [`flytekit.models.security`](packages/flytekit.models.security/_index) |  |
| [`flytekit.models.task`](packages/flytekit.models.task/_index) |  |
| [`flytekit.models.types`](packages/flytekit.models.types/_index) |  |
| [`flytekit.models.workflow_closure`](packages/flytekit.models.workflow_closure/_index) |  |
| [`flytekit.remote.backfill`](packages/flytekit.remote.backfill/_index) |  |
| [`flytekit.remote.data`](packages/flytekit.remote.data/_index) |  |
| [`flytekit.remote.entities`](packages/flytekit.remote.entities/_index) | This module contains shadow entities for all Flyte entities as represented in Flyte Admin / Control Plane. |
| [`flytekit.remote.executions`](packages/flytekit.remote.executions/_index) |  |
| [`flytekit.remote.interface`](packages/flytekit.remote.interface/_index) |  |
| [`flytekit.remote.lazy_entity`](packages/flytekit.remote.lazy_entity/_index) |  |
| [`flytekit.remote.metrics`](packages/flytekit.remote.metrics/_index) |  |
| [`flytekit.remote.remote`](packages/flytekit.remote.remote/_index) | This module provides the ``FlyteRemote`` object, which is the end-user's main starting point for interacting. |
| [`flytekit.remote.remote_callable`](packages/flytekit.remote.remote_callable/_index) |  |
| [`flytekit.remote.remote_fs`](packages/flytekit.remote.remote_fs/_index) |  |
| [`flytekit.sensor.base_sensor`](packages/flytekit.sensor.base_sensor/_index) |  |
| [`flytekit.sensor.file_sensor`](packages/flytekit.sensor.file_sensor/_index) |  |
| [`flytekit.sensor.sensor_engine`](packages/flytekit.sensor.sensor_engine/_index) |  |
| [`flytekit.tools.fast_registration`](packages/flytekit.tools.fast_registration/_index) |  |
| [`flytekit.tools.ignore`](packages/flytekit.tools.ignore/_index) |  |
| [`flytekit.tools.interactive`](packages/flytekit.tools.interactive/_index) |  |
| [`flytekit.tools.module_loader`](packages/flytekit.tools.module_loader/_index) |  |
| [`flytekit.tools.repo`](packages/flytekit.tools.repo/_index) |  |
| [`flytekit.tools.script_mode`](packages/flytekit.tools.script_mode/_index) |  |
| [`flytekit.tools.serialize_helpers`](packages/flytekit.tools.serialize_helpers/_index) |  |
| [`flytekit.tools.subprocess`](packages/flytekit.tools.subprocess/_index) |  |
| [`flytekit.tools.translator`](packages/flytekit.tools.translator/_index) |  |
| [`flytekit.types.directory`](packages/flytekit.types.directory/_index) | Similar to {{< py_class_ref flytekit.types.file.FlyteFile >}} there are some 'preformatted' directory types. |
| [`flytekit.types.directory.types`](packages/flytekit.types.directory.types/_index) |  |
| [`flytekit.types.error.error`](packages/flytekit.types.error.error/_index) |  |
| [`flytekit.types.file`](packages/flytekit.types.file/_index) | This module provides functionality related to FlyteFile. |
| [`flytekit.types.file.file`](packages/flytekit.types.file.file/_index) |  |
| [`flytekit.types.file.image`](packages/flytekit.types.file.image/_index) |  |
| [`flytekit.types.iterator.iterator`](packages/flytekit.types.iterator.iterator/_index) |  |
| [`flytekit.types.iterator.json_iterator`](packages/flytekit.types.iterator.json_iterator/_index) |  |
| [`flytekit.types.numpy.ndarray`](packages/flytekit.types.numpy.ndarray/_index) |  |
| [`flytekit.types.pickle.pickle`](packages/flytekit.types.pickle.pickle/_index) |  |
| [`flytekit.types.schema.types`](packages/flytekit.types.schema.types/_index) |  |
| [`flytekit.types.schema.types_pandas`](packages/flytekit.types.schema.types_pandas/_index) |  |
| [`flytekit.types.structured`](packages/flytekit.types.structured/_index) |  |
| [`flytekit.types.structured.basic_dfs`](packages/flytekit.types.structured.basic_dfs/_index) |  |
| [`flytekit.types.structured.bigquery`](packages/flytekit.types.structured.bigquery/_index) |  |
| [`flytekit.types.structured.snowflake`](packages/flytekit.types.structured.snowflake/_index) |  |
| [`flytekit.types.structured.structured_dataset`](packages/flytekit.types.structured.structured_dataset/_index) |  |
| [`flytekit.utils.asyn`](packages/flytekit.utils.asyn/_index) | Manages an async event loop on another thread. |
| [`flytekit.utils.dict_formatter`](packages/flytekit.utils.dict_formatter/_index) |  |
| [`flytekit.utils.pbhash`](packages/flytekit.utils.pbhash/_index) |  |
| [`flytekit.utils.rate_limiter`](packages/flytekit.utils.rate_limiter/_index) |  |

