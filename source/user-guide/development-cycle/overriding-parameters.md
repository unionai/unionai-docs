# Overriding parameters

Every task execution in Union occurs within a parameter context that defines various aspects of the [task parameters](../core-concepts/tasks/task-hardware-environment) and [software environment](../core-concepts/tasks/task-software-environment).

The parameter settings for a given execution are defined by a cascading set of configurations starting at the global level and proceeding through the project, workflow definition, task definition, and task invocation levels, with each level potentially overriding settings from the previous level.

In this section we will explain the parameters involved and how they are inherited and overridden.

To begin, let's take a look at which parameters we are talking about.

## Parameters

The parameters that are inherited and (potentially) overridden are the *execution settings and resource quotas* that govern the hardware and software environment within which a task is executed and other aspects of execution behavior. They are:

### Execution settings

* `container_image`: Specify a [container image](../core-concepts/tasks/task-software-environment/imagespec).

* `requests`: Specify [resource requests](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).
* `limits`: Specify [resource limits](../core-concepts/tasks/task-hardware-environment/customizing-task-resources).

* `accelerator`: Specify [accelerators](../core-concepts/tasks/task-hardware-environment/accelerators).
* `interruptible`: Specify whether the task is [interruptible](../core-concepts/tasks/task-hardware-environment/interruptible-instances).

* `name`: Give a specific name to this task execution. This will appear in the workflow flowchart in the UI (see [below](#using-with_overrides-with-name-and-node_name).
* `node_name`: Give a specific name to the DAG node for this task. This will appear in the workflow flowchart in the UI (see [below](#using-with_overrides-with-name-and-node_name)).

* `cache`: Enable [caching](../core-concepts/caching).
* `cache_version`: Specify the [cache version](../core-concepts/caching).
* `cache_serialize`: Enable [cache serialization](../core-concepts/caching).
* (from Task parameters page) `cache_ignore_input_vars`: Input variables that should not be included when calculating the hash for the cache.

* (from Task parameters page) `secret_requests`: See Managing secrets

* `retries`: Specify the [number of times to retry this task](../core-concepts/tasks/task-parameters.md#retries).
* `timeout`: Specify the [task timeout](../core-concepts/tasks/task-parameters.md#timeout).*

* `task_config`: Specify a [task config](../core-concepts/tasks/task-parameters.md#task_config).
* (from Task parameters page) `task_resolver`: Provide a custom task resolver.
* (from Task parameters page) `pod_template`: See Task hardware environment.
* (from Task parameters page) `pod_template_name`: See Task hardware environment.

* (from Task parameters page) `enable_deck`: If true, this task will output a Flyte Deck which can be used to visualize the task execution (see Decks⬀).
* (from Task parameters page) `node_dependency_hints`: A list of tasks, launch plans, or workflows that this task depends on. This is only for dynamic tasks/workflows, where Union cannot automatically determine the dependencies prior to runtime. Even on dynamic tasks this is optional, but in some scenarios it will make registering the workflow easier, because it allows registration to be done the same as for static tasks/workflows. For example this is useful to run launch plans dynamically, because launch plans must be registered on Flyteadmin before they can be run. Tasks and workflows do not have this requirement.
* (from Task parameters page) `deprecated`: A string that can be used to provide a warning message for deprecated task. Absence / empty str indicates that the task is active and not deprecated
* (from Task parameters page) `docs`: Documentation about this task.

### Resource quotas

(from UI)

* **Memory quota**: Default namespace memory quota. The sum of all concurrent task memory limits cannot exceed this value
* **CPU quota**: Default namespace CPU quota. The sum of all concurrent task CPU limits cannot exceed this value.
* **GPU quota**: Default namespace GPU quota. The total number of currently active GPUs cannot exceed this value.



## Scopes

Global: {a, b, c}
Domain(name): {d, e, f}
Org(name): {a, b, c, d, e, f}
Org(name)+ Domain(name): {d, e, f}
Project(name): {a, b, c, d, e, f}
Project(name) + Domain(name): {a, b, c, d, e, f}
TaskDef(name): {a, b, c, d, e, f}
TaskOverride(name): {a, b, c, d, e, f}


## Inheritance


Global -> Org -> Org+Domain -> Project -> Project+Domain -> TaskDef -> TaskOverride
Domain ---^








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
