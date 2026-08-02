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
| [`flytekit.clients.auth.auth_client.AuthorizationClient`](flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationclient) | Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`flytekit.clients.auth.auth_client.AuthorizationCode`](flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationcode) |  |
| [`flytekit.clients.auth.auth_client.EndpointMetadata`](flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientendpointmetadata) | This class can be used to control the rendering of the page on login successful or failure. |
| [`flytekit.clients.auth.auth_client.OAuthCallbackHandler`](flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthcallbackhandler) | A simple wrapper around BaseHTTPServer. |
| [`flytekit.clients.auth.auth_client.OAuthHTTPServer`](flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthhttpserver) | A simple wrapper around the BaseHTTPServer. |
| [`flytekit.clients.auth.authenticator.Authenticator`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticator) | Base authenticator for all authentication flows. |
| [`flytekit.clients.auth.authenticator.ClientConfig`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfig) | Client Configuration that is needed by the authenticator. |
| [`flytekit.clients.auth.authenticator.ClientConfigStore`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfigstore) | Client Config store retrieve client config. |
| [`flytekit.clients.auth.authenticator.ClientCredentialsAuthenticator`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientcredentialsauthenticator) | This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`flytekit.clients.auth.authenticator.CommandAuthenticator`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcommandauthenticator) | This Authenticator retrieves access_token using the provided command. |
| [`flytekit.clients.auth.authenticator.DeviceCodeAuthenticator`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatordevicecodeauthenticator) | This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`flytekit.clients.auth.authenticator.PKCEAuthenticator`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorpkceauthenticator) | This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`flytekit.clients.auth.authenticator.StaticClientConfigStore`](flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorstaticclientconfigstore) |  |
| [`flytekit.clients.auth.exceptions.AccessTokenNotFoundError`](flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsaccesstokennotfounderror) | This error is raised with Access token is not found or if Refreshing the token fails. |
| [`flytekit.clients.auth.exceptions.AuthenticationError`](flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsauthenticationerror) | This is raised for any AuthenticationError. |
| [`flytekit.clients.auth.exceptions.AuthenticationPending`](flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsauthenticationpending) | This is raised if the token endpoint returns authentication pending. |
| [`flytekit.clients.auth.keyring.Credentials`](flytekit.clients.auth.keyring#flytekitclientsauthkeyringcredentials) | Stores the credentials together. |
| [`flytekit.clients.auth.keyring.KeyringStore`](flytekit.clients.auth.keyring#flytekitclientsauthkeyringkeyringstore) | Methods to access Keyring Store. |
| [`flytekit.clients.auth.token_client.DeviceCodeResponse`](flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdevicecoderesponse) | Response from device auth flow endpoint. |
| [`flytekit.clients.auth.token_client.GrantType`](flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientgranttype) |  |
| [`flytekit.clients.auth_helper.AuthenticationHTTPAdapter`](flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticationhttpadapter) | A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`flytekit.clients.auth_helper.RemoteClientConfigStore`](flytekit.clients.auth_helper#flytekitclientsauth_helperremoteclientconfigstore) | This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |
| [`flytekit.clients.friendly.SynchronousFlyteClient`](flytekit.clients.friendly#flytekitclientsfriendlysynchronousflyteclient) | This is a low-level client that users can use to make direct gRPC service calls to the control plane. |
| [`flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor`](flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthunaryinterceptor) | This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`flytekit.clients.grpc_utils.deadline_interceptor.ScopedGrpcDeadlineInterceptor`](flytekit.clients.grpc_utils.deadline_interceptor#flytekitclientsgrpc_utilsdeadline_interceptorscopedgrpcdeadlineinterceptor) | Applies the currently scoped gRPC timeout to unary-unary calls. |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor.DefaultMetadataInterceptor`](flytekit.clients.grpc_utils.default_metadata_interceptor#flytekitclientsgrpc_utilsdefault_metadata_interceptordefaultmetadatainterceptor) |  |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.RetryExceptionWrapperInterceptor`](flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorretryexceptionwrapperinterceptor) |  |
| [`flytekit.clients.raw.RawSynchronousFlyteClient`](flytekit.clients.raw#flytekitclientsrawrawsynchronousflyteclient) | This is a thin synchronous wrapper around the auto-generated GRPC stubs for communicating with the admin service. |
| [`flytekit.clis.sdk_in_container.build.BuildCommand`](flytekit.clis.sdk_in_container.build#flytekitclissdk_in_containerbuildbuildcommand) | A click command group for building a image for flyte workflows & tasks in a file. |
| [`flytekit.clis.sdk_in_container.build.BuildParams`](flytekit.clis.sdk_in_container.build#flytekitclissdk_in_containerbuildbuildparams) |  |
| [`flytekit.clis.sdk_in_container.build.BuildWorkflowCommand`](flytekit.clis.sdk_in_container.build#flytekitclissdk_in_containerbuildbuildworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`flytekit.clis.sdk_in_container.run.DynamicEntityLaunchCommand`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrundynamicentitylaunchcommand) | This is a dynamic command that is created for each launch plan. |
| [`flytekit.clis.sdk_in_container.run.Entities`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunentities) | NamedTuple to group all entities in a file. |
| [`flytekit.clis.sdk_in_container.run.RemoteEntityGroup`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunremoteentitygroup) | click multicommand that retrieves launchplans from a remote flyte instance and executes them. |
| [`flytekit.clis.sdk_in_container.run.RunCommand`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunruncommand) | A click command group for registering and executing flyte workflows & tasks in a file. |
| [`flytekit.clis.sdk_in_container.run.RunLevelComputedParams`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrunlevelcomputedparams) | This class is used to store the computed parameters that are used to run a workflow / task / launchplan. |
| [`flytekit.clis.sdk_in_container.run.RunLevelParams`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrunlevelparams) | This class is used to store the parameters that are used to run a workflow / task / launchplan. |
| [`flytekit.clis.sdk_in_container.run.WorkflowCommand`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`flytekit.clis.sdk_in_container.run.YamlFileReadingCommand`](flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunyamlfilereadingcommand) |  |
| [`flytekit.clis.sdk_in_container.serialize.SerializationMode`](flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializeserializationmode) |  |
| [`flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand`](flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilserrorhandlingcommand) | Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`flytekit.clis.sdk_in_container.utils.PyFlyteParams`](flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspyflyteparams) |  |
| [`flytekit.configuration.AuthType`](flytekit.configuration#flytekitconfigurationauthtype) |  |
| [`flytekit.configuration.AzureBlobStorageConfig`](flytekit.configuration#flytekitconfigurationazureblobstorageconfig) | Any Azure Blob Storage specific configuration. |
| [`flytekit.configuration.Config`](flytekit.configuration#flytekitconfigurationconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.configuration.DataConfig`](flytekit.configuration#flytekitconfigurationdataconfig) | Any data storage specific configuration. |
| [`flytekit.configuration.EntrypointSettings`](flytekit.configuration#flytekitconfigurationentrypointsettings) | This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`flytekit.configuration.FastSerializationSettings`](flytekit.configuration#flytekitconfigurationfastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.configuration.GCSConfig`](flytekit.configuration#flytekitconfigurationgcsconfig) | Any GCS specific configuration. |
| [`flytekit.configuration.GenericPersistenceConfig`](flytekit.configuration#flytekitconfigurationgenericpersistenceconfig) | Data storage configuration that applies across any provider. |
| [`flytekit.configuration.Image`](flytekit.configuration#flytekitconfigurationimage) | Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.configuration.ImageConfig`](flytekit.configuration#flytekitconfigurationimageconfig) | We recommend you to use ImageConfig. |
| [`flytekit.configuration.LocalConfig`](flytekit.configuration#flytekitconfigurationlocalconfig) | Any configuration specific to local runs. |
| [`flytekit.configuration.PlatformConfig`](flytekit.configuration#flytekitconfigurationplatformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.configuration.S3Config`](flytekit.configuration#flytekitconfigurations3config) | S3 specific configuration. |
| [`flytekit.configuration.SecretsConfig`](flytekit.configuration#flytekitconfigurationsecretsconfig) | Configuration for secrets. |
| [`flytekit.configuration.SerializationSettings`](flytekit.configuration#flytekitconfigurationserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.configuration.StatsConfig`](flytekit.configuration#flytekitconfigurationstatsconfig) | Configuration for sending statsd. |
| [`flytekit.configuration.TaskConfig`](flytekit.configuration#flytekitconfigurationtaskconfig) | Any Project/Domain/Org configuration. |
| [`flytekit.configuration.default_images.DefaultImages`](flytekit.configuration.default_images#flytekitconfigurationdefault_imagesdefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`flytekit.configuration.default_images.PythonVersion`](flytekit.configuration.default_images#flytekitconfigurationdefault_imagespythonversion) |  |
| [`flytekit.configuration.feature_flags.FeatureFlags`](flytekit.configuration.feature_flags#flytekitconfigurationfeature_flagsfeatureflags) |  |
| [`flytekit.configuration.file.ConfigEntry`](flytekit.configuration.file#flytekitconfigurationfileconfigentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`flytekit.configuration.file.ConfigFile`](flytekit.configuration.file#flytekitconfigurationfileconfigfile) |  |
| [`flytekit.configuration.file.LegacyConfigEntry`](flytekit.configuration.file#flytekitconfigurationfilelegacyconfigentry) | Creates a record for the config entry. |
| [`flytekit.configuration.file.YamlConfigEntry`](flytekit.configuration.file#flytekitconfigurationfileyamlconfigentry) | Creates a record for the config entry. |
| [`flytekit.configuration.internal.AWS`](flytekit.configuration.internal#flytekitconfigurationinternalaws) |  |
| [`flytekit.configuration.internal.AZURE`](flytekit.configuration.internal#flytekitconfigurationinternalazure) |  |
| [`flytekit.configuration.internal.Credentials`](flytekit.configuration.internal#flytekitconfigurationinternalcredentials) |  |
| [`flytekit.configuration.internal.GCP`](flytekit.configuration.internal#flytekitconfigurationinternalgcp) |  |
| [`flytekit.configuration.internal.Images`](flytekit.configuration.internal#flytekitconfigurationinternalimages) |  |
| [`flytekit.configuration.internal.Local`](flytekit.configuration.internal#flytekitconfigurationinternallocal) |  |
| [`flytekit.configuration.internal.LocalSDK`](flytekit.configuration.internal#flytekitconfigurationinternallocalsdk) |  |
| [`flytekit.configuration.internal.Persistence`](flytekit.configuration.internal#flytekitconfigurationinternalpersistence) |  |
| [`flytekit.configuration.internal.Platform`](flytekit.configuration.internal#flytekitconfigurationinternalplatform) |  |
| [`flytekit.configuration.internal.Secrets`](flytekit.configuration.internal#flytekitconfigurationinternalsecrets) |  |
| [`flytekit.configuration.internal.StatsD`](flytekit.configuration.internal#flytekitconfigurationinternalstatsd) |  |
| [`flytekit.configuration.plugin.FlytekitPlugin`](flytekit.configuration.plugin#flytekitconfigurationpluginflytekitplugin) |  |
| [`flytekit.constants.CopyFileDetection`](flytekit.constants#flytekitconstantscopyfiledetection) |  |
| [`flytekit.core.annotation.FlyteAnnotation`](flytekit.core.annotation#flytekitcoreannotationflyteannotation) | A core object to add arbitrary annotations to flyte types. |
| [`flytekit.core.array_node.ArrayNode`](flytekit.core.array_node#flytekitcorearray_nodearraynode) |  |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTask`](flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskarraynodemaptask) |  |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTaskResolver`](flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskarraynodemaptaskresolver) | Special resolver that is used for ArrayNodeMapTasks. |
| [`flytekit.core.artifact.Artifact`](flytekit.core.artifact#flytekitcoreartifactartifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.core.artifact.ArtifactIDSpecification`](flytekit.core.artifact#flytekitcoreartifactartifactidspecification) | This is a special object that helps specify how Artifacts are to be created. |
| [`flytekit.core.artifact.ArtifactQuery`](flytekit.core.artifact#flytekitcoreartifactartifactquery) |  |
| [`flytekit.core.artifact.DefaultArtifactSerializationHandler`](flytekit.core.artifact#flytekitcoreartifactdefaultartifactserializationhandler) |  |
| [`flytekit.core.artifact.InputsBase`](flytekit.core.artifact#flytekitcoreartifactinputsbase) | A class to provide better partition semantics. |
| [`flytekit.core.artifact.Partition`](flytekit.core.artifact#flytekitcoreartifactpartition) |  |
| [`flytekit.core.artifact.Partitions`](flytekit.core.artifact#flytekitcoreartifactpartitions) |  |
| [`flytekit.core.artifact.Serializer`](flytekit.core.artifact#flytekitcoreartifactserializer) |  |
| [`flytekit.core.artifact.TimePartition`](flytekit.core.artifact#flytekitcoreartifacttimepartition) |  |
| [`flytekit.core.base_sql_task.SQLTask`](flytekit.core.base_sql_task#flytekitcorebase_sql_tasksqltask) | Base task types for all SQL tasks. |
| [`flytekit.core.base_task.IgnoreOutputs`](flytekit.core.base_task#flytekitcorebase_taskignoreoutputs) | This exception should be used to indicate that the outputs generated by this can be safely ignored. |
| [`flytekit.core.base_task.PythonTask`](flytekit.core.base_task#flytekitcorebase_taskpythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.base_task.Task`](flytekit.core.base_task#flytekitcorebase_tasktask) | The base of all Tasks in flytekit. |
| [`flytekit.core.base_task.TaskMetadata`](flytekit.core.base_task#flytekitcorebase_tasktaskmetadata) | Metadata for a Task. |
| [`flytekit.core.base_task.TaskResolverMixin`](flytekit.core.base_task#flytekitcorebase_tasktaskresolvermixin) | Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.cache.Cache`](flytekit.core.cache#flytekitcorecachecache) | Cache configuration for a task. |
| [`flytekit.core.cache.VersionParameters`](flytekit.core.cache#flytekitcorecacheversionparameters) | Parameters used for version hash generation. |
| [`flytekit.core.checkpointer.Checkpoint`](flytekit.core.checkpointer#flytekitcorecheckpointercheckpoint) | Base class for Checkpoint system. |
| [`flytekit.core.checkpointer.SyncCheckpoint`](flytekit.core.checkpointer#flytekitcorecheckpointersynccheckpoint) | This class is NOT THREAD-SAFE!. |
| [`flytekit.core.class_based_resolver.ClassStorageTaskResolver`](flytekit.core.class_based_resolver#flytekitcoreclass_based_resolverclassstoragetaskresolver) | Stores tasks inside a class variable. |
| [`flytekit.core.condition.BranchNode`](flytekit.core.condition#flytekitcoreconditionbranchnode) |  |
| [`flytekit.core.condition.Case`](flytekit.core.condition#flytekitcoreconditioncase) |  |
| [`flytekit.core.condition.Condition`](flytekit.core.condition#flytekitcoreconditioncondition) |  |
| [`flytekit.core.condition.ConditionalSection`](flytekit.core.condition#flytekitcoreconditionconditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.condition.LocalExecutedConditionalSection`](flytekit.core.condition#flytekitcoreconditionlocalexecutedconditionalsection) |  |
| [`flytekit.core.condition.SkippedConditionalSection`](flytekit.core.condition#flytekitcoreconditionskippedconditionalsection) | This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |
| [`flytekit.core.container_task.ContainerTask`](flytekit.core.container_task#flytekitcorecontainer_taskcontainertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flytekit.core.context_manager.BranchEvalMode`](flytekit.core.context_manager#flytekitcorecontext_managerbranchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.core.context_manager.CompilationState`](flytekit.core.context_manager#flytekitcorecontext_managercompilationstate) | Compilation state is used during the compilation of a workflow or task. |
| [`flytekit.core.context_manager.ExecutionParameters`](flytekit.core.context_manager#flytekitcorecontext_managerexecutionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.context_manager.ExecutionState`](flytekit.core.context_manager#flytekitcorecontext_managerexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.context_manager.FlyteContext`](flytekit.core.context_manager#flytekitcorecontext_managerflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.context_manager.FlyteContextManager`](flytekit.core.context_manager#flytekitcorecontext_managerflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.context_manager.FlyteEntities`](flytekit.core.context_manager#flytekitcorecontext_managerflyteentities) | This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.context_manager.OutputMetadata`](flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadata) |  |
| [`flytekit.core.context_manager.OutputMetadataTracker`](flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadatatracker) | This class is for the users to set arbitrary metadata on output literals. |
| [`flytekit.core.context_manager.SecretsManager`](flytekit.core.context_manager#flytekitcorecontext_managersecretsmanager) | This provides a secrets resolution logic at runtime. |
| [`flytekit.core.data_persistence.FileAccessProvider`](flytekit.core.data_persistence#flytekitcoredata_persistencefileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.core.docstring.Docstring`](flytekit.core.docstring#flytekitcoredocstringdocstring) |  |
| [`flytekit.core.environment.Environment`](flytekit.core.environment#flytekitcoreenvironmentenvironment) |  |
| [`flytekit.core.gate.Gate`](flytekit.core.gate#flytekitcoregategate) | A node type that waits for user input before proceeding with a workflow. |
| [`flytekit.core.hash.HashMethod`](flytekit.core.hash#flytekitcorehashhashmethod) | Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.core.hash.HashOnReferenceMixin`](flytekit.core.hash#flytekitcorehashhashonreferencemixin) |  |
| [`flytekit.core.interface.Interface`](flytekit.core.interface#flytekitcoreinterfaceinterface) | A Python native interface object, like inspect. |
| [`flytekit.core.launch_plan.LaunchPlan`](flytekit.core.launch_plan#flytekitcorelaunch_planlaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.launch_plan.ReferenceLaunchPlan`](flytekit.core.launch_plan#flytekitcorelaunch_planreferencelaunchplan) | A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.core.legacy_map_task.MapPythonTask`](flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmappythontask) | A MapPythonTask defines a {{< py_class_ref flytekit.PythonTask >}} which specifies how to run. |
| [`flytekit.core.legacy_map_task.MapTaskResolver`](flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmaptaskresolver) | Special resolver that is used for MapTasks. |
| [`flytekit.core.local_cache.LocalTaskCache`](flytekit.core.local_cache#flytekitcorelocal_cachelocaltaskcache) | This class implements a persistent store able to cache the result of local task executions. |
| [`flytekit.core.local_fsspec.FlyteLocalFileSystem`](flytekit.core.local_fsspec#flytekitcorelocal_fsspecflytelocalfilesystem) | This class doesn't do anything except override the separator so that it works on windows. |
| [`flytekit.core.mock_stats.MockStats`](flytekit.core.mock_stats#flytekitcoremock_statsmockstats) |  |
| [`flytekit.core.node.Node`](flytekit.core.node#flytekitcorenodenode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.notification.Email`](flytekit.core.notification#flytekitcorenotificationemail) | This notification should be used when sending regular emails to people. |
| [`flytekit.core.notification.Notification`](flytekit.core.notification#flytekitcorenotificationnotification) |  |
| [`flytekit.core.notification.PagerDuty`](flytekit.core.notification#flytekitcorenotificationpagerduty) | This notification should be used when sending emails to the PagerDuty service. |
| [`flytekit.core.notification.Slack`](flytekit.core.notification#flytekitcorenotificationslack) | This notification should be used when sending emails to the Slack. |
| [`flytekit.core.options.Options`](flytekit.core.options#flytekitcoreoptionsoptions) | These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.core.pod_template.PodTemplate`](flytekit.core.pod_template#flytekitcorepod_templatepodtemplate) | Custom PodTemplate specification for a Task. |
| [`flytekit.core.promise.ComparisonExpression`](flytekit.core.promise#flytekitcorepromisecomparisonexpression) | ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`flytekit.core.promise.ComparisonOps`](flytekit.core.promise#flytekitcorepromisecomparisonops) |  |
| [`flytekit.core.promise.ConjunctionExpression`](flytekit.core.promise#flytekitcorepromiseconjunctionexpression) | A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`flytekit.core.promise.ConjunctionOps`](flytekit.core.promise#flytekitcorepromiseconjunctionops) |  |
| [`flytekit.core.promise.NodeOutput`](flytekit.core.promise#flytekitcorepromisenodeoutput) |  |
| [`flytekit.core.promise.Promise`](flytekit.core.promise#flytekitcorepromisepromise) | This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.promise.VoidPromise`](flytekit.core.promise#flytekitcorepromisevoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.python_auto_container.DefaultNotebookTaskResolver`](flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaultnotebooktaskresolver) | This resolved is used when the task is defined in a notebook. |
| [`flytekit.core.python_auto_container.DefaultTaskResolver`](flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaulttaskresolver) | Please see the notes in the TaskResolverMixin as it describes this default behavior. |
| [`flytekit.core.python_auto_container.PickledEntity`](flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentity) | Represents the structure of the pickled object stored in the. |
| [`flytekit.core.python_auto_container.PickledEntityMetadata`](flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentitymetadata) | Metadata for a pickled entity containing version information. |
| [`flytekit.core.python_auto_container.PythonAutoContainerTask`](flytekit.core.python_auto_container#flytekitcorepython_auto_containerpythonautocontainertask) | A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_customized_container_task.PythonCustomizedContainerTask`](flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskpythoncustomizedcontainertask) | Please take a look at the comments for {{< py_class_ref flytekit.extend.ExecutableTemplateShimTask >}} as well. |
| [`flytekit.core.python_customized_container_task.TaskTemplateResolver`](flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktasktemplateresolver) | This is a special resolver that resolves the task above at execution time, using only the ``TaskTemplate``,. |
| [`flytekit.core.python_function_task.AsyncPythonFunctionTask`](flytekit.core.python_function_task#flytekitcorepython_function_taskasyncpythonfunctiontask) | This is the base task for eager tasks, as well as normal async tasks. |
| [`flytekit.core.python_function_task.EagerAsyncPythonFunctionTask`](flytekit.core.python_function_task#flytekitcorepython_function_taskeagerasyncpythonfunctiontask) | This is the base eager task (aka eager workflow) type. |
| [`flytekit.core.python_function_task.EagerFailureHandlerTask`](flytekit.core.python_function_task#flytekitcorepython_function_taskeagerfailurehandlertask) |  |
| [`flytekit.core.python_function_task.EagerFailureTaskResolver`](flytekit.core.python_function_task#flytekitcorepython_function_taskeagerfailuretaskresolver) |  |
| [`flytekit.core.python_function_task.PythonFunctionTask`](flytekit.core.python_function_task#flytekitcorepython_function_taskpythonfunctiontask) | A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.python_function_task.PythonInstanceTask`](flytekit.core.python_function_task#flytekitcorepython_function_taskpythoninstancetask) | This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.core.reference_entity.LaunchPlanReference`](flytekit.core.reference_entity#flytekitcorereference_entitylaunchplanreference) | A reference object containing metadata that points to a remote launch plan. |
| [`flytekit.core.reference_entity.Reference`](flytekit.core.reference_entity#flytekitcorereference_entityreference) |  |
| [`flytekit.core.reference_entity.ReferenceEntity`](flytekit.core.reference_entity#flytekitcorereference_entityreferenceentity) |  |
| [`flytekit.core.reference_entity.ReferenceSpec`](flytekit.core.reference_entity#flytekitcorereference_entityreferencespec) |  |
| [`flytekit.core.reference_entity.ReferenceTemplate`](flytekit.core.reference_entity#flytekitcorereference_entityreferencetemplate) |  |
| [`flytekit.core.reference_entity.TaskReference`](flytekit.core.reference_entity#flytekitcorereference_entitytaskreference) | A reference object containing metadata that points to a remote task. |
| [`flytekit.core.reference_entity.WorkflowReference`](flytekit.core.reference_entity#flytekitcorereference_entityworkflowreference) | A reference object containing metadata that points to a remote workflow. |
| [`flytekit.core.resources.ResourceSpec`](flytekit.core.resources#flytekitcoreresourcesresourcespec) |  |
| [`flytekit.core.resources.Resources`](flytekit.core.resources#flytekitcoreresourcesresources) | This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.schedule.CronSchedule`](flytekit.core.schedule#flytekitcoreschedulecronschedule) | Use this when you have a launch plan that you want to run on a cron expression. |
| [`flytekit.core.schedule.FixedRate`](flytekit.core.schedule#flytekitcoreschedulefixedrate) | Use this class to schedule a fixed-rate interval for a launch plan. |
| [`flytekit.core.schedule.OnSchedule`](flytekit.core.schedule#flytekitcorescheduleonschedule) |  |
| [`flytekit.core.shim_task.ExecutableTemplateShimTask`](flytekit.core.shim_task#flytekitcoreshim_taskexecutabletemplateshimtask) | The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`flytekit.core.shim_task.ShimTaskExecutor`](flytekit.core.shim_task#flytekitcoreshim_taskshimtaskexecutor) |  |
| [`flytekit.core.task.Echo`](flytekit.core.task#flytekitcoretaskecho) |  |
| [`flytekit.core.task.ReferenceTask`](flytekit.core.task#flytekitcoretaskreferencetask) | This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.task.TaskPlugins`](flytekit.core.task#flytekitcoretasktaskplugins) | This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |
| [`flytekit.core.tracked_abc.FlyteTrackedABC`](flytekit.core.tracked_abc#flytekitcoretracked_abcflytetrackedabc) | This class exists because if you try to inherit from abc. |
| [`flytekit.core.tracker.InstanceTrackingMeta`](flytekit.core.tracker#flytekitcoretrackerinstancetrackingmeta) | Please see the original class :flytekit. |
| [`flytekit.core.tracker.TrackedInstance`](flytekit.core.tracker#flytekitcoretrackertrackedinstance) | Please see the notes for the metaclass above first. |
| [`flytekit.core.type_engine.AsyncTypeTransformer`](flytekit.core.type_engine#flytekitcoretype_engineasynctypetransformer) |  |
| [`flytekit.core.type_engine.BatchSize`](flytekit.core.type_engine#flytekitcoretype_enginebatchsize) | This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`flytekit.core.type_engine.BinaryIOTransformer`](flytekit.core.type_engine#flytekitcoretype_enginebinaryiotransformer) | Handler for BinaryIO. |
| [`flytekit.core.type_engine.DataclassTransformer`](flytekit.core.type_engine#flytekitcoretype_enginedataclasstransformer) | The Dataclass Transformer provides a type transformer for dataclasses. |
| [`flytekit.core.type_engine.DictTransformer`](flytekit.core.type_engine#flytekitcoretype_enginedicttransformer) | Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`flytekit.core.type_engine.EnumTransformer`](flytekit.core.type_engine#flytekitcoretype_engineenumtransformer) | Enables converting a python type enum. |
| [`flytekit.core.type_engine.ListTransformer`](flytekit.core.type_engine#flytekitcoretype_enginelisttransformer) | Transformer that handles a univariate typing. |
| [`flytekit.core.type_engine.LiteralTypeTransformer`](flytekit.core.type_engine#flytekitcoretype_engineliteraltypetransformer) |  |
| [`flytekit.core.type_engine.LiteralsResolver`](flytekit.core.type_engine#flytekitcoretype_engineliteralsresolver) | LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.core.type_engine.ProtobufTransformer`](flytekit.core.type_engine#flytekitcoretype_engineprotobuftransformer) |  |
| [`flytekit.core.type_engine.RestrictedTypeError`](flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypeerror) |  |
| [`flytekit.core.type_engine.RestrictedTypeTransformer`](flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypetransformer) | Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. |
| [`flytekit.core.type_engine.SimpleTransformer`](flytekit.core.type_engine#flytekitcoretype_enginesimpletransformer) | A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate. |
| [`flytekit.core.type_engine.TextIOTransformer`](flytekit.core.type_engine#flytekitcoretype_enginetextiotransformer) | Handler for TextIO. |
| [`flytekit.core.type_engine.TypeEngine`](flytekit.core.type_engine#flytekitcoretype_enginetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.type_engine.TypeTransformer`](flytekit.core.type_engine#flytekitcoretype_enginetypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.TypeTransformerFailedError`](flytekit.core.type_engine#flytekitcoretype_enginetypetransformerfailederror) |  |
| [`flytekit.core.type_engine.UnionTransformer`](flytekit.core.type_engine#flytekitcoretype_engineuniontransformer) | Transformer that handles a typing. |
| [`flytekit.core.utils.AutoDeletingTempDir`](flytekit.core.utils#flytekitcoreutilsautodeletingtempdir) | Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`flytekit.core.utils.ClassDecorator`](flytekit.core.utils#flytekitcoreutilsclassdecorator) | Abstract class for class decorators. |
| [`flytekit.core.utils.Directory`](flytekit.core.utils#flytekitcoreutilsdirectory) |  |
| [`flytekit.core.utils.timeit`](flytekit.core.utils#flytekitcoreutilstimeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.worker_queue.Controller`](flytekit.core.worker_queue#flytekitcoreworker_queuecontroller) | This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint. |
| [`flytekit.core.worker_queue.ItemStatus`](flytekit.core.worker_queue#flytekitcoreworker_queueitemstatus) |  |
| [`flytekit.core.worker_queue.Update`](flytekit.core.worker_queue#flytekitcoreworker_queueupdate) |  |
| [`flytekit.core.worker_queue.WorkItem`](flytekit.core.worker_queue#flytekitcoreworker_queueworkitem) | This is a class to keep track of what the user requested. |
| [`flytekit.core.workflow.ImperativeWorkflow`](flytekit.core.workflow#flytekitcoreworkflowimperativeworkflow) | An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`flytekit.core.workflow.PythonFunctionWorkflow`](flytekit.core.workflow#flytekitcoreworkflowpythonfunctionworkflow) | Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`flytekit.core.workflow.ReferenceWorkflow`](flytekit.core.workflow#flytekitcoreworkflowreferenceworkflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.core.workflow.WorkflowBase`](flytekit.core.workflow#flytekitcoreworkflowworkflowbase) |  |
| [`flytekit.core.workflow.WorkflowFailurePolicy`](flytekit.core.workflow#flytekitcoreworkflowworkflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.core.workflow.WorkflowMetadata`](flytekit.core.workflow#flytekitcoreworkflowworkflowmetadata) |  |
| [`flytekit.core.workflow.WorkflowMetadataDefaults`](flytekit.core.workflow#flytekitcoreworkflowworkflowmetadatadefaults) | This class is similarly named to the one above. |
| [`flytekit.deck.deck.Deck`](flytekit.deck.deck#flytekitdeckdeckdeck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.deck.deck.DeckField`](flytekit.deck.deck#flytekitdeckdeckdeckfield) | DeckField is used to specify the fields that will be rendered in the deck. |
| [`flytekit.deck.deck.TimeLineDeck`](flytekit.deck.deck#flytekitdeckdecktimelinedeck) | The TimeLineDeck class is designed to render the execution time of each part of a task. |
| [`flytekit.deck.renderer.ArrowRenderer`](flytekit.deck.renderer#flytekitdeckrendererarrowrenderer) | Render an Arrow dataframe as an HTML table. |
| [`flytekit.deck.renderer.MarkdownRenderer`](flytekit.deck.renderer#flytekitdeckrenderermarkdownrenderer) | Convert a markdown string to HTML and return HTML as a unicode string. |
| [`flytekit.deck.renderer.PythonDependencyRenderer`](flytekit.deck.renderer#flytekitdeckrendererpythondependencyrenderer) | PythonDependencyDeck is a deck that contains information about packages installed via pip. |
| [`flytekit.deck.renderer.SourceCodeRenderer`](flytekit.deck.renderer#flytekitdeckrenderersourcecoderenderer) | Convert Python source code to HTML, and return HTML as a unicode string. |
| [`flytekit.deck.renderer.TopFrameRenderer`](flytekit.deck.renderer#flytekitdeckrenderertopframerenderer) | Render a DataFrame as an HTML table. |
| [`flytekit.exceptions.base.FlyteException`](flytekit.exceptions.base#flytekitexceptionsbaseflyteexception) |  |
| [`flytekit.exceptions.base.FlyteRecoverableException`](flytekit.exceptions.base#flytekitexceptionsbaseflyterecoverableexception) |  |
| [`flytekit.exceptions.eager.EagerException`](flytekit.exceptions.eager#flytekitexceptionseagereagerexception) | Raised when a node in an eager workflow encounters an error. |
| [`flytekit.exceptions.scopes.FlyteScopedException`](flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedexception) |  |
| [`flytekit.exceptions.scopes.FlyteScopedSystemException`](flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedsystemexception) |  |
| [`flytekit.exceptions.scopes.FlyteScopedUserException`](flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopeduserexception) |  |
| [`flytekit.exceptions.system.FlyteAgentNotFound`](flytekit.exceptions.system#flytekitexceptionssystemflyteagentnotfound) |  |
| [`flytekit.exceptions.system.FlyteConnectorNotFound`](flytekit.exceptions.system#flytekitexceptionssystemflyteconnectornotfound) |  |
| [`flytekit.exceptions.system.FlyteDownloadDataException`](flytekit.exceptions.system#flytekitexceptionssystemflytedownloaddataexception) |  |
| [`flytekit.exceptions.system.FlyteEntrypointNotLoadable`](flytekit.exceptions.system#flytekitexceptionssystemflyteentrypointnotloadable) |  |
| [`flytekit.exceptions.system.FlyteNonRecoverableSystemException`](flytekit.exceptions.system#flytekitexceptionssystemflytenonrecoverablesystemexception) |  |
| [`flytekit.exceptions.system.FlyteNotImplementedException`](flytekit.exceptions.system#flytekitexceptionssystemflytenotimplementedexception) |  |
| [`flytekit.exceptions.system.FlyteSystemAssertion`](flytekit.exceptions.system#flytekitexceptionssystemflytesystemassertion) |  |
| [`flytekit.exceptions.system.FlyteSystemException`](flytekit.exceptions.system#flytekitexceptionssystemflytesystemexception) |  |
| [`flytekit.exceptions.system.FlyteSystemUnavailableException`](flytekit.exceptions.system#flytekitexceptionssystemflytesystemunavailableexception) |  |
| [`flytekit.exceptions.system.FlyteUploadDataException`](flytekit.exceptions.system#flytekitexceptionssystemflyteuploaddataexception) |  |
| [`flytekit.exceptions.user.FlyteAssertion`](flytekit.exceptions.user#flytekitexceptionsuserflyteassertion) |  |
| [`flytekit.exceptions.user.FlyteAuthenticationException`](flytekit.exceptions.user#flytekitexceptionsuserflyteauthenticationexception) |  |
| [`flytekit.exceptions.user.FlyteCompilationException`](flytekit.exceptions.user#flytekitexceptionsuserflytecompilationexception) |  |
| [`flytekit.exceptions.user.FlyteDataNotFoundException`](flytekit.exceptions.user#flytekitexceptionsuserflytedatanotfoundexception) |  |
| [`flytekit.exceptions.user.FlyteDisapprovalException`](flytekit.exceptions.user#flytekitexceptionsuserflytedisapprovalexception) |  |
| [`flytekit.exceptions.user.FlyteEntityAlreadyExistsException`](flytekit.exceptions.user#flytekitexceptionsuserflyteentityalreadyexistsexception) |  |
| [`flytekit.exceptions.user.FlyteEntityNotExistException`](flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotexistexception) |  |
| [`flytekit.exceptions.user.FlyteEntityNotFoundException`](flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotfoundexception) |  |
| [`flytekit.exceptions.user.FlyteFailureNodeInputMismatchException`](flytekit.exceptions.user#flytekitexceptionsuserflytefailurenodeinputmismatchexception) |  |
| [`flytekit.exceptions.user.FlyteInvalidInputException`](flytekit.exceptions.user#flytekitexceptionsuserflyteinvalidinputexception) |  |
| [`flytekit.exceptions.user.FlyteMissingReturnValueException`](flytekit.exceptions.user#flytekitexceptionsuserflytemissingreturnvalueexception) |  |
| [`flytekit.exceptions.user.FlyteMissingTypeException`](flytekit.exceptions.user#flytekitexceptionsuserflytemissingtypeexception) |  |
| [`flytekit.exceptions.user.FlytePromiseAttributeResolveException`](flytekit.exceptions.user#flytekitexceptionsuserflytepromiseattributeresolveexception) |  |
| [`flytekit.exceptions.user.FlyteRecoverableException`](flytekit.exceptions.user#flytekitexceptionsuserflyterecoverableexception) |  |
| [`flytekit.exceptions.user.FlyteTimeout`](flytekit.exceptions.user#flytekitexceptionsuserflytetimeout) |  |
| [`flytekit.exceptions.user.FlyteTypeException`](flytekit.exceptions.user#flytekitexceptionsuserflytetypeexception) |  |
| [`flytekit.exceptions.user.FlyteUserException`](flytekit.exceptions.user#flytekitexceptionsuserflyteuserexception) |  |
| [`flytekit.exceptions.user.FlyteUserRuntimeException`](flytekit.exceptions.user#flytekitexceptionsuserflyteuserruntimeexception) |  |
| [`flytekit.exceptions.user.FlyteValidationException`](flytekit.exceptions.user#flytekitexceptionsuserflytevalidationexception) |  |
| [`flytekit.exceptions.user.FlyteValueException`](flytekit.exceptions.user#flytekitexceptionsuserflytevalueexception) |  |
| [`flytekit.extend.backend.base_connector.AsyncConnectorBase`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorbase) | This is the base class for all async connectors. |
| [`flytekit.extend.backend.base_connector.AsyncConnectorExecutorMixin`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorexecutormixin) | This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.ConnectorBase`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorbase) |  |
| [`flytekit.extend.backend.base_connector.ConnectorRegistry`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorregistry) | This is the registry for all connectors. |
| [`flytekit.extend.backend.base_connector.Resource`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresource) | This is the output resource of the job. |
| [`flytekit.extend.backend.base_connector.ResourceMeta`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresourcemeta) | This is the metadata for the job. |
| [`flytekit.extend.backend.base_connector.SyncConnectorBase`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorbase) | This is the base class for all sync connectors. |
| [`flytekit.extend.backend.base_connector.SyncConnectorExecutorMixin`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorexecutormixin) | This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.TaskCategory`](flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortaskcategory) |  |
| [`flytekit.extend.backend.connector_service.AsyncConnectorService`](flytekit.extend.backend.connector_service#flytekitextendbackendconnector_serviceasyncconnectorservice) |  |
| [`flytekit.extend.backend.connector_service.ConnectorMetadataService`](flytekit.extend.backend.connector_service#flytekitextendbackendconnector_serviceconnectormetadataservice) |  |
| [`flytekit.extend.backend.connector_service.SyncConnectorService`](flytekit.extend.backend.connector_service#flytekitextendbackendconnector_servicesyncconnectorservice) |  |
| [`flytekit.extras.accelerators.BaseAccelerator`](flytekit.extras.accelerators#flytekitextrasacceleratorsbaseaccelerator) | Base class for all accelerator types. |
| [`flytekit.extras.accelerators.GPUAccelerator`](flytekit.extras.accelerators#flytekitextrasacceleratorsgpuaccelerator) | Class that represents a GPU accelerator. |
| [`flytekit.extras.accelerators.MultiInstanceGPUAccelerator`](flytekit.extras.accelerators#flytekitextrasacceleratorsmultiinstancegpuaccelerator) | Base class for all multi-instance GPU accelerator types. |
| [`flytekit.extras.cloud_pickle_resolver.ExperimentalNaiveCloudPickleResolver`](flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolverexperimentalnaivecloudpickleresolver) | Please do not use this resolver, basically ever. |
| [`flytekit.extras.pydantic_transformer.transformer.PydanticTransformer`](flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerpydantictransformer) |  |
| [`flytekit.extras.sklearn.native.SklearnEstimatorTransformer`](flytekit.extras.sklearn.native#flytekitextrassklearnnativesklearnestimatortransformer) |  |
| [`flytekit.extras.sklearn.native.SklearnTypeTransformer`](flytekit.extras.sklearn.native#flytekitextrassklearnnativesklearntypetransformer) |  |
| [`flytekit.extras.sqlite3.task.SQLite3Config`](flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3config) | Use this configuration to configure if sqlite3 files that should be loaded by the task. |
| [`flytekit.extras.sqlite3.task.SQLite3Task`](flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3task) | Run client side SQLite3 queries that optionally return a FlyteSchema object. |
| [`flytekit.extras.sqlite3.task.SQLite3TaskExecutor`](flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3taskexecutor) |  |
| [`flytekit.extras.tasks.shell.AttrDict`](flytekit.extras.tasks.shell#flytekitextrastasksshellattrdict) | Convert a dictionary to an attribute style lookup. |
| [`flytekit.extras.tasks.shell.OutputLocation`](flytekit.extras.tasks.shell#flytekitextrastasksshelloutputlocation) |  |
| [`flytekit.extras.tasks.shell.ProcessResult`](flytekit.extras.tasks.shell#flytekitextrastasksshellprocessresult) | Stores a process return code, standard output and standard error. |
| [`flytekit.extras.tasks.shell.RawShellTask`](flytekit.extras.tasks.shell#flytekitextrastasksshellrawshelltask) |  |
| [`flytekit.extras.tasks.shell.ShellTask`](flytekit.extras.tasks.shell#flytekitextrastasksshellshelltask) |  |
| [`flytekit.extras.webhook.WebhookConnector`](flytekit.extras.webhook#flytekitextraswebhookwebhookconnector) | WebhookConnector is responsible for handling webhook tasks. |
| [`flytekit.extras.webhook.WebhookTask`](flytekit.extras.webhook#flytekitextraswebhookwebhooktask) | The WebhookTask is used to invoke a webhook. |
| [`flytekit.extras.webhook.connector.WebhookConnector`](flytekit.extras.webhook.connector#flytekitextraswebhookconnectorwebhookconnector) | WebhookConnector is responsible for handling webhook tasks. |
| [`flytekit.extras.webhook.task.WebhookTask`](flytekit.extras.webhook.task#flytekitextraswebhooktaskwebhooktask) | The WebhookTask is used to invoke a webhook. |
| [`flytekit.image_spec.default_builder.DefaultImageBuilder`](flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdefaultimagebuilder) | Image builder using Docker and buildkit. |
| [`flytekit.image_spec.image_spec.ImageBuildEngine`](flytekit.image_spec.image_spec#flytekitimage_specimage_specimagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.image_spec.image_spec.ImageSpec`](flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.image_spec.image_spec.ImageSpecBuilder`](flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespecbuilder) |  |
| [`flytekit.image_spec.noop_builder.NoOpBuilder`](flytekit.image_spec.noop_builder#flytekitimage_specnoop_buildernoopbuilder) | Noop image builder. |
| [`flytekit.interaction.click_types.DateTimeType`](flytekit.interaction.click_types#flytekitinteractionclick_typesdatetimetype) |  |
| [`flytekit.interaction.click_types.DirParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesdirparamtype) |  |
| [`flytekit.interaction.click_types.DurationParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesdurationparamtype) |  |
| [`flytekit.interaction.click_types.EnumParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesenumparamtype) |  |
| [`flytekit.interaction.click_types.FileParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesfileparamtype) |  |
| [`flytekit.interaction.click_types.FlyteLiteralConverter`](flytekit.interaction.click_types#flytekitinteractionclick_typesflyteliteralconverter) |  |
| [`flytekit.interaction.click_types.JSONIteratorParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratorparamtype) |  |
| [`flytekit.interaction.click_types.JsonParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesjsonparamtype) |  |
| [`flytekit.interaction.click_types.PickleParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typespickleparamtype) |  |
| [`flytekit.interaction.click_types.StructuredDatasetParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddatasetparamtype) | TODO handle column types. |
| [`flytekit.interaction.click_types.UnionParamType`](flytekit.interaction.click_types#flytekitinteractionclick_typesunionparamtype) | A composite type that allows for multiple types to be specified. |
| [`flytekit.interaction.rich_utils.RichCallback`](flytekit.interaction.rich_utils#flytekitinteractionrich_utilsrichcallback) |  |
| [`flytekit.interactive.vscode_lib.config.VscodeConfig`](flytekit.interactive.vscode_lib.config#flytekitinteractivevscode_libconfigvscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`flytekit.interactive.vscode_lib.decorator.vscode`](flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscode) |  |
| [`flytekit.interfaces.cli_identifiers.Identifier`](flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersidentifier) |  |
| [`flytekit.interfaces.cli_identifiers.TaskExecutionIdentifier`](flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifierstaskexecutionidentifier) |  |
| [`flytekit.interfaces.cli_identifiers.WorkflowExecutionIdentifier`](flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersworkflowexecutionidentifier) |  |
| [`flytekit.interfaces.stats.client.DummyStatsClient`](flytekit.interfaces.stats.client#flytekitinterfacesstatsclientdummystatsclient) | A dummy client for statsd. |
| [`flytekit.interfaces.stats.client.ScopeableStatsProxy`](flytekit.interfaces.stats.client#flytekitinterfacesstatsclientscopeablestatsproxy) | A Proxy object for an underlying statsd client. |
| [`flytekit.interfaces.stats.client.StatsClientProxy`](flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsclientproxy) |  |
| [`flytekit.interfaces.stats.taggable.TaggableStats`](flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggabletaggablestats) |  |
| [`flytekit.models.admin.common.Sort`](flytekit.models.admin.common#flytekitmodelsadmincommonsort) |  |
| [`flytekit.models.admin.task_execution.TaskExecution`](flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecution) |  |
| [`flytekit.models.admin.task_execution.TaskExecutionClosure`](flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecutionclosure) |  |
| [`flytekit.models.admin.workflow.Workflow`](flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflow) |  |
| [`flytekit.models.admin.workflow.WorkflowClosure`](flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowclosure) |  |
| [`flytekit.models.admin.workflow.WorkflowSpec`](flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowspec) |  |
| [`flytekit.models.annotation.TypeAnnotation`](flytekit.models.annotation#flytekitmodelsannotationtypeannotation) | Python class representation of the flyteidl TypeAnnotation message. |
| [`flytekit.models.array_job.ArrayJob`](flytekit.models.array_job#flytekitmodelsarray_jobarrayjob) |  |
| [`flytekit.models.common.Annotations`](flytekit.models.common#flytekitmodelscommonannotations) |  |
| [`flytekit.models.common.AuthRole`](flytekit.models.common#flytekitmodelscommonauthrole) |  |
| [`flytekit.models.common.EmailNotification`](flytekit.models.common#flytekitmodelscommonemailnotification) |  |
| [`flytekit.models.common.Envs`](flytekit.models.common#flytekitmodelscommonenvs) |  |
| [`flytekit.models.common.FlyteABCMeta`](flytekit.models.common#flytekitmodelscommonflyteabcmeta) |  |
| [`flytekit.models.common.FlyteCustomIdlEntity`](flytekit.models.common#flytekitmodelscommonflytecustomidlentity) |  |
| [`flytekit.models.common.FlyteIdlEntity`](flytekit.models.common#flytekitmodelscommonflyteidlentity) |  |
| [`flytekit.models.common.FlyteType`](flytekit.models.common#flytekitmodelscommonflytetype) |  |
| [`flytekit.models.common.Labels`](flytekit.models.common#flytekitmodelscommonlabels) |  |
| [`flytekit.models.common.NamedEntityIdentifier`](flytekit.models.common#flytekitmodelscommonnamedentityidentifier) |  |
| [`flytekit.models.common.Notification`](flytekit.models.common#flytekitmodelscommonnotification) |  |
| [`flytekit.models.common.PagerDutyNotification`](flytekit.models.common#flytekitmodelscommonpagerdutynotification) |  |
| [`flytekit.models.common.RawOutputDataConfig`](flytekit.models.common#flytekitmodelscommonrawoutputdataconfig) |  |
| [`flytekit.models.common.SlackNotification`](flytekit.models.common#flytekitmodelscommonslacknotification) |  |
| [`flytekit.models.common.UrlBlob`](flytekit.models.common#flytekitmodelscommonurlblob) |  |
| [`flytekit.models.concurrency.ConcurrencyLimitBehavior`](flytekit.models.concurrency#flytekitmodelsconcurrencyconcurrencylimitbehavior) |  |
| [`flytekit.models.concurrency.ConcurrencyPolicy`](flytekit.models.concurrency#flytekitmodelsconcurrencyconcurrencypolicy) | Defines the concurrency policy for a launch plan. |
| [`flytekit.models.core.catalog.CatalogArtifactTag`](flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogartifacttag) |  |
| [`flytekit.models.core.catalog.CatalogMetadata`](flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogmetadata) |  |
| [`flytekit.models.core.compiler.CompiledTask`](flytekit.models.core.compiler#flytekitmodelscorecompilercompiledtask) |  |
| [`flytekit.models.core.compiler.CompiledWorkflow`](flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflow) |  |
| [`flytekit.models.core.compiler.CompiledWorkflowClosure`](flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflowclosure) |  |
| [`flytekit.models.core.compiler.ConnectionSet`](flytekit.models.core.compiler#flytekitmodelscorecompilerconnectionset) |  |
| [`flytekit.models.core.condition.BooleanExpression`](flytekit.models.core.condition#flytekitmodelscoreconditionbooleanexpression) |  |
| [`flytekit.models.core.condition.ComparisonExpression`](flytekit.models.core.condition#flytekitmodelscoreconditioncomparisonexpression) |  |
| [`flytekit.models.core.condition.ConjunctionExpression`](flytekit.models.core.condition#flytekitmodelscoreconditionconjunctionexpression) |  |
| [`flytekit.models.core.condition.Operand`](flytekit.models.core.condition#flytekitmodelscoreconditionoperand) |  |
| [`flytekit.models.core.errors.ContainerError`](flytekit.models.core.errors#flytekitmodelscoreerrorscontainererror) |  |
| [`flytekit.models.core.errors.ErrorDocument`](flytekit.models.core.errors#flytekitmodelscoreerrorserrordocument) |  |
| [`flytekit.models.core.execution.ExecutionError`](flytekit.models.core.execution#flytekitmodelscoreexecutionexecutionerror) |  |
| [`flytekit.models.core.execution.NodeExecutionPhase`](flytekit.models.core.execution#flytekitmodelscoreexecutionnodeexecutionphase) |  |
| [`flytekit.models.core.execution.TaskExecutionPhase`](flytekit.models.core.execution#flytekitmodelscoreexecutiontaskexecutionphase) |  |
| [`flytekit.models.core.execution.TaskLog`](flytekit.models.core.execution#flytekitmodelscoreexecutiontasklog) |  |
| [`flytekit.models.core.execution.WorkflowExecutionPhase`](flytekit.models.core.execution#flytekitmodelscoreexecutionworkflowexecutionphase) | This class holds enum values used for setting notifications. |
| [`flytekit.models.core.identifier.Identifier`](flytekit.models.core.identifier#flytekitmodelscoreidentifieridentifier) |  |
| [`flytekit.models.core.identifier.NodeExecutionIdentifier`](flytekit.models.core.identifier#flytekitmodelscoreidentifiernodeexecutionidentifier) |  |
| [`flytekit.models.core.identifier.ResourceType`](flytekit.models.core.identifier#flytekitmodelscoreidentifierresourcetype) |  |
| [`flytekit.models.core.identifier.SignalIdentifier`](flytekit.models.core.identifier#flytekitmodelscoreidentifiersignalidentifier) |  |
| [`flytekit.models.core.identifier.TaskExecutionIdentifier`](flytekit.models.core.identifier#flytekitmodelscoreidentifiertaskexecutionidentifier) |  |
| [`flytekit.models.core.identifier.WorkflowExecutionIdentifier`](flytekit.models.core.identifier#flytekitmodelscoreidentifierworkflowexecutionidentifier) |  |
| [`flytekit.models.core.types.BlobType`](flytekit.models.core.types#flytekitmodelscoretypesblobtype) | This type represents offloaded data and is typically used for things like files. |
| [`flytekit.models.core.types.EnumType`](flytekit.models.core.types#flytekitmodelscoretypesenumtype) | Models _types_pb2. |
| [`flytekit.models.core.workflow.Alias`](flytekit.models.core.workflow#flytekitmodelscoreworkflowalias) |  |
| [`flytekit.models.core.workflow.ApproveCondition`](flytekit.models.core.workflow#flytekitmodelscoreworkflowapprovecondition) |  |
| [`flytekit.models.core.workflow.ArrayNode`](flytekit.models.core.workflow#flytekitmodelscoreworkflowarraynode) |  |
| [`flytekit.models.core.workflow.BranchNode`](flytekit.models.core.workflow#flytekitmodelscoreworkflowbranchnode) |  |
| [`flytekit.models.core.workflow.GateNode`](flytekit.models.core.workflow#flytekitmodelscoreworkflowgatenode) |  |
| [`flytekit.models.core.workflow.IfBlock`](flytekit.models.core.workflow#flytekitmodelscoreworkflowifblock) |  |
| [`flytekit.models.core.workflow.IfElseBlock`](flytekit.models.core.workflow#flytekitmodelscoreworkflowifelseblock) |  |
| [`flytekit.models.core.workflow.Node`](flytekit.models.core.workflow#flytekitmodelscoreworkflownode) |  |
| [`flytekit.models.core.workflow.NodeMetadata`](flytekit.models.core.workflow#flytekitmodelscoreworkflownodemetadata) |  |
| [`flytekit.models.core.workflow.SignalCondition`](flytekit.models.core.workflow#flytekitmodelscoreworkflowsignalcondition) |  |
| [`flytekit.models.core.workflow.SleepCondition`](flytekit.models.core.workflow#flytekitmodelscoreworkflowsleepcondition) |  |
| [`flytekit.models.core.workflow.TaskNode`](flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknode) |  |
| [`flytekit.models.core.workflow.TaskNodeOverrides`](flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknodeoverrides) |  |
| [`flytekit.models.core.workflow.WorkflowMetadata`](flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadata) |  |
| [`flytekit.models.core.workflow.WorkflowMetadataDefaults`](flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadatadefaults) |  |
| [`flytekit.models.core.workflow.WorkflowNode`](flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflownode) |  |
| [`flytekit.models.core.workflow.WorkflowTemplate`](flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowtemplate) |  |
| [`flytekit.models.documentation.Description`](flytekit.models.documentation#flytekitmodelsdocumentationdescription) | Full user description with formatting preserved. |
| [`flytekit.models.documentation.Documentation`](flytekit.models.documentation#flytekitmodelsdocumentationdocumentation) | DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.models.documentation.SourceCode`](flytekit.models.documentation#flytekitmodelsdocumentationsourcecode) | Link to source code used to define this task or workflow. |
| [`flytekit.models.domain.Domain`](flytekit.models.domain#flytekitmodelsdomaindomain) | Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |
| [`flytekit.models.dynamic_job.DynamicJobSpec`](flytekit.models.dynamic_job#flytekitmodelsdynamic_jobdynamicjobspec) |  |
| [`flytekit.models.event.TaskExecutionMetadata`](flytekit.models.event#flytekitmodelseventtaskexecutionmetadata) |  |
| [`flytekit.models.execution.AbortMetadata`](flytekit.models.execution#flytekitmodelsexecutionabortmetadata) |  |
| [`flytekit.models.execution.ClusterAssignment`](flytekit.models.execution#flytekitmodelsexecutionclusterassignment) |  |
| [`flytekit.models.execution.Execution`](flytekit.models.execution#flytekitmodelsexecutionexecution) |  |
| [`flytekit.models.execution.ExecutionClosure`](flytekit.models.execution#flytekitmodelsexecutionexecutionclosure) |  |
| [`flytekit.models.execution.ExecutionMetadata`](flytekit.models.execution#flytekitmodelsexecutionexecutionmetadata) |  |
| [`flytekit.models.execution.ExecutionSpec`](flytekit.models.execution#flytekitmodelsexecutionexecutionspec) |  |
| [`flytekit.models.execution.LiteralMapBlob`](flytekit.models.execution#flytekitmodelsexecutionliteralmapblob) |  |
| [`flytekit.models.execution.NodeExecutionGetDataResponse`](flytekit.models.execution#flytekitmodelsexecutionnodeexecutiongetdataresponse) |  |
| [`flytekit.models.execution.NotificationList`](flytekit.models.execution#flytekitmodelsexecutionnotificationlist) |  |
| [`flytekit.models.execution.SystemMetadata`](flytekit.models.execution#flytekitmodelsexecutionsystemmetadata) |  |
| [`flytekit.models.execution.TaskExecutionGetDataResponse`](flytekit.models.execution#flytekitmodelsexecutiontaskexecutiongetdataresponse) |  |
| [`flytekit.models.execution.WorkflowExecutionGetDataResponse`](flytekit.models.execution#flytekitmodelsexecutionworkflowexecutiongetdataresponse) |  |
| [`flytekit.models.filters.Contains`](flytekit.models.filters#flytekitmodelsfilterscontains) |  |
| [`flytekit.models.filters.Equal`](flytekit.models.filters#flytekitmodelsfiltersequal) |  |
| [`flytekit.models.filters.Filter`](flytekit.models.filters#flytekitmodelsfiltersfilter) |  |
| [`flytekit.models.filters.FilterList`](flytekit.models.filters#flytekitmodelsfiltersfilterlist) |  |
| [`flytekit.models.filters.GreaterThan`](flytekit.models.filters#flytekitmodelsfiltersgreaterthan) |  |
| [`flytekit.models.filters.GreaterThanOrEqual`](flytekit.models.filters#flytekitmodelsfiltersgreaterthanorequal) |  |
| [`flytekit.models.filters.LessThan`](flytekit.models.filters#flytekitmodelsfilterslessthan) |  |
| [`flytekit.models.filters.LessThanOrEqual`](flytekit.models.filters#flytekitmodelsfilterslessthanorequal) |  |
| [`flytekit.models.filters.NotEqual`](flytekit.models.filters#flytekitmodelsfiltersnotequal) |  |
| [`flytekit.models.filters.SetFilter`](flytekit.models.filters#flytekitmodelsfilterssetfilter) |  |
| [`flytekit.models.filters.ValueIn`](flytekit.models.filters#flytekitmodelsfiltersvaluein) |  |
| [`flytekit.models.filters.ValueNotIn`](flytekit.models.filters#flytekitmodelsfiltersvaluenotin) |  |
| [`flytekit.models.interface.Parameter`](flytekit.models.interface#flytekitmodelsinterfaceparameter) |  |
| [`flytekit.models.interface.ParameterMap`](flytekit.models.interface#flytekitmodelsinterfaceparametermap) |  |
| [`flytekit.models.interface.TypedInterface`](flytekit.models.interface#flytekitmodelsinterfacetypedinterface) |  |
| [`flytekit.models.interface.Variable`](flytekit.models.interface#flytekitmodelsinterfacevariable) |  |
| [`flytekit.models.interface.VariableMap`](flytekit.models.interface#flytekitmodelsinterfacevariablemap) |  |
| [`flytekit.models.launch_plan.Auth`](flytekit.models.launch_plan#flytekitmodelslaunch_planauth) |  |
| [`flytekit.models.launch_plan.LaunchPlan`](flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplan) |  |
| [`flytekit.models.launch_plan.LaunchPlanClosure`](flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanclosure) |  |
| [`flytekit.models.launch_plan.LaunchPlanMetadata`](flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanmetadata) |  |
| [`flytekit.models.launch_plan.LaunchPlanSpec`](flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanspec) |  |
| [`flytekit.models.launch_plan.LaunchPlanState`](flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanstate) |  |
| [`flytekit.models.literals.Binary`](flytekit.models.literals#flytekitmodelsliteralsbinary) |  |
| [`flytekit.models.literals.Binding`](flytekit.models.literals#flytekitmodelsliteralsbinding) |  |
| [`flytekit.models.literals.BindingData`](flytekit.models.literals#flytekitmodelsliteralsbindingdata) |  |
| [`flytekit.models.literals.BindingDataCollection`](flytekit.models.literals#flytekitmodelsliteralsbindingdatacollection) |  |
| [`flytekit.models.literals.BindingDataMap`](flytekit.models.literals#flytekitmodelsliteralsbindingdatamap) |  |
| [`flytekit.models.literals.Blob`](flytekit.models.literals#flytekitmodelsliteralsblob) |  |
| [`flytekit.models.literals.BlobMetadata`](flytekit.models.literals#flytekitmodelsliteralsblobmetadata) | This is metadata for the Blob literal. |
| [`flytekit.models.literals.Literal`](flytekit.models.literals#flytekitmodelsliteralsliteral) |  |
| [`flytekit.models.literals.LiteralCollection`](flytekit.models.literals#flytekitmodelsliteralsliteralcollection) |  |
| [`flytekit.models.literals.LiteralMap`](flytekit.models.literals#flytekitmodelsliteralsliteralmap) |  |
| [`flytekit.models.literals.LiteralOffloadedMetadata`](flytekit.models.literals#flytekitmodelsliteralsliteraloffloadedmetadata) |  |
| [`flytekit.models.literals.Primitive`](flytekit.models.literals#flytekitmodelsliteralsprimitive) |  |
| [`flytekit.models.literals.RetryStrategy`](flytekit.models.literals#flytekitmodelsliteralsretrystrategy) |  |
| [`flytekit.models.literals.Scalar`](flytekit.models.literals#flytekitmodelsliteralsscalar) |  |
| [`flytekit.models.literals.Schema`](flytekit.models.literals#flytekitmodelsliteralsschema) |  |
| [`flytekit.models.literals.StructuredDataset`](flytekit.models.literals#flytekitmodelsliteralsstructureddataset) |  |
| [`flytekit.models.literals.StructuredDatasetMetadata`](flytekit.models.literals#flytekitmodelsliteralsstructureddatasetmetadata) |  |
| [`flytekit.models.literals.Union`](flytekit.models.literals#flytekitmodelsliteralsunion) |  |
| [`flytekit.models.literals.Void`](flytekit.models.literals#flytekitmodelsliteralsvoid) |  |
| [`flytekit.models.matchable_resource.ClusterResourceAttributes`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceclusterresourceattributes) |  |
| [`flytekit.models.matchable_resource.ExecutionClusterLabel`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionclusterlabel) |  |
| [`flytekit.models.matchable_resource.ExecutionQueueAttributes`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionqueueattributes) |  |
| [`flytekit.models.matchable_resource.MatchableResource`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchableresource) |  |
| [`flytekit.models.matchable_resource.MatchingAttributes`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchingattributes) |  |
| [`flytekit.models.matchable_resource.PluginOverride`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverride) |  |
| [`flytekit.models.matchable_resource.PluginOverrides`](flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverrides) |  |
| [`flytekit.models.named_entity.NamedEntityIdentifier`](flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentityidentifier) |  |
| [`flytekit.models.named_entity.NamedEntityMetadata`](flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentitymetadata) |  |
| [`flytekit.models.named_entity.NamedEntityState`](flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentitystate) |  |
| [`flytekit.models.node_execution.DynamicWorkflowNodeMetadata`](flytekit.models.node_execution#flytekitmodelsnode_executiondynamicworkflownodemetadata) |  |
| [`flytekit.models.node_execution.NodeExecution`](flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecution) |  |
| [`flytekit.models.node_execution.NodeExecutionClosure`](flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecutionclosure) |  |
| [`flytekit.models.node_execution.TaskNodeMetadata`](flytekit.models.node_execution#flytekitmodelsnode_executiontasknodemetadata) |  |
| [`flytekit.models.node_execution.WorkflowNodeMetadata`](flytekit.models.node_execution#flytekitmodelsnode_executionworkflownodemetadata) |  |
| [`flytekit.models.presto.PrestoQuery`](flytekit.models.presto#flytekitmodelsprestoprestoquery) |  |
| [`flytekit.models.project.Project`](flytekit.models.project#flytekitmodelsprojectproject) |  |
| [`flytekit.models.qubole.HiveQuery`](flytekit.models.qubole#flytekitmodelsqubolehivequery) |  |
| [`flytekit.models.qubole.HiveQueryCollection`](flytekit.models.qubole#flytekitmodelsqubolehivequerycollection) |  |
| [`flytekit.models.qubole.QuboleHiveJob`](flytekit.models.qubole#flytekitmodelsqubolequbolehivejob) |  |
| [`flytekit.models.schedule.Schedule`](flytekit.models.schedule#flytekitmodelsscheduleschedule) |  |
| [`flytekit.models.security.Identity`](flytekit.models.security#flytekitmodelssecurityidentity) |  |
| [`flytekit.models.security.OAuth2Client`](flytekit.models.security#flytekitmodelssecurityoauth2client) |  |
| [`flytekit.models.security.OAuth2TokenRequest`](flytekit.models.security#flytekitmodelssecurityoauth2tokenrequest) |  |
| [`flytekit.models.security.Secret`](flytekit.models.security#flytekitmodelssecuritysecret) | See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.models.security.SecurityContext`](flytekit.models.security#flytekitmodelssecuritysecuritycontext) | This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.models.task.CompiledTask`](flytekit.models.task#flytekitmodelstaskcompiledtask) |  |
| [`flytekit.models.task.Container`](flytekit.models.task#flytekitmodelstaskcontainer) |  |
| [`flytekit.models.task.DataLoadingConfig`](flytekit.models.task#flytekitmodelstaskdataloadingconfig) |  |
| [`flytekit.models.task.IOStrategy`](flytekit.models.task#flytekitmodelstaskiostrategy) | Provides methods to manage data in and out of the Raw container using Download Modes. |
| [`flytekit.models.task.K8sObjectMetadata`](flytekit.models.task#flytekitmodelstaskk8sobjectmetadata) |  |
| [`flytekit.models.task.K8sPod`](flytekit.models.task#flytekitmodelstaskk8spod) |  |
| [`flytekit.models.task.Resources`](flytekit.models.task#flytekitmodelstaskresources) |  |
| [`flytekit.models.task.RuntimeMetadata`](flytekit.models.task#flytekitmodelstaskruntimemetadata) |  |
| [`flytekit.models.task.Sql`](flytekit.models.task#flytekitmodelstasksql) |  |
| [`flytekit.models.task.Task`](flytekit.models.task#flytekitmodelstasktask) |  |
| [`flytekit.models.task.TaskClosure`](flytekit.models.task#flytekitmodelstasktaskclosure) |  |
| [`flytekit.models.task.TaskExecutionMetadata`](flytekit.models.task#flytekitmodelstasktaskexecutionmetadata) |  |
| [`flytekit.models.task.TaskMetadata`](flytekit.models.task#flytekitmodelstasktaskmetadata) |  |
| [`flytekit.models.task.TaskSpec`](flytekit.models.task#flytekitmodelstasktaskspec) |  |
| [`flytekit.models.task.TaskTemplate`](flytekit.models.task#flytekitmodelstasktasktemplate) |  |
| [`flytekit.models.types.Error`](flytekit.models.types#flytekitmodelstypeserror) |  |
| [`flytekit.models.types.LiteralType`](flytekit.models.types#flytekitmodelstypesliteraltype) |  |
| [`flytekit.models.types.OutputReference`](flytekit.models.types#flytekitmodelstypesoutputreference) |  |
| [`flytekit.models.types.SchemaType`](flytekit.models.types#flytekitmodelstypesschematype) |  |
| [`flytekit.models.types.SimpleType`](flytekit.models.types#flytekitmodelstypessimpletype) |  |
| [`flytekit.models.types.StructuredDatasetType`](flytekit.models.types#flytekitmodelstypesstructureddatasettype) |  |
| [`flytekit.models.types.TypeStructure`](flytekit.models.types#flytekitmodelstypestypestructure) | Models _types_pb2. |
| [`flytekit.models.types.UnionType`](flytekit.models.types#flytekitmodelstypesuniontype) | Models _types_pb2. |
| [`flytekit.models.workflow_closure.WorkflowClosure`](flytekit.models.workflow_closure#flytekitmodelsworkflow_closureworkflowclosure) |  |
| [`flytekit.remote.entities.FlyteArrayNode`](flytekit.remote.entities#flytekitremoteentitiesflytearraynode) |  |
| [`flytekit.remote.entities.FlyteBranchNode`](flytekit.remote.entities#flytekitremoteentitiesflytebranchnode) |  |
| [`flytekit.remote.entities.FlyteGateNode`](flytekit.remote.entities#flytekitremoteentitiesflytegatenode) |  |
| [`flytekit.remote.entities.FlyteLaunchPlan`](flytekit.remote.entities#flytekitremoteentitiesflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.entities.FlyteNode`](flytekit.remote.entities#flytekitremoteentitiesflytenode) | A class encapsulating a remote Flyte node. |
| [`flytekit.remote.entities.FlyteTask`](flytekit.remote.entities#flytekitremoteentitiesflytetask) | A class encapsulating a remote Flyte task. |
| [`flytekit.remote.entities.FlyteTaskNode`](flytekit.remote.entities#flytekitremoteentitiesflytetasknode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`flytekit.remote.entities.FlyteWorkflow`](flytekit.remote.entities#flytekitremoteentitiesflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.entities.FlyteWorkflowNode`](flytekit.remote.entities#flytekitremoteentitiesflyteworkflownode) | A class encapsulating a workflow that a Flyte node needs to execute. |
| [`flytekit.remote.executions.FlyteNodeExecution`](flytekit.remote.executions#flytekitremoteexecutionsflytenodeexecution) | A class encapsulating a node execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteTaskExecution`](flytekit.remote.executions#flytekitremoteexecutionsflytetaskexecution) | A class encapsulating a task execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteWorkflowExecution`](flytekit.remote.executions#flytekitremoteexecutionsflyteworkflowexecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.RemoteExecutionBase`](flytekit.remote.executions#flytekitremoteexecutionsremoteexecutionbase) |  |
| [`flytekit.remote.interface.TypedInterface`](flytekit.remote.interface#flytekitremoteinterfacetypedinterface) |  |
| [`flytekit.remote.lazy_entity.LazyEntity`](flytekit.remote.lazy_entity#flytekitremotelazy_entitylazyentity) | Fetches the entity when the entity is called or when the entity is retrieved. |
| [`flytekit.remote.metrics.FlyteExecutionSpan`](flytekit.remote.metrics#flytekitremotemetricsflyteexecutionspan) |  |
| [`flytekit.remote.remote.FlyteRemote`](flytekit.remote.remote#flytekitremoteremoteflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.remote.remote.RegistrationSkipped`](flytekit.remote.remote#flytekitremoteremoteregistrationskipped) | RegistrationSkipped error is raised when trying to register an entity that is not registrable. |
| [`flytekit.remote.remote.ResolvedIdentifiers`](flytekit.remote.remote#flytekitremoteremoteresolvedidentifiers) |  |
| [`flytekit.remote.remote_callable.RemoteEntity`](flytekit.remote.remote_callable#flytekitremoteremote_callableremoteentity) |  |
| [`flytekit.remote.remote_fs.FlyteFS`](flytekit.remote.remote_fs#flytekitremoteremote_fsflytefs) | Want this to behave mostly just like the HTTP file system. |
| [`flytekit.remote.remote_fs.FlytePathResolver`](flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) |  |
| [`flytekit.remote.remote_fs.HttpFileWriter`](flytekit.remote.remote_fs#flytekitremoteremote_fshttpfilewriter) |  |
| [`flytekit.sensor.base_sensor.BaseSensor`](flytekit.sensor.base_sensor#flytekitsensorbase_sensorbasesensor) | Base class for all sensors. |
| [`flytekit.sensor.base_sensor.SensorMetadata`](flytekit.sensor.base_sensor#flytekitsensorbase_sensorsensormetadata) |  |
| [`flytekit.sensor.file_sensor.FileSensor`](flytekit.sensor.file_sensor#flytekitsensorfile_sensorfilesensor) |  |
| [`flytekit.sensor.sensor_engine.SensorEngine`](flytekit.sensor.sensor_engine#flytekitsensorsensor_enginesensorengine) |  |
| [`flytekit.tools.fast_registration.FastPackageOptions`](flytekit.tools.fast_registration#flytekittoolsfast_registrationfastpackageoptions) | FastPackageOptions is used to set configuration options when packaging files. |
| [`flytekit.tools.ignore.DockerIgnore`](flytekit.tools.ignore#flytekittoolsignoredockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`flytekit.tools.ignore.FlyteIgnore`](flytekit.tools.ignore#flytekittoolsignoreflyteignore) | Uses a. |
| [`flytekit.tools.ignore.GitIgnore`](flytekit.tools.ignore#flytekittoolsignoregitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`flytekit.tools.ignore.Ignore`](flytekit.tools.ignore#flytekittoolsignoreignore) | Base for Ignores, implements core logic. |
| [`flytekit.tools.ignore.IgnoreGroup`](flytekit.tools.ignore#flytekittoolsignoreignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`flytekit.tools.ignore.StandardIgnore`](flytekit.tools.ignore#flytekittoolsignorestandardignore) | Retains the standard ignore functionality that previously existed. |
| [`flytekit.tools.repo.NoSerializableEntitiesError`](flytekit.tools.repo#flytekittoolsreponoserializableentitieserror) |  |
| [`flytekit.types.directory.types.FlyteDirToMultipartBlobTransformer`](flytekit.types.directory.types#flytekittypesdirectorytypesflytedirtomultipartblobtransformer) | This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`flytekit.types.directory.types.FlyteDirectory`](flytekit.types.directory.types#flytekittypesdirectorytypesflytedirectory) |  |
| [`flytekit.types.error.error.ErrorTransformer`](flytekit.types.error.error#flytekittypeserrorerrorerrortransformer) | Enables converting a python type FlyteError to LiteralType. |
| [`flytekit.types.error.error.FlyteError`](flytekit.types.error.error#flytekittypeserrorerrorflyteerror) | Special Task type that will be used in the failure node. |
| [`flytekit.types.file.FileExt`](flytekit.types.file#flytekittypesfilefileext) | Used for annotating file extension types of FlyteFile. |
| [`flytekit.types.file.file.FlyteFile`](flytekit.types.file.file#flytekittypesfilefileflytefile) |  |
| [`flytekit.types.file.file.FlyteFilePathTransformer`](flytekit.types.file.file#flytekittypesfilefileflytefilepathtransformer) |  |
| [`flytekit.types.file.image.PILImageTransformer`](flytekit.types.file.image#flytekittypesfileimagepilimagetransformer) | TypeTransformer that supports PIL. |
| [`flytekit.types.iterator.iterator.FlyteIterator`](flytekit.types.iterator.iterator#flytekittypesiteratoriteratorflyteiterator) |  |
| [`flytekit.types.iterator.iterator.IteratorTransformer`](flytekit.types.iterator.iterator#flytekittypesiteratoriteratoriteratortransformer) |  |
| [`flytekit.types.iterator.json_iterator.JSONIterator`](flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorjsoniterator) |  |
| [`flytekit.types.iterator.json_iterator.JSONIteratorTransformer`](flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorjsoniteratortransformer) | A JSON iterator that handles conversion between an iterator/generator and a JSONL file. |
| [`flytekit.types.numpy.ndarray.NumpyArrayTransformer`](flytekit.types.numpy.ndarray#flytekittypesnumpyndarraynumpyarraytransformer) | TypeTransformer that supports np. |
| [`flytekit.types.pickle.pickle.FlytePickle`](flytekit.types.pickle.pickle#flytekittypespicklepickleflytepickle) | This type is only used by flytekit internally. |
| [`flytekit.types.pickle.pickle.FlytePickleTransformer`](flytekit.types.pickle.pickle#flytekittypespicklepickleflytepickletransformer) |  |
| [`flytekit.types.schema.types.FlyteSchema`](flytekit.types.schema.types#flytekittypesschematypesflyteschema) |  |
| [`flytekit.types.schema.types.FlyteSchemaTransformer`](flytekit.types.schema.types#flytekittypesschematypesflyteschematransformer) |  |
| [`flytekit.types.schema.types.LocalIOSchemaReader`](flytekit.types.schema.types#flytekittypesschematypeslocalioschemareader) |  |
| [`flytekit.types.schema.types.LocalIOSchemaWriter`](flytekit.types.schema.types#flytekittypesschematypeslocalioschemawriter) |  |
| [`flytekit.types.schema.types.SchemaEngine`](flytekit.types.schema.types#flytekittypesschematypesschemaengine) | This is the core Engine that handles all schema sub-systems. |
| [`flytekit.types.schema.types.SchemaFormat`](flytekit.types.schema.types#flytekittypesschematypesschemaformat) | Represents the schema storage format (at rest). |
| [`flytekit.types.schema.types.SchemaHandler`](flytekit.types.schema.types#flytekittypesschematypesschemahandler) |  |
| [`flytekit.types.schema.types.SchemaOpenMode`](flytekit.types.schema.types#flytekittypesschematypesschemaopenmode) |  |
| [`flytekit.types.schema.types.SchemaReader`](flytekit.types.schema.types#flytekittypesschematypesschemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types.SchemaWriter`](flytekit.types.schema.types#flytekittypesschematypesschemawriter) |  |
| [`flytekit.types.schema.types_pandas.PandasDataFrameTransformer`](flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasdataframetransformer) | Transforms a pd. |
| [`flytekit.types.schema.types_pandas.PandasSchemaReader`](flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemareader) |  |
| [`flytekit.types.schema.types_pandas.PandasSchemaWriter`](flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemawriter) |  |
| [`flytekit.types.schema.types_pandas.ParquetIO`](flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasparquetio) |  |
| [`flytekit.types.structured.basic_dfs.ArrowToParquetEncodingHandler`](flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsarrowtoparquetencodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.CSVToPandasDecodingHandler`](flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfscsvtopandasdecodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.PandasToCSVEncodingHandler`](flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastocsvencodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.PandasToParquetEncodingHandler`](flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastoparquetencodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.ParquetToArrowDecodingHandler`](flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettoarrowdecodinghandler) |  |
| [`flytekit.types.structured.basic_dfs.ParquetToPandasDecodingHandler`](flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettopandasdecodinghandler) |  |
| [`flytekit.types.structured.bigquery.ArrowToBQEncodingHandlers`](flytekit.types.structured.bigquery#flytekittypesstructuredbigqueryarrowtobqencodinghandlers) |  |
| [`flytekit.types.structured.bigquery.BQToArrowDecodingHandler`](flytekit.types.structured.bigquery#flytekittypesstructuredbigquerybqtoarrowdecodinghandler) |  |
| [`flytekit.types.structured.bigquery.BQToPandasDecodingHandler`](flytekit.types.structured.bigquery#flytekittypesstructuredbigquerybqtopandasdecodinghandler) |  |
| [`flytekit.types.structured.bigquery.PandasToBQEncodingHandlers`](flytekit.types.structured.bigquery#flytekittypesstructuredbigquerypandastobqencodinghandlers) |  |
| [`flytekit.types.structured.snowflake.PandasToSnowflakeEncodingHandlers`](flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakepandastosnowflakeencodinghandlers) |  |
| [`flytekit.types.structured.snowflake.SnowflakeToPandasDecodingHandler`](flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakesnowflaketopandasdecodinghandler) |  |
| [`flytekit.types.structured.structured_dataset.DuplicateHandlerError`](flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetduplicatehandlererror) |  |
| [`flytekit.types.structured.structured_dataset.StructuredDataset`](flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddataset) | This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetDecoder`](flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetdecoder) |  |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetEncoder`](flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetencoder) |  |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetTransformerEngine`](flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flytekit.utils.rate_limiter.RateLimiter`](flytekit.utils.rate_limiter#flytekitutilsrate_limiterratelimiter) | Rate limiter that allows up to a certain number of requests per minute. |

### Protocols

| Protocol | Description |
|-|-|
| [`flytekit.configuration.plugin.FlytekitPluginProtocol`](flytekit.configuration.plugin#flytekitconfigurationpluginflytekitpluginprotocol) |  |
| [`flytekit.core.artifact.ArtifactSerializationHandler`](flytekit.core.artifact#flytekitcoreartifactartifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`flytekit.core.cache.CachePolicy`](flytekit.core.cache#flytekitcorecachecachepolicy) |  |
| [`flytekit.core.context_manager.SerializableToString`](flytekit.core.context_manager#flytekitcorecontext_managerserializabletostring) | This protocol is used by the Artifact create_from function. |
| [`flytekit.core.promise.HasFlyteInterface`](flytekit.core.promise#flytekitcorepromisehasflyteinterface) |  |
| [`flytekit.core.promise.LocallyExecutable`](flytekit.core.promise#flytekitcorepromiselocallyexecutable) |  |
| [`flytekit.core.promise.SupportsNodeCreation`](flytekit.core.promise#flytekitcorepromisesupportsnodecreation) |  |
| [`flytekit.core.schedule.LaunchPlanTriggerBase`](flytekit.core.schedule#flytekitcoreschedulelaunchplantriggerbase) |  |
| [`flytekit.deck.renderer.Renderable`](flytekit.deck.renderer#flytekitdeckrendererrenderable) |  |
| [`flytekit.sensor.base_sensor.SensorConfig`](flytekit.sensor.base_sensor#flytekitsensorbase_sensorsensorconfig) |  |

### Functions

| Function | Description |
|-|-|
| [`flytekit.current_context()`](flytekit#current_context) | Use this method to get a handle of specific parameters available in a flyte task. |
| [`flytekit.load_implicit_plugins()`](flytekit#load_implicit_plugins) | This method allows loading all plugins that have the entrypoint specification. |
| [`flytekit.new_context()`](flytekit#new_context) |  |
| [`flytekit.bin.entrypoint.get_container_error_timestamp()`](flytekit.bin.entrypoint#get_container_error_timestamp) | Get timestamp for ContainerError. |
| [`flytekit.bin.entrypoint.get_one_of()`](flytekit.bin.entrypoint#get_one_of) | Helper function to iterate through a series of different environment variables. |
| [`flytekit.bin.entrypoint.get_traceback_str()`](flytekit.bin.entrypoint#get_traceback_str) |  |
| [`flytekit.bin.entrypoint.get_version_message()`](flytekit.bin.entrypoint#get_version_message) |  |
| [`flytekit.bin.entrypoint.normalize_inputs()`](flytekit.bin.entrypoint#normalize_inputs) |  |
| [`flytekit.bin.entrypoint.setup_execution()`](flytekit.bin.entrypoint#setup_execution) |  |
| [`flytekit.clients.auth.default_html.get_default_success_html()`](flytekit.clients.auth.default_html#get_default_success_html) |  |
| [`flytekit.clients.auth.token_client.get_basic_authorization_header()`](flytekit.clients.auth.token_client#get_basic_authorization_header) | This function transforms the client id and the client secret into a header that conforms with http basic auth. |
| [`flytekit.clients.auth.token_client.get_device_code()`](flytekit.clients.auth.token_client#get_device_code) | Retrieves the device Authentication code that can be done to authenticate the request using a browser on a. |
| [`flytekit.clients.auth.token_client.get_token()`](flytekit.clients.auth.token_client#get_token) | retrieved from the IDP, the third is the expiration in seconds. |
| [`flytekit.clients.auth.token_client.poll_token_endpoint()`](flytekit.clients.auth.token_client#poll_token_endpoint) |  |
| [`flytekit.clients.auth_helper.bootstrap_creds_from_server()`](flytekit.clients.auth_helper#bootstrap_creds_from_server) | Retrieves the SSL cert from the remote and uses that. |
| [`flytekit.clients.auth_helper.get_authenticated_channel()`](flytekit.clients.auth_helper#get_authenticated_channel) | Returns a new channel for the given config that is authenticated. |
| [`flytekit.clients.auth_helper.get_authenticator()`](flytekit.clients.auth_helper#get_authenticator) | Returns a new authenticator based on the platform config. |
| [`flytekit.clients.auth_helper.get_channel()`](flytekit.clients.auth_helper#get_channel) | Creates a new grpc. |
| [`flytekit.clients.auth_helper.get_proxy_authenticator()`](flytekit.clients.auth_helper#get_proxy_authenticator) |  |
| [`flytekit.clients.auth_helper.get_session()`](flytekit.clients.auth_helper#get_session) | Return a new session for the given platform config. |
| [`flytekit.clients.auth_helper.register_authenticator_plugin()`](flytekit.clients.auth_helper#register_authenticator_plugin) | Register an authenticator factory by name. |
| [`flytekit.clients.auth_helper.upgrade_channel_to_authenticated()`](flytekit.clients.auth_helper#upgrade_channel_to_authenticated) | Given a grpc. |
| [`flytekit.clients.auth_helper.upgrade_channel_to_proxy_authenticated()`](flytekit.clients.auth_helper#upgrade_channel_to_proxy_authenticated) | If activated in the platform config, given a grpc. |
| [`flytekit.clients.auth_helper.upgrade_session_to_proxy_authenticated()`](flytekit.clients.auth_helper#upgrade_session_to_proxy_authenticated) | Given a requests. |
| [`flytekit.clients.auth_helper.wrap_exceptions_channel()`](flytekit.clients.auth_helper#wrap_exceptions_channel) | Wraps the input channel with RetryExceptionWrapperInterceptor. |
| [`flytekit.clients.grpc_utils.deadline_interceptor.get_scoped_grpc_deadline()`](flytekit.clients.grpc_utils.deadline_interceptor#get_scoped_grpc_deadline) |  |
| [`flytekit.clients.grpc_utils.deadline_interceptor.scoped_grpc_deadline()`](flytekit.clients.grpc_utils.deadline_interceptor#scoped_grpc_deadline) |  |
| [`flytekit.clients.helpers.iterate_node_executions()`](flytekit.clients.helpers#iterate_node_executions) | This returns a generator for node executions. |
| [`flytekit.clients.helpers.iterate_task_executions()`](flytekit.clients.helpers#iterate_task_executions) | This returns a generator for task executions, given a node execution identifier. |
| [`flytekit.clis.helpers.display_help_with_error()`](flytekit.clis.helpers#display_help_with_error) |  |
| [`flytekit.clis.helpers.hydrate_registration_parameters()`](flytekit.clis.helpers#hydrate_registration_parameters) | This is called at registration time to fill out identifier fields (e. |
| [`flytekit.clis.helpers.parse_args_into_dict()`](flytekit.clis.helpers#parse_args_into_dict) | Takes a tuple like (u'input_b=mystr', u'input_c=18') and returns a dictionary of input name to the. |
| [`flytekit.clis.helpers.str2bool()`](flytekit.clis.helpers#str2bool) | bool('False') is True in Python, so we need to do some string parsing. |
| [`flytekit.clis.sdk_in_container.backfill.resolve_backfill_window()`](flytekit.clis.sdk_in_container.backfill#resolve_backfill_window) | Resolves the from_date -> to_date. |
| [`flytekit.clis.sdk_in_container.build.build_command()`](flytekit.clis.sdk_in_container.build#build_command) | Returns a function that is used to implement WorkflowCommand and build an image for flyte workflows. |
| [`flytekit.clis.sdk_in_container.helpers.get_and_save_remote_with_click_context()`](flytekit.clis.sdk_in_container.helpers#get_and_save_remote_with_click_context) | NB: This function will by default mutate the click Context. |
| [`flytekit.clis.sdk_in_container.helpers.parse_copy()`](flytekit.clis.sdk_in_container.helpers#parse_copy) | Helper function to parse cmd line args into enum. |
| [`flytekit.clis.sdk_in_container.helpers.patch_image_config()`](flytekit.clis.sdk_in_container.helpers#patch_image_config) | Merge ImageConfig object with images defined in config file. |
| [`flytekit.clis.sdk_in_container.run.dump_flyte_remote_snippet()`](flytekit.clis.sdk_in_container.run#dump_flyte_remote_snippet) |  |
| [`flytekit.clis.sdk_in_container.run.get_entities_in_file()`](flytekit.clis.sdk_in_container.run#get_entities_in_file) | Returns a list of flyte workflow names and list of Flyte tasks in a file. |
| [`flytekit.clis.sdk_in_container.run.is_optional()`](flytekit.clis.sdk_in_container.run#is_optional) | Checks if the given type is Optional Type. |
| [`flytekit.clis.sdk_in_container.run.load_naive_entity()`](flytekit.clis.sdk_in_container.run#load_naive_entity) | Load the workflow of a script file. |
| [`flytekit.clis.sdk_in_container.run.options_from_run_params()`](flytekit.clis.sdk_in_container.run#options_from_run_params) |  |
| [`flytekit.clis.sdk_in_container.run.run_command()`](flytekit.clis.sdk_in_container.run#run_command) | Returns a function that is used to implement WorkflowCommand and execute a flyte workflow. |
| [`flytekit.clis.sdk_in_container.run.run_remote()`](flytekit.clis.sdk_in_container.run#run_remote) | Helper method that executes the given remote FlyteLaunchplan, FlyteWorkflow or FlyteTask. |
| [`flytekit.clis.sdk_in_container.run.to_click_option()`](flytekit.clis.sdk_in_container.run#to_click_option) | This handles converting workflow input types to supported click parameters with callbacks to initialize. |
| [`flytekit.clis.sdk_in_container.serialize.serialize_all()`](flytekit.clis.sdk_in_container.serialize#serialize_all) | This function will write to the folder specified the following protobuf types. |
| [`flytekit.clis.sdk_in_container.serve.print_metadata()`](flytekit.clis.sdk_in_container.serve#print_metadata) |  |
| [`flytekit.clis.sdk_in_container.utils.get_option_from_metadata()`](flytekit.clis.sdk_in_container.utils#get_option_from_metadata) |  |
| [`flytekit.clis.sdk_in_container.utils.make_click_option_field()`](flytekit.clis.sdk_in_container.utils#make_click_option_field) |  |
| [`flytekit.clis.sdk_in_container.utils.pretty_print_exception()`](flytekit.clis.sdk_in_container.utils#pretty_print_exception) | This method will print the exception in a nice way. |
| [`flytekit.clis.sdk_in_container.utils.pretty_print_grpc_error()`](flytekit.clis.sdk_in_container.utils#pretty_print_grpc_error) | This method will print the grpc error that us more human readable. |
| [`flytekit.clis.sdk_in_container.utils.pretty_print_traceback()`](flytekit.clis.sdk_in_container.utils#pretty_print_traceback) | This method will print the Traceback of an error. |
| [`flytekit.clis.sdk_in_container.utils.remove_unwanted_traceback_frames()`](flytekit.clis.sdk_in_container.utils#remove_unwanted_traceback_frames) | Custom function to remove certain frames from the traceback. |
| [`flytekit.clis.sdk_in_container.utils.validate_package()`](flytekit.clis.sdk_in_container.utils#validate_package) | This method will validate the packages passed in by the user. |
| [`flytekit.configuration.file.bool_transformer()`](flytekit.configuration.file#bool_transformer) |  |
| [`flytekit.configuration.file.comma_list_transformer()`](flytekit.configuration.file#comma_list_transformer) |  |
| [`flytekit.configuration.file.int_transformer()`](flytekit.configuration.file#int_transformer) |  |
| [`flytekit.configuration.file.read_file_if_exists()`](flytekit.configuration.file#read_file_if_exists) | Reads the contents of the file if passed a path. |
| [`flytekit.configuration.file.set_if_exists()`](flytekit.configuration.file#set_if_exists) | Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set. |
| [`flytekit.configuration.plugin.get_plugin()`](flytekit.configuration.plugin#get_plugin) | Get current plugin. |
| [`flytekit.core.array_node.array_node()`](flytekit.core.array_node#array_node) | ArrayNode implementation that maps over tasks and other Flyte entities. |
| [`flytekit.core.array_node_map_task.array_node_map_task()`](flytekit.core.array_node_map_task#array_node_map_task) | Map task that uses the ``ArrayNode`` construct. |
| [`flytekit.core.array_node_map_task.map_task()`](flytekit.core.array_node_map_task#map_task) | Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask. |
| [`flytekit.core.artifact_utils.idl_partitions_from_dict()`](flytekit.core.artifact_utils#idl_partitions_from_dict) |  |
| [`flytekit.core.artifact_utils.idl_time_partition_from_datetime()`](flytekit.core.artifact_utils#idl_time_partition_from_datetime) |  |
| [`flytekit.core.base_task.kwtypes()`](flytekit.core.base_task#kwtypes) | This is a small helper function to convert the keyword arguments to an OrderedDict of types. |
| [`flytekit.core.condition.conditional()`](flytekit.core.condition#conditional) | Use a conditional section to control the flow of a workflow. |
| [`flytekit.core.condition.create_branch_node_promise_var()`](flytekit.core.condition#create_branch_node_promise_var) | Generates a globally (wf-level) unique id for a variable. |
| [`flytekit.core.condition.merge_promises()`](flytekit.core.condition#merge_promises) |  |
| [`flytekit.core.condition.to_branch_node()`](flytekit.core.condition#to_branch_node) |  |
| [`flytekit.core.condition.to_case_block()`](flytekit.core.condition#to_case_block) |  |
| [`flytekit.core.condition.to_ifelse_block()`](flytekit.core.condition#to_ifelse_block) |  |
| [`flytekit.core.condition.transform_to_boolexpr()`](flytekit.core.condition#transform_to_boolexpr) |  |
| [`flytekit.core.condition.transform_to_comp_expr()`](flytekit.core.condition#transform_to_comp_expr) |  |
| [`flytekit.core.condition.transform_to_conj_expr()`](flytekit.core.condition#transform_to_conj_expr) |  |
| [`flytekit.core.condition.transform_to_operand()`](flytekit.core.condition#transform_to_operand) |  |
| [`flytekit.core.data_persistence.azure_setup_args()`](flytekit.core.data_persistence#azure_setup_args) |  |
| [`flytekit.core.data_persistence.get_additional_fsspec_call_kwargs()`](flytekit.core.data_persistence#get_additional_fsspec_call_kwargs) | These are different from the setup args functions defined above. |
| [`flytekit.core.data_persistence.get_fsspec_storage_options()`](flytekit.core.data_persistence#get_fsspec_storage_options) |  |
| [`flytekit.core.data_persistence.s3_setup_args()`](flytekit.core.data_persistence#s3_setup_args) |  |
| [`flytekit.core.environment.forge()`](flytekit.core.environment#forge) |  |
| [`flytekit.core.environment.inherit()`](flytekit.core.environment#inherit) |  |
| [`flytekit.core.gate.approve()`](flytekit.core.gate#approve) | Create a Gate object for binary approval. |
| [`flytekit.core.gate.sleep()`](flytekit.core.gate#sleep) | Create a sleep Gate object. |
| [`flytekit.core.gate.wait_for_input()`](flytekit.core.gate#wait_for_input) | Create a Gate object that waits for user input of the specified type. |
| [`flytekit.core.interface.default_output_name()`](flytekit.core.interface#default_output_name) |  |
| [`flytekit.core.interface.detect_artifact()`](flytekit.core.interface#detect_artifact) | If the user wishes to control how Artifacts are created (i. |
| [`flytekit.core.interface.extract_return_annotation()`](flytekit.core.interface#extract_return_annotation) | The purpose of this function is to sort out whether a function is returning one thing, or multiple things, and to. |
| [`flytekit.core.interface.output_name_generator()`](flytekit.core.interface#output_name_generator) |  |
| [`flytekit.core.interface.remap_shared_output_descriptions()`](flytekit.core.interface#remap_shared_output_descriptions) | Deals with mixed styles of return value descriptions used in docstrings. |
| [`flytekit.core.interface.repr_kv()`](flytekit.core.interface#repr_kv) |  |
| [`flytekit.core.interface.repr_type_signature()`](flytekit.core.interface#repr_type_signature) | Converts an inputs and outputs to a type signature. |
| [`flytekit.core.interface.transform_function_to_interface()`](flytekit.core.interface#transform_function_to_interface) | From the annotations on a task function that the user should have provided, and the output names they want to use. |
| [`flytekit.core.interface.transform_inputs_to_parameters()`](flytekit.core.interface#transform_inputs_to_parameters) | Transforms the given interface (with inputs) to a Parameter Map with defaults set. |
| [`flytekit.core.interface.transform_interface_to_list_interface()`](flytekit.core.interface#transform_interface_to_list_interface) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed python map. |
| [`flytekit.core.interface.transform_interface_to_typed_interface()`](flytekit.core.interface#transform_interface_to_typed_interface) | Transform the given simple python native interface to FlyteIDL's interface. |
| [`flytekit.core.interface.transform_type()`](flytekit.core.interface#transform_type) |  |
| [`flytekit.core.interface.transform_types_to_list_of_type()`](flytekit.core.interface#transform_types_to_list_of_type) | Converts unbound inputs into the equivalent (optional) collections. |
| [`flytekit.core.interface.transform_variable_map()`](flytekit.core.interface#transform_variable_map) | Given a map of str (names of inputs for instance) to their Python native types, return a map of the name to a. |
| [`flytekit.core.interface.verify_outputs_artifact_bindings()`](flytekit.core.interface#verify_outputs_artifact_bindings) |  |
| [`flytekit.core.launch_plan.reference_launch_plan()`](flytekit.core.launch_plan#reference_launch_plan) | A reference launch plan is a pointer to a launch plan that already exists on your Flyte installation. |
| [`flytekit.core.legacy_map_task.map_task()`](flytekit.core.legacy_map_task#map_task) | Use a map task for parallelizable tasks that run across a list of an input type. |
| [`flytekit.core.node.assert_no_promises_in_resources()`](flytekit.core.node#assert_no_promises_in_resources) | This function will raise an exception if any of the resources have promises in them. |
| [`flytekit.core.node.assert_not_promise()`](flytekit.core.node#assert_not_promise) | This function will raise an exception if the value is a promise. |
| [`flytekit.core.node_creation.create_node()`](flytekit.core.node_creation#create_node) | This is the function you want to call if you need to specify dependencies between tasks that don't consume and/or. |
| [`flytekit.core.pod_template.serialize_pod_template()`](flytekit.core.pod_template#serialize_pod_template) |  |
| [`flytekit.core.promise.async_flyte_entity_call_handler()`](flytekit.core.promise#async_flyte_entity_call_handler) | This is a limited async version of the main call handler. |
| [`flytekit.core.promise.binding_data_from_python_std()`](flytekit.core.promise#binding_data_from_python_std) |  |
| [`flytekit.core.promise.binding_from_python_std()`](flytekit.core.promise#binding_from_python_std) |  |
| [`flytekit.core.promise.create_and_link_node()`](flytekit.core.promise#create_and_link_node) | This method is used to generate a node with bindings within a flytekit workflow. |
| [`flytekit.core.promise.create_and_link_node_from_remote()`](flytekit.core.promise#create_and_link_node_from_remote) | This method is used to generate a node with bindings especially when using remote entities, like FlyteWorkflow,. |
| [`flytekit.core.promise.create_native_named_tuple()`](flytekit.core.promise#create_native_named_tuple) | Creates and returns a Named tuple with all variables that match the expected named outputs. |
| [`flytekit.core.promise.create_task_output()`](flytekit.core.promise#create_task_output) |  |
| [`flytekit.core.promise.extract_obj_name()`](flytekit.core.promise#extract_obj_name) | Generates a shortened name, without the module information. |
| [`flytekit.core.promise.flyte_entity_call_handler()`](flytekit.core.promise#flyte_entity_call_handler) | This function is the call handler for tasks, workflows, and launch plans (which redirects to the underlying. |
| [`flytekit.core.promise.get_primitive_val()`](flytekit.core.promise#get_primitive_val) |  |
| [`flytekit.core.promise.resolve_attr_path_in_dict()`](flytekit.core.promise#resolve_attr_path_in_dict) |  |
| [`flytekit.core.promise.resolve_attr_path_in_pb_struct()`](flytekit.core.promise#resolve_attr_path_in_pb_struct) | Resolves the protobuf struct (e. |
| [`flytekit.core.promise.resolve_attr_path_in_promise()`](flytekit.core.promise#resolve_attr_path_in_promise) | resolve_attr_path_in_promise resolves the attribute path in a promise and returns a new promise with the resolved value. |
| [`flytekit.core.promise.resolve_attr_path_recursively()`](flytekit.core.promise#resolve_attr_path_recursively) | This function resolves the attribute path in a nested structure recursively. |
| [`flytekit.core.promise.to_binding()`](flytekit.core.promise#to_binding) |  |
| [`flytekit.core.promise.translate_inputs_to_literals()`](flytekit.core.promise#translate_inputs_to_literals) | The point of this function is to extract out Literals from a collection of either Python native values (which would. |
| [`flytekit.core.promise.translate_inputs_to_native()`](flytekit.core.promise#translate_inputs_to_native) |  |
| [`flytekit.core.python_auto_container.get_registerable_container_image()`](flytekit.core.python_auto_container#get_registerable_container_image) | Resolve the image to the real image name that should be used for registration. |
| [`flytekit.core.python_auto_container.update_image_spec_copy_handling()`](flytekit.core.python_auto_container#update_image_spec_copy_handling) | This helper function is where the relationship between fast register and ImageSpec is codified. |
| [`flytekit.core.reference.get_reference_entity()`](flytekit.core.reference#get_reference_entity) | See the documentation for {{< py_class_ref flytekit.reference_task >}} and {{< py_class_ref flytekit.reference_workflow >}} as well. |
| [`flytekit.core.resources.construct_extended_resources()`](flytekit.core.resources#construct_extended_resources) | Convert public extended resources to idl. |
| [`flytekit.core.resources.convert_resources_to_resource_model()`](flytekit.core.resources#convert_resources_to_resource_model) | Convert flytekit ``Resources`` objects to a Resources model. |
| [`flytekit.core.resources.pod_spec_from_resources()`](flytekit.core.resources#pod_spec_from_resources) |  |
| [`flytekit.core.task.decorate_function()`](flytekit.core.task#decorate_function) | Decorates the task with additional functionality if necessary. |
| [`flytekit.core.task.eager()`](flytekit.core.task#eager) | Eager workflow decorator. |
| [`flytekit.core.task.reference_task()`](flytekit.core.task#reference_task) | A reference task is a pointer to a task that already exists on your Flyte installation. |
| [`flytekit.core.task.task()`](flytekit.core.task#task) | This is the core decorator to use for any task type in flytekit. |
| [`flytekit.core.testing.patch()`](flytekit.core.testing#patch) | This is a decorator used for testing. |
| [`flytekit.core.testing.task_mock()`](flytekit.core.testing#task_mock) | Use this method to mock a task declaration. |
| [`flytekit.core.tracker.extract_task_module()`](flytekit.core.tracker#extract_task_module) | Returns the task-name, absolute module and the string name of the callable. |
| [`flytekit.core.tracker.get_full_module_path()`](flytekit.core.tracker#get_full_module_path) |  |
| [`flytekit.core.tracker.import_module_from_file()`](flytekit.core.tracker#import_module_from_file) |  |
| [`flytekit.core.tracker.is_functools_wrapped_module_level()`](flytekit.core.tracker#is_functools_wrapped_module_level) | Returns true if the function is a functools. |
| [`flytekit.core.tracker.is_ipython_or_pickle_exists()`](flytekit.core.tracker#is_ipython_or_pickle_exists) | Returns true if the code is running in an IPython notebook or if a pickle file exists. |
| [`flytekit.core.tracker.isnested()`](flytekit.core.tracker#isnested) | Returns true if a function is local to another function and is not accessible through a module. |
| [`flytekit.core.tracker.istestfunction()`](flytekit.core.tracker#istestfunction) | Return true if the function is defined in a test module. |
| [`flytekit.core.type_engine.convert_marshmallow_json_schema_to_python_class()`](flytekit.core.type_engine#convert_marshmallow_json_schema_to_python_class) | Generate a model class based on the provided JSON Schema. |
| [`flytekit.core.type_engine.convert_mashumaro_json_schema_to_python_class()`](flytekit.core.type_engine#convert_mashumaro_json_schema_to_python_class) | Generate a model class based on the provided JSON Schema. |
| [`flytekit.core.type_engine.dataclass_from_dict()`](flytekit.core.type_engine#dataclass_from_dict) | Utility function to construct a dataclass object from dict. |
| [`flytekit.core.type_engine.generate_attribute_list_from_dataclass_json()`](flytekit.core.type_engine#generate_attribute_list_from_dataclass_json) |  |
| [`flytekit.core.type_engine.generate_attribute_list_from_dataclass_json_mixin()`](flytekit.core.type_engine#generate_attribute_list_from_dataclass_json_mixin) |  |
| [`flytekit.core.type_engine.get_batch_size()`](flytekit.core.type_engine#get_batch_size) |  |
| [`flytekit.core.type_engine.get_underlying_type()`](flytekit.core.type_engine#get_underlying_type) | Return the underlying type for annotated types or the type itself. |
| [`flytekit.core.type_engine.is_annotated()`](flytekit.core.type_engine#is_annotated) |  |
| [`flytekit.core.type_engine.modify_literal_uris()`](flytekit.core.type_engine#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths in case they are of. |
| [`flytekit.core.type_engine.strict_type_hint_matching()`](flytekit.core.type_engine#strict_type_hint_matching) | Try to be smarter about guessing the type of the input (and hence the transformer). |
| [`flytekit.core.type_helpers.load_type_from_tag()`](flytekit.core.type_helpers#load_type_from_tag) | Loads python type from tag. |
| [`flytekit.core.type_match_checking.literal_types_match()`](flytekit.core.type_match_checking#literal_types_match) | Returns if two LiteralTypes are the same. |
| [`flytekit.core.utils.has_return_statement()`](flytekit.core.utils#has_return_statement) |  |
| [`flytekit.core.utils.load_proto_from_file()`](flytekit.core.utils#load_proto_from_file) |  |
| [`flytekit.core.utils.str2bool()`](flytekit.core.utils#str2bool) | Convert a string to a boolean. |
| [`flytekit.core.utils.write_proto_to_file()`](flytekit.core.utils#write_proto_to_file) |  |
| [`flytekit.core.workflow.construct_input_promises()`](flytekit.core.workflow#construct_input_promises) |  |
| [`flytekit.core.workflow.get_promise()`](flytekit.core.workflow#get_promise) | This is a helper function that will turn a binding into a Promise object, using a lookup map. |
| [`flytekit.core.workflow.get_promise_map()`](flytekit.core.workflow#get_promise_map) | Local execution of imperatively defined workflows is done node by node. |
| [`flytekit.core.workflow.reference_workflow()`](flytekit.core.workflow#reference_workflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.core.workflow.workflow()`](flytekit.core.workflow#workflow) | This decorator declares a function to be a Flyte workflow. |
| [`flytekit.deck.deck.generate_time_table()`](flytekit.deck.deck#generate_time_table) |  |
| [`flytekit.deck.deck.get_deck_template()`](flytekit.deck.deck#get_deck_template) |  |
| [`flytekit.exceptions.scopes.system_entry_point()`](flytekit.exceptions.scopes#system_entry_point) | The reason these two (see the user one below) decorators exist is to categorize non-Flyte exceptions at arbitrary. |
| [`flytekit.exceptions.scopes.user_entry_point()`](flytekit.exceptions.scopes#user_entry_point) | See the comment for the system_entry_point above as well. |
| [`flytekit.exceptions.utils.annotate_exception_with_code()`](flytekit.exceptions.utils#annotate_exception_with_code) | Annotate the exception with the source code, and will be printed in the rich panel. |
| [`flytekit.exceptions.utils.get_source_code_from_fn()`](flytekit.exceptions.utils#get_source_code_from_fn) | Get the source code of the function and the column offset of the parameter defined in the input signature. |
| [`flytekit.extend.backend.connector_service.record_connector_metrics()`](flytekit.extend.backend.connector_service#record_connector_metrics) |  |
| [`flytekit.extend.backend.utils.convert_to_flyte_phase()`](flytekit.extend.backend.utils#convert_to_flyte_phase) | Convert the state from the connector to the phase in flyte. |
| [`flytekit.extend.backend.utils.get_agent_secret()`](flytekit.extend.backend.utils#get_agent_secret) |  |
| [`flytekit.extend.backend.utils.get_connector_secret()`](flytekit.extend.backend.utils#get_connector_secret) |  |
| [`flytekit.extend.backend.utils.is_terminal_phase()`](flytekit.extend.backend.utils#is_terminal_phase) | Return true if the phase is terminal. |
| [`flytekit.extend.backend.utils.mirror_async_methods()`](flytekit.extend.backend.utils#mirror_async_methods) |  |
| [`flytekit.extend.backend.utils.render_task_template()`](flytekit.extend.backend.utils#render_task_template) |  |
| [`flytekit.extras.sqlite3.task.unarchive_file()`](flytekit.extras.sqlite3.task#unarchive_file) | Unarchive given archive and returns the unarchived file name. |
| [`flytekit.extras.tasks.shell.get_raw_shell_task()`](flytekit.extras.tasks.shell#get_raw_shell_task) |  |
| [`flytekit.extras.tasks.shell.subproc_execute()`](flytekit.extras.tasks.shell#subproc_execute) | Execute a command and capture its stdout and stderr. |
| [`flytekit.image_spec.default_builder.create_docker_context()`](flytekit.image_spec.default_builder#create_docker_context) | Populate tmp_dir with Dockerfile as specified by the `image_spec`. |
| [`flytekit.image_spec.default_builder.get_flytekit_for_pypi()`](flytekit.image_spec.default_builder#get_flytekit_for_pypi) | Get flytekit version on PyPI. |
| [`flytekit.image_spec.default_builder.prepare_poetry_lock_command()`](flytekit.image_spec.default_builder#prepare_poetry_lock_command) |  |
| [`flytekit.image_spec.default_builder.prepare_python_executable()`](flytekit.image_spec.default_builder#prepare_python_executable) |  |
| [`flytekit.image_spec.default_builder.prepare_python_install()`](flytekit.image_spec.default_builder#prepare_python_install) |  |
| [`flytekit.image_spec.default_builder.prepare_uv_lock_command()`](flytekit.image_spec.default_builder#prepare_uv_lock_command) |  |
| [`flytekit.image_spec.image_spec.validate_container_registry_name()`](flytekit.image_spec.image_spec#validate_container_registry_name) | Validate Docker container registry name. |
| [`flytekit.interaction.click_types.is_pydantic_basemodel()`](flytekit.interaction.click_types#is_pydantic_basemodel) | Checks if the python type is a pydantic BaseModel. |
| [`flytekit.interaction.click_types.key_value_callback()`](flytekit.interaction.click_types#key_value_callback) | Callback for click to parse key-value pairs. |
| [`flytekit.interaction.click_types.labels_callback()`](flytekit.interaction.click_types#labels_callback) | Callback for click to parse labels. |
| [`flytekit.interaction.click_types.literal_type_to_click_type()`](flytekit.interaction.click_types#literal_type_to_click_type) | Converts a Flyte LiteralType given a python_type to a click. |
| [`flytekit.interaction.click_types.modify_literal_uris()`](flytekit.interaction.click_types#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths. |
| [`flytekit.interaction.click_types.resource_callback()`](flytekit.interaction.click_types#resource_callback) | Click callback to parse resource strings like 'cpu=1,mem=2Gi' into a Resources object. |
| [`flytekit.interaction.parse_stdin.parse_stdin_to_literal()`](flytekit.interaction.parse_stdin#parse_stdin_to_literal) | Parses the user input from stdin and converts it to a literal of the given type. |
| [`flytekit.interaction.string_literals.literal_map_string_repr()`](flytekit.interaction.string_literals#literal_map_string_repr) | This method is used to convert a literal map to a string representation. |
| [`flytekit.interaction.string_literals.literal_string_repr()`](flytekit.interaction.string_literals#literal_string_repr) | This method is used to convert a literal to a string representation. |
| [`flytekit.interaction.string_literals.primitive_to_string()`](flytekit.interaction.string_literals#primitive_to_string) | This method is used to convert a primitive to a string representation. |
| [`flytekit.interaction.string_literals.scalar_to_string()`](flytekit.interaction.string_literals#scalar_to_string) | This method is used to convert a scalar to a string representation. |
| [`flytekit.interactive.utils.execute_command()`](flytekit.interactive.utils#execute_command) | Execute a command in the shell. |
| [`flytekit.interactive.utils.get_task_inputs()`](flytekit.interactive.utils#get_task_inputs) | Read task input data from inputs. |
| [`flytekit.interactive.utils.load_module_from_path()`](flytekit.interactive.utils#load_module_from_path) | Imports a Python module from a specified file path. |
| [`flytekit.interactive.vscode_lib.decorator.download_file()`](flytekit.interactive.vscode_lib.decorator#download_file) | Download a file from a given URL using fsspec. |
| [`flytekit.interactive.vscode_lib.decorator.download_vscode()`](flytekit.interactive.vscode_lib.decorator#download_vscode) | Download vscode server and extension from remote to local and add the directory of binary executable to $PATH. |
| [`flytekit.interactive.vscode_lib.decorator.exit_handler()`](flytekit.interactive.vscode_lib.decorator#exit_handler) | 1. |
| [`flytekit.interactive.vscode_lib.decorator.get_code_server_info()`](flytekit.interactive.vscode_lib.decorator#get_code_server_info) | Returns the code server information based on the system's architecture. |
| [`flytekit.interactive.vscode_lib.decorator.get_installed_extensions()`](flytekit.interactive.vscode_lib.decorator#get_installed_extensions) | Get the list of installed extensions. |
| [`flytekit.interactive.vscode_lib.decorator.is_extension_installed()`](flytekit.interactive.vscode_lib.decorator#is_extension_installed) |  |
| [`flytekit.interactive.vscode_lib.decorator.prepare_interactive_python()`](flytekit.interactive.vscode_lib.decorator#prepare_interactive_python) | 1. |
| [`flytekit.interactive.vscode_lib.decorator.prepare_launch_json()`](flytekit.interactive.vscode_lib.decorator#prepare_launch_json) | Generate the launch. |
| [`flytekit.interactive.vscode_lib.decorator.prepare_resume_task_python()`](flytekit.interactive.vscode_lib.decorator#prepare_resume_task_python) | Generate a Python script for users to resume the task. |
| [`flytekit.interfaces.random.seed_flyte_random()`](flytekit.interfaces.random#seed_flyte_random) | If one wants to influence the pseudo-random behavior of flytekit, this function can be used to seed the flytekit. |
| [`flytekit.interfaces.stats.client.get_base_stats()`](flytekit.interfaces.stats.client#get_base_stats) |  |
| [`flytekit.interfaces.stats.client.get_stats()`](flytekit.interfaces.stats.client#get_stats) |  |
| [`flytekit.interfaces.stats.taggable.get_stats()`](flytekit.interfaces.stats.taggable#get_stats) |  |
| [`flytekit.lazy_import.lazy_module.is_imported()`](flytekit.lazy_import.lazy_module#is_imported) | This function is used to check if a module has been imported by the regular import. |
| [`flytekit.lazy_import.lazy_module.lazy_module()`](flytekit.lazy_import.lazy_module#lazy_module) | This function is used to lazily import modules. |
| [`flytekit.loggers.get_level_from_cli_verbosity()`](flytekit.loggers#get_level_from_cli_verbosity) | Converts a verbosity level from the CLI to a logging level. |
| [`flytekit.loggers.initialize_global_loggers()`](flytekit.loggers#initialize_global_loggers) | Initializes the global loggers to the default configuration. |
| [`flytekit.loggers.is_display_progress_enabled()`](flytekit.loggers#is_display_progress_enabled) |  |
| [`flytekit.loggers.is_rich_logging_enabled()`](flytekit.loggers#is_rich_logging_enabled) |  |
| [`flytekit.loggers.set_developer_properties()`](flytekit.loggers#set_developer_properties) | developer logger is only used for debugging. |
| [`flytekit.loggers.set_flytekit_log_properties()`](flytekit.loggers#set_flytekit_log_properties) | flytekit logger, refers to the framework logger. |
| [`flytekit.loggers.set_user_logger_properties()`](flytekit.loggers#set_user_logger_properties) | user_space logger, refers to the user's logger. |
| [`flytekit.loggers.upgrade_to_rich_logging()`](flytekit.loggers#upgrade_to_rich_logging) |  |
| [`flytekit.remote.backfill.create_backfill_workflow()`](flytekit.remote.backfill#create_backfill_workflow) | Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan. |
| [`flytekit.remote.data.download_literal()`](flytekit.remote.data#download_literal) | Download a single literal to a file, if it is a blob or structured dataset. |
| [`flytekit.remote.metrics.aggregate_reference_span()`](flytekit.remote.metrics#aggregate_reference_span) |  |
| [`flytekit.remote.metrics.aggregate_spans()`](flytekit.remote.metrics#aggregate_spans) |  |
| [`flytekit.remote.metrics.print_span()`](flytekit.remote.metrics#print_span) |  |
| [`flytekit.remote.remote_fs.get_flyte_fs()`](flytekit.remote.remote_fs#get_flyte_fs) |  |
| [`flytekit.tools.fast_registration.compress_tarball()`](flytekit.tools.fast_registration#compress_tarball) | Compress code tarball using pigz if available, otherwise gzip. |
| [`flytekit.tools.fast_registration.compute_digest()`](flytekit.tools.fast_registration#compute_digest) | Walks the entirety of the source dir to compute a deterministic md5 hex digest of the dir contents. |
| [`flytekit.tools.fast_registration.download_distribution()`](flytekit.tools.fast_registration#download_distribution) | Downloads a remote code distribution and overwrites any local files. |
| [`flytekit.tools.fast_registration.fast_package()`](flytekit.tools.fast_registration#fast_package) | Takes a source directory and packages everything not covered by common ignores into a tarball. |
| [`flytekit.tools.fast_registration.get_additional_distribution_loc()`](flytekit.tools.fast_registration#get_additional_distribution_loc) | :return Text:. |
| [`flytekit.tools.fast_registration.print_ls_tree()`](flytekit.tools.fast_registration#print_ls_tree) |  |
| [`flytekit.tools.interactive.ipython_check()`](flytekit.tools.interactive#ipython_check) | Check if interface is launching from iPython (not colab). |
| [`flytekit.tools.module_loader.add_sys_path()`](flytekit.tools.module_loader#add_sys_path) | Temporarily add given path to `sys. |
| [`flytekit.tools.module_loader.just_load_modules()`](flytekit.tools.module_loader#just_load_modules) | This one differs from the above in that we don't yield anything, just load all the modules. |
| [`flytekit.tools.module_loader.load_object_from_module()`](flytekit.tools.module_loader#load_object_from_module) | TODO: Handle corner cases, like where the first part is [] maybe. |
| [`flytekit.tools.module_loader.module_load_error_handler()`](flytekit.tools.module_loader#module_load_error_handler) |  |
| [`flytekit.tools.repo.find_common_root()`](flytekit.tools.repo#find_common_root) | Given an arbitrary list of folders and files, this function will use the script mode function to walk up. |
| [`flytekit.tools.repo.list_packages_and_modules()`](flytekit.tools.repo#list_packages_and_modules) | This is a helper function that returns the input list of python packages/modules as a dot delinated list. |
| [`flytekit.tools.repo.package()`](flytekit.tools.repo#package) | Package the given entities and the source code (if fast is enabled) into a package with the given name in output. |
| [`flytekit.tools.repo.print_registration_status()`](flytekit.tools.repo#print_registration_status) |  |
| [`flytekit.tools.repo.register()`](flytekit.tools.repo#register) | Temporarily, for fast register, specify both the fast arg as well as copy_style. |
| [`flytekit.tools.repo.serialize_and_package()`](flytekit.tools.repo#serialize_and_package) | Fist serialize and then package all entities. |
| [`flytekit.tools.repo.serialize_get_control_plane_entities()`](flytekit.tools.repo#serialize_get_control_plane_entities) | See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}} to match the trailing index in the file name with the. |
| [`flytekit.tools.repo.serialize_load_only()`](flytekit.tools.repo#serialize_load_only) | See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}} to match the trailing index in the file name with the. |
| [`flytekit.tools.repo.serialize_to_folder()`](flytekit.tools.repo#serialize_to_folder) | Serialize the given set of python packages to a folder. |
| [`flytekit.tools.script_mode.add_imported_modules_from_source()`](flytekit.tools.script_mode#add_imported_modules_from_source) | Copies modules into destination that are in modules. |
| [`flytekit.tools.script_mode.compress_scripts()`](flytekit.tools.script_mode#compress_scripts) | Compresses the single script while maintaining the folder structure for that file. |
| [`flytekit.tools.script_mode.get_all_modules()`](flytekit.tools.script_mode#get_all_modules) | Import python file with module_name in source_path and return all modules. |
| [`flytekit.tools.script_mode.list_all_files()`](flytekit.tools.script_mode#list_all_files) |  |
| [`flytekit.tools.script_mode.list_imported_modules_as_files()`](flytekit.tools.script_mode#list_imported_modules_as_files) | Copies modules into destination that are in modules. |
| [`flytekit.tools.script_mode.ls_files()`](flytekit.tools.script_mode#ls_files) | user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the. |
| [`flytekit.tools.script_mode.tar_strip_file_attributes()`](flytekit.tools.script_mode#tar_strip_file_attributes) |  |
| [`flytekit.tools.serialize_helpers.get_registrable_entities()`](flytekit.tools.serialize_helpers#get_registrable_entities) | Returns all entities that can be serialized and should be sent over to Flyte backend. |
| [`flytekit.tools.serialize_helpers.persist_registrable_entities()`](flytekit.tools.serialize_helpers#persist_registrable_entities) | For protobuf serializable list of entities, writes a file with the name if the entity and. |
| [`flytekit.tools.subprocess.check_call()`](flytekit.tools.subprocess#check_call) |  |
| [`flytekit.tools.translator.gather_dependent_entities()`](flytekit.tools.translator#gather_dependent_entities) | The ``get_serializable`` function above takes in an ``OrderedDict`` that helps keep track of dependent entities. |
| [`flytekit.tools.translator.get_command_prefix_for_fast_execute()`](flytekit.tools.translator#get_command_prefix_for_fast_execute) |  |
| [`flytekit.tools.translator.get_reference_spec()`](flytekit.tools.translator#get_reference_spec) |  |
| [`flytekit.tools.translator.get_serializable()`](flytekit.tools.translator#get_serializable) | The flytekit authoring code produces objects representing Flyte entities (tasks, workflows, etc. |
| [`flytekit.tools.translator.get_serializable_array_node()`](flytekit.tools.translator#get_serializable_array_node) |  |
| [`flytekit.tools.translator.get_serializable_array_node_map_task()`](flytekit.tools.translator#get_serializable_array_node_map_task) |  |
| [`flytekit.tools.translator.get_serializable_branch_node()`](flytekit.tools.translator#get_serializable_branch_node) |  |
| [`flytekit.tools.translator.get_serializable_flyte_task()`](flytekit.tools.translator#get_serializable_flyte_task) | TODO replace with deep copy. |
| [`flytekit.tools.translator.get_serializable_flyte_workflow()`](flytekit.tools.translator#get_serializable_flyte_workflow) | TODO replace with deep copy. |
| [`flytekit.tools.translator.get_serializable_launch_plan()`](flytekit.tools.translator#get_serializable_launch_plan) |  |
| [`flytekit.tools.translator.get_serializable_node()`](flytekit.tools.translator#get_serializable_node) |  |
| [`flytekit.tools.translator.get_serializable_task()`](flytekit.tools.translator#get_serializable_task) |  |
| [`flytekit.tools.translator.get_serializable_workflow()`](flytekit.tools.translator#get_serializable_workflow) |  |
| [`flytekit.tools.translator.prefix_with_fast_execute()`](flytekit.tools.translator#prefix_with_fast_execute) |  |
| [`flytekit.tools.translator.to_serializable_case()`](flytekit.tools.translator#to_serializable_case) |  |
| [`flytekit.tools.translator.to_serializable_cases()`](flytekit.tools.translator#to_serializable_cases) |  |
| [`flytekit.types.directory.types.noop()`](flytekit.types.directory.types#noop) |  |
| [`flytekit.types.file.file.noop()`](flytekit.types.file.file#noop) |  |
| [`flytekit.types.numpy.ndarray.extract_metadata()`](flytekit.types.numpy.ndarray#extract_metadata) |  |
| [`flytekit.types.schema.types.generate_ordered_files()`](flytekit.types.schema.types#generate_ordered_files) |  |
| [`flytekit.types.structured.lazy_import_structured_dataset_handler()`](flytekit.types.structured#lazy_import_structured_dataset_handler) |  |
| [`flytekit.types.structured.basic_dfs.get_pandas_storage_options()`](flytekit.types.structured.basic_dfs#get_pandas_storage_options) |  |
| [`flytekit.types.structured.snowflake.get_private_key()`](flytekit.types.structured.snowflake#get_private_key) |  |
| [`flytekit.types.structured.structured_dataset.convert_schema_type_to_structured_dataset_type()`](flytekit.types.structured.structured_dataset#convert_schema_type_to_structured_dataset_type) |  |
| [`flytekit.types.structured.structured_dataset.extract_cols_and_format()`](flytekit.types.structured.structured_dataset#extract_cols_and_format) | Helper function, just used to iterate through Annotations and extract out the following information:. |
| [`flytekit.types.structured.structured_dataset.flatten_dict()`](flytekit.types.structured.structured_dataset#flatten_dict) |  |
| [`flytekit.types.structured.structured_dataset.get_supported_types()`](flytekit.types.structured.structured_dataset#get_supported_types) |  |
| [`flytekit.utils.dict_formatter.format_dict()`](flytekit.utils.dict_formatter#format_dict) | Recursively update a dictionary with format strings with values from another dictionary where the keys match. |
| [`flytekit.utils.dict_formatter.get_nested_value()`](flytekit.utils.dict_formatter#get_nested_value) | Retrieve the nested value from a dictionary based on a list of keys. |
| [`flytekit.utils.dict_formatter.replace_placeholder()`](flytekit.utils.dict_formatter#replace_placeholder) | Replace a placeholder in the original string and handle the specific logic for the sagemaker service and idempotence token. |
| [`flytekit.utils.pbhash.compute_hash()`](flytekit.utils.pbhash#compute_hash) | Computes a deterministic hash in bytes for the Protobuf object. |
| [`flytekit.utils.pbhash.compute_hash_string()`](flytekit.utils.pbhash#compute_hash_string) | Computes a deterministic hash in base64 encoded string for the Protobuf object. |

### Packages

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
| [`flytekit.clients.grpc_utils.deadline_interceptor`](flytekit.clients.grpc_utils.deadline_interceptor) |  |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor`](flytekit.clients.grpc_utils.default_metadata_interceptor) |  |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor`](flytekit.clients.grpc_utils.wrap_exception_interceptor) |  |
| [`flytekit.clients.helpers`](flytekit.clients.helpers) |  |
| [`flytekit.clients.raw`](flytekit.clients.raw) |  |
| [`flytekit.clis.helpers`](flytekit.clis.helpers) |  |
| [`flytekit.clis.sdk_in_container.backfill`](flytekit.clis.sdk_in_container.backfill) |  |
| [`flytekit.clis.sdk_in_container.build`](flytekit.clis.sdk_in_container.build) |  |
| [`flytekit.clis.sdk_in_container.constants`](flytekit.clis.sdk_in_container.constants) |  |
| [`flytekit.clis.sdk_in_container.executions`](flytekit.clis.sdk_in_container.executions) |  |
| [`flytekit.clis.sdk_in_container.helpers`](flytekit.clis.sdk_in_container.helpers) |  |
| [`flytekit.clis.sdk_in_container.metrics`](flytekit.clis.sdk_in_container.metrics) |  |
| [`flytekit.clis.sdk_in_container.package`](flytekit.clis.sdk_in_container.package) |  |
| [`flytekit.clis.sdk_in_container.pyflyte`](flytekit.clis.sdk_in_container.pyflyte) |  |
| [`flytekit.clis.sdk_in_container.run`](flytekit.clis.sdk_in_container.run) |  |
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
| [`flytekit.constants`](flytekit.constants) |  |
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
| [`flytekit.core.context_manager`](flytekit.core.context_manager) | These classes provide functionality related context management. |
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
| [`flytekit.core.schedule`](flytekit.core.schedule) | These classes provide functionality related to schedules. |
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
| [`flytekit.extend.backend.connector_service`](flytekit.extend.backend.connector_service) |  |
| [`flytekit.extend.backend.utils`](flytekit.extend.backend.utils) |  |
| [`flytekit.extras.accelerators`](flytekit.extras.accelerators) | ## Specifying Accelerators. |
| [`flytekit.extras.cloud_pickle_resolver`](flytekit.extras.cloud_pickle_resolver) |  |
| [`flytekit.extras.pydantic_transformer.transformer`](flytekit.extras.pydantic_transformer.transformer) |  |
| [`flytekit.extras.sklearn.native`](flytekit.extras.sklearn.native) |  |
| [`flytekit.extras.sqlite3.task`](flytekit.extras.sqlite3.task) |  |
| [`flytekit.extras.tasks.shell`](flytekit.extras.tasks.shell) |  |
| [`flytekit.extras.webhook`](flytekit.extras.webhook) |  |
| [`flytekit.extras.webhook.connector`](flytekit.extras.webhook.connector) |  |
| [`flytekit.extras.webhook.constants`](flytekit.extras.webhook.constants) |  |
| [`flytekit.extras.webhook.task`](flytekit.extras.webhook.task) |  |
| [`flytekit.image_spec.default_builder`](flytekit.image_spec.default_builder) |  |
| [`flytekit.image_spec.image_spec`](flytekit.image_spec.image_spec) |  |
| [`flytekit.image_spec.noop_builder`](flytekit.image_spec.noop_builder) |  |
| [`flytekit.interaction.click_types`](flytekit.interaction.click_types) |  |
| [`flytekit.interaction.parse_stdin`](flytekit.interaction.parse_stdin) |  |
| [`flytekit.interaction.rich_utils`](flytekit.interaction.rich_utils) |  |
| [`flytekit.interaction.string_literals`](flytekit.interaction.string_literals) |  |
| [`flytekit.interactive`](flytekit.interactive) | This module provides functionality related to Flytekit Interactive. |
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
| [`flytekit.models.concurrency`](flytekit.models.concurrency) |  |
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
| [`flytekit.types.file`](flytekit.types.file) | This module provides functionality related to FlyteFile. |
| [`flytekit.types.file.file`](flytekit.types.file.file) |  |
| [`flytekit.types.file.image`](flytekit.types.file.image) |  |
| [`flytekit.types.iterator.iterator`](flytekit.types.iterator.iterator) |  |
| [`flytekit.types.iterator.json_iterator`](flytekit.types.iterator.json_iterator) |  |
| [`flytekit.types.numpy.ndarray`](flytekit.types.numpy.ndarray) |  |
| [`flytekit.types.pickle.pickle`](flytekit.types.pickle.pickle) |  |
| [`flytekit.types.schema.types`](flytekit.types.schema.types) |  |
| [`flytekit.types.schema.types_pandas`](flytekit.types.schema.types_pandas) |  |
| [`flytekit.types.structured`](flytekit.types.structured) |  |
| [`flytekit.types.structured.basic_dfs`](flytekit.types.structured.basic_dfs) |  |
| [`flytekit.types.structured.bigquery`](flytekit.types.structured.bigquery) |  |
| [`flytekit.types.structured.snowflake`](flytekit.types.structured.snowflake) |  |
| [`flytekit.types.structured.structured_dataset`](flytekit.types.structured.structured_dataset) |  |
| [`flytekit.utils.asyn`](flytekit.utils.asyn) | Manages an async event loop on another thread. |
| [`flytekit.utils.dict_formatter`](flytekit.utils.dict_formatter) |  |
| [`flytekit.utils.pbhash`](flytekit.utils.pbhash) |  |
| [`flytekit.utils.rate_limiter`](flytekit.utils.rate_limiter) |  |

