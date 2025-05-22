---
title: Classes
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flytekit.clients.auth.auth_client.AuthorizationClient`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationclient) |Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`flytekit.clients.auth.auth_client.AuthorizationCode`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationcode) | |
| [`flytekit.clients.auth.auth_client.EndpointMetadata`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientendpointmetadata) |This class can be used to control the rendering of the page on login successful or failure. |
| [`flytekit.clients.auth.auth_client.OAuthCallbackHandler`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthcallbackhandler) |A simple wrapper around BaseHTTPServer. |
| [`flytekit.clients.auth.auth_client.OAuthHTTPServer`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthhttpserver) |A simple wrapper around the BaseHTTPServer. |
| [`flytekit.clients.auth.authenticator.Authenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticator) |Base authenticator for all authentication flows. |
| [`flytekit.clients.auth.authenticator.ClientConfig`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfig) |Client Configuration that is needed by the authenticator. |
| [`flytekit.clients.auth.authenticator.ClientConfigStore`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfigstore) |Client Config store retrieve client config. |
| [`flytekit.clients.auth.authenticator.ClientCredentialsAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientcredentialsauthenticator) |This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`flytekit.clients.auth.authenticator.CommandAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcommandauthenticator) |This Authenticator retrieves access_token using the provided command. |
| [`flytekit.clients.auth.authenticator.DeviceCodeAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatordevicecodeauthenticator) |This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`flytekit.clients.auth.authenticator.PKCEAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorpkceauthenticator) |This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`flytekit.clients.auth.authenticator.StaticClientConfigStore`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorstaticclientconfigstore) |Client Config store retrieve client config. |
| [`flytekit.clients.auth.exceptions.AccessTokenNotFoundError`](../packages/flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsaccesstokennotfounderror) |This error is raised with Access token is not found or if Refreshing the token fails. |
| [`flytekit.clients.auth.exceptions.AuthenticationError`](../packages/flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsauthenticationerror) |This is raised for any AuthenticationError. |
| [`flytekit.clients.auth.exceptions.AuthenticationPending`](../packages/flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsauthenticationpending) |This is raised if the token endpoint returns authentication pending. |
| [`flytekit.clients.auth.keyring.Credentials`](../packages/flytekit.clients.auth.keyring#flytekitclientsauthkeyringcredentials) |Stores the credentials together. |
| [`flytekit.clients.auth.keyring.KeyringStore`](../packages/flytekit.clients.auth.keyring#flytekitclientsauthkeyringkeyringstore) |Methods to access Keyring Store. |
| [`flytekit.clients.auth.token_client.DeviceCodeResponse`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdevicecoderesponse) |Response from device auth flow endpoint. |
| [`flytekit.clients.auth_helper.AuthenticationHTTPAdapter`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticationhttpadapter) |A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`flytekit.clients.auth_helper.RemoteClientConfigStore`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperremoteclientconfigstore) |This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |
| [`flytekit.clients.friendly.SynchronousFlyteClient`](../packages/flytekit.clients.friendly#flytekitclientsfriendlysynchronousflyteclient) |This is a low-level client that users can use to make direct gRPC service calls to the control plane. |
| [`flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor`](../packages/flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthunaryinterceptor) |This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor.DefaultMetadataInterceptor`](../packages/flytekit.clients.grpc_utils.default_metadata_interceptor#flytekitclientsgrpc_utilsdefault_metadata_interceptordefaultmetadatainterceptor) |Affords intercepting unary-unary invocations. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.RetryExceptionWrapperInterceptor`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorretryexceptionwrapperinterceptor) |Affords intercepting unary-unary invocations. |
| [`flytekit.clients.raw.RawSynchronousFlyteClient`](../packages/flytekit.clients.raw#flytekitclientsrawrawsynchronousflyteclient) |This is a thin synchronous wrapper around the auto-generated GRPC stubs for communicating with the admin service. |
| [`flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilserrorhandlingcommand) |Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`flytekit.clis.sdk_in_container.utils.PyFlyteParams`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspyflyteparams) | |
| [`flytekit.configuration.AzureBlobStorageConfig`](../packages/flytekit.configuration#flytekitconfigurationazureblobstorageconfig) |Any Azure Blob Storage specific configuration. |
| [`flytekit.configuration.Config`](../packages/flytekit.configuration#flytekitconfigurationconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.configuration.DataConfig`](../packages/flytekit.configuration#flytekitconfigurationdataconfig) |Any data storage specific configuration. |
| [`flytekit.configuration.EntrypointSettings`](../packages/flytekit.configuration#flytekitconfigurationentrypointsettings) |This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`flytekit.configuration.FastSerializationSettings`](../packages/flytekit.configuration#flytekitconfigurationfastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.configuration.GCSConfig`](../packages/flytekit.configuration#flytekitconfigurationgcsconfig) |Any GCS specific configuration. |
| [`flytekit.configuration.GenericPersistenceConfig`](../packages/flytekit.configuration#flytekitconfigurationgenericpersistenceconfig) |Data storage configuration that applies across any provider. |
| [`flytekit.configuration.Image`](../packages/flytekit.configuration#flytekitconfigurationimage) |Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.configuration.ImageConfig`](../packages/flytekit.configuration#flytekitconfigurationimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.configuration.LocalConfig`](../packages/flytekit.configuration#flytekitconfigurationlocalconfig) |Any configuration specific to local runs. |
| [`flytekit.configuration.PlatformConfig`](../packages/flytekit.configuration#flytekitconfigurationplatformconfig) |This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.configuration.S3Config`](../packages/flytekit.configuration#flytekitconfigurations3config) |S3 specific configuration. |
| [`flytekit.configuration.SecretsConfig`](../packages/flytekit.configuration#flytekitconfigurationsecretsconfig) |Configuration for secrets. |
| [`flytekit.configuration.SerializationSettings`](../packages/flytekit.configuration#flytekitconfigurationserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.configuration.StatsConfig`](../packages/flytekit.configuration#flytekitconfigurationstatsconfig) |Configuration for sending statsd. |
| [`flytekit.configuration.default_images.DefaultImages`](../packages/flytekit.configuration.default_images#flytekitconfigurationdefault_imagesdefaultimages) |We may want to load the default images from remote - maybe s3 location etc?. |
| [`flytekit.configuration.feature_flags.FeatureFlags`](../packages/flytekit.configuration.feature_flags#flytekitconfigurationfeature_flagsfeatureflags) | |
| [`flytekit.configuration.file.ConfigEntry`](../packages/flytekit.configuration.file#flytekitconfigurationfileconfigentry) |A top level Config entry holder, that holds multiple different representations of the config. |
| [`flytekit.configuration.file.ConfigFile`](../packages/flytekit.configuration.file#flytekitconfigurationfileconfigfile) | |
| [`flytekit.configuration.file.LegacyConfigEntry`](../packages/flytekit.configuration.file#flytekitconfigurationfilelegacyconfigentry) |Creates a record for the config entry. |
| [`flytekit.configuration.file.YamlConfigEntry`](../packages/flytekit.configuration.file#flytekitconfigurationfileyamlconfigentry) |Creates a record for the config entry. |
| [`flytekit.configuration.internal.AWS`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalaws) | |
| [`flytekit.configuration.internal.AZURE`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalazure) | |
| [`flytekit.configuration.internal.Credentials`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalcredentials) | |
| [`flytekit.configuration.internal.GCP`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalgcp) | |
| [`flytekit.configuration.internal.Images`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalimages) | |
| [`flytekit.configuration.internal.Local`](../packages/flytekit.configuration.internal#flytekitconfigurationinternallocal) | |
| [`flytekit.configuration.internal.LocalSDK`](../packages/flytekit.configuration.internal#flytekitconfigurationinternallocalsdk) | |
| [`flytekit.configuration.internal.Persistence`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalpersistence) | |
| [`flytekit.configuration.internal.Platform`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalplatform) | |
| [`flytekit.configuration.internal.Secrets`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalsecrets) | |
| [`flytekit.configuration.internal.StatsD`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalstatsd) | |
| [`flytekit.configuration.plugin.FlytekitPlugin`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginflytekitplugin) | |
| [`flytekit.configuration.plugin.FlytekitPluginProtocol`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginflytekitpluginprotocol) |Base class for protocol classes. |
| [`flytekit.core.annotation.FlyteAnnotation`](../packages/flytekit.core.annotation#flytekitcoreannotationflyteannotation) |A core object to add arbitrary annotations to flyte types. |
| [`flytekit.core.array_node.ArrayNode`](../packages/flytekit.core.array_node#flytekitcorearray_nodearraynode) | |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTask`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskarraynodemaptask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTaskResolver`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskarraynodemaptaskresolver) |Special resolver that is used for ArrayNodeMapTasks. |
| [`flytekit.core.artifact.Artifact`](../packages/flytekit.core.artifact#flytekitcoreartifactartifact) |An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.core.artifact.ArtifactIDSpecification`](../packages/flytekit.core.artifact#flytekitcoreartifactartifactidspecification) |This is a special object that helps specify how Artifacts are to be created. |
| [`flytekit.core.artifact.ArtifactQuery`](../packages/flytekit.core.artifact#flytekitcoreartifactartifactquery) | |
| [`flytekit.core.artifact.ArtifactSerializationHandler`](../packages/flytekit.core.artifact#flytekitcoreartifactartifactserializationhandler) |This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`flytekit.core.artifact.DefaultArtifactSerializationHandler`](../packages/flytekit.core.artifact#flytekitcoreartifactdefaultartifactserializationhandler) |This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`flytekit.core.artifact.InputsBase`](../packages/flytekit.core.artifact#flytekitcoreartifactinputsbase) |A class to provide better partition semantics. |
| [`flytekit.core.artifact.Partition`](../packages/flytekit.core.artifact#flytekitcoreartifactpartition) | |
| [`flytekit.core.artifact.Partitions`](../packages/flytekit.core.artifact#flytekitcoreartifactpartitions) | |
| [`flytekit.core.artifact.Serializer`](../packages/flytekit.core.artifact#flytekitcoreartifactserializer) | |
| [`flytekit.core.artifact.TimePartition`](../packages/flytekit.core.artifact#flytekitcoreartifacttimepartition) | |
| [`flytekit.core.base_sql_task.SQLTask`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_tasksqltask) |Base task types for all SQL tasks. |
| [`flytekit.core.base_task.IgnoreOutputs`](../packages/flytekit.core.base_task#flytekitcorebase_taskignoreoutputs) |This exception should be used to indicate that the outputs generated by this can be safely ignored. |
| [`flytekit.core.base_task.PythonTask`](../packages/flytekit.core.base_task#flytekitcorebase_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.base_task.Task`](../packages/flytekit.core.base_task#flytekitcorebase_tasktask) |The base of all Tasks in flytekit. |
| [`flytekit.core.base_task.TaskMetadata`](../packages/flytekit.core.base_task#flytekitcorebase_tasktaskmetadata) |Metadata for a Task. |
| [`flytekit.core.base_task.TaskResolverMixin`](../packages/flytekit.core.base_task#flytekitcorebase_tasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.cache.Cache`](../packages/flytekit.core.cache#flytekitcorecachecache) |Cache configuration for a task. |
| [`flytekit.core.cache.CachePolicy`](../packages/flytekit.core.cache#flytekitcorecachecachepolicy) |Base class for protocol classes. |
| [`flytekit.core.cache.VersionParameters`](../packages/flytekit.core.cache#flytekitcorecacheversionparameters) |Parameters used for version hash generation. |
| [`flytekit.core.checkpointer.Checkpoint`](../packages/flytekit.core.checkpointer#flytekitcorecheckpointercheckpoint) |Base class for Checkpoint system. |
| [`flytekit.core.checkpointer.SyncCheckpoint`](../packages/flytekit.core.checkpointer#flytekitcorecheckpointersynccheckpoint) |This class is NOT THREAD-SAFE!. |
| [`flytekit.core.class_based_resolver.ClassStorageTaskResolver`](../packages/flytekit.core.class_based_resolver#flytekitcoreclass_based_resolverclassstoragetaskresolver) |Stores tasks inside a class variable. |
| [`flytekit.core.condition.BranchNode`](../packages/flytekit.core.condition#flytekitcoreconditionbranchnode) | |
| [`flytekit.core.condition.Case`](../packages/flytekit.core.condition#flytekitcoreconditioncase) | |
| [`flytekit.core.condition.Condition`](../packages/flytekit.core.condition#flytekitcoreconditioncondition) | |
| [`flytekit.core.condition.ConditionalSection`](../packages/flytekit.core.condition#flytekitcoreconditionconditionalsection) |ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.condition.LocalExecutedConditionalSection`](../packages/flytekit.core.condition#flytekitcoreconditionlocalexecutedconditionalsection) |ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.condition.SkippedConditionalSection`](../packages/flytekit.core.condition#flytekitcoreconditionskippedconditionalsection) |This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |
| [`flytekit.core.container_task.ContainerTask`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskcontainertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flytekit.core.context_manager.CompilationState`](../packages/flytekit.core.context_manager#flytekitcorecontext_managercompilationstate) |Compilation state is used during the compilation of a workflow or task. |
| [`flytekit.core.context_manager.ExecutionParameters`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.context_manager.ExecutionState`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.context_manager.FlyteContext`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.context_manager.FlyteContextManager`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.context_manager.FlyteEntities`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerflyteentities) |This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.context_manager.OutputMetadata`](../packages/flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadata) | |
| [`flytekit.core.context_manager.OutputMetadataTracker`](../packages/flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadatatracker) |This class is for the users to set arbitrary metadata on output literals. |
| [`flytekit.core.context_manager.SecretsManager`](../packages/flytekit.core.context_manager#flytekitcorecontext_managersecretsmanager) |This provides a secrets resolution logic at runtime. |
| [`flytekit.core.context_manager.SerializableToString`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerserializabletostring) |This protocol is used by the Artifact create_from function. |
| [`flytekit.core.data_persistence.FileAccessProvider`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistencefileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.core.docstring.Docstring`](../packages/flytekit.core.docstring#flytekitcoredocstringdocstring) | |
| [`flytekit.core.environment.Environment`](../packages/flytekit.core.environment#flytekitcoreenvironmentenvironment) | |
| [`flytekit.core.gate.Gate`](../packages/flytekit.core.gate#flytekitcoregategate) |A node type that waits for user input before proceeding with a workflow. |
| [`flytekit.core.hash.HashMethod`](../packages/flytekit.core.hash#flytekitcorehashhashmethod) |Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.core.hash.HashOnReferenceMixin`](../packages/flytekit.core.hash#flytekitcorehashhashonreferencemixin) | |
| [`flytekit.core.interface.Interface`](../packages/flytekit.core.interface#flytekitcoreinterfaceinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.launch_plan.LaunchPlan`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planlaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.launch_plan.ReferenceLaunchPlan`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planreferencelaunchplan) |A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.core.legacy_map_task.MapPythonTask`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmappythontask) |A MapPythonTask defines a {{< py_class_ref flytekit.PythonTask >}} which specifies how to run. |
| [`flytekit.core.legacy_map_task.MapTaskResolver`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmaptaskresolver) |Special resolver that is used for MapTasks. |
| [`flytekit.core.local_cache.LocalTaskCache`](../packages/flytekit.core.local_cache#flytekitcorelocal_cachelocaltaskcache) |This class implements a persistent store able to cache the result of local task executions. |
| [`flytekit.core.local_fsspec.FlyteLocalFileSystem`](../packages/flytekit.core.local_fsspec#flytekitcorelocal_fsspecflytelocalfilesystem) |This class doesn't do anything except override the separator so that it works on windows. |
| [`flytekit.core.mock_stats.MockStats`](../packages/flytekit.core.mock_stats#flytekitcoremock_statsmockstats) | |
| [`flytekit.core.node.Node`](../packages/flytekit.core.node#flytekitcorenodenode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.notification.Email`](../packages/flytekit.core.notification#flytekitcorenotificationemail) |This notification should be used when sending regular emails to people. |
| [`flytekit.core.notification.Notification`](../packages/flytekit.core.notification#flytekitcorenotificationnotification) | |
| [`flytekit.core.notification.PagerDuty`](../packages/flytekit.core.notification#flytekitcorenotificationpagerduty) |This notification should be used when sending emails to the PagerDuty service. |
| [`flytekit.core.notification.Slack`](../packages/flytekit.core.notification#flytekitcorenotificationslack) |This notification should be used when sending emails to the Slack. |
| [`flytekit.core.options.Options`](../packages/flytekit.core.options#flytekitcoreoptionsoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.core.pod_template.PodTemplate`](../packages/flytekit.core.pod_template#flytekitcorepod_templatepodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.promise.ComparisonExpression`](../packages/flytekit.core.promise#flytekitcorepromisecomparisonexpression) |ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`flytekit.core.promise.ConjunctionExpression`](../packages/flytekit.core.promise#flytekitcorepromiseconjunctionexpression) |A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`flytekit.core.promise.HasFlyteInterface`](../packages/flytekit.core.promise#flytekitcorepromisehasflyteinterface) |Base class for protocol classes. |
| [`flytekit.core.promise.LocallyExecutable`](../packages/flytekit.core.promise#flytekitcorepromiselocallyexecutable) |Base class for protocol classes. |
| [`flytekit.core.promise.NodeOutput`](../packages/flytekit.core.promise#flytekitcorepromisenodeoutput) | |
| [`flytekit.core.promise.Promise`](../packages/flytekit.core.promise#flytekitcorepromisepromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.promise.SupportsNodeCreation`](../packages/flytekit.core.promise#flytekitcorepromisesupportsnodecreation) |Base class for protocol classes. |
| [`flytekit.core.promise.VoidPromise`](../packages/flytekit.core.promise#flytekitcorepromisevoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.python_auto_container.DefaultNotebookTaskResolver`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaultnotebooktaskresolver) |This resolved is used when the task is defined in a notebook. |
| [`flytekit.core.python_auto_container.DefaultTaskResolver`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaulttaskresolver) |Please see the notes in the TaskResolverMixin as it describes this default behavior. |
| [`flytekit.core.python_auto_container.PickledEntity`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentity) |Represents the structure of the pickled object stored in the. |
| [`flytekit.core.python_auto_container.PickledEntityMetadata`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentitymetadata) |Metadata for a pickled entity containing version information. |
| [`flytekit.core.python_auto_container.PythonAutoContainerTask`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_customized_container_task.PythonCustomizedContainerTask`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskpythoncustomizedcontainertask) |Please take a look at the comments for {{< py_class_ref flytekit.extend.ExecutableTemplateShimTask >}} as well. |
| [`flytekit.core.python_customized_container_task.TaskTemplateResolver`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktasktemplateresolver) |This is a special resolver that resolves the task above at execution time, using only the ``TaskTemplate``,. |
| [`flytekit.core.python_function_task.AsyncPythonFunctionTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskasyncpythonfunctiontask) |This is the base task for eager tasks, as well as normal async tasks. |
| [`flytekit.core.python_function_task.EagerAsyncPythonFunctionTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerasyncpythonfunctiontask) |This is the base eager task (aka eager workflow) type. |
| [`flytekit.core.python_function_task.EagerFailureHandlerTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerfailurehandlertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_function_task.EagerFailureTaskResolver`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerfailuretaskresolver) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.python_function_task.PythonFunctionTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.python_function_task.PythonInstanceTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpythoninstancetask) |This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.core.reference_entity.LaunchPlanReference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitylaunchplanreference) |A reference object containing metadata that points to a remote launch plan. |
| [`flytekit.core.reference_entity.Reference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreference) | |
| [`flytekit.core.reference_entity.ReferenceEntity`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreferenceentity) | |
| [`flytekit.core.reference_entity.ReferenceSpec`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreferencespec) | |
| [`flytekit.core.reference_entity.ReferenceTemplate`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreferencetemplate) | |
| [`flytekit.core.reference_entity.TaskReference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitytaskreference) |A reference object containing metadata that points to a remote task. |
| [`flytekit.core.reference_entity.WorkflowReference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityworkflowreference) |A reference object containing metadata that points to a remote workflow. |
| [`flytekit.core.resources.ResourceSpec`](../packages/flytekit.core.resources#flytekitcoreresourcesresourcespec) | |
| [`flytekit.core.resources.Resources`](../packages/flytekit.core.resources#flytekitcoreresourcesresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.schedule.CronSchedule`](../packages/flytekit.core.schedule#flytekitcoreschedulecronschedule) |Use this when you have a launch plan that you want to run on a cron expression. |
| [`flytekit.core.schedule.FixedRate`](../packages/flytekit.core.schedule#flytekitcoreschedulefixedrate) |Use this class to schedule a fixed-rate interval for a launch plan. |
| [`flytekit.core.schedule.LaunchPlanTriggerBase`](../packages/flytekit.core.schedule#flytekitcoreschedulelaunchplantriggerbase) |Base class for protocol classes. |
| [`flytekit.core.schedule.OnSchedule`](../packages/flytekit.core.schedule#flytekitcorescheduleonschedule) |Base class for protocol classes. |
| [`flytekit.core.shim_task.ExecutableTemplateShimTask`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskexecutabletemplateshimtask) |The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`flytekit.core.shim_task.ShimTaskExecutor`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskshimtaskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.core.task.Echo`](../packages/flytekit.core.task#flytekitcoretaskecho) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.task.ReferenceTask`](../packages/flytekit.core.task#flytekitcoretaskreferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.task.TaskPlugins`](../packages/flytekit.core.task#flytekitcoretasktaskplugins) |This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |
| [`flytekit.core.tracked_abc.FlyteTrackedABC`](../packages/flytekit.core.tracked_abc#flytekitcoretracked_abcflytetrackedabc) |This class exists because if you try to inherit from abc. |
| [`flytekit.core.tracker.InstanceTrackingMeta`](../packages/flytekit.core.tracker#flytekitcoretrackerinstancetrackingmeta) |Please see the original class :flytekit. |
| [`flytekit.core.tracker.TrackedInstance`](../packages/flytekit.core.tracker#flytekitcoretrackertrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.type_engine.AsyncTypeTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.BatchSize`](../packages/flytekit.core.type_engine#flytekitcoretype_enginebatchsize) |This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`flytekit.core.type_engine.BinaryIOTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginebinaryiotransformer) |Handler for BinaryIO. |
| [`flytekit.core.type_engine.DataclassTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginedataclasstransformer) |The Dataclass Transformer provides a type transformer for dataclasses. |
| [`flytekit.core.type_engine.DictTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginedicttransformer) |Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`flytekit.core.type_engine.EnumTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineenumtransformer) |Enables converting a python type enum. |
| [`flytekit.core.type_engine.ListTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginelisttransformer) |Transformer that handles a univariate typing. |
| [`flytekit.core.type_engine.LiteralsResolver`](../packages/flytekit.core.type_engine#flytekitcoretype_engineliteralsresolver) |LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.core.type_engine.ProtobufTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineprotobuftransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.RestrictedTypeError`](../packages/flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypeerror) |Common base class for all non-exit exceptions. |
| [`flytekit.core.type_engine.RestrictedTypeTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypetransformer) |Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. |
| [`flytekit.core.type_engine.SimpleTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginesimpletransformer) |A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate. |
| [`flytekit.core.type_engine.TextIOTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetextiotransformer) |Handler for TextIO. |
| [`flytekit.core.type_engine.TypeEngine`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.type_engine.TypeTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.TypeTransformerFailedError`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.core.type_engine.UnionTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineuniontransformer) |Transformer that handles a typing. |
| [`flytekit.core.utils.AutoDeletingTempDir`](../packages/flytekit.core.utils#flytekitcoreutilsautodeletingtempdir) |Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`flytekit.core.utils.ClassDecorator`](../packages/flytekit.core.utils#flytekitcoreutilsclassdecorator) |Abstract class for class decorators. |
| [`flytekit.core.utils.Directory`](../packages/flytekit.core.utils#flytekitcoreutilsdirectory) | |
| [`flytekit.core.utils.timeit`](../packages/flytekit.core.utils#flytekitcoreutilstimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.worker_queue.Controller`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuecontroller) |This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint. |
| [`flytekit.core.worker_queue.Update`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueupdate) | |
| [`flytekit.core.worker_queue.WorkItem`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueworkitem) |This is a class to keep track of what the user requested. |
| [`flytekit.core.workflow.ImperativeWorkflow`](../packages/flytekit.core.workflow#flytekitcoreworkflowimperativeworkflow) |An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`flytekit.core.workflow.PythonFunctionWorkflow`](../packages/flytekit.core.workflow#flytekitcoreworkflowpythonfunctionworkflow) |Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`flytekit.core.workflow.ReferenceWorkflow`](../packages/flytekit.core.workflow#flytekitcoreworkflowreferenceworkflow) |A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.core.workflow.WorkflowBase`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowbase) | |
| [`flytekit.core.workflow.WorkflowMetadata`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowmetadata) | |
| [`flytekit.core.workflow.WorkflowMetadataDefaults`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowmetadatadefaults) |This class is similarly named to the one above. |
| [`flytekit.deck.deck.Deck`](../packages/flytekit.deck.deck#flytekitdeckdeckdeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.deck.deck.TimeLineDeck`](../packages/flytekit.deck.deck#flytekitdeckdecktimelinedeck) |The TimeLineDeck class is designed to render the execution time of each part of a task. |
| [`flytekit.deck.renderer.ArrowRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrendererarrowrenderer) |Render an Arrow dataframe as an HTML table. |
| [`flytekit.deck.renderer.MarkdownRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrenderermarkdownrenderer) |Convert a markdown string to HTML and return HTML as a unicode string. |
| [`flytekit.deck.renderer.PythonDependencyRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrendererpythondependencyrenderer) |PythonDependencyDeck is a deck that contains information about packages installed via pip. |
| [`flytekit.deck.renderer.Renderable`](../packages/flytekit.deck.renderer#flytekitdeckrendererrenderable) |Base class for protocol classes. |
| [`flytekit.deck.renderer.SourceCodeRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrenderersourcecoderenderer) |Convert Python source code to HTML, and return HTML as a unicode string. |
| [`flytekit.deck.renderer.TopFrameRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrenderertopframerenderer) |Render a DataFrame as an HTML table. |
| [`flytekit.exceptions.base.FlyteException`](../packages/flytekit.exceptions.base#flytekitexceptionsbaseflyteexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.base.FlyteRecoverableException`](../packages/flytekit.exceptions.base#flytekitexceptionsbaseflyterecoverableexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.eager.EagerException`](../packages/flytekit.exceptions.eager#flytekitexceptionseagereagerexception) |Raised when a node in an eager workflow encounters an error. |
| [`flytekit.exceptions.scopes.FlyteScopedException`](../packages/flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.scopes.FlyteScopedSystemException`](../packages/flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopedsystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.scopes.FlyteScopedUserException`](../packages/flytekit.exceptions.scopes#flytekitexceptionsscopesflytescopeduserexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.system.FlyteAgentNotFound`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflyteagentnotfound) |Assertion failed. |
| [`flytekit.exceptions.system.FlyteConnectorNotFound`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflyteconnectornotfound) |Assertion failed. |
| [`flytekit.exceptions.system.FlyteDownloadDataException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflytedownloaddataexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.system.FlyteEntrypointNotLoadable`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflyteentrypointnotloadable) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.system.FlyteNonRecoverableSystemException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflytenonrecoverablesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.system.FlyteNotImplementedException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflytenotimplementedexception) |Method or function hasn't been implemented yet. |
| [`flytekit.exceptions.system.FlyteSystemAssertion`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflytesystemassertion) |Assertion failed. |
| [`flytekit.exceptions.system.FlyteSystemException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflytesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.system.FlyteSystemUnavailableException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflytesystemunavailableexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.system.FlyteUploadDataException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflyteuploaddataexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteAssertion`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteassertion) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteAuthenticationException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteauthenticationexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteCompilationException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytecompilationexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteDataNotFoundException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytedatanotfoundexception) |Inappropriate argument value (of correct type). |
| [`flytekit.exceptions.user.FlyteDisapprovalException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytedisapprovalexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteEntityAlreadyExistsException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteentityalreadyexistsexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteEntityNotExistException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotexistexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteEntityNotFoundException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteentitynotfoundexception) |Inappropriate argument value (of correct type). |
| [`flytekit.exceptions.user.FlyteFailureNodeInputMismatchException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytefailurenodeinputmismatchexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteInvalidInputException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteinvalidinputexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteMissingReturnValueException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytemissingreturnvalueexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteMissingTypeException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytemissingtypeexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlytePromiseAttributeResolveException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytepromiseattributeresolveexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteRecoverableException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyterecoverableexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteTimeout`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytetimeout) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteTypeException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytetypeexception) |Inappropriate argument type. |
| [`flytekit.exceptions.user.FlyteUserException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteuserexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteUserRuntimeException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflyteuserruntimeexception) |Common base class for all non-exit exceptions. |
| [`flytekit.exceptions.user.FlyteValidationException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytevalidationexception) |Assertion failed. |
| [`flytekit.exceptions.user.FlyteValueException`](../packages/flytekit.exceptions.user#flytekitexceptionsuserflytevalueexception) |Inappropriate argument value (of correct type). |
| [`flytekit.extend.backend.base_connector.AsyncConnectorBase`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorbase) |This is the base class for all async connectors. |
| [`flytekit.extend.backend.base_connector.AsyncConnectorExecutorMixin`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorexecutormixin) |This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.ConnectorBase`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorbase) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.extend.backend.base_connector.ConnectorRegistry`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorregistry) |This is the registry for all connectors. |
| [`flytekit.extend.backend.base_connector.Resource`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresource) |This is the output resource of the job. |
| [`flytekit.extend.backend.base_connector.ResourceMeta`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresourcemeta) |This is the metadata for the job. |
| [`flytekit.extend.backend.base_connector.SyncConnectorBase`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorbase) |This is the base class for all sync connectors. |
| [`flytekit.extend.backend.base_connector.SyncConnectorExecutorMixin`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorexecutormixin) |This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.TaskCategory`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortaskcategory) | |
| [`flytekit.extras.accelerators.BaseAccelerator`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsbaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.extras.accelerators.GPUAccelerator`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsgpuaccelerator) |Class that represents a GPU accelerator. |
| [`flytekit.extras.accelerators.MultiInstanceGPUAccelerator`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsmultiinstancegpuaccelerator) |Base class for all multi-instance GPU accelerator types. |
| [`flytekit.extras.cloud_pickle_resolver.ExperimentalNaiveCloudPickleResolver`](../packages/flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolverexperimentalnaivecloudpickleresolver) |Please do not use this resolver, basically ever. |
| [`flytekit.extras.sqlite3.task.SQLite3Config`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3config) |Use this configuration to configure if sqlite3 files that should be loaded by the task. |
| [`flytekit.extras.sqlite3.task.SQLite3Task`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3task) |Run client side SQLite3 queries that optionally return a FlyteSchema object. |
| [`flytekit.extras.sqlite3.task.SQLite3TaskExecutor`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3taskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.extras.tasks.shell.AttrDict`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellattrdict) |Convert a dictionary to an attribute style lookup. |
| [`flytekit.extras.tasks.shell.OutputLocation`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshelloutputlocation) | |
| [`flytekit.extras.tasks.shell.ProcessResult`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellprocessresult) |Stores a process return code, standard output and standard error. |
| [`flytekit.extras.tasks.shell.RawShellTask`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellrawshelltask) | |
| [`flytekit.extras.tasks.shell.ShellTask`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellshelltask) | |
| [`flytekit.image_spec.default_builder.DefaultImageBuilder`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdefaultimagebuilder) |Image builder using Docker and buildkit. |
| [`flytekit.image_spec.image_spec.ImageBuildEngine`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specimagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.image_spec.image_spec.ImageSpec`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.image_spec.image_spec.ImageSpecBuilder`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespecbuilder) | |
| [`flytekit.interaction.click_types.DateTimeType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdatetimetype) |The DateTime type converts date strings into `datetime` objects. |
| [`flytekit.interaction.click_types.DirParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdirparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.DurationParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdurationparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.EnumParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesenumparamtype) |The choice type allows a value to be checked against a fixed set. |
| [`flytekit.interaction.click_types.FileParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesfileparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.FlyteLiteralConverter`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflyteliteralconverter) | |
| [`flytekit.interaction.click_types.JSONIteratorParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratorparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.JsonParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesjsonparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.PickleParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typespickleparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.StructuredDatasetParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddatasetparamtype) |TODO handle column types. |
| [`flytekit.interaction.click_types.UnionParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesunionparamtype) |A composite type that allows for multiple types to be specified. |
| [`flytekit.interaction.rich_utils.RichCallback`](../packages/flytekit.interaction.rich_utils#flytekitinteractionrich_utilsrichcallback) |Base class and interface for callback mechanism. |
| [`flytekit.interactive.vscode_lib.config.VscodeConfig`](../packages/flytekit.interactive.vscode_lib.config#flytekitinteractivevscode_libconfigvscodeconfig) |VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`flytekit.interactive.vscode_lib.decorator.vscode`](../packages/flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscode) |Abstract class for class decorators. |
| [`flytekit.interfaces.cli_identifiers.Identifier`](../packages/flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersidentifier) | |
| [`flytekit.interfaces.cli_identifiers.TaskExecutionIdentifier`](../packages/flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifierstaskexecutionidentifier) | |
| [`flytekit.interfaces.cli_identifiers.WorkflowExecutionIdentifier`](../packages/flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersworkflowexecutionidentifier) | |
| [`flytekit.interfaces.stats.client.DummyStatsClient`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientdummystatsclient) |A dummy client for statsd. |
| [`flytekit.interfaces.stats.client.ScopeableStatsProxy`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientscopeablestatsproxy) |A Proxy object for an underlying statsd client. |
| [`flytekit.interfaces.stats.client.StatsClientProxy`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsclientproxy) |A Proxy object for an underlying statsd client. |
| [`flytekit.interfaces.stats.taggable.TaggableStats`](../packages/flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggabletaggablestats) |A Proxy object for an underlying statsd client. |
| [`flytekit.models.admin.common.Sort`](../packages/flytekit.models.admin.common#flytekitmodelsadmincommonsort) | |
| [`flytekit.models.admin.task_execution.TaskExecution`](../packages/flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecution) | |
| [`flytekit.models.admin.task_execution.TaskExecutionClosure`](../packages/flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecutionclosure) | |
| [`flytekit.models.admin.workflow.Workflow`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflow) | |
| [`flytekit.models.admin.workflow.WorkflowClosure`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowclosure) | |
| [`flytekit.models.admin.workflow.WorkflowSpec`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowspec) | |
| [`flytekit.models.annotation.TypeAnnotation`](../packages/flytekit.models.annotation#flytekitmodelsannotationtypeannotation) |Python class representation of the flyteidl TypeAnnotation message. |
| [`flytekit.models.array_job.ArrayJob`](../packages/flytekit.models.array_job#flytekitmodelsarray_jobarrayjob) | |
| [`flytekit.models.common.Annotations`](../packages/flytekit.models.common#flytekitmodelscommonannotations) | |
| [`flytekit.models.common.AuthRole`](../packages/flytekit.models.common#flytekitmodelscommonauthrole) | |
| [`flytekit.models.common.EmailNotification`](../packages/flytekit.models.common#flytekitmodelscommonemailnotification) | |
| [`flytekit.models.common.Envs`](../packages/flytekit.models.common#flytekitmodelscommonenvs) | |
| [`flytekit.models.common.FlyteABCMeta`](../packages/flytekit.models.common#flytekitmodelscommonflyteabcmeta) |Metaclass for defining Abstract Base Classes (ABCs). |
| [`flytekit.models.common.FlyteCustomIdlEntity`](../packages/flytekit.models.common#flytekitmodelscommonflytecustomidlentity) | |
| [`flytekit.models.common.FlyteIdlEntity`](../packages/flytekit.models.common#flytekitmodelscommonflyteidlentity) | |
| [`flytekit.models.common.FlyteType`](../packages/flytekit.models.common#flytekitmodelscommonflytetype) |Metaclass for defining Abstract Base Classes (ABCs). |
| [`flytekit.models.common.Labels`](../packages/flytekit.models.common#flytekitmodelscommonlabels) | |
| [`flytekit.models.common.NamedEntityIdentifier`](../packages/flytekit.models.common#flytekitmodelscommonnamedentityidentifier) | |
| [`flytekit.models.common.Notification`](../packages/flytekit.models.common#flytekitmodelscommonnotification) | |
| [`flytekit.models.common.PagerDutyNotification`](../packages/flytekit.models.common#flytekitmodelscommonpagerdutynotification) | |
| [`flytekit.models.common.RawOutputDataConfig`](../packages/flytekit.models.common#flytekitmodelscommonrawoutputdataconfig) | |
| [`flytekit.models.common.SlackNotification`](../packages/flytekit.models.common#flytekitmodelscommonslacknotification) | |
| [`flytekit.models.common.UrlBlob`](../packages/flytekit.models.common#flytekitmodelscommonurlblob) | |
| [`flytekit.models.core.catalog.CatalogArtifactTag`](../packages/flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogartifacttag) | |
| [`flytekit.models.core.catalog.CatalogMetadata`](../packages/flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogmetadata) | |
| [`flytekit.models.core.compiler.CompiledTask`](../packages/flytekit.models.core.compiler#flytekitmodelscorecompilercompiledtask) | |
| [`flytekit.models.core.compiler.CompiledWorkflow`](../packages/flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflow) | |
| [`flytekit.models.core.compiler.CompiledWorkflowClosure`](../packages/flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflowclosure) | |
| [`flytekit.models.core.compiler.ConnectionSet`](../packages/flytekit.models.core.compiler#flytekitmodelscorecompilerconnectionset) | |
| [`flytekit.models.core.condition.BooleanExpression`](../packages/flytekit.models.core.condition#flytekitmodelscoreconditionbooleanexpression) | |
| [`flytekit.models.core.condition.ComparisonExpression`](../packages/flytekit.models.core.condition#flytekitmodelscoreconditioncomparisonexpression) | |
| [`flytekit.models.core.condition.ConjunctionExpression`](../packages/flytekit.models.core.condition#flytekitmodelscoreconditionconjunctionexpression) | |
| [`flytekit.models.core.condition.Operand`](../packages/flytekit.models.core.condition#flytekitmodelscoreconditionoperand) | |
| [`flytekit.models.core.errors.ContainerError`](../packages/flytekit.models.core.errors#flytekitmodelscoreerrorscontainererror) | |
| [`flytekit.models.core.errors.ErrorDocument`](../packages/flytekit.models.core.errors#flytekitmodelscoreerrorserrordocument) | |
| [`flytekit.models.core.execution.ExecutionError`](../packages/flytekit.models.core.execution#flytekitmodelscoreexecutionexecutionerror) | |
| [`flytekit.models.core.execution.NodeExecutionPhase`](../packages/flytekit.models.core.execution#flytekitmodelscoreexecutionnodeexecutionphase) | |
| [`flytekit.models.core.execution.TaskExecutionPhase`](../packages/flytekit.models.core.execution#flytekitmodelscoreexecutiontaskexecutionphase) | |
| [`flytekit.models.core.execution.TaskLog`](../packages/flytekit.models.core.execution#flytekitmodelscoreexecutiontasklog) | |
| [`flytekit.models.core.execution.WorkflowExecutionPhase`](../packages/flytekit.models.core.execution#flytekitmodelscoreexecutionworkflowexecutionphase) |This class holds enum values used for setting notifications. |
| [`flytekit.models.core.identifier.Identifier`](../packages/flytekit.models.core.identifier#flytekitmodelscoreidentifieridentifier) | |
| [`flytekit.models.core.identifier.NodeExecutionIdentifier`](../packages/flytekit.models.core.identifier#flytekitmodelscoreidentifiernodeexecutionidentifier) | |
| [`flytekit.models.core.identifier.ResourceType`](../packages/flytekit.models.core.identifier#flytekitmodelscoreidentifierresourcetype) | |
| [`flytekit.models.core.identifier.SignalIdentifier`](../packages/flytekit.models.core.identifier#flytekitmodelscoreidentifiersignalidentifier) | |
| [`flytekit.models.core.identifier.TaskExecutionIdentifier`](../packages/flytekit.models.core.identifier#flytekitmodelscoreidentifiertaskexecutionidentifier) | |
| [`flytekit.models.core.identifier.WorkflowExecutionIdentifier`](../packages/flytekit.models.core.identifier#flytekitmodelscoreidentifierworkflowexecutionidentifier) | |
| [`flytekit.models.core.types.BlobType`](../packages/flytekit.models.core.types#flytekitmodelscoretypesblobtype) |This type represents offloaded data and is typically used for things like files. |
| [`flytekit.models.core.types.EnumType`](../packages/flytekit.models.core.types#flytekitmodelscoretypesenumtype) |Models _types_pb2. |
| [`flytekit.models.core.workflow.Alias`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowalias) | |
| [`flytekit.models.core.workflow.ApproveCondition`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowapprovecondition) | |
| [`flytekit.models.core.workflow.ArrayNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowarraynode) | |
| [`flytekit.models.core.workflow.BranchNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowbranchnode) | |
| [`flytekit.models.core.workflow.GateNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowgatenode) | |
| [`flytekit.models.core.workflow.IfBlock`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowifblock) | |
| [`flytekit.models.core.workflow.IfElseBlock`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowifelseblock) | |
| [`flytekit.models.core.workflow.Node`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflownode) | |
| [`flytekit.models.core.workflow.NodeMetadata`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflownodemetadata) | |
| [`flytekit.models.core.workflow.SignalCondition`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowsignalcondition) | |
| [`flytekit.models.core.workflow.SleepCondition`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowsleepcondition) | |
| [`flytekit.models.core.workflow.TaskNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknode) | |
| [`flytekit.models.core.workflow.TaskNodeOverrides`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowtasknodeoverrides) | |
| [`flytekit.models.core.workflow.WorkflowMetadata`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadata) | |
| [`flytekit.models.core.workflow.WorkflowMetadataDefaults`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowmetadatadefaults) | |
| [`flytekit.models.core.workflow.WorkflowNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflownode) | |
| [`flytekit.models.core.workflow.WorkflowTemplate`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowworkflowtemplate) | |
| [`flytekit.models.documentation.Description`](../packages/flytekit.models.documentation#flytekitmodelsdocumentationdescription) |Full user description with formatting preserved. |
| [`flytekit.models.documentation.Documentation`](../packages/flytekit.models.documentation#flytekitmodelsdocumentationdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.models.documentation.SourceCode`](../packages/flytekit.models.documentation#flytekitmodelsdocumentationsourcecode) |Link to source code used to define this task or workflow. |
| [`flytekit.models.domain.Domain`](../packages/flytekit.models.domain#flytekitmodelsdomaindomain) |Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |
| [`flytekit.models.dynamic_job.DynamicJobSpec`](../packages/flytekit.models.dynamic_job#flytekitmodelsdynamic_jobdynamicjobspec) | |
| [`flytekit.models.event.TaskExecutionMetadata`](../packages/flytekit.models.event#flytekitmodelseventtaskexecutionmetadata) | |
| [`flytekit.models.execution.AbortMetadata`](../packages/flytekit.models.execution#flytekitmodelsexecutionabortmetadata) | |
| [`flytekit.models.execution.ClusterAssignment`](../packages/flytekit.models.execution#flytekitmodelsexecutionclusterassignment) | |
| [`flytekit.models.execution.Execution`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecution) | |
| [`flytekit.models.execution.ExecutionClosure`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecutionclosure) | |
| [`flytekit.models.execution.ExecutionMetadata`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecutionmetadata) | |
| [`flytekit.models.execution.ExecutionSpec`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecutionspec) | |
| [`flytekit.models.execution.LiteralMapBlob`](../packages/flytekit.models.execution#flytekitmodelsexecutionliteralmapblob) | |
| [`flytekit.models.execution.NodeExecutionGetDataResponse`](../packages/flytekit.models.execution#flytekitmodelsexecutionnodeexecutiongetdataresponse) |Currently, node, task, and workflow execution all have the same get data response. |
| [`flytekit.models.execution.NotificationList`](../packages/flytekit.models.execution#flytekitmodelsexecutionnotificationlist) | |
| [`flytekit.models.execution.SystemMetadata`](../packages/flytekit.models.execution#flytekitmodelsexecutionsystemmetadata) | |
| [`flytekit.models.execution.TaskExecutionGetDataResponse`](../packages/flytekit.models.execution#flytekitmodelsexecutiontaskexecutiongetdataresponse) |Currently, node, task, and workflow execution all have the same get data response. |
| [`flytekit.models.execution.WorkflowExecutionGetDataResponse`](../packages/flytekit.models.execution#flytekitmodelsexecutionworkflowexecutiongetdataresponse) |Currently, node, task, and workflow execution all have the same get data response. |
| [`flytekit.models.filters.Contains`](../packages/flytekit.models.filters#flytekitmodelsfilterscontains) | |
| [`flytekit.models.filters.Equal`](../packages/flytekit.models.filters#flytekitmodelsfiltersequal) | |
| [`flytekit.models.filters.Filter`](../packages/flytekit.models.filters#flytekitmodelsfiltersfilter) | |
| [`flytekit.models.filters.FilterList`](../packages/flytekit.models.filters#flytekitmodelsfiltersfilterlist) | |
| [`flytekit.models.filters.GreaterThan`](../packages/flytekit.models.filters#flytekitmodelsfiltersgreaterthan) | |
| [`flytekit.models.filters.GreaterThanOrEqual`](../packages/flytekit.models.filters#flytekitmodelsfiltersgreaterthanorequal) | |
| [`flytekit.models.filters.LessThan`](../packages/flytekit.models.filters#flytekitmodelsfilterslessthan) | |
| [`flytekit.models.filters.LessThanOrEqual`](../packages/flytekit.models.filters#flytekitmodelsfilterslessthanorequal) | |
| [`flytekit.models.filters.NotEqual`](../packages/flytekit.models.filters#flytekitmodelsfiltersnotequal) | |
| [`flytekit.models.filters.SetFilter`](../packages/flytekit.models.filters#flytekitmodelsfilterssetfilter) | |
| [`flytekit.models.filters.ValueIn`](../packages/flytekit.models.filters#flytekitmodelsfiltersvaluein) | |
| [`flytekit.models.filters.ValueNotIn`](../packages/flytekit.models.filters#flytekitmodelsfiltersvaluenotin) | |
| [`flytekit.models.interface.Parameter`](../packages/flytekit.models.interface#flytekitmodelsinterfaceparameter) | |
| [`flytekit.models.interface.ParameterMap`](../packages/flytekit.models.interface#flytekitmodelsinterfaceparametermap) | |
| [`flytekit.models.interface.TypedInterface`](../packages/flytekit.models.interface#flytekitmodelsinterfacetypedinterface) | |
| [`flytekit.models.interface.Variable`](../packages/flytekit.models.interface#flytekitmodelsinterfacevariable) | |
| [`flytekit.models.interface.VariableMap`](../packages/flytekit.models.interface#flytekitmodelsinterfacevariablemap) | |
| [`flytekit.models.launch_plan.Auth`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planauth) | |
| [`flytekit.models.launch_plan.LaunchPlan`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplan) | |
| [`flytekit.models.launch_plan.LaunchPlanClosure`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanclosure) | |
| [`flytekit.models.launch_plan.LaunchPlanMetadata`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanmetadata) | |
| [`flytekit.models.launch_plan.LaunchPlanSpec`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanspec) | |
| [`flytekit.models.launch_plan.LaunchPlanState`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planlaunchplanstate) | |
| [`flytekit.models.literals.Binary`](../packages/flytekit.models.literals#flytekitmodelsliteralsbinary) | |
| [`flytekit.models.literals.Binding`](../packages/flytekit.models.literals#flytekitmodelsliteralsbinding) | |
| [`flytekit.models.literals.BindingData`](../packages/flytekit.models.literals#flytekitmodelsliteralsbindingdata) | |
| [`flytekit.models.literals.BindingDataCollection`](../packages/flytekit.models.literals#flytekitmodelsliteralsbindingdatacollection) | |
| [`flytekit.models.literals.BindingDataMap`](../packages/flytekit.models.literals#flytekitmodelsliteralsbindingdatamap) | |
| [`flytekit.models.literals.Blob`](../packages/flytekit.models.literals#flytekitmodelsliteralsblob) | |
| [`flytekit.models.literals.BlobMetadata`](../packages/flytekit.models.literals#flytekitmodelsliteralsblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.models.literals.Literal`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteral) | |
| [`flytekit.models.literals.LiteralCollection`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteralcollection) | |
| [`flytekit.models.literals.LiteralMap`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteralmap) | |
| [`flytekit.models.literals.LiteralOffloadedMetadata`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteraloffloadedmetadata) | |
| [`flytekit.models.literals.Primitive`](../packages/flytekit.models.literals#flytekitmodelsliteralsprimitive) | |
| [`flytekit.models.literals.RetryStrategy`](../packages/flytekit.models.literals#flytekitmodelsliteralsretrystrategy) | |
| [`flytekit.models.literals.Scalar`](../packages/flytekit.models.literals#flytekitmodelsliteralsscalar) | |
| [`flytekit.models.literals.Schema`](../packages/flytekit.models.literals#flytekitmodelsliteralsschema) | |
| [`flytekit.models.literals.StructuredDataset`](../packages/flytekit.models.literals#flytekitmodelsliteralsstructureddataset) | |
| [`flytekit.models.literals.StructuredDatasetMetadata`](../packages/flytekit.models.literals#flytekitmodelsliteralsstructureddatasetmetadata) | |
| [`flytekit.models.literals.Union`](../packages/flytekit.models.literals#flytekitmodelsliteralsunion) | |
| [`flytekit.models.literals.Void`](../packages/flytekit.models.literals#flytekitmodelsliteralsvoid) | |
| [`flytekit.models.matchable_resource.ClusterResourceAttributes`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceclusterresourceattributes) | |
| [`flytekit.models.matchable_resource.ExecutionClusterLabel`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionclusterlabel) | |
| [`flytekit.models.matchable_resource.ExecutionQueueAttributes`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionqueueattributes) | |
| [`flytekit.models.matchable_resource.MatchableResource`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchableresource) | |
| [`flytekit.models.matchable_resource.MatchingAttributes`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchingattributes) | |
| [`flytekit.models.matchable_resource.PluginOverride`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverride) | |
| [`flytekit.models.matchable_resource.PluginOverrides`](../packages/flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverrides) | |
| [`flytekit.models.named_entity.NamedEntityIdentifier`](../packages/flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentityidentifier) | |
| [`flytekit.models.named_entity.NamedEntityMetadata`](../packages/flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentitymetadata) | |
| [`flytekit.models.named_entity.NamedEntityState`](../packages/flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentitystate) | |
| [`flytekit.models.node_execution.DynamicWorkflowNodeMetadata`](../packages/flytekit.models.node_execution#flytekitmodelsnode_executiondynamicworkflownodemetadata) | |
| [`flytekit.models.node_execution.NodeExecution`](../packages/flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecution) | |
| [`flytekit.models.node_execution.NodeExecutionClosure`](../packages/flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecutionclosure) | |
| [`flytekit.models.node_execution.TaskNodeMetadata`](../packages/flytekit.models.node_execution#flytekitmodelsnode_executiontasknodemetadata) | |
| [`flytekit.models.node_execution.WorkflowNodeMetadata`](../packages/flytekit.models.node_execution#flytekitmodelsnode_executionworkflownodemetadata) | |
| [`flytekit.models.presto.PrestoQuery`](../packages/flytekit.models.presto#flytekitmodelsprestoprestoquery) | |
| [`flytekit.models.project.Project`](../packages/flytekit.models.project#flytekitmodelsprojectproject) | |
| [`flytekit.models.qubole.HiveQuery`](../packages/flytekit.models.qubole#flytekitmodelsqubolehivequery) | |
| [`flytekit.models.qubole.HiveQueryCollection`](../packages/flytekit.models.qubole#flytekitmodelsqubolehivequerycollection) | |
| [`flytekit.models.qubole.QuboleHiveJob`](../packages/flytekit.models.qubole#flytekitmodelsqubolequbolehivejob) | |
| [`flytekit.models.schedule.Schedule`](../packages/flytekit.models.schedule#flytekitmodelsscheduleschedule) | |
| [`flytekit.models.security.Identity`](../packages/flytekit.models.security#flytekitmodelssecurityidentity) | |
| [`flytekit.models.security.OAuth2Client`](../packages/flytekit.models.security#flytekitmodelssecurityoauth2client) | |
| [`flytekit.models.security.OAuth2TokenRequest`](../packages/flytekit.models.security#flytekitmodelssecurityoauth2tokenrequest) | |
| [`flytekit.models.security.Secret`](../packages/flytekit.models.security#flytekitmodelssecuritysecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.models.security.SecurityContext`](../packages/flytekit.models.security#flytekitmodelssecuritysecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.models.task.CompiledTask`](../packages/flytekit.models.task#flytekitmodelstaskcompiledtask) | |
| [`flytekit.models.task.Container`](../packages/flytekit.models.task#flytekitmodelstaskcontainer) | |
| [`flytekit.models.task.DataLoadingConfig`](../packages/flytekit.models.task#flytekitmodelstaskdataloadingconfig) | |
| [`flytekit.models.task.IOStrategy`](../packages/flytekit.models.task#flytekitmodelstaskiostrategy) |Provides methods to manage data in and out of the Raw container using Download Modes. |
| [`flytekit.models.task.K8sObjectMetadata`](../packages/flytekit.models.task#flytekitmodelstaskk8sobjectmetadata) | |
| [`flytekit.models.task.K8sPod`](../packages/flytekit.models.task#flytekitmodelstaskk8spod) | |
| [`flytekit.models.task.Resources`](../packages/flytekit.models.task#flytekitmodelstaskresources) | |
| [`flytekit.models.task.RuntimeMetadata`](../packages/flytekit.models.task#flytekitmodelstaskruntimemetadata) | |
| [`flytekit.models.task.Sql`](../packages/flytekit.models.task#flytekitmodelstasksql) | |
| [`flytekit.models.task.Task`](../packages/flytekit.models.task#flytekitmodelstasktask) | |
| [`flytekit.models.task.TaskClosure`](../packages/flytekit.models.task#flytekitmodelstasktaskclosure) | |
| [`flytekit.models.task.TaskExecutionMetadata`](../packages/flytekit.models.task#flytekitmodelstasktaskexecutionmetadata) | |
| [`flytekit.models.task.TaskMetadata`](../packages/flytekit.models.task#flytekitmodelstasktaskmetadata) | |
| [`flytekit.models.task.TaskSpec`](../packages/flytekit.models.task#flytekitmodelstasktaskspec) | |
| [`flytekit.models.task.TaskTemplate`](../packages/flytekit.models.task#flytekitmodelstasktasktemplate) | |
| [`flytekit.models.types.Error`](../packages/flytekit.models.types#flytekitmodelstypeserror) | |
| [`flytekit.models.types.LiteralType`](../packages/flytekit.models.types#flytekitmodelstypesliteraltype) | |
| [`flytekit.models.types.OutputReference`](../packages/flytekit.models.types#flytekitmodelstypesoutputreference) | |
| [`flytekit.models.types.SchemaType`](../packages/flytekit.models.types#flytekitmodelstypesschematype) | |
| [`flytekit.models.types.SimpleType`](../packages/flytekit.models.types#flytekitmodelstypessimpletype) | |
| [`flytekit.models.types.StructuredDatasetType`](../packages/flytekit.models.types#flytekitmodelstypesstructureddatasettype) | |
| [`flytekit.models.types.TypeStructure`](../packages/flytekit.models.types#flytekitmodelstypestypestructure) |Models _types_pb2. |
| [`flytekit.models.types.UnionType`](../packages/flytekit.models.types#flytekitmodelstypesuniontype) |Models _types_pb2. |
| [`flytekit.models.workflow_closure.WorkflowClosure`](../packages/flytekit.models.workflow_closure#flytekitmodelsworkflow_closureworkflowclosure) | |
| [`flytekit.remote.entities.FlyteArrayNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytearraynode) | |
| [`flytekit.remote.entities.FlyteBranchNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytebranchnode) | |
| [`flytekit.remote.entities.FlyteGateNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytegatenode) | |
| [`flytekit.remote.entities.FlyteLaunchPlan`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytelaunchplan) |A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.entities.FlyteNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytenode) |A class encapsulating a remote Flyte node. |
| [`flytekit.remote.entities.FlyteTask`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytetask) |A class encapsulating a remote Flyte task. |
| [`flytekit.remote.entities.FlyteTaskNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytetasknode) |A class encapsulating a task that a Flyte node needs to execute. |
| [`flytekit.remote.entities.FlyteWorkflow`](../packages/flytekit.remote.entities#flytekitremoteentitiesflyteworkflow) |A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.entities.FlyteWorkflowNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflyteworkflownode) |A class encapsulating a workflow that a Flyte node needs to execute. |
| [`flytekit.remote.executions.FlyteNodeExecution`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflytenodeexecution) |A class encapsulating a node execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteTaskExecution`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflytetaskexecution) |A class encapsulating a task execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteWorkflowExecution`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflyteworkflowexecution) |A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.RemoteExecutionBase`](../packages/flytekit.remote.executions#flytekitremoteexecutionsremoteexecutionbase) | |
| [`flytekit.remote.interface.TypedInterface`](../packages/flytekit.remote.interface#flytekitremoteinterfacetypedinterface) | |
| [`flytekit.remote.lazy_entity.LazyEntity`](../packages/flytekit.remote.lazy_entity#flytekitremotelazy_entitylazyentity) |Fetches the entity when the entity is called or when the entity is retrieved. |
| [`flytekit.remote.metrics.FlyteExecutionSpan`](../packages/flytekit.remote.metrics#flytekitremotemetricsflyteexecutionspan) | |
| [`flytekit.remote.remote.FlyteRemote`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.remote.remote.RegistrationSkipped`](../packages/flytekit.remote.remote#flytekitremoteremoteregistrationskipped) |RegistrationSkipped error is raised when trying to register an entity that is not registrable. |
| [`flytekit.remote.remote.ResolvedIdentifiers`](../packages/flytekit.remote.remote#flytekitremoteremoteresolvedidentifiers) | |
| [`flytekit.remote.remote_callable.RemoteEntity`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableremoteentity) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.remote.remote_fs.FlytePathResolver`](../packages/flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) | |
| [`flytekit.sensor.base_sensor.BaseSensor`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorbasesensor) |Base class for all sensors. |
| [`flytekit.sensor.base_sensor.SensorConfig`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorsensorconfig) |Base class for protocol classes. |
| [`flytekit.sensor.base_sensor.SensorMetadata`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorsensormetadata) | |
| [`flytekit.sensor.file_sensor.FileSensor`](../packages/flytekit.sensor.file_sensor#flytekitsensorfile_sensorfilesensor) |Base class for all sensors. |
| [`flytekit.sensor.sensor_engine.SensorEngine`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_enginesensorengine) |This is the base class for all async connectors. |
| [`flytekit.tools.fast_registration.FastPackageOptions`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationfastpackageoptions) |FastPackageOptions is used to set configuration options when packaging files. |
| [`flytekit.tools.ignore.DockerIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignoredockerignore) |Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`flytekit.tools.ignore.FlyteIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignoreflyteignore) |Uses a. |
| [`flytekit.tools.ignore.GitIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignoregitignore) |Uses git cli (if available) to list all ignored files and compare with those. |
| [`flytekit.tools.ignore.Ignore`](../packages/flytekit.tools.ignore#flytekittoolsignoreignore) |Base for Ignores, implements core logic. |
| [`flytekit.tools.ignore.IgnoreGroup`](../packages/flytekit.tools.ignore#flytekittoolsignoreignoregroup) |Groups multiple Ignores and checks a path against them. |
| [`flytekit.tools.ignore.StandardIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignorestandardignore) |Retains the standard ignore functionality that previously existed. |
| [`flytekit.tools.repo.NoSerializableEntitiesError`](../packages/flytekit.tools.repo#flytekittoolsreponoserializableentitieserror) |Common base class for all non-exit exceptions. |
| [`flytekit.types.directory.types.FlyteDirToMultipartBlobTransformer`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytedirtomultipartblobtransformer) |This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`flytekit.types.directory.types.FlyteDirectory`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytedirectory) | |
| [`flytekit.types.error.error.ErrorTransformer`](../packages/flytekit.types.error.error#flytekittypeserrorerrorerrortransformer) |Enables converting a python type FlyteError to LiteralType. |
| [`flytekit.types.error.error.FlyteError`](../packages/flytekit.types.error.error#flytekittypeserrorerrorflyteerror) |Special Task type that will be used in the failure node. |
| [`flytekit.types.file.FileExt`](../packages/flytekit.types.file#flytekittypesfilefileext) |Used for annotating file extension types of FlyteFile. |
| [`flytekit.types.file.file.FlyteFile`](../packages/flytekit.types.file.file#flytekittypesfilefileflytefile) | |
| [`flytekit.types.file.file.FlyteFilePathTransformer`](../packages/flytekit.types.file.file#flytekittypesfilefileflytefilepathtransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.iterator.iterator.FlyteIterator`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratorflyteiterator) | |
| [`flytekit.types.iterator.iterator.IteratorTransformer`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratoriteratortransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.iterator.json_iterator.JSONIterator`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorjsoniterator) |Abstract base class for generic types. |
| [`flytekit.types.iterator.json_iterator.JSONIteratorTransformer`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorjsoniteratortransformer) |A JSON iterator that handles conversion between an iterator/generator and a JSONL file. |
| [`flytekit.types.numpy.ndarray.NumpyArrayTransformer`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarraynumpyarraytransformer) |TypeTransformer that supports np. |
| [`flytekit.types.pickle.pickle.FlytePickle`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleflytepickle) |This type is only used by flytekit internally. |
| [`flytekit.types.pickle.pickle.FlytePickleTransformer`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleflytepickletransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.schema.types.FlyteSchema`](../packages/flytekit.types.schema.types#flytekittypesschematypesflyteschema) | |
| [`flytekit.types.schema.types.FlyteSchemaTransformer`](../packages/flytekit.types.schema.types#flytekittypesschematypesflyteschematransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.schema.types.LocalIOSchemaReader`](../packages/flytekit.types.schema.types#flytekittypesschematypeslocalioschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types.LocalIOSchemaWriter`](../packages/flytekit.types.schema.types#flytekittypesschematypeslocalioschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types.SchemaEngine`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemaengine) |This is the core Engine that handles all schema sub-systems. |
| [`flytekit.types.schema.types.SchemaHandler`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemahandler) | |
| [`flytekit.types.schema.types.SchemaReader`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types.SchemaWriter`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types_pandas.PandasDataFrameTransformer`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasdataframetransformer) |Transforms a pd. |
| [`flytekit.types.schema.types_pandas.PandasSchemaReader`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types_pandas.PandasSchemaWriter`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types_pandas.ParquetIO`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasparquetio) | |
| [`flytekit.types.structured.basic_dfs.ArrowToParquetEncodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsarrowtoparquetencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.CSVToPandasDecodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfscsvtopandasdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.PandasToCSVEncodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastocsvencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.PandasToParquetEncodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastoparquetencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.ParquetToArrowDecodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettoarrowdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.ParquetToPandasDecodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettopandasdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.structured_dataset.DuplicateHandlerError`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetduplicatehandlererror) |Inappropriate argument value (of correct type). |
| [`flytekit.types.structured.structured_dataset.StructuredDataset`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetDecoder`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetdecoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetEncoder`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetencoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetTransformerEngine`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettransformerengine) |Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flytekit.utils.rate_limiter.RateLimiter`](../packages/flytekit.utils.rate_limiter#flytekitutilsrate_limiterratelimiter) |Rate limiter that allows up to a certain number of requests per minute. |
