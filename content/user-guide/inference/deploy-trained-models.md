---
title: Deploy trained models
description: Serve a model trained in a Flyte task behind an endpoint, with vLLM, SGLang, or your own FastAPI app.
icon: rocket-takeoff
weight: 6
variants: +flyte +union
---

# Deploy trained models

A model trained in a task can go straight to an endpoint. The task saves the weights to object storage, and an app mounts them when it starts, so you never copy weights by hand or bake them into an image.

{{< variant union >}}
{{< markdown >}}

## Publish the model as an artifact

Return the weights from the training task and wrap them with `flyte.artifacts.new()`. Every run registers a new version of the artifact:

```python
import flyte
from flyte import artifacts
from flyte.io import Dir

env = flyte.TaskEnvironment(
    name="training",
    image=flyte.Image.from_debian_base().with_pip_packages("torch", "transformers", "accelerate"),
    resources=flyte.Resources(cpu="4", memory="32Gi", gpu="L40s:1", disk="100Gi"),
)


@env.task(produces_artifacts=True)
async def finetune(base_model: str) -> Dir:
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(base_model)

    ...  # your training loop

    model.save_pretrained("model")
    tokenizer.save_pretrained("model")

    weights = await Dir.from_local("model")
    return artifacts.new(
        weights,
        artifacts.Metadata.create_model_metadata(
            name="support-llm",
            framework="PyTorch",
            task="text-generation",
            serial_format="safetensors",
        ),
    )
```

The task must set `produces_artifacts=True`. Without it, no artifact is registered and the app has nothing to resolve. See [Task outputs as artifacts](../artifacts/task-outputs).

## Serve an LLM with vLLM

Pass the artifact to `VLLMAppEnvironment` as `model_path`. `SGLangAppEnvironment` takes the same argument:

```python
import flyte
import flyte.app
from flyteplugins.vllm import VLLMAppEnvironment

app_env = VLLMAppEnvironment(
    name="support-llm",
    model_path=flyte.app.ArtifactValue(name="support-llm", type="directory"),
    model_id="support-llm",
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1", disk="50Gi"),
    scaling=flyte.app.Scaling(replicas=(0, 1), scaledown_after=600),
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.deploy(app_env)
```

The directory must be in a format the engine can load, such as the output of `save_pretrained()`. A PEFT adapter saved on its own is not enough, so merge it into the base model first.

