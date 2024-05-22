# Launching workflows

From the [individual workflow view](viewing-workflows.md#workflow-view) (accessed, for example, by selecting a workflow in the [**Workflows** list](viewing-workflows.md#workflows-list)) you can select **Launch Workflow** in the top right:

![](/_static/images/launching-a-workflow.png)

This opens the **Create New Execution** dialog for workflows:

![](/_static/images/create-new-execution.png)

Here you can:

* Select the **Workflow Version** to launch.
* Select the **Launch Plan** to be used.
* Enter any Inputs that the workflow may require.

Selecting **Advanced options** expands the dialog:

![](/_static/images/advanced-options-1.png)

![](/_static/images/advanced-options-2.png)

* **IAM Role:** If your task code needs an IAM role that you have configured in your cloud environment, and you want to specify it specifically for this execution (as opposed to for all executions of a workflow or globally for this project) then add it here.
* **Kubernetes Service Account**: If your workflow code needs to access a service that you have configured in your cloud environment, and you want to specify that account specifically for this execution (as opposed to for all executions of this workflow or globally for this project) then add the name of that account here.
* **Labels**: Open the drop-down arrow to add labels.
* **Annotations**: Open the dropdown arrow to add annotations.
* **Disable all notifications**: A checkbox.
* **Raw output data config**: By default, workflow output will be written to the built-in metadata storage.
Alternatively, you can specify a custom location for output at the organization, project-domain, or individual execution levels.
This field is for specifying this setting at the execution level.
If this field is filled in it overrides any settings at higher levels.
The parameter is expected to be a URL to a writable resource (for example, `http://s3.amazonaws.com/my-bucket/`).
* **Max parallelism**: The maximum number of parallel executions.
* **Override interruptible flag**: A three-value setting:
  * **Interruptible (disabled)**: This execution will not be interruptible, regardless of the workflow-level setting.
  * **Interruptible (no override)**: The interruptible status of this execution will be determined by the workflow-level setting.
  * **Interruptible (enabled)**: This execution will be interruptible, regardless of the workflow-level setting
* **Caching**: If **Overwrite cached outputs** is enabled, then Flyte will ignore all previously computed and stored outputs for this single execution and run all calculations again, overwriting any cached data after a successful execution.

Finally, select **Launch** to launch the execution. This will take you to the [Execution view](viewing-workflow-executions).