---
title: First project
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# First project

In this section, you'll build an end-to-end machine learning project: a training pipeline that produces a model, and an app that serves it via an API.

This project demonstrates how Flyte's tasks and apps work together in a real-world scenario.

## What you'll build

```
┌─────────────────────┐         ┌─────────────────────┐
│   Training Tasks    │         │    Serving App      │
│                     │         │                     │
│  prepare_data()     │         │   FastAPI endpoint  │
│       ↓             │  model  │        ↓            │
│  fine_tune()  ──────┼────────→│   /generate         │
│       ↓             │  file   │                     │
│  training_pipeline()│         │                     │
└─────────────────────┘         └─────────────────────┘
```

**Training pipeline**: A set of tasks that prepare data, fine-tune a model, and save it as a file artifact.

**Serving app**: A FastAPI application that loads the trained model and exposes an inference endpoint.

The key insight is how these connect: the app references the training output using `RunOutput`, so it automatically loads the model from a completed training run.

## Prerequisites

Before starting, make sure you've completed:

- [Quickstart](../quickstart) - Your first workflow
- [Local setup](../local-setup) - Development environment configured
- [Flyte basics](../flyte-basics) - TaskEnvironment, tasks, runs, actions, and apps

## Project structure

This section is organized as a tutorial:

1. [**Training pipeline**](./training-pipeline) - Build the model training workflow
2. [**Serving the model**](./serving-the-model) - Create the FastAPI serving app
3. [**Connecting training to serving**](./connecting-training-to-serving) - Wire them together with RunOutput

Each part builds on the previous one. By the end, you'll have a working ML system with training and inference.
