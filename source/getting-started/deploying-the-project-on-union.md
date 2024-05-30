# Deploying the project on Union

## Deploying your project

The process of deploying is called registration.
The phrase "register your workflow" means the same things as "deploy your workflow".

## Register the workflow

```{code-block} shell
$ unionai register workflows --project wine-classification
```

This command does the following:

* Builds the images defined by the `ImageSpec` objects in your code and pushes them to the specified container registry.
* Pushes the workflow code to Union.
* Sets up the workflow DAG and its constituent task containers.
* Registers the workflow in the `dev` domain of your `wine-classification` project in Union (which, recall, you have already created with `uctl`).

## Make your image public

Before you can run the workflow from the Union interface, you must make sure that the image define in your `ImageSpec` is public.

In the GitHub Container Registry, switch the visibility of your container image to Public. For more information, see [Configuring a package's access control and visibility](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility.md#about-inheritance-of-access-permissions-and-visibility).

At this point, you can run the workflow from the Union interface.

:::{warning}
If you try to run a workflow that uses a private container image or an image that is inaccessible for some other reason, the system will return an error:

```
... Failed to pull image ...
... Error: ErrImagePull
... Back-off pulling image ...
... Error: ImagePullBackOff
```
:::
