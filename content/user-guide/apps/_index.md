---
title: Apps
description: Long-running services for dashboards, REST APIs, and model endpoints.
icon: window
weight: 3
variants: +flyte +union
---

# Apps

An app is a long-running service that Flyte keeps up, rather than a job that runs to completion. Use an app when something needs to stay reachable at a URL: a dashboard, a REST API, a model endpoint, or an MCP server.

Apps are declared the same way tasks are. An `AppEnvironment` names the image, the port, and the scaling behavior, and the code inside it is an ordinary web application.

```python
app = flyte.app.AppEnvironment(name="dashboard", image=..., port=8080)
```

Because apps and tasks live in the same project, an app can read what a task produced without moving data between systems, and a task can call an app it depends on.

Apps scale to zero when idle, so a rarely-used dashboard costs nothing between visits.

{{< grid >}}

{{< link-card target="configure-apps" icon="gear" title="Configure apps" >}}
Define `AppEnvironment`s with ports, autoscaling, custom domains, and authentication.
{{< /link-card >}}

{{< link-card target="build-apps" icon="code" title="Build apps" >}}
Build dashboards, REST APIs, and model endpoints with FastAPI, Streamlit, vLLM, and more.
{{< /link-card >}}

{{< link-card target="native-app-integrations" icon="plugin" title="Native app integrations" >}}
Use pre-built environments for popular frameworks like Streamlit, FastAPI, vLLM, SGLang, and Ollama.
{{< /link-card >}}

{{< link-card target="serve-and-deploy-apps" icon="rocket" title="Serve and deploy apps" >}}
Use `flyte serve` for fast iteration or `flyte deploy` for production deployments.
{{< /link-card >}}

{{< /grid >}}

## Related

{{< grid >}}

{{< link-card target="../tasks" icon="gear" title="Tasks" >}}
The batch workloads an app usually serves the results of.
{{< /link-card >}}

{{< link-card target="../agents" icon="robot" title="Agents" >}}
Agents are often deployed as apps so they can be reached over HTTP.
{{< /link-card >}}

{{< /grid >}}
