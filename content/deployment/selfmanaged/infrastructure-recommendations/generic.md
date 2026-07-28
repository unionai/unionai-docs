---
title: Generic Kubernetes
weight: 5
variants: -flyte +union
---

# Generic Kubernetes infrastructure

This page walks you through creating the resources needed for a Union data plane on generic (on-premise) Kubernetes. If you already have these resources, skip to [Deploy the dataplane](../deploy/_index).

> [!NOTE] If you are installing at a cloud provider, use the cloud provider specific instructions: [AWS](./aws), [GCP](./gcp), [Azure](./azure), [OCI](./oci).

## Kubernetes cluster

You need a Kubernetes cluster running one of the most recent three minor Kubernetes versions. See [Infrastructure recommendations](../infrastructure-recommendations/_index) for networking and node pool guidance.

If you don't already have a cluster, common options for provisioning one include:

- [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/): the standard Kubernetes bootstrap tool
- [k3s](https://k3s.io/): lightweight Kubernetes distribution
- [RKE2](https://docs.rke2.io/): Rancher's hardened Kubernetes distribution

Regardless of how you create your cluster, verify the following requirements are met:

- **Kubernetes version**: one of the most recent three minor versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/).
- **Networking**: a CNI plugin is installed and functioning (e.g. Calico, Flannel, Cilium).
- **DNS**: CoreDNS is running in the cluster.
- **Storage**: a default StorageClass is configured for persistent volume claims.
- **Load balancer or ingress**: an ingress controller or load balancer is available for exposing services.

Union supports autoscaling and the use of spot (interruptible) instances if your infrastructure provides them.

## Object storage

Each data plane uses S3-compatible object storage (such as [MinIO](https://min.io)) to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `flyte deploy` or `flyte run --copy-style all`.

You can also choose to use a single bucket.

Create the buckets. For example, using the [MinIO Client (`mc`)](https://min.io/docs/minio/linux/reference/minio-mc.html):

```bash
# Set an alias for your MinIO server (if not already configured)
mc alias set myminio https://minio.example.com MINIO_ACCESS_KEY MINIO_SECRET_KEY

# Create the buckets
mc mb myminio/union-metadata
mc mb myminio/union-fast-reg
```

### CORS configuration

To enable the [Code Viewer](../configuration/code-viewer) in the Union UI, configure a CORS policy on your bucket(s). This allows the UI to securely fetch code bundles directly from storage.

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

### Data retention

Union recommends using lifecycle policies on these buckets to manage storage costs. See [Data retention policy](../configuration/data-retention) for more information.

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

Note the registry URL (e.g. `registry.example.com:5000/union`); you will configure it in your Helm values.

## Identity & access

On generic Kubernetes, Union authenticates to object storage and the container registry using static credentials (access key and secret key). These are configured in the Helm values file during deployment.

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

## Deploy configuration

When you [deploy the data plane](../deploy/_index), start from the base values file (the published overlays cover AWS, GCP, and Azure only) and set the generic keys below. The shared `global` keys (`UNION_CONTROL_PLANE_HOST`, `CLUSTER_NAME`, `ORG_NAME`) are covered in the deploy walkthrough.

```bash
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.yaml
```

Set the storage keys for your S3-compatible provider:

- Set `storage.endpoint` to your S3-compatible storage endpoint (e.g. your MinIO URL).
- Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your bucket name(s).
- Set `storage.region` to the region of your storage provider.
- The same credentials are also needed in `fluentbit.env` for log shipping.

Rather than putting your storage credentials in the values file, store them in a Kubernetes Secret and reference it from the chart. Create the namespace and the secret first; the chart reads the secret while rendering, so it must exist before you install:

```bash
kubectl create namespace union
kubectl create secret generic storage-credentials -n union \
  --from-literal=access_key_id=<ACCESS_KEY_ID> \
  --from-literal=secret_key=<SECRET_ACCESS_KEY>
```

Then reference it instead of setting `storage.accessKey` and `storage.secretKey`:

```yaml
storage:
  provider: compat
  authType: accesskey
  credentialsSecretRef:
    name: storage-credentials
```

> [!NOTE]
> The chart resolves the secret with a Helm `lookup`, which returns nothing during `helm template` or `--dry-run`. Those commands render the storage config without credentials; only a real install picks them up. If your secret uses different field names, set `credentialsSecretRef.accessKeyIdKey` and `credentialsSecretRef.secretKeyKey` to match.
