---
title: Data plane setup on generic Kubernetes
weight: 3
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on generic Kubernetes

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.
The Union architecture is described on the [Architecture](./architecture/_index) page.

> [!NOTE] These instructions cover installing Union.ai in an on-premise Kubernetes cluster.
> If you are installing at a cloud provider, use the cloud provider specific instructions: [AWS](./selfmanaged-aws), [GCP](./selfmanaged-gcp), [Azure](./selfmanaged-azure), [OCI](./selfmanaged-oci).

## Object Storage

Each data plane uses S3-compatible object storage (such as [MinIO](https://min.io)) to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

### CORS Configuration

To enable the [Code Viewer](./configuration/code-viewer) in the Union UI, configure a CORS policy on your bucket(s). This allows the UI to securely fetch code bundles directly from storage.

The required CORS rule:

- **Allowed Origins:** `https://*.unionai.cloud`
- **Allowed Methods:** `GET`, `HEAD`
- **Allowed Headers:** `*`
- **Expose Headers:** `ETag`
- **Max Age Seconds:** `3600`

For MinIO, you can set this via `mc`:

```bash
cat > /tmp/cors.json <<'EOF'
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://*.unionai.cloud"],
      "AllowedMethods": ["GET", "HEAD"],
      "AllowedHeaders": ["*"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
EOF
mc anonymous set-json /tmp/cors.json myminio/<BUCKET_NAME>
```

Consult your object storage provider's documentation for the equivalent configuration.

### Data Retention

Union recommends using lifecycle policies on these buckets to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## Container Registry

You need a container registry accessible from your cluster for Image Builder to push and pull container images. Options include:

- A private [Docker Registry](https://docs.docker.com/registry/)
- [Harbor](https://goharbor.io/)
- Any OCI-compliant registry

Note the registry URL (e.g. `registry.example.com/union`) — you will configure it in your Helm values.

## Identity & Access

On generic Kubernetes, Union authenticates to object storage using static credentials (access key and secret key). These are configured in the generated values file during deployment.

Ensure the credentials you provide have read/write access to your storage bucket(s) and push/pull access to your container registry.

> [!NOTE] Worker pod authentication
> Worker pods (task executions) use the same storage credentials as the platform services. The credentials are injected into per-project namespaces via the cluster resource sync mechanism.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/).
* Object storage provided by a vendor or an S3-compatible platform (such as [MinIO](https://min.io)), with CORS configured as described above.
* A container registry accessible from your cluster.

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../api-reference/uctl-cli/_index).

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authorization permissions for the app to operate on the Union cluster name you have selected, generate values file to install dataplane in your Kubernetes cluster and provide follow-up instructions:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider metal
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `metal` (bare metal / generic).

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   - Set `storage.endpoint` to your S3-compatible storage endpoint (e.g. your MinIO URL).
   - Set `storage.accessKey` and `storage.secretKey` to your storage credentials.
   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your bucket name(s).
   - Set `storage.region` to the region of your storage provider.
   - The same credentials are also needed in `fluentbit.env` for log shipping.

4. Optionally configure the resource `limits` and `requests` for the different services.
   By default, these will be set minimally, will vary depending on usage, and follow the Kubernetes `ResourceRequirements` specification.

   * `operator.resources`
   * `executor.resources`
   * `proxy.resources`
   * `flytepropellerwebhook.resources`

5. Install the data plane Helm chart:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f <GENERATED_VALUES_FILE> \
     --namespace union \
     --create-namespace
   ```

6. Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <YOUR_ORG_NAME>
   ```

7. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

   ```bash
   uctl get cluster
    ----------- ------- --------------- -----------
   | NAME      | ORG   | STATE         | HEALTH    |
    ----------- ------- --------------- -----------
   | <cluster> | <org> | STATE_ENABLED | HEALTHY   |
    ----------- ------- --------------- -----------
   1 rows
   ```

8. You can then register and run some example workflows through your cluster to ensure that it is working correctly.

   ```bash
   uctl register examples --project=union-health-monitoring --domain=development
   uctl validate snacks --project=union-health-monitoring --domain=development
    ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
   | NAME                 | LAUNCH PLAN NAME                  | VERSION  | STARTED AT                     | ELAPSED TIME | RESULT    | ERROR MESSAGE |
    ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
   | alskkhcd6wx5m6cqjlwm | basics.hello_world.hello_world_wf | v0.3.341 | 2025-05-09T18:30:02.968183352Z | 4.452440953s | SUCCEEDED |               |
    ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
   1 rows
   ```
