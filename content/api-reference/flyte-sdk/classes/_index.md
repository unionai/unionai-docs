---
title: Classes & Protocols
version: 2.1.3.dev1+ge23e739d5
variants: +flyte +union
layout: py_api
sidebar_expanded: true
---

# Classes

| Class | Description |
|-|-|
| [`flyte.Cache`](../packages/flyte/cache) |Cache configuration for a task. |
| [`flyte.Cron`](../packages/flyte/cron) |Cron-based automation schedule for use with `Trigger`. |
| [`flyte.Device`](../packages/flyte/device) |Represents a device type, its quantity and partition if applicable. |
| [`flyte.Environment`](../packages/flyte/environment) | |
| [`flyte.FixedRate`](../packages/flyte/fixedrate) |Fixed-rate (interval-based) automation schedule for use with `Trigger`. |
| [`flyte.Image`](../packages/flyte/image) |Container image specification built using a fluent, two-step pattern:. |
| [`flyte.ImageBuild`](../packages/flyte/imagebuild) |Result of an image build operation. |
| [`flyte.PodTemplate`](../packages/flyte/podtemplate) |Custom PodTemplate specification for a Task. |
| [`flyte.Resources`](../packages/flyte/resources) |Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`flyte.RetryStrategy`](../packages/flyte/retrystrategy) |Retry strategy for the task or task environment. |
| [`flyte.ReusePolicy`](../packages/flyte/reusepolicy) |Configure a task environment for container reuse across multiple task invocations. |
| [`flyte.Secret`](../packages/flyte/secret) |Secrets are used to inject sensitive information into tasks or image build context. |
| [`flyte.TaskEnvironment`](../packages/flyte/taskenvironment) |Define an execution environment for a set of tasks. |
| [`flyte.Timeout`](../packages/flyte/timeout) |Timeout class to define a timeout for a task. |
| [`flyte.Trigger`](../packages/flyte/trigger) |Specification for a scheduled trigger that can be associated with any Flyte task. |
| [`flyte.app.AppEndpoint`](../packages/flyte.app/appendpoint) |Embed an upstream app's endpoint as an app parameter. |
| [`flyte.app.AppEnvironment`](../packages/flyte.app/appenvironment) |Configure a long-running app environment for APIs, dashboards, or model servers. |
| [`flyte.app.ConnectorEnvironment`](../packages/flyte.app/connectorenvironment) | |
| [`flyte.app.Domain`](../packages/flyte.app/domain) |Subdomain to use for the domain. |
| [`flyte.app.Link`](../packages/flyte.app/link) |Custom links to add to the app. |
| [`flyte.app.Parameter`](../packages/flyte.app/parameter) |Parameter for application. |
| [`flyte.app.Port`](../packages/flyte.app/port) | |
| [`flyte.app.RunOutput`](../packages/flyte.app/runoutput) |Use a run's output for app parameters. |
| [`flyte.app.Scaling`](../packages/flyte.app/scaling) |Controls replica count and autoscaling behavior for app environments. |
| [`flyte.app.Timeouts`](../packages/flyte.app/timeouts) |Timeout configuration for the application. |
| [`flyte.app.extras.FastAPIAppEnvironment`](../packages/flyte.app.extras/fastapiappenvironment) | |
| [`flyte.app.extras.FastAPIPassthroughAuthMiddleware`](../packages/flyte.app.extras/fastapipassthroughauthmiddleware) |FastAPI middleware that automatically sets Flyte auth metadata from request headers. |
| [`flyte.app.extras.FlyteWebhookAppEnvironment`](../packages/flyte.app.extras/flytewebhookappenvironment) |A pre-built FastAPI app environment for common Flyte webhook operations. |
| [`flyte.config.Config`](../packages/flyte.config/config) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flyte.connectors.AsyncConnector`](../packages/flyte.connectors/asyncconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyte.connectors.AsyncConnectorExecutorMixin`](../packages/flyte.connectors/asyncconnectorexecutormixin) |This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyte.connectors.ConnectorRegistry`](../packages/flyte.connectors/connectorregistry) |This is the registry for all connectors. |
| [`flyte.connectors.ConnectorService`](../packages/flyte.connectors/connectorservice) | |
| [`flyte.connectors.Resource`](../packages/flyte.connectors/resource) |This is the output resource of the job. |
| [`flyte.connectors.ResourceMeta`](../packages/flyte.connectors/resourcemeta) |This is the metadata for the job. |
| [`flyte.errors.ActionAbortedError`](../packages/flyte.errors/actionabortederror) |This error is raised when an action was aborted, externally. |
| [`flyte.errors.ActionNotFoundError`](../packages/flyte.errors/actionnotfounderror) |This error is raised when the user tries to access an action that does not exist. |
| [`flyte.errors.BaseRuntimeError`](../packages/flyte.errors/baseruntimeerror) |Base class for all Union runtime errors. |
| [`flyte.errors.CodeBundleError`](../packages/flyte.errors/codebundleerror) |This error is raised when the code bundle cannot be created, for example when no files are found to bundle. |
| [`flyte.errors.CustomError`](../packages/flyte.errors/customerror) |This error is raised when the user raises a custom error. |
| [`flyte.errors.DeploymentError`](../packages/flyte.errors/deploymenterror) |This error is raised when the deployment of a task fails, or some preconditions for deployment are not met. |
| [`flyte.errors.ImageBuildError`](../packages/flyte.errors/imagebuilderror) |This error is raised when the image build fails. |
| [`flyte.errors.ImagePullBackOffError`](../packages/flyte.errors/imagepullbackofferror) |This error is raised when the image cannot be pulled. |
| [`flyte.errors.InitializationError`](../packages/flyte.errors/initializationerror) |This error is raised when the Union system is tried to access without being initialized. |
| [`flyte.errors.InlineIOMaxBytesBreached`](../packages/flyte.errors/inlineiomaxbytesbreached) |This error is raised when the inline IO max bytes limit is breached. |
| [`flyte.errors.InvalidImageNameError`](../packages/flyte.errors/invalidimagenameerror) |This error is raised when the image name is invalid. |
| [`flyte.errors.InvalidPackageError`](../packages/flyte.errors/invalidpackageerror) |Raised when an invalid system package is detected during image build. |
| [`flyte.errors.LogsNotYetAvailableError`](../packages/flyte.errors/logsnotyetavailableerror) |This error is raised when the logs are not yet available for a task. |
| [`flyte.errors.ModuleLoadError`](../packages/flyte.errors/moduleloaderror) |This error is raised when the module cannot be loaded, either because it does not exist or because of a. |
| [`flyte.errors.NonRecoverableError`](../packages/flyte.errors/nonrecoverableerror) |Raised when an error is encountered that is not recoverable. |
| [`flyte.errors.NotInTaskContextError`](../packages/flyte.errors/notintaskcontexterror) |This error is raised when the user tries to access the task context outside of a task. |
| [`flyte.errors.OOMError`](../packages/flyte.errors/oomerror) |This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`flyte.errors.OnlyAsyncIOSupportedError`](../packages/flyte.errors/onlyasynciosupportederror) |This error is raised when the user tries to use sync IO in an async task. |
| [`flyte.errors.ParameterMaterializationError`](../packages/flyte.errors/parametermaterializationerror) |This error is raised when the user tries to use a Parameter in an App, that has delayed Materialization,. |
| [`flyte.errors.PrimaryContainerNotFoundError`](../packages/flyte.errors/primarycontainernotfounderror) |This error is raised when the primary container is not found. |
| [`flyte.errors.RemoteTaskNotFoundError`](../packages/flyte.errors/remotetasknotfounderror) |This error is raised when the user tries to access a task that does not exist. |
| [`flyte.errors.RemoteTaskUsageError`](../packages/flyte.errors/remotetaskusageerror) |This error is raised when the user tries to access a task that does not exist. |
| [`flyte.errors.RestrictedTypeError`](../packages/flyte.errors/restrictedtypeerror) |This error is raised when the user uses a restricted type, for example current a Tuple is not supported for one. |
| [`flyte.errors.RetriesExhaustedError`](../packages/flyte.errors/retriesexhaustederror) |This error is raised when the underlying task execution fails after all retries have been exhausted. |
| [`flyte.errors.RuntimeDataValidationError`](../packages/flyte.errors/runtimedatavalidationerror) |This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`flyte.errors.RuntimeSystemError`](../packages/flyte.errors/runtimesystemerror) |This error is raised when the underlying task execution fails because of a system error. |
| [`flyte.errors.RuntimeUnknownError`](../packages/flyte.errors/runtimeunknownerror) |This error is raised when the underlying task execution fails because of an unknown error. |
| [`flyte.errors.RuntimeUserError`](../packages/flyte.errors/runtimeusererror) |This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`flyte.errors.SlowDownError`](../packages/flyte.errors/slowdownerror) |This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`flyte.errors.TaskInterruptedError`](../packages/flyte.errors/taskinterruptederror) |This error is raised when the underlying task execution is interrupted. |
| [`flyte.errors.TaskTimeoutError`](../packages/flyte.errors/tasktimeouterror) |This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`flyte.errors.TraceDoesNotAllowNestedTasksError`](../packages/flyte.errors/tracedoesnotallownestedtaskserror) |This error is raised when the user tries to use a task from within a trace. |
| [`flyte.errors.UnionRpcError`](../packages/flyte.errors/unionrpcerror) |This error is raised when communication with the Union server fails. |
| [`flyte.extend.AsyncFunctionTaskTemplate`](../packages/flyte.extend/asyncfunctiontasktemplate) |A task template that wraps an asynchronous functions. |
| [`flyte.extend.ImageBuildEngine`](../packages/flyte.extend/imagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flyte.extend.TaskTemplate`](../packages/flyte.extend/tasktemplate) |Task template is a template for a task that can be executed. |
| [`flyte.extras.BatchStats`](../packages/flyte.extras/batchstats) |Monitoring statistics exposed by `DynamicBatcher. |
| [`flyte.extras.ContainerTask`](../packages/flyte.extras/containertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flyte.extras.DynamicBatcher`](../packages/flyte.extras/dynamicbatcher) |Batches records from many concurrent producers and runs them through. |
| [`flyte.extras.Prompt`](../packages/flyte.extras/prompt) |Simple prompt record with built-in token estimation. |
| [`flyte.extras.TokenBatcher`](../packages/flyte.extras/tokenbatcher) |Token-aware batcher for LLM inference workloads. |
| [`flyte.git.GitStatus`](../packages/flyte.git/gitstatus) |A class representing the status of a git repository. |
| [`flyte.io.DataFrame`](../packages/flyte.io/dataframe) |A Flyte meta DataFrame object, that wraps all other dataframe types (usually available as plugins, pandas. |
| [`flyte.io.Dir`](../packages/flyte.io/dir) |A generic directory class representing a directory with files of a specified format. |
| [`flyte.io.File`](../packages/flyte.io/file) |A generic file class representing a file with a specified format. |
| [`flyte.io.HashFunction`](../packages/flyte.io/hashfunction) |A hash method that wraps a user-provided function to compute hashes. |
| [`flyte.io.extend.DataFrameDecoder`](../packages/flyte.io.extend/dataframedecoder) | |
| [`flyte.io.extend.DataFrameEncoder`](../packages/flyte.io.extend/dataframeencoder) | |
| [`flyte.io.extend.DataFrameTransformerEngine`](../packages/flyte.io.extend/dataframetransformerengine) |Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flyte.models.ActionID`](../packages/flyte.models/actionid) |A class representing the ID of an Action, nested within a Run. |
| [`flyte.models.ActionPhase`](../packages/flyte.models/actionphase) |Represents the execution phase of a Flyte action (run). |
| [`flyte.models.Checkpoints`](../packages/flyte.models/checkpoints) |A class representing the checkpoints for a task. |
| [`flyte.models.CodeBundle`](../packages/flyte.models/codebundle) |A class representing a code bundle for a task. |
| [`flyte.models.GroupData`](../packages/flyte.models/groupdata) | |
| [`flyte.models.NativeInterface`](../packages/flyte.models/nativeinterface) |A class representing the native interface for a task. |
| [`flyte.models.PathRewrite`](../packages/flyte.models/pathrewrite) |Configuration for rewriting paths during input loading. |
| [`flyte.models.RawDataPath`](../packages/flyte.models/rawdatapath) |A class representing the raw data path for a task. |
| [`flyte.models.SerializationContext`](../packages/flyte.models/serializationcontext) |This object holds serialization time contextual information, that can be used when serializing the task and. |
| [`flyte.models.TaskContext`](../packages/flyte.models/taskcontext) |A context class to hold the current task executions context. |
| [`flyte.notify.Email`](../packages/flyte.notify/email) |Send email notifications. |
| [`flyte.notify.NamedDelivery`](../packages/flyte.notify/nameddelivery) |Use a pre-configured delivery channel by name. |
| [`flyte.notify.NamedRule`](../packages/flyte.notify/namedrule) |Reference a pre-defined notification rule by name. |
| [`flyte.notify.Notification`](../packages/flyte.notify/notification) |Base notification class. |
| [`flyte.notify.Slack`](../packages/flyte.notify/slack) |Send Slack notifications with optional Block Kit formatting. |
| [`flyte.notify.Teams`](../packages/flyte.notify/teams) |Send Microsoft Teams notifications with optional Adaptive Cards. |
| [`flyte.notify.Webhook`](../packages/flyte.notify/webhook) |Send custom HTTP webhook notifications (most flexible option). |
| [`flyte.prefetch.HuggingFaceModelInfo`](../packages/flyte.prefetch/huggingfacemodelinfo) |Information about a HuggingFace model to store. |
| [`flyte.prefetch.ShardConfig`](../packages/flyte.prefetch/shardconfig) |Configuration for model sharding. |
| [`flyte.prefetch.StoredModelInfo`](../packages/flyte.prefetch/storedmodelinfo) |Information about a stored model. |
| [`flyte.prefetch.VLLMShardArgs`](../packages/flyte.prefetch/vllmshardargs) |Arguments for sharding a model using vLLM. |
| [`flyte.remote.Action`](../packages/flyte.remote/action) |A class representing an action. |
| [`flyte.remote.ActionDetails`](../packages/flyte.remote/actiondetails) |A class representing an action. |
| [`flyte.remote.ActionInputs`](../packages/flyte.remote/actioninputs) |A class representing the inputs of an action. |
| [`flyte.remote.ActionOutputs`](../packages/flyte.remote/actionoutputs) |A class representing the outputs of an action. |
| [`flyte.remote.App`](../packages/flyte.remote/app) | |
| [`flyte.remote.Project`](../packages/flyte.remote/project) |A class representing a project in the Union API. |
| [`flyte.remote.Run`](../packages/flyte.remote/run) |A class representing a run of a task. |
| [`flyte.remote.RunDetails`](../packages/flyte.remote/rundetails) |A class representing a run of a task. |
| [`flyte.remote.Secret`](../packages/flyte.remote/secret) | |
| [`flyte.remote.Task`](../packages/flyte.remote/task) | |
| [`flyte.remote.TaskDetails`](../packages/flyte.remote/taskdetails) | |
| [`flyte.remote.TimeFilter`](../packages/flyte.remote/timefilter) |Filter for time-based fields (e. |
| [`flyte.remote.Trigger`](../packages/flyte.remote/trigger) |Represents a trigger in the Flyte platform. |
| [`flyte.remote.User`](../packages/flyte.remote/user) |Represents a user in the Flyte platform. |
| [`flyte.report.Report`](../packages/flyte.report/report) | |
| [`flyte.sandbox.CodeTaskTemplate`](../packages/flyte.sandbox/codetasktemplate) |A sandboxed task created from a code string rather than a decorated function. |
| [`flyte.sandbox.ImageConfig`](../packages/flyte.sandbox/imageconfig) |Configuration for Docker image building at runtime. |
| [`flyte.sandbox.SandboxedConfig`](../packages/flyte.sandbox/sandboxedconfig) |Configuration for a sandboxed task executed via Monty. |
| [`flyte.sandbox.SandboxedTaskTemplate`](../packages/flyte.sandbox/sandboxedtasktemplate) |A task template that executes the function body in a Monty sandbox. |
| [`flyte.storage.ABFS`](../packages/flyte.storage/abfs) |Any Azure Blob Storage specific configuration. |
| [`flyte.storage.GCS`](../packages/flyte.storage/gcs) |Any GCS specific configuration. |
| [`flyte.storage.S3`](../packages/flyte.storage/s3) |S3 specific configuration. |
| [`flyte.storage.Storage`](../packages/flyte.storage/storage) |Data storage configuration that applies across any provider. |
| [`flyte.syncify.Syncify`](../packages/flyte.syncify/syncify) |A decorator to convert asynchronous functions or methods into synchronous ones. |
| [`flyte.types.FlytePickle`](../packages/flyte.types/flytepickle) |This type is only used by flytekit internally. |
| [`flyte.types.TypeEngine`](../packages/flyte.types/typeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flyte.types.TypeTransformer`](../packages/flyte.types/typetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flyte.types.TypeTransformerFailedError`](../packages/flyte.types/typetransformerfailederror) | |
# Protocols

| Protocol | Description |
|-|-|
| [`flyte.AppHandle`](../packages/flyte/apphandle) |Protocol defining the common interface between local and remote app handles. |
| [`flyte.CachePolicy`](../packages/flyte/cachepolicy) |Protocol for custom cache version strategies. |
| [`flyte.Link`](../packages/flyte/link) | |
| [`flyte.extend.ImageBuilder`](../packages/flyte.extend/imagebuilder) | |
| [`flyte.extend.ImageChecker`](../packages/flyte.extend/imagechecker) | |
| [`flyte.extras.CostEstimator`](../packages/flyte.extras/costestimator) |Protocol for records that can estimate their own processing cost. |
| [`flyte.extras.TokenEstimator`](../packages/flyte.extras/tokenestimator) |Protocol for records that can estimate their own token count. |
| [`flyte.types.Renderable`](../packages/flyte.types/renderable) | |
