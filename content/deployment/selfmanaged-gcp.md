---
title: Data plane setup on GCP
weight: 4
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on GKE (GCP)

{{< key product_name >}}’s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.
The Union architecture is described on the [Architecture](./architecture/_index) page.

## GCS

Each data plane uses GCS buckets to store data used in workflow execution.
Union recommends the use of two buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

### CORS Configuration

To enable the [Code Viewer](./configuration/code-viewer) in the Union UI, configure a CORS policy on your fast registration bucket (or your single bucket if using one):

1. Create a `cors.json` file:

   ```json
   [
       {
           "origin": ["https://*.unionai.cloud"],
           "method": ["HEAD", "GET"],
           "responseHeader": ["ETag"],
           "maxAgeSeconds": 3600
       }
   ]
   ```

2. Apply the CORS configuration:

   ```bash
   gcloud storage buckets update gs://<BUCKET_NAME> --cors-file=cors.json
   ```

### Data Retention

See [Data retention policy](./configuration/data-retention) for information on managing storage costs with lifecycle policies.

## Artifact Registry

Create an [Artifact Registry Docker repository](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create) for Image Builder to push and pull container images. Note the repository path (e.g. `<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>`) — you will reference it when configuring Workload Identity permissions below.

## Workload Identity

Union recommends using [GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to securely access GCP resources.

Create a Google Service Account and bind it to the `union-system` Kubernetes service account:

```bash
gcloud iam service-accounts add-iam-policy-binding \
  <GSA_NAME>@<PROJECT_ID>.iam.gserviceaccount.com \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:<PROJECT_ID>.svc.id.goog[<NAMESPACE>/union-system]"
```

Grant the following roles to the Google Service Account:

- `roles/storage.objectAdmin` on the GCS bucket(s) used for workflow data
- `roles/artifactregistry.writer` on the Artifact Registry repository used by Image Builder
- `roles/iam.serviceAccountTokenCreator` at the project level (includes `iam.serviceAccounts.signBlob`, required for Image Builder authentication)

Annotate the `union-system` service account with the Google Service Account email in your Helm values:

```yaml
commonServiceAccount:
  annotations:
    iam.gke.io/gcp-service-account: "<GSA_NAME>@<PROJECT_ID>.iam.gserviceaccount.com"
```

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/).
* You have configured GCS bucket(s), Artifact Registry, and Workload Identity as described above.

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
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider gcp
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `gcp`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your GCS bucket name(s).
   - Set `storage.gcp.projectId` to your GCP project ID.
   - Replace all occurrences of `<GCP_SERVICE_ACCOUNT>` with the Google Service Account email created in the [Workload Identity](#workload-identity) section (e.g. `union-system@my-project.iam.gserviceaccount.com`). This appears in `additionalServiceAccountAnnotations`, `userRoleAnnotationValue`, and `fluentbit.serviceAccount.annotations`.

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