---
title: Data plane setup on OCI
weight: 4
variants: -flyte -serverless -byoc +selfmanaged
---

# Data plane setup on OCI

{{< key product_name >}}’s modular architecture allows for great flexibility and control. The customer can decide how many clusters to have, their shape, and who has access to what. All communication is encrypted.  The Union architecture is described on the [Architecture](../../architecture) page.

## Assumptions
* You have a {{< key product_name >}} organization and you know the Control Plane URL for your Organization.
* You have a cluster name provided by or coordinated with Union
* You have a Kubernetes cluster, running one of the most recent three minor K8s versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured an storage bucket(s)
* You have configured your OKE cluster as indicated in [Cluster Recommendations](./cluster-recommendations.md).


## Prerequisites
* Install [Helm 3](https://helm.sh/docs/intro/install/)
* Install [union](../api-reference/union-cli) and [uctl](../api-reference/uctl-cli).


## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:
```shell
helm repo add unionai https://unionai.github.io/helm-charts/
helm repo update
```

2. Use the `uctl create admin-oauth-app` command to generate a new client and client secret for communicating with your Union control plane:
```shell
uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
uctl create admin-oauth-app
```
   * The output will emit the ID, name, and a secret that will be used by the union services to communicate with your control plane.
```shell
 --------------- ---------------- ------------------------------------------------------------------
| CLIENT ID     | CLIENT NAME    | SECRET                                                           |
 --------------- ---------------- ------------------------------------------------------------------
| xxxxxxxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx |
 --------------- ---------------- ------------------------------------------------------------------
1 rows
```
   * Save the secret that is displayed. Union does not store the credentials and it cannot be retrieved later.

3. Create a values file that include, at a minimum, the following fields:

```yaml
host: <YOUR_UNION_CONTROL_PLANE_URL>  # Should not include the `https://`.
clusterName: <MY_CLUSTER> #unique cluster identifier
orgName: <MY_ORG> #Name of your {{< key product_name >}} organization
storage:
  provider: "compat"
  endpoint: <STORAGE_ENDPOINT> #This is the S3 API endpoint provided by your cloud vendor.
  accessKey: <S3_ACCESS_KEY>
  secretKey: <S3_SECRET_KEY>
  bucketName: <S3_BUCKET_NAME>
  fastRegistrationBucketName: <S3_BUCKET_NAME> #This can be the same as bucketName
  region: <CLOUD_REGION> #region where your S3 bucket is configured
secrets:
  admin:
    create: true
    clientId: <UNION_CLIENT_ID> # Generated in the previous step
    clientSecret: <UNION_CLIENT_SECRET> # Generated in the previous step
fluentbit:
  env:
    - name: AWS_ACCESS_KEY_ID
      value: <S3_ACCESS_KEY>        # Use the same <S3_ACCESS_KEY> as in storage section
    - name: AWS_SECRET_ACCESS_KEY
      value: <S3_SECRET_KEY>        # Use the same <S3_SECRET_KEY> as in storage section
```

4. Optionally configure the resource `limits` and `requests` for the different services.  By default these will be set minimally, will vary depending on usage, and follow the Kubernetes `ResourceRequirements` specification.
    * `clusterresourcesync.resources`
    * `flytepropeller.resources`
    * `flytepropellerwebhook.resources`
    * `operator.resources`
    * `proxy.resources`

5. Install the {{< key product_name >}} operator and CRDs:
```shell
helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds
helm upgrade --install unionai-dataplane unionai/dataplane \
    --create-namespace \
    --namespace union \
    --values <YOUR_VALUES_FILE>
```

6. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

```shell
uctl get cluster
 ----------- ------- --------------- -----------
| NAME      | ORG   | STATE         | HEALTH    |
 ----------- ------- --------------- -----------
| <cluster> | <org> | STATE_ENABLED | HEALTHY   |
 ----------- ------- --------------- -----------
1 rows
```

7. You can then register and run some example workflows through your cluster to ensure that it is working correctly.

```shell
uctl register examples --project=union-health-monitoring --domain=development
uctl validate snacks --project=union-health-monitoring --domain=development
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
| NAME                 | LAUNCH PLAN NAME                  | VERSION  | STARTED AT                     | ELAPSED TIME | RESULT    | ERROR MESSAGE |
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
| alskkhcd6wx5m6cqjlwm | basics.hello_world.hello_world_wf | v0.3.341 | 2025-05-09T18:30:02.968183352Z | 4.452440953s | SUCCEEDED |               |
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
1 rows
```
