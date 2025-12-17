---
title: Remote tasks
weight: 110
variants: +flyte +serverless +byoc +selfmanaged
---

# Remote tasks

Remote tasks let you use previously deployed tasks without importing their code or dependencies. This enables teams to share and reuse tasks without managing complex dependency chains or container images.

## Prerequisites

Remote tasks must be deployed before you can use them. See the [task deployment guide](../task-deployment) for details.

## Basic usage

Use `flyte.remote.Task.get()` to reference a deployed task:

```python
import flyte
import flyte.remote

env = flyte.TaskEnvironment(name="my_env")

# Get the latest version of a deployed task
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

# Use it in your task
@env.task
async def my_task(data_path: str) -> flyte.io.DataFrame:
    # Call the reference task like any other task
    result = await data_processor(input_path=data_path)
    return result
```

You can run this directly without deploying it:

```bash
flyte run my_workflow.py my_task --data_path s3://my-bucket/data.parquet
```

## Complete example

This example shows how different teams can collaborate using remote tasks.

### Team A: Spark environment

Team A maintains Spark-based data processing tasks:

```python
# spark_env.py
from dataclasses import dataclass
import flyte

env = flyte.TaskEnvironment(name="spark_env")

@dataclass
class AnalysisResult:
    mean_value: float
    std_dev: float

@env.task
async def analyze_data(data_path: str) -> AnalysisResult:
    # Spark code here (not shown)
    return AnalysisResult(mean_value=42.5, std_dev=3.2)

@env.task
async def compute_score(result: AnalysisResult) -> float:
    # More Spark processing
    return result.mean_value / result.std_dev
```

Deploy the Spark environment:

```bash
flyte deploy spark_env/
```

### Team B: ML environment

Team B maintains PyTorch-based ML tasks:

```python
# ml_env.py
from pydantic import BaseModel
import flyte

env = flyte.TaskEnvironment(name="ml_env")

class PredictionRequest(BaseModel):
    feature_x: float
    feature_y: float

class Prediction(BaseModel):
    score: float
    confidence: float
    model_version: str

@env.task
async def run_inference(request: PredictionRequest) -> Prediction:
    # PyTorch model inference (not shown)
    return Prediction(
        score=request.feature_x * 2.5,
        confidence=0.95,
        model_version="v2.1"
    )
```

Deploy the ML environment:

```bash
flyte deploy ml_env/
```

### Team C: Orchestration

Team C builds a workflow using remote tasks from both teams without needing Spark or PyTorch dependencies:

```python
# orchestration_env.py
import flyte.remote

env = flyte.TaskEnvironment(name="orchestration")

# Reference tasks from other teams
analyze_data = flyte.remote.Task.get(
    "spark_env.analyze_data",
    auto_version="latest"
)

compute_score = flyte.remote.Task.get(
    "spark_env.compute_score",
    auto_version="latest"
)

run_inference = flyte.remote.Task.get(
    "ml_env.run_inference",
    auto_version="latest"
)

@env.task
async def orchestrate_pipeline(data_path: str) -> float:
    # Use Spark tasks without Spark dependencies
    analysis = await analyze_data(data_path=data_path)

    # Access attributes from the result
    # (Flyte creates a fake type that allows attribute access)
    print(f"Analysis: mean={analysis.mean_value}, std={analysis.std_dev}")

    data_score = await compute_score(result=analysis)

    # Use ML task without PyTorch dependencies
    # Pass Pydantic models as dictionaries
    prediction = await run_inference(
        request={
            "feature_x": analysis.mean_value,
            "feature_y": data_score
        }
    )

    # Access Pydantic model attributes
    print(f"Prediction: {prediction.score} (confidence: {prediction.confidence})")

    return prediction.score
```

Run the orchestration task directly (no deployment needed):

**Using Python API**:
```python
if __name__ == "__main__":
    flyte.init_from_config()

    result = flyte.run(
        orchestrate_pipeline,
        data_path="s3://my-bucket/data.parquet"
    )

    print(f"Pipeline result: {result.output}")
    print(f"Execution URL: {result.url}")
```

**Using CLI**:
```bash
flyte run orchestration_env.py orchestrate_pipeline --data_path s3://my-bucket/data.parquet
```

## Why use remote tasks?

Remote tasks solve common collaboration and dependency management challenges:

**Cross-team collaboration**: Team A has deployed a Spark task that analyzes large datasets. Team B needs this analysis for their ML pipeline but doesn't want to learn Spark internals, install Spark dependencies, or build Spark-enabled container images. With remote tasks, Team B simply references Team A's deployed task.

**Platform reusability**: Platform teams can create common, reusable tasks (data validation, feature engineering, model serving) that other teams can use without duplicating code or managing complex dependencies.

