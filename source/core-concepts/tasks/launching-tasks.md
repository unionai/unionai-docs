# Launching tasks

From the [individual task view](viewing-tasks.md#task-view) (accessed, for example, by selecting a task in the [**Tasks** list](viewing-tasks.md#tasks-list)) you can select **Launch Task** in the top right:

![](/_static/images/launching-a-task.png)

This opens the **Create New Execution** dialog for tasks:

![](/_static/images/create-new-execution-task-1.png)

![](/_static/images/create-new-execution-task-2.png)

The settings are similar to those for workflows, with a few missing:

* **Task Version**: Select which version of the task to launch.
* **IAM Role:** If your task code needs an IAM role that you have configured in your cloud environment, and you want to specify it specifically for this execution (as opposed to for all executions of a workflow or globally for this project) then add it here.
* **Kubernetes Service Account**: If your workflow code needs to access a service that you have configured in your cloud environment, and you want to specify that account specifically for this execution (as opposed to for all executions of a workflow or globally for this project) then add the name of that account here.
* **Inputs**: Enter any parameters that the task may require.
* **Override interruptible flag**: A three-value setting:
  * **Interruptible (disabled)**: This execution will not be interruptible, regardless of the workflow-level setting.
  * **Interruptible (no override)**: The interruptible status of this execution will be determined by the workflow-level setting.
  * **Interruptible (enabled)**: This execution will be interruptible, regardless of the workflow-level setting
* **Caching**: If **Overwrite cached outputs** is enabled, then Flyte will ignore all previously computed and stored outputs for this single execution and run all calculations again, overwriting any cached data after a successful execution.

Finally, select **Launch** to launch the execution. This will take you to the [Execution view](../workflows/viewing-workflow-executions).
