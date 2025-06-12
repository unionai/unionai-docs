---
title: Container images
weight: 40
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

Every `task` in Flyte runs in its own container and every container needs a container image to define it.

We use the `image` parameter of the `TaskEnvironment` to specify an image.
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

With Flyte you can do it right in your Python code, using the [`Image`](../api-reference/flyte-sdk/packages/flyte#flyteimage) object.

Here is an example:

{{< code file="/external/migrate-to-unionai-examples-flyte2/container_images.py" lang="python" >}}

Here we leverage [`uv` inline script metadata](https://docs.astral.sh/uv/inline-scripts) to specify the dependencies required by our task.
You simply add a comment at the top of your script as shown above, that includes your dependencies, and then use the `flyte.Image.from_uv_script` method to create a `flyte.Image` object.

## Image building

When you run the code above, Flyte will automatically build the image for you on your local machine and push it to the registry you specified in the image definition.
Above we used `registry="ghcr.io/<your-github-handle>"`.
You can specify a registry of you choice.

You must ensure that:

* Docker is running on your local machine.
* You have successfully ran `docker login` to that registry from your local machine
* Your Flyte/Union installation has read access to that registry.

## Image pulling

Once the image is built and pushed to the registry, Flyte will deploy your code to your Flyte/Union instance.
Before a task is executed, Flyte pulls the image from the registry in preparation for running the task in a container based on that image.
This is why you need to ensure that your Flyte/Union instance has access to the registry where your image is stored. Note that images pushed to `ghcr.io` are private by default.

## Example

To run the above script, ensure you are in a virtual environment and install the dependencies locally:

```shell
uv pip install polars
```

Next, with the docker daemon running on your local machine, run the script:

```shell
flyte run container_images.py workflow
```

Your terminal will show something like the following:

```shell
(unionv2) johnvotta@JV---Work unionv2 % python container_images.py 
[flyte] Building Image for environment polars_image, image: Image(base_image='debian:bookworm-slim', dockerfile=None, registry='ghcr.io/jpvotta', name='flyte', platform=('linux/amd64', 'linux/arm64'), tag=None, python_version=(3, 12), _identifier_override=None, is_final=False, _layers=(PipPackages(packages=('polars',)),))
[flyte] Building image flyte for environment polars_image
[flyte] Image ghcr.io/jpvotta/flyte:33f83688ff9c10a6eb6a9b34d8fac7d7 does not exist in registry or force/dry-run, building...
[flyte] Buildx builder already exists.
[flyte] Temporary directory: /var/folders/1b/j0rhj5ms7hg20_jml81gscsh0000gn/T/tmpaz1hej1e
Run command: docker buildx build --builder flytex --tag ghcr.io/jpvotta/flyte:33f83688ff9c10a6eb6a9b34d8fac7d7 --platform linux/amd64,linux/arm64 --push --push /var/folders/1b/j0rhj5ms7hg20_jml81gscsh0000gn/T/tmpaz1hej1e 

...

View build details: docker-desktop://dashboard/build/flytex/flytex0/ugdzhhtdb2bdb8ovrf1kipl7p
[flyte] Built Image for environment polars_image, image: ghcr.io/jpvotta/flyte:33f83688ff9c10a6eb6a9b34d8fac7d7
Files to be copied for fast registration...
📂 /Users/johnvotta/code/unionv2 (detected source root)
┗━━ container_images.py
[flyte] Code bundle created at /var/folders/1b/j0rhj5ms7hg20_jml81gscsh0000gn/T/tmpbdjdoidu/fastef28a17cb2bb830b3eafb7170aa14112.tar.gz, size: 0.009765625 MB, archive size: 0.0006113052368164062 MB
bs4574422hln9kwkzwnn
https://demo.hosted.unionai.cloud/v2/runs/project/flytesnacks/domain/development/bs4574422hln9kwkzwnn
```

Note that if using `ghcr.io`, you may need to go to the image URI, click Package Settings, and change the visibility to public in order to access the image. Note that public images are on the public internet and should only be used for testing purposes. Do not place proprietary code in public images!

