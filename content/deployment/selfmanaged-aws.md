---
title: Data plane setup on AWS
weight: 4
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on AWS

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](./architecture/_index) page.

## S3

Each data plane uses S3 buckets to store data used in workflow execution.
Union recommends the use of two S3 buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

### Data Retention

Union recommends using Lifecycle Policy on these buckets to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## ECR

Create an [ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) for Image Builder to push and pull container images. Note the repository URI (e.g. `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<REPOSITORY>`) — you will reference it when configuring IAM permissions below.

## IAM

Create an IAM role for the `union-system` service account and grant it access to your S3 buckets and ECR.

1. Create an [IAM OIDC provider for your EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_eksctl).

2. Create a new IAM role named `union-system-role`. This role will be assumed by the `union-system` Kubernetes service account via [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

   The Trust Policy for this role will be:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Federated": "arn:aws:iam::$account_id:oidc-provider/$oidc_provider"
               },
               "Action": "sts:AssumeRoleWithWebIdentity",
               "Condition": {
                   "StringEquals": {
                       "$oidc_provider:aud": "sts.amazonaws.com",
                       "$oidc_provider:sub": "system:serviceaccount:<NAMESPACE>:union-system"
                   }
               }
           }
       ]
   }
   ```

   You can obtain the OIDC provider value using the AWS CLI:

   ```bash
   aws eks describe-cluster --region $cloud_region --name $cluster_name --query "cluster.identity.oidc.issuer" --output text
   ```

3. Create and attach an IAM policy to this role granting S3 access:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "S3BucketAccess",
               "Effect": "Allow",
               "Action": [
                   "s3:DeleteObject*",
                   "s3:GetObject*",
                   "s3:ListBucket",
                   "s3:PutObject*"
               ],
               "Resource": [
                   "arn:aws:s3:::<bucket-name>",
                   "arn:aws:s3:::<bucket-name>/*"
               ]
           }
       ]
   }
   ```

4. Attach ECR permissions to the same role for Image Builder:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "ECRAuth",
               "Effect": "Allow",
               "Action": [
                   "ecr:GetAuthorizationToken"
               ],
               "Resource": "*"
           },
           {
               "Sid": "ECRReadWrite",
               "Effect": "Allow",
               "Action": [
                   "ecr:BatchCheckLayerAvailability",
                   "ecr:BatchGetImage",
                   "ecr:GetDownloadUrlForLayer",
                   "ecr:DescribeImages",
                   "ecr:PutImage",
                   "ecr:InitiateLayerUpload",
                   "ecr:UploadLayerPart",
                   "ecr:CompleteLayerUpload"
               ],
               "Resource": "arn:aws:ecr:<AWS_REGION>:<AWS_ACCOUNT_ID>:repository/<REPOSITORY>"
           }
       ]
   }
   ```

5. Annotate the `union-system` service account with the role ARN in your Helm values:

   ```yaml
   commonServiceAccount:
     annotations:
       eks.amazonaws.com/role-arn: "arn:aws:iam::<account_id>:role/union-system-role"
   ```

## EKS configuration

Union recommends installing the following EKS add-ons:
  - CoreDNS
  - Amazon VPC CNI
  - Kube-proxy

Union supports Autoscaling and the use of spot (interruptible) instances.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor K8s versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured S3 bucket(s) and IAM role as described above.

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
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider aws
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `aws`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your S3 bucket name(s).
   - Set `storage.region` to the AWS region of your bucket(s).
   - Replace all occurrences of `<UNION_FLYTE_ROLE_ARN>` with the ARN of the IAM role created in the [IAM](#iam) section (e.g. `arn:aws:iam::<account_id>:role/union-system-role`). This appears in `additionalServiceAccountAnnotations`, `userRoleAnnotationValue`, and `fluentbit.serviceAccount.annotations`.

4. Optionally configure the resource `limits` and `requests` for the different services.
   By default, these will be set minimally, will vary depending on usage, and follow the Kubernetes `ResourceRequirements` specification.

   * `operator.resources`
   * `executor.resources`
   * `proxy.resources`
   * `flytepropellerwebhook.resources`

5. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

   ```bash
   uctl get cluster
    ----------- ------- --------------- -----------
   | NAME      | ORG   | STATE         | HEALTH    |
    ----------- ------- --------------- -----------
   | <cluster> | <org> | STATE_ENABLED | HEALTHY   |
    ----------- ------- --------------- -----------
   1 rows
   ```

6. You can then register and run some example workflows through your cluster to ensure that it is working correctly.

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
