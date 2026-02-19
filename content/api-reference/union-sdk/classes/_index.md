---
title: Classes & Protocols
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`union.ActorEnvironment`](../packages/union/actorenvironment) |ActorEnvironment class. |
| [`union.Artifact`](../packages/union/artifact) |This is a wrapper around the Flytekit Artifact class. |
| [`union.Cache`](../packages/union/cache) |Cache configuration for a task. |
| [`union.ContainerTask`](../packages/union/containertask) |This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`union.Deck`](../packages/union/deck) |Deck enable users to get customizable and default visibility into their tasks. |
| [`union.FlyteDirectory`](../packages/union/flytedirectory) | |
| [`union.FlyteFile`](../packages/union/flytefile) | |
| [`union.ImageSpec`](../packages/union/imagespec) |This class is used to specify the docker image that will be used to run the task. |
| [`union.LaunchPlan`](../packages/union/launchplan) |Launch Plans are one of the core constructs of Flyte. |
| [`union.PodTemplate`](../packages/union/podtemplate) |Custom PodTemplate specification for a Task. |
| [`union.Resources`](../packages/union/resources) |This class is used to specify both resource requests and resource limits. |
| [`union.Secret`](../packages/union/secret) |See :std:ref:`cookbook:secrets` for usage examples. |
| [`union.StructuredDataset`](../packages/union/structureddataset) |This is the user facing StructuredDataset class. |
| [`union.UnionRemote`](../packages/union/unionremote) | |
| [`union.VersionParameters`](../packages/union/versionparameters) |Parameters used for version hash generation. |
| [`union.actor.ActorEnvironment`](../packages/union.actor/actorenvironment) |ActorEnvironment class. |
| [`union.actor.ActorTask`](../packages/union.actor/actortask) | |
| [`union.app.App`](../packages/union.app/app) |App specification. |
| [`union.app.ArizeConfig`](../packages/union.app/arizeconfig) | |
| [`union.app.FlyteConnectorApp`](../packages/union.app/flyteconnectorapp) |FlyteConnector application specification that inherits from App. |
| [`union.app.Input`](../packages/union.app/input) |Input for application. |
| [`union.app.Link`](../packages/union.app/link) | |
| [`union.app.PhoenixConfig`](../packages/union.app/phoenixconfig) | |
| [`union.app.ScalingMetric`](../packages/union.app/scalingmetric) | |
| [`union.app.URLQuery`](../packages/union.app/urlquery) | |
| [`union.app.WeaveConfig`](../packages/union.app/weaveconfig) | |
| [`union.app.llm.SGLangApp`](../packages/union.app.llm/sglangapp) |App backed by FastAPI. |
| [`union.app.llm.VLLMApp`](../packages/union.app.llm/vllmapp) |App backed by FastAPI. |
| [`union.artifacts.Artifact`](../packages/union.artifacts/artifact) |This is a wrapper around the Flytekit Artifact class. |
| [`union.artifacts.DataCard`](../packages/union.artifacts/datacard) | |
| [`union.artifacts.ModelCard`](../packages/union.artifacts/modelcard) | |
| [`union.artifacts.OnArtifact`](../packages/union.artifacts/onartifact) |Event used to link upstream and downstream workflows together. |
| [`union.cache.CacheFunctionBody`](../packages/union.cache/cachefunctionbody) |A class that implements a versioning mechanism for functions by generating. |
| [`union.configuration.UnionAIPlugin`](../packages/union.configuration/unionaiplugin) | |
| [`union.filesystems.AsyncUnionFS`](../packages/union.filesystems/asyncunionfs) | |
| [`union.filesystems.AsyncUnionMetaFS`](../packages/union.filesystems/asyncunionmetafs) | |
| [`union.remote.HuggingFaceModelInfo`](../packages/union.remote/huggingfacemodelinfo) |Captures information about a Hugging Face model. |
| [`union.remote.ShardConfig`](../packages/union.remote/shardconfig) | |
| [`union.remote.UnionRemote`](../packages/union.remote/unionremote) | |
| [`union.remote.VLLMShardArgs`](../packages/union.remote/vllmshardargs) | |
| [`union.ucimage.UCImageSpecBuilder`](../packages/union.ucimage/ucimagespecbuilder) |ImageSpec builder for UnionAI. |
# Protocols

| Protocol | Description |
|-|-|
| [`union.CachePolicy`](../packages/union/cachepolicy) | |
