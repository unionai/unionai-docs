# ImageSpec

With Union, every task in a workflow runs within its own dedicated container.
Since a container requires a container image to run, every task in Union must have a container image associated with it.
You can specify the container image to be used by a task by defining an `ImageSpec` object and passing it to the `container_image` parameter of the `@task` decorator.
When you register the workflow, the container image is built locally and pushed to the container registry that you specify.
When the workflow is executed, the container image is pulled from that registry and used to run the task.

:::{note}
See the [flytekit documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.image_spec.ImageSpec.html#flytekit.image_spec.ImageSpec) for full documentation of `ImageSpec` class parameters and methods.
:::

To illustrate the process, we will walk through an example.

## Project structure

```
.
├── image-requirements.txt
├── local-requirements.txt
└── workflows
    ├── __init__.py
    └── imagespec-simple-example.py
```

### image-requirements.txt

```
pandas
```

### local-requirements.txt

```
flytekit
flytekitplugins-envd
-r image-requirements.txt
```

### imagespec-simple-example.py

```{code-block} python
import typing
import pandas as pd
from flytekit import ImageSpec, Resources, task, workflow

image_spec = ImageSpec(
    registry="ghcr.io/<my-github-org>",
    name="simple-example-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.11-latest",
    requirements="image-requirements.txt"
)

@task(container_image=image_spec)
def get_pandas_dataframe() -> typing.Tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv("https://storage.googleapis.com/download.tensorflow.org/data/heart.csv")
    print(df.head())
    return df[["age", "thalach", "trestbps", "chol", "oldpeak"]], df.pop("target")

@workflow()
def wf() --> typing.Tuple[pd.DataFrame, pd.Series]:
    return get_pandas_dataframe()
```

## Install and configure uctl and Docker

Ensure that you have Docker and `uctl` installed and have configure `uctl` to connect to your Union instance.
See [Installing Development Tools](../../../getting-started/installing-development-tools).

## Set up an image registry

You will need an image registry where the container image can be stored and pulled by Union when the task is executed.
You can use any image registry that you have access to, including public registries like Docker Hub or GitHub Container Registry.
Alternatively, you can use a registry that is part of your organization's infrastructure such as AWS Elastic Container Registry (ECR) or Google Artifact Registry (GAR).

The registry that you choose must be one that is accessible to the Union instance where the workflow will be executed.
Additionally, you will need to ensure that the specific image, once pushed to the registry, is itself publicly accessible.

In this example, we use GitHub's `ghcr.io` container registry.
See [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) for more information.

For an example using Amazon ECR see [ImageSpec with ECR](./imagespec-with-ecr).
For an example using Google Artifact Registry see [ImageSpec with GAR](./imagespec-with-gar).

## Authenticate to the registry

You will need to set up your local Docker client to authenticate with GHCR. This is needed for `pyflyte` to be able to push the image built according to the `ImageSpec` to GHCR.

Follow the directions [Working with the Container registry > Authenticating to the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry.md#authenticating-to-the-container-registry).

## Set up your project and domain on Union

You will need to set up a project on your Union instance to which you can register your workflow.
See [Setting up the project on Union](../../../getting-started/setting-up-the-project-on-union).

## Understand the requirements

You will notice that we have defined two requirements files: `local-requirements.txt` and `image-requirements.txt`.
As their names imply, the former defines the Python packages that you will need to run your workflow locally and to register it to Union,
while the latter defines only those packages need to run the workflow in the container on Union.
This setup is not mandatory, but it is a good practice to follow since it makes clear which dependencies are used where.

The `local-requirements.txt` includes the `flytekit` and `flytekitplugins-env` packages as well as the contents of the `image-requirements.txt` file.

The `flytekit` package is, of course, needed in your local requirements to define workflows and to provide the `pyflyte` CLI.
It is not need in the `image-requirements.txt` file because the task container image is based on an image that already includes `flytekit` (specifically the image `flytekit:py3.11-latest`).

The `flytekitplugins-env` package is needed in your local requirements because it provides (together with your local Docker install) the functionality to build and push the container image defined by the `ImageSpec`.
It is not needed in the `image-requirements.txt` file because it is not needed in the container image itself.

The content of the `image-requirements.txt` file is just the `pandas` package, which is needed by the task, so it is need both locally and in the container image running on Union.

## Set up a virtual Python environment

Set up a virtual Python environment and install the dependencies defined in the `local-requirements.txt` file.
Assuming you are in the local project root, run `pip install -r local-requirements.txt`.

## Run the workflow locally

You can now run the workflow locally.
In the project root directory, run: `pyflyte run workflows/imagespec-simple-example.py wf`.
See [Running Workflows Locally](../../../getting-started/running-in-a-local-python-environment.md) for more details.

:::{note}
When you run the workflow in your local Python environment, the image is not built or pushed (in fact, no container image is used at all).
:::

## Register the workflow

To register the workflow to Union, in the local project root, run:

```{code-block} shell
$ pyflyte register workflows/imagespec-simple-example.py
```

`pyflyte` will build the container image and push it to the registry that you specified in the `ImageSpec` object.
It will then register the workflow to Union.

To see the registered workflow, go to the Union console and navigate to the project and domain that you created above.

## Ensure that the image is publicly accessible

If you are using the `ghcr.io` image registry, you must switch the visibility of your container image to Public before you can run your workflow on Union.
See [Configuring a package's access control and visibility](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility.md#about-inheritance-of-access-permissions-and-visibility).

## Run the workflow on Union

Assuming your image is publicly accessible, you can now run the workflow on Union by clicking **Launch Workflow**.

:::{warning}
If you try to run a workflow that uses a private container image or an image that is inaccessible for some other reason, the system will return an error:

```
... Failed to pull image ...
... Error: ErrImagePull
... Back-off pulling image ...
... Error: ImagePullBackOff
```
:::
