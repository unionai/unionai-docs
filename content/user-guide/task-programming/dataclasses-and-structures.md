---
title: Dataclasses and structures
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Dataclasses and structures

Dataclasses and Pydantic models are fully supported in Flyte as **materialized data types**:
Structured data where the full content is serialized and passed between tasks.
Use these as you would normally, passing them as inputs and outputs of tasks.

Unlike **offloaded types** like [`DataFrame`s](./dataframes), [`File`s and `Dir`s](./files-and-directories), dataclass and Pydantic model data is fully serialized, stored, and deserialized between tasks.
This makes them ideal for configuration objects, metadata, and smaller structured data where all fields should be serializable.

## Example: Combining Dataclasses and Pydantic Models

This example demonstrates how dataclasses and Pydantic models work together as materialized data types, showing nested structures and batch processing patterns:

```python
import asyncio
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

import flyte

env = flyte.TaskEnvironment(name="ex-mixed-structures")


@dataclass
class InferenceRequest:
    feature_a: float
    feature_b: float


@dataclass
class BatchRequest:
    requests: List[InferenceRequest]
    batch_id: str = "default"


class PredictionSummary(BaseModel):
    predictions: List[float]
    average: float
    count: int
    batch_id: str


@env.task
async def predict_one(request: InferenceRequest) -> float:
    """
    A dummy linear model: prediction = 2 * feature_a + 3 * feature_b + bias(=1.0)
    """
    return 2.0 * request.feature_a + 3.0 * request.feature_b + 1.0


@env.task
async def process_batch(batch: BatchRequest) -> PredictionSummary:
    """
    Processes a batch of inference requests and returns summary statistics.
    """
    # Process all requests concurrently
    tasks = [predict_one(request=req) for req in batch.requests]
    predictions = await asyncio.gather(*tasks)

    # Calculate statistics
    average = sum(predictions) / len(predictions) if predictions else 0.0

    return PredictionSummary(
        predictions=predictions,
        average=average,
        count=len(predictions),
        batch_id=batch.batch_id
    )


@env.task
async def summarize_results(summary: PredictionSummary) -> str:
    """
    Creates a text summary from the prediction results.
    """
    return (
        f"Batch {summary.batch_id}: "
        f"Processed {summary.count} predictions, "
        f"average value: {summary.average:.2f}"
    )


if __name__ == "__main__":
    flyte.init_from_config()

    batch_req = BatchRequest(
        requests=[
            InferenceRequest(feature_a=1.0, feature_b=2.0),
            InferenceRequest(feature_a=3.0, feature_b=4.0),
            InferenceRequest(feature_a=5.0, feature_b=6.0),
        ],
        batch_id="demo_batch_001"
    )

    run = flyte.run(summarize_results, flyte.run(process_batch, batch_req))
    print(f"Run URL: {run.url}")
```

## Running the example

You can run the example with python like this:

```bash
python dataclasses-and-structures.py
```

This will run the `__main__` block, which initializes Flyte and deploys your code to the backend platform configured in your Flyte config file.
Not that in here there are two nested runs: the outer one runs the `summarize_results` task, and the inner one runs the `process_batch` task.
It uses the example `BatchRequest` dataclass defined in the code as input to the `process_batch` task, and then passes the output to the `summarize_results` task.

Alternatively, you can run the example using the `flyte` CLI:

```bash
flyte run dataclass_example.py process_batch --batch '{"requests": [{"feature_a": 1, "feature_b": 2}, {"feature_a": 3, "feature_b": 4}], "batch_id": "test_batch"}'
```

Here, the `--batch` argument is used because it matches the name of the parameter in the `process_batch` task, and its value is passed as a JSON string representing the `BatchRequest` dataclass.

You could then take the output of that run (a `PredictionSummary` Pydantic model) and pass it to the `summarize_results` task like this:

```bash
flyte run dataclass_example.py summarize_results --summary '{"predictions": [8.0, 18.0], "average": 13.0, "count": 2, "batch_id": "test_batch"}'
```
