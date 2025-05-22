---
title: Actor examples
weight: 2
variants: -flyte +serverless +byoc +selfmanaged
---

# Actor examples

### Refactoring from Regular Tasks to Actors

Notice that converting a non-actor workflow to use actors is as simple as replacing the `@{{< key kit_as >}}.task` decorator with the `@actor.task` decorator. Additionally, task decorator arguments can be moved either to the actor environment or the actor task decorator, depending on whether they apply to the entire environment (e.g. resource specifications) or to a single task execution (e.g. caching arguments).

```diff
import {{< key kit_import >}}

+ actor = {{< key kit_as >}}.ActorEnvironment(
+    name = "myenv",
+    replica_count = 10,
+    ttl_seconds = 120,
+    requests = {{< key kit_as >}}.Resources(mem="1Gi"),
+    container_image = "myrepo/myimage-with-scipy:latest",
+)
+
- @{{< key kit_as >}}.task(requests={{< key kit_as >}}.Resources(mem="1Gi"))
+ @actor.task
def add_numbers(a: float, b: float) -> float:
    return a + b

- @{{< key kit_as >}}.task(container_image="myrepo/myimage-with-scipy:latest")
+ @actor.task
def calculate_distance(point_a: list[int], point_b: list[int]) -> float:
    from scipy.spatial.distance import euclidean
    return euclidean(point_a, point_b)

- @{{< key kit_as >}}.task(cache=True, cache_version="v1")
+ @actor.task(cache=True, cache_version="v1")
def is_even(number: int) -> bool:
    return number % 2 == 0

@{{< key kit_as >}}.workflow
def distance_add_wf(point_a: list[int], point_b: list[int]) -> float:
    distance = calculate_distance(point_a=point_a, point_b=point_b)
    return add_numbers(a=distance, b=1.5)

@{{< key kit_as >}}.workflow
def is_even_wf(point_a: list[int]) -> list[bool]:
    return {{< key kit_as >}}.{{<key map_func>}}(is_even)(number=point_a)
```
<!-- TODO: emphasize-lines: 2,3,4,5,6,7,8,9,10,11,13,18,24 -->

## Multiple instances of the same task

In this example, the `actor.task`-decorated task is invoked multiple times in one workflow, and will use the same `ActorEnvironment` on each invocation:

{{< variant serverless >}}
{{< markdown >}}

```python
# plus_one.py

import {{< key kit_import >}}


actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=1,
    ttl_seconds=300,
    requests={{< key kit_as >}}.Resources(cpu="2", mem="500Mi"),
)


@actor.task
def plus_one(input: int) -> int:
    return input + 1


@{{< key kit_as >}}.workflow
def wf(input: int = 0) -> int:
    a = plus_one(input=input)
    b = plus_one(input=a)
    c = plus_one(input=b)
    return plus_one(input=c)
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

```python
# plus_one.py

import os

import {{< key kit_import >}}

image = {{< key kit_as >}}.ImageSpec(
    registry=os.environ.get("DOCKER_REGISTRY", None),
    packages=["union"],
)

actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=1,
    ttl_seconds=300,
    requests={{< key kit_as >}}.Resources(cpu="2", mem="500Mi"),
    container_image=image,
)


@actor.task
def plus_one(input: int) -> int:
    return input + 1


@{{< key kit_as >}}.workflow
def wf(input: int = 0) -> int:
    a = plus_one(input=input)
    b = plus_one(input=a)
    c = plus_one(input=b)
    return plus_one(input=c)


```

{{< /markdown >}}
{{< /variant >}}

## Multiple tasks

Every task execution in the following example will execute in the same `ActorEnvironment`.
You can use the same environment for multiple tasks in the same workflow and tasks across workflow definitions, using both subworkflows and launch plans:

{{< variant serverless >}}
{{< markdown >}}

```python
# multiple_tasks.py

import {{< key kit_import >}}


actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=1,
    ttl_seconds=30,
    requests={{< key kit_as >}}.Resources(cpu="1", mem="450Mi"),
)


@actor.task
def say_hello(name: str) -> str:
    return f"hello {name}"


@actor.task
def scream_hello(name: str) -> str:
    return f"HELLO {name}"


@{{< key kit_as >}}.workflow
def my_child_wf(name: str) -> str:
    return scream_hello(name=name)


