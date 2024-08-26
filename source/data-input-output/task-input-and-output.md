# Task input and output

The Union workflow engine automatically manages the passing of data from task to task (and to the workflow output).

This mechanism relies on on enforcing [strong typing]() of task function parameters and return values.
This enables the workflow engine to efficiently marshall and unmarshall values from one task container to the next.

The actual data is temporarily stored in a dedicated object store within your data plane (AWS S3, GCS, etc, depending on your cloud provider).

## Metadata and raw data

The system distinguishes between the metadata and raw data.

Primitive values (`int`, `str`, etc.) are stored directly in the metadata store while complex data objects (`pandas.DataFrame`, `FlyteFile`, etc.) are stored by reference, with the reference pointer in the in metadata store and the actual data in the raw data store.

## Metadata store

The metadata store is located in the dedicated Union object store in your data plane. Depending on your cloud provider, this may be an AWS S3 or GCS bucket.

This data is accessible to the control plane. It is used to run and manage workflows and is surfaced in the UI.

## Raw data store

The raw data store is, by default, also located in the dedicated Union object store in your data plane.

However, this location can be overridden per workflow or per execution using the **raw data prefix** parameter (see [Changing the raw data storage location](TODO)).

The data in the raw data store is not accessible to the control plane and will only be surfaced in the UI if your code explicitly does so (through, for example, a Flyte Deck).

See [Understand How Flyte Handles Data](https://docs.flyte.org/en/latest/concepts/data_management.html) for more details.

## Changing the raw data storage location

There are a number of ways to change the raw data location:

* When registering your workflow:
  * With [`uctl register`](https://docs.flyte.org/en/latest/flytectl/gen/flytectl_register.html), use the flag `--files.outputLocationPrefix`.
  * With [`union register`](https://docs.flyte.org/en/latest/api/flytekit/pyflyte.html#pyflyte-register), use the flag `--raw-data-prefix`.
* At the execution level:
  * In the UI, set the **Raw output data config** parameter in the execution dialog.

These options change the raw data location for **all large types** (`FlyteFile`, `FlyteDirectory`, `DataFrame`, any other large data object).

If you are only concerned with controlling where raw data used by [`FlyteFile`](./flyte-file-and-flyte-directory) or [`FlyteDirectory`](./flyte-file-and-flyte-directory) is stored, you can set the `remote_path` parameter in your task code when initializing objects of those types.

### Setting up your own object store

By default, when Union marshalls values across tasks it stores both metadata and raw data in its own dedicated object store bucket.
While this bucket is located in your Union BYOC data plane and is therefore under your control, it is part of the Union implementation and should not be accessed or modified directly by your task code.

When changing the default raw data location, the target should therefore be a bucket that you set up, separate from the Union-implementation bucket.

For information on setting up your own bucket, and enabling access to it, see [Enabling AWS S3](../integrations/enabling-aws-resources/enabling-aws-s3) or [Enabling Google Cloud Storage](../integrations/enabling-gcp-resources/enabling-google-cloud-storage), depending on your cloud provider.






