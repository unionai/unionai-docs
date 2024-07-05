# Remote dependencies with ImageSpec

During the development cycle you will want to be able to run your workflows both locally on your machine and remotely on Union,
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

```{rli} https://raw.githubusercontent.com/flyteorg/flytekit-python-template/main/basic-union-template/%7B%7Bcookiecutter.project_name%7D%7D/workflows/example.py
:language: python
:lines: 1-12
```

The `init` template includes all available `ImageSpec` parameters. Apart from the two parameters above (`name` and `requirements`), they are all commented out.
The two uncommented ones are the only ones needed for this example.

{@@ elif byoc @@}

```{rli} https://raw.githubusercontent.com/flyteorg/flytekit-python-template/main/basic-union-byoc-template/%7B%7Bcookiecutter.project_name%7D%7D/workflows/example.py
:language: python
:lines: 1-31
```

The `init` template includes all available `ImageSpec` parameters but apart from the two parameters above (`name` and `requirements`), they are all commented out.

Since you are running on Union BYOC, you will have to uncomment and configure the `registry` parameter as well.

Make sure that:

* You substitute the actual name of the registry you are using for `<my-registry>`.
  (For example if you are using GitHub's GHCR, you would use `https://ghcr.io/<my-github-org>`).

* You have Docker installed locally and are logged into the registry.

* The image, once pushed to the registry, is accessible to Union
  (for example, for GHCR, make sure the image is public).

This parameter is needed because with Union BYOC, when you register a workflow, the image is built on your local machine and pushed to the registry you specify.
On the other hand, with Union Serverless, when you register a workflow, the image is built and stored in the cloud on Union and therefore does not need to be pushed to a registry.

For more details on setting this up, see [Setting up container image handling](../first-workflow/setting-up-container-image-handling).

{@@ endif @@}

## Building the task container image

{@@ if serverless @@}

When you [register your workflow code](), Union builds the container images specified by the `ImageSpec` blocks using its `ImageBuilder` service in the cloud. These images are then stored in Union's own container registry. All of this is done transparently and does not require any set up by the user.

When a task that uses that image is executed on Union, the image will be pulled from Union's native registry and installed in he container that runs the task.

```{note}
Transparent building and storing of images with `ImageBuilder` is currently only supported on Union Serverless.
For information on how to set up image handling on Union BYOC, see [the BYOC version of this page](https://docs.union.ai/byoc/development-cycle/remote-dependencies-with-image-spec.html) and [Setting up container image handling](https://docs.union.ai/byoc/first-workflow/setting-up-container-image-handling.html).
```

{@@ elif byoc @@}

When you [register your workflow code](), your locally installed Union SDK will build the container image defined in the `ImageSpec` block and push it to the registry you specified.
When a task that uses that image is executed on Union, the image will be pulled from the registry and installed in he container that runs the task.

```{note}
Local building of container images and pushing them to your configured registry is only done on Union BYOC.
With Union Serverless, images are built and stored transparently by the `ImageBuilder` service on Union in the cloud.
For more information, see [the Serverless version of this page](https://docs.union.ai/serverless/development-cycle/remote-dependencies-with-image-spec.html).
```

{@@ endif @@}
