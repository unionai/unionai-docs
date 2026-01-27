---
title: Build apps
weight: 12
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Build apps

This section covers how to build different types of apps with Flyte, including Streamlit dashboards, FastAPI REST APIs, vLLM and SGLang model servers, webhooks, and WebSocket applications.

> [!TIP]
> Go to [Introducing apps](../flyte-basics/introducing-apps) for an overview of apps and a quick example.

## App types

Flyte supports various types of apps:

- **UI dashboard apps**: Interactive web dashboards and data visualization tools like Streamlit and Gradio
- **Web API apps**: REST APIs, webhooks, and backend services like FastAPI and Flask
- **Model serving apps**: High-performance LLM serving with vLLM and SGLang

## Next steps

- [**Single-script apps**](./single-script-apps): The simplest way to build and deploy apps in a single Python script
- [**Multi-script apps**](./multi-script-apps): Build FastAPI and Streamlit apps with multiple files
- [**App usage patterns**](./app-usage-patterns): Call apps from tasks, tasks from apps, and apps from apps
- [**Secret-based authentication**](./secret-based-authentication): Authenticate FastAPI apps using Flyte secrets
- [**Streamlit app**](./streamlit-app): Build interactive Streamlit dashboards
- [**FastAPI app**](./fastapi-app): Create REST APIs and backend services
- [**vLLM app**](./vllm-app): Serve large language models with vLLM
- [**SGLang app**](./sglang-app): Serve LLMs with SGLang for structured generation