**Microservices for data workflows**: Remote tasks work like microservices for long-running tasks or agents, enabling secure sharing while maintaining isolation.

## When to use remote tasks

Use remote tasks when you need to:

- Use functionality from another team without their dependencies
- Share common tasks across your organization
- Build reusable platform components
- Avoid dependency conflicts between different parts of your workflow
- Create modular, maintainable data pipelines

## How remote tasks work

### Security model

Remote tasks run in the **caller's project and domain** using the caller's compute resources, but execute with the **callee's service accounts, IAM roles, and secrets**. This ensures:

- Tasks are secure from misuse
- Resource usage is properly attributed
- Authentication and authorization are maintained
- Collaboration remains safe and controlled

### Type system

Remote tasks use Flyte's default types as inputs and outputs. Flyte's type system seamlessly translates data between tasks without requiring the original dependencies:

| Remote Task Type | Flyte Type |
|-------------------|------------|
| DataFrames (`pandas`, `polars`, `spark`, etc.) | `flyte.io.DataFrame` |
| Object store files | `flyte.io.File` |
| Object store directories | `flyte.io.Dir` |
| Pydantic models | Dictionary (Flyte creates a representation) |

Any DataFrame type (pandas, polars, spark) automatically becomes `flyte.io.DataFrame`, allowing seamless data exchange between tasks using different DataFrame libraries. You can also write custom integrations or explore Flyte's plugin system for additional types.

For Pydantic models specifically, you don't need the exact model locally. Pass a dictionary as input, and Flyte will handle the translation.

## Versioning options

Reference tasks support flexible versioning:

**Specific version**:

```python
task = flyte.remote.Task.get(
    "team_a.process_data",
    version="v1.2.3"
)
```

**Latest version** (`auto_version="latest"`):

```python
# Always use the most recently deployed version
task = flyte.remote.Task.get(
    "team_a.process_data",
    auto_version="latest"
)
```

**Current version** (`auto_version="current"`):

```python
# Use the same version as the calling task's deployment
# Useful when all environments deploy with the same version
# Can only be used from within a task context
task = flyte.remote.Task.get(
    "team_a.process_data",
    auto_version="current"
)
```

## Best practices

### 1. Use meaningful task names

Remote tasks are accessed by name, so use clear, descriptive naming:

```python
# Good
customer_segmentation = flyte.remote.Task.get("ml_platform.customer_segmentation")

# Avoid
task1 = flyte.remote.Task.get("team_a.task1")
```

### 2. Document task interfaces

Since remote tasks abstract away implementation details, clear documentation of inputs, outputs, and behavior is essential:

```python
@env.task
async def process_customer_data(
    customer_ids: list[str],
    date_range: tuple[str, str]
) -> flyte.io.DataFrame:
    """
    Process customer data for the specified date range.

    Args:
        customer_ids: List of customer IDs to process
        date_range: Tuple of (start_date, end_date) in YYYY-MM-DD format

    Returns:
        DataFrame with processed customer features
    """
    ...
```

### 3. Handle versioning thoughtfully

- Use `auto_version="latest"` during development for rapid iteration
- Use specific versions in production for stability and reproducibility
- Use `auto_version="current"` when coordinating multienvironment deployments

### 4. Deploy remote tasks first

Always deploy the remote tasks before using them. Tasks that reference them can be run directly without deployment:

```bash
# Deploy the Spark environment first
flyte deploy spark_env/

# Deploy the ML environment
flyte deploy ml_env/

# Now you can run the orchestration task directly (no deployment needed)
flyte run orchestration_env.py orchestrate_pipeline
```

If you want to deploy the orchestration task as well (for scheduled runs or to be referenced by other tasks), deploy it after its dependencies:

```bash
flyte deploy orchestration_env/
```

### 5. Test integration carefully

Remote tasks introduce remote dependencies. Test thoroughly:

```python
@env.task
async def integration_test() -> bool:
    ref_task = flyte.remote.Task.get("other_team.task", auto_version="latest")

    # Test with known inputs
    result = await ref_task(test_input="validation_data")

    # Verify expected outputs
    assert result.status == "success"
    return True
```

## Limitations

1. **Type fidelity**: While Flyte translates types seamlessly, you work with Flyte's representation of Pydantic models, not the exact original types

2. **Deployment order**: Referenced tasks must be deployed before tasks that reference them

3. **Context requirement**: Using `auto_version="current"` requires running within a task context

4. **Dictionary inputs**: Pydantic models must be passed as dictionaries, which loses compile-time type checking

## Next steps

- Learn about [task deployment](../task-deployment)
- Explore [task environments and configuration](../task-configuration)
