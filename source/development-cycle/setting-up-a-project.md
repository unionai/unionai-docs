# Setting up a project

In Union, your work is organized in a hierarchy with the following structure:

{@@ if serverless @@}

* **Account**: Your account on Union, tied to your GitHub identity.
* **Domains**: Within your account there are three domains, `development`, `staging`, and `production`, used to organize your code during the development process.
* **Projects**: Orthogonal to domains, projects are used to organize your code into logical groups. You can create as many projects as you need.

A given workflow will reside in a specific project. For example, let's say `my_workflow` is a workflow in `my_project`.
When you start working on `my_workflow` you would typically register it in the project-domain `my_project/development`.
As you work on successive iterations of the workflow you might promote `my_workflow` to `my_project/staging` and eventually  `my_project/production`.
Promotion is done simply by [re-registering the workflow to the new project-domain]().

{@@ elif byoc @@}

* **Organization**: Your company's Union instance, accessible at a specific URL like `union.my-company.com`.
* **Domains** Within an organization there are (typically) three domains, `development`, `staging`, and `production`, used to organize your code during the development process.
You can configure a custom set of domains to suit your needs during [onboarding](../data-plane-setup/configuring-your-data-plane).
* **Projects**: Orthogonal to domains, projects are used to organize your code into logical groups. You can create as many projects as you need.

A given workflow will reside in a specific project. For example, let's say `my_workflow` is a workflow in `my_project`.
When you start work on `my_workflow` you would typically register it in the project-domain `my_project/development`.
As you work on successive iterations of the workflow you might promote `my_workflow` to `my_project/staging` and eventually  `my_project/production`.
Promotion is done simply by [re-registering the workflow to the new project-domain]().

{@@ endif @@}

## Terminology

In everyday use the term "project" is often used to refer to not just the Union entity that holds a set of workflows, but also to the local directory in which you are developing those workflows, and to the GitHub (or other SCM) repository that you are using to store the same workflow code.

To avoid confusion, in this guide we will stick to the following naming conventions:

* **Union Project**: The entity in your Union instance that holds a set of workflows, as described above. Often referred to simply as a **project**.
* **Workflow directory**: The local directory in which you are developing workflows.
  This directory does not necessarily correspond one-to-one with a Union project.
  Often you will have multiple workflow directories that correspond to a single Union project.
* **Workflow repository**: The GitHub (or other SCM) repository that you are using to store and manage your workflow code.
  This repository does not necessarily correspond one-to-one with either workflow directory or a Union project, though it may correspond to at least the latter.

## Create a Union project

You can create a new project in the Union UI:

1. Navigate to the Projects page.
![Projects page navigation](/_static/images/projects-nav.png)
2. Click **New Project**.
![New project button](/_static/images/project-new-project-btn.png)
3. In the project creation modal, enter a **Project Name**, **Project id**, and optional **Description**.
![Project creation modal](/_static/images/project-creation-modal.png)
4. Click **Create Project**.

[DONE TO HERE]()


When organizing your work you will create projects on Union

Earlier, in the [First workflow](../first-workflow/index) section of the guide, we started with a pre-existing example project cloned from git.

In this section we'll start from scratch and create a new project using the `unionai` CLI tool.

The

Projects in Union are used to organize and manage your workflows.








## Creating a project locally using `unionai init`

We will use the `unionai` (the CLI tool that ships with `unionai`) to quickly initialize the local project from a template.
The `wine-classification` example is among the installable examples published in the GitHub repository [`flyteorg/flytekit-python-template`](https://github.com/flyteorg/flytekit-python-template).

Install the example, and `cd` into it:

```{code-block} shell
[~]:wine-classification
$ unionai init --template wine-classification wine-classification

[~]:wine-classification
$ cd wine-classification

[~/wine-classification]:wine-classification
$
```

:::{note}
If you need to use a Dockerfile in your project instead of ImageSpec, you can use the Dockerfile template:

```{code-block} shell
unionai init --template basic-template-imagespec my_project
```
:::

### Project structure

If you examine the `wine-classification` directory you’ll see the following file structure:

```{code-block} shell
[~/wine-classification]:wine-classification
$ tree
.
├── LICENSE
├── README.md
├── local-requirements.txt
├── image-requirements.txt
└── workflows
    ├── __init__.py
    └── example.py
```

:::{note}
You can create your own conventions and file structure for your Union projects.
The `unionai init` command just provides a good starting point.
:::

### Install the local dependencies

We will explain the significance of the two requirements files later.
For now, you just need to install the local dependencies.
Make sure that you have activated your `wine-classification` conda environment, then install the dependencies from `local-requirements.txt`:

```{code-block} shell
[~/wine-classification]:wine-classification
$ pip install -r local-requirements.txt
```


## Running the project in a local Python environment

To quickly try out the code, you can run it in your local Python environment using `unionai run`:

```{code-block} shell
[~/wine-classification]:wine-classification
$ unionai run workflows/wine_classification_example.py \
              training_workflow \
              --hyperparameters '{"C": 0.1}'
```

Here you are invoking `unionai run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `hyperparameters` and its value.

You should see the following output:

```{code-block} shell
LogisticRegression(C=0.1, max_iter=3000)
```

This output above tells you that your workflow was executed successfully, but little else.
To see actual results, we will need to run the workflow in a local Kubernetes cluster (see below).

### Passing parameters

`unionai run` enables you to execute a specific workflow using the syntax:

```{code-block} shell
$ unionai run <path/to/script.py> <workflow_or_task_function_name>
```

Keyword arguments can be supplied to `unionai run` by passing them in like this:

```{code-block} shell
--<keyword> <value>
```

For example, if file `foo.py` has a workflow `bar` with a named parameter `baz` , you would invoke it like this:

```{code-block} shell
$ unionai run foo.py bar --baz 'qux'
```

Here the the value `qux` is passed for the parameter `baz`.

With `snake_case` argument names, you have to convert them to `kebab-case`. For example,

```{code-block} shell
$ unionai run foo.py bar --baz-luhrmann 'qux'
```

would pass the value `qux` for the parameter `baz_luhrmann`.

### Why `unionai run` rather than `python`?

You could add a `main` guard at the end of the script like this:

```{code-block} python
if __name__ == "__main__":
    training_workflow(hyperparameters={"C": 0.1})
```

This would let you run it with `python example.py`, though you have to hard code your arguments.

It would become even more verbose if you want to pass in your arguments:

```{code-block} python
if __name__ == "__main__":
    import json
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--hyperparameters", type=json.loads)
    ...  # add the other options

    args = parser.parse_args()
    training_workflow(hyperparameters=args.hyperparameters)Py

```

`unionai run` lets you dispense with this verbosity and run the workflow with the desired arguments conveniently.

