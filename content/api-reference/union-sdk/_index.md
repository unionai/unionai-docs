---
title: Union SDK
version: 0.1.203
variants: -flyte +union
layout: py_api
---

# Union SDK

The Union SDK provides the Python API for writing Union workflows. It consists
of the open-source `flytekit` package in addition to the `union` package which
supports additional functionality specific to Union.

## Developing on Union

For developing on the Union platform you need to add the `union` package to your
project:

```shell
$ uv add union
```

This will install the Union SDK, which is a superset of the Flytekit SDK.
It will also install the `union` command-line tool.

When working with the Union SDK you will be using the `union` CLI and both the
Flytekit SDK and the Union SDK docs.


## Directory

### Classes

| Class | Description |
|-|-|
| [`union.ActorEnvironment`](union#unionactorenvironment) | ActorEnvironment class. |
| [`union.Artifact`](union#unionartifact) | This is a wrapper around the Flytekit Artifact class. |
| [`union.Cache`](union#unioncache) | Cache configuration for a task. |
| [`union.ContainerTask`](union#unioncontainertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`union.Deck`](union#uniondeck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`union.FlyteDirectory`](union#unionflytedirectory) |  |
| [`union.FlyteFile`](union#unionflytefile) |  |
| [`union.ImageSpec`](union#unionimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`union.LaunchPlan`](union#unionlaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`union.PodTemplate`](union#unionpodtemplate) | Custom PodTemplate specification for a Task. |
| [`union.Resources`](union#unionresources) | This class is used to specify both resource requests and resource limits. |
| [`union.Secret`](union#unionsecret) | See `cookbook:secrets` for usage examples. |
| [`union.StructuredDataset`](union#unionstructureddataset) | This is the user facing StructuredDataset class. |
| [`union.UnionRemote`](union#unionunionremote) |  |
| [`union.VersionParameters`](union#unionversionparameters) | Parameters used for version hash generation. |
| [`union.actor.ActorEnvironment`](union.actor#unionactoractorenvironment) | ActorEnvironment class. |
| [`union.actor.ActorTask`](union.actor#unionactoractortask) |  |
| [`union.app.App`](union.app#unionappapp) | App specification. |
| [`union.app.ArizeConfig`](union.app#unionapparizeconfig) |  |
| [`union.app.FlyteConnectorApp`](union.app#unionappflyteconnectorapp) | FlyteConnector application specification that inherits from App. |
| [`union.app.Input`](union.app#unionappinput) | Input for application. |
| [`union.app.Link`](union.app#unionapplink) |  |
| [`union.app.PhoenixConfig`](union.app#unionappphoenixconfig) |  |
| [`union.app.ScalingMetric`](union.app#unionappscalingmetric) |  |
| [`union.app.URLQuery`](union.app#unionappurlquery) |  |
| [`union.app.WeaveConfig`](union.app#unionappweaveconfig) |  |
| [`union.app.llm.SGLangApp`](union.app.llm#unionappllmsglangapp) | App backed by FastAPI. |
| [`union.app.llm.VLLMApp`](union.app.llm#unionappllmvllmapp) | App backed by FastAPI. |
| [`union.artifacts.Artifact`](union.artifacts#unionartifactsartifact) | This is a wrapper around the Flytekit Artifact class. |
| [`union.artifacts.DataCard`](union.artifacts#unionartifactsdatacard) |  |
| [`union.artifacts.ModelCard`](union.artifacts#unionartifactsmodelcard) |  |
| [`union.artifacts.OnArtifact`](union.artifacts#unionartifactsonartifact) | Event used to link upstream and downstream workflows together. |
| [`union.cache.CacheFunctionBody`](union.cache#unioncachecachefunctionbody) | A class that implements a versioning mechanism for functions by generating. |
| [`union.configuration.UnionAIPlugin`](union.configuration#unionconfigurationunionaiplugin) |  |
| [`union.filesystems.AsyncUnionFS`](union.filesystems#unionfilesystemsasyncunionfs) |  |
| [`union.filesystems.AsyncUnionMetaFS`](union.filesystems#unionfilesystemsasyncunionmetafs) |  |
| [`union.remote.HuggingFaceModelInfo`](union.remote#unionremotehuggingfacemodelinfo) | Captures information about a Hugging Face model. |
| [`union.remote.ShardConfig`](union.remote#unionremoteshardconfig) |  |
| [`union.remote.UnionRemote`](union.remote#unionremoteunionremote) |  |
| [`union.remote.VLLMShardArgs`](union.remote#unionremotevllmshardargs) |  |
| [`union.ucimage.UCImageSpecBuilder`](union.ucimage#unionucimageucimagespecbuilder) | ImageSpec builder for UnionAI. |

### Protocols

| Protocol | Description |
|-|-|
| [`union.CachePolicy`](union#unioncachepolicy) |  |

### Functions

| Function | Description |
|-|-|
| [`union.actor_cache()`](union#actor_cache) | Cache function between actor executions. |
| [`union.current_context()`](union#current_context) | Use this method to get a handle of specific parameters available in a flyte task. |
| [`union.map()`](union#map) | Use to map over tasks, actors, launch plans, reference tasks and launch plans, and remote tasks and. |
| [`union.map_task()`](union#map_task) | Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask. |
| [`union.task()`](union#task) | This is the core decorator to use for any task type in flytekit. |
| [`union.workflow()`](union#workflow) | This decorator declares a function to be a Flyte workflow. |
| [`union.actor.actor_cache()`](union.actor#actor_cache) | Cache function between actor executions. |
| [`union.map.map()`](union.map#map) | Use to map over tasks, actors, launch plans, reference tasks and launch plans, and remote tasks and. |

### Packages

| Package | Description |
|-|-|
| [`union`](union) |  |
| [`union.actor`](union.actor) |  |
| [`union.app`](union.app) |  |
| [`union.app.llm`](union.app.llm) |  |
| [`union.artifacts`](union.artifacts) |  |
| [`union.cache`](union.cache) |  |
| [`union.configuration`](union.configuration) |  |
| [`union.filesystems`](union.filesystems) | Module for fsspec implementations. |
| [`union.map`](union.map) |  |
| [`union.remote`](union.remote) |  |
| [`union.ucimage`](union.ucimage) |  |

