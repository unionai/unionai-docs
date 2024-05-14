# Web console

## Logging in

Once your organization has been onboarded with Union and your user accounts have been provisioned, go to the endpoint URL provided to you by the Union team.
It will be specific to your organization. Something like:

```{code-block} shell
https://<company>.<region>.unionai.cloud
```
You will be able to log in to your Union account here.

## Choose a project and domain

After logging in successfully, you will see a list of your projects:

![Project list](/_static/images/project-list.png)

The **Project list** includes all (non-archived) projects in your organization.
You can search for a project by name.
Each project has three domains: **development**, **staging**, and **production**.
To examine a project, select one of its domains.
This will take you to the [execution list](execution-list) for that project and domain.

## Left navigation

The left navigation provides access to all the major parts of the Union web console.

![Left navigation](/_static/images/left-navigation.png)

### Project-domain specific links

The top of the left navigation shows links to views for the current project-domain combination:

* **Projects**: Takes you to the [project list](index).
* **Executions**: Takes you to the [execution list](execution-list).
* **Workflows**: Takes you to the [workflow list](workflow-list).
* **Tasks**: Takes you to the [task list](task-list).
* **Launch Plans**: Takes you to the [launch plan list](launch-plan-list).

When no project-domain combination is selected (for example, when you first log into your organization) the left navigation will only display the **Projects** link at the top and the organization- and user- specific links at the bottom.

Once you navigate to a project and domain they will be set to be the current ones and from that point onward the left navigation will show the links for that project-domain combination.

### Organization-specific links

The bottom of the left navigation shows links to views for your organization:

* **Usage**: Takes you to the [Usage view](usage).
* **Users**: Takes you to the [**User Management** dialog](../administration/user-management).

### User-specific links

* The user ID link displays your identity and lets you sign out.

```{toctree}
:maxdepth: 2
:hidden:

execution-list
execution-view
logging
task-level-monitoring
workflow-list
workflow-view
launching-workflows-and-tasks
task-list
task-view
launch-plan-list
launch-plan-view
artifact-list
artifact-view
usage
```
