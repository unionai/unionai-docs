# Overriding parameters

Every task execution in Union occurs within a parameter context that defines various aspects of the [task parameters](../core-concepts/tasks/task-hardware-environment) and [software environment](../core-concepts/tasks/task-software-environment).

The parameter settings for a given execution are defined by a cascading set of configurations starting at the global level and proceeding through the project, workflow definition, task definition, and task invocation levels, with each level potentially overriding settings from the previous level.

In this section we will explain the parameters involved and how they are inherited and overridden.

To begin, let's take a look at which parameters we are talking about.

## Parameters

The parameters that are inherited and (potentially) overridden are the *execution settings and resource quotas* that govern the hardware and software environment within which a task is executed and other aspects of execution behavior. They are:

### Execution settings

* `container_image`: Specify a [container image](../core-concepts/tasks/task-software-environment/imagespec).

* `requests`: (Resources object) Specify [resource requests](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
    * `cpu`: (name) Specify the CPU request.
    * `gpu`: (name) Specify the GPU request.
    * `memory`: (amount) Specify the memory request.
    * `storage`: (amount) Specify the storage request.
    * `ephemeral_storage`: (amount) Specify the ephemeral storage request.
* `limits`: (Resources object) Specify [resource limits](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
    * `cpu`: (name) Specify the CPU request.
    * `gpu`: (name) Specify the GPU request.
    * `memory`: (amount) Specify the memory request.
    * `storage`: (amount) Specify the storage request.
    * `ephemeral_storage`: (amount) Specify the ephemeral storage request.
* `accelerator`: (name) Specify [accelerators](../core-concepts/tasks/task-hardware-environment/accelerators).
* `interruptible`: (boolean) Specify whether the task is [interruptible](../core-concepts/tasks/task-hardware-environment/interruptible-instances).

* `name`: (string) Give a specific name to this task execution. This will appear in the workflow flowchart in the UI (see [below](#using-with_overrides-with-name-and-node_name).
* `node_name`: (string) Give a specific name to the DAG node for this task. This will appear in the workflow flowchart in the UI (see [below](#using-with_overrides-with-name-and-node_name)).

* `cache`: (boolean) Enable [caching](../core-concepts/caching).
* `cache_version`: (string) Specify the [cache version](../core-concepts/caching).
* `cache_serialize`: (boolean) Enable [cache serialization](../core-concepts/caching).
* (from Task parameters page) `cache_ignore_input_vars`: (boolean) Input variables that should not be included when calculating the hash for the cache.

* (from Task parameters page) `secret_requests`: (Secrets object) See Managing secrets

* `retries`: (number) Specify the [number of times to retry this task](../core-concepts/tasks/task-parameters.md#retries).
* `timeout`: (time-period) Specify the [task timeout](../core-concepts/tasks/task-parameters.md#timeout).*

* `task_config`:(object) Specify a [task config](../core-concepts/tasks/task-parameters.md#task_config).
* (from Task parameters page) `task_resolver`: (object) Provide a custom task resolver.
* (from Task parameters page) `pod_template`: (object) See Task hardware environment.
* (from Task parameters page) `pod_template_name`: (string) See Task hardware environment.

* (from Task parameters page) `enable_deck`: (boolean) If true, this task will output a Flyte Deck which can be used to visualize the task execution (see Decks⬀).
* (from Task parameters page) `node_dependency_hints`: (list) A list of tasks, launch plans, or workflows that this task depends on. This is only for dynamic tasks/workflows, where Union cannot automatically determine the dependencies prior to runtime. Even on dynamic tasks this is optional, but in some scenarios it will make registering the workflow easier, because it allows registration to be done the same as for static tasks/workflows. For example this is useful to run launch plans dynamically, because launch plans must be registered on Flyteadmin before they can be run. Tasks and workflows do not have this requirement.
* (from Task parameters page) `deprecated`: (string) A string that can be used to provide a warning message for deprecated task. Absence / empty str indicates that the task is active and not deprecated
* (from Task parameters page) `docs`: (string) Documentation about this task.

### Resource quotas

(from UI)

* **Memory quota**: Default namespace memory quota. The sum of all concurrent task memory limits cannot exceed this value
* **CPU quota**: Default namespace CPU quota. The sum of all concurrent task CPU limits cannot exceed this value.
* **GPU quota**: Default namespace GPU quota. The total number of currently active GPUs cannot exceed this value.

## Notes

> So, if the Organization scope is equivalent to the Global scope, and the same parameters can be set, can we just omit Global from the story?
> It is an implementaion detail. The ultimate default settings are, in effect, the default Organization settings.

These levels can be separated into two groups. 1. Global and Domain. 2. Organization, Project, and Project-Domain.
The first group is default from us, and the second group can be configured by users.
So will it be easier for users to understand if we just hide the first group and say there are defaults?

> So the set of parameters governed by Global and the set governed by Domain are disjoint.
> There are no parameters in common (otherwise one would have to override the other).
> Is this correct?
Yes it is correct.
Currently, `Cluster Resource Attributes` and `Cluster Assignment` are in the Domain level and
`Task Resource Attributes`, `Workflow Execution Config`, and `External Resource Attributes` are in the Global level.

I think the reason we want to have the Domain level is that we want to provide Domain-to-Cluster mapping for multi-cluster users.

IMO, right now users are able to set organization level setting (they couldn't in the past),
most of the users don't have to ask us to change the default unless they are using Domain-to-Cluster mapping for multi-cluster.

## Scopes

Global: default={a, b, c}
Domain(d): default={d, e, f}
Org(o): override={a, b, c, d, e, f}
Project(p): {a, b, c, d, e, f}
Project(p)+Domain(d): {a, b, c, d, e, f}
TaskDef(t): {a, b, c, d, e, f}
TaskOverride(to): {a, b, c, d, e, f}

## Inheritance

Global -> Org -> Project -> Project+Domain -> TaskDef -> TaskOverride
Domain ---^

## Task Resource Attributes

```{code-block} proto
message TaskResourceSpec {
  string cpu = 1;
  string gpu = 2;
  string memory = 3;
  string storage = 4;
  string ephemeral_storage = 5;
}
```

## Workflow Execution Config

```{code-block} proto
message WorkflowExecutionConfig {
  // Can be used to control the number of parallel nodes to run within the workflow. This is useful to achieve fairness.
  int32 max_parallelism = 1;

  // Indicates security context permissions for executions triggered with this matchable attribute.
  core.SecurityContext security_context = 2;

  // Encapsulates user settings pertaining to offloaded data (i.e. Blobs, Schema, query data, etc.).
  RawOutputDataConfig raw_output_data_config = 3;

  // Custom labels to be applied to a triggered execution resource.
  Labels labels = 4;

  // Custom annotations to be applied to a triggered execution resource.
  Annotations annotations = 5;

  // Allows for the interruptible flag of a workflow to be overwritten for a single execution.
  // Omitting this field uses the workflow's value as a default.
  // As we need to distinguish between the field not being provided and its default value false, we have to use a wrapper
  // around the bool field.
  google.protobuf.BoolValue interruptible = 6;

  // Allows for all cached values of a workflow and its tasks to be overwritten for a single execution.
  // If enabled, all calculations are performed even if cached results would be available, overwriting the stored
  // data once execution finishes successfully.
  bool overwrite_cache = 7;

  // Environment variables to be set for the execution.
  Envs envs = 8;

  // Execution environment assignments to be set for the execution.
  repeated core.ExecutionEnvAssignment execution_env_assignments = 9;
}
```

## External Resource Attributes

```{code-block} proto
message ExternalResourceAttributes {
  // Connections here is used by the agent to connect to external systems.
  map<string, core.Connection> connections = 1;
}
```

## Cluster Resource Attributes

```{code-block} proto
message ClusterResourceAttributes {
  // Custom resource attributes which will be applied in cluster resource creation (e.g. quotas).
  // Map keys are the *case-sensitive* names of variables in templatized resource files.
  // Map values should be the custom values which get substituted during resource creation.
  map<string, string> attributes = 1;
}
```

## Cluster Assignment

```{code-block} proto
```

## with_overrides

The `with_overrides` method allows you to specify parameter overrides on [tasks](../core-concepts/tasks/index),
[subworkflows, and sub-launch plans](../core-concepts/workflows/subworkflows-and-sub-launch-plans) at execution time.
This is useful when you want to change the behavior of a task, subworkflow, or sub-launch plan without modifying the original definition.

## Task parameters

When calling a task, you can specify the following parameters in `with_overrides`:

* `accelerator`: Specify [accelerators](../core-concepts/tasks/task-hardware-environment/accelerators).
* `cache_serialize`: Enable [cache serialization](../core-concepts/caching).
* `cache_version`: Specify the [cache version](../core-concepts/caching).
* `cache`: Enable [caching](../core-concepts/caching).
* `container_image`: Specify a [container image](../core-concepts/tasks/task-software-environment/imagespec).
* `interruptible`: Specify whether the task is [interruptible](../core-concepts/tasks/task-hardware-environment/interruptible-instances).
* `limits`: Specify [resource limits](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
* `name`: Give a specific name to this task execution. This will appear in the workflow flowchart in the UI (see [below](#using-with_overrides-with-name-and-node_name).
* `node_name`: Give a specific name to the DAG node for this task. This will appear in the workflow flowchart in the UI (see [below](#using-with_overrides-with-name-and-node_name)).
* `requests`: Specify [resource requests](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
* `retries`: Specify the [number of times to retry this task](../core-concepts/tasks/task-parameters.md#retries).
* `task_config`: Specify a [task config](../core-concepts/tasks/task-parameters.md#task_config).
* `timeout`: Specify the [task timeout](../core-concepts/tasks/task-parameters.md#timeout).

For example, if you have a task that does not have caching enabled, you can use `with_overrides` to enable caching at execution time as follows:

```python
my_task(a=1, b=2, c=3).with_overrides(cache=True)
```

### Using `with_overrides` with `name` and `node_name`

Using `with_overrides` with `name` on a task is a particularly useful feature.
For example, you can use `with_overrides(name="my_task")` to give a specific name to a task execution, which will appear in the UI.
The name specified can be chosen or generated at invocation time without modifying the task definition.

```python
@workflow
def wf() -> int:
    my_task(a=1, b=1, c=1).with_overrides(name="my_task_1")
    my_task(a=2, b=2, c=2).with_overrides(name="my_task_2", node_name="my_node_2")
    return my_task(a=1, b=1, c=1)
```

The above code would produce the following workflow display in the UI:

![Overriding name](/_static/images/user-guide/development-cycle/overriding-parameters/override-name.png)

There is also a related parameter called `node_name` that can be used to give a specific name to the DAG node for this task.
The DAG node name is usually autogenerated as `n0`, `n1`, `n2`, etc. It appears in the `node` column of the workflow table.
Overriding `node_name` results in the autogenerated name being replaced by the specified name:

![Overriding node name](/_static/images/user-guide/development-cycle/overriding-parameters/override-node-name.png)

Note that the `node_name` was specified as `my_node_2` in the code but appears as `my_node_2` in the UI. This is to the fact that Kubernetes node names cannot contain underscores. Union automatically alters the name to be Kubernetes-compliant.

## Subworkflow and sub-launch plan parameters

When calling a workflow or launch plan from within a high-level workflow
(in other words, when invoking a subworkflow or sub-launch plan),
you can specify the following parameters in `with_overrides`:

* `cache_serialize`: Enable [cache serialization](../core-concepts/caching).
* `cache_version`: Specify the [cache version](../core-concepts/caching).
* `cache`: Enable [caching](../core-concepts/caching).
