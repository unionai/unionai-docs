# Data retention policy

Each data plane has its own Union-internal object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a Union administrator, you can specify retention policies for this data when setting up your data plane.
The policies are specified in discussion with the Union team when you set up your Union instance.
They are not adjustable through the UI or CLI.

The Union team can set up separate policies for each of the following four categories of data:

1. Task inputs and outputs (that is, primitive type literals, not `FlyteFile`/`FlyteDirectory` data).
2. `FlyteFile`/`FlyteDirectory` data (in its default location in the object store, as opposed to any custom location you may specify).
3. Flyte `Deck` data.
4. Fast registered code and plugin metadata (for example, Spark history server data).

## Specifying the retention period

A policy determines how long data in a given category will be retained in the object store before it is automatically deleted.
It is specified as a time period in days, or `unlimited` (in which case automatic data deletion is disabled for that category).
If you choose not to explicitly specify a retention policy for a category, the default is `unlimited`.

## Attempting to access deleted data

If you attempt to access a deleted workflow execution or any of tis associated data, you will receive an error.
To remedy this, you will have to re-register and re-run the workflow.

## Separate sets of policies per cluster

If you have a multi-cluster set up, you can specify a different set of retention policies (one per category) for each cluster.
