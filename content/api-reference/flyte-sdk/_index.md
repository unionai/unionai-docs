---
title: Flyte SDK
version: 2.6.0
variants: +flyte +union
layout: py_api
weight: 4
---

# Flyte SDK

These are the docs for Flyte SDK version 2.0

Flyte is the core Python SDK for the Union and Flyte platforms.



## Directory

### Classes

| Class | Description |
|-|-|
| [`flyte.AsyncFunctionTaskTemplate`](flyte/asyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |
| [`flyte.Backoff`](flyte/backoff) | Exponential backoff policy applied between user retries. |
| [`flyte.BaseCheckpoint`](flyte/basecheckpoint) | Base type for task checkpoint helpers. |
| [`flyte.Cache`](flyte/cache) | Cache configuration for a task. |
| [`flyte.Checkpoint`](flyte/checkpoint) | Checkpoint helper using `flyte.io.File` for all checkpoint blob I/O (load/save, async and sync). |
| [`flyte.ConditionWebhook`](flyte/conditionwebhook) | Webhook configuration for a condition notification. |
| [`flyte.Cron`](flyte/cron) | Cron-based automation schedule for use with `Trigger`. |
| [`flyte.Device`](flyte/device) | Represents a device type, its quantity and partition if applicable. |
| [`flyte.Environment`](flyte/environment) | Base class for execution environments, shared by `TaskEnvironment` and. |
| [`flyte.FixedRate`](flyte/fixedrate) | Fixed-rate (interval-based) automation schedule for use with `Trigger`. |
| [`flyte.Image`](flyte/image) | Container image specification built using a fluent, two-step pattern:. |
| [`flyte.ImageBuild`](flyte/imagebuild) | Result of an image build operation. |
| [`flyte.OnArtifact`](flyte/onartifact) | Artifact-based automation for use with `Trigger`: fire a run whenever a new. |
| [`flyte.PodTemplate`](flyte/podtemplate) | Custom PodTemplate specification for a Task. |
| [`flyte.Resources`](flyte/resources) | Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`flyte.RetryStrategy`](flyte/retrystrategy) | Retry strategy for a task. |
| [`flyte.ReusePolicy`](flyte/reusepolicy) | Configure a task environment for container reuse across multiple task invocations. |
| [`flyte.Secret`](flyte/secret) | Secrets are used to inject sensitive information into tasks or image build context. |
| [`flyte.TaskEnvironment`](flyte/taskenvironment) | Define an execution environment for a set of tasks. |
| [`flyte.TaskTemplate`](flyte/tasktemplate) | Task template is a template for a task that can be executed. |
| [`flyte.Timeout`](flyte/timeout) | Timeout bounds for a task. |
| [`flyte.Trigger`](flyte/trigger) | Specification for a scheduled trigger that can be associated with any Flyte task. |
| [`flyte.ai.agents.AccessDenied`](flyte.ai.agents/accessdenied) | Raised when a write targets a read-only or reserved prefix. |
| [`flyte.ai.agents.Agent`](flyte.ai.agents/agent) | A flyte-native tool-use agent harness. |
| [`flyte.ai.agents.AgentEvent`](flyte.ai.agents/agentevent) | Lightweight event emitted by the agent loop. |
| [`flyte.ai.agents.AgentResult`](flyte.ai.agents/agentresult) | Outcome of a single agent invocation. |
| [`flyte.ai.agents.AgentTool`](flyte.ai.agents/agenttool) | A normalized tool descriptor used by `flyte.ai.agents.Agent`. |
| [`flyte.ai.agents.ConcurrencyError`](flyte.ai.agents/concurrencyerror) | Raised when an `expected_sha` precondition does not match the current state. |
| [`flyte.ai.agents.LLMMessage`](flyte.ai.agents/llmmessage) | Provider-agnostic shape returned by `flyte.ai.agents.LLMCallable`. |
| [`flyte.ai.agents.MCPServerSpec`](flyte.ai.agents/mcpserverspec) | Declarative spec for a remote MCP server that exposes tools. |
| [`flyte.ai.agents.MemoryMeta`](flyte.ai.agents/memorymeta) | Per-file metadata sidecar (sha256, actor, timestamp, …) for a memory entry. |
| [`flyte.ai.agents.MemoryStore`](flyte.ai.agents/memorystore) | Conversation transcript + path-addressed artifact memory backed by `flyte.io.Dir`. |
| [`flyte.ai.agents.MemoryStoreError`](flyte.ai.agents/memorystoreerror) | Base class for `flyte.ai.agents.MemoryStore` errors. |
| [`flyte.ai.agents.ToolFn`](flyte.ai.agents/toolfn) | The tool under invocation, handed to a `flyte.ai.agents.ToolCallHandler`. |
| [`flyte.ai.agents.agent.Agent`](flyte.ai.agents.agent/agent) | A flyte-native tool-use agent harness. |
| [`flyte.ai.agents.agent.AgentEvent`](flyte.ai.agents.agent/agentevent) | Lightweight event emitted by the agent loop. |
| [`flyte.ai.agents.memory.AccessDenied`](flyte.ai.agents.memory/accessdenied) | Raised when a write targets a read-only or reserved prefix. |
| [`flyte.ai.agents.memory.ConcurrencyError`](flyte.ai.agents.memory/concurrencyerror) | Raised when an `expected_sha` precondition does not match the current state. |
| [`flyte.ai.agents.memory.MemoryMeta`](flyte.ai.agents.memory/memorymeta) | Per-file metadata sidecar (sha256, actor, timestamp, …) for a memory entry. |
| [`flyte.ai.agents.memory.MemoryStore`](flyte.ai.agents.memory/memorystore) | Conversation transcript + path-addressed artifact memory backed by `flyte.io.Dir`. |
| [`flyte.ai.agents.memory.MemoryStoreError`](flyte.ai.agents.memory/memorystoreerror) | Base class for `flyte.ai.agents.MemoryStore` errors. |
| [`flyte.ai.agents.protocol.AgentResult`](flyte.ai.agents.protocol/agentresult) | Outcome of a single agent invocation. |
| [`flyte.ai.chat.AgentChatAppEnvironment`](flyte.ai.chat/agentchatappenvironment) | An `flyte.app.AppEnvironment` that spins up a FastAPI chat. |
| [`flyte.ai.chat.CustomTheme`](flyte.ai.chat/customtheme) | Declarative color theme for the Agent Chat UI. |
| [`flyte.ai.chat.app.AgentChatAppEnvironment`](flyte.ai.chat.app/agentchatappenvironment) | An `flyte.app.AppEnvironment` that spins up a FastAPI chat. |
| [`flyte.ai.chat.app.CustomTheme`](flyte.ai.chat.app/customtheme) | Declarative color theme for the Agent Chat UI. |
| [`flyte.ai.mcp.FlyteMCPAppEnvironment`](flyte.ai.mcp/flytemcpappenvironment) | Serve a Flyte-facing MCP server over HTTP (FastMCP + Starlette + Uvicorn). |
| [`flyte.ai.mcp.MCPAppEnvironment`](flyte.ai.mcp/mcpappenvironment) | Serve a FastMCP server over HTTP (Starlette + Uvicorn) or over stdio. |
| [`flyte.app.AppEndpoint`](flyte.app/appendpoint) | Embed an upstream app's endpoint as an app parameter. |
| [`flyte.app.AppEnvironment`](flyte.app/appenvironment) | Configure a long-running app environment for APIs, dashboards, or model servers. |
| [`flyte.app.ArtifactValue`](flyte.app/artifactvalue) | Use a published artifact as an app parameter value. |
| [`flyte.app.ConnectorEnvironment`](flyte.app/connectorenvironment) | Configure a connector environment for custom Flyte connectors. |
| [`flyte.app.DeployedAppEnvironment`](flyte.app/deployedappenvironment) |  |
| [`flyte.app.Domain`](flyte.app/domain) | Subdomain to use for the domain. |
| [`flyte.app.Link`](flyte.app/link) | Custom links to add to the app. |
| [`flyte.app.Parameter`](flyte.app/parameter) | Parameter for application. |
| [`flyte.app.Port`](flyte.app/port) |  |
| [`flyte.app.RunOutput`](flyte.app/runoutput) | Use a run's output for app parameters. |
| [`flyte.app.Scaling`](flyte.app/scaling) | Controls replica count and autoscaling behavior for app environments. |
| [`flyte.app.Timeouts`](flyte.app/timeouts) | Timeout configuration for the application. |
| [`flyte.app.extras.FastAPIAppEnvironment`](flyte.app.extras/fastapiappenvironment) |  |
| [`flyte.app.extras.FastAPIPassthroughAuthMiddleware`](flyte.app.extras/fastapipassthroughauthmiddleware) | FastAPI middleware that automatically sets Flyte auth metadata from request headers. |
| [`flyte.app.extras.FlyteWebhookAppEnvironment`](flyte.app.extras/flytewebhookappenvironment) | A pre-built FastAPI app environment for common Flyte webhook operations. |
| [`flyte.artifacts.Card`](flyte.artifacts/card) |  |
| [`flyte.artifacts.Metadata`](flyte.artifacts/metadata) | Structured metadata for Flyte artifacts. |
| [`flyte.clustered.ClusterFailurePolicy`](flyte.clustered/clusterfailurepolicy) | Failure and restart policy for the JobSet as a whole. |
| [`flyte.clustered.ClusteredTaskEnvironment`](flyte.clustered/clusteredtaskenvironment) | A TaskEnvironment that emits a Kubernetes JobSet for distributed multi-node training. |
| [`flyte.clustered.ClusteredTaskTemplate`](flyte.clustered/clusteredtasktemplate) | Task template for `ClusteredTaskEnvironment`. |
| [`flyte.clustered.TorchRun`](flyte.clustered/torchrun) | TorchRun launcher configuration for a ClusteredTaskEnvironment. |
| [`flyte.config.Config`](flyte.config/config) | This the parent configuration object and holds all the underlying configuration object types. |
| [`flyte.connectors.AsyncConnector`](flyte.connectors/asyncconnector) | This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyte.connectors.AsyncConnectorExecutorMixin`](flyte.connectors/asyncconnectorexecutormixin) | This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyte.connectors.ConnectorRegistry`](flyte.connectors/connectorregistry) | This is the registry for all connectors. |
| [`flyte.connectors.ConnectorService`](flyte.connectors/connectorservice) |  |
| [`flyte.connectors.Resource`](flyte.connectors/resource) | This is the output resource of the job. |
| [`flyte.connectors.ResourceMeta`](flyte.connectors/resourcemeta) | This is the metadata for the job. |
| [`flyte.errors.ActionAbortedError`](flyte.errors/actionabortederror) | This error is raised when an action was aborted, externally. |
| [`flyte.errors.ActionNotFoundError`](flyte.errors/actionnotfounderror) | This error is raised when the user tries to access an action that does not exist. |
| [`flyte.errors.BaseRuntimeError`](flyte.errors/baseruntimeerror) | Base class for all Union runtime errors. |
| [`flyte.errors.CodeBundleError`](flyte.errors/codebundleerror) | This error is raised when the code bundle cannot be created, for example when no files are found to bundle. |
| [`flyte.errors.ConditionAlreadyExistsError`](flyte.errors/conditionalreadyexistserror) | This error is raised when the user tries to create a condition that already exists within the action. |
| [`flyte.errors.ConditionFailedError`](flyte.errors/conditionfailederror) | This error is raised when a condition fails during execution. |
| [`flyte.errors.ConditionNotFoundError`](flyte.errors/conditionnotfounderror) | This error is raised when the user tries to access a condition that does not exist. |
| [`flyte.errors.ConditionTimedoutError`](flyte.errors/conditiontimedouterror) | This error is raised when a condition is not signaled within its specified timeout. |
| [`flyte.errors.CustomError`](flyte.errors/customerror) | This error is raised when the user raises a custom error. |
| [`flyte.errors.DeploymentError`](flyte.errors/deploymenterror) | This error is raised when the deployment of a task fails, or some preconditions for deployment are not met. |
| [`flyte.errors.ImageBuildError`](flyte.errors/imagebuilderror) | This error is raised when the image build fails. |
| [`flyte.errors.ImagePullBackOffError`](flyte.errors/imagepullbackofferror) | This error is raised when the image cannot be pulled. |
| [`flyte.errors.InitializationError`](flyte.errors/initializationerror) | This error is raised when the Union system is tried to access without being initialized. |
| [`flyte.errors.InlineIOMaxBytesBreached`](flyte.errors/inlineiomaxbytesbreached) | This error is raised when the inline IO max bytes limit is breached. |
| [`flyte.errors.InvalidImageNameError`](flyte.errors/invalidimagenameerror) | This error is raised when the image name is invalid. |
| [`flyte.errors.InvalidPackageError`](flyte.errors/invalidpackageerror) | Raised when an invalid system package is detected during image build. |
| [`flyte.errors.LogsNotYetAvailableError`](flyte.errors/logsnotyetavailableerror) | This error is raised when the logs are not yet available for a task. |
| [`flyte.errors.ModuleLoadError`](flyte.errors/moduleloaderror) | This error is raised when the module cannot be loaded, either because it does not exist or because of a. |
| [`flyte.errors.NonRecoverableError`](flyte.errors/nonrecoverableerror) | Raised when an error is encountered that is not recoverable. |
| [`flyte.errors.NotInTaskContextError`](flyte.errors/notintaskcontexterror) | This error is raised when the user tries to access the task context outside of a task. |
| [`flyte.errors.OOMError`](flyte.errors/oomerror) | This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`flyte.errors.OnlyAsyncIOSupportedError`](flyte.errors/onlyasynciosupportederror) | This error is raised when the user tries to use sync IO in an async task. |
| [`flyte.errors.ParameterMaterializationError`](flyte.errors/parametermaterializationerror) | This error is raised when the user tries to use a Parameter in an App, that has delayed Materialization,. |
| [`flyte.errors.PrimaryContainerNotFoundError`](flyte.errors/primarycontainernotfounderror) | This error is raised when the primary container is not found. |
| [`flyte.errors.RemoteTaskNotFoundError`](flyte.errors/remotetasknotfounderror) | This error is raised when the user tries to access a task that does not exist. |
| [`flyte.errors.RemoteTaskUsageError`](flyte.errors/remotetaskusageerror) | This error is raised when the user tries to access a task that does not exist. |
| [`flyte.errors.RestrictedTypeError`](flyte.errors/restrictedtypeerror) | This error is raised when the user uses a restricted type, for example current a Tuple is not supported for one. |
| [`flyte.errors.RetriesExhaustedError`](flyte.errors/retriesexhaustederror) | This error is raised when the underlying task execution fails after all retries have been exhausted. |
| [`flyte.errors.RuntimeDataValidationError`](flyte.errors/runtimedatavalidationerror) | This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`flyte.errors.RuntimeSystemError`](flyte.errors/runtimesystemerror) | This error is raised when the underlying task execution fails because of a system error. |
| [`flyte.errors.RuntimeUnknownError`](flyte.errors/runtimeunknownerror) | This error is raised when the underlying task execution fails because of an unknown error. |
| [`flyte.errors.RuntimeUserError`](flyte.errors/runtimeusererror) | This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`flyte.errors.SlowDownError`](flyte.errors/slowdownerror) | This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`flyte.errors.TaskInterruptedError`](flyte.errors/taskinterruptederror) | This error is raised when the underlying task execution is interrupted. |
| [`flyte.errors.TaskTimeoutError`](flyte.errors/tasktimeouterror) | This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`flyte.errors.TraceDoesNotAllowNestedTasksError`](flyte.errors/tracedoesnotallownestedtaskserror) | This error is raised when the user tries to use a task from within a trace. |
| [`flyte.errors.UnionRpcError`](flyte.errors/unionrpcerror) | This error is raised when communication with the Union server fails. |
| [`flyte.extend.AsyncFunctionTaskTemplate`](flyte.extend/asyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |
| [`flyte.extend.ImageBuildEngine`](flyte.extend/imagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flyte.extend.TaskTemplate`](flyte.extend/tasktemplate) | Task template is a template for a task that can be executed. |
| [`flyte.extras.BatchStats`](flyte.extras/batchstats) | Monitoring statistics exposed by `DynamicBatcher.stats`. |
| [`flyte.extras.ContainerTask`](flyte.extras/containertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flyte.extras.DynamicBatcher`](flyte.extras/dynamicbatcher) | Batches records from many concurrent producers and runs them through. |
| [`flyte.extras.Prompt`](flyte.extras/prompt) | Simple prompt record with built-in token estimation. |
| [`flyte.extras.Sleep`](flyte.extras/sleep) | Route a task to the backend `core-sleep` plugin. |
| [`flyte.extras.SleepTask`](flyte.extras/sleeptask) |  |
| [`flyte.extras.TokenBatcher`](flyte.extras/tokenbatcher) | Token-aware batcher for LLM inference workloads. |
| [`flyte.extras.shell.FlagSpec`](flyte.extras.shell/flagspec) | How to render a typed input as a CLI flag in `{flags.<name>}`. |
| [`flyte.extras.shell.Glob`](flyte.extras.shell/glob) | A multi-file output bundle. |
| [`flyte.extras.shell.Stderr`](flyte.extras.shell/stderr) | Capture the task's stderr as a typed output. |
| [`flyte.extras.shell.Stdout`](flyte.extras.shell/stdout) | Capture the task's stdout as a typed output. |
| [`flyte.git.GitStatus`](flyte.git/gitstatus) | A class representing the status of a git repository. |
| [`flyte.io.DataFrame`](flyte.io/dataframe) | A Flyte meta DataFrame object, that wraps all other dataframe types (usually available as plugins, pandas. |
| [`flyte.io.Dir`](flyte.io/dir) | A generic directory class representing a directory with files of a specified format. |
| [`flyte.io.EmptyDir`](flyte.io/emptydir) | A sentinel `flyte.io.Dir` representing 'no directory was produced'. |
| [`flyte.io.File`](flyte.io/file) | A generic file class representing a file with a specified format. |
| [`flyte.io.HashFunction`](flyte.io/hashfunction) | A hash method that wraps a user-provided function to compute hashes. |
| [`flyte.io.extend.DataFrameDecoder`](flyte.io.extend/dataframedecoder) |  |
| [`flyte.io.extend.DataFrameEncoder`](flyte.io.extend/dataframeencoder) |  |
| [`flyte.io.extend.DataFrameTransformerEngine`](flyte.io.extend/dataframetransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flyte.models.ActionID`](flyte.models/actionid) | A class representing the ID of an Action, nested within a Run. |
| [`flyte.models.ActionPhase`](flyte.models/actionphase) | Represents the execution phase of a Flyte action (run). |
| [`flyte.models.CheckpointPaths`](flyte.models/checkpointpaths) | Paths the platform provides for this task's checkpoint output and optional previous-attempt input. |
| [`flyte.models.CodeBundle`](flyte.models/codebundle) | A class representing a code bundle for a task. |
| [`flyte.models.GroupData`](flyte.models/groupdata) |  |
| [`flyte.models.NativeInterface`](flyte.models/nativeinterface) | A class representing the native interface for a task. |
| [`flyte.models.PathRewrite`](flyte.models/pathrewrite) | Configuration for rewriting paths during input loading. |
| [`flyte.models.RawDataPath`](flyte.models/rawdatapath) | A class representing the raw data path for a task. |
| [`flyte.models.SerializationContext`](flyte.models/serializationcontext) | This object holds serialization time contextual information, that can be used when serializing the task and. |
| [`flyte.models.TaskContext`](flyte.models/taskcontext) | A context class to hold the current task executions context. |
| [`flyte.notify.Email`](flyte.notify/email) | Send email notifications. |
| [`flyte.notify.NamedDelivery`](flyte.notify/nameddelivery) | Use a pre-configured delivery channel by name. |
| [`flyte.notify.NamedRule`](flyte.notify/namedrule) | Reference a pre-defined notification rule by name. |
| [`flyte.notify.Notification`](flyte.notify/notification) | Base notification class. |
| [`flyte.notify.Slack`](flyte.notify/slack) | Send Slack notifications with optional Block Kit formatting. |
| [`flyte.notify.Teams`](flyte.notify/teams) | Send Microsoft Teams notifications with optional Adaptive Cards. |
| [`flyte.notify.Webhook`](flyte.notify/webhook) | Send custom HTTP webhook notifications (most flexible option). |
| [`flyte.prefetch.HuggingFaceModelInfo`](flyte.prefetch/huggingfacemodelinfo) | Information about a HuggingFace model to store. |
| [`flyte.prefetch.ShardConfig`](flyte.prefetch/shardconfig) | Configuration for model sharding. |
| [`flyte.prefetch.StoredModelInfo`](flyte.prefetch/storedmodelinfo) | Information about a stored model. |
| [`flyte.prefetch.VLLMShardArgs`](flyte.prefetch/vllmshardargs) | Arguments for sharding a model using vLLM. |
| [`flyte.remote.Action`](flyte.remote/action) | A class representing an action. |
| [`flyte.remote.ActionDetails`](flyte.remote/actiondetails) | A class representing an action. |
| [`flyte.remote.ActionInputs`](flyte.remote/actioninputs) | A class representing the inputs of an action. |
| [`flyte.remote.ActionOutputs`](flyte.remote/actionoutputs) | A class representing the outputs of an action. |
| [`flyte.remote.App`](flyte.remote/app) |  |
| [`flyte.remote.Artifact`](flyte.remote/artifact) | A published artifact in the Flyte artifact service: a typed value (stored as. |
| [`flyte.remote.Condition`](flyte.remote/condition) | A remote Condition registered within an action of a run. |
| [`flyte.remote.Project`](flyte.remote/project) | A class representing a project in the Union API. |
| [`flyte.remote.Run`](flyte.remote/run) | A class representing a run of a task. |
| [`flyte.remote.RunDetails`](flyte.remote/rundetails) | A class representing a run of a task. |
| [`flyte.remote.Secret`](flyte.remote/secret) |  |
| [`flyte.remote.Settings`](flyte.remote/settings) | Hierarchical configuration settings with inheritance support. |
| [`flyte.remote.Task`](flyte.remote/task) |  |
| [`flyte.remote.TaskDetails`](flyte.remote/taskdetails) |  |
| [`flyte.remote.TimeFilter`](flyte.remote/timefilter) | Filter for time-based fields (e. |
| [`flyte.remote.Trigger`](flyte.remote/trigger) | Represents a trigger in the Flyte platform. |
| [`flyte.remote.User`](flyte.remote/user) | Represents a user in the Flyte platform. |
| [`flyte.report.Report`](flyte.report/report) |  |
| [`flyte.report.Timeline`](flyte.report/timeline) | Append a best-effort chronological timeline to a tab of the task report. |
| [`flyte.sandbox.CodeTaskTemplate`](flyte.sandbox/codetasktemplate) | A sandboxed task created from a code string rather than a decorated function. |
| [`flyte.sandbox.ImageConfig`](flyte.sandbox/imageconfig) | Configuration for Docker image building at runtime. |
| [`flyte.sandbox.SandboxedConfig`](flyte.sandbox/sandboxedconfig) | Configuration for a sandboxed task executed via Monty. |
| [`flyte.sandbox.SandboxedTaskTemplate`](flyte.sandbox/sandboxedtasktemplate) | A task template that executes the function body in a Monty sandbox. |
| [`flyte.storage.ABFS`](flyte.storage/abfs) | Any Azure Blob Storage specific configuration. |
| [`flyte.storage.GCS`](flyte.storage/gcs) | Any GCS specific configuration. |
| [`flyte.storage.S3`](flyte.storage/s3) | S3 specific configuration. |
| [`flyte.storage.Storage`](flyte.storage/storage) | Data storage configuration that applies across any provider. |
| [`flyte.syncify.Syncify`](flyte.syncify/syncify) | A decorator to convert asynchronous functions or methods into synchronous ones. |
| [`flyte.types.FlytePickle`](flyte.types/flytepickle) | This type is only used by flytekit internally. |
| [`flyte.types.TypeEngine`](flyte.types/typeengine) | Core Extensible TypeEngine of Flytekit. |
| [`flyte.types.TypeTransformer`](flyte.types/typetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flyte.types.TypeTransformerFailedError`](flyte.types/typetransformerfailederror) |  |

### Protocols

| Protocol | Description |
|-|-|
| [`flyte.AppHandle`](flyte/apphandle) | Protocol defining the common interface between local and remote app handles. |
| [`flyte.CachePolicy`](flyte/cachepolicy) | Protocol for custom cache version strategies. |
| [`flyte.Link`](flyte/link) |  |
| [`flyte.ai.agents.AgentProtocol`](flyte.ai.agents/agentprotocol) | Minimal protocol that any agent must satisfy to work with. |
| [`flyte.ai.agents.protocol.AgentProtocol`](flyte.ai.agents.protocol/agentprotocol) | Minimal protocol that any agent must satisfy to work with. |
| [`flyte.artifacts.Artifact`](flyte.artifacts/artifact) | Protocol for objects wrapped with Flyte metadata. |
| [`flyte.extend.ImageBuilder`](flyte.extend/imagebuilder) |  |
| [`flyte.extend.ImageChecker`](flyte.extend/imagechecker) |  |
| [`flyte.extras.CostEstimator`](flyte.extras/costestimator) | Protocol for records that can estimate their own processing cost. |
| [`flyte.extras.TokenEstimator`](flyte.extras/tokenestimator) | Protocol for records that can estimate their own token count. |
| [`flyte.types.Renderable`](flyte.types/renderable) |  |

### Functions

| Function | Description |
|-|-|
| [`flyte.AMD_GPU()`](flyte/_index#amd_gpu) | Create an AMD GPU device instance. |
| [`flyte.GPU()`](flyte/_index#gpu) | Create a GPU device instance. |
| [`flyte.HABANA_GAUDI()`](flyte/_index#habana_gaudi) | Create a Habana Gaudi device instance. |
| [`flyte.Neuron()`](flyte/_index#neuron) | Create a Neuron device instance. |
| [`flyte.TPU()`](flyte/_index#tpu) | Create a TPU device instance. |
| [`flyte.build()`](flyte/_index#build) | Build an image. |
| [`flyte.build_images()`](flyte/_index#build_images) | Build the images for the given environment(s). |
| [`flyte.ctx()`](flyte/_index#ctx) | Returns the current flyte. |
| [`flyte.current_domain()`](flyte/_index#current_domain) | Returns the current domain from Runtime environment (on the cluster) or from the initialized configuration. |
| [`flyte.current_project()`](flyte/_index#current_project) | Returns the current project from the Runtime environment (on the cluster) or from the initialized configuration. |
| [`flyte.custom_context()`](flyte/_index#custom_context) | Synchronous context manager to set input context for tasks spawned within this block. |
| [`flyte.deploy()`](flyte/_index#deploy) | Deploy the given environment or list of environments. |
| [`flyte.get_custom_context()`](flyte/_index#get_custom_context) | Get the current input context. |
| [`flyte.group()`](flyte/_index#group) | Create a new group with the given name. |
| [`flyte.init()`](flyte/_index#init) | Initialize the Flyte system with the given configuration. |
| [`flyte.init_from_api_key()`](flyte/_index#init_from_api_key) | Initialize the Flyte system using an API key for authentication. |
| [`flyte.init_from_config()`](flyte/_index#init_from_config) | Initialize the Flyte system using a configuration file or Config object. |
| [`flyte.init_in_cluster()`](flyte/_index#init_in_cluster) |  |
| [`flyte.init_passthrough()`](flyte/_index#init_passthrough) | Initialize the Flyte system with passthrough authentication. |
| [`flyte.latest_checkpoint()`](flyte/_index#latest_checkpoint) | Return the file under *root* matching *glob_pattern* with the largest `key(path)`, or `None`. |
| [`flyte.load_interactive_ctx()`](flyte/_index#load_interactive_ctx) | Restore the task execution context from the config file written by a debug-mode task pod. |
| [`flyte.load_plugin_config()`](flyte/_index#load_plugin_config) | Load a plugin config instance from a YAML file. |
| [`flyte.map()`](flyte/_index#map) | Map a function over the provided arguments with concurrent execution. |
| [`flyte.new_condition()`](flyte/_index#new_condition) | Create a condition that can be awaited in a workflow. |
| [`flyte.rerun()`](flyte/_index#rerun) | Re-run a prior run, returning a new `Run`. |
| [`flyte.run()`](flyte/_index#run) | Run a task with the given parameters. |
| [`flyte.run_python_script()`](flyte/_index#run_python_script) | Package and run a Python script on a remote Flyte cluster. |
| [`flyte.serve()`](flyte/_index#serve) | Serve a Flyte app using an AppEnvironment. |
| [`flyte.trace()`](flyte/_index#trace) | A decorator that traces function execution with timing information. |
| [`flyte.version()`](flyte/_index#version) | Returns the version of the Flyte SDK. |
| [`flyte.with_runcontext()`](flyte/_index#with_runcontext) | Launch a new run with the given parameters as the context. |
| [`flyte.with_servecontext()`](flyte/_index#with_servecontext) | Create a serve context with custom configuration. |
| [`flyte.ai.agents.tool()`](flyte.ai.agents/_index#tool) | Wrap a task, `@flyte.trace` helper, plain callable, or `LazyEntity` as a `flyte.ai.agents.AgentTool`. |
| [`flyte.ai.chat.build_chat_html()`](flyte.ai.chat/_index#build_chat_html) | Build the full chat HTML with the given *title* and optional *custom_css*. |
| [`flyte.ai.mcp.resolve_tools()`](flyte.ai.mcp/_index#resolve_tools) | Return the set of MCP tool names to expose. |
| [`flyte.app.ctx()`](flyte.app/_index#ctx) | Returns the current app context. |
| [`flyte.app.get_parameter()`](flyte.app/_index#get_parameter) | Get parameters for application or endpoint. |
| [`flyte.artifacts.new()`](flyte.artifacts/_index#new) | Wrap an object with Flyte metadata while preserving its type interface. |
| [`flyte.config.auto()`](flyte.config/_index#auto) | Automatically constructs the Config Object. |
| [`flyte.config.set_if_exists()`](flyte.config/_index#set_if_exists) | Given a dict `d` sets the key `k` with value of config `v`, if the config value `v` is set. |
| [`flyte.connectors.utils.convert_to_flyte_phase()`](flyte.connectors.utils/_index#convert_to_flyte_phase) | Convert the state from the connector to the phase in flyte. |
| [`flyte.connectors.utils.is_terminal_phase()`](flyte.connectors.utils/_index#is_terminal_phase) | Return true if the phase is terminal. |
| [`flyte.connectors.utils.print_metadata()`](flyte.connectors.utils/_index#print_metadata) |  |
| [`flyte.durable.now()`](flyte.durable/_index#now) | Returns the current time for every unique invocation of durable_time. |
| [`flyte.durable.sleep()`](flyte.durable/_index#sleep) | durable_sleep enables the process to sleep for `seconds` seconds even if the process recovers from a crash. |
| [`flyte.durable.time()`](flyte.durable/_index#time) | Returns the current time for every unique invocation of durable_time. |
| [`flyte.errors.silence_polling_error()`](flyte.errors/_index#silence_polling_error) | Suppress specific polling errors in the event loop. |
| [`flyte.extend.download_code_bundle()`](flyte.extend/_index#download_code_bundle) | Downloads the code bundle if it is not already downloaded. |
| [`flyte.extend.get_proto_extended_resources()`](flyte.extend/_index#get_proto_extended_resources) | TODO Implement partitioning logic string handling for GPU. |
| [`flyte.extend.get_proto_resources()`](flyte.extend/_index#get_proto_resources) | Get main resources IDL representation from the resources object. |
| [`flyte.extend.is_initialized()`](flyte.extend/_index#is_initialized) | Check if the system has been initialized. |
| [`flyte.extend.lazy_module()`](flyte.extend/_index#lazy_module) | This function is used to lazily import modules. |
| [`flyte.extend.pod_spec_from_resources()`](flyte.extend/_index#pod_spec_from_resources) |  |
| [`flyte.extras.serialize()`](flyte.extras/_index#serialize) | Translate a single task to its wire TaskSpec, offline and code-agnostic. |
| [`flyte.extras.serialize_env()`](flyte.extras/_index#serialize_env) | Serialize every task in an environment. |
| [`flyte.extras.shell.create()`](flyte.extras.shell/_index#create) | Wrap a CLI tool packaged in a container as a Flyte task. |
| [`flyte.git.config_from_root()`](flyte.git/_index#config_from_root) | Get the config file from the git root directory. |
| [`flyte.models.generate_random_name()`](flyte.models/_index#generate_random_name) | Generate a random name for the task. |
| [`flyte.prefetch.hf_model()`](flyte.prefetch/_index#hf_model) | Store a HuggingFace model to remote storage. |
| [`flyte.remote.auth_metadata()`](flyte.remote/_index#auth_metadata) | This context manager allows you to pass contextualized auth metadata downstream to the Flyte authentication system. |
| [`flyte.remote.upload_dir()`](flyte.remote/_index#upload_dir) | Uploads a directory to a remote location and returns the remote URI. |
| [`flyte.remote.upload_file()`](flyte.remote/_index#upload_file) | Uploads a file to a remote location and returns the remote URI. |
| [`flyte.report.abbreviate()`](flyte.report/_index#abbreviate) | HTML-escape `value` for a report row. |
| [`flyte.report.current_report()`](flyte.report/_index#current_report) | Get the current report. |
| [`flyte.report.duration_ms()`](flyte.report/_index#duration_ms) | Format the gap between two ISO-8601 timestamps as `"<n> ms"` (best-effort). |
| [`flyte.report.flush()`](flyte.report/_index#flush) | Flush the report. |
| [`flyte.report.get_tab()`](flyte.report/_index#get_tab) | Get a tab by name. |
| [`flyte.report.log()`](flyte.report/_index#log) | Log content to the main tab. |
| [`flyte.report.replace()`](flyte.report/_index#replace) | Get the report. |
| [`flyte.sandbox.create()`](flyte.sandbox/_index#create) | Create a stateless Python code sandbox. |
| [`flyte.sandbox.orchestrate_local()`](flyte.sandbox/_index#orchestrate_local) | One-shot local execution of a code string in the Monty sandbox. |
| [`flyte.sandbox.orchestrator_from_str()`](flyte.sandbox/_index#orchestrator_from_str) | Create a reusable sandboxed task from a code string. |
| [`flyte.storage.exists()`](flyte.storage/_index#exists) | Check if a path exists. |
| [`flyte.storage.exists_sync()`](flyte.storage/_index#exists_sync) |  |
| [`flyte.storage.get()`](flyte.storage/_index#get) |  |
| [`flyte.storage.get_configured_fsspec_kwargs()`](flyte.storage/_index#get_configured_fsspec_kwargs) |  |
| [`flyte.storage.get_random_local_directory()`](flyte.storage/_index#get_random_local_directory) | pathlib. |
| [`flyte.storage.get_random_local_path()`](flyte.storage/_index#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name. |
| [`flyte.storage.get_stream()`](flyte.storage/_index#get_stream) | Get a stream of data from a remote location. |
| [`flyte.storage.get_underlying_filesystem()`](flyte.storage/_index#get_underlying_filesystem) |  |
| [`flyte.storage.is_remote()`](flyte.storage/_index#is_remote) | Let's find a replacement. |
| [`flyte.storage.join()`](flyte.storage/_index#join) | Join multiple paths together. |
| [`flyte.storage.open()`](flyte.storage/_index#open) | Asynchronously open a file and return an async context manager. |
| [`flyte.storage.put()`](flyte.storage/_index#put) |  |
| [`flyte.storage.put_stream()`](flyte.storage/_index#put_stream) | Put a stream of data to a remote location. |
| [`flyte.types.guess_interface()`](flyte.types/_index#guess_interface) | Returns the interface of the task with guessed types, as types may not be present in current env. |
| [`flyte.types.literal_string_repr()`](flyte.types/_index#literal_string_repr) | This method is used to convert a literal map to a string representation. |

### Packages

| Package | Description |
|-|-|
| [`flyte`](flyte/_index) | Flyte SDK for authoring compound AI applications, services and workflows. |
| [`flyte.ai.agents`](flyte.ai.agents/_index) | flyte. |
| [`flyte.ai.agents.agent`](flyte.ai.agents.agent/_index) | Agent — a flyte-native tool-use agent harness. |
| [`flyte.ai.agents.memory`](flyte.ai.agents.memory/_index) | Dir-backed memory for `flyte.ai.agents.Agent`. |
| [`flyte.ai.agents.protocol`](flyte.ai.agents.protocol/_index) | Agent protocol for the flyte. |
| [`flyte.ai.chat`](flyte.ai.chat/_index) | flyte. |
| [`flyte.ai.chat.app`](flyte.ai.chat.app/_index) | AgentChatAppEnvironment — FastAPI-based chat UI for any Agent. |
| [`flyte.ai.mcp`](flyte.ai.mcp/_index) |  |
| [`flyte.app`](flyte.app/_index) |  |
| [`flyte.app.extras`](flyte.app.extras/_index) |  |
| [`flyte.artifacts`](flyte.artifacts/_index) | Artifacts module. |
| [`flyte.clustered`](flyte.clustered/_index) |  |
| [`flyte.config`](flyte.config/_index) |  |
| [`flyte.connectors`](flyte.connectors/_index) |  |
| [`flyte.connectors.utils`](flyte.connectors.utils/_index) |  |
| [`flyte.durable`](flyte.durable/_index) | Flyte durable utilities. |
| [`flyte.errors`](flyte.errors/_index) | Exceptions raised by Union. |
| [`flyte.extend`](flyte.extend/_index) |  |
| [`flyte.extras`](flyte.extras/_index) | Flyte extras package. |
| [`flyte.extras.shell`](flyte.extras.shell/_index) | Shell task — wrap a CLI tool packaged in a container image. |
| [`flyte.git`](flyte.git/_index) |  |
| [`flyte.io`](flyte.io/_index) | ## IO data types. |
| [`flyte.io.extend`](flyte.io.extend/_index) |  |
| [`flyte.models`](flyte.models/_index) |  |
| [`flyte.notify`](flyte.notify/_index) | Task Notifications API for Flyte 2. |
| [`flyte.prefetch`](flyte.prefetch/_index) | Prefetch utilities for Flyte. |
| [`flyte.remote`](flyte.remote/_index) | Remote Entities that are accessible from the Union Server once deployed or created. |
| [`flyte.report`](flyte.report/_index) |  |
| [`flyte.sandbox`](flyte.sandbox/_index) | Sandbox utilities for running isolated code inside Flyte tasks. |
| [`flyte.storage`](flyte.storage/_index) |  |
| [`flyte.syncify`](flyte.syncify/_index) | # Syncify Module. |
| [`flyte.types`](flyte.types/_index) | # Flyte Type System. |

