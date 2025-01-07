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

Below is a simplified example showcasing the use of `@actor.cache` for caching repetitive tasks. This dummy example demonstrates caching operations like loading a directory and file, which theoretically take a long time, so they are cached to avoid repeated loading across replicas.

```python
from time import sleep
from flytekit import fl
from union.actor import ActorEnvironment

actor = ActorEnvironment(...)

class MyObject:
    def __init__(self, value: int):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


@fl.task(container_image=image, cache=True, cache_version="1")
def create_file() -> FlyteFile:
    ctx = current_context()
    working_dir = Path(ctx.working_directory)
    file = working_dir / "my_file.txt"
    file.write_text("34")
    return file


@fl.task(container_image=image, cache=True, cache_version="1")
def create_directory() -> FlyteDirectory:
    ctx = current_context()
    working_dir = Path(ctx.working_directory)
    file = working_dir / "another.txt"
    file.write_text("12")
    return working_dir


@actor.cache
def load_data(file: FlyteFile) -> int:
    sleep(2)  # Let's say the file takes a long time to load
    with open(file, "r") as f:
        return int(f.read())


@actor.cache
def load_directory(d: FlyteDirectory) -> int:
    path = Path(d.download())
    sleep(2)
    with (path / "another.txt").open("r") as f:
        return int(f.read())


@actor.cache
def get_value(obj: MyObject) -> int:
    sleep(2)
    return obj.value


@actor.task
def add_file(num: int, file: FlyteFile, d: FlyteDirectory) -> int:
    d1 = load_data(file=file)
    d2 = load_directory(d=d)
    my_obj = MyObject(value=1)
    val = get_value(my_obj)
    return num + d1 + d2 + val


@fl.workflow
def add_five(num: int) -> int:
    file = create_file()
    d = create_directory()
    result = add_file(num=num, file=file, d=d)
    result = add_file(num=result, file=file, d=d)
    result = add_file(num=result, file=file, d=d)
    result = add_file(num=result, file=file, d=d)
    return result
```

In this example, `load_data`, `load_directory`, and `get_value` are computed only once per unique input on a given actor replica, saving significant time across repeated calls.

## Example: Avoiding Race Conditions

To ensure that a resource is initialized before downstream tasks execute, use a separate task to preload the resource and set the dependency graph using `>>` notation. This approach avoids potential race conditions when multiple tasks access the same cache.

```python
actor = ActorEnvironment(...)

@actor.cache
def load(model_dir: str):
    # Simulate loading a model
    sleep(2)
    return f"Model loaded from {model_dir}"

@actor.task
def load_model_task(model_dir: str):
    # Ensure the model is loaded before downstream tasks execute
    load(model_dir=model_dir)

@actor.task
def run_inference(model_dir: str, input: list[str]) -> list[str]:
    model = load(model_dir=model_dir)
    return [f"{model} inference on {i}" for i in input]

@fl.workflow
def inference_workflow(model_dir: str, input: list[str]) -> list[str]:
    load_model_task(model_dir=model_dir)
    run = run_inference(model_dir=model_dir, input=input)
    load >> run  # always run `load` before `run` so that the model gets loaded first
```

In this example, `load_model_task` ensures the model is cached before any inference task runs, avoiding contention or redundant initialization.