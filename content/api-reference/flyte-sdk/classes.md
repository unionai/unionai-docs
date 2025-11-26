---
title: Classes & Protocols
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flyte.Cache`](../packages/flyte#flytecache) |Cache configuration for a task. |
| [`flyte.Cron`](../packages/flyte#flytecron) |This class defines a Cron automation that can be associated with a Trigger in Flyte. |
| [`flyte.Device`](../packages/flyte#flytedevice) |Represents a device type, its quantity and partition if applicable. |
| [`flyte.Environment`](../packages/flyte#flyteenvironment) | |
| [`flyte.FixedRate`](../packages/flyte#flytefixedrate) |This class defines a FixedRate automation that can be associated with a Trigger in Flyte. |
| [`flyte.Image`](../packages/flyte#flyteimage) |This is a representation of Container Images, which can be used to create layered images programmatically. |
| [`flyte.PodTemplate`](../packages/flyte#flytepodtemplate) |Custom PodTemplate specification for a Task. |
| [`flyte.Resources`](../packages/flyte#flyteresources) |Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`flyte.RetryStrategy`](../packages/flyte#flyteretrystrategy) |Retry strategy for the task or task environment. |
| [`flyte.ReusePolicy`](../packages/flyte#flytereusepolicy) |ReusePolicy can be used to configure a task to reuse the environment. |
| [`flyte.Secret`](../packages/flyte#flytesecret) |Secrets are used to inject sensitive information into tasks or image build context. |
| [`flyte.TaskEnvironment`](../packages/flyte#flytetaskenvironment) |Environment class to define a new environment for a set of tasks. |
| [`flyte.Timeout`](../packages/flyte#flytetimeout) |Timeout class to define a timeout for a task. |
| [`flyte.Trigger`](../packages/flyte#flytetrigger) |This class defines specification of a Trigger, that can be associated with any Flyte V2 task. |
| [`flyte.app.AppEnvironment`](../packages/flyte.app#flyteappappenvironment) | |
| [`flyte.app.Domain`](../packages/flyte.app#flyteappdomain) | |
| [`flyte.app.Input`](../packages/flyte.app#flyteappinput) |Input for application. |
| [`flyte.app.Link`](../packages/flyte.app#flyteapplink) | |
| [`flyte.app.Port`](../packages/flyte.app#flyteappport) | |
| [`flyte.app.Scaling`](../packages/flyte.app#flyteappscaling) | |
| [`flyte.app.extras.FastAPIAppEnvironment`](../packages/flyte.app.extras#flyteappextrasfastapiappenvironment) | |
| [`flyte.config.Config`](../packages/flyte.config#flyteconfigconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flyte.connectors.AsyncConnector`](../packages/flyte.connectors#flyteconnectorsasyncconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyte.connectors.AsyncConnectorExecutorMixin`](../packages/flyte.connectors#flyteconnectorsasyncconnectorexecutormixin) |This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyte.connectors.ConnectorRegistry`](../packages/flyte.connectors#flyteconnectorsconnectorregistry) |This is the registry for all connectors. |
| [`flyte.connectors.ConnectorService`](../packages/flyte.connectors#flyteconnectorsconnectorservice) | |
| [`flyte.connectors.Resource`](../packages/flyte.connectors#flyteconnectorsresource) |This is the output resource of the job. |
| [`flyte.connectors.ResourceMeta`](../packages/flyte.connectors#flyteconnectorsresourcemeta) |This is the metadata for the job. |
| [`flyte.errors.ActionNotFoundError`](../packages/flyte.errors#flyteerrorsactionnotfounderror) |This error is raised when the user tries to access an action that does not exist. |
| [`flyte.errors.BaseRuntimeError`](../packages/flyte.errors#flyteerrorsbaseruntimeerror) |Base class for all Union runtime errors. |
| [`flyte.errors.CustomError`](../packages/flyte.errors#flyteerrorscustomerror) |This error is raised when the user raises a custom error. |
| [`flyte.errors.DeploymentError`](../packages/flyte.errors#flyteerrorsdeploymenterror) |This error is raised when the deployment of a task fails, or some preconditions for deployment are not met. |
| [`flyte.errors.ImageBuildError`](../packages/flyte.errors#flyteerrorsimagebuilderror) |This error is raised when the image build fails. |
| [`flyte.errors.ImagePullBackOffError`](../packages/flyte.errors#flyteerrorsimagepullbackofferror) |This error is raised when the image cannot be pulled. |
| [`flyte.errors.InitializationError`](../packages/flyte.errors#flyteerrorsinitializationerror) |This error is raised when the Union system is tried to access without being initialized. |
| [`flyte.errors.InlineIOMaxBytesBreached`](../packages/flyte.errors#flyteerrorsinlineiomaxbytesbreached) |This error is raised when the inline IO max bytes limit is breached. |
| [`flyte.errors.InvalidImageNameError`](../packages/flyte.errors#flyteerrorsinvalidimagenameerror) |This error is raised when the image name is invalid. |
| [`flyte.errors.LogsNotYetAvailableError`](../packages/flyte.errors#flyteerrorslogsnotyetavailableerror) |This error is raised when the logs are not yet available for a task. |
| [`flyte.errors.ModuleLoadError`](../packages/flyte.errors#flyteerrorsmoduleloaderror) |This error is raised when the module cannot be loaded, either because it does not exist or because of a. |
| [`flyte.errors.NotInTaskContextError`](../packages/flyte.errors#flyteerrorsnotintaskcontexterror) |This error is raised when the user tries to access the task context outside of a task. |
| [`flyte.errors.OOMError`](../packages/flyte.errors#flyteerrorsoomerror) |This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`flyte.errors.OnlyAsyncIOSupportedError`](../packages/flyte.errors#flyteerrorsonlyasynciosupportederror) |This error is raised when the user tries to use sync IO in an async task. |
| [`flyte.errors.PrimaryContainerNotFoundError`](../packages/flyte.errors#flyteerrorsprimarycontainernotfounderror) |This error is raised when the primary container is not found. |
| [`flyte.errors.ReferenceTaskError`](../packages/flyte.errors#flyteerrorsreferencetaskerror) |This error is raised when the user tries to access a task that does not exist. |
| [`flyte.errors.RetriesExhaustedError`](../packages/flyte.errors#flyteerrorsretriesexhaustederror) |This error is raised when the underlying task execution fails after all retries have been exhausted. |
| [`flyte.errors.RunAbortedError`](../packages/flyte.errors#flyteerrorsrunabortederror) |This error is raised when the run is aborted by the user. |
| [`flyte.errors.RuntimeDataValidationError`](../packages/flyte.errors#flyteerrorsruntimedatavalidationerror) |This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`flyte.errors.RuntimeSystemError`](../packages/flyte.errors#flyteerrorsruntimesystemerror) |This error is raised when the underlying task execution fails because of a system error. |
| [`flyte.errors.RuntimeUnknownError`](../packages/flyte.errors#flyteerrorsruntimeunknownerror) |This error is raised when the underlying task execution fails because of an unknown error. |
| [`flyte.errors.RuntimeUserError`](../packages/flyte.errors#flyteerrorsruntimeusererror) |This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`flyte.errors.SlowDownError`](../packages/flyte.errors#flyteerrorsslowdownerror) |This error is raised when the user tries to access a resource that does not exist or is invalid. |
| [`flyte.errors.TaskInterruptedError`](../packages/flyte.errors#flyteerrorstaskinterruptederror) |This error is raised when the underlying task execution is interrupted. |
| [`flyte.errors.TaskTimeoutError`](../packages/flyte.errors#flyteerrorstasktimeouterror) |This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`flyte.errors.UnionRpcError`](../packages/flyte.errors#flyteerrorsunionrpcerror) |This error is raised when communication with the Union server fails. |
| [`flyte.extend.AsyncFunctionTaskTemplate`](../packages/flyte.extend#flyteextendasyncfunctiontasktemplate) |A task template that wraps an asynchronous functions. |
| [`flyte.extend.ImageBuildEngine`](../packages/flyte.extend#flyteextendimagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flyte.extend.TaskTemplate`](../packages/flyte.extend#flyteextendtasktemplate) |Task template is a template for a task that can be executed. |
| [`flyte.extras.ContainerTask`](../packages/flyte.extras#flyteextrascontainertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flyte.io.DataFrame`](../packages/flyte.io#flyteiodataframe) |This is the user facing DataFrame class. |
| [`flyte.io.DataFrameDecoder`](../packages/flyte.io#flyteiodataframedecoder) |Helper class that provides a standard way to create an ABC using. |
| [`flyte.io.DataFrameEncoder`](../packages/flyte.io#flyteiodataframeencoder) |Helper class that provides a standard way to create an ABC using. |
| [`flyte.io.DataFrameTransformerEngine`](../packages/flyte.io#flyteiodataframetransformerengine) |Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flyte.io.Dir`](../packages/flyte.io#flyteiodir) |A generic directory class representing a directory with files of a specified format. |
| [`flyte.io.File`](../packages/flyte.io#flyteiofile) |A generic file class representing a file with a specified format. |
| [`flyte.models.ActionID`](../packages/flyte.models#flytemodelsactionid) |A class representing the ID of an Action, nested within a Run. |
| [`flyte.models.Checkpoints`](../packages/flyte.models#flytemodelscheckpoints) |A class representing the checkpoints for a task. |
| [`flyte.models.CodeBundle`](../packages/flyte.models#flytemodelscodebundle) |A class representing a code bundle for a task. |
| [`flyte.models.GroupData`](../packages/flyte.models#flytemodelsgroupdata) | |
| [`flyte.models.NativeInterface`](../packages/flyte.models#flytemodelsnativeinterface) |A class representing the native interface for a task. |
| [`flyte.models.PathRewrite`](../packages/flyte.models#flytemodelspathrewrite) |Configuration for rewriting paths during input loading. |
| [`flyte.models.RawDataPath`](../packages/flyte.models#flytemodelsrawdatapath) |A class representing the raw data path for a task. |
| [`flyte.models.SerializationContext`](../packages/flyte.models#flytemodelsserializationcontext) |This object holds serialization time contextual information, that can be used when serializing the task and. |
| [`flyte.models.TaskContext`](../packages/flyte.models#flytemodelstaskcontext) |A context class to hold the current task executions context. |
| [`flyte.remote.Action`](../packages/flyte.remote#flyteremoteaction) |A class representing an action. |
| [`flyte.remote.ActionDetails`](../packages/flyte.remote#flyteremoteactiondetails) |A class representing an action. |
| [`flyte.remote.ActionInputs`](../packages/flyte.remote#flyteremoteactioninputs) |A class representing the inputs of an action. |
| [`flyte.remote.ActionOutputs`](../packages/flyte.remote#flyteremoteactionoutputs) |A class representing the outputs of an action. |
| [`flyte.remote.App`](../packages/flyte.remote#flyteremoteapp) |A mixin class that provides a method to convert an object to a JSON-serializable dictionary. |
| [`flyte.remote.Project`](../packages/flyte.remote#flyteremoteproject) |A class representing a project in the Union API. |
| [`flyte.remote.Run`](../packages/flyte.remote#flyteremoterun) |A class representing a run of a task. |
| [`flyte.remote.RunDetails`](../packages/flyte.remote#flyteremoterundetails) |A class representing a run of a task. |
| [`flyte.remote.Secret`](../packages/flyte.remote#flyteremotesecret) | |
| [`flyte.remote.Task`](../packages/flyte.remote#flyteremotetask) | |
| [`flyte.remote.TaskDetails`](../packages/flyte.remote#flyteremotetaskdetails) | |
| [`flyte.remote.Trigger`](../packages/flyte.remote#flyteremotetrigger) | |
| [`flyte.remote.User`](../packages/flyte.remote#flyteremoteuser) | |
| [`flyte.report.Report`](../packages/flyte.report#flytereportreport) | |
| [`flyte.storage.ABFS`](../packages/flyte.storage#flytestorageabfs) |Any Azure Blob Storage specific configuration. |
| [`flyte.storage.GCS`](../packages/flyte.storage#flytestoragegcs) |Any GCS specific configuration. |
| [`flyte.storage.S3`](../packages/flyte.storage#flytestorages3) |S3 specific configuration. |
| [`flyte.storage.Storage`](../packages/flyte.storage#flytestoragestorage) |Data storage configuration that applies across any provider. |
| [`flyte.syncify.Syncify`](../packages/flyte.syncify#flytesyncifysyncify) |A decorator to convert asynchronous functions or methods into synchronous ones. |
| [`flyte.types.FlytePickle`](../packages/flyte.types#flytetypesflytepickle) |This type is only used by flytekit internally. |
| [`flyte.types.TypeEngine`](../packages/flyte.types#flytetypestypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flyte.types.TypeTransformer`](../packages/flyte.types#flytetypestypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flyte.types.TypeTransformerFailedError`](../packages/flyte.types#flytetypestypetransformerfailederror) |Inappropriate argument type. |
# Protocols

| Protocol | Description |
|-|-|
| [`flyte.CachePolicy`](../packages/flyte#flytecachepolicy) |Base class for protocol classes. |
| [`flyte.types.Renderable`](../packages/flyte.types#flytetypesrenderable) |Base class for protocol classes. |
