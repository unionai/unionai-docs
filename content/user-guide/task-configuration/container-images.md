---
title: Container images
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

The `image` parameter of the [`TaskEnvironment`](../../api-reference/flyte-sdk/packages/flyte#flytetaskenvironment) to specify a container image.
Every task defined using that `TaskEnvironment` will run in a container based on that image.

If a `TaskEnvironment` does not specify an `image`, it will use the default Flyte image ([`ghcr.io/unionai-oss/flyte:latest`](https://github.com/orgs/unionai-oss/packages/container/package/)).


## Specifying your own image directly

You can directly reference an image by URL in the `image` parameter, like this:

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    image="docker.io/myorg/myimage"
)
```

This works well if you have a pre-built image available in a public registry like Docker Hub or in a private registry that your Union/Flyte instance can access.

## Specifying your own image with the `flyte.Image` object

You can also construct an image programmatically using the `flyte.Image` object.

The `flyte.Image` object provides a fluent interface for building container images with specific dependencies.

You start building your image with on of the `from_` methods:

* [`Image.from_base()`](../../api-reference/flyte-sdk/packages/flyte#from_base): Start from a specified Dockerfile.
* [`Image.from_debian_base()`](../../api-reference/flyte-sdk/packages/flyte#from_debian_base): Start from the Flyte default image
* [`Image.from_uv_script()`](../../api-reference/flyte-sdk/packages/flyte#from_uv_script): Starte from

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
* [`Image.with_workdir()`](../../api-reference/flyte-sdk/packages/flyte#with_workdir): Specify the working directory for the image.

You can also specify an image in one shot (with no possibility of layering) with:

* [`Image.from_dockerfile()`](../../api-reference/flyte-sdk/packages/flyte#from_dockerfile): Build the final image from a single Dockerfile.

Additionally, the `Image` class provides:

* [`Image.clone()`](../../api-reference/flyte-sdk/packages/flyte#clone): Clone an existing image.
* [`Image.validate()`](../../api-reference/flyte-sdk/packages/flyte#validate): Validate the image configuration.
* [`Image.with_local_v2()`](../../api-reference/flyte-sdk/packages/flyte#with_local_v2): Does not add a layer, instead it overrides any existing builder configuration and builds the image locally. See [Image building](#image-building) for more details.

Here are some examples of the most common patterns for building images with `flyte.Image`.

### Building custom images with `Image.from_debian_base`

The `Image.from_debian_base()` method is the recommended way to create custom container images for your tasks.
It provides the default Flyte image as the base. This image is itself based on the official Python Docker image (specifically `python:{version}-slim-bookworm`) with the addition of the Flyte SDK pre-installed.






### Basic usage

```python
import flyte

# Create a basic image with current Python version
image = flyte.Image.from_debian_base()

# Use it in a TaskEnvironment
env = flyte.TaskEnvironment(name="my_env", image=image)
```

### Parameters

The `from_debian_base()` method accepts several optional parameters:

- **`python_version`**: Specify the Python version as a tuple, e.g., `(3, 12)`
- **`install_flyte`**: Set to `False` if you want a clean Python environment without the Flyte SDK
- **`registry`**: Custom Docker registry for your image
- **`name`**: Custom name for your image
- **`platform`**: Target architecture(s), defaults to multi-arch (`linux/amd64`, `linux/arm64`)

### Common patterns

#### Specific Python version
```python
# Use Python 3.12
image = flyte.Image.from_debian_base(python_version=(3, 12))
```

#### Clean Python environment
```python
# Python environment without Flyte SDK pre-installed
image = flyte.Image.from_debian_base(install_flyte=False)
```

#### Custom registry and name
```python
# Push to your own registry
image = flyte.Image.from_debian_base(
    registry="my-registry.com",
    name="my-python-env"
)
```

### Layering additional components

The power of `from_debian_base()` comes from chaining it with additional methods to build up your image:

```python
image = (
    flyte.Image.from_debian_base()
    .with_apt_packages("git", "curl")  # System packages
    .with_pip_packages("numpy", "pandas", "scikit-learn")  # Python packages
    .with_env_vars({"MY_CONFIG": "production"})  # Environment variables
    .with_source_folder(Path("./src"))  # Include local code
)
```

### When to use `from_debian_base`

Use `Image.from_debian_base()` when you need:
- A standardized, reliable Python environment
- Multi-architecture support (AMD64 and ARM64)
- Integration with Flyte's caching and optimization features
- A starting point for complex, layered image builds
- Consistent development and production environments

The method creates images that are optimized for Flyte's execution environment while giving you full control over dependencies and configuration.

## Specify dependencies in your Python file

But, in many cases, you will want to build your own custom image that includes the dependencies required by your task, and you want to do that in as convenient a way as possible.

With Flyte you can do it right in your Python code, using the [`Image`](../../api-reference/flyte-sdk/packages/flyte#flyteimage) object and [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

## Example

Here is an example:

<!-- TODO:
Ketan Umare:
Its weird to have this as the first example. I think we should have a regular image building example Image.from_debian_base().with_pip_packages(...) and then have this maybe as an additional example
-->
{{< code file="/external/migrate/user-guide/task-configuration/container-images/container_images.py" lang="python" >}}

First, specify your dependencies using [`uv` inline script metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).
Simply add a comment at the top of your script as shown above, that includes your dependencies.

Next, use the `flyte.Image.from_uv_script` method to create a [`flyte.Image`](../../api-reference/flyte-sdk/packages/flyte#flyteimage) object.

## Image building

There are two ways that the image can be built:

* If you are running a Flyte OSS instance then the image will be built locally on your machine and pushed to the container registry you specified in the `Image` definition.
* If you are running a Union instance, the image can be built locally, as with Flyte OSS, or using the Union `ImageBuilder`, which runs remotely on Union's infrastructure.

### Configuring the `builder`

In [Earlier](../getting-started/local-setup#image-section), we discussed the `image.builder` property in the `config.yaml`.

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
