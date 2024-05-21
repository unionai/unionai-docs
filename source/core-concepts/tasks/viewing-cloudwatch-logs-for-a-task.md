# Viewing Cloudwatch logs for a task

:::{note}

This section applies to Union instances on AWS.

:::

In the [Execution view](../workflows/viewing-workflow-executions), selecting a task from the list in the **Nodes** tab will open the task details in the right panel.

Within that panel, in the **Execution** tab, under **Logs**, you will find a link labeled **Cloudwatch Logs**.

![](/_static/images/cloudwatch-logs.png)

This is a deep link into the Cloudwatch system.
Assuming you are logged into your AWS account with the appropriate role, you will be taken to the Cloudwatch logs specific to the container in which this particular task is running.
