---
title: Multiple environments
description: Give different tasks in one workload different images, resources, and configuration.
icon: layers
weight: 7
variants: +flyte +union
---

# Multiple environments

In many applications, different tasks within your workflow may require different configurations.
Flyte enables you to manage this complexity by allowing multiple environments within a single workflow.

Multiple environments are useful when:

- Different tasks in your workflow need different dependencies.
- Some tasks require specific CPU/GPU or memory configurations.
- A task requires a secret that other tasks do not (and you want to limit exposure of the secret value).
- You're integrating specialized tools that have conflicting requirements.

## Constraints on multiple environments

To use multiple environments in your workflow you define multiple `TaskEnvironment` instances, each with its own configuration, and then assign tasks to their respective environments.

There are, however, two additional constraints that you must take into account.
If `task_1` in environment `env_1` calls a `task_2` in environment `env_2`, then:

1. `env_1` must declare a deployment-time dependency on `env_2` in the `depends_on` parameter of `TaskEnvironment` that defines `env_1`.
2. The image used in the `TaskEnvironment` of `env_1` must include the import-time dependencies of the module that defines `task_2` (unless [`task_2` is invoked as a remote task](../task-programming/remote-tasks)).

### Task `depends_on` constraints

The `depends_on` parameter in `TaskEnvironment` is used to provide deployment-time dependencies by establishing a relationship between one `TaskEnvironment` and another.
The system uses this information to determine which environments (and, specifically which images) need to be built in order to be able to run the code.

On `flyte run` (or `flyte deploy`), the system walks the tree defined by the `depends_on` relationships, starting with the environment of the task being invoked (or the environment being deployed, in the case of `flyte deploy`), and prepares each required environment.
Most importantly, it ensures that the container images need for all required environments are available (and if not, it builds them).

This deploy-time determination of what to build is important because it means that for any given `run` or `deploy`, only those environments that are actually required are built.
The alternative strategy of building all environments defined in the set of deployed code can lead to unnecessary and expensive builds, especially when iterating on code.

### Dependency inclusion constraints

When a parent task invokes a child task in a different environment, the container image of the parent task environment must include the import-time dependencies of the module that defines the child task.
This is narrower than every dependency the child task uses.
It is what Python evaluates when the module is imported:

- To invoke a child task by function name, the parent has to import the module that defines it. Importing that module runs the module's top-level statements: its module-level imports, its `Image` and `TaskEnvironment` definitions, and the `@env.task` decoration of each task in it.
- Decorating a task builds its interface, which resolves the type annotations on the task's parameters and return value. Every name in those annotations has to be importable in the parent image.
- The body of the child task function does not run in the parent. The child task still executes in its own environment, using its own image.

So the parent image needs what the child's module imports at the top level, plus what the child task's signature refers to.
It does not need a package that the child task imports inside its function body.

You have two ways to keep a dependency out of the parent image: import it inside the task function, or invoke the child task remotely.

#### Import the dependency inside the task function

If a package is only used in the body of a child task, import it there rather than at module level.

The child task, in `other/run.py`:

```python
import flyte

other_env = flyte.TaskEnvironment(
    name="other_env",
    image=flyte.Image.from_debian_base().with_pip_packages("polars"),
)

@other_env.task
async def row_count(path: str) -> int:
    import polars as pl

    return pl.read_parquet(path).height
```

The parent task, in `main.py`:

```python
import flyte

from other.run import other_env, row_count

env = flyte.TaskEnvironment(
    name="main_env",
    depends_on=[other_env],
    image=flyte.Image.from_debian_base(),
)

@env.task
async def main(path: str) -> int:
    return await row_count(path)
```

The image for `main_env` does not include `polars`, because `other/run.py` imports it inside `row_count` rather than at module level.
Importing `other/run.py` in the parent still works, and `row_count` still runs in `other_env`, where `polars` is installed.

Keep at module level anything that has to resolve when the module is imported:

- Names used in a task's parameter or return annotations. A name imported only in the function body raises `NameError` when the module is imported, including in a module that uses `from __future__ import annotations`.
- Values passed to `TaskEnvironment`, `Image`, or the `@env.task` decorator, such as the package lists used to build an image.

#### Invoke the child task remotely

You can also avoid the requirement by [invoking a task in another environment _remotely_](../task-programming/remote-tasks).
The parent then refers to the child task by name instead of importing it, so the parent image needs nothing from the child's module.

## Example

The following example is a (very) simple mock of an AlphaFold2 pipeline.
It demonstrates a workflow with three tasks, each in its own environment.

The example project looks like this:

```bash
├── msa/
│   ├── __init__.py
│   └── run.py
├── fold/
│   ├── __init__.py
│   └── run.py
├── __init__.py
└── main.py
```

(The source code for this example can be found here:[AlphaFold2 mock example](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/task-configuration/multiple-environments/af2))

In file `msa/run.py` we define the task `run_msa`, which mocks the multiple sequence alignment step of the process:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/multiple-environments/af2/msa/run.py" lang="python" >}}

* A dedicated image (`msa_image`) is built using the `MSA_PACKAGES` dependency list, on top of the standard base image.
* A dedicated environment (`msa_env`) is defined for the task, using `msa_image`.
* The task is defined within the context of the `msa_env` environment.

In file `fold/run.py` we define the task `run_fold`, which mocks the fold step of the process:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/multiple-environments/af2/fold/run.py" lang="python" >}}

* A dedicated image (`fold_image`) is built using the `FOLD_PACKAGES` dependency list, on top of the standard base image.
* A dedicated environment (`fold_env`) is defined for the task, using `fold_image`.
* The task is defined within the context of the `fold_env` environment.

Finally, in file `main.py` we define the task `main` that ties everything together into a workflow.

We import the required modules and functions:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/multiple-environments/af2/main.py" fragment="import" lang="python" >}}

Notice that we import

* The task functions that we will be calling: `run_fold` and `run_msa`.
* The environments of those tasks: `fold_env` and `msa_env`.
* The dependency list of the `run_msa` task: `MSA_PACKAGES`
* The image of the `run_fold` task: `fold_image`

We then assemble the image and the environment:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/multiple-environments/af2/main.py" fragment="image_and_env" lang="python" >}}

The image for the `main` task (`main_image`) is built by starting with `fold_image` (the image for the `run_fold` task) and adding `MSA_PACKAGES` (the dependency list for the `run_msa` task).
This ensures that `main_image` can import `fold/run.py` and `msa/run.py`, whatever those modules import at the top level.

{{< note >}}
In this small example neither `msa/run.py` nor `fold/run.py` actually imports its packages at the top level, so a smaller `main_image` would also run.
Composing the parent image from the child images is the pattern that keeps working once those modules do import their packages at module level, and it saves you working out which ones they are.
{{< /note >}}

The environment for the `main` task is defined with:

* The image `main_image`. This ensures that the `main` task has all the dependencies it needs.
* A depends_on list that includes both `fold_env` and `msa_env`. This establishes the deploy-time dependencies on those environments.

Finally, we define the `main` task itself:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/multiple-environments/af2/main.py" fragment="task" lang="python" >}}

Here we call, in turn, the `run_msa` and `run_fold` tasks.
Since we call them directly rather than as [remote tasks](../task-programming/remote-tasks), `main_image` has to be able to import the modules that define them.

The final piece of the puzzle is the `if __name__ == "__main__":` block that allows us to run the `main` task on the configured Flyte backend:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/multiple-environments/af2/main.py" fragment="run" lang="python" >}}

Now you can run the workflow with:

```bash
python main.py
```
