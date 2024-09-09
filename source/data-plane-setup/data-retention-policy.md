# Data retention policy

Data retention polices allow you to control what data is stored in your data plane and for how long.
This allows you to reduce costs by ensuring that you only keep data that you actually need.

Each data plane has its own Union-internal object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a Union administrator, you can specify retention policies for this data when setting up your data plane.
The policies are specified in discussion with the Union team when you set up your Union instance.
They are not adjustable through the UI or CLI.

The Union team can set up separate policies for each of the following four categories of data:

1. Task inputs and outputs (that is, primitive type literals, not `FlyteFile`/`FlyteDirectory` data) & Flyte `Deck` data & `FlyteFile`/`FlyteDirectory` data (in its default location in the object store, as opposed to any custom location you may specify) & any auto serialised workflow/task output data 
2. Fast registered code when using `union register` or `union run` or `union run --copy-all`
3. Flyte plugin metadata (for example, Spark history server data).

## Specifying the retention period

A policy determines how long data in a given category will be retained in the object store before it is automatically deleted.
It is specified as a time period in days, or `unlimited` (in which case automatic data deletion is disabled for that category).
Since we enable versioning in the Union managed object store buckets, you are able to configure two retention periods for each category:

1. Retention for current versions (default: `unlimited`)

On default, retention for current versions is disabled. If a retention period for current versions of X days is defined, a data object older than X days will be soft deleted and move to a non-current version of this data object.

2. Retention for non-current versions (default: `7 Days`)

After 7 days a data object was soft deleted (manually or by retention for current versions), the data object will be deleted permanently.

## Attempting to access deleted data

If you attempt to access a deleted workflow execution or any of tis associated data, you will receive an error.
To remedy this, you will have to re-register and re-run the workflow.
( I feel like we should be more specific here. e.g. explain whats expected for the different categories of data?)

## Separate sets of policies per cluster

If you have a multi-cluster set up, you can specify a different set of retention policies (one per category) for each cluster.


## FAQ

1. How does data retention work with caching enabled tasks?
When enabling data retention, task caching will be adjusted accordingly. To avoid trying to retrieve cache data, which is already deleted, we'll always configure the `age` of the cache to be smaller than the sum of both retention periods. 
