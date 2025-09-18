---
title: Multiple environments
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
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

To use multiple environments in your workfow you define multiple `TaskEnvironment` instances, each with its own configuration, and then assign tasks to the appropriate environment.

There are, however, two additional constraints that you must take into account:

1. If a task in one environment calls a task in another environment, the environment of the calling task must declare a deployment-time dependency on the environment of the called task using the `depends_on` parameter of `TaskEnvironment`.
2. The environment of the calling task must include all dependencies declared in the environment of the called task (unless remote tasks are used)

### Task `depends_on` constraints

The `depends_on` parameter in `TaskEnvironment` is used to provide deployment-time dependencies by establishing a relationship between one `TaskEnvironment` and another.
The system uses this information to determine which environments (and, specifically which images) need to be built in order to be able to run the code.

On `flyte run` (or `flyte deploy`), the system walks the tree defined by the `depends_on` relationships, starting with the environment of the task being invoked (or the environment being deployed, in the case of `flyte deploy`), and prepares each required environment.
Most importantly, it ensures that the container images need for all required environments are available (and if not, it builds them).

This deploy-time determination of what to build is important because it means that for any given `run` or `deploy`, only those environments that are actually required are built.
The alternative strategy of building all environments defined in the set of deployed code can lead to unnecessary and expensive builds, especially when iterating on code.

### Dependency inclusion constraints

When a parent task invokes a child task in a different environment, the container image of the parent task environment must include all dependencies used by the child task.
This is necessary because of the way task invocation works in Flyte:

- When a child task is invoked by function name, that function, necessarily, has to be imported into the parent tasks's Python environment.
- This results in all the dependencies of the child task function also being imported.
- But, nonetheless, the actual execution of the child task occurs in its own environment.

To avoid this requirement, you can use [remote tasks]() to invoke tasks in other environments without importing them into the parent task's environment.

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
(The source code for this example can be found here:[AlphaFold2 mock example](https://github.com/unionai/unionai-examples/tree/main/user-guide-v2/task-configuration/multiple-environments/af2))

In file `msa/run.py` by defining the task `run_msa`, which mocks the multiple sequence alignment step of the process:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/multiple-environments/af2/msa/run.py" lang="python" >}}

* A dedicated image (`msa_image`) is built using the `MSA_PACKAGES` dependency list, on top of the standard base image.
* A dedicated environment (`msa_env`) is defined for the task, using `msa_image`.
* The task is defined within the context of the `msa_env` environment.

In file `fold/run.py` we define the task `run_fold`, which mocks the fold step of the process:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/multiple-environments/af2/fold/run.py" lang="python" >}}

* A dedicated image (`fold_image`) is built using the `FOLD_PACKAGES` dependency list, on top of the standard base image.
* A dedicated environment (`fold_env`) is defined for the task, using `msa_image`.
* The task is defined within the context of the `fold_env` environment.

Finally, in file `main.py` we define the task `main` that ties everything together into a workflow.

We import the required modules and functions:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/multiple-environments/af2/run_alphafold2.py" fragment=import lang="python" >}}

Notice that we import
* The task functions that we will be calling: `run_fold` and `run_msa`.
* The environments of those tasks: `fold_env` and `msa_env`.
* The dependency list of the `run_msa` task: `MSA_PACKAGES`
* The image of the `run_fold` task: `fold_image`

We then assemble the image and the environment:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/multiple-environments/af2/run_alphafold2.py" fragment=image_and_env lang="python" >}}

The image for the `main` task (`main_image`) is built by starting with `fold_image` (the image for the of the `run_fold` task) and adding `MSA_PACKAGES` (the dependency list for the `run_msa` task).
This ensures that `main_imagfe` includes all dependencies needed by both the `run_fold` and `run_msa` tasks.

The environment for the `main` task is defined with:
* The image `main_image`. This ensures that the `main` task has all the dependencies it needs.
* A depends_on list that includes both `fold_env` and `msa_env`. This establishes the deploy-time dependencies on those environments.

Finally, we define the `main` task itself:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/multiple-environments/af2/run_alphafold2.py" fragment=main_task lang="python">}}

Here we call, in turn, the `run_msa` and `run_fold` tasks.
Note that we call them directly, not as [remote tasks](), which is why we had to ensure that `main_image` includes all dependencies needed by both tasks.

The final piece of the puzzle is the `if __name__ == "__main__":` block that allows us to run the `main` task on the configured Flyte backend:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/multiple-environments/af2/run_alphafold2.py" fragment=run lang="python">}}

Now you can run the workflow with:

```bash
python main.py
```
