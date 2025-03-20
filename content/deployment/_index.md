---
title: Deployment
weight: 4
variants: +flyte -serverless +byoc +byok
top_menu: true
---

# Deployment

{{< variant byoc byok >}}
{{< markdown >}}
Union uses a hybrid model cloud service: Union maintains the control plane of the application on its own cloud infrastructure in Amazon Web Services (AWS).
This is where all administration and management functionality resides.

Your data and the actual computation involved in executing your Flyte tasks and workflows takes place on the data plane, a virtual private cloud that you control but that is administered and managed by the Union control plane.
To enable the administration and management of your data plane, you grant Union the required permissions when you set up your data plane.

Union supports data planes on Amazon WebServices (AWS), Google Cloud Platform (GCP), and Microsoft Azure.
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

Flyte is distributed as a Helm chart with different deployment scenarios supported as described in the following diagram:
```mermaid
flowchart TD
    A("Deployment paths") --> n1["Testing/evaluating"] & n4["Production <br>deployment"]
    n1 -- Flyte+Union in the browser --> n2["Union Serverless<br>"]
    n1 -- Compact Flyte cluster in a local container --> n3["flytectl demo start<br>"]
    n4 --> n5["Run Flyte"] & n8["Run Union"]
    n5 -- small scale --> n6["flyte-binary<br>Helm chart"]
    n5 -- large scale --> n7["flyte-core<br>Helm chart"]
    n8 -- "You manage your data plane. Union manage the control plane" --> n9["Bring your own K8s<br>(BYOK)"]
    n8 -- Union manage control and data planes --> n10["Bring Your Own Cloud<br>(BYOC)"]

    n1@{ shape: diam}
    n4@{ shape: rect}
    n2@{ shape: rect}
    n3@{ shape: rect}
    n5@{ shape: diam}
    n8@{ shape: diam}
    n6@{ shape: rect}
    n7@{ shape: rect}
    n9@{ shape: rect}
    n10@{ shape: rect}
```
This section walks you through the process to create a Flyte cluster and cover topics related to enabling and configuring plugins, authentication, performance tuning, and maintaining Flyte as a production-grade service.

{{< /markdown >}}
{{< /variant >}}
