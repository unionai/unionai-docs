---
title: FAQ
weight: 10
variants: -flyte -serverless +byoc +selfmanaged
---

# FAQ

## Onboarding my organization to {{< key product_name >}}

### What information does {{< key product_name >}} need to set up my service?

When you initially onboard your organization to {{< key product_name >}} you must specify which cloud provider(s) you wish to use and the configuration of the machine types you want.

For details, see [Configuring your data plane](../deployment/configuring-your-data-plane).

### How do I change the machine types in my cluster?

If you have already been onboarded and wish to change your machine types, {{< key product_name >}} will need to re-configure your node groups (in AWS) or instance groups (in GCP).
To initiate the process, submit the [Node Group Configuration Change form](https://wkf.ms/3pGNJqh).

## Data storage and handling

### How does {{< key product_name >}} store my data?

When data is passed from task to task in a workflow (and output at the end of the workflow), the workflow engine manages the transfer of these values.

The system distinguishes between metadata and raw data.
Primitive values (`int`, `str`, etc.) are stored directly in the metadata store
while complex data objects (`pandas.DataFrame`, `FlyteFile`, etc.) are stored by reference with the reference in metadata and the actual data in the raw data store.
By default, both metadata and raw data are stored in {{< key product_name >}}'s internal object store, located in your data plane in a pre-configured S3/GCS bucket.

For more details see [Task input and output](./data-input-output/task-input-and-output).

### Can I change the raw data storage location?

Yes. See [Task input and output > Changing the raw storage location](./data-input-output/task-input-and-output#changing-the-raw-data-storage-location).

### Can I use my own blob store for data storage that I handle myself?

Yes. You can certainly configure your own blob storage and then use your chosen library (like `boto3`, for example) to interact with that storage within your task code.
The only caveat is that you must ensure that your task code has access to the storage.

See [Enabling AWS S3](../deployment/enabling-aws-resources/enabling-aws-s3), [Enabling Google Cloud Storage](../deployment/enabling-gcp-resources/enabling-google-cloud-storage), or
[Enabling Azure Blob Storage](../deployment/enabling-azure-resources/enabling-azure-blob-storage).

### Can I control access to my own blob store?

Yes. As with all resources used by your task code, the storage must be accessible from within the cluster running that code on your data plane.
However, the data plane is your own, and you have full control over access.

See [Enabling AWS S3](../deployment/enabling-aws-resources/enabling-aws-s3), [Enabling Google Cloud Storage](../deployment/enabling-gcp-resources/enabling-google-cloud-storage), or
[Enabling Azure Blob Storage](../deployment/enabling-azure-resources/enabling-azure-blob-storage).

### Could someone maliciously delete or otherwise access my raw data?

No.
Your raw data resides in your data plane and is stored either in the default raw data storage or in storage that you set up yourself.
In either case, you control access to it.

The {{< key product_name >}} team does have access to your data plane for purposes of maintenance but does not have access to your raw data, secrets in secret managers, database, etc. unless you choose to permit such access.

Having said that, since the data plane is yours, you are ultimately responsible for preventing access by malicious third parties.

### Can I use s3fs from within a task?

Yes, but you probably don't need to.

[`s3fs`](https://github.com/s3fs-fuse/s3fs-fuse) is a FUSE-based file system backed by Amazon S3.
It is possible to set up `s3fs` in your task container image and use it from within your task code.

However, in most cases using either `FlyteFile`/`FlyteDirectory` or a library like `boto3` to access an S3 bucket directly is preferred (and easier).

If you do need to use `s3fs`, here are the basic steps:

* Set up the S3 bucket that you wish to access.
* Enable access to the bucket from your task code by configuring an appropriate IAM policy. See [Enabling AWS S3](../deployment/enabling-aws-resources/enabling-aws-s3).
* Specify your task container image to have `s3fs` correctly installed and configured.
* In the task decorator, configure a `PodTemplate` to run the task container in privileged mode (see links below).
* In your task code, invoke the `s3fs` command line tool to mount the S3-backed volume.

For example:

```python
subprocess.run(['s3fs', bucket_and_path, mount_point, '-o', 'iam_role=auto'], check=True)
```

See also:

<!-- TODO: add nbck when podtemplste section added in union  [Using PodTemplates](../deployment/flyte-configuration/configuring-podtemplates) -->
* [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

### Can I use BigQuery from within a task?

If your {{< key product_name >}} data plane is running on GCP, access to BigQuery should be enabled by default and bound to the default Google Service Account (referred to in this documentation as **\<UserFlyteGSA>**).
For details see [Enabling GCP resources](../deployment/enabling-gcp-resources).
If you want to bind it to a different GSA, follow the instructions in [Enabling BigQuery](../deployment/enabling-gcp-resources/enabling-bigquery).

To actually access your BigQuery instance from your code, you will need to use a `BigQueryTask`.
For details see [BigQuery connector](../integrations/connectors/bigquery-connector).

## `FlyteFile` and `FlyteDirectory`

### Where do `FlyteFile` and `FlyteDirectory` store their data?

[`FlyteFile` and `FlyteDirectory`](./data-input-output/flyte-file-and-flyte-directory) are two Python classes provided by {{< key product_name >}} to make it easy to pass files from one task to the next within a workflow.
They do this by wrapping a file or directory location path and, if necessary, uploading the referenced file to {{< key product_name >}}'s internal object store to persist it
across task containers.

### Can I accidentally overwrite `FlyteFil`e data?

In general, no.
When a task returns a [`FlyteFile` or `FlyteDirectory`](./data-input-output/flyte-file-and-flyte-directory) whose source is local to the origin container, {{< key product_name >}} automatically uploads it to a location with a randomized path in the raw data store.
This ensures that subsequent runs will not overwrite earlier data.

### Can I use my own blob store for `FlyteFile` and `FlyteDirectory` data storage?

Yes. If you do not want to use the default raw output store that is provided with your data plane you can configure your own storage.

### How do the typed aliases of `FlyteFile` and `FlyteDirectory` work?

`FlyteFile` and `FlyteDirectory` include specific type annotations such as `PDFFile`, `JPEGImageFile`, and so forth.
These aliases can be used when handling a file or directory of the specified type.
For details see [`FlyteFile` and `FlyteDirectory` > Typed aliases](./data-input-output/flyte-file-and-flyte-directory#typed-aliases).

## Building and running workflows

### What SDK should I download and use in workflow code?

You should install the `{{< key kit >}}` package, which will install the Union and Flytekit SDKs and the `{{< key cli >}}` command-line tool.
You will need to use the Flytekit SDK the majority of the time in the code to import core features and use the Union SDK for {{< key product_name >}}-specific features, such as artifacts.

### How do I authenticate `{{< key ctl >}}` and `{{< key cli >}}` CLIs to {{< key product_name >}}?

The command-line tools `{{< key ctl >}}` and `{{< key cli >}}` need to authenticate in order to connect with your {{< key product_name >}} instance (for example, when registering a workflow).
There are three ways to set up authentication.

1. **PKCE**: This is the default method.
When using this method, a browser pops up to authenticate the user.
2. **DeviceFlow**: A URL will be output to your terminal.
Navigate to it in your browser and follow the directions.
3. **ClientSecret:** This is the headless option.
It can be used, for example, by CI bots.
With this method, you create a {{< key product_name >}} application and configure your tools to pass the Client ID and App Secret to {{< key product_name >}}.

These methods are all configured in the `config.yaml` that your `{{< key ctl >}}` or `{{< key cli >}}` command uses. See [Authentication](./development-cycle/authentication) for full details.

Note that if you wish to run or register workflows in a remote SSH session, you will need to authenticate using the DeviceFlow or ClientSecret methods as PKCE attempts to open a local browser from the CLI.

### How do I specify resource requirements for a task?

You can specify either `requests` or `limits` (or both) on the resources that will be used by a specific task when it runs in its container.
This is done by setting the `requests` or `limits` property in the `@{{< key kit_as >}}.task` decorator to a `Resources` configuration object.
Within the `Resources` object you can specify the number of CPU cores, the number of GPU cores, the amount of main memory, the amount of persistent storage, and the amount of ephemeral storage.

You can also override the settings in the `@{{< key kit_as >}}.task` in a for more fine-grained control using the `with_overrides` method when invoking the task function.

See [Customizing task resources](./core-concepts/tasks/task-hardware-environment/customizing-task-resources) for more information.

### What command-line tools should I use to register and run workflows?

You should use the `{{< key cli >}}` CLI to register and run workflows and perform other operations on the command line. The `{{< key cli >}}` CLI is installed when you install the `{{< key kit >}}` package, which will also install the {{< key product_name >}} and Flytekit SDKs.

### How do I fix import errors when running workflows remotely?

If you run your workflows with `{{< key cli >}} run --remote ...`, you may encounter import errors when importing functions, classes, or variables from other modules in your project repository.
For example, if you have the following repository structure, and you want to import a model from `my_model.py`, some constants from `constants.py`, and a helper function from `utils.py` in a task that is defined in `my_workflow.py`, you will encounter import errors unless these Python modules were explicitly added to the image used by the task, since the container running the task does not recognize these modules by default.

```shell
├── requirements.txt
└── my_lib
    ├── __init__.py
    ├── models
    │    ├── __init__.py
    │    └── my_model.py
    └── workflows
        ├── __init__.py
        ├── constants.py
        ├── my_workflow.py
        └── workflow_helper_functions
            ├── __init__.py
            └── utils.py
```

Instead of building a custom Dockerfile that copies all the files and modules in your repository structure, you can do one of the following:
1. Use the `--copy-all` flag in `{{< key cli >}} run --remote ...`
2. Use `{{< key cli >}} register` to register your workflow and run it later.

Both of these methods work by adding all the files within your local project root to the container running your tasks. The project root is defined as the directory immediately above the highest-level directory containing an `__init__.py` file.

### What happens if an automated process launches a very large number of workflows?

By default, {{< key product_name >}} has a built-in limiting mechanism that prevents more than 10,000 concurrent workflow executions per data plane cluster (equivalently, per organization).
This limit can be adjusted on a per-customer basis (talk to the {{< key product_name >}} team).

Executions beyond the limit will be executed as soon as resources become available.
While waiting, the workflow execution will be reported as in the UNKNOWN state.

This limit prevents workflow requests from overwhelming the cluster and, in effect, performing a self-caused denial of service attack.

### How can I constrain the number of parallel executions for large, complex workflows?

Workflows can quickly get complex when dynamic workflows iterate over varying length inputs, workflows call subworkflows, and map tasks iterate over a series of inputs.
There are two levers to control the parallelism of a workflow: `max_parallelism` which controls parallelism at a workflow level, and `concurrency` which controls parallelism at a map task level.
Another way of thinking about this is that `max_parallelism` controls the number of simultaneous executions of all tasks _except_ for map tasks which are controlled separately.
This means that the total number of simultaneous executions during a workflow run cannot exceed `max_parallelism * concurrency` which would be the case if each parallel execution at the workflow level had its own map task.

By default, `max_parallelism` is set to 25. If `concurrency` is not set for a map task, the current default behavior is to execute over all inputs to the map task.
The trade-off that must be balanced when setting `max_parallelism` and `concurrency` is with resource availability at a workflow level.
If parallelism is too high, tasks can time out before resources can be allocated to them, making it important to consider the resource requirements of your tasks that will run in parallel.

When interpreting parallelism in the UI, it is important to note that dynamic workflows will immediately list all planned executions, even if the number exceeds `max_parallelism`.
However, this does not mean that all the executions are running. By toggling any embedded tasks or subworkflows, you should see an UNKNOWN status for any tasks that have not yet been processes due to the limitations of `max_parallelism`.
