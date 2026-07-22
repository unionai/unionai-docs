---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required Nebius resources (MK8s cluster, Object Storage bucket, service account, access key), see [Prepare infrastructure](../selfmanaged-nebius/prepare-infra) first.

> [!NOTE] Planning more than one cluster?
> This page covers the single-cluster path: one cluster in the `default` cluster pool, as created by the `flyte create cluster ... --pool default` command below. If you plan to connect several clusters to the same control plane, read [Multiple clusters](../configuration/multi-cluster) first. Pool membership governs metadata sharing -- clusters in the same pool share one metadata bucket, and clusters in different pools must use different ones -- so it affects the metadata bucket you configure below.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a Nebius Managed Kubernetes cluster running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have a Nebius Object Storage bucket, service account, and access key as described in [Prepare infrastructure](../selfmanaged-nebius/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli) (used later to run a sample workflow).
* Install the [`flyteplugins-union` plugin](../../../api-reference/flyte-cli#plugin-commands), which provides the `flyte get cluster` command: `pip install flyteplugins-union`.
* Install the [Nebius CLI](https://docs.nebius.com/cli) and authenticate with `nebius profile create`.

## Deploy the {{< key product_name >}} operator

1. Set your `KUBECONFIG` to the Nebius MK8s cluster where you want to deploy the data plane:

   ```bash
   nebius mk8s cluster get-credentials --id <CLUSTER_ID> --external
   export KUBECONFIG=<PATH_TO_KUBECONFIG>
   ```

2. Configure the `flyte` CLI to talk to your control plane, then register the cluster name:

   ```bash
   flyte create config --endpoint <ORG_NAME>.union.ai --org <ORG_NAME>
   flyte create cluster <CLUSTER_NAME> --pool default
   ```

   `flyte create config` writes `.flyte/config.yaml`. The first command that contacts the control plane opens a browser to authenticate you.

   Register the cluster before you install the chart -- the data plane binds to this record when it starts. Every organization is provisioned with a `default` pool, so `--pool default` needs no extra setup.

3. Configure the Union CLI and provision data plane resources:

   ```bash
   uctl config init --host=<ORG_NAME>.union.ai
   uctl selfserve provision-dataplane-resources --clusterName <CLUSTER_NAME> --provider custom
   ```

   The command outputs the client ID and client secret your data plane uses to communicate with Union's control plane. Save the secret that is displayed — Union does not store it, and it cannot be retrieved later.

4. Create a values file for the data plane chart. Start from the base values file and layer your Nebius-specific storage configuration on top, replacing the placeholders with your actual credentials and settings:

   ```bash
   curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.yaml
   ```

   Rather than putting your bucket access keys in the values file, store them in a Kubernetes Secret and reference it from the chart. Create the namespace and the secret first -- the chart reads the secret while rendering, so it must exist before you install:

   ```bash
   kubectl create namespace union
   kubectl create secret generic storage-credentials -n union \
     --from-literal=access_key_id=<YOUR_BUCKET_ACCESS_KEY> \
     --from-literal=secret_key=<YOUR_BUCKET_SECRET_KEY>
   ```

   Then point the values file at that secret:

   ```yaml
   host: <ORG_NAME>.union.ai
   clusterName: <CLUSTER_NAME>
   orgName: <ORG_NAME>
   provider: custom

   storage:
     bucketName: <YOUR_STORAGE_BUCKET_NAME>
     endpoint: https://storage.<REGION>.nebius.cloud
     fastRegistrationBucketName: <YOUR_STORAGE_BUCKET_NAME>
     provider: compat
     region: <REGION>
     credentialsSecretRef:
       name: storage-credentials
   ```

   > [!NOTE]
   > The chart resolves the secret with a Helm `lookup`, which returns nothing during `helm template` or `--dry-run`. Those commands render the storage config without credentials; only a real install picks them up. If your secret uses different field names, set `credentialsSecretRef.accessKeyIdKey` and `credentialsSecretRef.secretKeyKey` to match.

5. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

6. Install the data plane. Replace `<PATH_TO_VALUES_FILE>` with the path to the Helm values file you customized in step 4, and `<CLIENT_ID>` / `<CLIENT_SECRET>` with the credentials printed in step 3.

   ```bash
   helm upgrade --install unionai-dataplane unionai/dataplane \
     --namespace union --create-namespace \
     --values <PATH_TO_VALUES_FILE> \
     --set-string global.AUTH_CLIENT_ID=<CLIENT_ID> \
     --set secrets.admin.clientId=<CLIENT_ID> \
     --set secrets.admin.clientSecret=<CLIENT_SECRET> \
     --timeout 10m
   ```

7. Verify the pods are running:

   ```bash
   kubectl get pods -n union
   ```

   When the deployment succeeds, all pods show a `Running` status, including `union-operator-proxy`, `union-operator-buildkit`, and `executor`.

8. Verify the cluster is registered with the control plane:

   ```bash
   flyte get cluster
   ```

   The output is similar to the following:

   ```text
   Enabled Clusters
   NAME            ORG       STATE     HEALTH
   union-nebius    my-org    enabled   healthy
   ```

## GPU node configuration (Nebius-specific)

Follow these steps to run GPU workloads on Nebius:

1. Ensure the NVIDIA device plugin is installed and your task definitions request GPU resources. Nebius MK8s pre-installs the NVIDIA GPU operator on GPU node groups, so no additional setup is typically required. Learn more about [how to add nodes with GPUs to a cluster](https://docs.nebius.com/kubernetes/gpu/set-up#how-to-add-nodes-with-gpus-to-a-cluster).

2. Configure the Union backend to inject the required tolerations and label selectors so only tasks that require GPUs land in GPU-enabled nodes:

   1. Identify the node(s) that have GPU devices available:

      ```bash
      kubectl get nodes -o jsonpath='{range .items[?(@.status.allocatable.nvidia\.com/gpu)]}{.metadata.name}{"\n"}{end}'
      ```

   2. Get the labels of a GPU node:

      ```bash
      kubectl get node <node-name> -o jsonpath='{.metadata.labels}' | jq
      ```

      Nebius nodes typically include a label that displays the instance type. For example, for a node with NVIDIA H200 GPUs:

      ```text
      beta.kubernetes.io/instance-type=gpu-h200-sxm
      ```

   3. If the GPU device supports MIG partitions, the node typically also has a label indicating the partition profile. For example:

      ```text
      nvidia.com/gpu-partition-size: 2g.35gb
      ```

3. Update your Helm values file with the information gathered in the previous steps:

   ```yaml
   # all the existing content of your values file
   ...

   # ADD
   config:
     k8s:
       plugins:
         k8s:
           gpu-device-node-label: "beta.kubernetes.io/instance-type"
           accelerator-devices:
             - H200: "gpu-h200-sxm"
           gpu-partition-size-node-label: "nvidia.com/gpu-partition-size"
   ```

4. Update your installed release:

   ```bash
   helm upgrade unionai-dataplane unionai/dataplane \
     --namespace union \
     --values <PATH_TO_VALUES_FILE> \
     --timeout 10m
   ```

5. Once the above steps are completed, request GPU devices or MIG partitions directly from the Flyte task:

   ```python
   from flyte import Resources

   @env.task(resources=Resources(gpu="H200:1", memory="64Gi"))
   def train_model(...):
       ...
   ```

## Working with the Nebius Container Registry

Flyte executions bundle your code and run it inside a container in the Nebius MK8s cluster. The contents of the image include the `flyte` package, your task code, and any other dependency your workflow requires.

Flyte automates building the image using an efficient layered mechanism to detect changes. You can decide where to store the images. This section covers the configuration if you plan to use Nebius Container Registry to store your container images.

1. Obtain a long-lived token from Nebius as described in [Working in a CI/CD environment](https://docs.nebius.com/container-registry/authentication#working-in-a-ci/cd-environment).

2. Get the static key token value from the previous step (it usually starts with `v1...`) and add it to an environment variable:

   ```bash
   TOKEN='v1.CmQK...'
   ```

3. Encode it into a docker config file (replace the registry region accordingly):

   ```bash
   cat > docker-config-nebius.json <<EOF
   {
     "auths": {
       "cr.eu-north1.nebius.cloud": {
         "auth": "$(echo -n "iam:${TOKEN}" | base64)"
       }
     }
   }
   EOF
   ```

4. Create an image pull secret:

   ```bash
   flyte create secret --type image_pull nebius-image-secret \
     --from-docker-config \
     --docker-config-path docker-config-nebius.json \
     --registries cr.eu-north1.nebius.cloud
   ```

5. Use it in your Flyte `Image` definition:

   ```python
   custom_image = flyte.Image.from_debian_base(
       registry="cr.eu-north1.nebius.cloud/e00...",
       registry_secret="<your-secret-name>",
   )
   ```

6. Request the secret in your Flyte `TaskEnvironment` so tasks can pull the image:

   ```python
   env = flyte.TaskEnvironment(
       name="hello_v2",
       image=custom_image,
       secrets=["<your-secret-name>"],
   )
   ```

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

## Next: manage your cluster and pools

`uctl selfserve provision-dataplane-resources` provisions the data plane and
registers this cluster with the control plane. Once it is connected, you manage
the **cluster pool** it belongs to, and route work to it with queues, from the
[Cluster and workload management](../../../user-guide/cluster-workload-management/_index)
user guide:

- [Cluster pools](../../../user-guide/cluster-workload-management/cluster-pools): group clusters that share one data plane (object store, secrets, registry).
- [Clusters](../../../user-guide/cluster-workload-management/clusters): inspect and manage the cluster records registered with the control plane.
- [Queues](../../../user-guide/cluster-workload-management/queues): route workloads to a pool and enforce concurrency, priority, and fairness.

Every organization is provisioned with a `default` pool that new clusters join
automatically, so a single-cluster deployment needs no extra pool setup.

## Additional resources

For more information, see the following resources:

- [Nebius Managed Kubernetes documentation](https://docs.nebius.com/kubernetes)
- [Nebius Object Storage documentation](https://docs.nebius.com/object-storage)
- [Nebius IAM and service accounts](https://docs.nebius.com/iam)
