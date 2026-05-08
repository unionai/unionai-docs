---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required CoreWeave resources (CKS cluster, AI Object Storage bucket, access keys, access policy), see [Prepare infrastructure](../selfmanaged-coreweave/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a CKS cluster running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have a CoreWeave AI Object Storage bucket, access keys, and access policy as described in [Prepare infrastructure](../selfmanaged-coreweave/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli) (used later to run a sample workflow).

## Deploy the {{< key product_name >}} operator

1. Set your `KUBECONFIG` to the CKS cluster where you want to deploy the data plane:

   ```bash
   export KUBECONFIG=<PATH_TO_KUBECONFIG>
   ```

2. Configure the Union CLI and provision data plane resources:

   ```bash
   uctl config init --host=<ORG_NAME>.union.ai
   uctl selfserve provision-dataplane-resources --clusterName <CLUSTER_NAME> --provider metal
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML values file specific to the `metal` provider.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your CoreWeave-specific storage configuration. AI Object Storage requires virtual-hosted style S3 URLs, so you must override the default storage configuration. Replace the placeholders with your actual credentials and settings.

   ```yaml
   host: <ORG_NAME>.union.ai
   clusterName: <CLUSTER_NAME>
   orgName: <ORG_NAME>
   provider: metal

   storage:
     provider: custom
     bucketName: <BUCKET_NAME>
     fastRegistrationBucketName: <BUCKET_NAME>
     custom:
       type: stow
       container: <BUCKET_NAME>
       stow:
         kind: s3
         config:
           region: <AVAILABILITY_ZONE>
           auth_type: accesskey
           access_key_id: <ACCESS_KEY_ID>
           secret_key: <SECRET_ACCESS_KEY>
           endpoint: https://cwobject.com
           disable_ssl: false
           disable_force_path_style: true

   executor:
     extraEnvVars:
       - name: FLYTE_AWS_S3_ADDRESSING_STYLE
         value: "virtual"
       - name: FLYTE_AWS_ENDPOINT
         value: "https://cwobject.com"
       - name: AWS_ACCESS_KEY_ID
         value: <ACCESS_KEY_ID>
       - name: AWS_SECRET_ACCESS_KEY
         value: <SECRET_ACCESS_KEY>
       - name: AWS_DEFAULT_REGION
         value: <AVAILABILITY_ZONE>

   config:
     k8s:
       plugins:
         k8s:
           default-env-vars:
             - FLYTE_AWS_ENDPOINT: https://<BUCKET_NAME>.cwobject.com
             - FLYTE_AWS_S3_ADDRESSING_STYLE: "virtual"
             - AWS_ACCESS_KEY_ID: <ACCESS_KEY_ID>
             - AWS_SECRET_ACCESS_KEY: <SECRET_ACCESS_KEY>
             - AWS_DEFAULT_REGION: <AVAILABILITY_ZONE>

   operator:
     enableTunnelService: true

   secrets:
     admin:
       create: true
       clientId: <CLIENT_ID>
       clientSecret: <CLIENT_SECRET>

   fluentbit:
     enabled: true
     env:
       - name: AWS_ACCESS_KEY_ID
         value: <ACCESS_KEY_ID>
       - name: AWS_SECRET_ACCESS_KEY
         value: <SECRET_ACCESS_KEY>
   ```

   > [!NOTE]
   > The `uctl selfserve provision-dataplane-resources` command in step 2 generates the `<CLIENT_ID>` and `<CLIENT_SECRET>` values. Use the values from that command's output.

   The settings below are required for AI Object Storage compatibility:

   | Setting                                                                 | Value                                | Purpose                                                         |
   | ----------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------- |
   | `storage.custom.stow.config.disable_force_path_style`                   | `true`                               | Enables virtual-hosted style S3 URLs.                           |
   | `storage.custom.stow.config.endpoint`                                   | `https://cwobject.com`               | AI Object Storage endpoint for the control plane.               |
   | `config.k8s.plugins.k8s.default-env-vars` (entry: `FLYTE_AWS_ENDPOINT`) | `https://<BUCKET_NAME>.cwobject.com` | Bucket-specific endpoint injected into task pods.               |
   | `executor.extraEnvVars.FLYTE_AWS_S3_ADDRESSING_STYLE`                   | `virtual`                            | Configures the executor to use virtual-hosted style addressing. |

4. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

5. Install the Custom Resource Definitions (CRDs):

   ```bash
   helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds
   ```

6. Install the data plane. Replace `<PATH_TO_VALUES_FILE>` with the path to the Helm values file you customized in step 3.

   ```bash
   helm upgrade --install unionai-dataplane unionai/dataplane \
     --namespace union --create-namespace \
     --values <PATH_TO_VALUES_FILE> \
     --timeout 10m
   ```

7. Verify the pods are running:

   ```bash
   kubectl get pods -n union
   ```

   When the deployment succeeds, all pods show a `Running` status, including `union-operator-proxy`, `union-operator-buildkit`, `flytepropeller`, and `executor`.

8. Verify the cluster is registered with the control plane:

   ```bash
   uctl get cluster
   ```

   The output is similar to the following:

   ```text
   NAME               ORG          STATE          HEALTH
   union-coreweave    my-org       STATE_ENABLED  HEALTHY
   ```

9. Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <ORG_NAME>
   ```

   > [!NOTE]
   > If you receive a `PermissionDenied` error, contact [Union.ai support](https://www.union.ai/) to have the permission enabled for your organization.

## Test a workflow

To run a sample workflow, complete the following steps:

1. Create a Flyte CLI configuration file at the path `.flyte/config.yaml` in your project directory. Replace `<ORG_NAME>` and `<PROJECT_NAME>` with your organization and project identifiers.

   ```yaml
   admin:
     endpoint: dns:///<ORG_NAME>.union.ai
   image:
     builder: remote
   task:
     domain: development
     org: <ORG_NAME>
     project: <PROJECT_NAME>
   ```

2. Run a sample workflow:

   ```bash
   flyte run --image ghcr.io/flyteorg/flyte:py3.13-v2.0.2 \
     hello_world.py main --n 5
   ```

   > [!NOTE]
   > If the remote image builder isn't enabled for your organization, use the `--image` flag with a pre-built container image as in the preceding `flyte run` example.

3. Check the run status. Replace `<RUN_NAME>` with the workflow run identifier.

   ```bash
   flyte get run <RUN_NAME>
   ```

   Look for `ACTION_PHASE_SUCCEEDED` in the output to confirm the workflow completed successfully.

## Troubleshooting

| Symptom                                      | Cause                                                  | Fix                                                                                                                                                                 |
| -------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PathStyleRequestNotAllowed 400`             | The control plane generates path-style S3 URLs.        | Set `storage.custom.stow.config.disable_force_path_style` to `true` in the Helm values file.                                                                        |
| `403 Forbidden` on S3 operations             | No access policy for the storage key.                  | Create an object storage access policy in the [Cloud Console](https://docs.coreweave.com/products/storage/object-storage/auth-access/organization-policies/manage). |
| Task pods reach `s3.us-east-1.amazonaws.com` | Task pods are missing the CoreWeave endpoint.          | Add `FLYTE_AWS_ENDPOINT` to `config.k8s.plugins.k8s.default-env-vars` with the value `https://<BUCKET_NAME>.cwobject.com`.                                          |
| "All enabled clusters are unhealthy"         | The control plane can't reach the data plane.          | Verify the tunnel service is running: `kubectl get pods -n union \| grep proxy`.                                                                                    |
| "Remote image builder is not enabled"        | The remote builder isn't enabled on the control plane. | Contact Union.ai to enable the remote builder, or use `--image` with a pre-built image.                                                                             |
| `invalid keys: collectbillableresourceusage` | Chart version mismatch with the operator.              | Use matching chart and operator image versions.                                                                                                                     |
| Helm "another operation in progress"         | An interrupted Helm upgrade.                           | Run `helm rollback unionai-dataplane <LAST_GOOD_REVISION> -n union`.                                                                                                |
| "Provided Tunnel token is not valid"         | The control plane isn't configured for this cluster.   | Complete cluster registration first.                                                                                                                                |

## Additional resources

For more information, see the following resources:

- [CoreWeave AI Object Storage](https://docs.coreweave.com/products/storage/object-storage)
- [Create a CKS cluster](https://docs.coreweave.com/products/cks/clusters/create)
