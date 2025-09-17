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

