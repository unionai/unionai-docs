---
title: Deployment
weight: 4
variants: +flyte -serverless +byoc +byok
top_menu: true
mermaid: true
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

Flyte is distributed as a Helm chart with different supported deployment scenarios.  
Union is the platform built on top of Flyte that extends its capabilities to include RBAC, instant containers, real-time serving and more.  
The following diagram describes the available deployment paths for both options:

```mermaid
flowchart TD
    A("Deployment paths") --> n1["Testing/evaluating"] & n4["Production <br>deployment"]
    n1 -- Flyte+Union in the browser --> n2["Union Serverless<br>"]
    n1 -- Compact Flyte cluster in a local container --> n3["flytectl demo start<br>"]
    n4 --> n5["Run Flyte"] & n8["Run Union"]
    n5 -- small scale --> n6["flyte-binary<br>Helm chart"]
    n5 -- large scale or multi-cluster --> n7["flyte-core<br>Helm chart"]
    n8 -- "You manage your data plane. Union manages the control plane" --> n9["Bring Your Own K8s<br>(BYOK)"]
    n8 -- Union manages control and data planes --> n10["Bring Your Own Cloud<br>(BYOC)"]

    n1@{ shape: diam}
    n4@{ shape: rounded}
    n2@{ shape: rounded}
    n3@{ shape: rounded}
    n5@{ shape: diam}
    n8@{ shape: diam}
    n6@{ shape: rounded}
    n7@{ shape: rounded}
    n9@{ shape: rounded}
    n10@{ shape: rounded}
```

This section walks you through the process to create a Flyte cluster and cover topics related to enabling and configuring plugins, authentication, performance tuning, and maintaining Flyte as a production-grade service.

{{< /markdown >}}
{{< /variant >}}
