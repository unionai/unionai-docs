# First project

In this section we will set up a new project.
This involves creating a local project directory holding your project code
and a corresponding {@= Product =@} project to which you will deploy that code using the `{@= cli =@}` CLI.

{@@ if serverless or byoc or byok @@}

## Create a new Union project

Create a new project in the Union UI by clicking on the project breadcrumb at the top left and selecting **All projects**:

![Select all projects](/_static/images/user-guide/getting-started/first-project/select-all-projects.png)

This will take you to the **Projects list**:

![Projects list](/_static/images/user-guide/getting-started/first-project/projects-list.png)

Click on the **New Project** button and fill in the details for your new project.
For this example, let's create a project called **My project**:

```{image} /_static/images/user-guide/getting-started/first-project/create-new-project.png
:alt: Create new project
:width: 445px
:align: center
```

You now have a project on Union named "My Project" (and with project ID `my-project`) into which you can register your workflows.

:::{admonition} Default project
Union provides a default project (called **{@= default_project =@}**) where all your workflows will be registered unless you specify otherwise.
In this section, however, we will be using the project we just created, not the default.
:::


## Initialize a local project

We will use the `union init` command to initialize a new local project, corresponding to the project created on your Union instance:

```{code-block} shell
$ union init --template union-simple my-project
```

Here we use the `union-simple` template to create a new local project directory called `my-project`.
The resulting directory will look like this:

```{code-block} shell
.
├── LICENSE
├── README.md
├── hello_world.py
├── pyproject.toml
└── uv.lock
```

:::{admonition} Local project directory name same as Union project ID
It is good practice to name your local project directory the same as your Union project ID, as we have done here.
:::

Next, let's look at the contents of the local project directory.
[Understanding the code](understanding-the-code.md).

{@@ elif flyte @@}

## Create a new Flyte project

Create a new project on your local Flyte cluster:

```{code-block} shell
$ flytectl create project \
      --id "my-project" \
      --labels "my-label=my-project" \
      --description "My Flyte project" \
      --name "My project"
```

You can see the project you just created by going to `http://localhost:30080` in your browser:

![Welcome to Flyte](/_static/images/user-guide/getting-started/first-project/welcome-to-flyte.png)

:::{admonition} Default project
Flyte provides a default project (called `flytesnacks`) where all your workflows will be registered unless you specify otherwise.
In this section, however, we will be using the project we just created, not the default.
:::


## Initialize a local project

We will use the `pyflyte init` command to initialize a new local project corresponding to the project created on your local Flyte cluster:

```{code-block} shell
$ pyflyte init my-project
```

The resulting directory will look like this:

```{code-block} shell
my-project
├── LICENSE
├── README.md
├── requirements.txt
└── workflows
    ├── __init__.py
    └── example.py
```

:::{admonition} Local project directory name same as Flyte project ID
It is good practice to name your local project directory the same as your Flyte project ID, as we have done here.
:::

Next, let's look at the contents of the local project directory.
Continue to [Understanding the code](understanding-the-code.md).

{@@ endif @@}