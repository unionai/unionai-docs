```{eval-rst}
.. tags:: Containerization, Intermediate
```

# Image Spec

In this section, you will uncover how {@= Product =@} utilizes Docker images to construct containers under the hood, and you'll learn how to craft your own images to encompass all the necessary dependencies for your tasks or workflows.

You will explore how to execute a raw container with custom commands,
indicate multiple container images within a single workflow,
and get familiar with the ins and outs of `ImageSpec`!

`ImageSpec` allows you to customize the container image for your {@= Product =@} tasks without a Dockerfile. `ImageSpec` speeds up the build process by allowing you to reuse previously downloaded packages from the PyPI and APT caches.

{@@ if serverless or byoc or byok @@}

By default, the `ImageSpec` will be built using the [remote builder](https://docs.union.ai/byoc/user-guide/development-cycle/image-spec#union-ai-cloud-image-builder), but you can always specify your own e.g. local Docker.

{@@ elif flyte @@}

By default, the `ImageSpec` will be built using the default Docker builder, but you can always specify your own e.g. [flytekitplugins-envd](https://github.com/flyteorg/flytekit/plugins/flytekit-envd/flytekitplugins/envd/image_builder.py#L25) which uses envd to build the ImageSpec.

{@@ endif @@}

For every {py:class}`{@= kit =@}.PythonFunctionTask` task or a task decorated with the `@task` decorator, you can specify rules for binding container images. By default, {@= kit =@} binds a single container image, i.e.,
the [default Docker image](https://ghcr.io/flyteorg/flytekit), to all tasks. To modify this behavior, use the `container_image` parameter available in the {py:func}`{@= kit =@}.task` decorator, and pass an `ImageSpec` definition.

Before building the image, {@= Kit =@} checks the container registry to see if the image already exists. If the image does not exist, {@= Kit =@} will build the image before registering the workflow and replace the image name in the task template with the newly built image name.

{@@ if flyte @@}
:::{admonition} Prerequisites
:class: important

- Make sure `docker` is running on your local machine.
- When using a registry in ImageSpec, `docker login` is required to push the image
:::
{@@ endif @@}

## Install Python or APT packages
You can specify Python packages and APT packages in the `ImageSpec`.
These specified packages will be added on top of the [default image](https://github.com/flyteorg/flytekit/blob/master/Dockerfile), which can be found in the {@= Kit =@} Dockerfile.
More specifically, {@= kit =@} invokes [DefaultImages.default_image()](https://github.com/flyteorg/flytekit/flytekit/configuration/default_images.py#L26-L27) function. This function determines and returns the default image based on the Python version and {@= kit =@} version. For example, if you are using Python 3.8 and flytekit 1.6.0, the default image assigned will be `ghcr.io/flyteorg/flytekit:py3.8-1.6.0`.

{@@ if flyte @@}
:::{important}
Replace `ghcr.io/flyteorg` with a container registry you can publish to.
To upload the image to the local registry in the demo cluster, indicate the registry as `localhost:30000` using the `registry` argument to `ImageSpec`.
:::
{@@ endif @@}

```python
from {@= kit =@} import ImageSpec

sklearn_image_spec = ImageSpec(
  packages=["scikit-learn", "tensorflow==2.5.0"],
  apt_packages=["curl", "wget"],
)
```

## Install Conda packages
Define the `ImageSpec` to install packages from a specific conda channel.

```python
image_spec = ImageSpec(
  conda_packages=["langchain"],
  conda_channels=["conda-forge"],  # List of channels to pull packages from.
)
```

## Use different Python versions in the image
You can specify the Python version in the `ImageSpec` to build the image with a different Python version.

```python
image_spec = ImageSpec(
  packages=["pandas"],
  python_version="3.9",
)
```

## Import modules only in a specify imageSpec environment

The `is_container()` method is used to determine whether the task is utilizing the image constructed from the `ImageSpec`. If the task is indeed using the image built from the `ImageSpec`, it will return true. This approach helps minimize module loading time and prevents unnecessary dependency installation within a single image.

In the following example, both `task1` and `task2` will import the `pandas` module. However, `Tensorflow` will only be imported in `task2`.

```python
from flytekit import ImageSpec, task
import pandas as pd

pandas_image_spec = ImageSpec(
  packages=["pandas"],
  registry="ghcr.io/flyteorg",
)

tensorflow_image_spec = ImageSpec(
  packages=["tensorflow", "pandas"],
  registry="ghcr.io/flyteorg",
)

# Return if and only if the task is using the image built from tensorflow_image_spec.
if tensorflow_image_spec.is_container(): 
  import tensorflow as tf

@task(container_image=pandas_image_spec)
def task1() -> pd.DataFrame:
  return pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [1, 22]})


@task(container_image=tensorflow_image_spec)
def task2() -> int:
  num_gpus = len(tf.config.list_physical_devices('GPU'))
  print("Num GPUs Available: ", num_gpus)
  return num_gpus
```

## Install CUDA in the image
There are few ways to install CUDA in the image.

### Use Nvidia docker image
CUDA is pre-installed in the Nvidia docker image. You can specify the base image in the `ImageSpec`.
```python
image_spec = ImageSpec(
  base_image="nvidia/cuda:12.6.1-cudnn-devel-ubuntu22.04",
  packages=["tensorflow", "pandas"],
  python_version="3.9",
)
```

### Install packages from extra index
CUDA can be installed by specifying the `pip_extra_index_url` in the `ImageSpec`.
```python
image_spec = ImageSpec(
  name="pytorch-mnist",
  packages=["torch", "torchvision", "flytekitplugins-kfpytorch"],
  pip_extra_index_url=["https://download.pytorch.org/whl/cu118"],
)
```

## Build an image in different architecture
You can specify the platform in the `ImageSpec` to build the image in a different architecture, such as `linux/arm64` or `darwin/arm64`.
```python
image_spec = ImageSpec(
  packages=["pandas"],
  platform="linux/arm64",
)
```

{@@ if flyte @@}
## Install flytekit from GitHub
When you update the flytekit, you may want to test the changes with your tasks.
You can install the flytekit from a specific commit hash in the `ImageSpec`.

```python
new_flytekit = "git+https://github.com/flyteorg/flytekit@90a4455c2cc2b3e171dfff69f605f47d48ea1ff1"
new_spark_plugins = f"git+https://github.com/flyteorg/flytekit.git@90a4455c2cc2b3e171dfff69f605f47d48ea1ff1#subdirectory=plugins/flytekit-spark"

image_spec = ImageSpec(
  apt_packages=["git"],
  packages=[new_flytekit, new_spark_plugins],
  registry="ghcr.io/flyteorg",
)
```
{@@ endif @@}

## Customize the tag of the image
You can customize the tag of the image by specifying the `tag_format` in the `ImageSpec`. In the following example, the tag will be `<spec_hash>-dev`.

```python
image_spec = ImageSpec(
  name="my-image",
  packages=["pandas"],
  tag_format="{spec_hash}-dev",
)
```

## Copy additional files or directories
You can specify files or directories to be copied into the container `/root`, allowing users to access the required files. The directory structure will match the relative path. Since Docker only supports relative paths, absolute paths and paths outside the current working directory (e.g., paths with "../") are not allowed.

```py
from {@= kit =@} import task, workflow, ImageSpec

image_spec = ImageSpec(
    name="image_with_copy",
    copy=["files/input.txt"],
)

@task(container_image=image_spec)
def my_task() -> str:
    with open("/root/files/input.txt", "r") as f:
        return f.read()
```

## Define ImageSpec in a YAML File

You can override the container image by providing an ImageSpec YAML file to the `{@= cli =@} run` or `{@= cli =@} register` command. This allows for greater flexibility in specifying a custom container image. For example:

```yaml
# imageSpec.yaml
python_version: 3.11
packages:
  - sklearn
env:
  Debug: "True"
```

```
# Use {@= cli =@} to register the workflow
{@= cli =@} run --remote --image image.yaml image_spec.py wf
```

## Build the image without registering the workflow

If you only want to build the image without registering the workflow, you can use the `{@= cli =@} build` command.

```
{@= cli =@} build --remote image_spec.py wf
```

## Force push an image

In some cases, you may want to force an image to rebuild, even if the ImageSpec hasn’t changed. To overwrite an existing image, pass the `FLYTE_FORCE_PUSH_IMAGE_SPEC=True` to the `{@= cli =@}` command.

```bash
FLYTE_FORCE_PUSH_IMAGE_SPEC=True {@= cli =@} run --remote image_spec.py wf
```

You can also force push an image in the Python code by calling the `force_push()` method.

```python
image = ImageSpec(packages=["pandas"]).force_push()
```
[flytesnacks]: https://github.com/flyteorg/flytesnacks/tree/master/examples/customizing_dependencies/

## Getting source files into ImageSpec
Typically, getting source code files into a task's image at run time on a live {@= Product =@} backend is done through the fast registration mechanism.

However, if your `ImageSpec` constructor specifies a `source_root` and the `copy` argument is set to something other than `CopyFileDetection.NO_COPY`, then files will be copied regardless of fast registration status.
If the `source_root` and `copy` fields to an `ImageSpec` are left blank, then whether or not your source files are copied into the built `ImageSpec` image depends on whether or not you use fast registration. Please see [registering workflows](https://docs.union.ai/byoc/user-guide/core-concepts/#registering-tasks-and-workflows) for the full explanation.

Since files are sometimes copied into the built image, the tag that is published for an ImageSpec will change based on whether fast register is enabled, and the contents of any files copied.
