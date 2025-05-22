---
title: Task input and output
weight: 3
variants: +flyte -serverless +byoc +selfmanaged
---

# Task input and output

The {{< key product_name >}} workflow engine automatically manages the passing of data from task to task, and to the workflow output.

This mechanism relies on enforcing strong typing of task function parameters and return values.
This enables the workflow engine to efficiently marshall and unmarshall values from one task container to the next.

The actual data is temporarily stored in {{< key product_name >}}'s internal object store within your data plane (AWS S3, Google Cloud Storage, or Azure Blob Storage, depending on your cloud provider).

## Metadata and raw data

{{< key product_name >}} distinguishes between the metadata and raw data.

Primitive values (`int`, `str`, etc.) are stored directly in the metadata store, while complex data objects (`pandas.DataFrame`, `FlyteFile`, etc.) are stored by reference, with the reference pointer in the metadata store and the actual data in the raw data store.

## Metadata store

The metadata store is located in the dedicated {{< key product_name >}} object store in your data plane.
Depending on your cloud provider, this may be an AWS S3, Google Cloud Storage, or Azure Blob Storage bucket.

This data is accessible to the control plane. It is used to run and manage workflows and is surfaced in the UI.

## Raw data store

The raw data store is, by default, also located in the dedicated {{< key product_name >}} object store in your data plane.

However, this location can be overridden per workflow or per execution using the **raw data prefix** parameter.

The data in the raw data store is not accessible to the control plane and will only be surfaced in the UI if your code explicitly does so (for example, in a Deck).

<!-- TODO: incorporate the referenced page here -->
For more details, see [Understand How Flyte Handles Data](https://docs.flyte.org/en/latest/concepts/data_management.html).

## Changing the raw data storage location

There are a number of ways to change the raw data location:

* When registering your workflow:
  * With [`uctl register`](), use the flag `--files.outputLocationPrefix`.
  * With [`{{< key cli >}} register`](), use the flag `--raw-data-prefix`.
* At the execution level:
  * In the UI, set the **Raw output data config** parameter in the execution dialog.

These options change the raw data location for **all large types** (`FlyteFile`, `FlyteDirectory`, `DataFrame`, any other large data object).

If you are only concerned with controlling where raw data used by `FlyteFile` or `FlyteDirectory` is stored, you can [set the `remote_path` parameter](./flyte-file-and-flyte-directory#specifying-remote_path-for-a-flytefile-or-flytedirectory) in your task code when initializing objects of those types.

### Setting up your own object store

By default, when {{< key product_name >}} marshalls values across tasks, it stores both metadata and raw data in its own dedicated object store bucket.
While this bucket is located in your {{< key product_name >}} BYOC data plane and is therefore under your control, it is part of the {{< key product_name >}} implementation and should not be accessed or modified directly by your task code.

When changing the default raw data location, the target should therefore be a bucket that you set up, separate from the {{< key product_name >}}-implemented bucket.

For information on setting up your own bucket and enabling access to it, see [Enabling AWS S3](../integrations/enabling-aws-resources/enabling-aws-s3), [Enabling Google Cloud Storage](../integrations/enabling-gcp-resources/enabling-google-cloud-storage), or [Enabling Azure Blob Storage](../integrations/enabling-azure-resources/enabling-azure-blob-storage), depending on your cloud provider.






