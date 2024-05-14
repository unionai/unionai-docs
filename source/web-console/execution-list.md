# Execution list

The **Execution list** shows all executions in a project and domain combination.
An execution represents a single run of all or part of a workflow (including subworkflows and individual tasks).

This is the default view when you select a project and domain from the [**Projects list**](index).
You can also access it from the **Executions** link in the left navigation.

![Execution list](/_static/images/execution-list.png)

## Domain Settings

This section displays any domain-level settings that have been configured for this project-domain combination. They are:

* Security Context
* Labels
* Annotations
* Raw output data config
* Max parallelism

## All Executions in the Project

For each execution in this project and domain you can see the following:

* **Start time**: Select to view the [individual execution](execution-view).
* **Workflow/Task**: The [individual workflow](workflow-view) or [individual task](task-view) that ran in this execution.
* **Version**: The version of the workflow or task that ran in this execution.
* **Launch Plan**: The [Launch Plan](launch-plan-view) that was used to launch this execution.
* **Schedule**: The schedule that was used to launch this execution (if any).
* **Execution ID**: The ID of the execution.
* **Status**: The status of the execution. One of **QUEUED**, **RUNNING**, **SUCCEEDED**, **FAILED** or **UNKNOWN**.
* **Duration**: The duration of the execution.
