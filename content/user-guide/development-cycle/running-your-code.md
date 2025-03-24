---
title: Running your code
weight: 8
variants: +flyte +serverless +byoc +byok
---

# Running your code

## Set up your development environment

If you have not already done so, follow the [Getting started](../getting-started) section to sign in to {{< key product_name >}}, and set up your local environment.

## CLI commands for running your code

The {{< key cli_name >}} CLI and {{<key ctl_name >}} CLI provide commands that allow you to deploy and run your code at different stages of the development cycle:

<!-- TODO: Link to the union commands below to the reference section -->

1. `{{< key cli >}} run`: For deploying and running a single script immediately in your local Python environment.
2. `{{< key cli >}} run --remote`: For deploying and running a single script immediately in the cloud on {{< key product_name >}}.
3. `{{< key cli >}} register`: For deploying multiple scripts to {{< key product_name >}} and running them from the Web interface.

4. `{{< key cli >}} package` and `{{<key ctl >}} register`: For deploying workflows to production and for scripting within a CI/CD pipeline.

> [!NOTE]
> In some cases, you may want to test your code in a local cluster before deploying it to {{< key product_name >}}.
> This step corresponds to using the commands 2, 3, or 4, but targeting your local cluster instead of {{< key product_name >}}.
> For more details, see [Running in a local cluster](./running-in-a-local-cluster).

{{< variant flyte >}}
{{< markdown >}}

## Registration pattern summary

The following diagram provides a summarized view of the different registration patterns:

![Registration patterns](/_static/images/user-guide/development-cycle/running-your-code/registration-patterns.png)

{{< /markdown >}}
{{< /variant >}}

## Running a script in local Python with `{{< key cli >}} run`

During the development cycle you will want to run a specific workflow or task in your local Python environment to test it.
To quickly try out the code locally use `{{< key cli >}} run`:

```shell
$ {{< key cli >}} run workflows/example.py wf --name 'Albert'
```

Here you are invoking `{{< key cli >}} run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `name` and its value.

This command is useful for quickly testing a workflow locally to check for basic errors.
For more details see [{{< key cli >}} run details](./details-of-union-run).

## Running a script on {{< key product_name >}} with `{{< key cli >}} run --remote`

To quickly run a workflow on {{< key product_name >}}, use `{{< key cli >}} run --remote`:

```shell
$ {{< key cli >}} run --remote --project basic-example --domain development workflows/example.py wf --name 'Albert'
```

Here we are invoking `{{< key cli >}} run --remote` and passing:
* The project, `basic-example`
* The domain, `development`
* The Python file, `workflows/example.py`
* The workflow within that file that you want to run, `wf`
* The named parameter `name`, and its value

This command will:
* Build the container image defined in your `ImageSpec`.

{{< variant flyte >}}
{{< markdown >}}

* Push the image to the container registry specified in that `ImageSpec`. Don't forget make the image accessible to {{< key product_name >}}. For example, if you are using GitHub Container Registry, you will need to make the image public.

{{< /markdown >}}
{{< /variant >}}

* Package up your code and deploy it to the specified project and domain in {{< key product_name >}}.
* Run the workflow on {{< key product_name >}}.

This command is useful for quickly deploying and running a specific workflow on {{< key product_name >}}.
For more details see [{{< key cli >}} run details](./details-of-union-run).

### Fast registration

`{{< key cli >}} register` packages up your code through a mechanism called fast registration.
Fast registration is useful when you already have a container image that’s hosted in your container registry of choice, and you change your workflow/task code without any changes in your system-level/Python dependencies. At a high level, fast registration:

* Packages and zips up the directory/file that you specify as the argument to `{{< key cli >}} register`, along with any files in the root directory of your project. The result of this is a tarball that is packaged into a `.tar.gz` file, which also includes the serialized task (in `protobuf` format) and workflow specifications defined in your workflow code.

* Registers the package to the specified cluster and uploads the tarball containing the user-defined code into the configured blob store (e.g. S3, GCS).

At workflow execution time, {{< key product_name >}} knows to automatically inject the zipped up task/workflow code into the running container, thereby overriding the user-defined tasks/workflows that were originally baked into the image.

<!-- TODO: determine if this section should be included. There was some discussion of flyteignore no longer being relevant

Ignoring files during fast registration

In step (1) of the fast registration process, by default Flyte will package up all user-defined code at the root of your project. In some cases, your project directory may contain datasets, model files, and other potentially large artifacts that you want to exclude from the tarball.

You can do so by specifying these files in a .flyteignore file in the root of your project. You can also use .gitignore or .dockerignore if you’d like to avoid adding another file.
-->

> [!NOTE] WORKDIR, PYTHONPATH, and PATH
> When executing any of the above commands, the archive that gets creates is extracted wherever the `WORKDIR` is set.
> This can be handled directly via the `WORKDIR` directive in a `Dockerfile`, or specified via `source_root` if using `ImageSpec`.
> This is important for discovering code and executables via `PATH` or `PYTHONPATH`.
> A common pattern for making your Python packages fully discoverable is to have a top-level `src` folder, adding that to your `PYTHONPATH`,
> and making all your imports absolute.
> This avoids having to “install” your Python project in the image at any point e.g. via `pip install -e`.


## Deploying your code to {{< key product_name >}} with `{{< key cli >}} register`

```shell
$ {{< key cli >}} register workflows --project basic-example --domain development
```

Here we are registering all the code in the `workflows` directory to the project `basic-example` in the domain `development`.

This command will:
* Build the container image defined in your `ImageSpec`.
* Package up your code and deploy it to the specified project and domain in {{< key product_name >}}.
  The package will contain the code in the Python package located in the `workflows` directory.
  Note that the presence of the `__init__.py` file in this directory is necessary in order to make it a Python package.

The command will not run the workflow. You can run it from the Web interface.

This command is useful for deploying your full set of workflows to {{< key product_name >}} for testing.

## Deploying your code to production with `{{< key cli >}} package` and `{{< key ctl >}} register`

The combination of `{{< key cli >}} package` and `{{< key ctl >}} register` is the standard way of deploying your code to production.
This method is often used in scripts to [build and deploy workflows in a CI/CD pipeline](./ci-cd-deployment).

First, package your workflows:

```shell
$ {{< key cli >}} --pkgs workflows package
```

This will create a tar file called `flyte-package.tgz` of the Python package located in the `workflows` directory.
Note that the presence of the `__init__.py` file in this directory is necessary in order to make it a Python package.

Once the code is packaged you register it using the `{{< key ctl >}}` CLI:

```shell
$ {{< key ctl >}} register files --project basic-example --domain development \
       --archive flyte-package.tgz --version 1.0
