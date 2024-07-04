# Looking at the dependencies

You will notice that we have defined two requirements files, `image-requirements.txt` and `local-requirements.txt`:

## image-requirements.txt

```{code-block} text
pandas
scikit-learn
```

## local-requirements.txt

```{code-block} text
unionai
flytekitplugins-envd
-r image-requirements.txt
```

We use two requirements files because the workflow needs to be able to run in two different environments:
* Remotely on Union or the local demo cluster on your machine
* Locally in your Python environment

When deployed to Union (or your local demo cluster), each task in a Union workflow runs inside a container.
The `image-requirements.txt` file includes all (and only) the packages needed to run the workflow in the container.
This file is used to define the container image through the `ImageSpec` object (which we will see when we look at the Python code).

The `local-requirements.txt` file includes the contents of `image-requirements.txt` and adds the `unionai` and `flytekitplugins-envd` packages.

The `unionai` package is needed in your local requirements file to define workflows and tasks and to provide the `unionai` CLI. (Though you may already have installed `unionai`, it is good practice to have it listed in this file as well.) `unionai` (which would install `flytekit`) is not need in the `image-requirements.txt` file because the task container image  is based on an image that already includes `flytekit` (you will see this in the `ImageSpec` definition later).

The `flytekitplugins-envd` package is needed in your local requirements file because it provides (together with your local Docker installation) the functionality to build and push the container image defined by the `ImageSpec`.
`flytekitplugins-envd` is not needed in the `image-requirements.txt` file because it is not needed in the container image itself.

The `image-requirements.txt` file includes the `pandas` and `scikit-learn` packages, which are used by the task code in the following example project. These dependencies are needed both locally and in the container image.

