# Core concepts

Union is a platform for building and orchestrating the execution of interconnected software processes across machines in a computer cluster.
In Union terminology, the software processes are called *tasks* and the overall organization of connections between tasks is called a *workflow*.
The tasks in a workflow are connected to each other by their inputs and outputs. The output of one task becomes the input of another.

More precisely, a workflow in Union is a *directed acyclic graph (DAG)* of *nodes* where each node is a unit of execution and the edges between nodes represent the flow of data between them.
The most common type of node is a task node (which encapsulates a task), though the are also workflow node (which encapsulate subworkflows) and branch nodes.
In most contexts we just say that a workflow is a DAG of tasks.

You define tasks and workflows in Python using the Flytekit SDK. The Flytekit SDK provides a set of decorators and classes that allow you to define tasks and workflows in a way that is easy to understand and work with.
Once defined, tasks and workflows are deployed to your Union instance (we say they are *registered* to the instance), where they are compiled into a form that can be executed on your Union cluster.

In addition to tasks and workflows, another important concept in Union is the [*launch plan*](launch-plans/index).
A launch plan is like a template that can be used to define the inputs to a workflow.
Triggering a launch plan will launch its associated workflow with the specified parameters.

## Defining tasks and workflows

Using the Flytekit SDK, tasks and workflows are defined as Python functions using the `@task` and `@workflow` decorators, respectively:

**`./workflows/my_example.py`**
```{code-block} python
from flytekit import task, workflow

@task
def task_1(a: int, b: int, c: int) -> int:
    return a + b + c

@task
def task_2(m: int, n: int) -> int:
    return m * n

@task
def task_3(x: int, y: int) -> int:
    return x - y

@workflow
def my_workflow(a: int, b: int, c: int, m: int, n: int) -> int:
    x = task_1(a=a, b=b, c=c)
    y = task_2(m=m, n=n)
    return task_3(x=x, y=y)
```

Here we see three tasks defined using the `@task` decorator and a workflow defined using the `@workflow` decorator.
The workflow calls `task_1` and `task_2` and passes the results to `task_3` before finally outputting the result of `task_3`.

When the workflow is registered, Union compiles the workflow into a directed acyclic graph (DAG) based on the input/output dependencies between the tasks.
The DAG is then used to execute the tasks in the correct order, taking advantage of any parallelism that is possible.
For example, the workflow above results in the following DAG:

![Workflow DAG](/_static/images/concepts-workflows-1.png)

### Type annotation is required

One important difference between Union and generic Python is that in Union all inputs and outputs *must be type annotated*.
This is because tasks are strongly typed(/todo), meaning that the types of the inputs and outputs are validated at deployment time.

