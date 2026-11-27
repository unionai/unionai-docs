---
title: Task access to cloud resources
description: Which cloud identity your tasks run as on a data plane created with the Add a cluster wizard, and how to give it access to your own resources.
icon: key
weight: 5
variants: -flyte +union
---

# Task access to cloud resources

On a data plane created with the **Add a cluster** wizard, task pods run by default as one cloud identity that Union.ai creates in your account: the cluster's _worker_ identity. A task or run that sets its own `service_account` doesn't run as it.
To let your task code reach your own cloud resources, such as a storage bucket, grant that identity access to them in your cloud account. On AWS, a permissions boundary limits what you can grant: see [AWS](#aws).
Access you grant the worker identity applies to tasks in all projects and domains.

For a data plane that wasn't created with the wizard, see [Legacy setup](./legacy/_index) instead. Those data planes use different identities.

## AWS

Tasks run as the IAM role `<cluster>-worker`, where `<cluster>` is the name of the EKS cluster Union.ai created for the data plane.
Union.ai names that cluster `union-<org>-<cluster name>` and shortens long names, ending them with a short hash.
To find the role, search **IAM → Roles** in the AWS console for the EKS cluster's name.

The role carries a permissions boundary created by the CloudFormation stack you launched: a managed policy whose name starts with `union-ai-admin` and ends with `-boundary`.
A policy you attach to the role grants only what the boundary also allows:

- S3 only on buckets whose names start with `union-`.
- Secrets Manager only on the secrets that hold {{< key product_name >}} secrets, and secrets whose names start with `union-`.
- No access to services such as DynamoDB, SQS, or Athena, and no `sts:AssumeRole` into another IAM role.

So a policy that grants access to an S3 bucket with another name, for example, has no effect.

## GCP

Tasks run as the service account `<prefix>-worker@<project>.iam.gserviceaccount.com`, where `<prefix>` is the name of the GKE cluster Union.ai created for the data plane and `<project>` is your GCP project ID.
Union.ai names that cluster `union-<org>-<cluster name>` and shortens long names, ending them with a short hash.
You can find the service account under **IAM & Admin → Service accounts** in the Google Cloud console.

To give your tasks access to a resource, add the service account as a principal on that resource, or on the project, with a role that has the permissions your code needs.
For example, on a Cloud Storage bucket, grant it **Storage Object Viewer** to read objects, or **Storage Object Admin** to read and write them.

## Azure

Tasks run as the user-assigned managed identity `<prefix>-worker`, in the resource group `<prefix>` that the setup script created.
`<prefix>` is `union-<org>-<cluster name>`, and long names are shortened, ending with a short hash.
You can find the identity under **Managed Identities** in the Azure portal.

The setup script gives the identity these roles on that resource group: **Storage Blob Data Contributor**, **Key Vault Secrets User**, and **AcrPush**.
To give your tasks access to a resource outside the resource group, [create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) for the identity on that resource.
For example, assign **Storage Blob Data Contributor** on a storage account or container to read and write blobs, or **Key Vault Secrets User** on a key vault to read its secrets.
