---
title: Container images
weight: 60
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

Every `task` in Flyte runs in its own container (unless you are using [reusable containers](./reusable-containers)) and every container needs a container image to define it.

We use the `image` parameter of the [`TaskEnvironment`](../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) to specify an image.
Every task that uses that `TaskEnvironment` will run in a container based on that image.

If a `TaskEnvironment` does not specify an `image`, it will use the default Flyte image ([`ghcr.io/unionai-oss/flyte:latest`](https://github.com/orgs/unionai-oss/packages/container/package/)).


## Specifying your own image directly

You can directly reference an image by URL in the `image` parameter, like this:

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    image="docker.io/myorg/myimage:latest"
)
```

This works well if you have a pre-built image available in a public registry like Docker Hub or in a private registry that your Union instance can access.

## Specify dependencies in your Python file

But, in many cases, you will want to build your own custom image that includes the dependencies required by your task, and you want to do that in as convenient a way as possible.

With Flyte you can do it right in your Python code, using the [`Image`](../api-reference/flyte-sdk/packages/flyte#flyteimage) object and [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

## Example

Here is an example:

<!-- TODO:
Ketan Umare:
Its weird to have this as the first example. I think we should have a regular image building example Image.from_debian_base().with_pip_packages(...) and then have this maybe as an additional example
-->
{{< code file="/external/migrate-to-unionai-examples-flyte2/container_images.py" lang="python" >}}

First, specify your dependencies using [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).
Simply add a comment at the top of your script as shown above, that includes your dependencies.

Next, use the `flyte.Image.from_uv_script` method to create a [`flyte.Image`](../api-reference/flyte-sdk/packages/flyte#flyteimage) object.

## Image building

There are two ways that the image can be built:

* If you are running a Flyte OSS instance then the image will be built locally on your machine and pushed to the container registry you specified in the `Image` definition.
* If you are running a Union instance, the image can be built locally, as with Flyte OSS, or using the Union `ImageBuilder`, which runs remotely on Union's infrastructure.

### Configuring the `builder`

In [Configuration > Setting up the configuration file > `image` section](./configuration#image-section), we discussed the `image.builder` property in the `config.yaml`.

For Flyte OSS instances, this property must be set to `local`.

For Union instances, this property can be set to `remote` to use the Union `ImageBuilder`, or `local` to build the image locally on your machine.

### Running the script

To run the script, use the `uv run` command:

```shell
uv run --prerelease=allow container_images.py
```

### Local image building

When `image.builder` in the `config.yaml` is set to `local`, running the code above executes the `flyte.run()` command, which does the following:

* Builds the Docker image using your local Docker installation, installing the dependencies specified in the `uv` inline script metadata.
* Pushes the image to the container registry you specified.
* Deploys your code to the backend.
* Kicks off the execution of your workflow
* Before the task that uses your custom image is executed, the backend pulls the image from the registry to set up the container.

> [!NOTE]
> Above, we used `registry=MY_CONTAINER_REGISTRY`.
>
> Be sure to set the constant `MY_CONTAINER_REGISTRY`
> to the URL of your actual container registry.

You must ensure that:

* Docker is running on your local machine.
* You have successfully run `docker login` to that registry from your local machine (For example GitHub uses the syntax `echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin`)
* Your Union/Flyte installation has read access to that registry.

> [!NOTE]
> If you are using the GitHub container registry (`ghcr.io`)
> note that images pushed there are private by default. You may need to go to the image URI,
> click Package Settings, and change the visibility to public in order to access the image.
>
> Other registries (such as Docker Hub) require that you pre-create the image repository
> before pushing the image. In that case you can set it to public when you create it.
>
> Public images are on the public internet and should only be used for testing purposes.
> Do not place proprietary code in public images.

### Remote `ImageBuilder`

When `image.builder` in the `config.yaml` is set to `remote` (and you are running Union.ai), running the code above executes the `flyte.run()` command, which does the following:

* Builds the Docker image on you Union instance with `ImageBuilder`, installing the dependencies specified in the `uv` inline script metadata.
* Pushes the image to the internal container registry of your Union instance.
* Deploys your code to the backend.
* Kicks off the execution of your workflow
* Before the task that uses your custom image is executed, the backend pulls the image from the internal registry to set up the container.

There is no set up of Docker nor any access control configuration required on your part.
