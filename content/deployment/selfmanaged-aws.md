---
title: Data plane setup on AWS
weight: 4
variants: -flyte -byoc +selfmanaged
---

# Data plane setup on AWS

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](./architecture/_index) page.

## EKS Cluster

You need an EKS cluster running one of the most recent three minor Kubernetes versions. See [Cluster Recommendations](./cluster-recommendations) for networking and node pool guidance.

If you don't already have a cluster, create one with `eksctl`:

```bash
eksctl create cluster \
  --name union-dataplane \
  --region us-east-2 \
  --version 1.31 \
  --node-type m5.xlarge \
  --nodes 3 \
  --with-oidc \
  --managed
```

> [!NOTE] The `--with-oidc` flag creates an IAM OIDC provider for the cluster, which is required for [IRSA](#iam) below.

The following EKS add-ons are required and come pre-installed on managed clusters created with `eksctl`:
  - CoreDNS
  - Amazon VPC CNI
  - Kube-proxy

If you created your cluster through other means, verify they are installed:

```bash
aws eks list-addons --cluster-name union-dataplane --region ${AWS_REGION}
```

Union supports Autoscaling and the use of spot (interruptible) instances.

## S3

Each data plane uses S3 buckets to store data used in workflow execution.
Union recommends the use of two S3 buckets:

1. **Metadata bucket**: contains workflow execution data such as task inputs and outputs.
2. **Fast registration bucket**: contains local code artifacts copied into the Flyte task container at runtime when using `union register` or `union run --remote --copy-all`.

You can also choose to use a single bucket.

Create the buckets:

```bash
export BUCKET_PREFIX=union-dataplane   # choose a globally unique prefix
export AWS_REGION=us-east-2

aws s3api create-bucket \
  --bucket ${BUCKET_PREFIX}-metadata \
  --region ${AWS_REGION} \
  --create-bucket-configuration LocationConstraint=${AWS_REGION}

aws s3api create-bucket \
  --bucket ${BUCKET_PREFIX}-fast-reg \
  --region ${AWS_REGION} \
  --create-bucket-configuration LocationConstraint=${AWS_REGION}
```

> [!NOTE] If your region is `us-east-1`, omit the `--create-bucket-configuration` flag.

### CORS Configuration

To enable the [Code Viewer](./configuration/code-viewer) in the Union UI, configure a CORS policy on your buckets. This allows the UI to securely fetch code bundles directly from S3.

Save the following as `cors.json`:

```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "HEAD"],
      "AllowedOrigins": ["https://*.unionai.cloud"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```

Apply it to both buckets:

```bash
aws s3api put-bucket-cors --bucket ${BUCKET_PREFIX}-metadata --cors-configuration file://cors.json
aws s3api put-bucket-cors --bucket ${BUCKET_PREFIX}-fast-reg --cors-configuration file://cors.json
```

### Data Retention

Union recommends using Lifecycle Policy on these buckets to manage storage costs. See [Data retention policy](./configuration/data-retention) for more information.

## ECR

Create an [ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) for Image Builder to push and pull container images:

```bash
aws ecr create-repository \
  --repository-name union-dataplane/imagebuilder \
  --region ${AWS_REGION} \
  --image-scanning-configuration scanOnPush=true
```

Note the repository URI from the output (e.g. `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/union-dataplane/imagebuilder`) — you will reference it when configuring IAM permissions below.

## IAM

Create an IAM role that both the Union platform services and workflow task pods will use to access S3 and ECR. This role is assumed via [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

### 1. Enable OIDC

If you created your cluster with `--with-oidc` above, this is already done. Otherwise, create an [IAM OIDC provider for your EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_eksctl):

```bash
eksctl utils associate-iam-oidc-provider --cluster union-dataplane --region ${AWS_REGION} --approve
```

Get the OIDC provider URL (you'll need it for the trust policy):

```bash
export OIDC_PROVIDER=$(aws eks describe-cluster \
  --region ${AWS_REGION} \
  --name union-dataplane \
  --query "cluster.identity.oidc.issuer" \
  --output text | sed 's|https://||')

export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```

### 2. Create the IAM role

Save the following trust policy as `trust-policy.json`:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::$AWS_ACCOUNT_ID:oidc-provider/$OIDC_PROVIDER"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "$OIDC_PROVIDER:aud": "sts.amazonaws.com"
                },
                "StringLike": {
                    "$OIDC_PROVIDER:sub": "system:serviceaccount:*"
                }
            }
        }
    ]
}
```

> [!NOTE] Why `system:serviceaccount:*`?
> Union platform services run in the data plane namespace (e.g. `union`), but workflow task pods run in per-project namespaces (e.g. `union-health-monitoring-development`). Both need to assume this role to access S3 and ECR.

Substitute your values and create the role:

```bash
envsubst < trust-policy.json > /tmp/trust-policy.json

aws iam create-role \
  --role-name union-system-role \
  --assume-role-policy-document file:///tmp/trust-policy.json
```

### 3. Attach the S3 policy

Save as `s3-policy.json` (replace `<BUCKET_PREFIX>` with your actual prefix):

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
                "arn:aws:s3:::<BUCKET_PREFIX>-metadata",
                "arn:aws:s3:::<BUCKET_PREFIX>-metadata/*",
                "arn:aws:s3:::<BUCKET_PREFIX>-fast-reg",
                "arn:aws:s3:::<BUCKET_PREFIX>-fast-reg/*"
            ]
        }
    ]
}
```

```bash
aws iam put-role-policy \
  --role-name union-system-role \
  --policy-name union-s3-access \
  --policy-document file://s3-policy.json
```

### 4. Attach the ECR policy

Save as `ecr-policy.json` (replace `<AWS_REGION>`, `<AWS_ACCOUNT_ID>`, and `<REPOSITORY>`):

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

```bash
aws iam put-role-policy \
  --role-name union-system-role \
  --policy-name union-ecr-access \
  --policy-document file://ecr-policy.json
```

### 5. Configure the service account annotation

In your Helm values, annotate the `union-system` service account with the role ARN:

```yaml
commonServiceAccount:
  annotations:
    eks.amazonaws.com/role-arn: "arn:aws:iam::<AWS_ACCOUNT_ID>:role/union-system-role"
```

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have an EKS cluster with OIDC enabled, running one of the most recent three minor K8s versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured S3 bucket(s), ECR, and IAM role as described above.

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