my_child_wf_lp = {{< key kit_as >}}.LaunchPlan.get_default_launch_plan({{< key kit_as >}}.current_context(), my_child_wf)


@{{< key kit_as >}}.workflow
def my_parent_wf(name: str) -> str:
    a = say_hello(name=name)
    b = my_child_wf(name=a)
    return my_child_wf_lp(name=b)
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

```python
# multiple_tasks.py

import os

import {{< key kit_import >}}

image = {{< key kit_as >}}.ImageSpec(
    registry=os.environ.get("DOCKER_REGISTRY", None),
    packages=["union"],
)

actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=1,
    ttl_seconds=30,
    requests={{< key kit_as >}}.Resources(cpu="1", mem="450Mi"),
    container_image=image,
)


@actor.task
def say_hello(name: str) -> str:
    return f"hello {name}"


@actor.task
def scream_hello(name: str) -> str:
    return f"HELLO {name}"


@{{< key kit_as >}}.workflow
def my_child_wf(name: str) -> str:
    return scream_hello(name=name)


my_child_wf_lp = {{< key kit_as >}}.LaunchPlan.get_default_launch_plan({{< key kit_as >}}.current_context(), my_child_wf)


@{{< key kit_as >}}.workflow
def my_parent_wf(name: str) -> str:
    a = say_hello(name=name)
    b = my_child_wf(name=a)
    return my_child_wf_lp(name=b)
```

{{< /markdown >}}
{{< /variant >}}

## Custom PodTemplates

Both tasks in the following example will be executed in the same `ActorEnvironment`, which is created with a `PodTemplate` for additional configuration.

```python
# pod_template.py

import os

from kubernetes.client.models import (
    V1Container,
    V1PodSpec,
    V1ResourceRequirements,
    V1EnvVar,
)
import {{< key kit_import >}}

image = {{< key kit_as >}}.ImageSpec(
    registry=os.environ.get("DOCKER_REGISTRY", None),
    packages=["union", "flytekitplugins-pod"],
)

pod_template = {{< key kit_as >}}.PodTemplate(
    primary_container_name="primary",
    pod_spec=V1PodSpec(
        containers=[
            V1Container(
                name="primary",
                image=image,
                resources=V1ResourceRequirements(
                    requests={
                        "cpu": "1",
                        "memory": "1Gi",
                    },
                    limits={
                        "cpu": "1",
                        "memory": "1Gi",
                    },
                ),
                env=[V1EnvVar(name="COMP_KEY_EX", value="compile_time")],
            ),
        ],
    ),
)

actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=1,
    ttl_seconds=30,
    pod_template=pod_template,
)

@actor.task
def get_and_set() -> str:
    os.environ["RUN_KEY_EX"] = "run_time"
    return os.getenv("COMP_KEY_EX")


@actor.task
def check_set() -> str:
    return os.getenv("RUN_KEY_EX")


@{{< key kit_as >}}.workflow
def wf() -> tuple[str,str]:
    return get_and_set(), check_set()
```

## Example: `@actor_cache` with `map`

With map tasks, each task is executed within the same environment, making actors a natural fit for this pattern. If a task has an expensive operation, like model loading, caching it with `@actor_cache` can improve performance. This example shows how to cache model loading in a mapped task to avoid redundant work and save resources.

{{< variant serverless >}}
{{< markdown >}}

```python
# caching_map_task.py

from functools import partial
from pathlib import Path
from time import sleep

import {{< key kit_import >}}

actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=2,
)


class MyModel:
    """Simple model that multiples value with model_state."""

    def __init__(self, model_state: int):
        self.model_state = model_state

    def __call__(self, value: int):
        return self.model_state * value


@{{< key kit_as >}}.task(cache=True, cache_version="v1")
def create_model_state() -> {{< key kit_as >}}.FlyteFile:
    working_dir = Path({{< key kit_as >}}.current_context().working_directory)
    model_state_path = working_dir / "model_state.txt"
    model_state_path.write_text("4")
    return model_state_path


@{{< key kit_as >}}.actor_cache
def load_model(model_state_path: {{< key kit_as >}}.FlyteFile) -> MyModel:
    # Simulate model loading time. This can take a long time
    # because the FlyteFile download is large, or when the
    # model is loaded onto the GPU.
    sleep(10)
    with model_state_path.open("r") as f:
        model_state = int(f.read())

    return MyModel(model_state=model_state)


@actor.task
def inference(value: int, model_state_path: {{< key kit_as >}}.FlyteFile) -> int:
    model = load_model(model_state_path)
    return model(value)


@{{< key kit_as >}}.workflow
def run_inference(values: list[int] = list(range(20))) -> list[int]:
    model_state = create_model_state()
    inference_ = partial(inference, model_state_path=model_state)
    return {{< key kit_as >}}.{{<key map_func>}}(inference_)(value=values)
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

```python
# caching_map_task.py

