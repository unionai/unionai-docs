---
title: Flyte plugins
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Flyte plugins

Flyte is designed to be extensible, allowing you to integrate new tools and frameworks into your workflows. By installing and configuring plugins, you can tailor Flyte to your data and compute ecosystem — whether you need to run large-scale distributed training, process data with a specific engine, or interact with external APIs.

Common reasons to extend Flyte include:
- **Specialized compute:** Use plugins like Spark or Ray to create distributed compute clusters.
- **AI integration:** Connect Flyte with frameworks like OpenAI to run LLM agentic applications.
- **Custom infrastructure:** Add plugins to interface with your organization’s storage, databases, or proprietary systems.

For example, you can install the PyTorch plugin to run distributed PyTorch jobs natively on a Kubernetes cluster.

| Plugin | Description |
| ------ | ----------- |
| [Ray](./ray) | Run Ray jobs on your Flyte cluster |
| [Spark](./spark) | Run Spark jobs on your Flyte cluster |
| [OpenAI](./openai) | Integrate with OpenAI SDKs in your Flyte workflows |
| [Dask](./dask) | Run Dask jobs on your Flyte cluster |