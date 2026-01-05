---
title: Configuring your data plane
weight: 3
variants: -flyte -serverless +byoc -selfmanaged
---

# Configuring your data plane

After you set up your data plane account(s), the next step is to specify the infrastructure you want to deploy.
You will need to send the following details to the {{< key product_name >}} team:

* Which [cloud provider](#cloud-provider) will you use?
* Will this be a [multi-cluster](#multi-cluster) setup?
    * If so, how will Flyte domains and/or Flyte projects be mapped to clusters?
    * Additionally, how will clusters be grouped into cluster pools? (Each cluster pool will have its own metadata bucket)
* For each cluster:
    * [Account ID](#account-id) for this cluster (each cluster must be in its own account on your cloud provider)
    * [Region](#region) in which the cluster will be deployed.
    * [VPC](#vpc) setup (will you use your own VPC or have {{< key product_name >}} provision one for you?)
    * [Data retention policy](#data-retention-policy) for workflow execution data stored in this cloud provider account.
    * For each [node group](#node-group-name):
        * [Node type](#node-type)
        * [Minimum](#minimum)
        * [Maximum](#maximum)
        * [Interruptible](#interruptible-instances)
        * [Taints](#taints)
        * [Disk](#disk)

## Cloud provider

You can choose either AWS or GCP as your cloud provider.
If you choose to have multiple clusters, they must all be in the same provider.

## Multi-cluster

You can choose a single or multi-cluster configuration.

In a multi-cluster configuration, you have separate clusters for each of your Flyte domains and/or Flyte projects.

A cluster in this context refers to a distinct EKS (in AWS) or GKE (in GCP) instance in its own AWS account or GCP project.

The most common set up is to have a separate cluster for each Flyte domain: development, staging, and production.

You can further partition your deployment so that each Flyte domain-project pair has its own cluster in its own account.

In addition, clusters are grouped into cluster pools. Each cluster pool will have its own metadata bucket. You can group your clusters into pools based on your own criteria, for example, by region or by the type of workloads that will run on them.

See [Multi-cluster](./multi-cluster) for more information.

## Account ID

Provide the ID of the AWS account or GCP project in which each cluster will reside.

## Region

For each cluster, specify the region. Available regions are `us-west`, `us-east`, `eu-west`, and `eu-central`.

## VPC

Specify whether you want to set up your own VPC or use one provided by {{< key product_name >}}.
If you are provisioning your own VPC, provide the VPC ID.

## Data retention policy

Each cluster has its own internal object store that is used to store data used in the execution of workflows.
This includes task input-output metadata, task input-output raw data, Flyte Decks data, and fast registration data.
For each cluster, you can choose to enable a data retention policy that defines a maximum time for this data to be stored, after which it will be automatically deleted.
Alternatively, you can set this to `unlimited` to disable automatic data deletion.
See [Data retention policy](./data-retention-policy) for more details.

## Worker node groups

Specify the worker node groups (in AWS) or worker node pools (in GCP) that you wish to have, with the following details for each. For more information about worker nodes, see [Platform architecture](./platform-architecture).

### Node group name

The name of the node group. This will be used as the node group name in the EKS or GKE console.

### Node type

The instance type name, for example, `p3d.4xlarge`. (See [AWS instance types](https://aws.amazon.com/ec2/instance-types) or [GCP machine types](https://cloud.google.com/compute/docs/machine-types) for more information. Also see [Resources held back](#resources-held-back) below.)

### Minimum

The minimum node number. The default is `0`.

Setting a minimum of `0` means that an execution may take longer to schedule since a node may have to spun up.
If you want to ensure that at least node is always available, set the minimum to `1`.

Note however, that a setting of `1` will only help the `0` to `1` spin-up issue.
It will not help in the case where you have `1` node available but need `2`, and so forth.
Ultimately, the minimum should be determined by the workload pattern that you expect.

### Maximum

The maximum node number. This setting must be explicitly set to a value greater than `0`.

### Interruptible instances

> [!NOTE]
> In AWS, the term *spot instance* is used.
> In GCP, the equivalent term is *spot vm*.
> Here we use the term *interruptible instance* generically for both providers.

Specify whether this will be a **interruptible instance** or an **on-demand instance** node group.

Note that for each interruptible node group, an identical on-demand group will be configured as a fallback.
This fallback group will be identical in all respects to the interruptible group (instance type, taints, disk size, etc.), apart from being on-demand instead of interruptible.
The fallback group will be used when the retries on the interruptible group have been exhausted.

For more information on interruptible instances, see [Interruptible instances](../user-guide/core-concepts/tasks/task-hardware-environment/interruptible-instances).

### Taints

Specify whether this node group will be a specialized node group reserved for specific tasks (typically with specialized hardware requirements).

If so, it will be configured with a *taint* so that only tasks configured with a *toleration* for that taint will be able to run on it.

Typically, only GPU node groups fall into this specialized category, and they will always be assigned taints in any case. It is not common to place taints on other types of node groups, but you can do so if you wish.

<!-- TODO ADD: For more detail on how taints and tolerations work see [Taints and tolerations](). -->

### Disk

Specify the disk size for the nodes in GiB. The default is `500 GiB`.

## Resources held back

When specifying node types and other resource parameters, you should keep in mind that the nominally quoted amount of a given resource is not always available to Flyte tasks.
For example, in an node instance rated at `16GiB`, some of that is held back for overhead and will not be available to Flyte task processes.

## Example specification
Values provided by you are in single quotes (').

```yaml
- Cloud provider: 'AWS'
- Multi-cluster: 'True'
    - Mapping: 'domain -> cluster'
- Clusters:
    - 'development'
        - Account ID: 'account-id-1'
        - Region: 'us-west'
        - VPC: 'vpc-id-1'
        - Data retention policy: '30 days'
        - Node groups:
            - 'node-group-1'
                - Node type: 'p3d.4xlarge'
                - Min: '2'
                - Max: '5'
                - Spot: 'True'
                - Taints: 'False'
                - Disk: '1500 GiB'
            - 'node-group2'
                - Node type: 't4.24xlarge'
                - Min: '2'
                - Max: '5'
                - Spot: 'True'
                - Taints: 'False'
                - Disk: '1500 GiB'
    - 'staging'
        - Account ID: 'account-id-2'
        - Region: 'us-west'
        - VPC: 'vpc-id-2'
        - Data retention policy: '30 days'
        - Node groups:
            - 'node-group-1'
                - Node type: 'p3d.4xlarge'
                - Min: '2'
                - Max: '5'
                - Spot: 'True'
                - Taints: 'False'
                - Disk: '1500 GiB'
            - 'node-group-2'
                - Node type: 't4.24xlarge'
                - Min: '2'
                - Max: '5'
                - Spot: 'True'
                - Taints: 'False'
                - Disk: '1500 GiB'
    - 'production'
        - Account ID: 'account-id-3'
        - Region: 'us-west'
        - VPC: 'vpc-id-3'
        - Data retention policy: 'unlimited'
        - Node groups:
            - 'node-group-1'
                - Node type: 'p3d.4xlarge'
                - Min: '2'
                - Max: '5'
                - Spot: 'False'
                - Taints: 'False'
                - Disk: '1500 GiB'
            - 'node-group-2'
                - Node type: 't4.24xlarge'
                - Min: '2'
                - Max: '5'
                - Spot: 'False'
                - Taints: 'False'
                - Disk: '1500 GiB'
```

## After deployment

Once {{< key product_name >}} has configured and deployed your cluster(s), you will be able to see your data plane setup in [Usage > Compute](../user-guide/administration/resources).

## Adjusting your configuration

To make changes to your cluster configuration, go to the [{{< key product_name >}} Support Portal](https://get.support.union.ai/servicedesk/customer/portal/1/group/6/create/30).
This portal also accessible from **Usage > Compute** through the **Adjust Configuration** button.