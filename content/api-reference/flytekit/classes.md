---
title: Classes
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flytekit.Annotations`](../packages/flytekit#flytekitannotations) | |
| [`flytekit.Artifact`](../packages/flytekit#flytekitartifact) |An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.AuthRole`](../packages/flytekit#flytekitauthrole) | |
| [`flytekit.BatchSize`](../packages/flytekit#flytekitbatchsize) |This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`flytekit.Blob`](../packages/flytekit#flytekitblob) | |
| [`flytekit.BlobMetadata`](../packages/flytekit#flytekitblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.BlobType`](../packages/flytekit#flytekitblobtype) |This type represents offloaded data and is typically used for things like files. |
| [`flytekit.Cache`](../packages/flytekit#flytekitcache) |Cache configuration for a task. |
| [`flytekit.CachePolicy`](../packages/flytekit#flytekitcachepolicy) |Base class for protocol classes. |
| [`flytekit.Checkpoint`](../packages/flytekit#flytekitcheckpoint) |Base class for Checkpoint system. |
| [`flytekit.Config`](../packages/flytekit#flytekitconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.ContainerTask`](../packages/flytekit#flytekitcontainertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flytekit.CronSchedule`](../packages/flytekit#flytekitcronschedule) |Use this when you have a launch plan that you want to run on a cron expression. |
| [`flytekit.Deck`](../packages/flytekit#flytekitdeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.Description`](../packages/flytekit#flytekitdescription) |Full user description with formatting preserved. |
| [`flytekit.Documentation`](../packages/flytekit#flytekitdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.Email`](../packages/flytekit#flytekitemail) |This notification should be used when sending regular emails to people. |
| [`flytekit.Environment`](../packages/flytekit#flytekitenvironment) | |
| [`flytekit.ExecutionParameters`](../packages/flytekit#flytekitexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.FixedRate`](../packages/flytekit#flytekitfixedrate) |Use this class to schedule a fixed-rate interval for a launch plan. |
| [`flytekit.FlyteContext`](../packages/flytekit#flytekitflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.FlyteContextManager`](../packages/flytekit#flytekitflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.FlyteDirectory`](../packages/flytekit#flytekitflytedirectory) | |
| [`flytekit.FlyteFile`](../packages/flytekit#flytekitflytefile) | |
| [`flytekit.FlyteRemote`](../packages/flytekit#flytekitflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.HashMethod`](../packages/flytekit#flytekithashmethod) |Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.ImageSpec`](../packages/flytekit#flytekitimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.Labels`](../packages/flytekit#flytekitlabels) | |
| [`flytekit.LaunchPlan`](../packages/flytekit#flytekitlaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.LaunchPlanReference`](../packages/flytekit#flytekitlaunchplanreference) |A reference object containing metadata that points to a remote launch plan. |
| [`flytekit.Literal`](../packages/flytekit#flytekitliteral) | |
| [`flytekit.LiteralType`](../packages/flytekit#flytekitliteraltype) | |
| [`flytekit.Options`](../packages/flytekit#flytekitoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.PagerDuty`](../packages/flytekit#flytekitpagerduty) |This notification should be used when sending emails to the PagerDuty service. |
| [`flytekit.PodTemplate`](../packages/flytekit#flytekitpodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.PythonFunctionTask`](../packages/flytekit#flytekitpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.PythonInstanceTask`](../packages/flytekit#flytekitpythoninstancetask) |This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.Resources`](../packages/flytekit#flytekitresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.SQLTask`](../packages/flytekit#flytekitsqltask) |Base task types for all SQL tasks. |
| [`flytekit.Scalar`](../packages/flytekit#flytekitscalar) | |
| [`flytekit.Secret`](../packages/flytekit#flytekitsecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.SecurityContext`](../packages/flytekit#flytekitsecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.SensorEngine`](../packages/flytekit#flytekitsensorengine) |This is the base class for all async connectors. |
| [`flytekit.Slack`](../packages/flytekit#flytekitslack) |This notification should be used when sending emails to the Slack. |
| [`flytekit.SourceCode`](../packages/flytekit#flytekitsourcecode) |Link to source code used to define this task or workflow. |
| [`flytekit.StructuredDataset`](../packages/flytekit#flytekitstructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.StructuredDatasetFormat`](../packages/flytekit#flytekitstructureddatasetformat) |str(object='') -> str. |
| [`flytekit.StructuredDatasetTransformerEngine`](../packages/flytekit#flytekitstructureddatasettransformerengine) |Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flytekit.StructuredDatasetType`](../packages/flytekit#flytekitstructureddatasettype) | |
| [`flytekit.TaskMetadata`](../packages/flytekit#flytekittaskmetadata) |Metadata for a Task. |
| [`flytekit.TaskReference`](../packages/flytekit#flytekittaskreference) |A reference object containing metadata that points to a remote task. |
| [`flytekit.VersionParameters`](../packages/flytekit#flytekitversionparameters) |Parameters used for version hash generation. |
| [`flytekit.Workflow`](../packages/flytekit#flytekitworkflow) |An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`flytekit.WorkflowExecutionPhase`](../packages/flytekit#flytekitworkflowexecutionphase) |This class holds enum values used for setting notifications. |
| [`flytekit.WorkflowFailurePolicy`](../packages/flytekit#flytekitworkflowfailurepolicy) |Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.WorkflowReference`](../packages/flytekit#flytekitworkflowreference) |A reference object containing metadata that points to a remote workflow. |
| [`flytekit.bin.entrypoint.ExecutionParameters`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.bin.entrypoint.ExecutionState`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.bin.entrypoint.FastSerializationSettings`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointfastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.bin.entrypoint.FileAccessProvider`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointfileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.bin.entrypoint.FlyteContext`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.bin.entrypoint.FlyteContextManager`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.bin.entrypoint.FlyteException`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointflyteexception) |Common base class for all non-exit exceptions. |
| [`flytekit.bin.entrypoint.FlyteNonRecoverableSystemException`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointflytenonrecoverablesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.bin.entrypoint.FlyteRecoverableException`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointflyterecoverableexception) |Common base class for all non-exit exceptions. |
| [`flytekit.bin.entrypoint.FlyteUserRuntimeException`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointflyteuserruntimeexception) |Common base class for all non-exit exceptions. |
| [`flytekit.bin.entrypoint.IgnoreOutputs`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointignoreoutputs) |This exception should be used to indicate that the outputs generated by this can be safely ignored. |
| [`flytekit.bin.entrypoint.ImageConfig`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.bin.entrypoint.OutputMetadataTracker`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointoutputmetadatatracker) |This class is for the users to set arbitrary metadata on output literals. |
| [`flytekit.bin.entrypoint.PythonTask`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.bin.entrypoint.SerializationSettings`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.bin.entrypoint.StatsConfig`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointstatsconfig) |Configuration for sending statsd. |
| [`flytekit.bin.entrypoint.SyncCheckpoint`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointsynccheckpoint) |This class is NOT THREAD-SAFE!. |
| [`flytekit.bin.entrypoint.Timestamp`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointtimestamp) |A ProtocolMessage. |
| [`flytekit.bin.entrypoint.VoidPromise`](../packages/flytekit.bin.entrypoint#flytekitbinentrypointvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.clients.auth.auth_client.AccessTokenNotFoundError`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientaccesstokennotfounderror) |This error is raised with Access token is not found or if Refreshing the token fails. |
| [`flytekit.clients.auth.auth_client.AuthorizationClient`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationclient) |Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`flytekit.clients.auth.auth_client.AuthorizationCode`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationcode) | |
| [`flytekit.clients.auth.auth_client.Credentials`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientcredentials) |Stores the credentials together. |
| [`flytekit.clients.auth.auth_client.EndpointMetadata`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientendpointmetadata) |This class can be used to control the rendering of the page on login successful or failure. |
| [`flytekit.clients.auth.auth_client.OAuthCallbackHandler`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthcallbackhandler) |A simple wrapper around BaseHTTPServer. |
| [`flytekit.clients.auth.auth_client.OAuthHTTPServer`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthhttpserver) |A simple wrapper around the BaseHTTPServer. |
| [`flytekit.clients.auth.auth_client.Queue`](../packages/flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientqueue) |Create a queue object with a given maximum size. |
| [`flytekit.clients.auth.authenticator.AccessTokenNotFoundError`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatoraccesstokennotfounderror) |This error is raised with Access token is not found or if Refreshing the token fails. |
| [`flytekit.clients.auth.authenticator.AuthenticationError`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticationerror) |This is raised for any AuthenticationError. |
| [`flytekit.clients.auth.authenticator.AuthenticationPending`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticationpending) |This is raised if the token endpoint returns authentication pending. |
| [`flytekit.clients.auth.authenticator.Authenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticator) |Base authenticator for all authentication flows. |
| [`flytekit.clients.auth.authenticator.AuthorizationClient`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthorizationclient) |Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`flytekit.clients.auth.authenticator.ClientConfig`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfig) |Client Configuration that is needed by the authenticator. |
| [`flytekit.clients.auth.authenticator.ClientConfigStore`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfigstore) |Client Config store retrieve client config. |
| [`flytekit.clients.auth.authenticator.ClientCredentialsAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientcredentialsauthenticator) |This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`flytekit.clients.auth.authenticator.CommandAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcommandauthenticator) |This Authenticator retrieves access_token using the provided command. |
| [`flytekit.clients.auth.authenticator.Credentials`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcredentials) |Stores the credentials together. |
| [`flytekit.clients.auth.authenticator.DeviceCodeAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatordevicecodeauthenticator) |This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`flytekit.clients.auth.authenticator.KeyringStore`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorkeyringstore) |Methods to access Keyring Store. |
| [`flytekit.clients.auth.authenticator.PKCEAuthenticator`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorpkceauthenticator) |This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`flytekit.clients.auth.authenticator.StaticClientConfigStore`](../packages/flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorstaticclientconfigstore) |Client Config store retrieve client config. |
| [`flytekit.clients.auth.default_html.suppress`](../packages/flytekit.clients.auth.default_html#flytekitclientsauthdefault_htmlsuppress) |Context manager to suppress specified exceptions. |
| [`flytekit.clients.auth.exceptions.AccessTokenNotFoundError`](../packages/flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsaccesstokennotfounderror) |This error is raised with Access token is not found or if Refreshing the token fails. |
| [`flytekit.clients.auth.exceptions.AuthenticationError`](../packages/flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsauthenticationerror) |This is raised for any AuthenticationError. |
| [`flytekit.clients.auth.exceptions.AuthenticationPending`](../packages/flytekit.clients.auth.exceptions#flytekitclientsauthexceptionsauthenticationpending) |This is raised if the token endpoint returns authentication pending. |
| [`flytekit.clients.auth.keyring.Credentials`](../packages/flytekit.clients.auth.keyring#flytekitclientsauthkeyringcredentials) |Stores the credentials together. |
| [`flytekit.clients.auth.keyring.KeyringStore`](../packages/flytekit.clients.auth.keyring#flytekitclientsauthkeyringkeyringstore) |Methods to access Keyring Store. |
| [`flytekit.clients.auth.keyring.NoKeyringError`](../packages/flytekit.clients.auth.keyring#flytekitclientsauthkeyringnokeyringerror) |Raised when there is no keyring backend. |
| [`flytekit.clients.auth.keyring.PasswordDeleteError`](../packages/flytekit.clients.auth.keyring#flytekitclientsauthkeyringpassworddeleteerror) |Raised when the password can't be deleted. |
| [`flytekit.clients.auth.token_client.AuthenticationError`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientauthenticationerror) |This is raised for any AuthenticationError. |
| [`flytekit.clients.auth.token_client.AuthenticationPending`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientauthenticationpending) |This is raised if the token endpoint returns authentication pending. |
| [`flytekit.clients.auth.token_client.DeviceCodeResponse`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdevicecoderesponse) |Response from device auth flow endpoint. |
| [`flytekit.clients.auth.token_client.GrantType`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientgranttype) |str(object='') -> str. |
| [`flytekit.clients.auth.token_client.datetime`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.clients.auth.token_client.timedelta`](../packages/flytekit.clients.auth.token_client#flytekitclientsauthtoken_clienttimedelta) |Difference between two datetime values. |
| [`flytekit.clients.auth_helper.AuthMetadataServiceStub`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperauthmetadataservicestub) |The following defines an RPC service that is also served over HTTP via grpc-gateway. |
| [`flytekit.clients.auth_helper.AuthType`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperauthtype) |Create a collection of name/value pairs. |
| [`flytekit.clients.auth_helper.AuthUnaryInterceptor`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperauthunaryinterceptor) |This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`flytekit.clients.auth_helper.AuthenticationHTTPAdapter`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticationhttpadapter) |A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`flytekit.clients.auth_helper.Authenticator`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticator) |Base authenticator for all authentication flows. |
| [`flytekit.clients.auth_helper.ClientConfig`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperclientconfig) |Client Configuration that is needed by the authenticator. |
| [`flytekit.clients.auth_helper.ClientConfigStore`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperclientconfigstore) |Client Config store retrieve client config. |
| [`flytekit.clients.auth_helper.ClientCredentialsAuthenticator`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperclientcredentialsauthenticator) |This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`flytekit.clients.auth_helper.CommandAuthenticator`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helpercommandauthenticator) |This Authenticator retrieves access_token using the provided command. |
| [`flytekit.clients.auth_helper.DefaultMetadataInterceptor`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperdefaultmetadatainterceptor) |Affords intercepting unary-unary invocations. |
| [`flytekit.clients.auth_helper.DeviceCodeAuthenticator`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperdevicecodeauthenticator) |This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`flytekit.clients.auth_helper.HTTPStatus`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperhttpstatus) |HTTP status codes and reason phrases. |
| [`flytekit.clients.auth_helper.OAuth2MetadataRequest`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperoauth2metadatarequest) |A ProtocolMessage. |
| [`flytekit.clients.auth_helper.PKCEAuthenticator`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperpkceauthenticator) |This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`flytekit.clients.auth_helper.PlatformConfig`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperplatformconfig) |This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.clients.auth_helper.PublicClientAuthConfigRequest`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperpublicclientauthconfigrequest) |A ProtocolMessage. |
| [`flytekit.clients.auth_helper.RemoteClientConfigStore`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperremoteclientconfigstore) |This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |
| [`flytekit.clients.auth_helper.RetryExceptionWrapperInterceptor`](../packages/flytekit.clients.auth_helper#flytekitclientsauth_helperretryexceptionwrapperinterceptor) |Affords intercepting unary-unary invocations. |
| [`flytekit.clients.friendly.Duration`](../packages/flytekit.clients.friendly#flytekitclientsfriendlyduration) |A ProtocolMessage. |
| [`flytekit.clients.friendly.SynchronousFlyteClient`](../packages/flytekit.clients.friendly#flytekitclientsfriendlysynchronousflyteclient) |This is a low-level client that users can use to make direct gRPC service calls to the control plane. |
| [`flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor`](../packages/flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthunaryinterceptor) |This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`flytekit.clients.grpc_utils.auth_interceptor.Authenticator`](../packages/flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthenticator) |Base authenticator for all authentication flows. |
| [`flytekit.clients.grpc_utils.default_metadata_interceptor.DefaultMetadataInterceptor`](../packages/flytekit.clients.grpc_utils.default_metadata_interceptor#flytekitclientsgrpc_utilsdefault_metadata_interceptordefaultmetadatainterceptor) |Affords intercepting unary-unary invocations. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteAuthenticationException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteauthenticationexception) |Assertion failed. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteEntityAlreadyExistsException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteentityalreadyexistsexception) |Assertion failed. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteEntityNotExistException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteentitynotexistexception) |Assertion failed. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteInvalidInputException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteinvalidinputexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteSystemException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflytesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteSystemUnavailableException`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflytesystemunavailableexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clients.grpc_utils.wrap_exception_interceptor.RetryExceptionWrapperInterceptor`](../packages/flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorretryexceptionwrapperinterceptor) |Affords intercepting unary-unary invocations. |
| [`flytekit.clients.raw.DataProxyServiceStub`](../packages/flytekit.clients.raw#flytekitclientsrawdataproxyservicestub) |DataProxyService defines an RPC Service that allows access to user-data in a controlled manner. |
| [`flytekit.clients.raw.GetDomainRequest`](../packages/flytekit.clients.raw#flytekitclientsrawgetdomainrequest) |A ProtocolMessage. |
| [`flytekit.clients.raw.PlatformConfig`](../packages/flytekit.clients.raw#flytekitclientsrawplatformconfig) |This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.clients.raw.ProjectListRequest`](../packages/flytekit.clients.raw#flytekitclientsrawprojectlistrequest) |A ProtocolMessage. |
| [`flytekit.clients.raw.RawSynchronousFlyteClient`](../packages/flytekit.clients.raw#flytekitclientsrawrawsynchronousflyteclient) |This is a thin synchronous wrapper around the auto-generated GRPC stubs for communicating with the admin service. |
| [`flytekit.clients.raw.SignalList`](../packages/flytekit.clients.raw#flytekitclientsrawsignallist) |A ProtocolMessage. |
| [`flytekit.clients.raw.SignalListRequest`](../packages/flytekit.clients.raw#flytekitclientsrawsignallistrequest) |A ProtocolMessage. |
| [`flytekit.clients.raw.SignalSetRequest`](../packages/flytekit.clients.raw#flytekitclientsrawsignalsetrequest) |A ProtocolMessage. |
| [`flytekit.clients.raw.SignalSetResponse`](../packages/flytekit.clients.raw#flytekitclientsrawsignalsetresponse) |A ProtocolMessage. |
| [`flytekit.clis.flyte_cli.main.FlyteContextManager`](../packages/flytekit.clis.flyte_cli.main#flytekitclisflyte_climainflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.clis.helpers.LaunchPlan`](../packages/flytekit.clis.helpers#flytekitclishelperslaunchplan) |A ProtocolMessage. |
| [`flytekit.clis.helpers.TaskSpec`](../packages/flytekit.clis.helpers#flytekitclishelperstaskspec) |A ProtocolMessage. |
| [`flytekit.clis.helpers.WorkflowSpec`](../packages/flytekit.clis.helpers#flytekitclishelpersworkflowspec) |A ProtocolMessage. |
| [`flytekit.clis.sdk_in_container.backfill.DateTimeType`](../packages/flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilldatetimetype) |The DateTime type converts date strings into `datetime` objects. |
| [`flytekit.clis.sdk_in_container.backfill.DurationParamType`](../packages/flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilldurationparamtype) |Represents the type of a parameter. |
| [`flytekit.clis.sdk_in_container.backfill.WorkflowFailurePolicy`](../packages/flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfillworkflowfailurepolicy) |Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.clis.sdk_in_container.backfill.datetime`](../packages/flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilldatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.clis.sdk_in_container.backfill.timedelta`](../packages/flytekit.clis.sdk_in_container.backfill#flytekitclissdk_in_containerbackfilltimedelta) |Difference between two datetime values. |
| [`flytekit.clis.sdk_in_container.executions.FlyteRemote`](../packages/flytekit.clis.sdk_in_container.executions#flytekitclissdk_in_containerexecutionsflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.clis.sdk_in_container.fetch.FlyteRemote`](../packages/flytekit.clis.sdk_in_container.fetch#flytekitclissdk_in_containerfetchflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.clis.sdk_in_container.fetch.Literal`](../packages/flytekit.clis.sdk_in_container.fetch#flytekitclissdk_in_containerfetchliteral) | |
| [`flytekit.clis.sdk_in_container.fetch.LiteralsResolver`](../packages/flytekit.clis.sdk_in_container.fetch#flytekitclissdk_in_containerfetchliteralsresolver) |LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.clis.sdk_in_container.fetch.Panel`](../packages/flytekit.clis.sdk_in_container.fetch#flytekitclissdk_in_containerfetchpanel) |A console renderable that draws a border around its contents. |
| [`flytekit.clis.sdk_in_container.fetch.Pretty`](../packages/flytekit.clis.sdk_in_container.fetch#flytekitclissdk_in_containerfetchpretty) |A rich renderable that pretty prints an object. |
| [`flytekit.clis.sdk_in_container.get.Console`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetconsole) |A high level console interface. |
| [`flytekit.clis.sdk_in_container.get.FlyteRemote`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.clis.sdk_in_container.get.Identifier`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetidentifier) | |
| [`flytekit.clis.sdk_in_container.get.LaunchPlanState`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetlaunchplanstate) | |
| [`flytekit.clis.sdk_in_container.get.NamedEntityIdentifier`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetnamedentityidentifier) | |
| [`flytekit.clis.sdk_in_container.get.ResourceType`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetresourcetype) | |
| [`flytekit.clis.sdk_in_container.get.Sort`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetsort) | |
| [`flytekit.clis.sdk_in_container.get.Table`](../packages/flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergettable) |A console renderable to draw a table. |
| [`flytekit.clis.sdk_in_container.helpers.CopyFileDetection`](../packages/flytekit.clis.sdk_in_container.helpers#flytekitclissdk_in_containerhelperscopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.clis.sdk_in_container.helpers.FlyteRemote`](../packages/flytekit.clis.sdk_in_container.helpers#flytekitclissdk_in_containerhelpersflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.clis.sdk_in_container.helpers.ImageConfig`](../packages/flytekit.clis.sdk_in_container.helpers#flytekitclissdk_in_containerhelpersimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.clis.sdk_in_container.init.BytesIO`](../packages/flytekit.clis.sdk_in_container.init#flytekitclissdk_in_containerinitbytesio) |Buffered I/O implementation using an in-memory bytes buffer. |
| [`flytekit.clis.sdk_in_container.init.ZipFile`](../packages/flytekit.clis.sdk_in_container.init#flytekitclissdk_in_containerinitzipfile) |Class with methods to open, read, write, close, list zip files. |
| [`flytekit.clis.sdk_in_container.launchplan.LaunchPlanState`](../packages/flytekit.clis.sdk_in_container.launchplan#flytekitclissdk_in_containerlaunchplanlaunchplanstate) | |
| [`flytekit.clis.sdk_in_container.launchplan.Progress`](../packages/flytekit.clis.sdk_in_container.launchplan#flytekitclissdk_in_containerlaunchplanprogress) |Renders an auto-updating progress bar(s). |
| [`flytekit.clis.sdk_in_container.local_cache.LocalTaskCache`](../packages/flytekit.clis.sdk_in_container.local_cache#flytekitclissdk_in_containerlocal_cachelocaltaskcache) |This class implements a persistent store able to cache the result of local task executions. |
| [`flytekit.clis.sdk_in_container.package.CopyFileDetection`](../packages/flytekit.clis.sdk_in_container.package#flytekitclissdk_in_containerpackagecopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.clis.sdk_in_container.package.FastPackageOptions`](../packages/flytekit.clis.sdk_in_container.package#flytekitclissdk_in_containerpackagefastpackageoptions) |FastPackageOptions is used to set configuration options when packaging files. |
| [`flytekit.clis.sdk_in_container.package.FastSerializationSettings`](../packages/flytekit.clis.sdk_in_container.package#flytekitclissdk_in_containerpackagefastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.clis.sdk_in_container.package.ImageConfig`](../packages/flytekit.clis.sdk_in_container.package#flytekitclissdk_in_containerpackageimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.clis.sdk_in_container.package.NoSerializableEntitiesError`](../packages/flytekit.clis.sdk_in_container.package#flytekitclissdk_in_containerpackagenoserializableentitieserror) |Common base class for all non-exit exceptions. |
| [`flytekit.clis.sdk_in_container.package.SerializationSettings`](../packages/flytekit.clis.sdk_in_container.package#flytekitclissdk_in_containerpackageserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.clis.sdk_in_container.serialize.Enum`](../packages/flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializeenum) |Create a collection of name/value pairs. |
| [`flytekit.clis.sdk_in_container.serialize.FastSerializationSettings`](../packages/flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializefastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.clis.sdk_in_container.serialize.ImageConfig`](../packages/flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializeimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.clis.sdk_in_container.serialize.SerializationMode`](../packages/flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializeserializationmode) |Create a collection of name/value pairs. |
| [`flytekit.clis.sdk_in_container.serialize.SerializationSettings`](../packages/flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializeserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.clis.sdk_in_container.serve.Console`](../packages/flytekit.clis.sdk_in_container.serve#flytekitclissdk_in_containerserveconsole) |A high level console interface. |
| [`flytekit.clis.sdk_in_container.serve.Table`](../packages/flytekit.clis.sdk_in_container.serve#flytekitclissdk_in_containerservetable) |A console renderable to draw a table. |
| [`flytekit.clis.sdk_in_container.utils.Console`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsconsole) |A high level console interface. |
| [`flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilserrorhandlingcommand) |Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`flytekit.clis.sdk_in_container.utils.Field`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsfield) | |
| [`flytekit.clis.sdk_in_container.utils.FlyteCompilationException`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsflytecompilationexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clis.sdk_in_container.utils.FlyteException`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsflyteexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clis.sdk_in_container.utils.FlyteInvalidInputException`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsflyteinvalidinputexception) |Common base class for all non-exit exceptions. |
| [`flytekit.clis.sdk_in_container.utils.MappingProxyType`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsmappingproxytype) |Read-only proxy of a mapping. |
| [`flytekit.clis.sdk_in_container.utils.Panel`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspanel) |A console renderable that draws a border around its contents. |
| [`flytekit.clis.sdk_in_container.utils.PyFlyteParams`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspyflyteparams) | |
| [`flytekit.clis.sdk_in_container.utils.Syntax`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilssyntax) |Construct a Syntax object to render syntax highlighted code. |
| [`flytekit.clis.sdk_in_container.utils.Traceback`](../packages/flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilstraceback) |A Console renderable that renders a traceback. |
| [`flytekit.clis.version.FlyteRemote`](../packages/flytekit.clis.version#flytekitclisversionflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.clis.version.Panel`](../packages/flytekit.clis.version#flytekitclisversionpanel) |A console renderable that draws a border around its contents. |
| [`flytekit.configuration.AuthType`](../packages/flytekit.configuration#flytekitconfigurationauthtype) |Create a collection of name/value pairs. |
| [`flytekit.configuration.AzureBlobStorageConfig`](../packages/flytekit.configuration#flytekitconfigurationazureblobstorageconfig) |Any Azure Blob Storage specific configuration. |
| [`flytekit.configuration.BytesIO`](../packages/flytekit.configuration#flytekitconfigurationbytesio) |Buffered I/O implementation using an in-memory bytes buffer. |
| [`flytekit.configuration.Config`](../packages/flytekit.configuration#flytekitconfigurationconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.configuration.ConfigEntry`](../packages/flytekit.configuration#flytekitconfigurationconfigentry) |A top level Config entry holder, that holds multiple different representations of the config. |
| [`flytekit.configuration.ConfigFile`](../packages/flytekit.configuration#flytekitconfigurationconfigfile) | |
| [`flytekit.configuration.DataClassJsonMixin`](../packages/flytekit.configuration#flytekitconfigurationdataclassjsonmixin) |DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`flytekit.configuration.DataConfig`](../packages/flytekit.configuration#flytekitconfigurationdataconfig) |Any data storage specific configuration. |
| [`flytekit.configuration.DefaultImages`](../packages/flytekit.configuration#flytekitconfigurationdefaultimages) |We may want to load the default images from remote - maybe s3 location etc?. |
| [`flytekit.configuration.EntrypointSettings`](../packages/flytekit.configuration#flytekitconfigurationentrypointsettings) |This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`flytekit.configuration.FastSerializationSettings`](../packages/flytekit.configuration#flytekitconfigurationfastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.configuration.GCSConfig`](../packages/flytekit.configuration#flytekitconfigurationgcsconfig) |Any GCS specific configuration. |
| [`flytekit.configuration.GenericPersistenceConfig`](../packages/flytekit.configuration#flytekitconfigurationgenericpersistenceconfig) |Data storage configuration that applies across any provider. |
| [`flytekit.configuration.Image`](../packages/flytekit.configuration#flytekitconfigurationimage) |Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.configuration.ImageBuildEngine`](../packages/flytekit.configuration#flytekitconfigurationimagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.configuration.ImageConfig`](../packages/flytekit.configuration#flytekitconfigurationimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.configuration.ImageSpec`](../packages/flytekit.configuration#flytekitconfigurationimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.configuration.LocalConfig`](../packages/flytekit.configuration#flytekitconfigurationlocalconfig) |Any configuration specific to local runs. |
| [`flytekit.configuration.PlatformConfig`](../packages/flytekit.configuration#flytekitconfigurationplatformconfig) |This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.configuration.S3Config`](../packages/flytekit.configuration#flytekitconfigurations3config) |S3 specific configuration. |
| [`flytekit.configuration.SecretsConfig`](../packages/flytekit.configuration#flytekitconfigurationsecretsconfig) |Configuration for secrets. |
| [`flytekit.configuration.SerializationSettings`](../packages/flytekit.configuration#flytekitconfigurationserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.configuration.StatsConfig`](../packages/flytekit.configuration#flytekitconfigurationstatsconfig) |Configuration for sending statsd. |
| [`flytekit.configuration.default_images.DefaultImages`](../packages/flytekit.configuration.default_images#flytekitconfigurationdefault_imagesdefaultimages) |We may want to load the default images from remote - maybe s3 location etc?. |
| [`flytekit.configuration.default_images.PythonVersion`](../packages/flytekit.configuration.default_images#flytekitconfigurationdefault_imagespythonversion) |Create a collection of name/value pairs. |
| [`flytekit.configuration.default_images.suppress`](../packages/flytekit.configuration.default_images#flytekitconfigurationdefault_imagessuppress) |Context manager to suppress specified exceptions. |
| [`flytekit.configuration.feature_flags.FeatureFlags`](../packages/flytekit.configuration.feature_flags#flytekitconfigurationfeature_flagsfeatureflags) | |
| [`flytekit.configuration.file.ConfigEntry`](../packages/flytekit.configuration.file#flytekitconfigurationfileconfigentry) |A top level Config entry holder, that holds multiple different representations of the config. |
| [`flytekit.configuration.file.ConfigFile`](../packages/flytekit.configuration.file#flytekitconfigurationfileconfigfile) | |
| [`flytekit.configuration.file.LegacyConfigEntry`](../packages/flytekit.configuration.file#flytekitconfigurationfilelegacyconfigentry) |Creates a record for the config entry. |
| [`flytekit.configuration.file.Path`](../packages/flytekit.configuration.file#flytekitconfigurationfilepath) |PurePath subclass that can make system calls. |
| [`flytekit.configuration.file.YamlConfigEntry`](../packages/flytekit.configuration.file#flytekitconfigurationfileyamlconfigentry) |Creates a record for the config entry. |
| [`flytekit.configuration.internal.AWS`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalaws) | |
| [`flytekit.configuration.internal.AZURE`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalazure) | |
| [`flytekit.configuration.internal.ConfigEntry`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalconfigentry) |A top level Config entry holder, that holds multiple different representations of the config. |
| [`flytekit.configuration.internal.ConfigFile`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalconfigfile) | |
| [`flytekit.configuration.internal.Credentials`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalcredentials) | |
| [`flytekit.configuration.internal.GCP`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalgcp) | |
| [`flytekit.configuration.internal.Images`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalimages) | |
| [`flytekit.configuration.internal.LegacyConfigEntry`](../packages/flytekit.configuration.internal#flytekitconfigurationinternallegacyconfigentry) |Creates a record for the config entry. |
| [`flytekit.configuration.internal.Local`](../packages/flytekit.configuration.internal#flytekitconfigurationinternallocal) | |
| [`flytekit.configuration.internal.LocalSDK`](../packages/flytekit.configuration.internal#flytekitconfigurationinternallocalsdk) | |
| [`flytekit.configuration.internal.Persistence`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalpersistence) | |
| [`flytekit.configuration.internal.Platform`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalplatform) | |
| [`flytekit.configuration.internal.Secrets`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalsecrets) | |
| [`flytekit.configuration.internal.StatsD`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalstatsd) | |
| [`flytekit.configuration.internal.YamlConfigEntry`](../packages/flytekit.configuration.internal#flytekitconfigurationinternalyamlconfigentry) |Creates a record for the config entry. |
| [`flytekit.configuration.plugin.CachePolicy`](../packages/flytekit.configuration.plugin#flytekitconfigurationplugincachepolicy) |Base class for protocol classes. |
| [`flytekit.configuration.plugin.Config`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.configuration.plugin.FlyteRemote`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.configuration.plugin.FlytekitPlugin`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginflytekitplugin) | |
| [`flytekit.configuration.plugin.FlytekitPluginProtocol`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginflytekitpluginprotocol) |Base class for protocol classes. |
| [`flytekit.configuration.plugin.Group`](../packages/flytekit.configuration.plugin#flytekitconfigurationplugingroup) |A group allows a command to have subcommands attached. |
| [`flytekit.configuration.plugin.Protocol`](../packages/flytekit.configuration.plugin#flytekitconfigurationpluginprotocol) |Base class for protocol classes. |
| [`flytekit.constants.CopyFileDetection`](../packages/flytekit.constants#flytekitconstantscopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.constants.Enum`](../packages/flytekit.constants#flytekitconstantsenum) |Create a collection of name/value pairs. |
| [`flytekit.core.annotation.Any`](../packages/flytekit.core.annotation#flytekitcoreannotationany) |Special type indicating an unconstrained type. |
| [`flytekit.core.annotation.FlyteAnnotation`](../packages/flytekit.core.annotation#flytekitcoreannotationflyteannotation) |A core object to add arbitrary annotations to flyte types. |
| [`flytekit.core.array_node.Any`](../packages/flytekit.core.array_node#flytekitcorearray_nodeany) |Special type indicating an unconstrained type. |
| [`flytekit.core.array_node.ArrayNode`](../packages/flytekit.core.array_node#flytekitcorearray_nodearraynode) | |
| [`flytekit.core.array_node.ExecutionState`](../packages/flytekit.core.array_node#flytekitcorearray_nodeexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.array_node.FlyteContext`](../packages/flytekit.core.array_node#flytekitcorearray_nodeflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.array_node.LaunchPlan`](../packages/flytekit.core.array_node#flytekitcorearray_nodelaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.array_node.Literal`](../packages/flytekit.core.array_node#flytekitcorearray_nodeliteral) | |
| [`flytekit.core.array_node.LiteralCollection`](../packages/flytekit.core.array_node#flytekitcorearray_nodeliteralcollection) | |
| [`flytekit.core.array_node.Node`](../packages/flytekit.core.array_node#flytekitcorearray_nodenode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.array_node.Promise`](../packages/flytekit.core.array_node#flytekitcorearray_nodepromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.array_node.ReferenceLaunchPlan`](../packages/flytekit.core.array_node#flytekitcorearray_nodereferencelaunchplan) |A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.core.array_node.ReferenceTask`](../packages/flytekit.core.array_node#flytekitcorearray_nodereferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.array_node.Scalar`](../packages/flytekit.core.array_node#flytekitcorearray_nodescalar) | |
| [`flytekit.core.array_node.VoidPromise`](../packages/flytekit.core.array_node#flytekitcorearray_nodevoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.array_node_map_task.Any`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTask`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskarraynodemaptask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.array_node_map_task.ArrayNodeMapTaskResolver`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskarraynodemaptaskresolver) |Special resolver that is used for ArrayNodeMapTasks. |
| [`flytekit.core.array_node_map_task.Container`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskcontainer) | |
| [`flytekit.core.array_node_map_task.ExecutionState`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.array_node_map_task.FlyteContext`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.array_node_map_task.FlyteContextManager`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.array_node_map_task.K8sPod`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskk8spod) | |
| [`flytekit.core.array_node_map_task.LaunchPlan`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasklaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.array_node_map_task.NodeMetadata`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasknodemetadata) | |
| [`flytekit.core.array_node_map_task.PythonFunctionTask`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.array_node_map_task.PythonInstanceTask`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskpythoninstancetask) |This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.core.array_node_map_task.PythonTask`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.array_node_map_task.ReferenceTask`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskreferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.array_node_map_task.SerializationSettings`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.array_node_map_task.Sql`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasksql) | |
| [`flytekit.core.array_node_map_task.Task`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasktask) | |
| [`flytekit.core.array_node_map_task.TaskResolverMixin`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.array_node_map_task.TypeEngine`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasktypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.array_node_map_task.Variable`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_taskvariable) | |
| [`flytekit.core.array_node_map_task.timeit`](../packages/flytekit.core.array_node_map_task#flytekitcorearray_node_map_tasktimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.artifact.Artifact`](../packages/flytekit.core.artifact#flytekitcoreartifactartifact) |An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.core.artifact.ArtifactIDSpecification`](../packages/flytekit.core.artifact#flytekitcoreartifactartifactidspecification) |This is a special object that helps specify how Artifacts are to be created. |
| [`flytekit.core.artifact.ArtifactQuery`](../packages/flytekit.core.artifact#flytekitcoreartifactartifactquery) | |
| [`flytekit.core.artifact.ArtifactSerializationHandler`](../packages/flytekit.core.artifact#flytekitcoreartifactartifactserializationhandler) |This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`flytekit.core.artifact.DefaultArtifactSerializationHandler`](../packages/flytekit.core.artifact#flytekitcoreartifactdefaultartifactserializationhandler) |This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`flytekit.core.artifact.FlyteContextManager`](../packages/flytekit.core.artifact#flytekitcoreartifactflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.artifact.InputsBase`](../packages/flytekit.core.artifact#flytekitcoreartifactinputsbase) |A class to provide better partition semantics. |
| [`flytekit.core.artifact.OutputMetadata`](../packages/flytekit.core.artifact#flytekitcoreartifactoutputmetadata) | |
| [`flytekit.core.artifact.Partition`](../packages/flytekit.core.artifact#flytekitcoreartifactpartition) | |
| [`flytekit.core.artifact.Partitions`](../packages/flytekit.core.artifact#flytekitcoreartifactpartitions) | |
| [`flytekit.core.artifact.SerializableToString`](../packages/flytekit.core.artifact#flytekitcoreartifactserializabletostring) |This protocol is used by the Artifact create_from function. |
| [`flytekit.core.artifact.Serializer`](../packages/flytekit.core.artifact#flytekitcoreartifactserializer) | |
| [`flytekit.core.artifact.TimePartition`](../packages/flytekit.core.artifact#flytekitcoreartifacttimepartition) | |
| [`flytekit.core.artifact.Timestamp`](../packages/flytekit.core.artifact#flytekitcoreartifacttimestamp) |A ProtocolMessage. |
| [`flytekit.core.artifact.timedelta`](../packages/flytekit.core.artifact#flytekitcoreartifacttimedelta) |Difference between two datetime values. |
| [`flytekit.core.artifact_utils.LabelValue`](../packages/flytekit.core.artifact_utils#flytekitcoreartifact_utilslabelvalue) |A ProtocolMessage. |
| [`flytekit.core.artifact_utils.Partitions`](../packages/flytekit.core.artifact_utils#flytekitcoreartifact_utilspartitions) |A ProtocolMessage. |
| [`flytekit.core.artifact_utils.TimePartition`](../packages/flytekit.core.artifact_utils#flytekitcoreartifact_utilstimepartition) |A ProtocolMessage. |
| [`flytekit.core.artifact_utils.Timestamp`](../packages/flytekit.core.artifact_utils#flytekitcoreartifact_utilstimestamp) |A ProtocolMessage. |
| [`flytekit.core.artifact_utils.datetime`](../packages/flytekit.core.artifact_utils#flytekitcoreartifact_utilsdatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.core.base_sql_task.Any`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.base_sql_task.Interface`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_taskinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.base_sql_task.PythonTask`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.base_sql_task.SQLTask`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_tasksqltask) |Base task types for all SQL tasks. |
| [`flytekit.core.base_sql_task.TaskMetadata`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_tasktaskmetadata) |Metadata for a Task. |
| [`flytekit.core.base_sql_task.TypeVar`](../packages/flytekit.core.base_sql_task#flytekitcorebase_sql_tasktypevar) |Type variable. |
| [`flytekit.core.base_task.Any`](../packages/flytekit.core.base_task#flytekitcorebase_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.base_task.DeckField`](../packages/flytekit.core.base_task#flytekitcorebase_taskdeckfield) |DeckField is used to specify the fields that will be rendered in the deck. |
| [`flytekit.core.base_task.Description`](../packages/flytekit.core.base_task#flytekitcorebase_taskdescription) |Full user description with formatting preserved. |
| [`flytekit.core.base_task.Documentation`](../packages/flytekit.core.base_task#flytekitcorebase_taskdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.core.base_task.ExecutionParameters`](../packages/flytekit.core.base_task#flytekitcorebase_taskexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.base_task.ExecutionState`](../packages/flytekit.core.base_task#flytekitcorebase_taskexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.base_task.FlyteContext`](../packages/flytekit.core.base_task#flytekitcorebase_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.base_task.FlyteContextManager`](../packages/flytekit.core.base_task#flytekitcorebase_taskflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.base_task.FlyteDownloadDataException`](../packages/flytekit.core.base_task#flytekitcorebase_taskflytedownloaddataexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.base_task.FlyteEntities`](../packages/flytekit.core.base_task#flytekitcorebase_taskflyteentities) |This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.base_task.FlyteNonRecoverableSystemException`](../packages/flytekit.core.base_task#flytekitcorebase_taskflytenonrecoverablesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.base_task.FlyteUploadDataException`](../packages/flytekit.core.base_task#flytekitcorebase_taskflyteuploaddataexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.base_task.FlyteUserRuntimeException`](../packages/flytekit.core.base_task#flytekitcorebase_taskflyteuserruntimeexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.base_task.Generic`](../packages/flytekit.core.base_task#flytekitcorebase_taskgeneric) |Abstract base class for generic types. |
| [`flytekit.core.base_task.IgnoreOutputs`](../packages/flytekit.core.base_task#flytekitcorebase_taskignoreoutputs) |This exception should be used to indicate that the outputs generated by this can be safely ignored. |
| [`flytekit.core.base_task.Interface`](../packages/flytekit.core.base_task#flytekitcorebase_taskinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.base_task.LocalConfig`](../packages/flytekit.core.base_task#flytekitcorebase_tasklocalconfig) |Any configuration specific to local runs. |
| [`flytekit.core.base_task.LocalTaskCache`](../packages/flytekit.core.base_task#flytekitcorebase_tasklocaltaskcache) |This class implements a persistent store able to cache the result of local task executions. |
| [`flytekit.core.base_task.Promise`](../packages/flytekit.core.base_task#flytekitcorebase_taskpromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.base_task.PythonTask`](../packages/flytekit.core.base_task#flytekitcorebase_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.base_task.SecurityContext`](../packages/flytekit.core.base_task#flytekitcorebase_tasksecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.core.base_task.SerializationSettings`](../packages/flytekit.core.base_task#flytekitcorebase_taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.base_task.Task`](../packages/flytekit.core.base_task#flytekitcorebase_tasktask) |The base of all Tasks in flytekit. |
| [`flytekit.core.base_task.TaskMetadata`](../packages/flytekit.core.base_task#flytekitcorebase_tasktaskmetadata) |Metadata for a Task. |
| [`flytekit.core.base_task.TaskResolverMixin`](../packages/flytekit.core.base_task#flytekitcorebase_tasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.base_task.TrackedInstance`](../packages/flytekit.core.base_task#flytekitcorebase_tasktrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.base_task.TypeEngine`](../packages/flytekit.core.base_task#flytekitcorebase_tasktypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.base_task.TypeTransformerFailedError`](../packages/flytekit.core.base_task#flytekitcorebase_tasktypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.core.base_task.TypeVar`](../packages/flytekit.core.base_task#flytekitcorebase_tasktypevar) |Type variable. |
| [`flytekit.core.base_task.Variable`](../packages/flytekit.core.base_task#flytekitcorebase_taskvariable) | |
| [`flytekit.core.base_task.VoidPromise`](../packages/flytekit.core.base_task#flytekitcorebase_taskvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.base_task.timeit`](../packages/flytekit.core.base_task#flytekitcorebase_tasktimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.cache.Cache`](../packages/flytekit.core.cache#flytekitcorecachecache) |Cache configuration for a task. |
| [`flytekit.core.cache.CachePolicy`](../packages/flytekit.core.cache#flytekitcorecachecachepolicy) |Base class for protocol classes. |
| [`flytekit.core.cache.Generic`](../packages/flytekit.core.cache#flytekitcorecachegeneric) |Abstract base class for generic types. |
| [`flytekit.core.cache.ImageSpec`](../packages/flytekit.core.cache#flytekitcorecacheimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.core.cache.ParamSpec`](../packages/flytekit.core.cache#flytekitcorecacheparamspec) |Parameter specification variable. |
| [`flytekit.core.cache.PodTemplate`](../packages/flytekit.core.cache#flytekitcorecachepodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.cache.Protocol`](../packages/flytekit.core.cache#flytekitcorecacheprotocol) |Base class for protocol classes. |
| [`flytekit.core.cache.TypeVar`](../packages/flytekit.core.cache#flytekitcorecachetypevar) |Type variable. |
| [`flytekit.core.cache.VersionParameters`](../packages/flytekit.core.cache#flytekitcorecacheversionparameters) |Parameters used for version hash generation. |
| [`flytekit.core.checkpointer.Checkpoint`](../packages/flytekit.core.checkpointer#flytekitcorecheckpointercheckpoint) |Base class for Checkpoint system. |
| [`flytekit.core.checkpointer.Path`](../packages/flytekit.core.checkpointer#flytekitcorecheckpointerpath) |PurePath subclass that can make system calls. |
| [`flytekit.core.checkpointer.SyncCheckpoint`](../packages/flytekit.core.checkpointer#flytekitcorecheckpointersynccheckpoint) |This class is NOT THREAD-SAFE!. |
| [`flytekit.core.class_based_resolver.ClassStorageTaskResolver`](../packages/flytekit.core.class_based_resolver#flytekitcoreclass_based_resolverclassstoragetaskresolver) |Stores tasks inside a class variable. |
| [`flytekit.core.class_based_resolver.PythonAutoContainerTask`](../packages/flytekit.core.class_based_resolver#flytekitcoreclass_based_resolverpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.class_based_resolver.SerializationSettings`](../packages/flytekit.core.class_based_resolver#flytekitcoreclass_based_resolverserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.class_based_resolver.TaskResolverMixin`](../packages/flytekit.core.class_based_resolver#flytekitcoreclass_based_resolvertaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.class_based_resolver.TrackedInstance`](../packages/flytekit.core.class_based_resolver#flytekitcoreclass_based_resolvertrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.condition.Binding`](../packages/flytekit.core.condition#flytekitcoreconditionbinding) | |
| [`flytekit.core.condition.BindingData`](../packages/flytekit.core.condition#flytekitcoreconditionbindingdata) | |
| [`flytekit.core.condition.BranchNode`](../packages/flytekit.core.condition#flytekitcoreconditionbranchnode) | |
| [`flytekit.core.condition.Case`](../packages/flytekit.core.condition#flytekitcoreconditioncase) | |
| [`flytekit.core.condition.ComparisonExpression`](../packages/flytekit.core.condition#flytekitcoreconditioncomparisonexpression) |ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`flytekit.core.condition.ComparisonOps`](../packages/flytekit.core.condition#flytekitcoreconditioncomparisonops) |Create a collection of name/value pairs. |
| [`flytekit.core.condition.Condition`](../packages/flytekit.core.condition#flytekitcoreconditioncondition) | |
| [`flytekit.core.condition.ConditionalSection`](../packages/flytekit.core.condition#flytekitcoreconditionconditionalsection) |ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.condition.ConjunctionExpression`](../packages/flytekit.core.condition#flytekitcoreconditionconjunctionexpression) |A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`flytekit.core.condition.ConjunctionOps`](../packages/flytekit.core.condition#flytekitcoreconditionconjunctionops) |Create a collection of name/value pairs. |
| [`flytekit.core.condition.Error`](../packages/flytekit.core.condition#flytekitcoreconditionerror) | |
| [`flytekit.core.condition.FlyteContextManager`](../packages/flytekit.core.condition#flytekitcoreconditionflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.condition.Literal`](../packages/flytekit.core.condition#flytekitcoreconditionliteral) | |
| [`flytekit.core.condition.LocalExecutedConditionalSection`](../packages/flytekit.core.condition#flytekitcoreconditionlocalexecutedconditionalsection) |ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.condition.Node`](../packages/flytekit.core.condition#flytekitcoreconditionnode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.condition.NodeOutput`](../packages/flytekit.core.condition#flytekitcoreconditionnodeoutput) | |
| [`flytekit.core.condition.Promise`](../packages/flytekit.core.condition#flytekitcoreconditionpromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.condition.RetryStrategy`](../packages/flytekit.core.condition#flytekitcoreconditionretrystrategy) | |
| [`flytekit.core.condition.SkippedConditionalSection`](../packages/flytekit.core.condition#flytekitcoreconditionskippedconditionalsection) |This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |
| [`flytekit.core.condition.VoidPromise`](../packages/flytekit.core.condition#flytekitcoreconditionvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.container_task.Any`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.container_task.ContainerTask`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskcontainertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flytekit.core.container_task.Enum`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskenum) |Create a collection of name/value pairs. |
| [`flytekit.core.container_task.FlyteContext`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.container_task.ImageSpec`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.core.container_task.Interface`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.container_task.LiteralMap`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskliteralmap) | |
| [`flytekit.core.container_task.PodTemplate`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskpodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.container_task.PythonTask`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.container_task.ResourceSpec`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskresourcespec) | |
| [`flytekit.core.container_task.Resources`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.container_task.Secret`](../packages/flytekit.core.container_task#flytekitcorecontainer_tasksecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.core.container_task.SecurityContext`](../packages/flytekit.core.container_task#flytekitcorecontainer_tasksecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.core.container_task.SerializationSettings`](../packages/flytekit.core.container_task#flytekitcorecontainer_taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.container_task.TaskMetadata`](../packages/flytekit.core.container_task#flytekitcorecontainer_tasktaskmetadata) |Metadata for a Task. |
| [`flytekit.core.context_manager.BranchEvalMode`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerbranchevalmode) |This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.core.context_manager.Checkpoint`](../packages/flytekit.core.context_manager#flytekitcorecontext_managercheckpoint) |Base class for Checkpoint system. |
| [`flytekit.core.context_manager.CompilationState`](../packages/flytekit.core.context_manager#flytekitcorecontext_managercompilationstate) |Compilation state is used during the compilation of a workflow or task. |
| [`flytekit.core.context_manager.Config`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.core.context_manager.ContextVar`](../packages/flytekit.core.context_manager#flytekitcorecontext_managercontextvar) | |
| [`flytekit.core.context_manager.Enum`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerenum) |Create a collection of name/value pairs. |
| [`flytekit.core.context_manager.ExecutionParameters`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.context_manager.ExecutionState`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.context_manager.FileAccessProvider`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerfileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.core.context_manager.FlyteContext`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.context_manager.FlyteContextManager`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.context_manager.FlyteEntities`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerflyteentities) |This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.context_manager.FrameType`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerframetype) | |
| [`flytekit.core.context_manager.Node`](../packages/flytekit.core.context_manager#flytekitcorecontext_managernode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.context_manager.OutputMetadata`](../packages/flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadata) | |
| [`flytekit.core.context_manager.OutputMetadataTracker`](../packages/flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadatatracker) |This class is for the users to set arbitrary metadata on output literals. |
| [`flytekit.core.context_manager.SecretsConfig`](../packages/flytekit.core.context_manager#flytekitcorecontext_managersecretsconfig) |Configuration for secrets. |
| [`flytekit.core.context_manager.SecretsManager`](../packages/flytekit.core.context_manager#flytekitcorecontext_managersecretsmanager) |This provides a secrets resolution logic at runtime. |
| [`flytekit.core.context_manager.SerializableToString`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerserializabletostring) |This protocol is used by the Artifact create_from function. |
| [`flytekit.core.context_manager.SerializationSettings`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.context_manager.SyncCheckpoint`](../packages/flytekit.core.context_manager#flytekitcorecontext_managersynccheckpoint) |This class is NOT THREAD-SAFE!. |
| [`flytekit.core.context_manager.WorkflowExecutionIdentifier`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerworkflowexecutionidentifier) | |
| [`flytekit.core.context_manager.datetime`](../packages/flytekit.core.context_manager#flytekitcorecontext_managerdatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.core.context_manager.timezone`](../packages/flytekit.core.context_manager#flytekitcorecontext_managertimezone) |Fixed offset from UTC implementation of tzinfo. |
| [`flytekit.core.data_persistence.Any`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceany) |Special type indicating an unconstrained type. |
| [`flytekit.core.data_persistence.AsyncFileSystem`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceasyncfilesystem) |Async file operations, default implementations. |
| [`flytekit.core.data_persistence.DataConfig`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistencedataconfig) |Any data storage specific configuration. |
| [`flytekit.core.data_persistence.FileAccessProvider`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistencefileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.core.data_persistence.FlyteAssertion`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceflyteassertion) |Assertion failed. |
| [`flytekit.core.data_persistence.FlyteDataNotFoundException`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceflytedatanotfoundexception) |Inappropriate argument value (of correct type). |
| [`flytekit.core.data_persistence.FlyteDownloadDataException`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceflytedownloaddataexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.data_persistence.FlyteLocalFileSystem`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceflytelocalfilesystem) |This class doesn't do anything except override the separator so that it works on windows. |
| [`flytekit.core.data_persistence.FlyteUploadDataException`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceflyteuploaddataexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.data_persistence.UUID`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistenceuuid) |Instances of the UUID class represent UUIDs as specified in RFC 4122. |
| [`flytekit.core.data_persistence.timeit`](../packages/flytekit.core.data_persistence#flytekitcoredata_persistencetimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.docstring.Docstring`](../packages/flytekit.core.docstring#flytekitcoredocstringdocstring) | |
| [`flytekit.core.dynamic_workflow_task.PythonFunctionTask`](../packages/flytekit.core.dynamic_workflow_task#flytekitcoredynamic_workflow_taskpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.environment.Any`](../packages/flytekit.core.environment#flytekitcoreenvironmentany) |Special type indicating an unconstrained type. |
| [`flytekit.core.environment.Console`](../packages/flytekit.core.environment#flytekitcoreenvironmentconsole) |A high level console interface. |
| [`flytekit.core.environment.Environment`](../packages/flytekit.core.environment#flytekitcoreenvironmentenvironment) | |
| [`flytekit.core.environment.Panel`](../packages/flytekit.core.environment#flytekitcoreenvironmentpanel) |A console renderable that draws a border around its contents. |
| [`flytekit.core.environment.ParamSpec`](../packages/flytekit.core.environment#flytekitcoreenvironmentparamspec) |Parameter specification variable. |
| [`flytekit.core.environment.Pretty`](../packages/flytekit.core.environment#flytekitcoreenvironmentpretty) |A rich renderable that pretty prints an object. |
| [`flytekit.core.environment.TypeVar`](../packages/flytekit.core.environment#flytekitcoreenvironmenttypevar) |Type variable. |
| [`flytekit.core.environment.partial`](../packages/flytekit.core.environment#flytekitcoreenvironmentpartial) |Create a new function with partial application of the given arguments. |
| [`flytekit.core.gate.ExecutionState`](../packages/flytekit.core.gate#flytekitcoregateexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.gate.FlyteContext`](../packages/flytekit.core.gate#flytekitcoregateflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.gate.FlyteContextManager`](../packages/flytekit.core.gate#flytekitcoregateflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.gate.FlyteDisapprovalException`](../packages/flytekit.core.gate#flytekitcoregateflytedisapprovalexception) |Assertion failed. |
| [`flytekit.core.gate.Gate`](../packages/flytekit.core.gate#flytekitcoregategate) |A node type that waits for user input before proceeding with a workflow. |
| [`flytekit.core.gate.LiteralType`](../packages/flytekit.core.gate#flytekitcoregateliteraltype) | |
| [`flytekit.core.gate.Promise`](../packages/flytekit.core.gate#flytekitcoregatepromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.gate.Scalar`](../packages/flytekit.core.gate#flytekitcoregatescalar) | |
| [`flytekit.core.gate.TypeEngine`](../packages/flytekit.core.gate#flytekitcoregatetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.gate.VoidPromise`](../packages/flytekit.core.gate#flytekitcoregatevoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.hash.Generic`](../packages/flytekit.core.hash#flytekitcorehashgeneric) |Abstract base class for generic types. |
| [`flytekit.core.hash.HashMethod`](../packages/flytekit.core.hash#flytekitcorehashhashmethod) |Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.core.hash.HashOnReferenceMixin`](../packages/flytekit.core.hash#flytekitcorehashhashonreferencemixin) | |
| [`flytekit.core.hash.TypeVar`](../packages/flytekit.core.hash#flytekitcorehashtypevar) |Type variable. |
| [`flytekit.core.interface.Any`](../packages/flytekit.core.interface#flytekitcoreinterfaceany) |Special type indicating an unconstrained type. |
| [`flytekit.core.interface.Artifact`](../packages/flytekit.core.interface#flytekitcoreinterfaceartifact) |An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.core.interface.ArtifactIDSpecification`](../packages/flytekit.core.interface#flytekitcoreinterfaceartifactidspecification) |This is a special object that helps specify how Artifacts are to be created. |
| [`flytekit.core.interface.ArtifactQuery`](../packages/flytekit.core.interface#flytekitcoreinterfaceartifactquery) | |
| [`flytekit.core.interface.Docstring`](../packages/flytekit.core.interface#flytekitcoreinterfacedocstring) | |
| [`flytekit.core.interface.FlyteContextManager`](../packages/flytekit.core.interface#flytekitcoreinterfaceflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.interface.FlyteMissingReturnValueException`](../packages/flytekit.core.interface#flytekitcoreinterfaceflytemissingreturnvalueexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.interface.FlyteMissingTypeException`](../packages/flytekit.core.interface#flytekitcoreinterfaceflytemissingtypeexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.interface.FlyteValidationException`](../packages/flytekit.core.interface#flytekitcoreinterfaceflytevalidationexception) |Assertion failed. |
| [`flytekit.core.interface.Interface`](../packages/flytekit.core.interface#flytekitcoreinterfaceinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.interface.Literal`](../packages/flytekit.core.interface#flytekitcoreinterfaceliteral) | |
| [`flytekit.core.interface.OrderedDict`](../packages/flytekit.core.interface#flytekitcoreinterfaceordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.core.interface.Scalar`](../packages/flytekit.core.interface#flytekitcoreinterfacescalar) | |
| [`flytekit.core.interface.TypeEngine`](../packages/flytekit.core.interface#flytekitcoreinterfacetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.interface.TypeVar`](../packages/flytekit.core.interface#flytekitcoreinterfacetypevar) |Type variable. |
| [`flytekit.core.interface.UnionTransformer`](../packages/flytekit.core.interface#flytekitcoreinterfaceuniontransformer) |Transformer that handles a typing. |
| [`flytekit.core.interface.Void`](../packages/flytekit.core.interface#flytekitcoreinterfacevoid) | |
| [`flytekit.core.launch_plan.Any`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planany) |Special type indicating an unconstrained type. |
| [`flytekit.core.launch_plan.FlyteContext`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.launch_plan.FlyteContextManager`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.launch_plan.FlyteEntities`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planflyteentities) |This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.launch_plan.Interface`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.launch_plan.LaunchPlan`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planlaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.launch_plan.LaunchPlanReference`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planlaunchplanreference) |A reference object containing metadata that points to a remote launch plan. |
| [`flytekit.core.launch_plan.LaunchPlanTriggerBase`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planlaunchplantriggerbase) |Base class for protocol classes. |
| [`flytekit.core.launch_plan.ReferenceEntity`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planreferenceentity) | |
| [`flytekit.core.launch_plan.ReferenceLaunchPlan`](../packages/flytekit.core.launch_plan#flytekitcorelaunch_planreferencelaunchplan) |A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.core.legacy_map_task.Any`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.legacy_map_task.ArrayJob`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskarrayjob) | |
| [`flytekit.core.legacy_map_task.Container`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskcontainer) | |
| [`flytekit.core.legacy_map_task.ExecutionState`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.legacy_map_task.FlyteContext`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.legacy_map_task.FlyteContextManager`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.legacy_map_task.K8sPod`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskk8spod) | |
| [`flytekit.core.legacy_map_task.MapPythonTask`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmappythontask) |A MapPythonTask defines a :py:class:`flytekit. |
| [`flytekit.core.legacy_map_task.MapTaskResolver`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmaptaskresolver) |Special resolver that is used for MapTasks. |
| [`flytekit.core.legacy_map_task.PythonFunctionTask`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.legacy_map_task.PythonInstanceTask`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskpythoninstancetask) |This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.core.legacy_map_task.PythonTask`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.legacy_map_task.SerializationSettings`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.legacy_map_task.Sql`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_tasksql) | |
| [`flytekit.core.legacy_map_task.Task`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_tasktask) |The base of all Tasks in flytekit. |
| [`flytekit.core.legacy_map_task.TaskResolverMixin`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_tasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.legacy_map_task.TrackedInstance`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_tasktrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.legacy_map_task.Variable`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskvariable) | |
| [`flytekit.core.legacy_map_task.timeit`](../packages/flytekit.core.legacy_map_task#flytekitcorelegacy_map_tasktimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.local_cache.Cache`](../packages/flytekit.core.local_cache#flytekitcorelocal_cachecache) |Disk and file backed cache. |
| [`flytekit.core.local_cache.Literal`](../packages/flytekit.core.local_cache#flytekitcorelocal_cacheliteral) | |
| [`flytekit.core.local_cache.LiteralCollection`](../packages/flytekit.core.local_cache#flytekitcorelocal_cacheliteralcollection) | |
| [`flytekit.core.local_cache.LiteralMap`](../packages/flytekit.core.local_cache#flytekitcorelocal_cacheliteralmap) |A ProtocolMessage. |
| [`flytekit.core.local_cache.LocalTaskCache`](../packages/flytekit.core.local_cache#flytekitcorelocal_cachelocaltaskcache) |This class implements a persistent store able to cache the result of local task executions. |
| [`flytekit.core.local_cache.ModelLiteralMap`](../packages/flytekit.core.local_cache#flytekitcorelocal_cachemodelliteralmap) | |
| [`flytekit.core.local_fsspec.FlyteLocalFileSystem`](../packages/flytekit.core.local_fsspec#flytekitcorelocal_fsspecflytelocalfilesystem) |This class doesn't do anything except override the separator so that it works on windows. |
| [`flytekit.core.local_fsspec.LocalFileSystem`](../packages/flytekit.core.local_fsspec#flytekitcorelocal_fsspeclocalfilesystem) |Interface to files on local storage. |
| [`flytekit.core.mock_stats.MockStats`](../packages/flytekit.core.mock_stats#flytekitcoremock_statsmockstats) | |
| [`flytekit.core.node.Any`](../packages/flytekit.core.node#flytekitcorenodeany) |Special type indicating an unconstrained type. |
| [`flytekit.core.node.BaseAccelerator`](../packages/flytekit.core.node#flytekitcorenodebaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.core.node.Node`](../packages/flytekit.core.node#flytekitcorenodenode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.node.PodTemplate`](../packages/flytekit.core.node#flytekitcorenodepodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.node.ResourceSpec`](../packages/flytekit.core.node#flytekitcorenoderesourcespec) | |
| [`flytekit.core.node.Resources`](../packages/flytekit.core.node#flytekitcorenoderesources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.node_creation.BranchEvalMode`](../packages/flytekit.core.node_creation#flytekitcorenode_creationbranchevalmode) |This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.core.node_creation.ExecutionState`](../packages/flytekit.core.node_creation#flytekitcorenode_creationexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.node_creation.FlyteContext`](../packages/flytekit.core.node_creation#flytekitcorenode_creationflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.node_creation.LaunchPlan`](../packages/flytekit.core.node_creation#flytekitcorenode_creationlaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.node_creation.Node`](../packages/flytekit.core.node_creation#flytekitcorenode_creationnode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.node_creation.PythonTask`](../packages/flytekit.core.node_creation#flytekitcorenode_creationpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.node_creation.VoidPromise`](../packages/flytekit.core.node_creation#flytekitcorenode_creationvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.node_creation.WorkflowBase`](../packages/flytekit.core.node_creation#flytekitcorenode_creationworkflowbase) | |
| [`flytekit.core.notification.Email`](../packages/flytekit.core.notification#flytekitcorenotificationemail) |This notification should be used when sending regular emails to people. |
| [`flytekit.core.notification.Notification`](../packages/flytekit.core.notification#flytekitcorenotificationnotification) | |
| [`flytekit.core.notification.PagerDuty`](../packages/flytekit.core.notification#flytekitcorenotificationpagerduty) |This notification should be used when sending emails to the PagerDuty service. |
| [`flytekit.core.notification.Slack`](../packages/flytekit.core.notification#flytekitcorenotificationslack) |This notification should be used when sending emails to the Slack. |
| [`flytekit.core.options.Options`](../packages/flytekit.core.options#flytekitcoreoptionsoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.core.pod_template.PodTemplate`](../packages/flytekit.core.pod_template#flytekitcorepod_templatepodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.promise.Any`](../packages/flytekit.core.promise#flytekitcorepromiseany) |Special type indicating an unconstrained type. |
| [`flytekit.core.promise.AsyncTypeTransformer`](../packages/flytekit.core.promise#flytekitcorepromiseasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.promise.BaseAccelerator`](../packages/flytekit.core.promise#flytekitcorepromisebaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.core.promise.Binary`](../packages/flytekit.core.promise#flytekitcorepromisebinary) | |
| [`flytekit.core.promise.BranchEvalMode`](../packages/flytekit.core.promise#flytekitcorepromisebranchevalmode) |This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.core.promise.ComparisonExpression`](../packages/flytekit.core.promise#flytekitcorepromisecomparisonexpression) |ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`flytekit.core.promise.ComparisonOps`](../packages/flytekit.core.promise#flytekitcorepromisecomparisonops) |Create a collection of name/value pairs. |
| [`flytekit.core.promise.ConjunctionExpression`](../packages/flytekit.core.promise#flytekitcorepromiseconjunctionexpression) |A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`flytekit.core.promise.ConjunctionOps`](../packages/flytekit.core.promise#flytekitcorepromiseconjunctionops) |Create a collection of name/value pairs. |
| [`flytekit.core.promise.DictTransformer`](../packages/flytekit.core.promise#flytekitcorepromisedicttransformer) |Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`flytekit.core.promise.Enum`](../packages/flytekit.core.promise#flytekitcorepromiseenum) |Create a collection of name/value pairs. |
| [`flytekit.core.promise.ExecutionParameters`](../packages/flytekit.core.promise#flytekitcorepromiseexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.promise.ExecutionState`](../packages/flytekit.core.promise#flytekitcorepromiseexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.promise.FlyteContext`](../packages/flytekit.core.promise#flytekitcorepromiseflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.promise.FlyteContextManager`](../packages/flytekit.core.promise#flytekitcorepromiseflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.promise.FlytePromiseAttributeResolveException`](../packages/flytekit.core.promise#flytekitcorepromiseflytepromiseattributeresolveexception) |Assertion failed. |
| [`flytekit.core.promise.HasFlyteInterface`](../packages/flytekit.core.promise#flytekitcorepromisehasflyteinterface) |Base class for protocol classes. |
| [`flytekit.core.promise.Interface`](../packages/flytekit.core.promise#flytekitcorepromiseinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.promise.Iterable`](../packages/flytekit.core.promise#flytekitcorepromiseiterable) | |
| [`flytekit.core.promise.ListTransformer`](../packages/flytekit.core.promise#flytekitcorepromiselisttransformer) |Transformer that handles a univariate typing. |
| [`flytekit.core.promise.Literal`](../packages/flytekit.core.promise#flytekitcorepromiseliteral) | |
| [`flytekit.core.promise.LocallyExecutable`](../packages/flytekit.core.promise#flytekitcorepromiselocallyexecutable) |Base class for protocol classes. |
| [`flytekit.core.promise.Node`](../packages/flytekit.core.promise#flytekitcorepromisenode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.promise.NodeOutput`](../packages/flytekit.core.promise#flytekitcorepromisenodeoutput) | |
| [`flytekit.core.promise.OutputMetadataTracker`](../packages/flytekit.core.promise#flytekitcorepromiseoutputmetadatatracker) |This class is for the users to set arbitrary metadata on output literals. |
| [`flytekit.core.promise.Primitive`](../packages/flytekit.core.promise#flytekitcorepromiseprimitive) | |
| [`flytekit.core.promise.Promise`](../packages/flytekit.core.promise#flytekitcorepromisepromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.promise.Protocol`](../packages/flytekit.core.promise#flytekitcorepromiseprotocol) |Base class for protocol classes. |
| [`flytekit.core.promise.Resources`](../packages/flytekit.core.promise#flytekitcorepromiseresources) | |
| [`flytekit.core.promise.Scalar`](../packages/flytekit.core.promise#flytekitcorepromisescalar) | |
| [`flytekit.core.promise.SimpleType`](../packages/flytekit.core.promise#flytekitcorepromisesimpletype) | |
| [`flytekit.core.promise.SupportsNodeCreation`](../packages/flytekit.core.promise#flytekitcorepromisesupportsnodecreation) |Base class for protocol classes. |
| [`flytekit.core.promise.TypeEngine`](../packages/flytekit.core.promise#flytekitcorepromisetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.promise.TypeTransformer`](../packages/flytekit.core.promise#flytekitcorepromisetypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.promise.TypeTransformerFailedError`](../packages/flytekit.core.promise#flytekitcorepromisetypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.core.promise.UnionTransformer`](../packages/flytekit.core.promise#flytekitcorepromiseuniontransformer) |Transformer that handles a typing. |
| [`flytekit.core.promise.VoidPromise`](../packages/flytekit.core.promise#flytekitcorepromisevoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.python_auto_container.ABC`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.core.python_auto_container.BaseAccelerator`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerbaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.core.python_auto_container.CopyFileDetection`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containercopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.core.python_auto_container.DefaultNotebookTaskResolver`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaultnotebooktaskresolver) |This resolved is used when the task is defined in a notebook. |
| [`flytekit.core.python_auto_container.DefaultTaskResolver`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaulttaskresolver) |Please see the notes in the TaskResolverMixin as it describes this default behavior. |
| [`flytekit.core.python_auto_container.FlyteContextManager`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.python_auto_container.FlyteTrackedABC`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerflytetrackedabc) |This class exists because if you try to inherit from abc. |
| [`flytekit.core.python_auto_container.ImageBuildEngine`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerimagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.core.python_auto_container.ImageConfig`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.core.python_auto_container.ImageSpec`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.core.python_auto_container.PickledEntity`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentity) |Represents the structure of the pickled object stored in the . |
| [`flytekit.core.python_auto_container.PickledEntityMetadata`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentitymetadata) |Metadata for a pickled entity containing version information. |
| [`flytekit.core.python_auto_container.PodTemplate`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.python_auto_container.PythonAutoContainerTask`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_auto_container.PythonTask`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.python_auto_container.ResourceSpec`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerresourcespec) | |
| [`flytekit.core.python_auto_container.Resources`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.python_auto_container.Secret`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containersecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.core.python_auto_container.SecurityContext`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containersecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.core.python_auto_container.SerializationSettings`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containerserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.python_auto_container.TaskMetadata`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containertaskmetadata) |Metadata for a Task. |
| [`flytekit.core.python_auto_container.TaskResolverMixin`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containertaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.python_auto_container.TrackedInstance`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containertrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.python_auto_container.TypeVar`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containertypevar) |Type variable. |
| [`flytekit.core.python_auto_container.timeit`](../packages/flytekit.core.python_auto_container#flytekitcorepython_auto_containertimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.python_customized_container_task.Any`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.python_customized_container_task.ExecutableTemplateShimTask`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskexecutabletemplateshimtask) |The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`flytekit.core.python_customized_container_task.FlyteContext`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.python_customized_container_task.Image`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskimage) |Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.core.python_customized_container_task.ImageConfig`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.core.python_customized_container_task.ImageSpec`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.core.python_customized_container_task.PythonCustomizedContainerTask`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskpythoncustomizedcontainertask) |Please take a look at the comments for :py:class`flytekit. |
| [`flytekit.core.python_customized_container_task.PythonTask`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.python_customized_container_task.ResourceSpec`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskresourcespec) | |
| [`flytekit.core.python_customized_container_task.Resources`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.python_customized_container_task.Secret`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasksecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.core.python_customized_container_task.SecurityContext`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasksecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.core.python_customized_container_task.SerializationSettings`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.python_customized_container_task.ShimTaskExecutor`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_taskshimtaskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.core.python_customized_container_task.Task`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktask) |The base of all Tasks in flytekit. |
| [`flytekit.core.python_customized_container_task.TaskResolverMixin`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.python_customized_container_task.TaskTemplateResolver`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktasktemplateresolver) |This is a special resolver that resolves the task above at execution time, using only the ``TaskTemplate``,. |
| [`flytekit.core.python_customized_container_task.TrackedInstance`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.python_customized_container_task.TypeVar`](../packages/flytekit.core.python_customized_container_task#flytekitcorepython_customized_container_tasktypevar) |Type variable. |
| [`flytekit.core.python_function_task.ABC`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.core.python_function_task.Any`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.python_function_task.AsyncPythonFunctionTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskasyncpythonfunctiontask) |This is the base task for eager tasks, as well as normal async tasks. |
| [`flytekit.core.python_function_task.Controller`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskcontroller) |This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint. |
| [`flytekit.core.python_function_task.Deck`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskdeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.core.python_function_task.Docstring`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskdocstring) | |
| [`flytekit.core.python_function_task.EagerAsyncPythonFunctionTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerasyncpythonfunctiontask) |This is the base eager task (aka eager workflow) type. |
| [`flytekit.core.python_function_task.EagerException`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerexception) |Raised when a node in an eager workflow encounters an error. |
| [`flytekit.core.python_function_task.EagerFailureHandlerTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerfailurehandlertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_function_task.EagerFailureTaskResolver`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskeagerfailuretaskresolver) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.python_function_task.Enum`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskenum) |Create a collection of name/value pairs. |
| [`flytekit.core.python_function_task.ExecutionState`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.python_function_task.FlyteContext`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.python_function_task.FlyteContextManager`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.python_function_task.FlyteNonRecoverableSystemException`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskflytenonrecoverablesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.python_function_task.FlyteTrackedABC`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskflytetrackedabc) |This class exists because if you try to inherit from abc. |
| [`flytekit.core.python_function_task.FlyteValueException`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskflytevalueexception) |Inappropriate argument value (of correct type). |
| [`flytekit.core.python_function_task.ImageConfig`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.core.python_function_task.ImageSpec`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.core.python_function_task.Interface`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.python_function_task.LiteralMap`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskliteralmap) | |
| [`flytekit.core.python_function_task.OrderedDict`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.core.python_function_task.Promise`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.python_function_task.PythonAutoContainerTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.python_function_task.PythonFunctionTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.python_function_task.PythonFunctionWorkflow`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpythonfunctionworkflow) |Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`flytekit.core.python_function_task.PythonInstanceTask`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskpythoninstancetask) |This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.core.python_function_task.SerializationSettings`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.python_function_task.Task`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_tasktask) |The base of all Tasks in flytekit. |
| [`flytekit.core.python_function_task.TaskMetadata`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_tasktaskmetadata) |Metadata for a Task. |
| [`flytekit.core.python_function_task.TaskResolverMixin`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_tasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.python_function_task.TypeVar`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_tasktypevar) |Type variable. |
| [`flytekit.core.python_function_task.ValueIn`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskvaluein) | |
| [`flytekit.core.python_function_task.VoidPromise`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.python_function_task.WorkflowBase`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskworkflowbase) | |
| [`flytekit.core.python_function_task.WorkflowFailurePolicy`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskworkflowfailurepolicy) |Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.core.python_function_task.WorkflowMetadata`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskworkflowmetadata) | |
| [`flytekit.core.python_function_task.WorkflowMetadataDefaults`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_taskworkflowmetadatadefaults) |This class is similarly named to the one above. |
| [`flytekit.core.python_function_task.suppress`](../packages/flytekit.core.python_function_task#flytekitcorepython_function_tasksuppress) |Context manager to suppress specified exceptions. |
| [`flytekit.core.reference.FlyteValidationException`](../packages/flytekit.core.reference#flytekitcorereferenceflytevalidationexception) |Assertion failed. |
| [`flytekit.core.reference.ReferenceLaunchPlan`](../packages/flytekit.core.reference#flytekitcorereferencereferencelaunchplan) |A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.core.reference.ReferenceTask`](../packages/flytekit.core.reference#flytekitcorereferencereferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.reference.ReferenceWorkflow`](../packages/flytekit.core.reference#flytekitcorereferencereferenceworkflow) |A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.core.reference_entity.ABC`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.core.reference_entity.Any`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityany) |Special type indicating an unconstrained type. |
| [`flytekit.core.reference_entity.BranchEvalMode`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitybranchevalmode) |This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.core.reference_entity.ExecutionState`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.reference_entity.FlyteContext`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.reference_entity.Interface`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.reference_entity.LaunchPlanReference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitylaunchplanreference) |A reference object containing metadata that points to a remote launch plan. |
| [`flytekit.core.reference_entity.Promise`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitypromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.reference_entity.Reference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreference) | |
| [`flytekit.core.reference_entity.ReferenceEntity`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreferenceentity) | |
| [`flytekit.core.reference_entity.ReferenceSpec`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreferencespec) | |
| [`flytekit.core.reference_entity.ReferenceTemplate`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityreferencetemplate) | |
| [`flytekit.core.reference_entity.TaskReference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitytaskreference) |A reference object containing metadata that points to a remote task. |
| [`flytekit.core.reference_entity.TypeEngine`](../packages/flytekit.core.reference_entity#flytekitcorereference_entitytypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.reference_entity.VoidPromise`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.reference_entity.WorkflowReference`](../packages/flytekit.core.reference_entity#flytekitcorereference_entityworkflowreference) |A reference object containing metadata that points to a remote workflow. |
| [`flytekit.core.resources.BaseAccelerator`](../packages/flytekit.core.resources#flytekitcoreresourcesbaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.core.resources.DataClassJSONMixin`](../packages/flytekit.core.resources#flytekitcoreresourcesdataclassjsonmixin) | |
| [`flytekit.core.resources.ResourceSpec`](../packages/flytekit.core.resources#flytekitcoreresourcesresourcespec) | |
| [`flytekit.core.resources.Resources`](../packages/flytekit.core.resources#flytekitcoreresourcesresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.schedule.CronSchedule`](../packages/flytekit.core.schedule#flytekitcoreschedulecronschedule) |Use this when you have a launch plan that you want to run on a cron expression. |
| [`flytekit.core.schedule.FixedRate`](../packages/flytekit.core.schedule#flytekitcoreschedulefixedrate) |Use this class to schedule a fixed-rate interval for a launch plan. |
| [`flytekit.core.schedule.LaunchPlanTriggerBase`](../packages/flytekit.core.schedule#flytekitcoreschedulelaunchplantriggerbase) |Base class for protocol classes. |
| [`flytekit.core.schedule.OnSchedule`](../packages/flytekit.core.schedule#flytekitcorescheduleonschedule) |Base class for protocol classes. |
| [`flytekit.core.schedule.Protocol`](../packages/flytekit.core.schedule#flytekitcorescheduleprotocol) |Base class for protocol classes. |
| [`flytekit.core.shim_task.Any`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.shim_task.ExecutableTemplateShimTask`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskexecutabletemplateshimtask) |The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`flytekit.core.shim_task.ExecutionParameters`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.core.shim_task.ExecutionState`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.shim_task.FlyteContext`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.shim_task.FlyteContextManager`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.shim_task.Generic`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskgeneric) |Abstract base class for generic types. |
| [`flytekit.core.shim_task.ShimTaskExecutor`](../packages/flytekit.core.shim_task#flytekitcoreshim_taskshimtaskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.core.shim_task.TrackedInstance`](../packages/flytekit.core.shim_task#flytekitcoreshim_tasktrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.shim_task.TypeEngine`](../packages/flytekit.core.shim_task#flytekitcoreshim_tasktypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.shim_task.TypeVar`](../packages/flytekit.core.shim_task#flytekitcoreshim_tasktypevar) |Type variable. |
| [`flytekit.core.task.Any`](../packages/flytekit.core.task#flytekitcoretaskany) |Special type indicating an unconstrained type. |
| [`flytekit.core.task.AsyncPythonFunctionTask`](../packages/flytekit.core.task#flytekitcoretaskasyncpythonfunctiontask) |This is the base task for eager tasks, as well as normal async tasks. |
| [`flytekit.core.task.BaseAccelerator`](../packages/flytekit.core.task#flytekitcoretaskbaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.core.task.Cache`](../packages/flytekit.core.task#flytekitcoretaskcache) |Cache configuration for a task. |
| [`flytekit.core.task.DeckField`](../packages/flytekit.core.task#flytekitcoretaskdeckfield) |DeckField is used to specify the fields that will be rendered in the deck. |
| [`flytekit.core.task.Documentation`](../packages/flytekit.core.task#flytekitcoretaskdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.core.task.EagerAsyncPythonFunctionTask`](../packages/flytekit.core.task#flytekitcoretaskeagerasyncpythonfunctiontask) |This is the base eager task (aka eager workflow) type. |
| [`flytekit.core.task.Echo`](../packages/flytekit.core.task#flytekitcoretaskecho) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.task.ImageSpec`](../packages/flytekit.core.task#flytekitcoretaskimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.core.task.Interface`](../packages/flytekit.core.task#flytekitcoretaskinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.task.ParamSpec`](../packages/flytekit.core.task#flytekitcoretaskparamspec) |Parameter specification variable. |
| [`flytekit.core.task.PodTemplate`](../packages/flytekit.core.task#flytekitcoretaskpodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.task.PythonFunctionTask`](../packages/flytekit.core.task#flytekitcoretaskpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.core.task.PythonTask`](../packages/flytekit.core.task#flytekitcoretaskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.task.ReferenceEntity`](../packages/flytekit.core.task#flytekitcoretaskreferenceentity) | |
| [`flytekit.core.task.ReferenceTask`](../packages/flytekit.core.task#flytekitcoretaskreferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.core.task.Resources`](../packages/flytekit.core.task#flytekitcoretaskresources) |This class is used to specify both resource requests and resource limits. |
| [`flytekit.core.task.Secret`](../packages/flytekit.core.task#flytekitcoretasksecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.core.task.TaskMetadata`](../packages/flytekit.core.task#flytekitcoretasktaskmetadata) |Metadata for a Task. |
| [`flytekit.core.task.TaskPlugins`](../packages/flytekit.core.task#flytekitcoretasktaskplugins) |This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |
| [`flytekit.core.task.TaskReference`](../packages/flytekit.core.task#flytekitcoretasktaskreference) |A reference object containing metadata that points to a remote task. |
| [`flytekit.core.task.TaskResolverMixin`](../packages/flytekit.core.task#flytekitcoretasktaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.core.task.TypeVar`](../packages/flytekit.core.task#flytekitcoretasktypevar) |Type variable. |
| [`flytekit.core.task.VersionParameters`](../packages/flytekit.core.task#flytekitcoretaskversionparameters) |Parameters used for version hash generation. |
| [`flytekit.core.task.partial`](../packages/flytekit.core.task#flytekitcoretaskpartial) |Create a new function with partial application of the given arguments. |
| [`flytekit.core.task.vscode`](../packages/flytekit.core.task#flytekitcoretaskvscode) |Abstract class for class decorators. |
| [`flytekit.core.testing.MagicMock`](../packages/flytekit.core.testing#flytekitcoretestingmagicmock) |MagicMock is a subclass of Mock with default implementations. |
| [`flytekit.core.testing.PythonTask`](../packages/flytekit.core.testing#flytekitcoretestingpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.testing.ReferenceEntity`](../packages/flytekit.core.testing#flytekitcoretestingreferenceentity) | |
| [`flytekit.core.testing.WorkflowBase`](../packages/flytekit.core.testing#flytekitcoretestingworkflowbase) | |
| [`flytekit.core.tracked_abc.ABC`](../packages/flytekit.core.tracked_abc#flytekitcoretracked_abcabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.core.tracked_abc.FlyteTrackedABC`](../packages/flytekit.core.tracked_abc#flytekitcoretracked_abcflytetrackedabc) |This class exists because if you try to inherit from abc. |
| [`flytekit.core.tracked_abc.TrackedInstance`](../packages/flytekit.core.tracked_abc#flytekitcoretracked_abctrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.tracker.FeatureFlags`](../packages/flytekit.core.tracker#flytekitcoretrackerfeatureflags) | |
| [`flytekit.core.tracker.InstanceTrackingMeta`](../packages/flytekit.core.tracker#flytekitcoretrackerinstancetrackingmeta) |Please see the original class :py:class`flytekit. |
| [`flytekit.core.tracker.ModuleType`](../packages/flytekit.core.tracker#flytekitcoretrackermoduletype) |Create a module object. |
| [`flytekit.core.tracker.Path`](../packages/flytekit.core.tracker#flytekitcoretrackerpath) |PurePath subclass that can make system calls. |
| [`flytekit.core.tracker.TrackedInstance`](../packages/flytekit.core.tracker#flytekitcoretrackertrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.core.type_engine.ABC`](../packages/flytekit.core.type_engine#flytekitcoretype_engineabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.core.type_engine.Any`](../packages/flytekit.core.type_engine#flytekitcoretype_engineany) |Special type indicating an unconstrained type. |
| [`flytekit.core.type_engine.AsyncTypeTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.BatchSize`](../packages/flytekit.core.type_engine#flytekitcoretype_enginebatchsize) |This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`flytekit.core.type_engine.Binary`](../packages/flytekit.core.type_engine#flytekitcoretype_enginebinary) | |
| [`flytekit.core.type_engine.BinaryIOTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginebinaryiotransformer) |Handler for BinaryIO. |
| [`flytekit.core.type_engine.DataClassJSONMixin`](../packages/flytekit.core.type_engine#flytekitcoretype_enginedataclassjsonmixin) | |
| [`flytekit.core.type_engine.DataClassJsonMixin`](../packages/flytekit.core.type_engine#flytekitcoretype_enginedataclassjsonmixin) |DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`flytekit.core.type_engine.DataclassTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginedataclasstransformer) |The Dataclass Transformer provides a type transformer for dataclasses. |
| [`flytekit.core.type_engine.DictTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginedicttransformer) |Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`flytekit.core.type_engine.EnumTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineenumtransformer) |Enables converting a python type enum. |
| [`flytekit.core.type_engine.FlyteAnnotation`](../packages/flytekit.core.type_engine#flytekitcoretype_engineflyteannotation) |A core object to add arbitrary annotations to flyte types. |
| [`flytekit.core.type_engine.FlyteContext`](../packages/flytekit.core.type_engine#flytekitcoretype_engineflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.type_engine.GenericAlias`](../packages/flytekit.core.type_engine#flytekitcoretype_enginegenericalias) |Represent a PEP 585 generic type. |
| [`flytekit.core.type_engine.HashMethod`](../packages/flytekit.core.type_engine#flytekitcoretype_enginehashmethod) |Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.core.type_engine.JSONDecoder`](../packages/flytekit.core.type_engine#flytekitcoretype_enginejsondecoder) |Abstract base class for generic types. |
| [`flytekit.core.type_engine.JSONEncoder`](../packages/flytekit.core.type_engine#flytekitcoretype_enginejsonencoder) |Abstract base class for generic types. |
| [`flytekit.core.type_engine.ListTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginelisttransformer) |Transformer that handles a univariate typing. |
| [`flytekit.core.type_engine.Literal`](../packages/flytekit.core.type_engine#flytekitcoretype_engineliteral) | |
| [`flytekit.core.type_engine.LiteralCollection`](../packages/flytekit.core.type_engine#flytekitcoretype_engineliteralcollection) | |
| [`flytekit.core.type_engine.LiteralMap`](../packages/flytekit.core.type_engine#flytekitcoretype_engineliteralmap) | |
| [`flytekit.core.type_engine.LiteralType`](../packages/flytekit.core.type_engine#flytekitcoretype_engineliteraltype) | |
| [`flytekit.core.type_engine.LiteralsResolver`](../packages/flytekit.core.type_engine#flytekitcoretype_engineliteralsresolver) |LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.core.type_engine.Message`](../packages/flytekit.core.type_engine#flytekitcoretype_enginemessage) |Abstract base class for protocol messages. |
| [`flytekit.core.type_engine.MessagePackDecoder`](../packages/flytekit.core.type_engine#flytekitcoretype_enginemessagepackdecoder) |Abstract base class for generic types. |
| [`flytekit.core.type_engine.MessagePackEncoder`](../packages/flytekit.core.type_engine#flytekitcoretype_enginemessagepackencoder) |Abstract base class for generic types. |
| [`flytekit.core.type_engine.OrderedDict`](../packages/flytekit.core.type_engine#flytekitcoretype_engineordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.core.type_engine.Primitive`](../packages/flytekit.core.type_engine#flytekitcoretype_engineprimitive) | |
| [`flytekit.core.type_engine.ProtobufTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineprotobuftransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.RestrictedTypeError`](../packages/flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypeerror) |Common base class for all non-exit exceptions. |
| [`flytekit.core.type_engine.RestrictedTypeTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginerestrictedtypetransformer) |Types registered with the RestrictedTypeTransformer are not allowed to be converted to and from literals. |
| [`flytekit.core.type_engine.Scalar`](../packages/flytekit.core.type_engine#flytekitcoretype_enginescalar) | |
| [`flytekit.core.type_engine.SimpleTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginesimpletransformer) |A Simple implementation of a type transformer that uses simple lambdas to transform and reduces boilerplate. |
| [`flytekit.core.type_engine.SimpleType`](../packages/flytekit.core.type_engine#flytekitcoretype_enginesimpletype) | |
| [`flytekit.core.type_engine.Struct`](../packages/flytekit.core.type_engine#flytekitcoretype_enginestruct) |A ProtocolMessage. |
| [`flytekit.core.type_engine.TextIOTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetextiotransformer) |Handler for TextIO. |
| [`flytekit.core.type_engine.TypeAnnotationModel`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypeannotationmodel) |Python class representation of the flyteidl TypeAnnotation message. |
| [`flytekit.core.type_engine.TypeEngine`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.type_engine.TypeStructure`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypestructure) |Models _types_pb2. |
| [`flytekit.core.type_engine.TypeTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.core.type_engine.TypeTransformerFailedError`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.core.type_engine.Union`](../packages/flytekit.core.type_engine#flytekitcoretype_engineunion) | |
| [`flytekit.core.type_engine.UnionTransformer`](../packages/flytekit.core.type_engine#flytekitcoretype_engineuniontransformer) |Transformer that handles a typing. |
| [`flytekit.core.type_engine.UnionType`](../packages/flytekit.core.type_engine#flytekitcoretype_engineuniontype) |Models _types_pb2. |
| [`flytekit.core.type_engine.Void`](../packages/flytekit.core.type_engine#flytekitcoretype_enginevoid) | |
| [`flytekit.core.type_engine.timeit`](../packages/flytekit.core.type_engine#flytekitcoretype_enginetimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.type_match_checking.EnumType`](../packages/flytekit.core.type_match_checking#flytekitcoretype_match_checkingenumtype) |Models _types_pb2. |
| [`flytekit.core.type_match_checking.LiteralType`](../packages/flytekit.core.type_match_checking#flytekitcoretype_match_checkingliteraltype) | |
| [`flytekit.core.type_match_checking.UnionType`](../packages/flytekit.core.type_match_checking#flytekitcoretype_match_checkinguniontype) |Models _types_pb2. |
| [`flytekit.core.utils.ABC`](../packages/flytekit.core.utils#flytekitcoreutilsabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.core.utils.Any`](../packages/flytekit.core.utils#flytekitcoreutilsany) |Special type indicating an unconstrained type. |
| [`flytekit.core.utils.AutoDeletingTempDir`](../packages/flytekit.core.utils#flytekitcoreutilsautodeletingtempdir) |Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`flytekit.core.utils.ClassDecorator`](../packages/flytekit.core.utils#flytekitcoreutilsclassdecorator) |Abstract class for class decorators. |
| [`flytekit.core.utils.Directory`](../packages/flytekit.core.utils#flytekitcoreutilsdirectory) | |
| [`flytekit.core.utils.Path`](../packages/flytekit.core.utils#flytekitcoreutilspath) |PurePath subclass that can make system calls. |
| [`flytekit.core.utils.PodTemplate`](../packages/flytekit.core.utils#flytekitcoreutilspodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.core.utils.ResourceSpec`](../packages/flytekit.core.utils#flytekitcoreutilsresourcespec) | |
| [`flytekit.core.utils.SerializationSettings`](../packages/flytekit.core.utils#flytekitcoreutilsserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.utils.timeit`](../packages/flytekit.core.utils#flytekitcoreutilstimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.core.worker_queue.Controller`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuecontroller) |This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint. |
| [`flytekit.core.worker_queue.Deck`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuedeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.core.worker_queue.Enum`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueenum) |Create a collection of name/value pairs. |
| [`flytekit.core.worker_queue.FlyteContextManager`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.worker_queue.FlyteSystemException`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueflytesystemexception) |Common base class for all non-exit exceptions. |
| [`flytekit.core.worker_queue.ImageConfig`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.core.worker_queue.ItemStatus`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueitemstatus) |Create a collection of name/value pairs. |
| [`flytekit.core.worker_queue.Labels`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuelabels) | |
| [`flytekit.core.worker_queue.LaunchPlan`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuelaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.core.worker_queue.Options`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.core.worker_queue.PythonTask`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuepythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.worker_queue.RateLimiter`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueratelimiter) |Rate limiter that allows up to a certain number of requests per minute. |
| [`flytekit.core.worker_queue.ReferenceEntity`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queuereferenceentity) | |
| [`flytekit.core.worker_queue.SerializationSettings`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.core.worker_queue.Update`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueupdate) | |
| [`flytekit.core.worker_queue.WorkItem`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueworkitem) |This is a class to keep track of what the user requested. |
| [`flytekit.core.worker_queue.WorkflowBase`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueworkflowbase) | |
| [`flytekit.core.worker_queue.WorkflowExecutionPhase`](../packages/flytekit.core.worker_queue#flytekitcoreworker_queueworkflowexecutionphase) |This class holds enum values used for setting notifications. |
| [`flytekit.core.workflow.Any`](../packages/flytekit.core.workflow#flytekitcoreworkflowany) |Special type indicating an unconstrained type. |
| [`flytekit.core.workflow.ClassStorageTaskResolver`](../packages/flytekit.core.workflow#flytekitcoreworkflowclassstoragetaskresolver) |Stores tasks inside a class variable. |
| [`flytekit.core.workflow.CompilationState`](../packages/flytekit.core.workflow#flytekitcoreworkflowcompilationstate) |Compilation state is used during the compilation of a workflow or task. |
| [`flytekit.core.workflow.ConditionalSection`](../packages/flytekit.core.workflow#flytekitcoreworkflowconditionalsection) |ConditionalSection is used to denote a condition within a Workflow. |
| [`flytekit.core.workflow.Description`](../packages/flytekit.core.workflow#flytekitcoreworkflowdescription) |Full user description with formatting preserved. |
| [`flytekit.core.workflow.Docstring`](../packages/flytekit.core.workflow#flytekitcoreworkflowdocstring) | |
| [`flytekit.core.workflow.Documentation`](../packages/flytekit.core.workflow#flytekitcoreworkflowdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.core.workflow.Enum`](../packages/flytekit.core.workflow#flytekitcoreworkflowenum) |Create a collection of name/value pairs. |
| [`flytekit.core.workflow.ExecutionState`](../packages/flytekit.core.workflow#flytekitcoreworkflowexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.core.workflow.FlyteContext`](../packages/flytekit.core.workflow#flytekitcoreworkflowflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.core.workflow.FlyteContextManager`](../packages/flytekit.core.workflow#flytekitcoreworkflowflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.core.workflow.FlyteEntities`](../packages/flytekit.core.workflow#flytekitcoreworkflowflyteentities) |This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`flytekit.core.workflow.FlyteError`](../packages/flytekit.core.workflow#flytekitcoreworkflowflyteerror) |Special Task type that will be used in the failure node. |
| [`flytekit.core.workflow.FlyteFailureNodeInputMismatchException`](../packages/flytekit.core.workflow#flytekitcoreworkflowflytefailurenodeinputmismatchexception) |Assertion failed. |
| [`flytekit.core.workflow.FlyteValidationException`](../packages/flytekit.core.workflow#flytekitcoreworkflowflytevalidationexception) |Assertion failed. |
| [`flytekit.core.workflow.FlyteValueException`](../packages/flytekit.core.workflow#flytekitcoreworkflowflytevalueexception) |Inappropriate argument value (of correct type). |
| [`flytekit.core.workflow.ImperativeWorkflow`](../packages/flytekit.core.workflow#flytekitcoreworkflowimperativeworkflow) |An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`flytekit.core.workflow.Interface`](../packages/flytekit.core.workflow#flytekitcoreworkflowinterface) |A Python native interface object, like inspect. |
| [`flytekit.core.workflow.Node`](../packages/flytekit.core.workflow#flytekitcoreworkflownode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.core.workflow.NodeOutput`](../packages/flytekit.core.workflow#flytekitcoreworkflownodeoutput) | |
| [`flytekit.core.workflow.Options`](../packages/flytekit.core.workflow#flytekitcoreworkflowoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.core.workflow.ParamSpec`](../packages/flytekit.core.workflow#flytekitcoreworkflowparamspec) |Parameter specification variable. |
| [`flytekit.core.workflow.Promise`](../packages/flytekit.core.workflow#flytekitcoreworkflowpromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.core.workflow.PythonAutoContainerTask`](../packages/flytekit.core.workflow#flytekitcoreworkflowpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.core.workflow.PythonFunctionWorkflow`](../packages/flytekit.core.workflow#flytekitcoreworkflowpythonfunctionworkflow) |Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`flytekit.core.workflow.PythonTask`](../packages/flytekit.core.workflow#flytekitcoreworkflowpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.core.workflow.ReferenceEntity`](../packages/flytekit.core.workflow#flytekitcoreworkflowreferenceentity) | |
| [`flytekit.core.workflow.ReferenceWorkflow`](../packages/flytekit.core.workflow#flytekitcoreworkflowreferenceworkflow) |A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.core.workflow.Task`](../packages/flytekit.core.workflow#flytekitcoreworkflowtask) |The base of all Tasks in flytekit. |
| [`flytekit.core.workflow.TypeEngine`](../packages/flytekit.core.workflow#flytekitcoreworkflowtypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.core.workflow.VoidPromise`](../packages/flytekit.core.workflow#flytekitcoreworkflowvoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.core.workflow.WorkflowBase`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowbase) | |
| [`flytekit.core.workflow.WorkflowFailurePolicy`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowfailurepolicy) |Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.core.workflow.WorkflowMetadata`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowmetadata) | |
| [`flytekit.core.workflow.WorkflowMetadataDefaults`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowmetadatadefaults) |This class is similarly named to the one above. |
| [`flytekit.core.workflow.WorkflowReference`](../packages/flytekit.core.workflow#flytekitcoreworkflowworkflowreference) |A reference object containing metadata that points to a remote workflow. |
| [`flytekit.deck.Deck`](../packages/flytekit.deck#flytekitdeckdeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.deck.DeckField`](../packages/flytekit.deck#flytekitdeckdeckfield) |DeckField is used to specify the fields that will be rendered in the deck. |
| [`flytekit.deck.MarkdownRenderer`](../packages/flytekit.deck#flytekitdeckmarkdownrenderer) |Convert a markdown string to HTML and return HTML as a unicode string. |
| [`flytekit.deck.SourceCodeRenderer`](../packages/flytekit.deck#flytekitdecksourcecoderenderer) |Convert Python source code to HTML, and return HTML as a unicode string. |
| [`flytekit.deck.TopFrameRenderer`](../packages/flytekit.deck#flytekitdecktopframerenderer) |Render a DataFrame as an HTML table. |
| [`flytekit.deck.deck.Deck`](../packages/flytekit.deck.deck#flytekitdeckdeckdeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`flytekit.deck.deck.DeckField`](../packages/flytekit.deck.deck#flytekitdeckdeckdeckfield) |DeckField is used to specify the fields that will be rendered in the deck. |
| [`flytekit.deck.deck.ExecutionParameters`](../packages/flytekit.deck.deck#flytekitdeckdeckexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.deck.deck.ExecutionState`](../packages/flytekit.deck.deck#flytekitdeckdeckexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.deck.deck.FlyteContext`](../packages/flytekit.deck.deck#flytekitdeckdeckflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.deck.deck.FlyteContextManager`](../packages/flytekit.deck.deck#flytekitdeckdeckflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.deck.deck.Template`](../packages/flytekit.deck.deck#flytekitdeckdecktemplate) |A string class for supporting $-substitutions. |
| [`flytekit.deck.deck.TimeLineDeck`](../packages/flytekit.deck.deck#flytekitdeckdecktimelinedeck) |The TimeLineDeck class is designed to render the execution time of each part of a task. |
| [`flytekit.deck.renderer.Any`](../packages/flytekit.deck.renderer#flytekitdeckrendererany) |Special type indicating an unconstrained type. |
| [`flytekit.deck.renderer.ArrowRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrendererarrowrenderer) |Render an Arrow dataframe as an HTML table. |
| [`flytekit.deck.renderer.MarkdownRenderer`](../packages/flytekit.deck.renderer#flytekitdeckrenderermarkdownrenderer) |Convert a markdown string to HTML and return HTML as a unicode string. |
| [`flytekit.deck.renderer.Protocol`](../packages/flytekit.deck.renderer#flytekitdeckrendererprotocol) |Base class for protocol classes. |
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
| [`flytekit.exceptions.system.FlyteException`](../packages/flytekit.exceptions.system#flytekitexceptionssystemflyteexception) |Common base class for all non-exit exceptions. |
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
| [`flytekit.exceptions.utils.FlyteUserException`](../packages/flytekit.exceptions.utils#flytekitexceptionsutilsflyteuserexception) |Common base class for all non-exit exceptions. |
| [`flytekit.experimental.eager_function.DataConfig`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functiondataconfig) |Any data storage specific configuration. |
| [`flytekit.experimental.eager_function.ExecutionState`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functionexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.experimental.eager_function.FlyteContext`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functionflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.experimental.eager_function.FlyteContextManager`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functionflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.experimental.eager_function.FlyteRemote`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functionflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.experimental.eager_function.PlatformConfig`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functionplatformconfig) |This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`flytekit.experimental.eager_function.S3Config`](../packages/flytekit.experimental.eager_function#flytekitexperimentaleager_functions3config) |S3 specific configuration. |
| [`flytekit.extend.ClassStorageTaskResolver`](../packages/flytekit.extend#flytekitextendclassstoragetaskresolver) |Stores tasks inside a class variable. |
| [`flytekit.extend.DictTransformer`](../packages/flytekit.extend#flytekitextenddicttransformer) |Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`flytekit.extend.ExecutableTemplateShimTask`](../packages/flytekit.extend#flytekitextendexecutabletemplateshimtask) |The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`flytekit.extend.ExecutionState`](../packages/flytekit.extend#flytekitextendexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.extend.FileAccessProvider`](../packages/flytekit.extend#flytekitextendfileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.extend.IgnoreOutputs`](../packages/flytekit.extend#flytekitextendignoreoutputs) |This exception should be used to indicate that the outputs generated by this can be safely ignored. |
| [`flytekit.extend.Image`](../packages/flytekit.extend#flytekitextendimage) |Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.extend.ImageConfig`](../packages/flytekit.extend#flytekitextendimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.extend.Interface`](../packages/flytekit.extend#flytekitextendinterface) |A Python native interface object, like inspect. |
| [`flytekit.extend.Promise`](../packages/flytekit.extend#flytekitextendpromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.extend.PythonCustomizedContainerTask`](../packages/flytekit.extend#flytekitextendpythoncustomizedcontainertask) |Please take a look at the comments for :py:class`flytekit. |
| [`flytekit.extend.PythonTask`](../packages/flytekit.extend#flytekitextendpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.extend.SQLTask`](../packages/flytekit.extend#flytekitextendsqltask) |Base task types for all SQL tasks. |
| [`flytekit.extend.SecretsManager`](../packages/flytekit.extend#flytekitextendsecretsmanager) |This provides a secrets resolution logic at runtime. |
| [`flytekit.extend.SerializationSettings`](../packages/flytekit.extend#flytekitextendserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.extend.ShimTaskExecutor`](../packages/flytekit.extend#flytekitextendshimtaskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.extend.TaskPlugins`](../packages/flytekit.extend#flytekitextendtaskplugins) |This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |
| [`flytekit.extend.TaskResolverMixin`](../packages/flytekit.extend#flytekitextendtaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.extend.TypeEngine`](../packages/flytekit.extend#flytekitextendtypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.extend.TypeTransformer`](../packages/flytekit.extend#flytekitextendtypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extend.backend.base_agent.AgentBase`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentagentbase) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.extend.backend.base_agent.AgentRegistry`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentagentregistry) |This is the registry for all connectors. |
| [`flytekit.extend.backend.base_agent.AsyncAgentBase`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentasyncagentbase) |This is the base class for all async connectors. |
| [`flytekit.extend.backend.base_agent.AsyncAgentExecutorMixin`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentasyncagentexecutormixin) |This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_agent.Resource`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentresource) |This is the output resource of the job. |
| [`flytekit.extend.backend.base_agent.ResourceMeta`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentresourcemeta) |This is the metadata for the job. |
| [`flytekit.extend.backend.base_agent.SyncAgentBase`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentsyncagentbase) |This is the base class for all sync connectors. |
| [`flytekit.extend.backend.base_agent.SyncAgentExecutorMixin`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentsyncagentexecutormixin) |This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_agent.TaskCategory`](../packages/flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttaskcategory) | |
| [`flytekit.extend.backend.base_connector.ABC`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.extend.backend.base_connector.Agent`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectoragent) |A ProtocolMessage. |
| [`flytekit.extend.backend.base_connector.Any`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorany) |Special type indicating an unconstrained type. |
| [`flytekit.extend.backend.base_connector.AsyncConnectorBase`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorbase) |This is the base class for all async connectors. |
| [`flytekit.extend.backend.base_connector.AsyncConnectorExecutorMixin`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorasyncconnectorexecutormixin) |This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.ConnectorBase`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorbase) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.extend.backend.base_connector.ConnectorRegistry`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorconnectorregistry) |This is the registry for all connectors. |
| [`flytekit.extend.backend.base_connector.ExecutionState`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.extend.backend.base_connector.FlyteConnectorNotFound`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorflyteconnectornotfound) |Assertion failed. |
| [`flytekit.extend.backend.base_connector.FlyteContext`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.extend.backend.base_connector.FlyteContextManager`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.extend.backend.base_connector.FlyteUserException`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorflyteuserexception) |Common base class for all non-exit exceptions. |
| [`flytekit.extend.backend.base_connector.FrameType`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorframetype) | |
| [`flytekit.extend.backend.base_connector.GetTaskLogsResponse`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorgettasklogsresponse) |A ProtocolMessage. |
| [`flytekit.extend.backend.base_connector.GetTaskMetricsResponse`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorgettaskmetricsresponse) |A ProtocolMessage. |
| [`flytekit.extend.backend.base_connector.ImageConfig`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.extend.backend.base_connector.LiteralMap`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorliteralmap) | |
| [`flytekit.extend.backend.base_connector.OrderedDict`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.extend.backend.base_connector.Progress`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorprogress) |Renders an auto-updating progress bar(s). |
| [`flytekit.extend.backend.base_connector.PythonFunctionTask`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.extend.backend.base_connector.PythonTask`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.extend.backend.base_connector.Resource`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresource) |This is the output resource of the job. |
| [`flytekit.extend.backend.base_connector.ResourceMeta`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorresourcemeta) |This is the metadata for the job. |
| [`flytekit.extend.backend.base_connector.RichHandler`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorrichhandler) |A logging handler that renders output with Rich. |
| [`flytekit.extend.backend.base_connector.SerializationSettings`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.extend.backend.base_connector.Struct`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorstruct) |A ProtocolMessage. |
| [`flytekit.extend.backend.base_connector.SyncConnectorBase`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorbase) |This is the base class for all sync connectors. |
| [`flytekit.extend.backend.base_connector.SyncConnectorExecutorMixin`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorsyncconnectorexecutormixin) |This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`flytekit.extend.backend.base_connector.TaskCategory`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortaskcategory) | |
| [`flytekit.extend.backend.base_connector.TaskExecution`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortaskexecution) |A ProtocolMessage. |
| [`flytekit.extend.backend.base_connector.TaskExecutionMetadata`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortaskexecutionmetadata) | |
| [`flytekit.extend.backend.base_connector.TaskLog`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortasklog) |A ProtocolMessage. |
| [`flytekit.extend.backend.base_connector.TaskTemplate`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortasktemplate) | |
| [`flytekit.extend.backend.base_connector.TypeEngine`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectortypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.extend.backend.base_connector.partial`](../packages/flytekit.extend.backend.base_connector#flytekitextendbackendbase_connectorpartial) |Create a new function with partial application of the given arguments. |
| [`flytekit.extend.backend.utils.TaskExecution`](../packages/flytekit.extend.backend.utils#flytekitextendbackendutilstaskexecution) |A ProtocolMessage. |
| [`flytekit.extend.backend.utils.TaskTemplate`](../packages/flytekit.extend.backend.utils#flytekitextendbackendutilstasktemplate) | |
| [`flytekit.extras.accelerators.BaseAccelerator`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsbaseaccelerator) |Base class for all accelerator types. |
| [`flytekit.extras.accelerators.GPUAccelerator`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsgpuaccelerator) |Class that represents a GPU accelerator. |
| [`flytekit.extras.accelerators.Generic`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsgeneric) |Abstract base class for generic types. |
| [`flytekit.extras.accelerators.MultiInstanceGPUAccelerator`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorsmultiinstancegpuaccelerator) |Base class for all multi-instance GPU accelerator types. |
| [`flytekit.extras.accelerators.TypeVar`](../packages/flytekit.extras.accelerators#flytekitextrasacceleratorstypevar) |Type variable. |
| [`flytekit.extras.cloud_pickle_resolver.ExperimentalNaiveCloudPickleResolver`](../packages/flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolverexperimentalnaivecloudpickleresolver) |Please do not use this resolver, basically ever. |
| [`flytekit.extras.cloud_pickle_resolver.PythonAutoContainerTask`](../packages/flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolverpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.extras.cloud_pickle_resolver.SerializationSettings`](../packages/flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolverserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.extras.cloud_pickle_resolver.TaskResolverMixin`](../packages/flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolvertaskresolvermixin) |Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`flytekit.extras.cloud_pickle_resolver.TrackedInstance`](../packages/flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolvertrackedinstance) |Please see the notes for the metaclass above first. |
| [`flytekit.extras.pydantic_transformer.decorator.Any`](../packages/flytekit.extras.pydantic_transformer.decorator#flytekitextraspydantic_transformerdecoratorany) |Special type indicating an unconstrained type. |
| [`flytekit.extras.pydantic_transformer.decorator.TypeVar`](../packages/flytekit.extras.pydantic_transformer.decorator#flytekitextraspydantic_transformerdecoratortypevar) |Type variable. |
| [`flytekit.extras.pydantic_transformer.transformer.BaseModel`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerbasemodel) |Usage docs: https://docs. |
| [`flytekit.extras.pydantic_transformer.transformer.Binary`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerbinary) | |
| [`flytekit.extras.pydantic_transformer.transformer.FlyteContext`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.extras.pydantic_transformer.transformer.Literal`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerliteral) | |
| [`flytekit.extras.pydantic_transformer.transformer.LiteralType`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerliteraltype) | |
| [`flytekit.extras.pydantic_transformer.transformer.PydanticTransformer`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerpydantictransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pydantic_transformer.transformer.Scalar`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformerscalar) | |
| [`flytekit.extras.pydantic_transformer.transformer.TypeAnnotationModel`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypeannotationmodel) |Python class representation of the flyteidl TypeAnnotation message. |
| [`flytekit.extras.pydantic_transformer.transformer.TypeEngine`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.extras.pydantic_transformer.transformer.TypeStructure`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypestructure) |Models _types_pb2. |
| [`flytekit.extras.pydantic_transformer.transformer.TypeTransformer`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pydantic_transformer.transformer.TypeTransformerFailedError`](../packages/flytekit.extras.pydantic_transformer.transformer#flytekitextraspydantic_transformertransformertypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.extras.pytorch.PyTorchCheckpoint`](../packages/flytekit.extras.pytorch#flytekitextraspytorchpytorchcheckpoint) |This class is helpful to save a checkpoint. |
| [`flytekit.extras.pytorch.PyTorchCheckpointTransformer`](../packages/flytekit.extras.pytorch#flytekitextraspytorchpytorchcheckpointtransformer) |TypeTransformer that supports serializing and deserializing checkpoint. |
| [`flytekit.extras.pytorch.PyTorchModuleTransformer`](../packages/flytekit.extras.pytorch#flytekitextraspytorchpytorchmoduletransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.PyTorchTensorTransformer`](../packages/flytekit.extras.pytorch#flytekitextraspytorchpytorchtensortransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.checkpoint.Any`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointany) |Special type indicating an unconstrained type. |
| [`flytekit.extras.pytorch.checkpoint.Blob`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointblob) | |
| [`flytekit.extras.pytorch.checkpoint.BlobMetadata`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.extras.pytorch.checkpoint.DataClassJsonMixin`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointdataclassjsonmixin) |DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`flytekit.extras.pytorch.checkpoint.FlyteContext`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.extras.pytorch.checkpoint.IsDataclass`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointisdataclass) |Base class for protocol classes. |
| [`flytekit.extras.pytorch.checkpoint.Literal`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointliteral) | |
| [`flytekit.extras.pytorch.checkpoint.LiteralType`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointliteraltype) | |
| [`flytekit.extras.pytorch.checkpoint.Protocol`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointprotocol) |Base class for protocol classes. |
| [`flytekit.extras.pytorch.checkpoint.PyTorchCheckpoint`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointpytorchcheckpoint) |This class is helpful to save a checkpoint. |
| [`flytekit.extras.pytorch.checkpoint.PyTorchCheckpointTransformer`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointpytorchcheckpointtransformer) |TypeTransformer that supports serializing and deserializing checkpoint. |
| [`flytekit.extras.pytorch.checkpoint.Scalar`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointscalar) | |
| [`flytekit.extras.pytorch.checkpoint.TypeEngine`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointtypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.extras.pytorch.checkpoint.TypeTransformer`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointtypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.checkpoint.TypeTransformerFailedError`](../packages/flytekit.extras.pytorch.checkpoint#flytekitextraspytorchcheckpointtypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.extras.pytorch.native.Blob`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativeblob) | |
| [`flytekit.extras.pytorch.native.BlobMetadata`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativeblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.extras.pytorch.native.FlyteContext`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativeflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.extras.pytorch.native.Literal`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativeliteral) | |
| [`flytekit.extras.pytorch.native.LiteralType`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativeliteraltype) | |
| [`flytekit.extras.pytorch.native.PyTorchModuleTransformer`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativepytorchmoduletransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.native.PyTorchTensorTransformer`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativepytorchtensortransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.native.PyTorchTypeTransformer`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativepytorchtypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.native.Scalar`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativescalar) | |
| [`flytekit.extras.pytorch.native.TypeEngine`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.extras.pytorch.native.TypeTransformer`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativetypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.extras.pytorch.native.TypeTransformerFailedError`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativetypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.extras.pytorch.native.TypeVar`](../packages/flytekit.extras.pytorch.native#flytekitextraspytorchnativetypevar) |Type variable. |
| [`flytekit.extras.sqlite3.task.DefaultImages`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3taskdefaultimages) |We may want to load the default images from remote - maybe s3 location etc?. |
| [`flytekit.extras.sqlite3.task.FlyteContext`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3taskflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.extras.sqlite3.task.PythonCustomizedContainerTask`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3taskpythoncustomizedcontainertask) |Please take a look at the comments for :py:class`flytekit. |
| [`flytekit.extras.sqlite3.task.SQLTask`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqltask) |Base task types for all SQL tasks. |
| [`flytekit.extras.sqlite3.task.SQLite3Config`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3config) |Use this configuration to configure if sqlite3 files that should be loaded by the task. |
| [`flytekit.extras.sqlite3.task.SQLite3Task`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3task) |Run client side SQLite3 queries that optionally return a FlyteSchema object. |
| [`flytekit.extras.sqlite3.task.SQLite3TaskExecutor`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3taskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.extras.sqlite3.task.SerializationSettings`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3taskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.extras.sqlite3.task.ShimTaskExecutor`](../packages/flytekit.extras.sqlite3.task#flytekitextrassqlite3taskshimtaskexecutor) |Please see the notes for the metaclass above first. |
| [`flytekit.extras.tasks.shell.AttrDict`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellattrdict) |Convert a dictionary to an attribute style lookup. |
| [`flytekit.extras.tasks.shell.ExecutionParameters`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellexecutionparameters) |This is a run-time user-centric context object that is accessible to every @task method. |
| [`flytekit.extras.tasks.shell.FlyteDirectory`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellflytedirectory) | |
| [`flytekit.extras.tasks.shell.FlyteFile`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellflytefile) | |
| [`flytekit.extras.tasks.shell.FlyteRecoverableException`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellflyterecoverableexception) |Common base class for all non-exit exceptions. |
| [`flytekit.extras.tasks.shell.Interface`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellinterface) |A Python native interface object, like inspect. |
| [`flytekit.extras.tasks.shell.OutputLocation`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshelloutputlocation) |. |
| [`flytekit.extras.tasks.shell.ProcessResult`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellprocessresult) |Stores a process return code, standard output and standard error. |
| [`flytekit.extras.tasks.shell.PythonInstanceTask`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellpythoninstancetask) |This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`flytekit.extras.tasks.shell.RawShellTask`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellrawshelltask) | |
| [`flytekit.extras.tasks.shell.ShellTask`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshellshelltask) | |
| [`flytekit.extras.tasks.shell.TaskPlugins`](../packages/flytekit.extras.tasks.shell#flytekitextrastasksshelltaskplugins) |This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |
| [`flytekit.extras.webhook.WebhookConnector`](../packages/flytekit.extras.webhook#flytekitextraswebhookwebhookconnector) |WebhookConnector is responsible for handling webhook tasks. |
| [`flytekit.extras.webhook.WebhookTask`](../packages/flytekit.extras.webhook#flytekitextraswebhookwebhooktask) |The WebhookTask is used to invoke a webhook. |
| [`flytekit.extras.webhook.connector.ConnectorRegistry`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectorconnectorregistry) |This is the registry for all connectors. |
| [`flytekit.extras.webhook.connector.LiteralMap`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectorliteralmap) | |
| [`flytekit.extras.webhook.connector.Resource`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectorresource) |This is the output resource of the job. |
| [`flytekit.extras.webhook.connector.SyncConnectorBase`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectorsyncconnectorbase) |This is the base class for all sync connectors. |
| [`flytekit.extras.webhook.connector.TaskExecution`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectortaskexecution) |A ProtocolMessage. |
| [`flytekit.extras.webhook.connector.TaskTemplate`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectortasktemplate) | |
| [`flytekit.extras.webhook.connector.WebhookConnector`](../packages/flytekit.extras.webhook.connector#flytekitextraswebhookconnectorwebhookconnector) |WebhookConnector is responsible for handling webhook tasks. |
| [`flytekit.extras.webhook.task.Any`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktaskany) |Special type indicating an unconstrained type. |
| [`flytekit.extras.webhook.task.Documentation`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktaskdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.extras.webhook.task.Interface`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktaskinterface) |A Python native interface object, like inspect. |
| [`flytekit.extras.webhook.task.PythonTask`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktaskpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.extras.webhook.task.SerializationSettings`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktaskserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.extras.webhook.task.SyncConnectorExecutorMixin`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktasksyncconnectorexecutormixin) |This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`flytekit.extras.webhook.task.WebhookTask`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktaskwebhooktask) |The WebhookTask is used to invoke a webhook. |
| [`flytekit.extras.webhook.task.timedelta`](../packages/flytekit.extras.webhook.task#flytekitextraswebhooktasktimedelta) |Difference between two datetime values. |
| [`flytekit.image_spec.DefaultImageBuilder`](../packages/flytekit.image_spec#flytekitimage_specdefaultimagebuilder) |Image builder using Docker and buildkit. |
| [`flytekit.image_spec.ImageBuildEngine`](../packages/flytekit.image_spec#flytekitimage_specimagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.image_spec.ImageSpec`](../packages/flytekit.image_spec#flytekitimage_specimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.image_spec.default_builder.CopyFileDetection`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_buildercopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.image_spec.default_builder.DefaultImageBuilder`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdefaultimagebuilder) |Image builder using Docker and buildkit. |
| [`flytekit.image_spec.default_builder.DockerIgnore`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdockerignore) |Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`flytekit.image_spec.default_builder.GitIgnore`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_buildergitignore) |Uses git cli (if available) to list all ignored files and compare with those. |
| [`flytekit.image_spec.default_builder.IgnoreGroup`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderignoregroup) |Groups multiple Ignores and checks a path against them. |
| [`flytekit.image_spec.default_builder.ImageSpec`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.image_spec.default_builder.ImageSpecBuilder`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderimagespecbuilder) | |
| [`flytekit.image_spec.default_builder.Path`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderpath) |PurePath subclass that can make system calls. |
| [`flytekit.image_spec.default_builder.StandardIgnore`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_builderstandardignore) |Retains the standard ignore functionality that previously existed. |
| [`flytekit.image_spec.default_builder.Template`](../packages/flytekit.image_spec.default_builder#flytekitimage_specdefault_buildertemplate) |A string class for supporting $-substitutions. |
| [`flytekit.image_spec.image_spec.CopyFileDetection`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_speccopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.image_spec.image_spec.FlyteAssertion`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specflyteassertion) |Assertion failed. |
| [`flytekit.image_spec.image_spec.ImageBuildEngine`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specimagebuildengine) |ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`flytekit.image_spec.image_spec.ImageSpec`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.image_spec.image_spec.ImageSpecBuilder`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespecbuilder) | |
| [`flytekit.image_spec.image_spec.Version`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_specversion) |This class abstracts handling of a project's versions. |
| [`flytekit.image_spec.image_spec.cached_property`](../packages/flytekit.image_spec.image_spec#flytekitimage_specimage_speccached_property) | |
| [`flytekit.interaction.click_types.ArtifactQuery`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesartifactquery) | |
| [`flytekit.interaction.click_types.BlobType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesblobtype) |This type represents offloaded data and is typically used for things like files. |
| [`flytekit.interaction.click_types.DataClassJsonMixin`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdataclassjsonmixin) |DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`flytekit.interaction.click_types.DateTimeType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdatetimetype) |The DateTime type converts date strings into `datetime` objects. |
| [`flytekit.interaction.click_types.DirParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdirparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.DurationParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesdurationparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.EnumParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesenumparamtype) |The choice type allows a value to be checked against a fixed set. |
| [`flytekit.interaction.click_types.FileAccessProvider`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesfileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.interaction.click_types.FileParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesfileparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.FlyteContext`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.interaction.click_types.FlyteDirectory`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflytedirectory) | |
| [`flytekit.interaction.click_types.FlyteFile`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflytefile) | |
| [`flytekit.interaction.click_types.FlyteLiteralConverter`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflyteliteralconverter) | |
| [`flytekit.interaction.click_types.FlytePathResolver`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflytepathresolver) | |
| [`flytekit.interaction.click_types.FlytePickleTransformer`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflytepickletransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.interaction.click_types.FlyteSchema`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesflyteschema) | |
| [`flytekit.interaction.click_types.JSONIteratorParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratorparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.JSONIteratorTransformer`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesjsoniteratortransformer) |A JSON iterator that handles conversion between an iterator/generator and a JSONL file. |
| [`flytekit.interaction.click_types.JsonParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesjsonparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.Literal`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesliteral) | |
| [`flytekit.interaction.click_types.LiteralType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesliteraltype) | |
| [`flytekit.interaction.click_types.PickleParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typespickleparamtype) |Represents the type of a parameter. |
| [`flytekit.interaction.click_types.SimpleType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typessimpletype) | |
| [`flytekit.interaction.click_types.StructuredDataset`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.interaction.click_types.StructuredDatasetParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesstructureddatasetparamtype) |TODO handle column types. |
| [`flytekit.interaction.click_types.TypeEngine`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typestypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.interaction.click_types.UnionParamType`](../packages/flytekit.interaction.click_types#flytekitinteractionclick_typesunionparamtype) |A composite type that allows for multiple types to be specified. |
| [`flytekit.interaction.parse_stdin.FlyteContext`](../packages/flytekit.interaction.parse_stdin#flytekitinteractionparse_stdinflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.interaction.parse_stdin.Literal`](../packages/flytekit.interaction.parse_stdin#flytekitinteractionparse_stdinliteral) | |
| [`flytekit.interaction.parse_stdin.LiteralType`](../packages/flytekit.interaction.parse_stdin#flytekitinteractionparse_stdinliteraltype) | |
| [`flytekit.interaction.parse_stdin.TypeEngine`](../packages/flytekit.interaction.parse_stdin#flytekitinteractionparse_stdintypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.interaction.rich_utils.Callback`](../packages/flytekit.interaction.rich_utils#flytekitinteractionrich_utilscallback) |Base class and interface for callback mechanism. |
| [`flytekit.interaction.rich_utils.Progress`](../packages/flytekit.interaction.rich_utils#flytekitinteractionrich_utilsprogress) |Renders an auto-updating progress bar(s). |
| [`flytekit.interaction.rich_utils.RichCallback`](../packages/flytekit.interaction.rich_utils#flytekitinteractionrich_utilsrichcallback) |Base class and interface for callback mechanism. |
| [`flytekit.interaction.string_literals.Literal`](../packages/flytekit.interaction.string_literals#flytekitinteractionstring_literalsliteral) | |
| [`flytekit.interaction.string_literals.LiteralMap`](../packages/flytekit.interaction.string_literals#flytekitinteractionstring_literalsliteralmap) | |
| [`flytekit.interaction.string_literals.Primitive`](../packages/flytekit.interaction.string_literals#flytekitinteractionstring_literalsprimitive) | |
| [`flytekit.interaction.string_literals.Scalar`](../packages/flytekit.interaction.string_literals#flytekitinteractionstring_literalsscalar) | |
| [`flytekit.interactive.VscodeConfig`](../packages/flytekit.interactive#flytekitinteractivevscodeconfig) |VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`flytekit.interactive.vscode`](../packages/flytekit.interactive#flytekitinteractivevscode) |Abstract class for class decorators. |
| [`flytekit.interactive.utils.FlyteContextManager`](../packages/flytekit.interactive.utils#flytekitinteractiveutilsflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.interactive.utils.TypeEngine`](../packages/flytekit.interactive.utils#flytekitinteractiveutilstypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.interactive.vscode_lib.config.VscodeConfig`](../packages/flytekit.interactive.vscode_lib.config#flytekitinteractivevscode_libconfigvscodeconfig) |VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`flytekit.interactive.vscode_lib.decorator.ClassDecorator`](../packages/flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorclassdecorator) |Abstract class for class decorators. |
| [`flytekit.interactive.vscode_lib.decorator.FlyteContextManager`](../packages/flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.interactive.vscode_lib.decorator.VscodeConfig`](../packages/flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscodeconfig) |VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`flytekit.interactive.vscode_lib.decorator.vscode`](../packages/flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscode) |Abstract class for class decorators. |
| [`flytekit.interactive.vscode_lib.vscode_constants.Path`](../packages/flytekit.interactive.vscode_lib.vscode_constants#flytekitinteractivevscode_libvscode_constantspath) |PurePath subclass that can make system calls. |
| [`flytekit.interfaces.cli_identifiers.Identifier`](../packages/flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersidentifier) | |
| [`flytekit.interfaces.cli_identifiers.TaskExecutionIdentifier`](../packages/flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifierstaskexecutionidentifier) | |
| [`flytekit.interfaces.cli_identifiers.WorkflowExecutionIdentifier`](../packages/flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersworkflowexecutionidentifier) | |
| [`flytekit.interfaces.stats.client.DummyStatsClient`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientdummystatsclient) |A dummy client for statsd. |
| [`flytekit.interfaces.stats.client.ScopeableStatsProxy`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientscopeablestatsproxy) |A Proxy object for an underlying statsd client. |
| [`flytekit.interfaces.stats.client.StatsClientProxy`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsclientproxy) |A Proxy object for an underlying statsd client. |
| [`flytekit.interfaces.stats.client.StatsConfig`](../packages/flytekit.interfaces.stats.client#flytekitinterfacesstatsclientstatsconfig) |Configuration for sending statsd. |
| [`flytekit.interfaces.stats.taggable.StatsConfig`](../packages/flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggablestatsconfig) |Configuration for sending statsd. |
| [`flytekit.interfaces.stats.taggable.TaggableStats`](../packages/flytekit.interfaces.stats.taggable#flytekitinterfacesstatstaggabletaggablestats) |A Proxy object for an underlying statsd client. |
| [`flytekit.models.admin.common.Sort`](../packages/flytekit.models.admin.common#flytekitmodelsadmincommonsort) | |
| [`flytekit.models.admin.task_execution.TaskExecution`](../packages/flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecution) | |
| [`flytekit.models.admin.task_execution.TaskExecutionClosure`](../packages/flytekit.models.admin.task_execution#flytekitmodelsadmintask_executiontaskexecutionclosure) | |
| [`flytekit.models.admin.workflow.Documentation`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`flytekit.models.admin.workflow.Workflow`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflow) | |
| [`flytekit.models.admin.workflow.WorkflowClosure`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowclosure) | |
| [`flytekit.models.admin.workflow.WorkflowSpec`](../packages/flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowspec) | |
| [`flytekit.models.annotation.Any`](../packages/flytekit.models.annotation#flytekitmodelsannotationany) |Special type indicating an unconstrained type. |
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
| [`flytekit.models.common.StringIO`](../packages/flytekit.models.common#flytekitmodelscommonstringio) |Text I/O implementation using an in-memory buffer. |
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
| [`flytekit.models.core.errors.Timestamp`](../packages/flytekit.models.core.errors#flytekitmodelscoreerrorstimestamp) |A ProtocolMessage. |
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
| [`flytekit.models.core.workflow.BoolValue`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowboolvalue) |A ProtocolMessage. |
| [`flytekit.models.core.workflow.BranchNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowbranchnode) | |
| [`flytekit.models.core.workflow.GateNode`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowgatenode) | |
| [`flytekit.models.core.workflow.IfBlock`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowifblock) | |
| [`flytekit.models.core.workflow.IfElseBlock`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowifelseblock) | |
| [`flytekit.models.core.workflow.K8sObjectMetadata`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowk8sobjectmetadata) | |
| [`flytekit.models.core.workflow.Node`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflownode) | |
| [`flytekit.models.core.workflow.NodeMetadata`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflownodemetadata) | |
| [`flytekit.models.core.workflow.PodTemplate`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowpodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.models.core.workflow.Resources`](../packages/flytekit.models.core.workflow#flytekitmodelscoreworkflowresources) | |
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
| [`flytekit.models.documentation.Enum`](../packages/flytekit.models.documentation#flytekitmodelsdocumentationenum) |Create a collection of name/value pairs. |
| [`flytekit.models.documentation.SourceCode`](../packages/flytekit.models.documentation#flytekitmodelsdocumentationsourcecode) |Link to source code used to define this task or workflow. |
| [`flytekit.models.domain.Domain`](../packages/flytekit.models.domain#flytekitmodelsdomaindomain) |Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |
| [`flytekit.models.dynamic_job.DynamicJobSpec`](../packages/flytekit.models.dynamic_job#flytekitmodelsdynamic_jobdynamicjobspec) | |
| [`flytekit.models.event.TaskExecutionMetadata`](../packages/flytekit.models.event#flytekitmodelseventtaskexecutionmetadata) |. |
| [`flytekit.models.execution.AbortMetadata`](../packages/flytekit.models.execution#flytekitmodelsexecutionabortmetadata) | |
| [`flytekit.models.execution.BoolValue`](../packages/flytekit.models.execution#flytekitmodelsexecutionboolvalue) |A ProtocolMessage. |
| [`flytekit.models.execution.ClusterAssignment`](../packages/flytekit.models.execution#flytekitmodelsexecutionclusterassignment) | |
| [`flytekit.models.execution.DynamicWorkflowNodeMetadata`](../packages/flytekit.models.execution#flytekitmodelsexecutiondynamicworkflownodemetadata) | |
| [`flytekit.models.execution.Execution`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecution) | |
| [`flytekit.models.execution.ExecutionClosure`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecutionclosure) | |
| [`flytekit.models.execution.ExecutionClusterLabel`](../packages/flytekit.models.execution#flytekitmodelsexecutionexecutionclusterlabel) | |
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
| [`flytekit.models.launch_plan.Any`](../packages/flytekit.models.launch_plan#flytekitmodelslaunch_planany) |A ProtocolMessage. |
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
| [`flytekit.models.literals.Error`](../packages/flytekit.models.literals#flytekitmodelsliteralserror) | |
| [`flytekit.models.literals.Literal`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteral) | |
| [`flytekit.models.literals.LiteralCollection`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteralcollection) | |
| [`flytekit.models.literals.LiteralMap`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteralmap) | |
| [`flytekit.models.literals.LiteralOffloadedMetadata`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteraloffloadedmetadata) | |
| [`flytekit.models.literals.LiteralType`](../packages/flytekit.models.literals#flytekitmodelsliteralsliteraltype) | |
| [`flytekit.models.literals.Primitive`](../packages/flytekit.models.literals#flytekitmodelsliteralsprimitive) | |
| [`flytekit.models.literals.RetryStrategy`](../packages/flytekit.models.literals#flytekitmodelsliteralsretrystrategy) | |
| [`flytekit.models.literals.Scalar`](../packages/flytekit.models.literals#flytekitmodelsliteralsscalar) | |
| [`flytekit.models.literals.Schema`](../packages/flytekit.models.literals#flytekitmodelsliteralsschema) | |
| [`flytekit.models.literals.Struct`](../packages/flytekit.models.literals#flytekitmodelsliteralsstruct) |A ProtocolMessage. |
| [`flytekit.models.literals.StructuredDataset`](../packages/flytekit.models.literals#flytekitmodelsliteralsstructureddataset) | |
| [`flytekit.models.literals.StructuredDatasetMetadata`](../packages/flytekit.models.literals#flytekitmodelsliteralsstructureddatasetmetadata) | |
| [`flytekit.models.literals.StructuredDatasetType`](../packages/flytekit.models.literals#flytekitmodelsliteralsstructureddatasettype) | |
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
| [`flytekit.models.security.Enum`](../packages/flytekit.models.security#flytekitmodelssecurityenum) |Create a collection of name/value pairs. |
| [`flytekit.models.security.Identity`](../packages/flytekit.models.security#flytekitmodelssecurityidentity) | |
| [`flytekit.models.security.OAuth2Client`](../packages/flytekit.models.security#flytekitmodelssecurityoauth2client) | |
| [`flytekit.models.security.OAuth2TokenRequest`](../packages/flytekit.models.security#flytekitmodelssecurityoauth2tokenrequest) | |
| [`flytekit.models.security.Secret`](../packages/flytekit.models.security#flytekitmodelssecuritysecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`flytekit.models.security.SecurityContext`](../packages/flytekit.models.security#flytekitmodelssecuritysecuritycontext) |This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`flytekit.models.task.BoolValue`](../packages/flytekit.models.task#flytekitmodelstaskboolvalue) |A ProtocolMessage. |
| [`flytekit.models.task.CompiledTask`](../packages/flytekit.models.task#flytekitmodelstaskcompiledtask) | |
| [`flytekit.models.task.Container`](../packages/flytekit.models.task#flytekitmodelstaskcontainer) | |
| [`flytekit.models.task.DataLoadingConfig`](../packages/flytekit.models.task#flytekitmodelstaskdataloadingconfig) | |
| [`flytekit.models.task.Documentation`](../packages/flytekit.models.task#flytekitmodelstaskdocumentation) |DescriptionEntity contains detailed description for the task/workflow/launch plan. |
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
| [`flytekit.models.types.TypeAnnotationModel`](../packages/flytekit.models.types#flytekitmodelstypestypeannotationmodel) |Python class representation of the flyteidl TypeAnnotation message. |
| [`flytekit.models.types.TypeStructure`](../packages/flytekit.models.types#flytekitmodelstypestypestructure) |Models _types_pb2. |
| [`flytekit.models.types.UnionType`](../packages/flytekit.models.types#flytekitmodelstypesuniontype) |Models _types_pb2. |
| [`flytekit.models.workflow_closure.WorkflowClosure`](../packages/flytekit.models.workflow_closure#flytekitmodelsworkflow_closureworkflowclosure) | |
| [`flytekit.remote.FlyteBranchNode`](../packages/flytekit.remote#flytekitremoteflytebranchnode) | |
| [`flytekit.remote.FlyteLaunchPlan`](../packages/flytekit.remote#flytekitremoteflytelaunchplan) |A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.FlyteNode`](../packages/flytekit.remote#flytekitremoteflytenode) |A class encapsulating a remote Flyte node. |
| [`flytekit.remote.FlyteNodeExecution`](../packages/flytekit.remote#flytekitremoteflytenodeexecution) |A class encapsulating a node execution being run on a Flyte remote backend. |
| [`flytekit.remote.FlyteRemote`](../packages/flytekit.remote#flytekitremoteflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.remote.FlyteTask`](../packages/flytekit.remote#flytekitremoteflytetask) |A class encapsulating a remote Flyte task. |
| [`flytekit.remote.FlyteTaskExecution`](../packages/flytekit.remote#flytekitremoteflytetaskexecution) |A class encapsulating a task execution being run on a Flyte remote backend. |
| [`flytekit.remote.FlyteTaskNode`](../packages/flytekit.remote#flytekitremoteflytetasknode) |A class encapsulating a task that a Flyte node needs to execute. |
| [`flytekit.remote.FlyteWorkflow`](../packages/flytekit.remote#flytekitremoteflyteworkflow) |A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.FlyteWorkflowExecution`](../packages/flytekit.remote#flytekitremoteflyteworkflowexecution) |A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`flytekit.remote.FlyteWorkflowNode`](../packages/flytekit.remote#flytekitremoteflyteworkflownode) |A class encapsulating a workflow that a Flyte node needs to execute. |
| [`flytekit.remote.backfill.FlyteLaunchPlan`](../packages/flytekit.remote.backfill#flytekitremotebackfillflytelaunchplan) |A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.backfill.ImperativeWorkflow`](../packages/flytekit.remote.backfill#flytekitremotebackfillimperativeworkflow) |An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`flytekit.remote.backfill.LaunchPlan`](../packages/flytekit.remote.backfill#flytekitremotebackfilllaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.remote.backfill.WorkflowBase`](../packages/flytekit.remote.backfill#flytekitremotebackfillworkflowbase) | |
| [`flytekit.remote.backfill.WorkflowFailurePolicy`](../packages/flytekit.remote.backfill#flytekitremotebackfillworkflowfailurepolicy) |Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.remote.backfill.croniter`](../packages/flytekit.remote.backfill#flytekitremotebackfillcroniter) | |
| [`flytekit.remote.backfill.datetime`](../packages/flytekit.remote.backfill#flytekitremotebackfilldatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.remote.backfill.timedelta`](../packages/flytekit.remote.backfill#flytekitremotebackfilltimedelta) |Difference between two datetime values. |
| [`flytekit.remote.data.BlobType`](../packages/flytekit.remote.data#flytekitremotedatablobtype) |This type represents offloaded data and is typically used for things like files. |
| [`flytekit.remote.data.FileAccessProvider`](../packages/flytekit.remote.data#flytekitremotedatafileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.remote.data.Literal`](../packages/flytekit.remote.data#flytekitremotedataliteral) | |
| [`flytekit.remote.data.RichCallback`](../packages/flytekit.remote.data#flytekitremotedatarichcallback) |Base class and interface for callback mechanism. |
| [`flytekit.remote.entities.Binding`](../packages/flytekit.remote.entities#flytekitremoteentitiesbinding) | |
| [`flytekit.remote.entities.FlyteArrayNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytearraynode) | |
| [`flytekit.remote.entities.FlyteBranchNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytebranchnode) | |
| [`flytekit.remote.entities.FlyteContext`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.remote.entities.FlyteGateNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytegatenode) | |
| [`flytekit.remote.entities.FlyteLaunchPlan`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytelaunchplan) |A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.entities.FlyteNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytenode) |A class encapsulating a remote Flyte node. |
| [`flytekit.remote.entities.FlyteTask`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytetask) |A class encapsulating a remote Flyte task. |
| [`flytekit.remote.entities.FlyteTaskNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflytetasknode) |A class encapsulating a task that a Flyte node needs to execute. |
| [`flytekit.remote.entities.FlyteWorkflow`](../packages/flytekit.remote.entities#flytekitremoteentitiesflyteworkflow) |A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.entities.FlyteWorkflowNode`](../packages/flytekit.remote.entities#flytekitremoteentitiesflyteworkflownode) |A class encapsulating a workflow that a Flyte node needs to execute. |
| [`flytekit.remote.entities.Identifier`](../packages/flytekit.remote.entities#flytekitremoteentitiesidentifier) | |
| [`flytekit.remote.entities.Node`](../packages/flytekit.remote.entities#flytekitremoteentitiesnode) | |
| [`flytekit.remote.entities.RemoteEntity`](../packages/flytekit.remote.entities#flytekitremoteentitiesremoteentity) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.remote.entities.TaskSpec`](../packages/flytekit.remote.entities#flytekitremoteentitiestaskspec) | |
| [`flytekit.remote.entities.TypedInterface`](../packages/flytekit.remote.entities#flytekitremoteentitiestypedinterface) | |
| [`flytekit.remote.entities.WorkflowMetadata`](../packages/flytekit.remote.entities#flytekitremoteentitiesworkflowmetadata) | |
| [`flytekit.remote.entities.WorkflowMetadataDefaults`](../packages/flytekit.remote.entities#flytekitremoteentitiesworkflowmetadatadefaults) | |
| [`flytekit.remote.entities.WorkflowSpec`](../packages/flytekit.remote.entities#flytekitremoteentitiesworkflowspec) | |
| [`flytekit.remote.executions.FlyteNodeExecution`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflytenodeexecution) |A class encapsulating a node execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteTask`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflytetask) |A class encapsulating a remote Flyte task. |
| [`flytekit.remote.executions.FlyteTaskExecution`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflytetaskexecution) |A class encapsulating a task execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.FlyteWorkflow`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflyteworkflow) |A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.executions.FlyteWorkflowExecution`](../packages/flytekit.remote.executions#flytekitremoteexecutionsflyteworkflowexecution) |A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`flytekit.remote.executions.LiteralsResolver`](../packages/flytekit.remote.executions#flytekitremoteexecutionsliteralsresolver) |LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.remote.executions.RemoteExecutionBase`](../packages/flytekit.remote.executions#flytekitremoteexecutionsremoteexecutionbase) | |
| [`flytekit.remote.executions.TypedInterface`](../packages/flytekit.remote.executions#flytekitremoteexecutionstypedinterface) | |
| [`flytekit.remote.executions.timedelta`](../packages/flytekit.remote.executions#flytekitremoteexecutionstimedelta) |Difference between two datetime values. |
| [`flytekit.remote.interface.TypedInterface`](../packages/flytekit.remote.interface#flytekitremoteinterfacetypedinterface) | |
| [`flytekit.remote.lazy_entity.FlyteContext`](../packages/flytekit.remote.lazy_entity#flytekitremotelazy_entityflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.remote.lazy_entity.Identifier`](../packages/flytekit.remote.lazy_entity#flytekitremotelazy_entityidentifier) | |
| [`flytekit.remote.lazy_entity.LazyEntity`](../packages/flytekit.remote.lazy_entity#flytekitremotelazy_entitylazyentity) |Fetches the entity when the entity is called or when the entity is retrieved. |
| [`flytekit.remote.lazy_entity.Lock`](../packages/flytekit.remote.lazy_entity#flytekitremotelazy_entitylock) |A lock object is a synchronization primitive. |
| [`flytekit.remote.lazy_entity.RemoteEntity`](../packages/flytekit.remote.lazy_entity#flytekitremotelazy_entityremoteentity) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.remote.metrics.FlyteExecutionSpan`](../packages/flytekit.remote.metrics#flytekitremotemetricsflyteexecutionspan) | |
| [`flytekit.remote.metrics.datetime`](../packages/flytekit.remote.metrics#flytekitremotemetricsdatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.remote.remote.ArrayNodeMapTask`](../packages/flytekit.remote.remote#flytekitremoteremotearraynodemaptask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.remote.remote.Artifact`](../packages/flytekit.remote.remote#flytekitremoteremoteartifact) |An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`flytekit.remote.remote.BranchNode`](../packages/flytekit.remote.remote#flytekitremoteremotebranchnode) | |
| [`flytekit.remote.remote.ClusterAssignment`](../packages/flytekit.remote.remote#flytekitremoteremoteclusterassignment) | |
| [`flytekit.remote.remote.Config`](../packages/flytekit.remote.remote#flytekitremoteremoteconfig) |This the parent configuration object and holds all the underlying configuration object types. |
| [`flytekit.remote.remote.ConfigFile`](../packages/flytekit.remote.remote#flytekitremoteremoteconfigfile) | |
| [`flytekit.remote.remote.CopyFileDetection`](../packages/flytekit.remote.remote#flytekitremoteremotecopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.remote.remote.CoreNode`](../packages/flytekit.remote.remote#flytekitremoteremotecorenode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.remote.remote.DataConfig`](../packages/flytekit.remote.remote#flytekitremoteremotedataconfig) |Any data storage specific configuration. |
| [`flytekit.remote.remote.Domain`](../packages/flytekit.remote.remote#flytekitremoteremotedomain) |Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |
| [`flytekit.remote.remote.ExecutionClusterLabel`](../packages/flytekit.remote.remote#flytekitremoteremoteexecutionclusterlabel) | |
| [`flytekit.remote.remote.ExecutionMetadata`](../packages/flytekit.remote.remote#flytekitremoteremoteexecutionmetadata) | |
| [`flytekit.remote.remote.ExecutionSpec`](../packages/flytekit.remote.remote#flytekitremoteremoteexecutionspec) | |
| [`flytekit.remote.remote.FastPackageOptions`](../packages/flytekit.remote.remote#flytekitremoteremotefastpackageoptions) |FastPackageOptions is used to set configuration options when packaging files. |
| [`flytekit.remote.remote.FastSerializationSettings`](../packages/flytekit.remote.remote#flytekitremoteremotefastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.remote.remote.FileAccessProvider`](../packages/flytekit.remote.remote#flytekitremoteremotefileaccessprovider) |This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`flytekit.remote.remote.FlyteAssertion`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteassertion) |Assertion failed. |
| [`flytekit.remote.remote.FlyteContext`](../packages/flytekit.remote.remote#flytekitremoteremoteflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.remote.remote.FlyteContextManager`](../packages/flytekit.remote.remote#flytekitremoteremoteflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.remote.remote.FlyteEntityAlreadyExistsException`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteentityalreadyexistsexception) |Assertion failed. |
| [`flytekit.remote.remote.FlyteEntityNotExistException`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteentitynotexistexception) |Assertion failed. |
| [`flytekit.remote.remote.FlyteExecutionSpan`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteexecutionspan) | |
| [`flytekit.remote.remote.FlyteLaunchPlan`](../packages/flytekit.remote.remote#flytekitremoteremoteflytelaunchplan) |A class encapsulating a remote Flyte launch plan. |
| [`flytekit.remote.remote.FlyteNode`](../packages/flytekit.remote.remote#flytekitremoteremoteflytenode) |A class encapsulating a remote Flyte node. |
| [`flytekit.remote.remote.FlyteNodeExecution`](../packages/flytekit.remote.remote#flytekitremoteremoteflytenodeexecution) |A class encapsulating a node execution being run on a Flyte remote backend. |
| [`flytekit.remote.remote.FlyteRemote`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.remote.remote.FlyteTask`](../packages/flytekit.remote.remote#flytekitremoteremoteflytetask) |A class encapsulating a remote Flyte task. |
| [`flytekit.remote.remote.FlyteTaskExecution`](../packages/flytekit.remote.remote#flytekitremoteremoteflytetaskexecution) |A class encapsulating a task execution being run on a Flyte remote backend. |
| [`flytekit.remote.remote.FlyteTaskNode`](../packages/flytekit.remote.remote#flytekitremoteremoteflytetasknode) |A class encapsulating a task that a Flyte node needs to execute. |
| [`flytekit.remote.remote.FlyteValueException`](../packages/flytekit.remote.remote#flytekitremoteremoteflytevalueexception) |Inappropriate argument value (of correct type). |
| [`flytekit.remote.remote.FlyteWorkflow`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteworkflow) |A class encapsulating a remote Flyte workflow. |
| [`flytekit.remote.remote.FlyteWorkflowExecution`](../packages/flytekit.remote.remote#flytekitremoteremoteflyteworkflowexecution) |A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`flytekit.remote.remote.Identifier`](../packages/flytekit.remote.remote#flytekitremoteremoteidentifier) | |
| [`flytekit.remote.remote.ImageConfig`](../packages/flytekit.remote.remote#flytekitremoteremoteimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.remote.remote.ImageSpec`](../packages/flytekit.remote.remote#flytekitremoteremoteimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.remote.remote.LaunchPlan`](../packages/flytekit.remote.remote#flytekitremoteremotelaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.remote.remote.LaunchPlanState`](../packages/flytekit.remote.remote#flytekitremoteremotelaunchplanstate) | |
| [`flytekit.remote.remote.LazyEntity`](../packages/flytekit.remote.remote#flytekitremoteremotelazyentity) |Fetches the entity when the entity is called or when the entity is retrieved. |
| [`flytekit.remote.remote.Literal`](../packages/flytekit.remote.remote#flytekitremoteremoteliteral) | |
| [`flytekit.remote.remote.LiteralMap`](../packages/flytekit.remote.remote#flytekitremoteremoteliteralmap) | |
| [`flytekit.remote.remote.LiteralsResolver`](../packages/flytekit.remote.remote#flytekitremoteremoteliteralsresolver) |LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`flytekit.remote.remote.NamedEntityIdentifier`](../packages/flytekit.remote.remote#flytekitremoteremotenamedentityidentifier) | |
| [`flytekit.remote.remote.Node`](../packages/flytekit.remote.remote#flytekitremoteremotenode) | |
| [`flytekit.remote.remote.NodeExecutionGetDataResponse`](../packages/flytekit.remote.remote#flytekitremoteremotenodeexecutiongetdataresponse) |Currently, node, task, and workflow execution all have the same get data response. |
| [`flytekit.remote.remote.NodeMetadata`](../packages/flytekit.remote.remote#flytekitremoteremotenodemetadata) | |
| [`flytekit.remote.remote.NotificationList`](../packages/flytekit.remote.remote#flytekitremoteremotenotificationlist) | |
| [`flytekit.remote.remote.Options`](../packages/flytekit.remote.remote#flytekitremoteremoteoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.remote.remote.OrderedDict`](../packages/flytekit.remote.remote#flytekitremoteremoteordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.remote.remote.PickledEntity`](../packages/flytekit.remote.remote#flytekitremoteremotepickledentity) |Represents the structure of the pickled object stored in the . |
| [`flytekit.remote.remote.PickledEntityMetadata`](../packages/flytekit.remote.remote#flytekitremoteremotepickledentitymetadata) |Metadata for a pickled entity containing version information. |
| [`flytekit.remote.remote.Progress`](../packages/flytekit.remote.remote#flytekitremoteremoteprogress) |Renders an auto-updating progress bar(s). |
| [`flytekit.remote.remote.Project`](../packages/flytekit.remote.remote#flytekitremoteremoteproject) | |
| [`flytekit.remote.remote.PythonAutoContainerTask`](../packages/flytekit.remote.remote#flytekitremoteremotepythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.remote.remote.PythonFunctionTask`](../packages/flytekit.remote.remote#flytekitremoteremotepythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.remote.remote.PythonFunctionWorkflow`](../packages/flytekit.remote.remote#flytekitremoteremotepythonfunctionworkflow) |Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`flytekit.remote.remote.PythonTask`](../packages/flytekit.remote.remote#flytekitremoteremotepythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.remote.remote.ReferenceEntity`](../packages/flytekit.remote.remote#flytekitremoteremotereferenceentity) | |
| [`flytekit.remote.remote.ReferenceLaunchPlan`](../packages/flytekit.remote.remote#flytekitremoteremotereferencelaunchplan) |A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.remote.remote.ReferenceSpec`](../packages/flytekit.remote.remote#flytekitremoteremotereferencespec) | |
| [`flytekit.remote.remote.ReferenceTask`](../packages/flytekit.remote.remote#flytekitremoteremotereferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.remote.remote.ReferenceWorkflow`](../packages/flytekit.remote.remote#flytekitremoteremotereferenceworkflow) |A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.remote.remote.RegistrationSkipped`](../packages/flytekit.remote.remote#flytekitremoteremoteregistrationskipped) |RegistrationSkipped error is raised when trying to register an entity that is not registrable. |
| [`flytekit.remote.remote.RemoteEntity`](../packages/flytekit.remote.remote#flytekitremoteremoteremoteentity) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.remote.remote.ResolvedIdentifiers`](../packages/flytekit.remote.remote#flytekitremoteremoteresolvedidentifiers) | |
| [`flytekit.remote.remote.ResourceType`](../packages/flytekit.remote.remote#flytekitremoteremoteresourcetype) | |
| [`flytekit.remote.remote.SerializationSettings`](../packages/flytekit.remote.remote#flytekitremoteremoteserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.remote.remote.Signal`](../packages/flytekit.remote.remote#flytekitremoteremotesignal) |A ProtocolMessage. |
| [`flytekit.remote.remote.SignalIdentifier`](../packages/flytekit.remote.remote#flytekitremoteremotesignalidentifier) | |
| [`flytekit.remote.remote.SignalListRequest`](../packages/flytekit.remote.remote#flytekitremoteremotesignallistrequest) |A ProtocolMessage. |
| [`flytekit.remote.remote.SignalSetRequest`](../packages/flytekit.remote.remote#flytekitremoteremotesignalsetrequest) |A ProtocolMessage. |
| [`flytekit.remote.remote.Sort`](../packages/flytekit.remote.remote#flytekitremoteremotesort) | |
| [`flytekit.remote.remote.SynchronousFlyteClient`](../packages/flytekit.remote.remote#flytekitremoteremotesynchronousflyteclient) |This is a low-level client that users can use to make direct gRPC service calls to the control plane. |
| [`flytekit.remote.remote.TextColumn`](../packages/flytekit.remote.remote#flytekitremoteremotetextcolumn) |A column containing text. |
| [`flytekit.remote.remote.TimeElapsedColumn`](../packages/flytekit.remote.remote#flytekitremoteremotetimeelapsedcolumn) |Renders time elapsed. |
| [`flytekit.remote.remote.TypeEngine`](../packages/flytekit.remote.remote#flytekitremoteremotetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.remote.remote.TypedInterface`](../packages/flytekit.remote.remote#flytekitremoteremotetypedinterface) | |
| [`flytekit.remote.remote.WorkflowBase`](../packages/flytekit.remote.remote#flytekitremoteremoteworkflowbase) | |
| [`flytekit.remote.remote.WorkflowExecutionGetDataResponse`](../packages/flytekit.remote.remote#flytekitremoteremoteworkflowexecutiongetdataresponse) |Currently, node, task, and workflow execution all have the same get data response. |
| [`flytekit.remote.remote.WorkflowExecutionIdentifier`](../packages/flytekit.remote.remote#flytekitremoteremoteworkflowexecutionidentifier) | |
| [`flytekit.remote.remote.WorkflowFailurePolicy`](../packages/flytekit.remote.remote#flytekitremoteremoteworkflowfailurepolicy) |Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`flytekit.remote.remote.datetime`](../packages/flytekit.remote.remote#flytekitremoteremotedatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.remote.remote.timedelta`](../packages/flytekit.remote.remote#flytekitremoteremotetimedelta) |Difference between two datetime values. |
| [`flytekit.remote.remote_callable.ABC`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.remote.remote_callable.Any`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableany) |Special type indicating an unconstrained type. |
| [`flytekit.remote.remote_callable.BranchEvalMode`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callablebranchevalmode) |This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`flytekit.remote.remote_callable.ExecutionState`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableexecutionstate) |This is the context that is active when executing a task or a local workflow. |
| [`flytekit.remote.remote_callable.FlyteContext`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.remote.remote_callable.Identifier`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableidentifier) | |
| [`flytekit.remote.remote_callable.NodeMetadata`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callablenodemetadata) | |
| [`flytekit.remote.remote_callable.Promise`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callablepromise) |This object is a wrapper and exists for three main reasons. |
| [`flytekit.remote.remote_callable.RemoteEntity`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callableremoteentity) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.remote.remote_callable.VoidPromise`](../packages/flytekit.remote.remote_callable#flytekitremoteremote_callablevoidpromise) |This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`flytekit.remote.remote_fs.FlytePathResolver`](../packages/flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) | |
| [`flytekit.remote.remote_fs.NoOpCallback`](../packages/flytekit.remote.remote_fs#flytekitremoteremote_fsnoopcallback) |This implementation of Callback does exactly nothing. |
| [`flytekit.remote.remote_fs.UUID`](../packages/flytekit.remote.remote_fs#flytekitremoteremote_fsuuid) |Instances of the UUID class represent UUIDs as specified in RFC 4122. |
| [`flytekit.sensor.BaseSensor`](../packages/flytekit.sensor#flytekitsensorbasesensor) |Base class for all sensors. |
| [`flytekit.sensor.FileSensor`](../packages/flytekit.sensor#flytekitsensorfilesensor) |Base class for all sensors. |
| [`flytekit.sensor.SensorEngine`](../packages/flytekit.sensor#flytekitsensorsensorengine) |This is the base class for all async connectors. |
| [`flytekit.sensor.base_sensor.Any`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorany) |Special type indicating an unconstrained type. |
| [`flytekit.sensor.base_sensor.AsyncConnectorExecutorMixin`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorasyncconnectorexecutormixin) |This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekit.sensor.base_sensor.BaseSensor`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorbasesensor) |Base class for all sensors. |
| [`flytekit.sensor.base_sensor.Interface`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorinterface) |A Python native interface object, like inspect. |
| [`flytekit.sensor.base_sensor.Protocol`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorprotocol) |Base class for protocol classes. |
| [`flytekit.sensor.base_sensor.PythonTask`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.sensor.base_sensor.ResourceMeta`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorresourcemeta) |This is the metadata for the job. |
| [`flytekit.sensor.base_sensor.SensorConfig`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorsensorconfig) |Base class for protocol classes. |
| [`flytekit.sensor.base_sensor.SensorMetadata`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorsensormetadata) | |
| [`flytekit.sensor.base_sensor.SerializationSettings`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensorserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.sensor.base_sensor.TaskMetadata`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensortaskmetadata) |Metadata for a Task. |
| [`flytekit.sensor.base_sensor.TypeVar`](../packages/flytekit.sensor.base_sensor#flytekitsensorbase_sensortypevar) |Type variable. |
| [`flytekit.sensor.file_sensor.BaseSensor`](../packages/flytekit.sensor.file_sensor#flytekitsensorfile_sensorbasesensor) |Base class for all sensors. |
| [`flytekit.sensor.file_sensor.FileSensor`](../packages/flytekit.sensor.file_sensor#flytekitsensorfile_sensorfilesensor) |Base class for all sensors. |
| [`flytekit.sensor.file_sensor.FlyteContextManager`](../packages/flytekit.sensor.file_sensor#flytekitsensorfile_sensorflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.sensor.sensor_engine.AsyncConnectorBase`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_engineasyncconnectorbase) |This is the base class for all async connectors. |
| [`flytekit.sensor.sensor_engine.ConnectorRegistry`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_engineconnectorregistry) |This is the registry for all connectors. |
| [`flytekit.sensor.sensor_engine.FlyteContextManager`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_engineflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.sensor.sensor_engine.LiteralMap`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_engineliteralmap) | |
| [`flytekit.sensor.sensor_engine.Resource`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_engineresource) |This is the output resource of the job. |
| [`flytekit.sensor.sensor_engine.SensorEngine`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_enginesensorengine) |This is the base class for all async connectors. |
| [`flytekit.sensor.sensor_engine.SensorMetadata`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_enginesensormetadata) | |
| [`flytekit.sensor.sensor_engine.TaskExecution`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_enginetaskexecution) |A ProtocolMessage. |
| [`flytekit.sensor.sensor_engine.TaskTemplate`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_enginetasktemplate) | |
| [`flytekit.sensor.sensor_engine.TypeEngine`](../packages/flytekit.sensor.sensor_engine#flytekitsensorsensor_enginetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.testing.SecretsManager`](../packages/flytekit.testing#flytekittestingsecretsmanager) |This provides a secrets resolution logic at runtime. |
| [`flytekit.tools.fast_registration.BarColumn`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationbarcolumn) |Renders a visual progress bar. |
| [`flytekit.tools.fast_registration.CopyFileDetection`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationcopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.tools.fast_registration.DockerIgnore`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationdockerignore) |Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`flytekit.tools.fast_registration.FastPackageOptions`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationfastpackageoptions) |FastPackageOptions is used to set configuration options when packaging files. |
| [`flytekit.tools.fast_registration.FlyteContextManager`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.tools.fast_registration.FlyteDataNotFoundException`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationflytedatanotfoundexception) |Inappropriate argument value (of correct type). |
| [`flytekit.tools.fast_registration.FlyteIgnore`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationflyteignore) |Uses a . |
| [`flytekit.tools.fast_registration.GitIgnore`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationgitignore) |Uses git cli (if available) to list all ignored files and compare with those. |
| [`flytekit.tools.fast_registration.Ignore`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationignore) |Base for Ignores, implements core logic. |
| [`flytekit.tools.fast_registration.IgnoreGroup`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationignoregroup) |Groups multiple Ignores and checks a path against them. |
| [`flytekit.tools.fast_registration.Progress`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationprogress) |Renders an auto-updating progress bar(s). |
| [`flytekit.tools.fast_registration.StandardIgnore`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationstandardignore) |Retains the standard ignore functionality that previously existed. |
| [`flytekit.tools.fast_registration.TextColumn`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationtextcolumn) |A column containing text. |
| [`flytekit.tools.fast_registration.TimeElapsedColumn`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationtimeelapsedcolumn) |Renders time elapsed. |
| [`flytekit.tools.fast_registration.Tree`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationtree) |A renderable for a tree structure. |
| [`flytekit.tools.fast_registration.timeit`](../packages/flytekit.tools.fast_registration#flytekittoolsfast_registrationtimeit) |A context manager and a decorator that measures the execution time of the wrapped code block or functions. |
| [`flytekit.tools.ignore.ABC`](../packages/flytekit.tools.ignore#flytekittoolsignoreabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.tools.ignore.DockerIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignoredockerignore) |Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`flytekit.tools.ignore.FlyteIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignoreflyteignore) |Uses a . |
| [`flytekit.tools.ignore.GitIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignoregitignore) |Uses git cli (if available) to list all ignored files and compare with those. |
| [`flytekit.tools.ignore.Ignore`](../packages/flytekit.tools.ignore#flytekittoolsignoreignore) |Base for Ignores, implements core logic. |
| [`flytekit.tools.ignore.IgnoreGroup`](../packages/flytekit.tools.ignore#flytekittoolsignoreignoregroup) |Groups multiple Ignores and checks a path against them. |
| [`flytekit.tools.ignore.Path`](../packages/flytekit.tools.ignore#flytekittoolsignorepath) |PurePath subclass that can make system calls. |
| [`flytekit.tools.ignore.PatternMatcher`](../packages/flytekit.tools.ignore#flytekittoolsignorepatternmatcher) | |
| [`flytekit.tools.ignore.StandardIgnore`](../packages/flytekit.tools.ignore#flytekittoolsignorestandardignore) |Retains the standard ignore functionality that previously existed. |
| [`flytekit.tools.module_loader.Any`](../packages/flytekit.tools.module_loader#flytekittoolsmodule_loaderany) |Special type indicating an unconstrained type. |
| [`flytekit.tools.repo.CopyFileDetection`](../packages/flytekit.tools.repo#flytekittoolsrepocopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.tools.repo.FastSerializationSettings`](../packages/flytekit.tools.repo#flytekittoolsrepofastserializationsettings) |This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`flytekit.tools.repo.FlyteContextManager`](../packages/flytekit.tools.repo#flytekittoolsrepoflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.tools.repo.FlyteRemote`](../packages/flytekit.tools.repo#flytekittoolsrepoflyteremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`flytekit.tools.repo.Identifier`](../packages/flytekit.tools.repo#flytekittoolsrepoidentifier) | |
| [`flytekit.tools.repo.ImageConfig`](../packages/flytekit.tools.repo#flytekittoolsrepoimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.tools.repo.NoSerializableEntitiesError`](../packages/flytekit.tools.repo#flytekittoolsreponoserializableentitieserror) |Common base class for all non-exit exceptions. |
| [`flytekit.tools.repo.Options`](../packages/flytekit.tools.repo#flytekittoolsrepooptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.tools.repo.Path`](../packages/flytekit.tools.repo#flytekittoolsrepopath) |PurePath subclass that can make system calls. |
| [`flytekit.tools.repo.RegistrationSkipped`](../packages/flytekit.tools.repo#flytekittoolsreporegistrationskipped) |RegistrationSkipped error is raised when trying to register an entity that is not registrable. |
| [`flytekit.tools.repo.SerializationSettings`](../packages/flytekit.tools.repo#flytekittoolsreposerializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.tools.script_mode.CopyFileDetection`](../packages/flytekit.tools.script_mode#flytekittoolsscript_modecopyfiledetection) |Create a collection of name/value pairs. |
| [`flytekit.tools.script_mode.IgnoreGroup`](../packages/flytekit.tools.script_mode#flytekittoolsscript_modeignoregroup) |Groups multiple Ignores and checks a path against them. |
| [`flytekit.tools.script_mode.ModuleType`](../packages/flytekit.tools.script_mode#flytekittoolsscript_modemoduletype) |Create a module object. |
| [`flytekit.tools.script_mode.Path`](../packages/flytekit.tools.script_mode#flytekittoolsscript_modepath) |PurePath subclass that can make system calls. |
| [`flytekit.tools.script_mode.datetime`](../packages/flytekit.tools.script_mode#flytekittoolsscript_modedatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.tools.script_mode.timezone`](../packages/flytekit.tools.script_mode#flytekittoolsscript_modetimezone) |Fixed offset from UTC implementation of tzinfo. |
| [`flytekit.tools.serialize_helpers.EagerAsyncPythonFunctionTask`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helperseagerasyncpythonfunctiontask) |This is the base eager task (aka eager workflow) type. |
| [`flytekit.tools.serialize_helpers.LaunchPlan`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helperslaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.tools.serialize_helpers.Options`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helpersoptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.tools.serialize_helpers.OrderedDict`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helpersordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.tools.serialize_helpers.PythonTask`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helperspythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.tools.serialize_helpers.RemoteEntity`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helpersremoteentity) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.tools.serialize_helpers.TaskSpec`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helperstaskspec) | |
| [`flytekit.tools.serialize_helpers.WorkflowBase`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helpersworkflowbase) | |
| [`flytekit.tools.serialize_helpers.WorkflowSpec`](../packages/flytekit.tools.serialize_helpers#flytekittoolsserialize_helpersworkflowspec) | |
| [`flytekit.tools.translator.ApproveCondition`](../packages/flytekit.tools.translator#flytekittoolstranslatorapprovecondition) | |
| [`flytekit.tools.translator.ArrayNode`](../packages/flytekit.tools.translator#flytekittoolstranslatorarraynode) | |
| [`flytekit.tools.translator.ArrayNodeMapTask`](../packages/flytekit.tools.translator#flytekittoolstranslatorarraynodemaptask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.tools.translator.ArrayNodeModel`](../packages/flytekit.tools.translator#flytekittoolstranslatorarraynodemodel) | |
| [`flytekit.tools.translator.BranchNode`](../packages/flytekit.tools.translator#flytekittoolstranslatorbranchnode) | |
| [`flytekit.tools.translator.BranchNodeModel`](../packages/flytekit.tools.translator#flytekittoolstranslatorbranchnodemodel) | |
| [`flytekit.tools.translator.ClassDecorator`](../packages/flytekit.tools.translator#flytekittoolstranslatorclassdecorator) |Abstract class for class decorators. |
| [`flytekit.tools.translator.ContainerTask`](../packages/flytekit.tools.translator#flytekittoolstranslatorcontainertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`flytekit.tools.translator.EagerAsyncPythonFunctionTask`](../packages/flytekit.tools.translator#flytekittoolstranslatoreagerasyncpythonfunctiontask) |This is the base eager task (aka eager workflow) type. |
| [`flytekit.tools.translator.Gate`](../packages/flytekit.tools.translator#flytekittoolstranslatorgate) |A node type that waits for user input before proceeding with a workflow. |
| [`flytekit.tools.translator.GateNode`](../packages/flytekit.tools.translator#flytekittoolstranslatorgatenode) | |
| [`flytekit.tools.translator.Image`](../packages/flytekit.tools.translator#flytekittoolstranslatorimage) |Image is a structured wrapper for task container images used in object serialization. |
| [`flytekit.tools.translator.ImageConfig`](../packages/flytekit.tools.translator#flytekittoolstranslatorimageconfig) |We recommend you to use ImageConfig. |
| [`flytekit.tools.translator.ImageSpec`](../packages/flytekit.tools.translator#flytekittoolstranslatorimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`flytekit.tools.translator.LaunchPlan`](../packages/flytekit.tools.translator#flytekittoolstranslatorlaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`flytekit.tools.translator.MapPythonTask`](../packages/flytekit.tools.translator#flytekittoolstranslatormappythontask) |A MapPythonTask defines a :py:class:`flytekit. |
| [`flytekit.tools.translator.Node`](../packages/flytekit.tools.translator#flytekittoolstranslatornode) |This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`flytekit.tools.translator.Options`](../packages/flytekit.tools.translator#flytekittoolstranslatoroptions) |These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`flytekit.tools.translator.OrderedDict`](../packages/flytekit.tools.translator#flytekittoolstranslatorordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.tools.translator.PodTemplate`](../packages/flytekit.tools.translator#flytekittoolstranslatorpodtemplate) |Custom PodTemplate specification for a Task. |
| [`flytekit.tools.translator.PythonAutoContainerTask`](../packages/flytekit.tools.translator#flytekittoolstranslatorpythonautocontainertask) |A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`flytekit.tools.translator.PythonFunctionTask`](../packages/flytekit.tools.translator#flytekittoolstranslatorpythonfunctiontask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`flytekit.tools.translator.PythonTask`](../packages/flytekit.tools.translator#flytekittoolstranslatorpythontask) |Base Class for all Tasks with a Python native ``Interface``. |
| [`flytekit.tools.translator.ReferenceEntity`](../packages/flytekit.tools.translator#flytekittoolstranslatorreferenceentity) | |
| [`flytekit.tools.translator.ReferenceLaunchPlan`](../packages/flytekit.tools.translator#flytekittoolstranslatorreferencelaunchplan) |A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`flytekit.tools.translator.ReferenceSpec`](../packages/flytekit.tools.translator#flytekittoolstranslatorreferencespec) | |
| [`flytekit.tools.translator.ReferenceTask`](../packages/flytekit.tools.translator#flytekittoolstranslatorreferencetask) |This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`flytekit.tools.translator.ReferenceTemplate`](../packages/flytekit.tools.translator#flytekittoolstranslatorreferencetemplate) | |
| [`flytekit.tools.translator.ReferenceWorkflow`](../packages/flytekit.tools.translator#flytekittoolstranslatorreferenceworkflow) |A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`flytekit.tools.translator.SerializationSettings`](../packages/flytekit.tools.translator#flytekittoolstranslatorserializationsettings) |These settings are provided while serializing a workflow and task, before registration. |
| [`flytekit.tools.translator.SignalCondition`](../packages/flytekit.tools.translator#flytekittoolstranslatorsignalcondition) | |
| [`flytekit.tools.translator.SleepCondition`](../packages/flytekit.tools.translator#flytekittoolstranslatorsleepcondition) | |
| [`flytekit.tools.translator.SourceCode`](../packages/flytekit.tools.translator#flytekittoolstranslatorsourcecode) |Link to source code used to define this task or workflow. |
| [`flytekit.tools.translator.TaskNodeOverrides`](../packages/flytekit.tools.translator#flytekittoolstranslatortasknodeoverrides) | |
| [`flytekit.tools.translator.TaskSpec`](../packages/flytekit.tools.translator#flytekittoolstranslatortaskspec) | |
| [`flytekit.tools.translator.TaskTemplate`](../packages/flytekit.tools.translator#flytekittoolstranslatortasktemplate) | |
| [`flytekit.tools.translator.WorkflowBase`](../packages/flytekit.tools.translator#flytekittoolstranslatorworkflowbase) | |
| [`flytekit.tools.translator.WorkflowSpec`](../packages/flytekit.tools.translator#flytekittoolstranslatorworkflowspec) | |
| [`flytekit.types.directory.FlyteDirToMultipartBlobTransformer`](../packages/flytekit.types.directory#flytekittypesdirectoryflytedirtomultipartblobtransformer) |This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`flytekit.types.directory.FlyteDirectory`](../packages/flytekit.types.directory#flytekittypesdirectoryflytedirectory) | |
| [`flytekit.types.directory.TFRecordsDirectory`](../packages/flytekit.types.directory#flytekittypesdirectorytfrecordsdirectory) |FlyteDirectory(path: 'typing. |
| [`flytekit.types.directory.TensorboardLogs`](../packages/flytekit.types.directory#flytekittypesdirectorytensorboardlogs) |FlyteDirectory(path: 'typing. |
| [`flytekit.types.directory.types.Any`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesany) |Special type indicating an unconstrained type. |
| [`flytekit.types.directory.types.AsyncTypeTransformer`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.directory.types.Binary`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesbinary) | |
| [`flytekit.types.directory.types.Blob`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesblob) | |
| [`flytekit.types.directory.types.BlobMetadata`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.types.directory.types.BlobType`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesblobtype) |This type represents offloaded data and is typically used for things like files. |
| [`flytekit.types.directory.types.DataClassJsonMixin`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesdataclassjsonmixin) |DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`flytekit.types.directory.types.FileExt`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesfileext) |Used for annotating file extension types of FlyteFile. |
| [`flytekit.types.directory.types.FlyteAssertion`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflyteassertion) |Assertion failed. |
| [`flytekit.types.directory.types.FlyteContext`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.directory.types.FlyteContextManager`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.types.directory.types.FlyteDirToMultipartBlobTransformer`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytedirtomultipartblobtransformer) |This transformer handles conversion between the Python native FlyteDirectory class defined above, and the Flyte. |
| [`flytekit.types.directory.types.FlyteDirectory`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytedirectory) | |
| [`flytekit.types.directory.types.FlyteFile`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytefile) | |
| [`flytekit.types.directory.types.Literal`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesliteral) | |
| [`flytekit.types.directory.types.LiteralType`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesliteraltype) | |
| [`flytekit.types.directory.types.Path`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypespath) |PurePath subclass that can make system calls. |
| [`flytekit.types.directory.types.Scalar`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesscalar) | |
| [`flytekit.types.directory.types.SerializableType`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesserializabletype) | |
| [`flytekit.types.directory.types.Struct`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesstruct) |A ProtocolMessage. |
| [`flytekit.types.directory.types.TypeEngine`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypestypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.directory.types.TypeTransformerFailedError`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypestypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.directory.types.UUID`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypesuuid) |Instances of the UUID class represent UUIDs as specified in RFC 4122. |
| [`flytekit.types.directory.types.partial`](../packages/flytekit.types.directory.types#flytekittypesdirectorytypespartial) |Create a new function with partial application of the given arguments. |
| [`flytekit.types.error.FlyteError`](../packages/flytekit.types.error#flytekittypeserrorflyteerror) |Special Task type that will be used in the failure node. |
| [`flytekit.types.error.error.DataClassJSONMixin`](../packages/flytekit.types.error.error#flytekittypeserrorerrordataclassjsonmixin) | |
| [`flytekit.types.error.error.Error`](../packages/flytekit.types.error.error#flytekittypeserrorerrorerror) | |
| [`flytekit.types.error.error.ErrorTransformer`](../packages/flytekit.types.error.error#flytekittypeserrorerrorerrortransformer) |Enables converting a python type FlyteError to LiteralType. |
| [`flytekit.types.error.error.FlyteContext`](../packages/flytekit.types.error.error#flytekittypeserrorerrorflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.error.error.FlyteError`](../packages/flytekit.types.error.error#flytekittypeserrorerrorflyteerror) |Special Task type that will be used in the failure node. |
| [`flytekit.types.error.error.Literal`](../packages/flytekit.types.error.error#flytekittypeserrorerrorliteral) | |
| [`flytekit.types.error.error.LiteralType`](../packages/flytekit.types.error.error#flytekittypeserrorerrorliteraltype) | |
| [`flytekit.types.error.error.Scalar`](../packages/flytekit.types.error.error#flytekittypeserrorerrorscalar) | |
| [`flytekit.types.error.error.TypeEngine`](../packages/flytekit.types.error.error#flytekittypeserrorerrortypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.error.error.TypeTransformer`](../packages/flytekit.types.error.error#flytekittypeserrorerrortypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.error.error.TypeTransformerFailedError`](../packages/flytekit.types.error.error#flytekittypeserrorerrortypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.error.error.TypeVar`](../packages/flytekit.types.error.error#flytekittypeserrorerrortypevar) |Type variable. |
| [`flytekit.types.file.CSVFile`](../packages/flytekit.types.file#flytekittypesfilecsvfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.FileExt`](../packages/flytekit.types.file#flytekittypesfilefileext) |Used for annotating file extension types of FlyteFile. |
| [`flytekit.types.file.FlyteFile`](../packages/flytekit.types.file#flytekittypesfileflytefile) | |
| [`flytekit.types.file.FlyteFilePathTransformer`](../packages/flytekit.types.file#flytekittypesfileflytefilepathtransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.file.HDF5EncodedFile`](../packages/flytekit.types.file#flytekittypesfilehdf5encodedfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.HTMLPage`](../packages/flytekit.types.file#flytekittypesfilehtmlpage) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.JPEGImageFile`](../packages/flytekit.types.file#flytekittypesfilejpegimagefile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.JSONLFile`](../packages/flytekit.types.file#flytekittypesfilejsonlfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.JoblibSerializedFile`](../packages/flytekit.types.file#flytekittypesfilejoblibserializedfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.ONNXFile`](../packages/flytekit.types.file#flytekittypesfileonnxfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.PDFFile`](../packages/flytekit.types.file#flytekittypesfilepdffile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.PNGImageFile`](../packages/flytekit.types.file#flytekittypesfilepngimagefile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.PythonNotebook`](../packages/flytekit.types.file#flytekittypesfilepythonnotebook) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.PythonPickledFile`](../packages/flytekit.types.file#flytekittypesfilepythonpickledfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.SVGImageFile`](../packages/flytekit.types.file#flytekittypesfilesvgimagefile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.TFRecordFile`](../packages/flytekit.types.file#flytekittypesfiletfrecordfile) |FlyteFile(path: 'typing. |
| [`flytekit.types.file.file.AsyncTypeTransformer`](../packages/flytekit.types.file.file#flytekittypesfilefileasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.file.file.Binary`](../packages/flytekit.types.file.file#flytekittypesfilefilebinary) | |
| [`flytekit.types.file.file.Blob`](../packages/flytekit.types.file.file#flytekittypesfilefileblob) | |
| [`flytekit.types.file.file.BlobMetadata`](../packages/flytekit.types.file.file#flytekittypesfilefileblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.types.file.file.BlobType`](../packages/flytekit.types.file.file#flytekittypesfilefileblobtype) |This type represents offloaded data and is typically used for things like files. |
| [`flytekit.types.file.file.DataClassJSONMixin`](../packages/flytekit.types.file.file#flytekittypesfilefiledataclassjsonmixin) | |
| [`flytekit.types.file.file.FlyteAssertion`](../packages/flytekit.types.file.file#flytekittypesfilefileflyteassertion) |Assertion failed. |
| [`flytekit.types.file.file.FlyteContext`](../packages/flytekit.types.file.file#flytekittypesfilefileflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.file.file.FlyteContextManager`](../packages/flytekit.types.file.file#flytekittypesfilefileflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.types.file.file.FlyteFile`](../packages/flytekit.types.file.file#flytekittypesfilefileflytefile) | |
| [`flytekit.types.file.file.FlyteFilePathTransformer`](../packages/flytekit.types.file.file#flytekittypesfilefileflytefilepathtransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.file.file.FlytePickleTransformer`](../packages/flytekit.types.file.file#flytekittypesfilefileflytepickletransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.file.file.Literal`](../packages/flytekit.types.file.file#flytekittypesfilefileliteral) | |
| [`flytekit.types.file.file.LiteralType`](../packages/flytekit.types.file.file#flytekittypesfilefileliteraltype) | |
| [`flytekit.types.file.file.Scalar`](../packages/flytekit.types.file.file#flytekittypesfilefilescalar) | |
| [`flytekit.types.file.file.SerializableType`](../packages/flytekit.types.file.file#flytekittypesfilefileserializabletype) | |
| [`flytekit.types.file.file.Struct`](../packages/flytekit.types.file.file#flytekittypesfilefilestruct) |A ProtocolMessage. |
| [`flytekit.types.file.file.TypeEngine`](../packages/flytekit.types.file.file#flytekittypesfilefiletypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.file.file.TypeTransformerFailedError`](../packages/flytekit.types.file.file#flytekittypesfilefiletypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.file.file.partial`](../packages/flytekit.types.file.file#flytekittypesfilefilepartial) |Create a new function with partial application of the given arguments. |
| [`flytekit.types.file.image.Blob`](../packages/flytekit.types.file.image#flytekittypesfileimageblob) | |
| [`flytekit.types.file.image.BlobMetadata`](../packages/flytekit.types.file.image#flytekittypesfileimageblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.types.file.image.FlyteContext`](../packages/flytekit.types.file.image#flytekittypesfileimageflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.file.image.Literal`](../packages/flytekit.types.file.image#flytekittypesfileimageliteral) | |
| [`flytekit.types.file.image.LiteralType`](../packages/flytekit.types.file.image#flytekittypesfileimageliteraltype) | |
| [`flytekit.types.file.image.PILImageTransformer`](../packages/flytekit.types.file.image#flytekittypesfileimagepilimagetransformer) |TypeTransformer that supports PIL. |
| [`flytekit.types.file.image.Scalar`](../packages/flytekit.types.file.image#flytekittypesfileimagescalar) | |
| [`flytekit.types.file.image.TypeEngine`](../packages/flytekit.types.file.image#flytekittypesfileimagetypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.file.image.TypeTransformer`](../packages/flytekit.types.file.image#flytekittypesfileimagetypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.file.image.TypeTransformerFailedError`](../packages/flytekit.types.file.image#flytekittypesfileimagetypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.iterator.FlyteIterator`](../packages/flytekit.types.iterator#flytekittypesiteratorflyteiterator) | |
| [`flytekit.types.iterator.iterator.FlyteContext`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratorflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.iterator.iterator.FlyteIterator`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratorflyteiterator) | |
| [`flytekit.types.iterator.iterator.IteratorTransformer`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratoriteratortransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.iterator.iterator.Literal`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratorliteral) | |
| [`flytekit.types.iterator.iterator.LiteralCollection`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratorliteralcollection) | |
| [`flytekit.types.iterator.iterator.LiteralType`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratorliteraltype) | |
| [`flytekit.types.iterator.iterator.TypeEngine`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratortypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.iterator.iterator.TypeTransformer`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratortypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.iterator.iterator.TypeTransformerFailedError`](../packages/flytekit.types.iterator.iterator#flytekittypesiteratoriteratortypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.iterator.json_iterator.Any`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorany) |Special type indicating an unconstrained type. |
| [`flytekit.types.iterator.json_iterator.AsyncTypeTransformer`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.iterator.json_iterator.Blob`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorblob) | |
| [`flytekit.types.iterator.json_iterator.BlobMetadata`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.types.iterator.json_iterator.FlyteContext`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.iterator.json_iterator.JSONIterator`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorjsoniterator) |Abstract base class for generic types. |
| [`flytekit.types.iterator.json_iterator.JSONIteratorTransformer`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorjsoniteratortransformer) |A JSON iterator that handles conversion between an iterator/generator and a JSONL file. |
| [`flytekit.types.iterator.json_iterator.Literal`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorliteral) | |
| [`flytekit.types.iterator.json_iterator.LiteralType`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorliteraltype) | |
| [`flytekit.types.iterator.json_iterator.Path`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorpath) |PurePath subclass that can make system calls. |
| [`flytekit.types.iterator.json_iterator.Scalar`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratorscalar) | |
| [`flytekit.types.iterator.json_iterator.TypeEngine`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratortypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.iterator.json_iterator.TypeTransformerFailedError`](../packages/flytekit.types.iterator.json_iterator#flytekittypesiteratorjson_iteratortypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.numpy.NumpyArrayTransformer`](../packages/flytekit.types.numpy#flytekittypesnumpynumpyarraytransformer) |TypeTransformer that supports np. |
| [`flytekit.types.numpy.ndarray.AsyncTypeTransformer`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.numpy.ndarray.Blob`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayblob) | |
| [`flytekit.types.numpy.ndarray.BlobMetadata`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.types.numpy.ndarray.FlyteContext`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.numpy.ndarray.HashMethod`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayhashmethod) |Flyte-specific object used to wrap the hash function for a specific type. |
| [`flytekit.types.numpy.ndarray.Literal`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayliteral) | |
| [`flytekit.types.numpy.ndarray.LiteralType`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayliteraltype) | |
| [`flytekit.types.numpy.ndarray.NumpyArrayTransformer`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarraynumpyarraytransformer) |TypeTransformer that supports np. |
| [`flytekit.types.numpy.ndarray.OrderedDict`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayordereddict) |Dictionary that remembers insertion order. |
| [`flytekit.types.numpy.ndarray.Scalar`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarrayscalar) | |
| [`flytekit.types.numpy.ndarray.TypeEngine`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarraytypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.numpy.ndarray.TypeTransformerFailedError`](../packages/flytekit.types.numpy.ndarray#flytekittypesnumpyndarraytypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.pickle.FlytePickle`](../packages/flytekit.types.pickle#flytekittypespickleflytepickle) |This type is only used by flytekit internally. |
| [`flytekit.types.pickle.pickle.AsyncTypeTransformer`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.pickle.pickle.Blob`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleblob) | |
| [`flytekit.types.pickle.pickle.BlobMetadata`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleblobmetadata) |This is metadata for the Blob literal. |
| [`flytekit.types.pickle.pickle.FlyteContext`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.pickle.pickle.FlyteContextManager`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.types.pickle.pickle.FlytePickle`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleflytepickle) |This type is only used by flytekit internally. |
| [`flytekit.types.pickle.pickle.FlytePickleTransformer`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleflytepickletransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.pickle.pickle.Literal`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleliteral) | |
| [`flytekit.types.pickle.pickle.LiteralType`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickleliteraltype) | |
| [`flytekit.types.pickle.pickle.Scalar`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepicklescalar) | |
| [`flytekit.types.pickle.pickle.TypeEngine`](../packages/flytekit.types.pickle.pickle#flytekittypespicklepickletypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.schema.FlyteSchema`](../packages/flytekit.types.schema#flytekittypesschemaflyteschema) | |
| [`flytekit.types.schema.FlyteSchemaTransformer`](../packages/flytekit.types.schema#flytekittypesschemaflyteschematransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.schema.LocalIOSchemaReader`](../packages/flytekit.types.schema#flytekittypesschemalocalioschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.LocalIOSchemaWriter`](../packages/flytekit.types.schema#flytekittypesschemalocalioschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.SchemaEngine`](../packages/flytekit.types.schema#flytekittypesschemaschemaengine) |This is the core Engine that handles all schema sub-systems. |
| [`flytekit.types.schema.SchemaFormat`](../packages/flytekit.types.schema#flytekittypesschemaschemaformat) |Represents the schema storage format (at rest). |
| [`flytekit.types.schema.SchemaHandler`](../packages/flytekit.types.schema#flytekittypesschemaschemahandler) | |
| [`flytekit.types.schema.SchemaOpenMode`](../packages/flytekit.types.schema#flytekittypesschemaschemaopenmode) |Create a collection of name/value pairs. |
| [`flytekit.types.schema.SchemaReader`](../packages/flytekit.types.schema#flytekittypesschemaschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.SchemaWriter`](../packages/flytekit.types.schema#flytekittypesschemaschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types.AsyncTypeTransformer`](../packages/flytekit.types.schema.types#flytekittypesschematypesasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.schema.types.Binary`](../packages/flytekit.types.schema.types#flytekittypesschematypesbinary) | |
| [`flytekit.types.schema.types.DataClassJSONMixin`](../packages/flytekit.types.schema.types#flytekittypesschematypesdataclassjsonmixin) | |
| [`flytekit.types.schema.types.Enum`](../packages/flytekit.types.schema.types#flytekittypesschematypesenum) |Create a collection of name/value pairs. |
| [`flytekit.types.schema.types.FlyteContext`](../packages/flytekit.types.schema.types#flytekittypesschematypesflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.schema.types.FlyteContextManager`](../packages/flytekit.types.schema.types#flytekittypesschematypesflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.types.schema.types.FlyteSchema`](../packages/flytekit.types.schema.types#flytekittypesschematypesflyteschema) | |
| [`flytekit.types.schema.types.FlyteSchemaTransformer`](../packages/flytekit.types.schema.types#flytekittypesschematypesflyteschematransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.schema.types.Literal`](../packages/flytekit.types.schema.types#flytekittypesschematypesliteral) | |
| [`flytekit.types.schema.types.LiteralType`](../packages/flytekit.types.schema.types#flytekittypesschematypesliteraltype) | |
| [`flytekit.types.schema.types.LocalIOSchemaReader`](../packages/flytekit.types.schema.types#flytekittypesschematypeslocalioschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types.LocalIOSchemaWriter`](../packages/flytekit.types.schema.types#flytekittypesschematypeslocalioschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types.Path`](../packages/flytekit.types.schema.types#flytekittypesschematypespath) |PurePath subclass that can make system calls. |
| [`flytekit.types.schema.types.Scalar`](../packages/flytekit.types.schema.types#flytekittypesschematypesscalar) | |
| [`flytekit.types.schema.types.Schema`](../packages/flytekit.types.schema.types#flytekittypesschematypesschema) | |
| [`flytekit.types.schema.types.SchemaEngine`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemaengine) |This is the core Engine that handles all schema sub-systems. |
| [`flytekit.types.schema.types.SchemaFormat`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemaformat) |Represents the schema storage format (at rest). |
| [`flytekit.types.schema.types.SchemaHandler`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemahandler) | |
| [`flytekit.types.schema.types.SchemaOpenMode`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemaopenmode) |Create a collection of name/value pairs. |
| [`flytekit.types.schema.types.SchemaReader`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types.SchemaType`](../packages/flytekit.types.schema.types#flytekittypesschematypesschematype) | |
| [`flytekit.types.schema.types.SchemaWriter`](../packages/flytekit.types.schema.types#flytekittypesschematypesschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types.SerializableType`](../packages/flytekit.types.schema.types#flytekittypesschematypesserializabletype) | |
| [`flytekit.types.schema.types.Struct`](../packages/flytekit.types.schema.types#flytekittypesschematypesstruct) |A ProtocolMessage. |
| [`flytekit.types.schema.types.TypeEngine`](../packages/flytekit.types.schema.types#flytekittypesschematypestypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.schema.types.TypeTransformerFailedError`](../packages/flytekit.types.schema.types#flytekittypesschematypestypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.types.schema.types_pandas.AsyncTypeTransformer`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.schema.types_pandas.FlyteContext`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.schema.types_pandas.Literal`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasliteral) | |
| [`flytekit.types.schema.types_pandas.LiteralType`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasliteraltype) | |
| [`flytekit.types.schema.types_pandas.LocalIOSchemaReader`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaslocalioschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types_pandas.LocalIOSchemaWriter`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaslocalioschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types_pandas.PandasDataFrameTransformer`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasdataframetransformer) |Transforms a pd. |
| [`flytekit.types.schema.types_pandas.PandasSchemaReader`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemareader) |Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`flytekit.types.schema.types_pandas.PandasSchemaWriter`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandaspandasschemawriter) |Abstract base class for generic types. |
| [`flytekit.types.schema.types_pandas.ParquetIO`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasparquetio) | |
| [`flytekit.types.schema.types_pandas.Scalar`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasscalar) | |
| [`flytekit.types.schema.types_pandas.Schema`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasschema) | |
| [`flytekit.types.schema.types_pandas.SchemaEngine`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasschemaengine) |This is the core Engine that handles all schema sub-systems. |
| [`flytekit.types.schema.types_pandas.SchemaFormat`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasschemaformat) |Represents the schema storage format (at rest). |
| [`flytekit.types.schema.types_pandas.SchemaHandler`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasschemahandler) | |
| [`flytekit.types.schema.types_pandas.SchemaType`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandasschematype) | |
| [`flytekit.types.schema.types_pandas.TypeEngine`](../packages/flytekit.types.schema.types_pandas#flytekittypesschematypes_pandastypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.structured.ArrowRenderer`](../packages/flytekit.types.structured#flytekittypesstructuredarrowrenderer) |Render an Arrow dataframe as an HTML table. |
| [`flytekit.types.structured.DuplicateHandlerError`](../packages/flytekit.types.structured#flytekittypesstructuredduplicatehandlererror) |Inappropriate argument value (of correct type). |
| [`flytekit.types.structured.StructuredDataset`](../packages/flytekit.types.structured#flytekittypesstructuredstructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.StructuredDatasetDecoder`](../packages/flytekit.types.structured#flytekittypesstructuredstructureddatasetdecoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.StructuredDatasetEncoder`](../packages/flytekit.types.structured#flytekittypesstructuredstructureddatasetencoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.StructuredDatasetTransformerEngine`](../packages/flytekit.types.structured#flytekittypesstructuredstructureddatasettransformerengine) |Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flytekit.types.structured.TopFrameRenderer`](../packages/flytekit.types.structured#flytekittypesstructuredtopframerenderer) |Render a DataFrame as an HTML table. |
| [`flytekit.types.structured.basic_dfs.ArrowToParquetEncodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsarrowtoparquetencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.CSVToPandasDecodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfscsvtopandasdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.DataConfig`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsdataconfig) |Any data storage specific configuration. |
| [`flytekit.types.structured.basic_dfs.FlyteContext`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.structured.basic_dfs.NoCredentialsError`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsnocredentialserror) |No credentials could be found. |
| [`flytekit.types.structured.basic_dfs.PandasToCSVEncodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastocsvencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.PandasToParquetEncodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastoparquetencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.ParquetToArrowDecodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettoarrowdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.ParquetToPandasDecodingHandler`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettopandasdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.Path`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspath) |PurePath subclass that can make system calls. |
| [`flytekit.types.structured.basic_dfs.StructuredDataset`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.basic_dfs.StructuredDatasetDecoder`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasetdecoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.StructuredDatasetEncoder`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasetencoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.basic_dfs.StructuredDatasetMetadata`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasetmetadata) | |
| [`flytekit.types.structured.basic_dfs.StructuredDatasetType`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasettype) | |
| [`flytekit.types.structured.basic_dfs.TypeVar`](../packages/flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfstypevar) |Type variable. |
| [`flytekit.types.structured.snowflake.FlyteContext`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakeflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.structured.snowflake.PandasToSnowflakeEncodingHandlers`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakepandastosnowflakeencodinghandlers) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.snowflake.SnowflakeToPandasDecodingHandler`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakesnowflaketopandasdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.snowflake.StructuredDataset`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakestructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.snowflake.StructuredDatasetDecoder`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakestructureddatasetdecoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.snowflake.StructuredDatasetEncoder`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakestructureddatasetencoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.snowflake.StructuredDatasetMetadata`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakestructureddatasetmetadata) | |
| [`flytekit.types.structured.snowflake.StructuredDatasetType`](../packages/flytekit.types.structured.snowflake#flytekittypesstructuredsnowflakestructureddatasettype) | |
| [`flytekit.types.structured.structured_dataset.ABC`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetabc) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.structured_dataset.AsyncTypeTransformer`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetasynctypetransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekit.types.structured.structured_dataset.Binary`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetbinary) | |
| [`flytekit.types.structured.structured_dataset.DataClassJSONMixin`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetdataclassjsonmixin) | |
| [`flytekit.types.structured.structured_dataset.DuplicateHandlerError`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetduplicatehandlererror) |Inappropriate argument value (of correct type). |
| [`flytekit.types.structured.structured_dataset.FlyteContext`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetflytecontext) |This is an internal-facing context object, that most users will not have to deal with. |
| [`flytekit.types.structured.structured_dataset.FlyteContextManager`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetflytecontextmanager) |FlyteContextManager manages the execution context within Flytekit. |
| [`flytekit.types.structured.structured_dataset.Generic`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetgeneric) |Abstract base class for generic types. |
| [`flytekit.types.structured.structured_dataset.Literal`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetliteral) | |
| [`flytekit.types.structured.structured_dataset.LiteralType`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetliteraltype) | |
| [`flytekit.types.structured.structured_dataset.Renderable`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetrenderable) |Base class for protocol classes. |
| [`flytekit.types.structured.structured_dataset.Scalar`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetscalar) | |
| [`flytekit.types.structured.structured_dataset.SchemaType`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetschematype) | |
| [`flytekit.types.structured.structured_dataset.SerializableType`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetserializabletype) | |
| [`flytekit.types.structured.structured_dataset.Struct`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstruct) |A ProtocolMessage. |
| [`flytekit.types.structured.structured_dataset.StructuredDataset`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddataset) |This is the user facing StructuredDataset class. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetDecoder`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetdecoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetEncoder`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetencoder) |Helper class that provides a standard way to create an ABC using. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetFormat`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetformat) |str(object='') -> str. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetMetadata`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetmetadata) | |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetTransformerEngine`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettransformerengine) |Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`flytekit.types.structured.structured_dataset.StructuredDatasetType`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettype) | |
| [`flytekit.types.structured.structured_dataset.TypeEngine`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasettypeengine) |Core Extensible TypeEngine of Flytekit. |
| [`flytekit.types.structured.structured_dataset.TypeTransformerFailedError`](../packages/flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasettypetransformerfailederror) |Inappropriate argument type. |
| [`flytekit.utils.asyn.Any`](../packages/flytekit.utils.asyn#flytekitutilsasynany) |Special type indicating an unconstrained type. |
| [`flytekit.utils.asyn.ParamSpec`](../packages/flytekit.utils.asyn#flytekitutilsasynparamspec) |Parameter specification variable. |
| [`flytekit.utils.asyn.TypeVar`](../packages/flytekit.utils.asyn#flytekitutilsasyntypevar) |Type variable. |
| [`flytekit.utils.dict_formatter.Any`](../packages/flytekit.utils.dict_formatter#flytekitutilsdict_formatterany) |Special type indicating an unconstrained type. |
| [`flytekit.utils.pbhash.Message`](../packages/flytekit.utils.pbhash#flytekitutilspbhashmessage) |Abstract base class for protocol messages. |
| [`flytekit.utils.rate_limiter.RateLimiter`](../packages/flytekit.utils.rate_limiter#flytekitutilsrate_limiterratelimiter) |Rate limiter that allows up to a certain number of requests per minute. |
| [`flytekit.utils.rate_limiter.datetime`](../packages/flytekit.utils.rate_limiter#flytekitutilsrate_limiterdatetime) |datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`flytekit.utils.rate_limiter.deque`](../packages/flytekit.utils.rate_limiter#flytekitutilsrate_limiterdeque) |A list-like sequence optimized for data accesses near its endpoints. |
| [`flytekit.utils.rate_limiter.timedelta`](../packages/flytekit.utils.rate_limiter#flytekitutilsrate_limitertimedelta) |Difference between two datetime values. |
