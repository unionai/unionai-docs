---
title: Data retention policy
weight: 8
variants: -flyte -serverless +byoc +selfmanaged
---

# Data retention policy

{{< variant byoc >}}
{{< markdown >}}

Data retention polices allow you to control what data is stored in your data plane and for how long.
This allows you to reduce costs by ensuring that you only keep data that you actually need.

Each data plane has its own {{< key product_name >}}-internal object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a {{< key product_name >}} administrator, you can specify retention policies for this data when setting up your data plane.
The policies are specified in discussion with the {{< key product_name >}} team when you set up your {{< key product_name >}} instance.
They are not adjustable through the UI or CLI.

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

Each data plane uses an object store (an AWS S3 bucket, GCS bucket or ABS container) that is used to store data used in the execution of workflows.
As a {{< key product_name >}} administrator, you can specify retention policies for this data when setting up your data plane.

{{< /markdown >}}
{{< /variant >}}

## Data categories

{{< variant byoc >}}
{{< markdown >}}

The retention policy system distinguishes three categories of data:

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

There are three categories of data:

{{< /markdown >}}
{{< /variant >}}

1. Workflow execution data:
   - Task inputs and outputs (that is, primitive type literals)
   - `FlyteFile`/`FlyteDirectory` and other large offloaded data objects (like `DataFrame`s) both in their default locations and in any custom `raw-data-prefix` locations that may have been specified at execution time
   - Flyte `Deck` data.
   - Artifact data.
   - Internal metadata used by {{< key product_name >}}.
2. Fast-registered code:
   - Local code artifacts that will be copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.
3. Flyte plugin metadata (for example, Spark history server data).

{{< variant byoc >}}
{{< markdown >}}

Each category of data is stored in a separate {{< key product_name >}}-managed object store bucket and versioning is enabled on these buckets.
This means that two separate retention policies can be specified for each data category: one for current versions and one for non-current versions.
The result is that there are four distinct retention policies to specify (though in most cases you can stick with the defaults, see below).

{{< /markdown >}}
{{< /variant >}}

> [!NOTE] Object versions are not the same as {{< key product_name >}} entity versions
> The versions discussed here are at the object level and are not related to the versions of workflows,
> tasks and other {{< key product_name >}} entities that you see in the {{< key product_name >}} UI.

## How policies are specified

{{< variant byoc >}}
{{< markdown >}}

A policy determines how long data in a given category and version-state (current vs. non-current) will be retained in the object store before it is automatically deleted.

A policy is specified as a time period in days, or `unlimited` (in which case automatic data deletion is disabled for that category and version-state).

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

The policy will be configured on the object store bucket(s) which you are using for {{< key product_name >}}.
- For AWS S3 buckets use [S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- For GCP GCS buckets use [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle)
- For Azure Blob Storage use [lifecycle management policies](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal)

{{< /markdown >}}
{{< /variant >}}

## Deletion of current versions

For current version, deletion due to a retention period running out means moving the object to a non-current version, which we refer to as _soft-deletion_.

## Deletion of non-current versions

For non-current versions, deletion due to a retention period running out means permanent deletion.

{{< variant byoc >}}
{{< markdown >}}

## Defaults

{{< /markdown >}}
{{< /variant >}}
{{< variant selfmanaged >}}
{{< markdown >}}

## Example policy

{{< /markdown >}}
{{< /variant >}}

|                     | Workflow execution data | Fast-registered code | Flyte-plugin metadata |
| ------------------- | ----------------------- | -------------------- | --------------------- |
| Current version     | unlimited               | unlimited            | unlimited             |
| Non-current version | 7 days                  | 7 days               | 7 days                |

{{< variant byoc >}}
{{< markdown >}}

By default:

{{< /markdown >}}
{{< /variant >}}

- The retention policy for _current versions in all categories_ is `unlimited`, meaning that auto-deletion is disabled.

  - If you change this to a specified number of days, then auto-deletion will occur after that time period, but because it applies to current versions the data object will be soft-deleted (that is, moved to a non-current version), not permanently deleted.

- The retention policy for _non-current versions in all categories_ is `7 days`, meaning that auto-deletion will occur after 7 days and that the data will be permanently deleted.

## Attempting to access deleted data

If you attempt to access deleted data, you will receive an error:

- When workflow node input/output data is deleted, the Input/Output tabs in the UI will display a _Not Found_ error.
- When `Deck` data is deleted, the `Deck` view in the UI will display a _Not Found_ error.
- When artifacts are deleted, the artifacts UI will work, but it will display a URL that points to no longer existing artifact.

To remedy these types of errors, you will have to re-run the workflow that generated the data in question.

- When fast registered code data is deleted, the workflow execution will fail.

To remedy this type of error, you will have to both re-register and re-run the workflow.

## Separate sets of policies per cluster

If you have a multi-cluster set up, you can specify a different set of retention policies (one per category) for each cluster.

## Data retention and task caching

When enabling data retention, task caching will be adjusted accordingly. To avoid attempts to retrieve cache data that has already been deleted, the `age` of the cache will always be configured to be less than the sum of both retention periods.
