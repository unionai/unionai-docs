---
title: How task deployment works
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# How task deployment works

In this section, we will take a deep dive into how the `flyte deploy` command and the `flyte.deploy()` SDK function work under the hood to deploy tasks to your Flyte backend.

When you perform a deployment, here's what happens:

## 1. Module loading and task environment discovery

In the first step, Flyte determines which files to load in order to search for task environments, based on the command line options provided:

### Single file (default)

```bash
flyte deploy my_example.py env
```

- The file `my_example.py` is executed,
- All declared `TaskEnvironment` objects in the file are instantiated,
  but only the one assigned to the variable `env` is selected for deployment.

### `--all` option

```bash
flyte deploy --all my_example.py
```
- The file `my_example.py` is executed,
- All declared `TaskEnvironment` objects in the file are instantiated and selected for deployment.
- No specific variable name is required.

### `--recursive` option

```bash
flyte deploy --recursive ./directory
```

- The directory is recursively traversed and all Python files are executed and all `TaskEnvironment` objects are instantiated.
- All `TaskEnvironment` objects across all files are selected for deployment.

## 2. Task analysis and serialization

- For every task environment selected for deployment, all of its tasks are identified.
- Task metadata is extracted: parameter types, return types, and resource requirements.
- Each task is serialized into a Flyte `TaskTemplate`.
- Dependency graphs between environments are built (see below).

## 3. Task environment dependency resolution

In many cases, a task in one environment may invoke a task in another environment, establishing a dependency between the two environments.
For example, if `env_a` has a task that calls a task in `env_b`, then `env_a` depends on `env_b`.
This means that when deploying `env_a`, `env_b` must also be deployed to ensure that all tasks can be executed correctly.

To handle this, `TaskEnvironment`s can declare dependencies on other `TaskEnvironment`s using the `depends_on` parameter.
During deployment, the system performs the following steps to resolve these dependencies:

1. Starting with specified environment(s)
2. Recursively discovering all transitive dependencies
3. Including all dependencies in the deployment plan
4. Processing dependencies depth-first to ensure correct order

```python
# Define environments with dependencies
prep_env = flyte.TaskEnvironment(name="preprocessing")
ml_env = flyte.TaskEnvironment(name="ml_training", depends_on=[prep_env])
viz_env = flyte.TaskEnvironment(name="visualization", depends_on=[ml_env])

# Deploy only viz_env - automatically includes ml_env and prep_env
deployment = flyte.deploy(viz_env, version="v2.0.0")

# Or deploy multiple environments explicitly
deployment = flyte.deploy(data_env, ml_env, viz_env, version="v2.0.0")
```

For detailed information about working with multiple environments, see [Multiple Environments](../task-configuration/multiple-environments).

## 4. Code bundle creation and upload

Once the task environments and their dependencies are resolved, Flyte proceeds to package your code into a bundle based on the `copy_style` option:

### `--copy_style loaded_modules` (default)

This is the smart bundling approach that analyzes which Python modules were actually imported during the task environment discovery phase.
It examines the runtime module registry (`sys.modules`) and includes only those modules that meet specific criteria:
they must have source files located within your project directory (not in system locations like `site-packages`), and they must not be part of the Flyte SDK itself.
This selective approach results in smaller, faster-to-upload bundles that contain exactly the code needed to run your tasks, making it ideal for most development and production scenarios.

### `--copy_style all`

This comprehensive bundling strategy takes a directory-walking approach, recursively traversing your entire project directory and including every file it encounters.
Unlike the smart bundling that only includes imported Python modules, this method captures all project files regardless of whether they were imported during discovery.
This is particularly useful for projects that use dynamic imports, load configuration files or data assets at runtime, or have dependencies that aren't captured through normal Python import mechanisms.

### `--copy_style none`

This option completely skips code bundle creation, meaning no source code is packaged or uploaded to cloud storage.
When using this approach, you must provide an explicit version parameter since there's no code bundle to generate a version from.
This strategy is designed for scenarios where your code is already baked into custom container images, eliminating the need for separate code injection during task execution.
It results in the fastest deployment times but requires more complex image management workflows.

### `--root-dir` option

By default, Flyte uses your current working directory as the root for code bundling.
You can override this with `--root-dir` to specify a different base directory - particularly useful for monorepos or when deploying from subdirectories. This affects all copy styles: `loaded_modules` will look for imported modules relative to the root directory, `all` will walk the directory tree starting from the root, and the root directory setting works with any copy style. See the [Deploy command options](./deploy-command-options#--root-dir) for detailed usage examples.

After the code bundle is created (if applicable), it is uploaded to a cloud storage location (like S3 or GCS) accessible by your Flyte backend. It is now ready to be run.

## 5. Image building

If your `TaskEnvironment` specifies [custom images](../task-configuration/container-images), Flyte builds and pushes container images before deploying tasks.
The build process varies based on your configuration and backend type:

### Local image building

When `image.builder` is set to `local` in [your `config.yaml`](../getting-started/local-setup), images are built on your local machine using Docker. This approach:
- Requires Docker to be installed and running on your development machine
- Uses Docker BuildKit to build images from generated Dockerfiles or your custom Dockerfile
- Pushes built images to the container registry specified in your `Image` configuration
- Is the only option available for Flyte OSS instances

### Remote image building

When `image.builder` is set to `remote` in [your `config.yaml`](../getting-started/local-setup), images are built on cloud infrastructure. This approach:
- Builds images using Union's ImageBuilder service (currently only available for Union backends, not OSS Flyte)
- Requires no local Docker installation or configuration
- Can push to Union's internal registry or external registries you specify
- Provides faster, more consistent builds by leveraging cloud resources

> [!NOTE]
> Remote building is currently exclusive to Union backends. OSS Flyte installations must use `local`

## Understanding option relationships

It's important to understand how the various deployment options work together.
The **discovery options** (`--recursive` and `--all`) operate independently of the **bundling options** (`--copy-style`),
giving you flexibility in how you structure your deployments.

Environment discovery determines which files Flyte will examine to find `TaskEnvironment` objects,
while code bundling controls what gets packaged and uploaded for execution.
You can freely combine these approaches.
For example, discovering environments recursively across your entire project while using smart bundling to include only the necessary code modules.

When multiple environments are discovered, they all share the same code bundle, which is efficient for related services or components that use common dependencies:

```bash
# All discovered environments share the same code bundle
flyte deploy --recursive --copy-style loaded_modules ./project
```

For a full overview of all deployment options, see [Deploy command options](/api-reference/flyte-cli#flyte-deploy).
