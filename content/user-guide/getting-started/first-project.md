---
title: First project
weight: 3
variants: "+flyte +serverless +byoc +byok"
---

# First project

In this section we will set up a new project.
This involves creating a local project directory holding your project code
and a corresponding {@= Product =@} project to which you will deploy that code using the `{@= cli =@}` CLI.

{{< if-variant "serverless byoc byok" >}}

## Create a new Union project

Create a new project in the Union UI by clicking on the project breadcrumb at the top left and selecting **All projects**:

![Select all projects](/_static/images/user-guide/getting-started/first-project/select-all-projects.png)

This will take you to the **Projects list**:

![Projects list](/_static/images/user-guide/getting-started/first-project/projects-list.png)

Click on the **New Project** button and fill in the details for your new project.
For this example, let's create a project called **My project**:

```--image-- /_static/images/user-guide/getting-started/first-project/create-new-project.png
:alt: Create new project
:width: 445px
:align: center
```

You now have a project on Union named "My Project" (and with project ID `my-project`) into which you can register your workflows.

{{< note "Default project" >}}
Union provides a default project (called **{@= default_project =@}**) where all your workflows will be registered unless you specify otherwise.
In this section, however, we will be using the project we just created, not the default.
{{< /note >}}

{{< /if-variant >}}
{{< if-variant flyte >}}

## Create a new Flyte project

Create a new project on your local Flyte cluster:

```shell
$ flytectl create project \
      --id "my-project" \
      --labels "my-label=my-project" \
      --description "My Flyte project" \
      --name "My project"
```

You can see the project you just created by going to `http://localhost:30080` in your browser:

![Welcome to Flyte](/_static/images/user-guide/getting-started/first-project/welcome-to-flyte.png)

{{< note "Default project" >}}
Flyte provides a default project (called `flytesnacks`) where all your workflows will be registered unless you specify otherwise.
In this section, however, we will be using the project we just created, not the default.
{{< /note >}}

{{< /if-variant >}}

## Initialize a local project

We will use the `{@= cli =@} init` command to initialize a new local project corresponding to the project created on your {@= Product =@} instance:

```shell
$ {@= cli =@} init --template {@= product =@}-simple my-project
```

The resulting directory will look like this:

```shell
.
├── LICENSE
├── README.md
├── hello_world.py
├── pyproject.toml
└── uv.lock
```

{{< note "Local project directory name same as {@= Product =@} project ID" >}}
It is good practice to name your local project directory the same as your {@= Product =@} project ID, as we have done here.
{{< /note >}}

Next, let's look at the contents of the local project directory.
Continue to [Understanding the code](understanding-the-code.md).
