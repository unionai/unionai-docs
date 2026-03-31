---
title: Data plane setup on OCI
weight: 6
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on OCI

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.
The Union architecture is described on the [Architecture](./architecture/_index) page.

## Object Storage

Each data plane uses OCI Object Storage buckets to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

Create your bucket(s) in the [OCI Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm) or via the OCI CLI.

### CORS Configuration

To enable the [Code Viewer](./configuration/code-viewer) in the Union UI, configure a CORS policy on your bucket(s). This allows the UI to securely fetch code bundles directly from storage.

OCI Object Storage CORS is configured via bucket settings. See the [OCI CORS documentation](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-CORS.htm) for details. Apply the following rule:

- **Allowed Origins:** `https://*.unionai.cloud`
- **Allowed Methods:** `GET`, `HEAD`
- **Allowed Headers:** `*`
- **Expose Headers:** `ETag`
- **Max Age Seconds:** `3600`

### Data Retention

Union recommends using lifecycle policies on these buckets to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## Container Registry

Create an [OCI Container Registry (OCIR)](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm) repository for Image Builder to push and pull container images. Note the repository path (e.g. `<REGION>.ocir.io/<TENANCY_NAMESPACE>/<REPOSITORY>`) — you will reference it when configuring access below.

## Identity & Access

Union services and workflow task pods need access to your Object Storage buckets and Container Registry. OCI supports two authentication models:

### Option A: Instance Principals (recommended)

Use [Instance Principals](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm) so that pods running on OKE nodes inherit permissions automatically.

1. Create a [Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm) matching your OKE worker nodes:

   ```
   ALL {instance.compartment.id = '<COMPARTMENT_OCID>'}
   ```

2. Create IAM policies granting the dynamic group access to Object Storage and OCIR:

   ```
   Allow dynamic-group <DYNAMIC_GROUP_NAME> to manage objects in compartment <COMPARTMENT_NAME> where target.bucket.name='<BUCKET_NAME>'
   Allow dynamic-group <DYNAMIC_GROUP_NAME> to manage repos in compartment <COMPARTMENT_NAME>
   ```

### Option B: Static Credentials

If Instance Principals are not available, you can use S3-compatible access keys:

1. Generate a [Customer Secret Key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#s3) for S3 Compatibility API access.
2. You will configure these credentials in the generated values file during deployment (see step 3 below).

## OKE Configuration

Union recommends configuring your OKE cluster as indicated in [Cluster Recommendations](./cluster-recommendations).

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor Kubernetes versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured Object Storage bucket(s), Container Registry, and IAM access as described above.

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../api-reference/uctl-cli/_index).

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authorization permissions for the app to operate on the union cluster name you have selected, generate values file to install dataplane in your Kubernetes cluster and provide follow-up instructions:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider oci
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `oci`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your Object Storage bucket name(s).
   - Set `storage.region` to your OCI region.
   - If using static credentials (Option B), set `storage.accessKey` and `storage.secretKey` to your S3 Compatibility API credentials.

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
