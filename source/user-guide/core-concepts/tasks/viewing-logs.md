# Viewing logs

In the [Execution view](../workflows/viewing-workflow-executions), selecting a task from the list in the **Nodes** tab will open the task details in the right panel.

Within that panel, in the **Execution** tab, under **Logs**, you will find a link labeled **Live Logs**.

![Live logs links](/_static/images/user-guide/core-concepts/tasks/viewing-logs/live-logs-link.png)

This leads to the **Execution logs tab** of the **Execution details page**:

![Execution logs](/_static/images/user-guide/core-concepts/tasks/viewing-logs/live-logs-execution-logs.png)

The execution logs provide a live view into the standard output of the task execution.

For example, any `print` statements in the tasks Python code will be displayed here.

## Other tabs

Alongside the **Execution logs** tab in the the **Execution details page**, you will also find the **Execution resources** and **Inputs & Outputs** tabs.

{@@ if byoc @@}

## Cloud provider logs

In addition to the **Live Logs** link:

* If your BYOC environment is on AWS, you will also see a **Cloudwatch Logs** link in the execution side bar.
* If your BYOC environment is on GCP, you will also see a **Stackdriver Logs** link in the execution side bar.
* If your BYOC environment is on Azure, you will also see a **Azure Logs** link in the execution side bar.

These are deep links into the logging systems of their respective provider. Assuming you are logged into your cloud provider account with the appropriate permissions, you will be taken to the logs specific to the container in which this particular task execution is running.

{@@ endif @@}
