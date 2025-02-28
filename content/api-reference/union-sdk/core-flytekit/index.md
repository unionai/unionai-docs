# Core flytekit

This package contains the most common abstractions you'll need to write Flyte workflows and extend flytekit.

## Basic authoring

```{eval-rst}

.. currentmodule:: flytekit

These are the essentials needed to get started writing tasks and workflows.

.. autosummary::
   :nosignatures:

   task
   workflow
   kwtypes
   current_context
   ExecutionParameters
   FlyteContext
   ~core.array_node_map_task.map_task
   ~core.workflow.ImperativeWorkflow
   ~core.node_creation.create_node
   ~core.promise.NodeOutput
   FlyteContextManager
```


```{note}
Tasks and workflows can both be locally run, assuming the relevant tasks are capable of local execution.
This is useful for unit testing.
```

## Branching and conditionals

Branches and conditionals can be expressed explicitly in Flyte. These conditions are evaluated
in the flyte engine and hence should be used for control flow. [Dynamic workflows](./dynamic-and-nested-workflows.md) can be used to perform custom conditional logic not supported by flytekit.

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   conditional
```

## Customizing Tasks & Workflows

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   TaskMetadata - Wrapper object that allows users to specify Task
   Resources - Things like CPUs/Memory, etc.
   WorkflowFailurePolicy - Customizes what happens when a workflow fails.
   PodTemplate - Custom PodTemplate for a task.
```

## Dynamic and nested workflows

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   dynamic
```

## Signaling

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   approve
   sleep
   wait_for_input
```

## Scheduling

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   CronSchedule
   FixedRate
```

## Notifications

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   Email
   PagerDuty
   Slack
```

## Reference entities

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   get_reference_entity
   LaunchPlanReference
   TaskReference
   WorkflowReference
   reference_task
   reference_workflow
   reference_launch_plan
```

## Core task types

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   SQLTask
   ContainerTask
   PythonFunctionTask
   PythonInstanceTask
   LaunchPlan
```

## Secrets and SecurityContext

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   Secret
   SecurityContext
```

## Common Flyte IDL Objects

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   AuthRole
   Labels
   Annotations
   WorkflowExecutionPhase
   Blob
   BlobMetadata
   Literal
   Scalar
   LiteralType
   BlobType
```

## Task utilities

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   HashMethod
```

## Artifacts

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   Artifact
```

## Documentation

```{eval-rst}

.. currentmodule:: flytekit

.. autosummary::
   :nosignatures:

   Description
   Documentation
   SourceCode
```