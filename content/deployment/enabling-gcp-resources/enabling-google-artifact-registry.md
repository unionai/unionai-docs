---
title: Enabling Google Artifact Registry
weight: 2
variants: -flyte -serverless +byoc -selfmanaged
---

# Enabling Google Artifact Registry

## Access to Artifact Registry in the same project is enabled by default

When registering tasks and workflows, the {{< key product_name >}} infrastructure in your data plane must have access to the container registry that holds the task container images you will be using.
If your data plane is on GCP then you may want to use Google Artifact Registry (GAR) to store these images.

**In most cases, you will be using a GAR repository in the same GCP project as your data plane.**
**If this is the case, then you do not need to configure anything.**
**Access to GAR in the same project is enabled by default.**

## Enabling cross-project access to Artifact Registry

If you want to store your task container images in a GAR repository in a GCP project _other than the one that holds your data plane_, you must enable the node pool of your data plane to access that GAR.
This is the infrastructure-level access that we discussed [earlier](.#infrastructure-level-access).
It is mediated by the a specific Google Service Account (GSA) which we will refer to here as `<FlyteWorkerGSA>`
(recall that this is in contrast to the task code access, which is mediated by a different default GSA, `<UserFlyteGSA>`).

> [!NOTE] `<FlyteWorkerGSA>`
> Here we refer to the default global-access GSA as`<FlyteWorkerGSA>`because the precise name differs across installations.
> This GSA is identified by name and email of the following form:
>
> * Name: `<OrgName>-flyteworker-<Suffix>`
> * Email: `<OrgName>-flyteworker-<Suffix>@<OrgName>-gcp-dataplane.iam.gserviceaccount.com`

To enable access to the GAR repository in the other account, do the following:

* In your data plane GCP project, go to **IAM > Service Accounts**.
  Find the GSA `<FlyteWorkerGSA>` and copy its email.
  We will call this `<FlyteWorkerGSAEmail>`.
* In the other GCP project account (the one that contains the GAR instance), go to **Artifact Registry > Repositories**.
* Find the GAR repository you want to enable and select the checkbox beside it.
* Under **Permissions** in the side panel, select **Add Principal**.
* Specify the `<FlyteWorkerGSAEmail>` as a **Principal** and assign (at least) the role **Artifact Registry Reader**.
* Select **Save**.

Your {{< key product_name >}} data plane infrastructure should now be able to pull images from the GAR repository.
