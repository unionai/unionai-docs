# Serving a model

In this section we use a Union app to serve a model created with a Union workflow.

## Example app

In this example we first use a Union workflow to train a model and output it as a Union `Artifact`.
We then use a Union app to serve the model using `FastAPI`.

In a local directory, create the following files:

```{code-block}bash
.
├── app.py
├── main.py
└── wf.py
```

## App declaration

```{code-block} python
:caption: app.py

"""A Union app that uses FastAPI to serve model created by a Union workflow."""

from union import Artifact, Resources
from union.app import App, Input

SklearnModel = Artifact(name="sklearn-model")

fast_api_app = App(
    name="simple-fastapi-sklearn",
    inputs=[
        Input(
            name="sklearn_model",
            value=SklearnModel.query(),
            auto_download=True,
        )
    ],
    container_image="ghcr.io/thomasjpfan/union-serve-sklearn-fastapi:0.1.2",
    limits=Resources(cpu="2", mem="4Gi"),
    port=8082,
    include=["./main.py"],
    command=["fastapi", "dev", "--port", "8082"],
)
```

## main.py

```{code-block} python
:caption: main.py

"""Set up the FastAPI app."""

from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI
from union_runtime import get_input

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    model_file = get_input("sklearn_model")
    ml_models["model"] = joblib.load(model_file)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float, y: float) -> float:
    result = ml_models["model"]([[x, y]])
    return {"result": result}
```

## wf.py

Import the required packages:

```{code-block} python
:caption: wf.py

"""A Union workflow that trains a model and evaluates it."""

from pathlib import Path
from typing import Annotated

import joblib
import numpy as np
from flytekit import Artifact, FlyteFile, ImageSpec, Resources, current_context, task, workflow
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
```

Create the [`Artifact`](../artifacts/index.md):

```{code-block} python
SklearnModel = Artifact(name="sklearn-model")
```

Define the container image that will be used to run the tasks using [`ImageSpec`](../tasks/task-software-environment/imagespec.md).
Note that you must replace `YOUR_REGISTRY` with the actual URI of your own container registry.

```{code-block} python
image_spec = ImageSpec(
    name="flytekit",
    packages=["scikit-learn==1.5.2"],
    registry="YOUR_REGISTRY",
)
```

Define the tasks and workflow:

```{code-block} python
@task(
    cache=True,
    cache_version="2",
    container_image=image_spec,
)
def load_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate the example using sklearn.datasets.make_regression and split it into training and testing sets."""
    X, y = make_regression(n_samples=3)
    return train_test_split(X, y, random_state=42)


@task(
    limits=Resources(cpu="2", mem="4Gi"),
    cache=True,
    cache_version="2",
    container_image=image_spec,
)

def train_model(X_train: np.ndarray, y_train: np.ndarray) -> Annotated[FlyteFile, SklearnModel]:
    """Train a RandomForestRegressor model and save it as a file."""
    working_dir = Path(current_context().working_directory)
    model_file = working_dir / "model.joblib"

    rf = RandomForestRegressor().fit(X_train, y_train)
    joblib.dump(rf, model_file)
    return model_file


@task(
    container_image=image_spec,
    limits=Resources(cpu="2", mem="2Gi"),
    cache=True,
    cache_version="2",
)
def evaluate_model(model: FlyteFile, X_test: np.ndarray, y_test: np.ndarray) -> float:
    """Evaluate the model using mean absolute percentage error."""
    model_ = joblib.load(model.download())
    y_pred = model_.predict(X_test)
    return float(mean_absolute_percentage_error(y_test, y_pred))


@workflow
def wf() -> float:
    """Train a model and evaluate it."""
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train=X_train, y_train=y_train)
    return evaluate_model(model=model, X_test=X_test, y_test=y_test)
```

## Run the example

To run this example you will need to register and run the workflow first:

```{code-block} bash
:caption: Run the workflow
$ union run --remote wf.py wf
```

The workflow first uses `sklearn.datasets.make_regression` to generate a random regression problem.
It then trains a model against that problem, evaluates the model and saves it as a file.
The file is defined as a Union `Artifact`, enabling it to be retrieved later by the serving app for display.

Once the workflow has completed, you can deploy the app:

```{code-block} bash
$ union deploy apps app.py simple-fastapi-sklearn
```
