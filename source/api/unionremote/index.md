# UnionRemote

`UnionRemote` is a superset of `FlyteRemote` that provides additional methods specific to Union.

## Entrypoint

|       |        |
|-------|--------|
| [`UnionRemote`](./entrypoint.md#unionai.remote.UnionRemote) | Main entrypoint for programmatically accessing a Union remote backend.|
| [`Options`](./entrypoint.md#flytekit.remote.remote.Options) | Options that can be configured for a launch plan during registration or overridden during an execution.|

## Entities

|       |        |
|-------|--------|
| [`FlyteTask`](./entities.md#flytekit.remote.entities.FlyteTask) | A class encapsulating a remote Flyte task. |
| [`FlyteWorkflow`](./entities.md#flytekit.remote.entities.FlyteWorkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteLaunchPlan`](./entities.md#flytekit.remote.entities.FlyteLaunchPlan) | A class encapsulating a remote Flyte launch plan. |

## Entity components

|       |        |
|-------|--------|
| [`FlyteNode`](./entity-components.md#flytekit.remote.entities.FlyteNode) | A class encapsulating a remote Flyte node. |
| [`FlyteTaskNode`](./entity-components.md#flytekit.remote.entities.FlyteTaskNode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`FlyteWorkflowNode`](./entity-components.md#flytekit.remote.entities.FlyteWorkflowNode) | A class encapsulating a workflow that a Flyte node needs to execute. |

## Execution objects

|       |        |
|-------|--------|
| [`FlyteWorkflowExecution`](./execution-objects.md#flytekit.remote.executions.FlyteWorkflowExecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`FlyteTaskExecution`](./execution-objects.md#flytekit.remote.executions.FlyteTaskExecution) | A class encapsulating a task execution being run on a Flyte remote backend. |
| [`FlyteNodeExecution`](./execution-objects.md#flytekit.remote.executions.FlyteNodeExecution) | A class encapsulating a node execution being run on a Flyte remote backend. |