---
title: FastAPI app
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# FastAPI app

FastAPI is a modern, fast web framework for building APIs. Flyte provides `FastAPIAppEnvironment` which makes it easy to deploy FastAPI applications.

## Basic FastAPI app

Here's a simple FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/basic_fastapi.py" lang=python >}}

Once deployed, you can:
- Access the API at the generated URL
- View interactive API docs at `/docs` (Swagger UI)
- View alternative docs at `/redoc`

## Serving a machine learning model

Here's an example of serving a scikit-learn model:

```python
import os
from contextlib import asynccontextmanager

import joblib
import flyte
from fastapi import FastAPI
from flyte.app.extras import FastAPIAppEnvironment
from pydantic import BaseModel


app = FastAPI(title="ML Model API")

# Define request/response models
class PredictionRequest(BaseModel):
    feature1: float
    feature2: float
    feature3: float

class PredictionResponse(BaseModel):
    prediction: float
    probability: float

# Load model (you would typically load this from storage)
model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    model_path = os.getenv("MODEL_PATH", "/app/models/model.joblib")
    # In production, load from your storage
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    yield

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Make prediction
    # prediction = model.predict([[request.feature1, request.feature2, request.feature3]])
    
    # Dummy prediction for demo
    prediction = 0.85
    probability = 0.92
    
    return PredictionResponse(
        prediction=prediction,
        probability=probability,
    )

env = FastAPIAppEnvironment(
    name="ml-model-api",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi",
        "uvicorn",
        "scikit-learn",
        "pydantic",
        "joblib",
    ),
    parameters=[
        flyte.app.Parameter(
            name="model_file",
            value=flyte.io.File("s3://bucket/models/model.joblib"),
            mount="/app/models",
            env_var="MODEL_PATH",
        ),
    ]
    resources=flyte.Resources(cpu=2, memory="2Gi"),
    requires_auth=False,
)

if __name__ == "__main__":
    flyte.init_from_config()
    app_deployment = flyte.deploy(env)
    print(f"API URL: {app_deployment[0].url}")
    print(f"Swagger docs: {app_deployment[0].url}/docs")
```


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

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import flyte
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI(title="Product API")

# Data models
class Product(BaseModel):
    id: int
    name: str
    price: float

class ProductCreate(BaseModel):
    name: str
    price: float

# In-memory database (use real database in production)
products_db = []

@app.get("/products", response_model=List[Product])
async def get_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=Product)
async def create_product(product: ProductCreate):
    new_product = {
        "id": len(products_db) + 1,
        "name": product.name,
        "price": product.price,
    }
    products_db.append(new_product)
    return new_product

env = FastAPIAppEnvironment(
    name="product-api",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi",
        "uvicorn",
    ),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

if __name__ == "__main__":
    flyte.init_from_config()
    app_deployment = flyte.deploy(env)
    print(f"API URL: {app_deployment[0].url}")
    print(f"Swagger docs: {app_deployment[0].url}/docs")
```

## Multi-file FastAPI app

Here's an example of a multi-file FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/app.py" lang=python >}}

The helper module:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/module.py" lang=python >}}

See [Multi-script apps](./multi-script-apps) for more details on building FastAPI apps with multiple files.

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

