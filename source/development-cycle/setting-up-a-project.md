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

In everyday use, the term "project" is often used to refer to not just the Union entity that holds a set of workflows, but also to the local directory in which you are developing those workflows, and to the GitHub (or other SCM) repository that you are using to store the same workflow code.

To avoid confusion, in this guide we will stick to the following naming conventions:

* **Union project**: The entity in your Union instance that holds a set of workflows, as described above. Often referred to simply as a **project**.
* **Workflow directory**: The local directory in which you are developing workflows.
  This directory does not necessarily correspond one-to-one with a Union project.
  Often you will have multiple workflow directories that are all registered to a single Union project.
* **Workflow repository**: The GitHub (or other SCM) repository that you are using to store and manage your workflow code.
  This repository does not necessarily correspond one-to-one with either workflow directory or a Union project.

## Create a Union project

You can create a new project in the Union UI:

1. Navigate to the Projects page.
![Projects page navigation](/_static/images/projects-nav.png)
2. Click **New Project**.
![New project button](/_static/images/project-new-project-btn.png)
3. In the project creation modal, enter a **Project Name**, **Project ID**, and optional **Description**.
![Project creation modal](/_static/images/project-creation-modal.png)
For the purposes of this exercise, name the project **Basic example**, and give it the ID `basic-example`.
4. Click **Create Project**.

You now have a project on Union into which you can register your workflows.
The next step is to set up a local workflow directory.

## Creating a local workflow directory using `unionai init`

Earlier, in the [First workflow](../first-workflow/index) section of the guide, we started with a pre-existing example project, cloned from git.
In this section we'll start from scratch and create a new project using the `unionai` CLI tool.

We will use the `unionai init` command to create a new workflow directory on your local machine pre-populated with a basic project structure defined by the [`basic-union-template`](https://github.com/flyteorg/flytekit-python-template/tree/main/basic-union-template) found in the repository [`flyteorg/flytekit-python-template`](https://github.com/flyteorg/flytekit-python-template).

To create the workflow directory, run the following command:

```{code-block} shell
$ unionai init --template basic-union-template basic-example
```

## Directory structure

If you `cd` into the `basic-example` directory you’ll see the following file structure:

```{code-block} shell
$ cd basic-example

$ tree
.
├── LICENSE
├── README.md
├── requirements.txt
└── workflows
    ├── __init__.py
    └── example.py
```

You can create your own conventions and file structure for your Union projects.
The `unionai init` command just provides a good starting point.

However, the separate `workflows` subdirectory and the contained `__init__.py` file are significant.
We will discuss them when we cover the [registration process]().
