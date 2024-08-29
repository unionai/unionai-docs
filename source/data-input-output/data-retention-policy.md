# Data retention policy

Each data plane has its own Union-internal object store (and AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
This includes task input-output metadata, task input-output raw data, Flyte Decks data, and fast registration data.

When setting up your data plane (or multiple data planes, if you are using a [multi-cluster set up](../data-plane-setup/multi-cluster)) you can specify the data retention policy for that data plane.
This policy determines how long workflow execution data will be stored in the object store before it is automatically deleted.

A retention policy is specified as a maximum time in days or, "unlimited", in the case where automatic data deletion is disabled.

## Data retention is specified at set up time

The retention policy is one of the items that you specify in discussion with the Union team when you set up your Union BYOC instance.
This not a setting that is user-adjustable through UI or CLI.

## Examples

For example, if you have a single-cluster set up and specify a 30day data retention policy, then all workflow data in your Union instance will be deleted after 30 days.
This means that if you register and run a workflow, its associated data, including the workflow code itself, will be deleted after 30 days.
If you attempt to access a workflow execution, or its associated data,  that is older than 30 days, you will receive an error in the UI.
To remedy this you would have to re-register and re-run the workflow.

If you have multi-cluster setup, you can specify different retention policies for each cluster. For example if you have partitioned your instance so that `development` and `staging` domains are on one cluster while `production` is on another, you could specify a 30 day retention for `development` and `staging` while having an unlimited retention for `production`.

