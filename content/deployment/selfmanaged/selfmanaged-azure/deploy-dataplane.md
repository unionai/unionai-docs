---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required Azure resources (AKS cluster, Storage Account, Managed Identities, Workload Identity), see [Prepare infrastructure](../selfmanaged-azure/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have an AKS cluster with OIDC issuer and Workload Identity enabled, running one of the most recent three minor K8s versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/).
* You have configured a Storage Account, Managed Identities, and Workload Identity as described in [Prepare infrastructure](../selfmanaged-azure/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authorization permissions for the app to operate on the Union cluster name you have selected, generate values file to install dataplane in your Kubernetes cluster and provide follow-up instructions:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider azure
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file `<org>-values.yaml` specific to the provider that you specify, in this case `azure`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   Using the [environment variables](../selfmanaged-azure/prepare-infra#environment-variables) from the prepare infrastructure step:

   - Set `global.BACKEND_IAM_ROLE_ARN` to `${BACKEND_CLIENT_ID}` (the backend managed identity client ID).
   - Set `global.WORKER_IAM_ROLE_ARN` to `${WORKER_CLIENT_ID}` (the worker managed identity client ID).
   - Set `global.METADATA_BUCKET` to `${METADATA_CONTAINER}`.
   - Set `storage.custom.stow.config.account` to `${STORAGE_ACCOUNT}`.
   - Set `storage.region` to `${LOCATION}`.
   - Set `commonServiceAccount.annotations."azure.workload.identity/client-id"` to `${BACKEND_CLIENT_ID}`.

   If using Azure Key Vault (optional):
   - Set `AZURE_KEY_VAULT_URI` to `https://${KEY_VAULT_NAME}.vault.azure.net/`.

4. Install the data plane CRDs via server-side apply. The CRDs are vendored in [unionai/helm-charts](https://github.com/unionai/helm-charts) under `crds/`:

   ```bash
   git clone https://github.com/unionai/helm-charts.git
   cd helm-charts

   # Required — FlyteWorkflow CRD consumed by propeller.
   kubectl apply --server-side --force-conflicts -f crds/flyte-v1/

   # Required when monitoring.enabled=true. Skip if monitoring is disabled (the chart default)
   kubectl apply --server-side --force-conflicts -f crds/kube-prometheus-stack/
   ```

   Server-side apply avoids the 256 KiB `last-applied-configuration` annotation overflow on larger CRDs. `--force-conflicts` is needed only on first install.

5. Install the data plane Helm chart with `--skip-crds` so Helm doesn't re-manage the CRDs you just applied:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f <GENERATED_VALUES_FILE> \
     --namespace union \
     --create-namespace \
     --skip-crds \
     --force-conflicts
   ```

6. **Required for helm charts on a version <= 2026.5.8.** Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

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

8. Follow the [Quickstart](../../../user-guide/quickstart) to run your first workflow and verify your cluster is working correctly.
