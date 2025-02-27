# ImageSpec

With Union, every task in a workflow runs within its own dedicated container.
Since a container requires a container image to run, every task in Union must have a container image associated with it.
You can specify the container image to be used by a task by defining an `ImageSpec` object and passing it to the `container_image` parameter of the `@union.task` decorator.
When you register the workflow, the container image is built locally and pushed to the container registry that you specify.
When the workflow is executed, the container image is pulled from that registry and used to run the task.

:::{note}
See the [Flytekit documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.image_spec.ImageSpec.html#flytekit.image_spec.ImageSpec) for full documentation of `ImageSpec` class parameters and methods.
:::

To illustrate the process, we will walk through an example.

## Project structure

```{code-block} shell
├── requirements.txt
└── workflows
    ├── __init__.py
    └── imagespec-simple-example.py
```

### requirements.txt

```{code-block} shell
union
pandas
```

### imagespec-simple-example.py

```{code-block} python
import typing
import pandas as pd
import union

image_spec = union.ImageSpec(
    registry="ghcr.io/<my-github-org>",
    name="simple-example-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.11-latest",
    requirements="requirements.txt"
)

@union.task(container_image=image_spec)
def get_pandas_dataframe() -> typing.Tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv("https://storage.googleapis.com/download.tensorflow.org/data/heart.csv")
    print(df.head())
    return df[["age", "thalach", "trestbps", "chol", "oldpeak"]], df.pop("target")

@union.workflow()
def wf() -> typing.Tuple[pd.DataFrame, pd.Series]:
    return get_pandas_dataframe()
```

## Install and configure `union` and Docker

To install Docker, see [Setting up container image handling](../../../first-workflow/setting-up-container-image-handling.md).
To configure `union` to connect to your Union instance, see [Quick start](../../../../quick-start.md).

## Set up an image registry

You will need an image registry where the container image can be stored and pulled by Union when the task is executed.
You can use any image registry that you have access to, including public registries like Docker Hub or GitHub Container Registry.
Alternatively, you can use a registry that is part of your organization's infrastructure such as AWS Elastic Container Registry (ECR) or Google Artifact Registry (GAR).

The registry that you choose must be one that is accessible to the Union instance where the workflow will be executed.
Additionally, you will need to ensure that the specific image, once pushed to the registry, is itself publicly accessible.

In this example, we use GitHub's `ghcr.io` container registry.
See [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) for more information.

For an example using Amazon ECR see [ImageSpec with ECR](./imagespec-with-ecr.md).
For an example using Google Artifact Registry see [ImageSpec with GAR](./imagespec-with-gar.md).

## Authenticate to the registry

You will need to set up your local Docker client to authenticate with GHCR. This is needed for `union` to be able to push the image built according to the `ImageSpec` to GHCR.

Follow the directions [Working with the Container registry > Authenticating to the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry.md#authenticating-to-the-container-registry).

## Set up your project and domain on Union

You will need to set up a project on your Union instance to which you can register your workflow.
See [Setting up the project](../../../development-cycle/setting-up-a-project.md).

## Understand the requirements

The `requirements.txt` file contains the `union` package and the `pandas` package, both of which are needed by the task.

## Set up a virtual Python environment

Set up a virtual Python environment and install the dependencies defined in the `requirements.txt` file.
Assuming you are in the local project root, run `pip install -r requirements.txt`.

## Run the workflow locally

You can now run the workflow locally.
In the project root directory, run: `union run workflows/imagespec-simple-example.py wf`.
See [Running your code](../../../development-cycle/running-your-code.md) for more details.

:::{note}
When you run the workflow in your local Python environment, the image is not built or pushed (in fact, no container image is used at all).
:::

## Register the workflow

To register the workflow to Union, in the local project root, run:

```{code-block} shell
$ union register workflows/imagespec-simple-example.py
```

`union` will build the container image and push it to the registry that you specified in the `ImageSpec` object.
It will then register the workflow to Union.

To see the registered workflow, go to the UI and navigate to the project and domain that you created above.

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
