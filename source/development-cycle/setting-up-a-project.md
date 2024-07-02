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

You now have a project on Union into which you can register your workflows.
The next step is to set up a local workflow directory.

## Creating a local workflow directory using `unionai init`

Earlier, in the [First workflow](../first-workflow/index) section of the guide, we started with a pre-existing example project cloned from git.
In this section we'll start from scratch and create a new project using the `unionai` CLI tool.

We will use the `unionai init` command to create a new workflow directory on your local machine pre-populated with a basic project structure defined by the [`basic-template-imagespec`](https://github.com/flyteorg/flytekit-python-template/tree/main/basic-template-imagespec) found in the [`flyteorg/flytekit-python-template`](https://github.com/flyteorg/flytekit-python-template).

To create the workflow directory, run the following command:

```{code-block} shell
$ unionai init --template basic-template-imagespec my-project
```

## Project structure


If you cd into the `my-project` directory you’ll see the following file structure:

```{code-block} shell
$ cd my-project

$ tree
.
├── LICENSE
├── README.md
├── requirements.txt
└── workflows
    ├── __init__.py
    └── example.py
```

:::{note}
You can create your own conventions and file structure for your Union projects.
The `unionai init` command just provides a good starting point.
:::




[TODO: should rests of this page be its own page?]()



## Running the project in a local Python environment

To quickly try out the code, you can run it in your local Python environment using `unionai run`:

```{code-block} shell
$ unionai run workflows/example.py wf --name 'Albert'
```

Here you are invoking `unionai run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `name` and its value.

You should see the following output:

```{code-block} shell
Hello, Albert!
```

## Passing parameters

`unionai run` enables you to execute a specific workflow using the syntax:

```{code-block} shell
$ unionai run <path/to/script.py> <workflow_or_task_function_name>
```

Keyword arguments can be supplied to `unionai run` by passing them in like this:

```{code-block} shell
--<keyword> <value>
```

For example, above we invoked `unionai run` with script `example.py`, workflow `wf`, and named parameter `name`:

```{code-block} shell
$ unionai run example.py wf --name 'Albert'
```

The value `Albert` is passed for the parameter `name`.

With `snake_case` argument names, you have to convert them to `kebab-case`. For example,

```{code-block} shell
$ unionai run example.py wf --last-name 'Einstein'
```

would pass the value `Einstein` for the parameter `last_name`.

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

