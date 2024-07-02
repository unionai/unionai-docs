# Setting up remote dependencies with ImageSpec

During the development cycle you will want ot be able to run your workflows both locally on your machine and remotely on Union,
so you will need ensure that the required dependencies are installed in both environments.

Here we will explain how to set up the dependencies for you workflow to run remotely on Union.
For information on how to make your dependencies available locally, see [Setting up local dependencies]().

## ImageSpec

When a workflow is deployed to Union, each task is set up to run in its own container in the Kubernetes cluster.
You specify the dependencies as part of the definition of the container image to be used for each task using the `ImageSpec` class.
See [ImageSpec](../core-concepts/tasks/task-software-environment/imagespec) for more details.

In the template code generated when you did `union init`, you will see a `ImageSpec` block in the script.
The relevant part for our purposes is:

{@@ if serverless @@}
```python
image_spec = ImageSpec(
    name="basic-union-byoc-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.11-latest",
    requirements="requirements.txt",
    registry="ghcr.io/<my-github-org>"
)

@task(container_image=image_spec)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"
```











Before building the image, Union checks the container registry first to see if the image already exists. By doing so, Union avoids having to rebuild the image. If the image does not exist, Union will build the image before registering the workflow and replace the image name in the task template with the newly built image name.

You can specify Python packages, `apt` packages, and environment variables in the `ImageSpec`.
These specified packages will be added on top of the default image. To override the default image, set the `base_image` parameter in your `ImageSpec` block.



{@@ if serverless @@}

```python

from flytekit import ImageSpec, task

my_image_spec = ImageSpec(
    base_image="cr.union.ai/union/unionai:py3.11-latest",
    packages=["pandas", "numpy"],
    python_version="3.11",
    apt_packages=["git"],
    env={"Debug": "True"},
)
```

{@@ elif byoc @@}

```python

from flytekit import ImageSpec, task

my_image_spec = ImageSpec(
    base_image="cr.flyte.org/flyteorg/flytekit:py3.9-latest",
    packages=["pandas", "numpy"],
    python_version="3.9",
    apt_packages=["git"],
    env={"Debug": "True"},
    registry="ghcr.io/flyteorg",
)
```

:::{important}
For the `registry` parameter, you must replace `ghcr.io/flyteorg` with a container registry you can publish to.
To upload the image to the local registry in the demo cluster, set `registry` to `localhost:30000`.
:::

{@@ endif @@}

## Building container images

{@@ if byoc @@}

:::{admonition} Prerequisites
:class: important

- Install [flytekitplugins-envd](https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-envd) to build the `ImageSpec`.
- `docker login` is required to push the image to the specified registry.
- To build the image on a remote machine, see [this doc](https://envd.tensorchord.ai/teams/context.html#start-remote-buildkitd-on-builder-machine).
:::

The `ImageSpec` code block will be converted to an [Envd](https://envd.tensorchord.ai/) config, and the [Envd builder](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-envd/flytekitplugins/envd/image_builder.py#L12-L34) will build the image for you. However, you can also register your own builder and specify it in the `builder` parameter to build the image using other tools.

{@@ elif serverless @@}

The `ImageSpec` code block will be converted to an [Envd](https://envd.tensorchord.ai/) config, and the Serverless image builder will build the image for you.

With the Union Serverless image builder, the Docker images used by your tasks are built in the cloud on Union.
For this example, save the following as `image_build.py`:

```{code-block} python
from flytekit import ImageSpec, task, workflow

image = ImageSpec(
    builder="unionai",
    packages=["numpy==1.26.4"],
)

@task(container_image=image)
def fn() -> int:
    import numpy as np
    x = np.array([1, 2, 3])
    return int(x.sum())

@workflow
def main() -> int:
    return fn()

```

This example contains an `ImageSpec` that specifies the dependencies of the `@task`. We
set `builder="unionai"` to configure `ImageSpec` to build the image on our hosted image
builder. Next, run run the `image_build.py` script to see how it works:

```{code-block} shell
unionai run --remote image_build.py main
```

This command will start up an image builder task on Union:

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless.union.ai/org/cosmicbboy/projects/default/domains/development/executions/EXECUTION_ID
```

{@@ endif @@}

After the build is complete, then the original workflow will run with the newly created image!

## Specifying a custom image for a task

To specify a custom image for a task, set the `container_image` parameter to the name of your `ImageSpec` in the `@task` decorator. If you do not specify a container image, the default Docker image is used.

```python
@task(container_image=my_image_spec)
def my_task() -> pd.DataFrame
    ...

```