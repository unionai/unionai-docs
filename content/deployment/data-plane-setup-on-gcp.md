---
title: Data plane setup on GCP
weight: 6
variants: -flyte -serverless +byoc -selfmanaged
---

# Data plane setup on GCP

To set up your data plane on Google Cloud Platform (GCP) you must allow {{< key product_name >}} to provision and maintain compute resources under your GCP account.
To do this you will need to provision a service account with sufficient permissions to perform these tasks.

## Select or create a project

The first step is to select an existing project or create a new one.
This is where {{< key product_name >}} will provision all resources for your data plane.
Below, we use the placeholder `<ProjectID>` for the project ID.
The actual ID can be whatever you choose.
In addition, you will need the project number associated with your project.
Below we use the placeholder `<ProjectNumber>`.
The project number is visible on your project's [welcome page](https://console.cloud.google.com/welcome).

## Ensure billing is linked

Before your data plane can be deployed, you need to make sure that a billing account is linked to your project:
Go to the [billing page](https://console.cloud.google.com/billing/linkedaccount) of your `<ProjectId>` project and confirm that a billing account is linked.

## Create a workload identity pool and provider

Though your data plane will be in your project in GCP, the {{< key product_name >}} control plane is still run in AWS.
To allow the control plane to interact with your data plane you must create a _workload identity pool_ and add {{< key product_name >}}'s AWS account as a workload provider.
For more details see the Google Cloud guide for [setting up workload identity federation](https://cloud.google.com/iam/docs/configuring-workload-identity-federation).

### In the GCP web console

1. In your project `<ProjectId>`, under **IAM & Admin > Workload Identity Federation**, select **+ CREATE POOL** to [create a new workload provider and pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/create).
If you have not done so already, you will be guided to [enable the required APIs](https://console.cloud.google.com/flows/enableapi?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com,iamcredentials.googleapis.com,sts.googleapis.com).
2. **Pool Name**: `unionai` (you can also fill in the description if you like).
3. Under **Add a provider to pool**:
  * For **Select a provider**, choose **AWS**.
  * For **Provider name**, enter `unionai-aws`.
  * The **Provider ID** should be automatically set to `unionai-aws` as well. If not, select **EDIT** and enter it manually.
4. For **AWS Account ID**, enter `479331373192` ({{< key product_name >}}'s management account ID)
5. **Continue** with the default attribute mappings and conditions.

### On the command line using `gcloud`

Assuming you have the [`gcloud` tool ](https://cloud.google.com/sdk/gcloud)installed locally and are logged into `<UnionDataPlaneProjectID>`, you can check the existing workflow identity pools in your project with:

```shell
$ gcloud iam workload-identity-pools list --location="global"
```

To create the workload identity pool, do:

```shell
$ gcloud iam workload-identity-pools create unionai \
    --location="global" \
    --description="Union AI WIF" \
    --display-name="unionai"
```

To add the provider, do:

```shell
$ gcloud iam workload-identity-pools providers create-aws unionai-aws \
    --location="global"  \
    --workload-identity-pool="unionai" \
    --account-id="479331373192"
```

## Create a role for {{< key product_name >}} admin

To ensure that the {{< key product_name >}} team has all the privileges needed to deploy the data plane, _but no more than strictly necessary_, you will need to create a custom role that the {{< key product_name >}} service account will assume.

To avoid having to manually select each separate required privilege we recommend that you perform this step on the command-line with `gcloud`.

First, you will need to download the following YAML file to the directory where you are running your `gcloud` commands.
This file is the role definition. It is a list of the privileges that will make up the new role.

- [`union-ai-admin-role.yaml`](https://github.com/unionai/union-cloud-infrastructure/blob/main/union-ai-admin/gcp/union-ai-admin-role.yaml)

Assuming you have the above file (`union-ai-admin-role.yaml`) in your current directory and substituting your project ID, do:

```shell
$ gcloud iam roles create UnionaiAdministrator \
    --project=<ProjectId> \
    --file=union-ai-admin-role.yaml
```

## Create the {{< key product_name >}} admin service account

### In the GCP web console

1. Go to **IAM & Admin >** [**Service Accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts).
2. Select **Create Service Account**
3. For **Name**, enter `{{< key product_name >}} Administrator`.
4. For **ID**, enter `unionai-administrator`.
_Note that setup process used by the {{< key product_name >}} team depends on the ID being this precise string_.
_If you use a different ID (though this is not recommended) then you must inform the {{< key product_name >}} team of this change._
5. You can enter a **Description** if you wish.
6. Grant this service account access to your project `<ProjectId>` with the role create above, `UnionaiAdministrator`.

### On the command line using `gcloud`

Create the service account like this:

```shell
$ gcloud iam service-accounts create unionai-administrator \
    --project <ProjectId>
```

Bind the service account to the project and add the {{< key product_name >}} Administrator role like this (again, substituting your project ID):

```shell
$ gcloud projects add-iam-policy-binding <ProjectId> \
    --member="serviceAccount:unionai-administrator@<ProjectId>.iam.gserviceaccount.com" \
    --role="projects/<ProjectId>/roles/UnionaiAdministrator"
```

## Grant access for the Workflow Identity Pool to the Service Account

### In the GCP web console

1. Go to the newly created [workload identity pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/pool/unionai) page.
2. Select **Grant Access**.
3. Choose the newly created service account.
4. Select **Save**.

### On the command line using `gcloud`

To grant the WIP access to the service account, do the following.
Notice that you must substitute your `<ProjectId>` and your `<ProjectNumber>`.

```shell
$ gcloud iam service-accounts add-iam-policy-binding unionai-administrator@<ProjectId>.iam.gserviceaccount.com \
      --project=<ProjectId> \
      --role="roles/iam.workloadIdentityUser" \
      --member="principalSet://iam.googleapis.com/projects/<ProjectNumber>/locations/global/workloadIdentityPools/unionai/*"
```

## Enable services API

You will need to enable the following service APIs.

| Name | Endpoint |
|------|----------|
| Artifact Registry API | `artifactregistry.googleapis.com` |
| Cloud Autoscaling API | `autoscaling.googleapis.com` |
| Cloud Key Management Service (KMS) API | `cloudkms.googleapis.com` |
| Cloud Resource Manager API | `cloudresourcemanager.googleapis.com` |
| Compute Engine API | `compute.googleapis.com` |
| Kubernetes Engine API | `container.googleapis.com` |
| Container File System API | `containerfilesystem.googleapis.com` |
| Container Registry API | `containerregistry.googleapis.com` |
| Identity and Access Management (IAM) APIs | `iam.googleapis.com` |
| IAM Service Account Credentials API | `iamcredentials.googleapis.com` |
| Cloud Logging API | `logging.googleapis.com` |
| Cloud Monitoring API | `monitoring.googleapis.com` |
| Secret Manager API | `secretmanager.googleapis.com` |
| Service Networking API | `servicenetworking.googleapis.com` |
| Security Token Service API | `sts.googleapis.com` |
| Cloud SQL Admin API | `sqladmin.googleapis.com` |
| Cloud Storage Services API | `storage-api.googleapis.com` |

### In the GCP web console

Go to [Google Cloud API library](https://console.cloud.google.com/apis/library) and enable each of these by searching for it and clicking **ENABLE**.

### On the command line using `gcloud`

Perform the following `gcloud` commands:

```shell
$ gcloud services enable artifactregistry.googleapis.com
$ gcloud services enable autoscaling.googleapis.com
$ gcloud services enable cloudkms.googleapis.com
$ gcloud services enable cloudresourcemanager.googleapis.com
$ gcloud services enable compute.googleapis.com
$ gcloud services enable container.googleapis.com
$ gcloud services enable containerfilesystem.googleapis.com
$ gcloud services enable containerregistry.googleapis.com
$ gcloud services enable iam.googleapis.com
$ gcloud services enable iamcredentials.googleapis.com
$ gcloud services enable logging.googleapis.com
$ gcloud services enable monitoring.googleapis.com
$ gcloud services enable secretmanager.googleapis.com
$ gcloud services enable servicenetworking.googleapis.com
$ gcloud services enable sts.googleapis.com
$ gcloud services enable sqladmin.googleapis.com
$ gcloud services enable storage-api.googleapis.com
```

## Export Workflow Identity Config

1. Go to the newly created [workload identity pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/pool/unionai) page.
2. Select **Connected Service Accounts** in the right pane.
3. Select **Download** under **Client Library Config**.
4. Send the downloaded file to the {{< key product_name >}} Team to complete the setup process.
   There are no secrets stored in this file.

## Setting up and managing your own VPC (optional)

If you decide to manage your own VPC instead of leaving it to {{< key product_name >}}, then you will need to set it up yourself.
The VPC should be configured with the following characteristics:

* We recommend using a VPC that resides in the same project as the {{< key product_name >}} Data Plane Kubernetes cluster. If you want to use a [shared VPC](https://cloud.google.com/vpc/docs/shared-vpc), contact {{< key product_name >}} support.
* Create a single VPC subnet with:
  * A primary IPv4 range with /18 CIDR mask. This is used for cluster node IP addresses.
  * A secondary range with /15 CIDR mask. This is used for Kubernetes Pod IP addresses. We recommend associating the name with pods, e.g. `gke-pods`.
  * A secondary range with /18 CIDR mask. This is used for Kubernetes service IP address. We recommend associating the name with services, e.g. `gke-services`.
  * Identify a /28 CIDR block that will be used for the Kubernetes Master IP addresses. Note this CIDR block is not reserved within the subnet. Google Kubernetes Engine requires this /28 block to be available.

Once your VPC is set up, provide the following to {{< key product_name >}}:

* VPC name
* Subnet region and name
* The secondary range name for the /15 CIDR mask and /16 CIDR mask
* The /18 CIDR block that was left unallocated for the Kubernetes Master

### Example VPC CIDR Block allocation

* 10.0.0.0/18 Subnet 1 primary IPv4 range → Used for GCP Nodes
* 10.32.0.0/14 Cluster secondary IPv4 range named `gke-pods` → Used for Kubernetes Pods
* 10.64.0.0/18 Service secondary IPv4 range named `gke-services` → Used for Kubernetes Services
* 10.65.0.0/28 Unallocated for Kubernetes Master