```

See [{{< key ctl_name >}} CLI](../../api-reference/uctl-cli) for more details.

## Productionizing your workflows

{{< key product_name >}}’s core design decision is to make workflows reproducible and repeatable.
One way it achieves this is by providing a way for you to bake-in user-defined workflows and all of their dependencies into a Docker container.

The third method of registering your workflows uses two commands:

* `{{< key cli >}} package`: Packages your tasks and workflows into `protobuf` format.

* `{{< key ctl >}} register`: Registers the package to the configured cluster.

This is the production-grade registration flow that we recommend because this method ensures that the workflows are fully containerized,
which ensures that the system- and Python-level dependencies along with your workflow source code are immutable.

### Rolling you own images

While we recommend that you use `ImageSpec` and the `union` cloud image builder, you can, if you wish build and deploy your own images.

You can start with `{{< key cli >}} init --template basic-template-dockerfile`, the resulting template project includes a `docker_build.sh` script that you can use to build and tag a container according to the recommended practice:

```shell
$ ./docker_build.sh
```

By default, the `docker_build.sh` script:

* Uses the PROJECT_NAME specified in the {{< key cli >}}  command, which in this case is my_project.

* Will not use any remote registry.

* Uses the Git SHA to version your tasks and workflows.

You can override the default values with the following flags:

```shell
$ ./docker_build.sh -p <PROJECT_NAME> -r <REGISTRY> -v <VERSION>
```

For example, if you want to push your Docker image to Github’s container registry you can specify the `-r ghcr.io` flag.

> [!NOTE]
> The `docker_build.sh` script is purely for convenience; you can always roll your own way of building Docker containers.

Once you’ve built the image, you can push it to the specified registry. For example, if you’re using Github container registry, do the following:

```shell
$ docker login ghcr.io
$ docker push <tag>
```

### Pulling private images

For many projects it’s convenient to make your images public, but in the case that you’re building proprietary images or images that may contain sensitive metadata/configuration, it’s more secure if they’re private.

Learn more about how to pull private image in the User Guide.

### Relationship between ImageSpec and fast registration

The ImageSpec construct available in `flytekit` also has a mechanism to copy files into the image being built. Its behavior depends on the type of registration used:

* If fast register is used, then it’s assumed that you don’t also want to copy source files into the built image.

* If fast register is not used (which is the default for `pyflyte package`, or if `pyflyte register --copy none` is specified), then it’s assumed that you do want source files copied into the built image.

* If your `ImageSpec` constructor specifies a `source_root` and the `copy` argument is set to something other than `CopyFileDetection.NO_COPY`, then files will be copied regardless of fast registration status.

### Package your project with pyflyte package

You can package your project with the pyflyte package command like so:

```shell
$ pyflyte --pkgs workflows package --image ghcr.io/flyteorg/flytekit:py3.9-latest
```

Expected Output:

```shell
Successfully serialized 4 flyte objects
  Packaging workflows.example.say_hello -> 0_workflows.example.say_hello_1.pb
  Packaging workflows.example.greeting_length -> 1_workflows.example.greeting_length_1.pb
  Packaging workflows.example.wf -> 2_workflows.example.wf_2.pb
  Packaging workflows.example.wf -> 3_workflows.example.wf_3.pb
