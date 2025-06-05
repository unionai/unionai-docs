---
title: Container images
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

Every `task` in Flyte runs in its own container and every container needs a container image to define it.

We use the `image` parameter of the `TaskEnvironment` to specify an image.
Every task that uses that `TaskEnvironment` will run in a container based on that image.

If a `TaskEnvironment` does not specify an `image`, it will use the default Flyte image.

The simplest way to specify a container image is to directly reference it by URL in the `image` parameter, like this:

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    image="docker.io/myorg/myimage:latest"
)
```

This works well if you have a pre-built image available in a public registry like Docker Hub or in a private registry that your Flyte/Union instance can access.

But, in many cases, you will want to build your own custom image that includes the dependencies required by your task, and you want to do that in as convenient a way as possible.

With Flyte you can do it right in your Python code, using the [`Image`](../api-reference/flyte-sdk/packages/flyte#flyteimage) object.

Here is an example:

```python
# /// script
# dependencies = [
#    "polars",
# ]
# ///

import polars as pl

import flyte

env = flyte.TaskEnvironment(
    name="polars_image",
    image=flyte.Image.from_uv_script(
        __file__,
        name="flyte",
        registry="ghcr.io/unionai-oss",
        arch=("linux/amd64", "linux/arm64"),
    ),
)


@env.task
async def create_dataframe() -> pl.DataFrame:
    return pl.DataFrame(
        {"name": ["Alice", "Bob", "Charlie"], "age": [25, 32, 37], "city": ["New York", "Paris", "Berlin"]}
    )


@env.task
async def print_dataframe(dataframe: pl.DataFrame):
    print(dataframe)


@env.task
async def workflow():
    df = await create_dataframe()
    await print_dataframe(df)


if __name__ == "__main__":
    flyte.init_auto_from_config("./config.yaml")
    run = flyte.run(workflow)
    print(run.name)
    print(run.url)
    run.wait(run)

```

Here we leverage [`uv` inline script metadata](https://docs.astral.sh/uv/inline-scripts) to specify the dependencies required by our task.
You simply add a comment at the top of your script as shown above, that includes your dependencies, and then use the `flyte.Image.from_uv_script` method to create a `flyte.Image` object.

## Image building

When you run the code above, Flyte will automatically build the image for you on your local machine and push it to the registry you specified in the image definition.
Above we used `registry="ghcr.io/unionai-oss"`.
You can specify a registry of you choice.

You must ensure that:

* Docker is running on your local machine.
* You have successful done `docker login` to that registry from your local machine
* Your Flyte/Union installation has read access to that registry.

## Image pulling

Once the image is built and pushed to the registry, Flyte will deploy your code to your Flyte/Union instance.
Before a task is executed, Flyte pulls the image from the registry in preparation for running the task in a container based on that image.
This is why you need to ensure that your Flyte/Union instance has access to the registry where your image is stored.
