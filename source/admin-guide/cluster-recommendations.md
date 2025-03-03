# Cluster Recommendations

Union is capable of running on any Kubernetes cluster.  This includes managed Kubernetes services such as Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS), and Amazon Elastic Kubernetes Service (EKS), as well as self-managed Kubernetes clusters.

While many configurations are supported, we have some recommendations to ensure the best performance and reliability of your Union deployment.

## Kubernetes Versions

We recommend running Kubernetes versions that are [actively supported by the Kubernetes community](https://kubernetes.io/releases/).  This
typically means running one of the most recent three minor versions.  For example, if the most recent version is 1.32, we recommend
running 1.32, 1.31, or 1.30.

## Networking Requirements

Many Container Network Interface (CNI) plugins require planning for IP address allocation capacity.  For example, [Amazon's VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html) and [GKE's Dataplane v2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)
allocate IP addresses to Kubernetes Pods out of one or more or your VPC's subnets.  If you are using one of these CNI plugins, you should
ensure that your VPC's subnets have enough available IP addresses to support the number of concurrent tasks you expect to run.

We recommend using at least a `/16` CIDR range (65,536 addresses), you may optionally sub-divide this range into smaller subnets to
support multiple availability zones or other network segmentation requirements.

In short, you should aim to have at least 1 IP address available for each task you expect to run concurrently.
