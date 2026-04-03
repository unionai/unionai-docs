---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required resources (Kubernetes cluster, object storage, container registry, credentials), see [Prepare infrastructure](../selfmanaged-generic/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/).
* Object storage provided by a vendor or an S3-compatible platform (such as [MinIO](https://min.io)), with CORS configured as described in [Prepare infrastructure](../selfmanaged-generic/prepare-infra).
* A container registry accessible from your cluster.

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
