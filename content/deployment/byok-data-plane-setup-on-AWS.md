---
title: Data plane setup on AWS
weight: 4
variants: -flyte -serverless -byoc +selfmanaged
---

# Data plane setup on AWS

{{< key product_name >}}’s modular architecture allows for great flexibility and control. The customer can decide how many clusters to have, their shape, and who has access to what. All communication is encrypted.  The Union architecture is described on the [Architecture](../../architecture) page.

## Assumptions
* You have a {{< key product_name >}} organization and you know the Control Plane URL for your Organization.
* You have a cluster name provided by or coordinated with Union
* You have a Kubernetes cluster, running one of the most recent three minor K8s versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured an S3 bucket(s)
* You have an IAM Role, Trust Policy and OIDC provider configured as indicated in the [AWS section in Cluster Recommendations](./cluster-recommendations.md/#aws) section.


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

3.  Create a values file that include, at a minimum, the following fields:

```yaml
host: <YOUR_UNION_CONTROL_PLANE_URL>  # Should not include the `http://`.
clusterName: <MY_CLUSTER> #arbitrary and unique cluster identifier
orgName: <MY_ORG> #Name of your {{< key product_name >}} organization
provider: aws #The cloud provider your cluster is running in.  Acceptable values include `aws`, `gcp`, `azure`, `oci`, and `metal` (for self-managed or on-prem clusters).
storage:
  provider: aws
  authType: iam
  bucketName: <S3_BUCKET_NAME>
  fastRegistrationBucketName: <S3_BUCKET_NAME> #This can be the same as bucketName
  region: <CLOUD_REGION>
  enableMultiContainer: true
secrets:
  admin:
    create: true
    clientId: <UNION_CLIENT_ID> # Generated in the previous step
    clientSecret: <UNION_CLIENT_SECRET> # Generated in the previous step
additionalServiceAccountAnnotations:
  eks.amazonaws.com/role-arn: <UNION_FLYTE_ROLE_ARN>
userRoleAnnotationKey: eks.amazonaws.com/role-arn
userRoleAnnotationValue: <UNION_FLYTE_ROLE_ARN>
fluentbit:
  serviceAccount:
    annotations:
      eks.amazonaws.com/role-arn: <UNION_FLYTE_ROLE_ARN>
```
where `<UNION_FLYTE_ROLE_ARN>` is the ARN of the new IAM role created in the [AWS Cluster Recommendations](./cluster-recommendations.md#iam)


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
