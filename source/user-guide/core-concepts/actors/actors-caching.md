# Caching on Actor Replicas

The `@actor.cache` decorator provides a powerful mechanism to cache the results of Python callables on individual actor replicas. This is particularly beneficial for workflows involving repetitive tasks, such as data preprocessing, model loading, or initialization of shared resources, where caching can minimize redundant operations and improve overall efficiency. This avoids repetitive computation or loading processes, particularly useful for workflows that involve expensive operations like loading large datasets or initializing machine learning models. Once a callable is cached on a replica, subsequent tasks that use the same actor can access the cached result, significantly improving performance and efficiency.

## When to Use `actor.cache`

- **Shared Initialization Costs:**  
  For expensive, shared initialization processes that multiple tasks rely on.

- **Repetitive Task Execution:**  
  When tasks repeatedly require the same resource or computation on the same actor replica.

- **Complex Object Caching:**  
  Use custom Python objects as keys to define unique cache entries.

- **Avoiding Resource Contention:**  
  Ensure some tasks are explicitly run to initialize shared resources, avoiding race conditions.

## Example: Caching Expensive Operations

Below is a simplified example showcasing the use of `@actor.cache` for caching repetitive tasks. This dummy example demonstrates caching model that is loaded by the `load_model` task.

```python
from time import sleep

from union import ActorEnvironment, workflow

image = "ghcr.io/unionai-oss/union:py3.11-0.1.121"

actor = ActorEnvironment(
    name="my-actor",
    container_image=image,
    replica_count=1,
)


@actor.cache
def load_model(state: int) -> callable:
    sleep(4)  # simulate model loading
    return lambda value: state + value


@actor.task
def evaluate(value: int, state: int) -> int:
    model = load_model(state=state)
    return model(value)


@workflow
def wf(init_value: int = 1, state: int = 3) -> int:
    out = evaluate(value=init_value, state=state)
    out = evaluate(value=out, state=state)
    out = evaluate(value=out, state=state)
    out = evaluate(value=out, state=state)
    return out
```

![Actor caching example 1](/_static/images/user-guide/core-concepts/actors/caching/actor-cache-example-1.png)

You can see that the first call of `evaluate` took considerable time as it involves allocating a node for the task, creating a container, and loading the model. The subsequent calls of `evaluate` execute in a fraction of the time. 

## Example: `@actor.cache` with `map_task`

It can be idea to use map tasks with since they reuse the same environment and involve repetition. If a task has an expensive operation, like model loading, caching it with `@actor.cache` can improve performance. This example shows how to cache model loading in a mapped task to avoid redundant work and save resources.

```python
from functools import partial
from pathlib import Path
from time import sleep

from union import ActorEnvironment, FlyteFile, current_context, map_task, task, workflow

image = "ghcr.io/unionai-oss/union:py3.11-0.1.121"

actor = ActorEnvironment(
    name="my-actor",
    container_image=image,
    replica_count=2,
)


class MyModel:
    """Simple model that multiples value with model_state."""

    def __init__(self, model_state: int):
        self.model_state = model_state

    def __call__(self, value: int):
        return self.model_state * value


@task(container_image=image, cache=True, cache_version="v1")
def create_model_state() -> FlyteFile:
    working_dir = Path(current_context().working_directory)
    model_state_path = working_dir / "model_state.txt"
    model_state_path.write_text("4")
    return model_state_path


@actor.cache
def load_model(model_state_path: FlyteFile) -> MyModel:
    # Simulate model loading time. This can take a long time
    # because the FlyteFile download is large, or when the  
    # model is loaded onto the GPU.
    sleep(10)
    with model_state_path.open("r") as f:
        model_state = int(f.read())

    return MyModel(model_state=model_state)


@actor.task
def inference(value: int, model_state_path: FlyteFile) -> int:
    model = load_model(model_state_path)
    return model(value)


@workflow
def run_inference(values: list[int] = list(range(20))) -> list[int]:
    model_state = create_model_state()
    inference_ = partial(inference, model_state_path=model_state)
    return map_task(inference_)(value=values)
```

## Example: Caching with Custom Objects

Finally, we can cache custom objects by defining the `__hash__` and `__eq__` methods. These methods allow `@actor.cache` to determine if an object is the same between runs, ensuring that expensive operations are skipped if the object hasn’t changed.

```python
from time import sleep

from union import ActorEnvironment, workflow

image = "ghcr.io/unionai-oss/union:py3.11-0.1.121"

actor = ActorEnvironment(
    name="my-actor",
    container_image=image,
    replica_count=1,
)


class MyObj:
    def __init__(self, state: int):
        self.state = state

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state


@actor.cache
def get_state(obj: MyObj) -> int:
    sleep(2)
    return obj.state


@actor.task
def construct_and_get_value(state: int) -> int:
    obj = MyObj(state=state)
    return get_state(obj)


@workflow
def wf(state: int = 2) -> int:
    value = construct_and_get_value(state=state)
    value = construct_and_get_value(state=value)
    value = construct_and_get_value(state=value)
    value = construct_and_get_value(state=value)
    return value
```