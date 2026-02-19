---
title: flytekit.core.context_manager
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.context_manager


These classes provide functionality related context management.

## Directory

### Classes

| Class | Description |
|-|-|
| [`BranchEvalMode`](../flytekit.core.context_manager/branchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`CompilationState`](../flytekit.core.context_manager/compilationstate) | Compilation state is used during the compilation of a workflow or task. |
| [`ExecutionParameters`](../flytekit.core.context_manager/executionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`ExecutionState`](../flytekit.core.context_manager/executionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](../flytekit.core.context_manager/flytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](../flytekit.core.context_manager/flytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteEntities`](../flytekit.core.context_manager/flyteentities) | This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`OutputMetadata`](../flytekit.core.context_manager/outputmetadata) |  |
| [`OutputMetadataTracker`](../flytekit.core.context_manager/outputmetadatatracker) | This class is for the users to set arbitrary metadata on output literals. |
| [`SecretsManager`](../flytekit.core.context_manager/secretsmanager) | This provides a secrets resolution logic at runtime. |

### Protocols

| Protocol | Description |
|-|-|
| [`SerializableToString`](../flytekit.core.context_manager/serializabletostring) | This protocol is used by the Artifact create_from function. |

### Variables

| Property | Type | Description |
|-|-|-|
| `flyte_context_Var` | `ContextVar` |  |