See [Tasks are strongly typed](tasks/index.md#tasks-are-strongly-typed) for more details.

### Workflows *are not* full Python functions

The definition of a workflow must be a valid Python function, so it can be run locally as a normal Python function during development,
but only *a subset of Python syntax is allowed*, because it must also be compiled into a DAG that is deployed and executed on Union.

*Technically then, the language of a workflow function is a domain-specific language (DSL) that is a subset of Python.*

See [Workflows](workflows/index) for more details.

## Registering tasks and workflows

### Registering on the command line with `pyflyte` or `uctl`

In most cases, workflows and tasks (and possibly other things, such as launch plans) are defined in your project code and registered as a bundle using `pyflyte` or `uctl` For example:

```{code-block} shell
pyflyte register ./workflows --project my_project --domain development
```

Tasks can also be registered individually, but it is more common to register alongside the workflow that uses them.

See [Registering workflows](../development-cycle/registering-workflows).

### Registering in Python with `FlyteRemote`

As with all Union command line actions, you can also perform registration of workflows and tasks programmatically with [`FlyteRemote`](https://docs.flyte.org/en/latest/api/flytekit/design/control_plane.html), specifically, [`FlyteRemote.register_script`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.register_script),
[`FlyteRemote.register_workflow`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.register_workflow), and
[`FlyteRemote.register_task`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.register_task).

## Results of registration

When the code above is registered to Union, it results in the creation of five objects:

* The tasks `workflows.my_example.task_1`, `workflows.my_example.task_2`, and `workflows.my_example.task_3` (see [Task fundamentals](tasks/index) for more details).
* The workflow `workflows.my_example.my_workflow`.
* The default launch plan `workflows.my_example.my_workflow` (see [Launch plans](launch-plans/index) for more details).

Notice that the task and workflow names are derived from the path, file name and function name of the Python code that defines them: `<folder>.<file>.<function>`.
The default launch plan for a workflow always has the same name as its workflow.

## Changing tasks and workflows

Tasks and workflows are changed by altering their definition in code and re-registering.
When a task or workflow with the same project, domain, and name as a preexisting one is re-registered, a new version of that entity is created.

## Inspecting tasks and workflows

### Inspecting workflows in the Union console

Select **Workflows** in the sidebar to display a list of all the registered workflows in the project and domain:

![Workflow list](/_static/images/concepts-workflows-2.png)

You can search the workflows by name.

Click on a workflow in the list to see the workflow view:

![Workflow view](/_static/images/concepts-workflows-3.png)

The sections in the workflow view are as follows:

#### Recent Workflow Versions

A list of recent versions of this workflow. Select a version to see the **Workflow version view**:

![Workflow version view](/_static/images/concepts-workflows-4.png)

This view shows the DAG and a list of all version of the task. You can switch between versions with the radio buttons.

#### All Executions in the Workflow

A list of all executions of this workflow. Click on an execution to go to the execution view.

#### Launch Workflow button

In the top right of the workflow view, you can click the **Launch Workflow** button to run the task with the default inputs.

### Inspecting tasks in the Union console

Select **Tasks** in the sidebar to display a list of all the registered tasks in the project and domain:

![Task list](/_static/images/concepts-tasks-1.png)

You can search the launch plans by name.
To filter for only those that are archived, check the **Show Only Archived Tasks** box.

Click on a task in the list to see the task view:

![Task view](/_static/images/concepts-tasks-2.png)

The sections in the task view are as follows:

#### Inputs & Outputs

The name and type of each input and output for the latest version of this task.

#### Recent Task Versions

A list of recent versions of this task. Select a version to see the **Task version view**:

![Task version view](/_static/images/concepts-tasks-3.png)

This view shows the task details and a list of all version of the task. You can switch between versions with the radio buttons.
See [Tasks](tasks/index) for more information.

#### All Executions in the Task

A list of all executions of this task. Click on an execution to go to the execution view.

#### Launch Task button

In the top right of the task view, you can click the **Launch Task** button to run the task with the default inputs.

### Inspecting workflows on the command line with `uctl`

To view all tasks within a project and domain:

```{code-block} shell
$ uctl get workflows \
       --project <project-id> \
       --domain <domain>
```

To view a specific workflow:

```{code-block} shell
$ uctl get workflow \
       --project <project-id> \
       --domain <domain> \
       <workflow-name>
       <workflow-version>
```

<!-- TODO add back when uctl reference exists
See the [`uctl` reference]() for more details.
-->

### Inspecting tasks on the command line with `uctl`

To view all tasks within a project and domain:

```{code-block} shell
$ uctl get tasks \
       --project <project-id> \
       --domain <domain>
```

To view a specific task:

```{code-block} shell
$ uctl get task \
       --project <project-id> \
       --domain <domain> \
       <task-name>
       <task-version>
```

<!-- TODO add back when uctl reference exists
See the [`uctl` reference]() for more details.
-->

### Inspecting tasks and workflows in Python with `FlyteRemote`

Use the method [`FlyteRemote.fetch_workflow`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.fetch_workflow) or [`FlyteRemote.client.get_workflow`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.clients.friendly.SynchronousFlyteClient.html#flytekit.clients.friendly.SynchronousFlyteClient.get_workflow) to get a workflow.
See [FlyteRemote](https://docs.flyte.org/en/latest/api/flytekit/design/control_plane.html) for more options and details.

Use the method [`FlyteRemote.fetch_task`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.fetch_task) or [`FlyteRemote.client.get_task`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.clients.friendly.SynchronousFlyteClient.html#flytekit.clients.friendly.SynchronousFlyteClient.get_task) to get a task.
See [FlyteRemote](https://docs.flyte.org/en/latest/api/flytekit/design/control_plane.html) for more options and details.

## Running tasks and workflows

### Running a task or workflow in the Union console

To run a workflow in the Union console, click the **Launch Workflow** button in the workflow view.

You can also run individual tasks in the Union console by clicking the **Launch Task** button in the task view.

### Running a task or workflow locally on the command line with `pyflyte` or `python`

You can execute a Flyte workflow or task locally simply by calling it just like any regular Python function.
For example, you can add the following to the above code:

```{code-block} python
if __name__ == "__main__":
   my_workflow(a=1, b=2, c=3, m=4, n=5)
```

If the file is saved as `my_example.py`, you can run it locally using the following command:

```{code-block} shell
$ python my_example.py
```

Alternatively, you can run the task locally with the `flytekit` command line tool `pyflyte`:

To run it locally, you can use the following `pyflyte run` command:

```{code-block} shell
$ pyflyte run my_example.py my_workflow --a 1 --b 2 --c 3 --m 4 --n 5
```

This has the advantage of allowing you to specify the input values as command line arguments.
For more details on running workflows and tasks, see [Development cycle](../development-cycle/index).

### Running a task or workflow remotely on the command line with `pyflyte`

To run a workflow remotely on your Union installation, use the following command (this assumes that you have your [FLYTECTL_CONFIG set up correctly](../getting-started/setting-up-the-project-on-union)):

```{code-block} shell
$ pyflyte run --remote my_example.py my_workflow --a 1 --b 2 --c 3 --m 4 --n 5
```

### Running a task or workflow remotely in Python with `FlyteRemote`

To run a workflow remotely in Python, use the method [`FlyteRemote.execute`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.execute). See [FlyteRemote](https://docs.flyte.org/en/latest/api/flytekit/design/control_plane.html) for more options and details.

To run a task remotely in Python, use the method [`FlyteRemote.execute`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.execute). See [FlyteRemote](https://docs.flyte.org/en/latest/api/flytekit/design/control_plane.html) for more options and details.
