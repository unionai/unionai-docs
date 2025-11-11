---
title: Container images
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

The `image` parameter of the [`TaskEnvironment`](../../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) is used to specify a container image.
Every task defined using that `TaskEnvironment` will run in a container based on that image.

If a `TaskEnvironment` does not specify an `image`, it will use the default Flyte image ([`ghcr.io/flyteorg/flyte:py{python-version}-v{flyte_version}`](https://github.com/orgs/flyteorg/packages/container/package/flyte)).

## Specifying your own image directly

You can directly reference an image by URL in the `image` parameter, like this:

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    image="docker.io/myorg/myimage:mytag"
)
```

This works well if you have a pre-built image available in a public registry like Docker Hub or in a private registry that your Union/Flyte instance can access.

## Specifying your own image with the `flyte.Image` object

You can also construct an image programmatically using the `flyte.Image` object.

The `flyte.Image` object provides a fluent interface for building container images with specific dependencies.

You start building your image with on of the `from_` methods:

* [`Image.from_base()`](../../api-reference/flyte-sdk/packages/flyte#from_base): Start from a specified Dockerfile.
* [`Image.from_debian_base()`](../../api-reference/flyte-sdk/packages/flyte#from_debian_base): Start from the Flyte default image
* [`Image.from_uv_script()`](../../api-reference/flyte-sdk/packages/flyte#from_uv_script): Start from a [uv script](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)

You can then layer on additional components using the `with_` methods:

* [`Image.with_apt_packages()`](../../api-reference/flyte-sdk/packages/flyte#with_apt_packages): Add Debian packages to the image.
* [`Image.with_commands()`](../../api-reference/flyte-sdk/packages/flyte#with_commands): Add commands to run in the image.
* [`Image.with_dockerignore()`](../../api-reference/flyte-sdk/packages/flyte#with_dockerignore): Specify a `.dockerignore` file.
* [`Image.with_env_vars()`](../../api-reference/flyte-sdk/packages/flyte#with_env_vars): Set environment variables in the image.
* [`Image.with_pip_packages()`](../../api-reference/flyte-sdk/packages/flyte#with_pip_packages): Add Python packages to the image.
* [`Image.with_requirements()`](../../api-reference/flyte-sdk/packages/flyte#with_requirements): Specify a requirements.txt file.
* [`Image.with_source_file()`](../../api-reference/flyte-sdk/packages/flyte#with_source_file): Specify a source file to include in the image.
* [`Image.with_source_folder()`](../../api-reference/flyte-sdk/packages/flyte#with_source_folder): Specify a source folder to include in the image.
* [`Image.with_uv_project()`](../../api-reference/flyte-sdk/packages/flyte#with_uv_project): Use the `uv` script metadata in the source file to specify the image.
* [`Image.with_poetry_project()`](../../api-reference/flyte-sdk/packages/flyte#with_poetry_project): Create a new image with the specified `pyproject.toml`
* [`Image.with_workdir()`](../../api-reference/flyte-sdk/packages/flyte#with_workdir): Specify the working directory for the image.

You can also specify an image in one shot (with no possibility of layering) with:

* [`Image.from_dockerfile()`](../../api-reference/flyte-sdk/packages/flyte#from_dockerfile): Build the final image from a single Dockerfile.

Additionally, the `Image` class provides:

* [`Image.clone()`](../../api-reference/flyte-sdk/packages/flyte#clone): Clone an existing image.
* [`Image.validate()`](../../api-reference/flyte-sdk/packages/flyte#validate): Validate the image configuration.
* [`Image.with_local_v2()`](../../api-reference/flyte-sdk/packages/flyte#with_local_v2): Does not add a layer, instead it overrides any existing builder configuration and builds the image locally. See [Image building](#image-building) for more details.

Here are some examples of the most common patterns for building images with `flyte.Image`.

## Example: Defining a custom image with `Image.from_debian_base`

The `Image.from_debian_base()` provides the default Flyte image as the base.
This image is itself based on the official Python Docker image (specifically `python:{version}-slim-bookworm`) with the addition of the Flyte SDK pre-installed.
Starting there, you can layer additional features onto your image.
For example:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/container-images/from_debian_base.py" lang="python" >}}

> [!NOTE]
> The `registry` parameter is only needed if you are building the image locally. It is not required when using the Union backend `ImageBuilder`.
> See [Image building](#image-building) for more details.

> [!NOTE]
> Images built with `flyte.Image.from_debian_base()` do not include CA certificates by default, which can cause TLS
> validation errors and block access to HTTPS-based storage such as Amazon S3. Libraries like Polars (e.g., `polars.scan_parquet()`) are particularly affected.
> **Solution:** Add `"ca-certificates"` using `.with_apt_packages()` in your image definition.


## Example: Defining an image based on uv script metadata

Another common technique for defining an image is to use [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) to specify your dependencies right in your Python file and then use the `flyte.Image.from_uv_script()` method to create a `flyte.Image` object.
The `from_uv_script` method starts with the default Flyte image and adds the dependencies specified in the `uv` metadata.
For example:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/container-images/from_uv_script.py" lang="python" >}}

The advantage of this approach is that the dependencies used when running a script locally and when running it on the Flyte/Union backend are always the same (as long as you use `uv` to run your scripts locally).
This means you can develop and test your scripts in a consistent environment, reducing the chances of encountering issues when deploying to the backend.

In the above example you can see how to use `flyte.init_from_config()` for remote runs and `flyte.init()` for local runs.
Uncomment the `flyte.init()` line (and comment out `flyte.init_from_config()`) to enable local runs.
Do the opposite to enable remote runs.

> [!NOTE]
> When using `uv` metadata in this way, be sure to include the `flyte` package in your `uv` script dependencies.
> This will ensure that `flyte` is installed when running the script locally using `uv run`.
> When running on the Flyte/Union backend, the `flyte` package from the uv script dependencies will overwrite the one included automatically from the default Flyte image.

## Image building

There are two ways that the image can be built:

* If you are running a Flyte OSS instance then the image will be built locally on your machine and pushed to the container registry you specified in the `Image` definition.
* If you are running a Union instance, the image can be built locally, as with Flyte OSS, or using the Union `ImageBuilder`, which runs remotely on Union's infrastructure.

### Configuring the `builder`

[Earlier](../getting-started/local-setup), we discussed the `image.builder` property in the `config.yaml`.

For Flyte OSS instances, this property must be set to `local`.

For Union instances, this property can be set to `remote` to use the Union `ImageBuilder`, or `local` to build the image locally on your machine.

### Local image building

When `image.builder` in the `config.yaml` is set to `local`, `flyte.run()` does the following:

* Builds the Docker image using your local Docker installation, installing the dependencies specified in the `uv` inline script metadata.
* Pushes the image to the container registry you specified.
* Deploys your code to the backend.
* Kicks off the execution of your workflow
* Before the task that uses your custom image is executed, the backend pulls the image from the registry to set up the container.

> [!NOTE]
> Above, we used `registry="ghcr.io/my_gh_org"`.
>
> Be sure to change `ghcr.io/my_gh_org` to the URL of your actual container registry.

You must ensure that:

* Docker is running on your local machine.
* You have successfully run `docker login` to that registry from your local machine (For example GitHub uses the syntax `echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin`)
* Your Union/Flyte installation has read access to that registry.

> [!NOTE]
> If you are using the GitHub container registry (`ghcr.io`)
> note that images pushed there are private by default.
> You may need to go to the image URI, click **Package Settings**, and change the visibility to public in order to access the image.
>
> Other registries (such as Docker Hub) require that you pre-create the image repository before pushing the image.
> In that case you can set it to public when you create it.
>
> Public images are on the public internet and should only be used for testing purposes.
> Do not place proprietary code in public images.

### Remote `ImageBuilder`

`ImageBuilder` is a service provided by Union that builds container images on Union's infrastructure and provides an internal container registry for storing the built images.

When `image.builder` in the `config.yaml` is set to `remote` (and you are running Union.ai), `flyte.run()` does the following:

* Builds the Docker image on your Union instance with `ImageBuilder`.
* Pushes the image to a registry
  * If you did not specify a `registry` in the `Image` definition, it pushes to the internal registry in your Union instance.
  * If you did specify a `registry`, it pushes to that registry. Be sure to also set the `registry_secret` parameter in the `Image` definition to enable `ImageBuilder` to authenticate to that registry (see [below](#imagebuilder-with-external-registries)).
* Deploys your code to the backend.
* Kicks off the execution of your workflow.
* Before the task that uses your custom image is executed, the backend pulls the image from the registry to set up the container.

There is no set up of Docker nor any other local configuration required on your part.

#### ImageBuilder with external registries

If you are want to push the images built by `ImageBuilder` to an external registry, you can do this by setting the `registry` parameter in the `Image` object.
You will also need to set the `registry_secret` parameter to provide the secret needed to push and pull images to the private registry.
For example:

```python
# Add registry credentials so the Union remote builder can pull the base image
# and push the resulting image to your private registry.
image=flyte.Image.from_debian_base(
    name="my-image",
    base_image="registry.example.com/my-org/my-private-image:latest",
    registry="registry.example.com/my-org"
    registry_secret="my-secret"
)

# Reference the same secret in the TaskEnvironment so Flyte can pull the image at runtime.
env = flyte.TaskEnvironment(
    name="my_task_env",
    image=image,
    secrets="my-secret"
)
```

The value of the `registry_secret` parameter must be the name of a Flyte secret of type `image_pull` that contains the credentials needed to access the private registry. It must match the name specified in the `secrets` parameter of the `TaskEnvironment` so that Flyte can use it to pull the image at runtime.

To create an `image_pull` secret for the remote builder and the task environment, run the following command:

```shell
$ flyte create secret --type image_pull my-secret --from-file ~/.docker/config.json
```

The format of this secret matches the standard Kubernetes [image pull secret](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#log-in-to-docker-hub), and should look like this:

```json
{
  "auths": {
    "registry.example.com": {
      "auth": "base64-encoded-auth"
    }
  }
}
```

> [!NOTE]
> The `auth` field contains the base64-encoded credentials for your registry (username and password or token).

### Install private PyPI packages

To install Python packages from a private PyPI index (for example, from GitHub), you can mount a secret to the image layer.
This allows your build to authenticate securely during dependency installation.
For example:

```python
private_package = "git+https://$GITHUB_PAT@github.com/pingsutw/flytex.git@2e20a2acebfc3877d84af643fdd768edea41d533"
image = (
    Image.from_debian_base()
    .with_apt_packages("git")
    .with_pip_packages(private_package, pre=True, secret_mounts=Secret("GITHUB_PAT"))
)
```