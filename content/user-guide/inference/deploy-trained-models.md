---
title: Deploy trained models
description: Serve a model trained in a Flyte task behind an endpoint, with vLLM, SGLang, or your own FastAPI app.
icon: rocket-takeoff
weight: 7
variants: +flyte +union
---

# Deploy trained models

A model trained in a task can go straight to an endpoint. The task saves the weights to object storage, and an app mounts them when it starts, so you never copy weights by hand or bake them into an image.

{{< variant union >}}
{{< markdown >}}

## Publish the model as an artifact

Return the weights from the training task and wrap them with `flyte.artifacts.new()`. Every run registers a new version of the artifact:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/train_artifact.py" fragment="finetune" lang="python" >}}

{{< markdown >}}

The task must set `produces_artifacts=True`. Without it, no artifact is registered and the app has nothing to resolve. See [Task outputs as artifacts](../artifacts/task-outputs).

## Serve an LLM with vLLM

Pass the artifact to `VLLMAppEnvironment` as `model_path`. `SGLangAppEnvironment` takes the same argument:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/serve_artifact_vllm.py" fragment="app" lang="python" >}}

{{< markdown >}}

The directory must be in a format the engine can load, such as the output of `save_pretrained()`. A PEFT adapter saved on its own is not enough, so merge it into the base model first.

Call the deployed app with any OpenAI client. See [Using the OpenAI-compatible API](./vllm-app#using-the-openai-compatible-api).

## Serve any other model with FastAPI

For a model vLLM and SGLang don't serve, such as a classifier, publish it the same way:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/train_artifact.py" fragment="train-classifier" lang="python" >}}

{{< markdown >}}

Then mount the artifact into a `FastAPIAppEnvironment` with a parameter:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/serve_artifact_fastapi.py" fragment="app" lang="python" >}}

{{< markdown >}}

`mount` is always a directory. A `flyte.io.File` artifact is downloaded into it, and a `flyte.io.Dir` artifact appears at it. An artifact used as an app parameter must store one of those two types. See [Use artifacts in apps](../artifacts/artifacts-in-apps).

## Pin and roll back a version

An app resolves the latest artifact version when you deploy it and keeps that version until you deploy again. A version published later doesn't change a running app.

To roll back, deploy with an explicit version:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/serve_artifact_vllm.py" fragment="pin" lang="python" >}}

{{< markdown >}}

List the versions with `flyte get artifact support-llm`. The artifact's [lineage view](../artifacts/lineage) shows which app deployment serves each version and which run produced it.

## Automate training through deployment

To retrain, check, and deploy in one step, with an accuracy gate or a person's approval before release, use a factory. See [End in an app](../factories/serve).

{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

## Return the model from a task

Save the weights in the training task and return them as a `flyte.io.Dir`:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/train_output.py" fragment="finetune" lang="python" >}}

{{< markdown >}}

## Serve an LLM with vLLM

Pass the task's output to `VLLMAppEnvironment` as `model_path` with `flyte.app.RunOutput`. `SGLangAppEnvironment` takes the same argument:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/serve_output_vllm.py" fragment="app" lang="python" >}}

{{< markdown >}}

`task_name` is `<environment name>.<task name>`, and the app uses the latest successful run of that task when you deploy it. To serve the output of one specific run, pass `run_name` instead.

The directory must be in a format the engine can load, such as the output of `save_pretrained()`. A PEFT adapter saved on its own is not enough, so merge it into the base model first.

Call the deployed app with any OpenAI client. See [Using the OpenAI-compatible API](./vllm-app#using-the-openai-compatible-api).

## Serve any other model with FastAPI

For a model vLLM and SGLang don't serve, such as a classifier, return it the same way:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/train_output.py" fragment="train-classifier" lang="python" >}}

{{< markdown >}}

Then mount the task's output into a `FastAPIAppEnvironment` with a parameter:

{{< /markdown >}}

{{< code file="/unionai-examples/v2/user-guide/inference/deploy-trained-models/serve_output_fastapi.py" fragment="app" lang="python" >}}

{{< markdown >}}

`mount` is always a directory. A `flyte.io.File` output is downloaded into it, and a `flyte.io.Dir` output appears at it. See [Passing parameters into app environments](../apps/configure-apps/passing-parameters).

{{< /markdown >}}
{{< /variant >}}

## Choose an app type

| Model | App | Details |
|---|---|---|
| LLM, high throughput | `VLLMAppEnvironment` | [vLLM app](./vllm-app) |
| LLM, structured generation | `SGLangAppEnvironment` | [SGLang app](./sglang-app) |
| Anything else | `FastAPIAppEnvironment` | [FastAPI app](../apps/native-app-integrations/fastapi-app) |
