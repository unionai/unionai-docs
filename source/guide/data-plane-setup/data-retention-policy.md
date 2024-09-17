# Data retention policy

Data retention polices allow you to control what data is stored in your data plane and for how long.
This allows you to reduce costs by ensuring that you only keep data that you actually need.

Each data plane has its own Union-internal object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a Union administrator, you can specify retention policies for this data when setting up your data plane.
The policies are specified in discussion with the Union team when you set up your Union instance.
They are not adjustable through the UI or CLI.

## Data categories

The retention policy system distinguishes three categories of data:

1. Workflow execution data:
    * Task inputs and outputs (that is, primitive type literals)
    * `FlyteFile`/`FlyteDirectory` and other large offloaded data objects (like `DataFrame`s) both in their default locations and in any custom `raw-data-prefix` locations that may have been specified at execution time
    * Flyte `Deck` data.
    * Artifact data.
    * Internal metadata used by Union.
2. Fast-registered code:
    * Local code artifacts that will be copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.
3. Flyte plugin metadata (for example, Spark history server data).

Each category of data is stored in a separate Union-managed object store bucket and versioning is enabled on these buckets.
This means that two separate retention policies can be specified for each data category: one for current versions and one for non-current versions.
The result is that there are four distinct retention policies to specify (though in most cases you can stick with the defaults, see below).

:::{admonition} Object versions are not the same as Union entity versions
The versions discussed here are at the object level and are not related to the versions of workflows, tasks and other Union entities that you see in the Union UI.
:::

## How policies are specified

A policy determines how long data in a given category and version-state (current vs. non-current) will be retained in the object store before it is automatically deleted.

A policy is specified as a time period in days, or `unlimited` (in which case automatic data deletion is disabled for that category and version-state).

## Deletion of current versions

For current version, deletion due to a retention period running out means moving the object to a non-current version, which we refer to as *soft-deletion*.

## Deletion of non-current versions

For non-current versions, deletion due to a retention period running out means permanent deletion.

## Defaults

|                     | Workflow execution data | Fast-registered code | Flyte-plugin metadata |
|---------------------|-------------------------|----------------------|-----------------------|
| Current version     | unlimited               | unlimited            | unlimited             |
| Non-current version | 7 days                  | 7 days               | 7 days                |


By default:

* The retention policy for *current versions in all categories* is `unlimited`, meaning that auto-deletion is disabled.
    * If you change this to a specified number of days, then auto-deletion will occur after that time period, but because it applies to current versions the data object will be soft-deleted (that is, moved to a non-current version), not permanently deleted.

* The retention policy for *non-current versions in all categories* is `7 days`, meaning that auto-deletion will occur after 7 days and that the data will be permanently deleted.

## Attempting to access deleted data

If you attempt to access deleted data, you will receive an error:

* When workflow node input/output data is deleted, the Input/Output tabs in the UI will display a *Not Found* error.
* When Flyte `Deck` data is deleted, the `Deck` view in the UI will display a *Not Found* error.
* When artifacts are deleted, the artifacts UI will work, but it will display an URL that points to no longer existing artifact.
* When fast registered code data is deleted, flyte tasks will fail downloading the code artifacts, displaying a *Not Found* error in the console.

To remedy these types of errors, you will have to re-run the workflows that generated the data in question.

## Separate sets of policies per cluster

If you have a multi-cluster set up, you can specify a different set of retention policies (one per category) for each cluster.

## Data retention and task caching

When enabling data retention, task caching will be adjusted accordingly. To avoid attempts to retrieve cache data that has already been deleted, the `age` of the cache will always be configured to be less than the sum of both retention periods.
