---
title: Databricks connector
weight: 11
variants: +flyte -serverless -byoc -selfmanaged
---

# Databricks connector

This guide provides an overview of how to set up Databricks connector in your Flyte deployment.

## Spin up a cluster

### Flyte binary

You can spin up a demo cluster using the following command:

```bash
flytectl demo start
```

Or install Flyte using the [flyte-binary helm chart](#deployment-deployment-cloud-simple).

### Flyte core

If you've installed Flyte using the
[flyte-core helm chart](https://github.com/flyteorg/flyte/tree/master/charts/flyte-core), please ensure:

- You have the correct kubeconfig and have selected the correct Kubernetes context.
- You have configured the correct flytectl settings in `~/.flyte/config.yaml`.

> [!NOTE]
> Add the Flyte chart repo to Helm if you're installing via the Helm charts.

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
```

## Databricks workspace

To set up your Databricks account, follow these steps:

1. Create a [Databricks account](https://www.databricks.com/).

   ![A screenshot of Databricks workspace creation.](https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/deployment/plugins/databricks/databricks_workspace.png)

2. Ensure that you have a Databricks workspace up and running.

   ![A screenshot of Databricks workspace.](https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/deployment/plugins/databricks/open_workspace.png)

3. Generate a [personal access token](https://docs.databricks.com/dev-tools/auth.html#databricks-personal-ACCESS_TOKEN-authentication) to be used in the Flyte configuration.
   You can find the personal access token in the user settings within the workspace. **User settings** -> **Developer** -> **Access tokens**

   ![A screenshot of access token.](https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/deployment/plugins/databricks/databricks_access_token.png)

4. Enable custom containers on your Databricks cluster before you trigger the workflow.

```bash
curl -X PATCH -n -H "Authorization: Bearer <your-personal-access-token>" \
https://<databricks-instance>/api/2.0/workspace-conf \
-d '{"enableDcs": "true"}'
```

For more detail, check [custom containers](https://docs.databricks.com/administration-guide/clusters/container-services.html).

5. Create an [instance profile](https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html) for the Spark cluster. This profile enables the Spark job to access your data in the S3 bucket.

### Create an instance profile using the AWS console (For AWS Users)

1. In the AWS console, go to the IAM service.
2. Click the Roles tab in the sidebar.
3. Click Create role.
   - Under Trusted entity type, select AWS service.
   - Under Use case, select **EC2**.
   - Click Next.
   - At the bottom of the page, click Next.
   - In the Role name field, type a role name.
   - Click Create role.
4. In the role list, click the **AmazonS3FullAccess** role.
5. Click Create role button.

In the role summary, copy the Role ARN.

   ![A screenshot of s3 arn.](https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/deployment/plugins/databricks/s3_arn.png)

### Locate the IAM role that created the Databricks deployment

1. As an account admin, log in to the account console.
2. Go to **Workspaces** and click your workspace name.
3. In the **Credentials** box, note the role name at the end of the Role ARN

For example, in the Role ARN `arn:aws:iam::123456789123:role/finance-prod`, the role name is `finance-prod`.

### Edit the IAM role that created the Databricks deployment

1. In the AWS console, go to the IAM service.
2. Click the Roles tab in the sidebar.
3. Click the role that created the Databricks deployment.
4. On the **Permissions** tab, click the policy.
5. Click **Edit Policy**.
6. Append the following block to the end of the **Statement** array. Ensure that you don’t overwrite any of the existing policy. Replace `<iam-role-for-s3-access>` with the role you created in **Configure S3 access with instance profiles**.

```json
{
  "Effect": "Allow",
  "Action": "iam:PassRole",
  "Resource": "arn:aws:iam::<aws-account-id-databricks>:role/<iam-role-for-s3-access>"
}
```

## Specify connector configuration

### Flyte binary

#### Demo cluster

Enable the Databricks connector on the demo cluster by updating the ConfigMap:

```bash
kubectl edit configmap flyte-sandbox-config -n flyte
```

```yaml
tasks:
  task-plugins:
    default-for-task-types:
      container: container
      container_array: k8s-array
      sidecar: sidecar
      databricks: connector-service
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
      - connector-service
```

#### Helm chart

Edit the relevant YAML file to specify the plugin.

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
      - connector-service
    default-for-task-types:
      - container: container
      - container_array: k8s-array
      - databricks: connector-service
```

## Add the Databricks access token

Set the Databricks token to the Flyte configuration.

1. Install the flyteconnector pod using helm

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
helm install flyteconnector flyteorg/flyteconnector --namespace flyte
```

2. Set Your Databricks Token as a Secret (Base64 Encoded):

```bash
SECRET_VALUE=$(echo -n "<DATABRICKS_TOKEN>" | base64) && \
kubectl patch secret flyteconnector -n flyte --patch "{\"data\":{\"flyte_databricks_access_token\":\"$SECRET_VALUE\"}}"
```

3. Restart deployment:

```bash
kubectl rollout restart deployment flyteconnector -n flyte
```

## Upgrade the deployment

### Flyte binary

#### Demo cluster

```bash
kubectl rollout restart deployment flyte-sandbox -n flyte
```

#### Helm chart

```bash
helm upgrade <RELEASE_NAME> flyteorg/flyte-binary -n <YOUR_NAMESPACE> --values <YOUR_YAML_FILE>
```

Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte-backend`), `<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`), and `<YOUR_YAML_FILE>` with the name of your YAML file.

For Databricks connector on the Flyte cluster, see [Databricks connector](https://docs.flyte.org/en/latest/flytesnacks/examples/databricks_connector/index.html).
