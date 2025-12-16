---
title: Multi-cluster and multi-cloud
weight: 4
variants: -flyte -serverless +byoc -selfmanaged
---

# Multi-cluster and multi-cloud

When [configuring your data plane](./configuring-your-data-plane), you can map each domain or project to its own GCP project or AWS subaccount. You can even mix cloud providers: Some of your domains and/or projects can be mapped to AWS subaccounts while others can be mapped to GCP projects.

## Domain isolation

If you choose domain isolation, then you would have one GCP project or AWS subaccount for each domain. For example:

| Domain        | GCP project or AWS subaccount     |
| ------------- | --------------------------------- |
| `development` | `gcp-project-union-development`   |
| `staging`     | `gcp-project-union-staging`       |
| `production`  | `aws-subaccount-union-production` |

## Project isolation

If you choose project isolation, then you would have one GCP project or AWS subaccount for each {{< key product_name >}} project-domain pair. For example:

| Domain/Project          | GCP Project or AWS Subaccount               |
| ----------------------- | ------------------------------------------- |
| `development/project-1` | `gcp-project-union-development-project-1`   |
| `development/project-2` | `gcp-project-union-development-project-2`   |
| `development/project-3` | `gcp-project-union-development-project-3`   |
| `staging/project-1`     | `gcp-project-union-staging-project-1`       |
| `staging/project-2`     | `gcp-project-union-staging-project-1`       |
| `staging/project-3`     | `gcp-project-union-staging-project-1`       |
| `production/project-1`  | `aws-subaccount-union-production-project-1` |
| `production/project-2`  | `aws-subaccount-union-production-project-1` |
| `production/project-3`  | `aws-subaccount-union-production-project-1` |

The precise set of GCP projects and/or AWS subaccounts depends on the number of {{< key product_name >}} domains and projects that you have.

> [!NOTE] Limitations of project per GCP project/AWS subaccount
> Note that if you choose to map each {{< key product_name >}} project to its own GCP project/AWS subaccount,
> you will need to define the set of such projects up front. This is because the {{< key product_name >}} project will have to be
> created when the GCP project/AWS subaccount is set up.
>
> If you also want the ability to create projects on demand, this can be supported by having an additional
> _default_ GCP project/AWS subaccount. Any projects created _after_ onboarding will be created in that
> default GCP project/AWS subaccount.

## Data and metadata isolation

Each domain or project is isolated within its own AWS account or Google project, and therefore provides the level of compute and data isolation intrinsic to that arrangement. Specifically, execution-time isolation per domain or project is maintained for both compute and user data stored in blob store (or other configured storage).

In addition, metadata specific to the internals of {{< key product_name >}} can be either isolated or shared across clusters, depending on the configuration you choose.

Specifically, the sharing of metadata is controlled by the cluster pool to which a cluster belongs. If two clusters are in the same cluster pool, then they _must_ share the same metadata bucket. If they are in different cluster pools, then they _must_ have different metadata buckets. You could, for example, have a single metadata bucket for all your development clusters, and a separate one for all your production clusters, by grouping the clusters into cluster pools accordingly. Alternatively you could have a separate metadata bucket for each cluster, by putting each cluster in its own cluster pool.

You specify the cluster pool to which a cluster belongs when you [configure your data plane](./configuring-your-data-plane) with the help of the {{< key product_name >}} team.
