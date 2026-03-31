---
title: Data plane setup on generic Kubernetes
weight: 3
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on generic Kubernetes

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](./architecture/_index) page.

> [!NOTE] These instructions cover installing Union.ai in an on-premise Kubernetes cluster.
> If you are installing at a cloud provider, use the cloud provider specific instructions: [AWS](./selfmanaged-aws), [GCP](./selfmanaged-gcp), [Azure](./selfmanaged-azure), [OCI](./selfmanaged-oci).

## Kubernetes Cluster

You need a Kubernetes cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](./cluster-recommendations) for networking and node pool guidance.

If you don't already have a cluster, common options for provisioning one include:

- [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) — the standard Kubernetes bootstrap tool
- [k3s](https://k3s.io/) — lightweight Kubernetes distribution
- [RKE2](https://docs.rke2.io/) — Rancher's hardened Kubernetes distribution

Regardless of how you create your cluster, verify the following requirements are met:

- **Kubernetes version**: one of the most recent three minor versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/).
- **Networking**: a CNI plugin is installed and functioning (e.g. Calico, Flannel, Cilium).
- **DNS**: CoreDNS is running in the cluster.
- **Storage**: a default StorageClass is configured for persistent volume claims.
- **Load balancer or ingress**: an ingress controller or load balancer is available for exposing services.

Union supports autoscaling and the use of spot (interruptible) instances if your infrastructure provides them.

## Object Storage

Each data plane uses S3-compatible object storage (such as [MinIO](https://min.io)) to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

Create the buckets. For example, using the [MinIO Client (`mc`)](https://min.io/docs/minio/linux/reference/minio-mc.html):

```bash
# Set an alias for your MinIO server (if not already configured)
mc alias set myminio https://minio.example.com MINIO_ACCESS_KEY MINIO_SECRET_KEY

# Create the buckets
mc mb myminio/union-metadata
mc mb myminio/union-fast-reg
```

### CORS Configuration

To enable the [Code Viewer](./configuration/code-viewer) in the Union UI, configure a CORS policy on your bucket(s). This allows the UI to securely fetch code bundles directly from storage.

Save the following as `cors.json`:

```json
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
```

Apply it to both buckets:

```bash
mc anonymous set-json cors.json myminio/union-metadata
mc anonymous set-json cors.json myminio/union-fast-reg
```

Consult your object storage provider's documentation for the equivalent configuration if you are not using MinIO.

### Data Retention

Union recommends using lifecycle policies on these buckets to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## Container Registry

You need a container registry accessible from your cluster for Image Builder to push and pull container images. Options include:

- A private [Docker Registry](https://docs.docker.com/registry/)
- [Harbor](https://goharbor.io/)
- Any OCI-compliant registry

For a basic private Docker Registry, you can start one with:

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

> [!NOTE] This runs an unauthenticated registry suitable for testing. For production, configure TLS and authentication. See the [Docker Registry documentation](https://docs.docker.com/registry/deploying/) for details.

Note the registry URL (e.g. `registry.example.com:5000/union`) — you will configure it in your Helm values.

## Identity & Access

On generic Kubernetes, Union authenticates to object storage and the container registry using static credentials (access key and secret key). These are configured in the generated values file during deployment.

### Storage credentials

Ensure the credentials you provide have read/write access to your storage bucket(s). If you are using MinIO, you can create a dedicated access key pair through the MinIO Console or the `mc` CLI:

```bash
# Create a new access key on your MinIO server
mc admin user add myminio union-service GENERATED_SECRET_KEY

# Attach a read/write policy for the Union buckets
mc admin policy attach myminio readwrite --user union-service
```

> [!NOTE] For production, create a scoped policy that limits access to only the Union buckets rather than using the built-in `readwrite` policy.

### Registry credentials

Ensure you have push/pull credentials for your container registry. The specifics depend on your registry choice (Docker Registry basic auth, Harbor robot accounts, etc.).

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
