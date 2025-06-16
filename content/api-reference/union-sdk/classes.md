---
title: Classes
version: 0.1.171.dev4+g052020f1.d20250404
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`union.ActorEnvironment`](../packages/union#unionactorenvironment) |ActorEnvironment class. |
| [`union.Artifact`](../packages/union#unionartifact) |This is a wrapper around the Flytekit Artifact class. |
| [`union.Cache`](../packages/union#unioncache) |Cache configuration for a task. |
| [`union.CachePolicy`](../packages/union#unioncachepolicy) |Base class for protocol classes. |
| [`union.ContainerTask`](../packages/union#unioncontainertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`union.Deck`](../packages/union#uniondeck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`union.FlyteDirectory`](../packages/union#unionflytedirectory) | |
| [`union.FlyteFile`](../packages/union#unionflytefile) | |
| [`union.ImageSpec`](../packages/union#unionimagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`union.LaunchPlan`](../packages/union#unionlaunchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`union.PodTemplate`](../packages/union#unionpodtemplate) |Custom PodTemplate specification for a Task. |
| [`union.Resources`](../packages/union#unionresources) |This class is used to specify both resource requests and resource limits. |
| [`union.Secret`](../packages/union#unionsecret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`union.StructuredDataset`](../packages/union#unionstructureddataset) |This is the user facing StructuredDataset class. |
| [`union.UnionRemote`](../packages/union#unionunionremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`union.VersionParameters`](../packages/union#unionversionparameters) |Parameters used for version hash generation. |
| [`union.actor.ActorEnvironment`](../packages/union.actor#unionactoractorenvironment) |ActorEnvironment class. |
| [`union.actor.ActorTask`](../packages/union.actor#unionactoractortask) |A Python Function task should be used as the base for all extensions that have a python function. |
| [`union.app.App`](../packages/union.app#unionappapp) |App specification. |
| [`union.app.FlyteConnectorApp`](../packages/union.app#unionappflyteconnectorapp) |FlyteConnector application specification that inherits from App. |
| [`union.app.Input`](../packages/union.app#unionappinput) |Input for application. |
| [`union.app.ScalingMetric`](../packages/union.app#unionappscalingmetric) | |
| [`union.app.URLQuery`](../packages/union.app#unionappurlquery) | |
| [`union.artifacts.Artifact`](../packages/union.artifacts#unionartifactsartifact) |This is a wrapper around the Flytekit Artifact class. |
| [`union.artifacts.DataCard`](../packages/union.artifacts#unionartifactsdatacard) |. |
| [`union.artifacts.ModelCard`](../packages/union.artifacts#unionartifactsmodelcard) |. |
| [`union.artifacts.OnArtifact`](../packages/union.artifacts#unionartifactsonartifact) |Event used to link upstream and downstream workflows together. |
| [`union.cache.CacheFunctionBody`](../packages/union.cache#unioncachecachefunctionbody) |A class that implements a versioning mechanism for functions by generating. |
| [`union.configuration.UnionAIPlugin`](../packages/union.configuration#unionconfigurationunionaiplugin) | |
| [`union.filesystems.AsyncUnionFS`](../packages/union.filesystems#unionfilesystemsasyncunionfs) |Async file operations, default implementations. |
| [`union.filesystems.AsyncUnionMetaFS`](../packages/union.filesystems#unionfilesystemsasyncunionmetafs) |Async file operations, default implementations. |
| [`union.remote.HuggingFaceModelInfo`](../packages/union.remote#unionremotehuggingfacemodelinfo) |Captures information about a Hugging Face model. |
| [`union.remote.UnionRemote`](../packages/union.remote#unionremoteunionremote) |Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`union.ucimage.UCImageSpecBuilder`](../packages/union.ucimage#unionucimageucimagespecbuilder) |ImageSpec builder for UnionAI. |
