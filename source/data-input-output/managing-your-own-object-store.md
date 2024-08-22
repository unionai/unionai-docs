# Managing your own object store

Yes. You can certainly configure your own blob storage and then use your chosen library (like `boto3`, for example) to interact with that storage within your task code.
The only caveat is that you must ensure that your task code has access to the storage (see [Enabling AWS S3](./integrations/enabling-aws-resources/enabling-aws-s3) or [Enabling Google Cloud Storage](./integrations/enabling-gcp-resources/enabling-google-cloud-storage)).

### Can I control access to my own blob store?

Yes. As with all resources used by your Flyte task code, the storage must be accessible from within the cluster running your code on your data plane.
However, the data plane is your own and you have full control over access (see [Enabling AWS S3](./integrations/enabling-aws-resources/enabling-aws-s3) or [Enabling Google Cloud Storage](./integrations/enabling-gcp-resources/enabling-google-cloud-storage)).

### Could someone maliciously delete or otherwise access my raw data?

No.
Your raw data resides in your data plane and is stored either in the default raw data storage or in storage that you set up yourself.
In either case, you control access to it.

The Union team does have access to your data plane for purposes of maintenance but does not have access to your raw data, secrets in secret managers, database, etc. unless you choose to permit such access.

Having said that, since the data plane is yours, you are ultimately responsible for preventing access by malicious third parties.

### Can I use s3fs from within a task?

Yes, but you probably don't need to.

[`s3fs`](https://github.com/s3fs-fuse/s3fs-fuse) is a FUSE-based filesystem backed by Amazon S3.
It is possible to set up `s3fs` in your task container image and use it from within your task code.

However, in most cases using either `FlyteFile`/`FlyteDirectory` or a library like `boto3` to access an S3 bucket directly is preferred (and easier).

If you do need to use `s3fs`, here are the basic steps:

* Set up the S3 bucket that you wish to access.
* Enable access to the bucket from your task code by configuring an appropriate IAM policy.
See [Enabling AWS S3](./integrations/enabling-aws-resources/enabling-aws-s3).
* Specify your task container image to have `s3fs` correctly installed and configured.
* In the task decorator, configure a `PodTemplate` to run the task container in privileged mode (see links below).
* In your task code, invoke the `s3fs` command line tool to mount the S3-backed volume.
For example:

```{code-block} python
subprocess.run(['s3fs', bucket_and_path, mount_point, '-o', 'iam_role=auto'], check=True)
```

See also:

* [Configuring Custom K8s Resources > Using K8s PodTemplates](https://docs.flyte.org/en/latest/deployment/configuration/general.html#using-k8s-podtemplates)
* [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

### Can I use BigQuery from within a task?

If your Union data plane is running on GCP, access to BigQuery should be enabled by default and bound to the default Google Service Account (referred to in this documentation as **`<UserFlyteGSA>`**.
For details see [Enabling GCP resources](./integrations/enabling-gcp-resources/index).
If you want to bind it to a different GSA, follow the instructions in [Enabling BigQuery](./integrations/enabling-gcp-resources/enabling-bigquery).

To actually access your BigQuery instance from your code, you will need to use a `BigQueryTask`.
For details see [BigQuery Query](https://docs.flyte.org/en/latest/flytesnacks/examples/bigquery_plugin/bigquery.html).