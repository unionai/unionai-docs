---
title: Data plane setup on CoreWeave
weight: 7
variants: -flyte +union
---

# Data plane setup on CoreWeave

[Union.ai](https://www.union.ai/) is a managed platform for [Flyte](https://flyte.org/), an open-source workflow orchestrator for data and ML pipelines. Union.ai provides a hosted control plane while the data plane runs on your infrastructure, keeping data and compute within your CoreWeave Kubernetes Service (CKS) cluster.

This guide shows you how to deploy a Union.ai self-managed data plane on CKS with [CoreWeave AI Object Storage](https://docs.coreweave.com/products/storage/object-storage) as the storage backend. After completing this guide, you can run Flyte workflows on CoreWeave GPU and CPU instances managed through the Union.ai control plane.

This guide is for operators who administer a CKS cluster and a Union.ai organization.

## Prerequisites

Before you begin, confirm you've met all of the following prerequisites:

- A [CKS cluster](https://docs.coreweave.com/products/cks/clusters/introduction) with `kubectl` access configured.
- The `helm` CLI installed. For installation instructions, see [Install Helm](https://helm.sh/docs/intro/install/).
- The [`uctl` CLI](../../../api-reference/uctl-cli/_index) installed.
- The [`flyte` CLI](../../../api-reference/flyte-cli) installed.
- A Union.ai organization. Contact [Union.ai](https://www.union.ai/) to create one if you don't have one.

## Configure CoreWeave AI Object Storage

Union.ai uses AI Object Storage (S3-compatible) to store workflow data and artifacts. To configure storage, complete the following steps:

### Create a bucket

Create a bucket in the [CoreWeave Cloud Console](https://console.coreweave.com/). Navigate to **Storage > Object Storage** and create a bucket in your desired Availability Zone.

For detailed instructions, see [Create a bucket](https://docs.coreweave.com/products/storage/object-storage/buckets/create-bucket).

### Generate access credentials

Navigate to **Administration > Object Storage Access Keys** in the Cloud Console and create an access key pair. Record the **Access Key ID** and **Secret Key** for use in later steps.

You need this key pair so the Helm values and workload environment variables can authenticate to your bucket.

For detailed instructions, see [Create access keys](https://docs.coreweave.com/products/storage/object-storage/auth-access/manage-access-keys/create-keys).

### Create an access policy

Create an organization access policy that grants your access key permissions on the bucket. Navigate to **Administration > Policies > Object Storage Access** in the Cloud Console and create a policy with the following JSON. Replace `[BUCKET-NAME]` with the name of your bucket.

```json
{
  "policy": {
    "version": "v1alpha1",
    "name": "union-ai-bucket-access",
    "statements": [
      {
        "name": "allow-union-s3-access",
        "effect": "Allow",
        "actions": ["s3:*"],
        "resources": [
          "[BUCKET-NAME]",
          "[BUCKET-NAME]/*"
        ],
        "principals": ["*"]
      }
    ]
  }
}
```

For detailed instructions on creating and managing policies, see [Organization access policies](https://docs.coreweave.com/products/storage/object-storage/auth-access/organization-policies/about).

> [!WARNING]
> Without an access policy, API operations return `403 Forbidden` errors even with valid access keys.

You now have a bucket, credentials, and a policy that allow the data plane to use AI Object Storage.

## Configure the Union CLI

Update your `uctl` configuration to point to your Union.ai organization endpoint.

Edit the `~/.union/config.yaml` file:

```yaml
admin:
  endpoint: dns:///[ORG-NAME].union.ai
  insecure: false
  authType: Pkce
```

Replace `[ORG-NAME]` with your Union.ai organization name.

To verify connectivity, run:

```bash
uctl get project
```

A successful response shows that `uctl` uses the correct organization endpoint.

## Provision data plane resources

Set your `KUBECONFIG` to the CKS cluster where you want to deploy the data plane:

```bash
export KUBECONFIG=[PATH-TO-KUBECONFIG]
```

To provision the data plane resources, run:

```bash
uctl selfserve provision-dataplane-resources \
  --clusterName [CLUSTER-NAME] \
  --provider metal
```

This command generates a Helm values file with default configuration. Don't use the generated file as-is. You must update the storage configuration for AI Object Storage as described in the next section.

You now have a generated Helm values file to customize.

## Create the Helm values file

AI Object Storage requires virtual-hosted style S3 URLs. The default Union.ai configuration uses path-style URLs, which CoreWeave doesn't support.

Update the generated Helm values file with the following storage configuration. Replace all placeholder values with your actual credentials and settings.

```yaml
host: "[ORG-NAME].union.ai"
clusterName: "[CLUSTER-NAME]"
orgName: "[ORG-NAME]"
provider: metal

storage:
  provider: custom
  bucketName: "[BUCKET-NAME]"
  fastRegistrationBucketName: "[BUCKET-NAME]"
  custom:
    type: stow
    container: "[BUCKET-NAME]"
    stow:
      kind: s3
      config:
        region: "[AVAILABILITY-ZONE]"
        auth_type: accesskey
        access_key_id: "[ACCESS-KEY-ID]"
        secret_key: "[SECRET-ACCESS-KEY]"
        endpoint: https://cwobject.com
        disable_ssl: false
        disable_force_path_style: "true"

executor:
  extraEnvVars:
    - name: FLYTE_AWS_S3_ADDRESSING_STYLE
      value: "virtual"
    - name: FLYTE_AWS_ENDPOINT
      value: "https://cwobject.com"
    - name: AWS_ACCESS_KEY_ID
      value: "[ACCESS-KEY-ID]"
    - name: AWS_SECRET_ACCESS_KEY
      value: "[SECRET-ACCESS-KEY]"
    - name: AWS_DEFAULT_REGION
      value: "[AVAILABILITY-ZONE]"

config:
  k8s:
    plugins:
      k8s:
        default-env-vars:
          - FLYTE_AWS_ENDPOINT: "https://[BUCKET-NAME].cwobject.com"
          - FLYTE_AWS_S3_ADDRESSING_STYLE: "virtual"
          - AWS_ACCESS_KEY_ID: "[ACCESS-KEY-ID]"
          - AWS_SECRET_ACCESS_KEY: "[SECRET-ACCESS-KEY]"
          - AWS_DEFAULT_REGION: "[AVAILABILITY-ZONE]"

operator:
  enableTunnelService: true

secrets:
  admin:
    create: true
    clientId: [CLIENT-ID]
    clientSecret: [CLIENT-SECRET]

fluentbit:
  enabled: true
  env:
    - name: AWS_ACCESS_KEY_ID
      value: [ACCESS-KEY-ID]
    - name: AWS_SECRET_ACCESS_KEY
      value: [SECRET-ACCESS-KEY]
```

> [!NOTE]
> The `uctl selfserve provision-dataplane-resources` command in the previous step generates the `[CLIENT-ID]` and `[CLIENT-SECRET]` values. Use the values from that command's output.

You need these settings for AI Object Storage compatibility.

| Setting                                                      | Value                                | Purpose                                                         |
| ------------------------------------------------------------ | ------------------------------------ | --------------------------------------------------------------- |
| `storage.custom.stow.config.disable_force_path_style`        | `true`                               | Enables virtual-hosted style S3 URLs.                           |
| `storage.custom.stow.config.endpoint`                        | `https://cwobject.com`               | AI Object Storage endpoint for the control plane.               |
| `config.k8s.plugins.k8s.default-env-vars.FLYTE_AWS_ENDPOINT` | `https://[BUCKET-NAME].cwobject.com` | Bucket-specific endpoint injected into task pods.               |
| `executor.extraEnvVars.FLYTE_AWS_S3_ADDRESSING_STYLE`        | `virtual`                            | Configures the executor to use virtual-hosted style addressing. |

Together, these values align the chart with AI Object Storage.

## Deploy the Union data plane

To deploy the data plane, complete the following steps:

1. Clone the Union Helm charts repository and check out the latest stable release:

   Replace `[RELEASE-TAG]` with the latest stable release tag (for example, `dataplane-2026.3.3`). Check the [Union Helm charts repository](https://github.com/unionai/helm-charts) for available tags.

   ```bash
   git clone https://github.com/unionai/helm-charts.git
   cd helm-charts
   git checkout [RELEASE-TAG]
   ```

   After checkout, you have the CRD and dataplane charts for the release you install.

2. Install the Custom Resource Definitions (CRDs):

   ```bash
   helm upgrade --install unionai-dataplane-crds charts/dataplane-crds
   ```

3. Build the chart dependencies and install the data plane:

   Replace `[PATH-TO-VALUES-FILE]` with the path to the Helm values file you customized in the previous section.

   ```bash
   cd charts/dataplane
   helm dependency build
   helm upgrade --install unionai-dataplane . \
     --namespace union --create-namespace \
     --values [PATH-TO-VALUES-FILE] \
     --timeout 10m
   ```

4. Verify the pods are running:

   ```bash
   kubectl get pods -n union
   ```

   When the deployment succeeds, all pods show a `Running` status, including `union-operator-proxy`, `union-operator-buildkit`, `flytepropeller`, and `executor`.

5. Verify the cluster is registered with the control plane:

   ```bash
   uctl get cluster
   ```

   The output is similar to the following:

   ```text
   NAME               ORG          STATE          HEALTH
   union-coreweave    my-org       STATE_ENABLED  HEALTHY
   ```

At this point the Union.ai data plane runs in your cluster and is registered with the control plane.

## Create the eager API key

To create an API key required for Flyte v2 task execution, run:

```bash
uctl create apikey --keyName EAGER_API_KEY --org [ORG-NAME]
```

> [!NOTE]
> If you receive a `PermissionDenied` error, contact [Union.ai support](https://www.union.ai/) to have the permission enabled for your organization.

## Test a workflow

To run a sample workflow, complete the following steps:

1. Create a Flyte CLI configuration file at the path `.flyte/config.yaml` in your project directory:

   Replace `[ORG-NAME]` and `[PROJECT-NAME]` with your organization and project identifiers.

   ```yaml
   admin:
     endpoint: dns:///[ORG-NAME].union.ai
   image:
     builder: remote
   task:
     domain: development
     org: [ORG-NAME]
     project: [PROJECT-NAME]
   ```

2. Run a sample workflow:

   ```bash
   flyte run --image ghcr.io/flyteorg/flyte:py3.13-v2.0.2 \
     hello_world.py main --n 5
   ```

   > [!NOTE]
   > If the remote image builder isn't enabled for your organization, use the `--image` flag with a pre-built container image as in the preceding `flyte run` example.

3. Check the run status:

   Replace `[RUN-NAME]` with the workflow run identifier.

   ```bash
   flyte get run [RUN-NAME]
   ```

   Look for `ACTION_PHASE_SUCCEEDED` in the output.

When `ACTION_PHASE_SUCCEEDED` appears in the output, this sample workflow completed successfully on your deployment.

## Troubleshooting

| Symptom                                      | Cause                                                  | Fix                                                                                                                                       |
| -------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `PathStyleRequestNotAllowed 400`             | The control plane generates path-style S3 URLs.        | Set `storage.custom.stow.config.disable_force_path_style` to `"true"` in the Helm values file.                                            |
| `403 Forbidden` on S3 operations             | No access policy for the storage key.                  | Create an object storage access policy in the [Cloud Console](https://docs.coreweave.com/products/storage/object-storage/auth-access/organization-policies/manage). |
| Task pods reach `s3.us-east-1.amazonaws.com` | Task pods are missing the CoreWeave endpoint.          | Add `FLYTE_AWS_ENDPOINT` to `config.k8s.plugins.k8s.default-env-vars` with the value `https://[BUCKET-NAME].cwobject.com`.                |
| "All enabled clusters are unhealthy"         | The control plane can't reach the data plane.          | Verify the tunnel service is running: `kubectl get pods -n union \| grep proxy`.                                                          |
| "Remote image builder is not enabled"        | The remote builder isn't enabled on the control plane. | Contact Union.ai to enable the remote builder, or use `--image` with a pre-built image.                                                   |
| `invalid keys: collectbillableresourceusage` | Chart version mismatch with the operator.              | Use matching chart and operator image versions.                                                                                           |
| Helm "another operation in progress"         | An interrupted Helm upgrade.                           | Run `helm rollback unionai-dataplane [LAST-GOOD-REVISION] -n union`.                                                                      |
| "Provided Tunnel token is not valid"         | The control plane isn't configured for this cluster.   | Complete cluster registration first.                                                                                                      |

## Additional resources

For more information, see the following resources:

- [Union.ai documentation](https://docs.union.ai/)
- [Flyte documentation](https://docs.flyte.org/)
- [CoreWeave AI Object Storage](https://docs.coreweave.com/products/storage/object-storage)
- [Create a CKS cluster](https://docs.coreweave.com/products/cks/clusters/create)
