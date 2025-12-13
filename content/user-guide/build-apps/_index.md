---
title: Build apps
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Build apps

This section covers how to build different types of apps with Flyte, including Streamlit dashboards, FastAPI REST APIs, vLLM and SGLang model servers, webhooks, and WebSocket applications.

## App types

Flyte supports various types of apps:

- **Streamlit apps**: Interactive web dashboards and data visualization tools
- **FastAPI apps**: REST APIs, webhooks, and backend services
- **vLLM apps**: High-performance LLM serving with vLLM
- **SGLang apps**: Fast structured generation for LLMs with SGLang

## Topics

- [**Single-script apps**](./single-script-apps): The simplest way to build and deploy apps in a single Python script
- [**Streamlit app**](./streamlit-app): Build interactive Streamlit dashboards
- [**FastAPI app**](./fastapi-app): Create REST APIs and backend services
- [**vLLM app**](./vllm-app): Serve large language models with vLLM
- [**SGLang app**](./sglang-app): Serve LLMs with SGLang for structured generation
- [**App calling patterns**](./app-calling-patterns): Call apps from tasks, tasks from apps, and apps from apps
- [**Passing inputs into apps**](./passing-inputs): Use delayed inputs like RunOutput and AppEndpoint
- [**Multi-script apps**](./multi-script-apps): Build FastAPI and Streamlit apps with multiple files

## Quick start: Simple FastAPI app

Here's a minimal FastAPI app example:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/basic_fastapi.py" lang=python >}}

This creates a simple FastAPI app with a single endpoint. Once deployed, you can access it at the generated URL and see the interactive API documentation at `/docs`.

## Next steps

Choose the type of app you want to build:

- [**Streamlit apps**](./streamlit-app) - For dashboards and interactive UIs
- [**FastAPI apps**](./fastapi-app) - For REST APIs and backend services
- [**vLLM apps**](./vllm-app) - For serving LLMs with vLLM
- [**SGLang apps**](./sglang-app) - For serving LLMs with SGLang

