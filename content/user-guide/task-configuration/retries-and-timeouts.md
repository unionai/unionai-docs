---
title: Retries and timeouts
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# Retries and timeouts

Flyte provides robust error handling through configurable retry strategies and timeout controls. These parameters help ensure task reliability and prevent resource waste from runaway processes.

## Retries

The `retries` parameter controls how many times a failed task should be retried before giving up. It accepts both simple integer values and advanced retry strategies.

### Simple integer retries

```python
import flyte

env = flyte.TaskEnvironment(name="my-env", image="python:3.12")

@env.task(retries=3)
async def unreliable_task():
    # This task will be retried up to 3 times if it fails
    import random
    if random.random() < 0.7:  # 70% failure rate
        raise Exception("Task failed!")
    return "Success!"
```

### Advanced retry strategy

For more control over retry behavior, use `RetryStrategy`:

```python
from flyte import RetryStrategy
from datetime import timedelta

@env.task(retries=RetryStrategy(
    count=5,                          # Retry up to 5 times
    backoff=timedelta(seconds=10),    # Maximum backoff time between retries
    backoff_factor=2.0                # Exponential backoff factor
))
async def network_task():
    # Retries with exponential backoff: 2s, 4s, 8s, 10s (max), 10s (max)
    import httpx
    response = httpx.get("https://api.example.com/data")
    response.raise_for_status()
    return response.json()
```

**RetryStrategy parameters:**
- `count`: Number of retry attempts
- `backoff`: Maximum time to wait between retries (float seconds or timedelta)
- `backoff_factor`: Multiplier for exponential backoff (e.g., 2.0 doubles wait time each retry)

## Timeouts

The `timeout` parameter sets limits on how long a task can run, preventing resource waste from stuck processes. It supports multiple formats for different use cases.

### Simple timeout (seconds)

```python
@env.task(timeout=300)  # 5 minutes
async def data_processing():
    # Task will be terminated if it runs longer than 5 minutes
    process_large_dataset()
    return "Processing complete"
```

### Timedelta timeout

```python
from datetime import timedelta

@env.task(timeout=timedelta(minutes=10))
async def model_training():
    # More readable timeout specification
    train_machine_learning_model()
    return "Model trained"
```

### Advanced timeout control

For fine-grained control over queue and execution time:

```python
from flyte import Timeout
from datetime import timedelta

@env.task(timeout=Timeout(
    max_runtime=timedelta(minutes=5),      # Max execution time per attempt
    max_queued_time=timedelta(minutes=2)   # Max time in queue before starting
))
async def priority_task():
    # Task fails if:
    # - Queued for more than 2 minutes, OR
    # - Any single execution attempt runs longer than 5 minutes
    return perform_critical_operation()
```

**Timeout parameters:**
- `max_runtime`: Maximum time the task can execute (per attempt)
- `max_queued_time`: Maximum time the task can wait in the queue before execution starts

## Combining retries and timeouts

Retries and timeouts work together to provide comprehensive error handling:

```python
@env.task(
    retries=RetryStrategy(
        count=3,
        backoff=timedelta(seconds=30),
        backoff_factor=2.0
    ),
    timeout=Timeout(
        max_runtime=timedelta(minutes=10),
        max_queued_time=timedelta(minutes=5)
    )
)
async def robust_task():
    """
    This task configuration provides:
    - Up to 3 retry attempts with exponential backoff (30s, 60s, 120s)
    - Each attempt times out after 10 minutes
    - Task fails if queued for more than 5 minutes
    - Total possible runtime: 5min queue + (10min × 3 attempts) + backoff time
    """
    return perform_complex_operation()
```

## Key behaviors

### Retry timing
- Each retry attempt gets the full timeout duration
- Backoff time is calculated as: `min(backoff, initial_wait * backoff_factor^attempt)`
- Retries are independent - a timeout doesn't consume retry attempts

### Failure handling
- If all retries are exhausted, the task fails permanently
- Timeout failures can be retried (if retries are configured)
- Queue timeouts are separate from execution timeouts

### Resource implications
- Failed tasks still consume resources during their runtime
- Exponential backoff prevents overwhelming downstream services
- Queue timeouts help manage cluster resource allocation

## Best practices

### Choose appropriate retry counts
```python
# Network calls: Higher retry count with backoff
@env.task(retries=RetryStrategy(count=5, backoff_factor=2.0))
async def api_call(): pass

# File I/O: Moderate retries
@env.task(retries=3)
async def file_operation(): pass

# Deterministic computation: No retries needed
@env.task(retries=0)
async def math_calculation(): pass
```

### Set realistic timeouts
```python
# Quick operations: Short timeout
@env.task(timeout=timedelta(seconds=30))
async def validation(): pass

# Data processing: Longer timeout based on data size
@env.task(timeout=timedelta(hours=2))
async def etl_pipeline(): pass

# Interactive tasks: Queue timeout for responsiveness
@env.task(timeout=Timeout(
    max_runtime=timedelta(minutes=30),
    max_queued_time=timedelta(seconds=30)  # Fast queue turnaround
))
async def user_request(): pass
```

### Environment-specific strategies
```python
# Development: Fail fast for quick feedback
dev_env = flyte.TaskEnvironment(name="dev", image="python:3.12")

@dev_env.task(retries=1, timeout=timedelta(minutes=5))
async def dev_task(): pass

# Production: Robust retry strategy
prod_env = flyte.TaskEnvironment(name="prod", image="python:3.12")

@prod_env.task(
    retries=RetryStrategy(count=3, backoff_factor=1.5),
    timeout=timedelta(minutes=30)
)
async def prod_task(): pass
```

Proper retry and timeout configuration ensures your Flyte workflows are both reliable and efficient, handling transient failures gracefully while preventing resource waste.