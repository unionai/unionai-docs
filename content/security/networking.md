---
title: Networking
variants: -flyte -serverless +byoc +selfmanaged
weight: 3
---

# Networking

As described in the architecture, Union has two major components:

| Component     | Purpose                                             | Hosted At |
| ------------- | --------------------------------------------------- | --------- |
| Control Plane | Manages the Union cluster, including the Data Plane | Union     |
| Data Plane    | Executes the workflow tasks                         | Customer  |

## Control Plane <=> Data Plane Communication

### No Ingress

To ensure that the Union system is secure, we do not open public endpoints for the bi-directional communication. We leverage Cloudflare Tunnels for that, protecting both the Data Plane and Control Plane from attacks and threat of exposure.

### Cloudflare

Cloudflare Tunnels provide secure, private, and non-internet connectivity to the customer cloud accounts. The Data Plane needs to reach to the service (egress only) to establish the bi-directional communication of the Control Plane and Data Plane.

**Why?** When a user submits a job, the Data Plane needs to be notified, as fast as possible, that new work needs to be scheduled and executed. Union sends these signals through the Cloudflare tunnel.

In locked down environments, the networking team -- or Union if managing the networking for the customer -- can limit the egress access to the published CIDR blocks of the Cloudflare tunnel. Cloudflare publishes their IP list [here][cloudflare-ips].

You can limit further the IP list by restricting to specific regions. If you plan to do so, instead of using the full list above, please discuss with Union networking team, so they can ensure the cloudflare daemon is also restricted to the same region, as a mismatch between the service and the tunnel can cause service interruption.

### Control Plane

The Data Plane needs to reach out to the Control Plane to establish the bi-directional communication. For this reason, the Control Plane (hosted at Union), exposes an endpoint for the Data Plane.

| Area   | Region         | Endpoint (DNS)               |
| ------ | -------------- | ---------------------------- |
| US     | `us-east-2`    | `hosted.unionai.cloud`       |
| US     | `us-west-2`    | `us-west-2.unionai.cloud`    |
| Europe | `eu-west-1`    | `eu-west-1.unionai.cloud`    |
| Europe | `eu-west-2`    | `eu-west-2.unionai.cloud`    |
| Europe | `eu-central-1` | `eu-central-1.unionai.cloud` |

To acquire the current IP addresses for the service, ensure you resolve the DNS records for the endpoint.

## Cluster Management

> [!WARNING] Do not expose your Kubernetes to the Internet!
>
> Union strongly recommends against exposing your Kubernetes cluster to the Internet.
> Doing so can expose your cluster to security risks, such as unauthorized access, data breaches, and DDoS attacks.
> It will not just make your infrastructure significantly more exposed, but it will violate multiple standards that you > may need to follow.
>
> Please refer to the [Security Standards](standards.md) page for guidance details.

### Technologies

Union leverages the following technologies to provide secure, private, and non-internet connectivity to the customer cloud accounts.

| Provider | Technology              | Documentation                                             |
| -------- | ----------------------- | --------------------------------------------------------- |
| AWS      | AWS Private Link        | https://aws.amazon.com/privatelink/                       |
| GCP      | Private Service Connect | https://cloud.google.com/vpc/docs/private-service-connect |
| Azure    | Azure Private Link      | https://azure.microsoft.com/en-us/products/private-link   |

If you are using a cloud provider that is not listed above, please contact Union to discuss a customized solution that adhere to your security standards.

## Image Builder

Union users can leverage the [Image Builder](../deployment/configuration/image-builder.md) to create and manage container images required to
run workflows tasks with ease.

{{< todo public="true" >}}Add more details about the Image Builder.{{< /todo >}}

[cloudflare-ips]: https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/configure-tunnels/tunnel-with-firewall
