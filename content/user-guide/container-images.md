---
title: Container images
weight: 50
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

Every `task` in Flyte runs in its own container and every container needs a container image to define it.

We use the `image` parameter of the [`TaskEnvironment`](../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) to specify an image.
Every task that uses that `TaskEnvironment` will run in a container based on that image.

If a `TaskEnvironment` does not specify an `image`, it will use the default Flyte image.

You can directly reference an image by URL in the `image` parameter, like this:

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    image="docker.io/myorg/myimage:latest"
)
```

This works well if you have a pre-built image available in a public registry like Docker Hub or in a private registry that your Union instance can access.

But, in many cases, you will want to build your own custom image that includes the dependencies required by your task, and you want to do that in as convenient a way as possible.

With Flyte you can do it right in your Python code, using the [`Image`](../api-reference/flyte-sdk/packages/flyte#flyteimage) object and [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

## Example

Here is an example:

{{< code file="/external/migrate-to-unionai-examples-flyte2/container_images.py" lang="python" >}}

First, specify your dependencies using [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).
Simply add a comment at the top of your script as shown above, that includes your dependencies.

Next, use the `flyte.Image.from_uv_script` method to create a [`flyte.Image`](../api-reference/flyte-sdk/packages/flyte#flyteimage) object.

## Image building

When you run the code above, Flyte will automatically build the image for you on your local machine and push it to the registry you specified in the image definition.
Above we used `registry="ghcr.io/<your-github-handle>"`.
You can specify a registry of you choice.

You must ensure that:

* Docker is running on your local machine.
* You have successfully run `docker login` to that registry from your local machine (GitHub uses the syntax `echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin`)
* Your Flyte/Union installation has read access to that registry.

Note that images pushed to `ghcr.io` are private by default.
If using GitHub Packages (i.e. `ghcr.io`), you may need to go to the image URI, click Package Settings, and change the visibility to public in order to access the image.

> [!NOTE]
> Public images are on the public internet and should only be used for testing purposes.
> Do not place proprietary code in public images.)

Once the image is built and pushed to the registry, Flyte will deploy your code to your backend.
When a Flyte task is executed, The backend pulls the image from the registry to set up the container for that task.

## uv run

To run the script, use the `uv run` command:

```shell
uv run --prerelease=allow container_images.py
```

[`uv run`](https://docs.astral.sh/uv/reference/cli/#uv-run) will read the [inline script metadata](https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies), create an on-demand virtual environment, install the dependencies, and then execute the Flyte code.

In your terminal you should see something like this:

```shell
$ uv run --prerelease=allow container_images.py
Reading inline script metadata from `container_images.py`
[flyte] Temporary directory: /var/folders/1b/j0rhj5ms7hg20_jml81gscsh0000gn/T/tmpsjk553dj
Run command: docker buildx build --builder flytex --tag ghcr.io/myregistry/flyte:d1c1a0a9c3e65c329bae976afddea670 --platform linux/amd64,linux/arm64 --push --push /var/folders/1b/j0rhj5ms7hg20_jml81gscsh0000gn/T/tmpsjk553dj

...

View build details: docker-desktop://dashboard/build/flytex/flytex0/dz3x633t2seh5wkxk3ubhmg4s
7lkfjscn4pbf429drr98
https://playground.canary.unionai.cloud/v2/runs/project/flytesnacks/domain/development/7lkfjscn4pbf429drr98
Run 'a0' completed successfully.
```

