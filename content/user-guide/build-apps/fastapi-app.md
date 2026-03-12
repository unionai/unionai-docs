---
title: FastAPI app
weight: 9
variants: +flyte +byoc +selfmanaged
---

# FastAPI app

FastAPI is a modern, fast web framework for building APIs. Flyte provides `FastAPIAppEnvironment` which makes it easy to deploy FastAPI applications.

## Basic FastAPI app

Here's a simple FastAPI app:

{{< code file="/unionai-examples/v2/user-guide/build-apps/fastapi/basic_fastapi.py" lang=python >}}

Once deployed, you can:
- Access the API at the generated URL
- View interactive API docs at `/docs` (Swagger UI)
- View alternative docs at `/redoc`

## Serving a machine learning model

Here's an example of serving a scikit-learn model:

{{< code file="/unionai-examples/v2/user-guide/build-apps/fastapi/ml_model_serving.py" fragment=ml-model lang=python >}}


## Accessing Swagger documentation

FastAPI automatically generates interactive API documentation. Once deployed:

- **Swagger UI**: Access at `{app_url}/docs`
- **ReDoc**: Access at `{app_url}/redoc`
- **OpenAPI JSON**: Access at `{app_url}/openapi.json`

The Swagger UI provides an interactive interface where you can:
- See all available endpoints
- Test API calls directly from the browser
- View request/response schemas
- See example payloads

## Example: REST API with multiple endpoints

{{< code file="/unionai-examples/v2/user-guide/build-apps/fastapi/rest_api.py" fragment=rest-api lang=python >}}

## Multi-file FastAPI app

Here's an example of a multi-file FastAPI app:

{{< code file="/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/app.py" lang=python >}}

The helper module:

{{< code file="/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/module.py" lang=python >}}

See [Multi-script apps](./multi-script-apps) for more details on building FastAPI apps with multiple files.

## Local-to-remote model serving

A common ML pattern: train a model with a Flyte pipeline, then serve predictions from it. During local development, the app loads the model from a local file (e.g. `model.pt` saved by your training pipeline). When deployed remotely, Flyte's `Parameter` system automatically resolves the model from the latest training run output.

```python
from contextlib import asynccontextmanager
from pathlib import Path
import os

from fastapi import FastAPI
import flyte
from flyte.app import Parameter, RunOutput
from flyte.app.extras import FastAPIAppEnvironment

MODEL_PATH_ENV = "MODEL_PATH"

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model on startup, either local file or remote run output."""
    model_path = Path(os.environ.get(MODEL_PATH_ENV, "model.pt"))
    model = load_model(model_path)
    app.state.model = model
    yield

app = FastAPI(title="MNIST Predictor", lifespan=lifespan)

serving_env = FastAPIAppEnvironment(
    name="mnist-predictor",
    app=app,
    parameters=[
        # Remote: resolves model from the latest train run and sets MODEL_PATH
        Parameter(
            name="model",
            value=RunOutput(task_name="ml_pipeline.pipeline", type="file", getter=(1,)),
            download=True,
            env_var=MODEL_PATH_ENV,
        ),
    ],
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi", "uvicorn", "torch", "torchvision",
    ),
    resources=flyte.Resources(cpu=1, memory="4Gi"),
)

@app.get("/predict")
async def predict(index: int = 0) -> dict:
    return {"prediction": app.state.model(index)}

if __name__ == "__main__":
    # Local: skip RunOutput resolution, lifespan falls back to local model.pt
    serving_env.parameters = []
    local_app = flyte.with_servecontext(mode="local").serve(serving_env)
    local_app.activate(wait=True)
```

Locally, the app loads `model.pt` from disk:

```bash
python serve_model.py
```

Remotely, Flyte resolves the model from the latest training run:

```bash
flyte deploy serve_model.py serving_env
```

The key idea: `Parameter` with `RunOutput` bridges the gap between local and remote. Locally, the app falls back to a local file. Remotely, Flyte resolves the model artifact from the latest pipeline run automatically.

## Best practices

1. **Use Pydantic models**: Define request/response models for type safety and automatic validation
2. **Handle errors**: Use HTTPException for proper error responses
3. **Async operations**: Use async/await for I/O operations
4. **Environment variables**: Use environment variables for configuration
5. **Logging**: Add proper logging for debugging and monitoring
6. **Health checks**: Always include a `/health` endpoint
7. **API documentation**: FastAPI auto-generates docs, but add descriptions to your endpoints

## Advanced features

FastAPI supports many features that work with Flyte:

- **Dependencies**: Use FastAPI's dependency injection system
- **Background tasks**: Run background tasks with BackgroundTasks
- **WebSockets**: See [WebSocket-based patterns](./app-usage-patterns#websocket-based-patterns) for details
- **Authentication**: Add authentication middleware (see [secret-based authentication](./secret-based-authentication))
- **CORS**: Configure CORS for cross-origin requests
- **Rate limiting**: Add rate limiting middleware

## Troubleshooting

**App not starting:**
- Check that uvicorn can find your app module
- Verify all dependencies are installed in the image
- Check container logs for startup errors

**Import errors:**
- Ensure all imported modules are available
- Use `include` parameter if you have custom modules
- Check that file paths are correct

**API not accessible:**
- Verify `requires_auth` setting
- Check that the app is listening on the correct port (8080)
- Review network/firewall settings

