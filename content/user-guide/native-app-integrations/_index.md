---
title: Native app integrations
weight: 17
variants: +flyte +union
llm_readable_bundle: true
---

# Native app integrations

{{< llm-bundle-note >}}

Flyte ships with a set of pre-built [`AppEnvironment`](../build-apps/_index) integrations that wrap popular frameworks and serving runtimes, so you can deploy common app types without writing the integration glue yourself. Each integration provides a ready-to-use environment class — just configure your app, image, resources, and scaling, and Flyte handles the rest.

> [!TIP]
> If you're new to apps in Flyte, start with [Introducing apps](../core-concepts/introducing-apps) for an overview, then see [Build apps](../build-apps/_index) to learn how to build custom app environments from scratch.

## When to use a native integration

Use a native integration when your app fits one of the supported frameworks and you want:

- **A minimal, opinionated setup** — sensible defaults for the framework, no boilerplate
- **First-class support** — features like model streaming, OpenAI-compatible APIs, and passthrough auth wired in for you
- **Faster time-to-deploy** — focus on your app logic, not on packaging and serving plumbing

For app types not covered here, build a custom [`AppEnvironment`](../build-apps/_index) using the patterns in the [Build apps](../build-apps/_index) section.

## Available integrations

| Integration | Framework | Typical use case |
|---|---|---|
| [Streamlit app](./streamlit-app) | [Streamlit](https://streamlit.io/) | Interactive dashboards and data apps |
| [FastAPI app](./fastapi-app) | [FastAPI](https://fastapi.tiangolo.com/) | REST APIs, webhooks, and backend services |
| [vLLM app](./vllm-app) | [vLLM](https://docs.vllm.ai/) | High-throughput LLM inference with an OpenAI-compatible API |
| [SGLang app](./sglang-app) | [SGLang](https://docs.sglang.io/) | Structured generation and LLM serving with an OpenAI-compatible API |
| [Flyte webhook](./flyte-webhook) | [FastAPI](https://fastapi.tiangolo.com/) | Pre-built HTTP endpoints for common Flyte control-plane operations |

## Next steps

- [**Streamlit app**](./streamlit-app): Build interactive Streamlit dashboards
- [**FastAPI app**](./fastapi-app): Create REST APIs and backend services
- [**vLLM app**](./vllm-app): Serve large language models with vLLM
- [**SGLang app**](./sglang-app): Serve LLMs with SGLang for structured generation
- [**Flyte webhook**](./flyte-webhook): Pre-built webhook for common Flyte operations
