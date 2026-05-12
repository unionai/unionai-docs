---
title: Build apps
weight: 16
variants: +flyte +union
llm_readable_bundle: true
---

# Build apps

{{< llm-bundle-note >}}

This section covers how to build different types of apps with Flyte, from single-script apps to multi-file projects, common usage patterns, and authentication.

> [!TIP]
> Go to [Introducing apps](../core-concepts/introducing-apps) for an overview of apps and a quick example. For pre-built environments for popular frameworks like Streamlit, FastAPI, vLLM, and SGLang, see [Native app integrations](../native-app-integrations/_index).

## App types

Flyte supports various types of apps:

- **UI dashboard apps**: Interactive web dashboards and data visualization tools like Streamlit and Gradio
- **Web API apps**: REST APIs, webhooks, and backend services like FastAPI and Flask
- **Model serving apps**: High-performance LLM serving with vLLM and SGLang

For ready-to-use environments for these frameworks, see [Native app integrations](../native-app-integrations/_index).

## Usage patterns

Apps and tasks can interact in various ways: calling each other via HTTP, webhooks, WebSockets, or direct browser usage.

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| App | Stand-alone serving app | HTTP requests from arbitrary clients |
| App → App | Microservices, proxies, agent routers, LLM routers | HTTP requests between apps |
| App → Task | Webhooks, APIs triggering workflows | Flyte SDK in app |
| Task → App | Batch processing using inference services | HTTP requests from task |
| Browser app | User-facing dashboards (e.g. Streamlit, Gradio) | Direct browser access |

## Next steps

- [**Single-script apps**](./single-script-apps): The simplest way to build and deploy apps in a single Python script
- [**Multi-script apps**](./multi-script-apps): Build FastAPI and Streamlit apps with multiple files
- [**Serving graphs**](./serving-graphs): Apps calling other apps for microservice architectures
- [**Hybrid graphs**](./hybrid-graphs): Tasks calling apps and apps calling tasks (webhooks, APIs)
- [**WebSocket apps**](./websocket-apps): Real-time, bidirectional communication with WebSockets
- [**Browser apps**](./browser-apps): User-facing dashboards and UIs
- [**Secret-based authentication**](./secret-based-authentication): Authenticate FastAPI apps using Flyte secrets
