---
title: Introducing apps
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Introducing apps

Before we build our serving component, let's understand what apps are and how they differ from tasks.

## Tasks vs apps

You've already learned about **tasks**: Python functions that run to completion in containers. Tasks are great for data processing, training, and batch operations.

**Apps** are different. An app is a long-running service that stays active and handles requests over time. Apps are ideal for:

- REST APIs and webhooks
- Model inference endpoints
- Interactive dashboards
- Real-time data services

| Aspect | Task | App |
|--------|------|-----|
| Lifecycle | Runs once, then exits | Stays running indefinitely |
| Invocation | Called with inputs, returns outputs | Receives HTTP requests |
| Use case | Batch processing, training | APIs, inference, dashboards |
| Durability | Inputs/outputs stored, can resume | Stateless request handling |

## AppEnvironment

Just as tasks use `TaskEnvironment`, apps use `AppEnvironment` to configure their runtime.

An `AppEnvironment` specifies:

- **Hardware**: CPU, memory, GPU allocation
- **Software**: Container image with dependencies
- **App-specific settings**: Ports, scaling, authentication

Here's a simple example:

```python
import flyte
from flyte.app.extras import FastAPIAppEnvironment

env = FastAPIAppEnvironment(
    name="my-app",
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn"),
    limits=flyte.Resources(cpu="1", mem="2Gi"),
)
```

## A hello world app

Let's create a minimal FastAPI app to see how this works.

First, create `hello_app.py`:

{{< code file="/external/unionai-examples/v2/user-guide/getting-started/serving/hello_app.py" lang="python" >}}

### Understanding the code

- **`FastAPI()`** creates the web application with its endpoints
- **`FastAPIAppEnvironment`** configures the container and resources
- **`@app.get("/")`** defines an HTTP endpoint that returns a greeting
- **`flyte.serve()`** deploys and starts the app on your Flyte backend

### Serving the app

With your config file in place, serve the app:

```shell
flyte serve hello_app.py env
```

Or run the Python file directly (which calls `flyte.serve()` in the main block):

```shell
python hello_app.py
```

You'll see output like:

```shell
https://my-instance.flyte.com/v2/domain/development/project/my-project/apps/hello-app
App 'hello-app' is now serving.
```

Click the link to view your app in the UI. You can find the app URL there, or visit `/docs` for FastAPI's interactive API documentation.

## When to use apps vs tasks

Use **tasks** when:
- Processing takes seconds to hours
- You need durability (inputs/outputs tracked)
- Work is triggered by events or schedules
- Results need to be cached or resumed

Use **apps** when:
- Responses must be fast (milliseconds)
- You're serving an API or dashboard
- Users interact in real-time
- You need a persistent endpoint

In our project, we'll use:
- **Tasks** for training (batch processing, needs durability)
- **App** for serving (fast inference, HTTP endpoint)

## Next steps

Now that you understand apps, let's build the [training pipeline](./training-pipeline) that will produce the model our app will serve.
