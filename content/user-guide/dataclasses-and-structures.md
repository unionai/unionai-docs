---
title: Dataclasses and structures
weight: 90
variants: +flyte +serverless +byoc +selfmanaged
---

# Dataclasses and structures

Dataclasses and Pydantic models are fully supported in Flyte.
Use these as you would normally, passing them as inputs and outputs of tasks.
The only thing to keep in mind is that data between tasks is serialized, stored, and deserialized. That means that the fields in your dataclass should also be serializable.

## Basic Usage

Dataclasses can be inputs to tasks as in the following.

```python
import asyncio
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="ex-dataclasses")


@dataclass
class InferenceRequest:
    feature_a: float
    feature_b: float


@env.task
async def predict_one(request: InferenceRequest) -> float:
    """
    A dummy linear model: prediction = 2 * feature_a + 3 * feature_b + bias(=1.0)
    """
    return 2.0 * request.feature_a + 3.0 * request.feature_b + 1.0

```

### Running

When invoking keep in mind you can just call the task directly. This keeps Flyte out of the way and just invokes the raw function.

```python
result_one = asyncio.run(predict_one(InferenceRequest(feature_a=1.0, feature_b=2.0)))
print(f"Prediction for single request: {result_one}")
```

Or run locally through Flyte.

```python
run = flyte.run(predict_one, InferenceRequest(feature_a=1.0, feature_b=2.0))
print(run.url)
```

Keep in mind if you're running from the command line, you can pass in the dataclass using JSON.

```bash
flyte --org testorg --endpoint dns:///<endpoint> run -p testproject -d development dataclass_example.py predict_one \
  --request '{"feature_a": 1, "feature_b": 2}'
```

Dataclasses can also be nested within others, as in a list.
Also, Flyte's offloaded types can also be included as fields.
Because Flyte comes with a serialization/deserialization mechanism for these types, there's no need to add any transformers to the type engine.

This example below runs a set of predictions, writes out to a file, and invokes a subsequent task to read from the file.

```python
@dataclass
class BatchRequest:
    requests: List[InferenceRequest]


class BatchPredictionResults(BaseModel):
    predictions: List[float]
    results_file: File

    class Config:
        arbitrary_types_allowed = True


@env.task
async def predict_batch(batch: BatchRequest) -> BatchPredictionResults:
    """
    Runs the same dummy linear model on each element in the batch.
    """
    tasks = [predict_one(request=req) for req in batch.requests]
    results = await asyncio.gather(*tasks)

    # 2) Write predictions to a local CSV
    import csv

    output_path = "predictions.csv"
    with open(output_path, mode="w", newline="") as f:  # noqa: ASYNC230
        writer = csv.writer(f)
        writer.writerow(["prediction"])
        for p in results:
            writer.writerow([p])

    csv_file = await File.from_local(output_path)

    return BatchPredictionResults(predictions=results, results_file=csv_file)


@env.task
async def avg_from_file(results: BatchPredictionResults) -> float:
    """
    Reads the CSV in results.results_file, computes the average of the 'prediction' column.
    """
    total = 0.0
    count = 0
    async with results.results_file.open() as f:
        iter_f = iter(f)
        next(iter_f)  # Skip header
        for row in iter_f:
            total += float(row)
            count += 1

    return total / count if count else 0.0


@env.task
async def dc_wf(batch: BatchRequest):
    """
    Runs the batch prediction and computes the average of the predictions.
    """
    results = await predict_batch(batch=batch)
    avg = await avg_from_file(results=results)

    print(f"Average prediction: {avg}")


if __name__ == "__main__":
    flyte.init(
        endpoint="localhost:8090",
        insecure=True,
        project="testproject",
        domain="development",
        org="testorg",
    )

    batch_req = BatchRequest(
        requests=[
            InferenceRequest(feature_a=1.0, feature_b=2.0),
            InferenceRequest(feature_a=3.0, feature_b=4.0),
            InferenceRequest(feature_a=5.0, feature_b=6.0),
        ]
    )

    run = flyte.run(dc_wf, batch_req)
    print(f"Run URL: {run.url}")
```


