---
title: Serving the model
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Serving the model

Now let's create the FastAPI app that will serve our trained model. This app loads the model at startup and exposes an inference endpoint.

## Define request and response models

First, define the data structures for API requests and responses:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-models" >}}

These Pydantic models give us automatic validation and documentation.

## Create the FastAPI application

Set up the FastAPI app with an inference endpoint:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-app" >}}

The endpoint:
- Receives a prompt and generation parameters
- Uses the model stored in `app.state`
- Returns generated text

## Configure the app environment

This is where the magic happens. We configure the app to load the model from our training pipeline:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-env" >}}

The `parameters` list specifies what the app needs at startup. The `RunOutput` tells Flyte to fetch the model from a training run.

**Parameter options:**
- `name`: Identifier for the parameter
- `value`: A `RunOutput` referencing the task that produced the model
- `download`: When `True`, downloads the file to the container
- `env_var`: Environment variable where the file path is stored

## Load the model at startup

The `@env.server` decorator defines initialization logic that runs once when the app starts:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-server" >}}

This loads the model into memory once, not on every request. The model is stored in `app.state` so all request handlers can access it.

## Deploy the app

Add a main block to serve the app:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-main" >}}

## Run the serving app

After your training pipeline has completed, deploy the serving app:

```bash
uv run serve.py
```

The app will:
1. Find the most recent `training_pipeline` run
2. Download the model file from that run
3. Load the model into memory
4. Start serving requests

## Test the API

Once the app is running, test it with curl:

```bash
curl -X POST "https://<app-url>/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Once upon a time", "max_length": 100}'
```

Or visit `https://<app-url>/docs` for FastAPI's interactive Swagger UI.

## Next steps

The app is now serving our trained model. In the final section, we'll dive deeper into [connecting training to serving](./connecting-training-to-serving) with `RunOutput`.