Successfully packaged 4 flyte objects into /Users/nielsbantilan/sandbox/my_project/flyte-package.tgz
This will create a portable package flyte-package.tgz containing all the Flyte entities compiled as protobuf files that you can register with multiple Flyte clusters.
```

> [!NOTE]
> You can specify multiple workflow directories using the following command:

```shell
$ pyflyte --pkgs <dir1> --pkgs <dir2> package ...
```

This is useful in cases where you want to register two different Flyte projects that you maintain in a single place.

If you encounter a ModuleNotFoundError when packaging, use the --source option to include the correct source paths. For instance:

pyflyte --pkgs <dir1> package --source ./src -f
Register with flytectl register
Finally, register your tasks and workflows with flytectl register files:

flytectl register files \
    --project flytesnacks \
    --domain development \
    --archive flyte-package.tgz \
    --version "$(git rev-parse HEAD)"
Let’s break down what each flag is doing here:

--project: A project is a Flyte concept for built-in multi-tenancy so that you can logically group tasks and workflows. The Flyte demo cluster ships with a default project called flytesnacks.

--domain: A domain enables workflows to be executed in different environment, with separate resource isolation and feature configurations. The Flyte demo cluster ships with three default domains: development, staging, and production.

--archive: This argument allows you to pass in a package file, which in this case is flyte-package.tgz.

--version: This is a version string that can be any string, but we recommend using the git sha in general, especially in production use cases.

Using pyflyte register versus pyflyte package + flytectl register
As a rule of thumb, pyflyte register works well in a single Flyte cluster where you are iterating quickly on your task/workflow code.

On the other hand, pyflyte package and flytectl register is appropriate if you’re:

Working with multiple Flyte clusters since it uses a portable package

Deploying workflows to a production context

Testing your Flyte workflows in your CI/CD infrastructure.

Programmatic Python API

You can also perform the equivalent of the three methods of registration using a FlyteRemote object. You can learn more about how to do this here.

CI/CD with Flyte and GitHub Actions
You can use any of the commands we learned in this guide to register, execute, or test Flyte workflows in your CI/CD process. The core Flyte team maintains two GitHub actions that facilitates this:

flyte-setup-action: This action handles the installation of flytectl in your action runner.

flyte-register-action: This action uses flytectl register under the hood to handle registration of Flyte packages, for example, the .tgz archives that are created by pyflyte package.

Some CI/CD best practices
In case Flyte workflows are registered on each commit in your build pipelines, you can consider the following recommendations and approach:

Versioning Strategy : Determining the version of the build for different types of commits makes them consistent and identifiable. For commits on feature branches, use <branch-name>-<short-commit-hash> and for the ones on main branches, use main-<short-commit-hash>. Use version numbers for the released (tagged) versions.

Workflow Serialization and Registration : Workflows should be serialized and registered based on the versioning of the build and the container image. Depending on whether the build is for a feature branch or main, the registration domain should be adjusted accordingly. For more context, please visit the Registering workflows page.

Container Image Specification : When managing multiple images across tasks within a Flyte workflow, use the --image flag during registration to specify which image to use. This avoids hardcoding the image within the task definition, promoting reusability and flexibility in workflows.