from functools import partial
from pathlib import Path
from time import sleep
import os

import {{< key kit_import >}}

image = {{< key kit_as >}}.ImageSpec(
    registry=os.environ.get("DOCKER_REGISTRY", None),
    packages=["union"],
)

actor = {{< key kit_as >}}.ActorEnvironment(
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


@{{< key kit_as >}}.task(container_image=image, cache=True, cache_version="v1")
def create_model_state() -> {{< key kit_as >}}.FlyteFile:
    working_dir = Path({{< key kit_as >}}.current_context().working_directory)
    model_state_path = working_dir / "model_state.txt"
    model_state_path.write_text("4")
    return model_state_path


@{{< key kit_as >}}.actor_cache
def load_model(model_state_path: {{< key kit_as >}}.FlyteFile) -> MyModel:
    # Simulate model loading time. This can take a long time
    # because the FlyteFile download is large, or when the
    # model is loaded onto the GPU.
    sleep(10)
    with model_state_path.open("r") as f:
        model_state = int(f.read())

    return MyModel(model_state=model_state)


@actor.task
def inference(value: int, model_state_path: {{< key kit_as >}}.FlyteFile) -> int:
    model = load_model(model_state_path)
    return model(value)


@{{< key kit_as >}}.workflow
def run_inference(values: list[int] = list(range(20))) -> list[int]:
    model_state = create_model_state()
    inference_ = partial(inference, model_state_path=model_state)
    return {{< key kit_as >}}.{{<key map_func>}}(inference_)(value=values)
```

{{< /markdown >}}
{{< /variant >}}

## Example: Caching with Custom Objects

Finally, we can cache custom objects by defining the `__hash__` and `__eq__` methods. These methods allow `@actor_cache` to determine if an object is the same between runs, ensuring that expensive operations are skipped if the object hasn’t changed.

{{< variant serverless >}}
{{< markdown >}}

```python
# caching_custom_object.py

from time import sleep

import {{< key kit_import >}}


actor = {{< key kit_as >}}.ActorEnvironment(
    name="my-actor",
    replica_count=1,
)


class MyObj:
    def __init__(self, state: int):
        self.state = state

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state


@{{< key kit_as >}}.actor_cache
def get_state(obj: MyObj) -> int:
    sleep(2)
    return obj.state


@actor.task
def construct_and_get_value(state: int) -> int:
    obj = MyObj(state=state)
    return get_state(obj)


@{{< key kit_as >}}.workflow
def wf(state: int = 2) -> int:
    value = construct_and_get_value(state=state)
    value = construct_and_get_value(state=value)
    value = construct_and_get_value(state=value)
    value = construct_and_get_value(state=value)
    return value
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

```python
# caching_custom_object.py

from time import sleep
import os

import {{< key kit_import >}}

image = {{< key kit_as >}}.ImageSpec(
    registry=os.environ.get("DOCKER_REGISTRY", None),
    packages=["union"],
)

actor = {{< key kit_as >}}.ActorEnvironment(
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


@{{< key kit_as >}}.actor_cache
def get_state(obj: MyObj) -> int:
    sleep(2)
    return obj.state


@actor.task
def construct_and_get_value(state: int) -> int:
    obj = MyObj(state=state)
    return get_state(obj)


@{{< key kit_as >}}.workflow
def wf(state: int = 2) -> int:
    value = construct_and_get_value(state=state)
    value = construct_and_get_value(state=value)
    value = construct_and_get_value(state=value)
    value = construct_and_get_value(state=value)
    return value
```

{{< /markdown >}}
{{< /variant >}}