Call the deployed app with any OpenAI client. See [Using the OpenAI-compatible API](./vllm-app#using-the-openai-compatible-api).

## Serve any other model with FastAPI

For a model vLLM and SGLang don't serve, such as a classifier, mount the artifact into a `FastAPIAppEnvironment` with a parameter. Here the artifact is a directory that holds `model.joblib`:

```python
from contextlib import asynccontextmanager

import flyte
import flyte.app
import joblib
from fastapi import FastAPI
from flyte.app import Parameter
from flyte.app.extras import FastAPIAppEnvironment

MODEL_DIR = "/tmp/model"
state = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    state["model"] = joblib.load(f"{MODEL_DIR}/model.joblib")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
async def predict(features: list[float]) -> dict:
    return {"prediction": state["model"].predict([features]).tolist()[0]}


app_env = FastAPIAppEnvironment(
    name="churn-classifier",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn", "joblib", "scikit-learn"),
    resources=flyte.Resources(cpu="2", memory="4Gi"),
    parameters=[
        Parameter(
            name="model",
            value=flyte.app.ArtifactValue(name="churn-classifier", type="directory"),
            mount=MODEL_DIR,
        ),
    ],
)
```

`mount` is always a directory. A `flyte.io.File` artifact is downloaded into it, and a `flyte.io.Dir` artifact appears at it. Only those two types can be app parameters. See [Use artifacts in apps](../artifacts/artifacts-in-apps).

## Pin and roll back a version

An app resolves the latest artifact version when you deploy it and keeps that version until you deploy again. A version published later doesn't change a running app.

To roll back, deploy with an explicit version:

```python
flyte.app.ArtifactValue(name="support-llm", type="directory", version="<artifact-version>")
```

List the versions with `flyte get artifact support-llm`. The artifact's [lineage view](../artifacts/lineage) shows which app deployment serves each version and which run produced it.

## Automate training through deployment

To retrain, check, and deploy in one step, with an accuracy gate or a person's approval before release, use a factory. See [End in an app](../factories/serve).

{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

## Return the model from a task

Save the weights in the training task and return them as a `flyte.io.Dir`:

```python
import flyte
from flyte.io import Dir

env = flyte.TaskEnvironment(
    name="training",
    image=flyte.Image.from_debian_base().with_pip_packages("torch", "transformers", "accelerate"),
    resources=flyte.Resources(cpu="4", memory="32Gi", gpu="L40s:1", disk="100Gi"),
)


@env.task
async def finetune(base_model: str) -> Dir:
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(base_model)

    ...  # your training loop

    model.save_pretrained("model")
    tokenizer.save_pretrained("model")
    return await Dir.from_local("model")
```

## Serve an LLM with vLLM

Pass the task's output to `VLLMAppEnvironment` as `model_path` with `flyte.app.RunOutput`. `SGLangAppEnvironment` takes the same argument:

```python
import flyte
import flyte.app
from flyteplugins.vllm import VLLMAppEnvironment

app_env = VLLMAppEnvironment(
    name="support-llm",
    model_path=flyte.app.RunOutput(type="directory", task_name="training.finetune"),
    model_id="support-llm",
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1", disk="50Gi"),
    scaling=flyte.app.Scaling(replicas=(0, 1), scaledown_after=600),
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.deploy(app_env)
```

`task_name` is `<environment name>.<task name>`, and the app uses the latest run of that task when you deploy it. To serve the output of one specific run, pass `run_name` instead.

The directory must be in a format the engine can load, such as the output of `save_pretrained()`. A PEFT adapter saved on its own is not enough, so merge it into the base model first.

Call the deployed app with any OpenAI client. See [Using the OpenAI-compatible API](./vllm-app#using-the-openai-compatible-api).

## Serve any other model with FastAPI

For a model vLLM and SGLang don't serve, such as a classifier, mount the task's output into a `FastAPIAppEnvironment` with a parameter. Here the task returns a directory that holds `model.joblib`:

```python
from contextlib import asynccontextmanager

import flyte
import flyte.app
import joblib
from fastapi import FastAPI
from flyte.app import Parameter
from flyte.app.extras import FastAPIAppEnvironment

MODEL_DIR = "/tmp/model"
state = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    state["model"] = joblib.load(f"{MODEL_DIR}/model.joblib")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
async def predict(features: list[float]) -> dict:
    return {"prediction": state["model"].predict([features]).tolist()[0]}


app_env = FastAPIAppEnvironment(
    name="churn-classifier",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn", "joblib", "scikit-learn"),
    resources=flyte.Resources(cpu="2", memory="4Gi"),
    parameters=[
        Parameter(
            name="model",
            value=flyte.app.RunOutput(type="directory", task_name="training.train_classifier"),
            mount=MODEL_DIR,
        ),
    ],
)
```

`mount` is always a directory. A `flyte.io.File` output is downloaded into it, and a `flyte.io.Dir` output appears at it. See [Passing parameters into app environments](../apps/configure-apps/passing-parameters).

{{< /markdown >}}
{{< /variant >}}

## Choose an app type

| Model | App | Details |
|---|---|---|
| LLM, high throughput | `VLLMAppEnvironment` | [vLLM app](./vllm-app) |
| LLM, structured generation | `SGLangAppEnvironment` | [SGLang app](./sglang-app) |
| Anything else | `FastAPIAppEnvironment` | [FastAPI app](../apps/native-app-integrations/fastapi-app) |
