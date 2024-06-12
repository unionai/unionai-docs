# Actors

Actors allow you to reuse containers between tasks that need to maintain state. You can create an actor by instantiating the [`ActorEnvironment`](../api/sdk/actor.actorenvironment) class, then add the `@actor` decorator to thet task that requires a stateful environment every time it's invoked. 

## `ActorEnvironment` parameters

* **backlog_length**
* **container_image**
* **environment**
* **parallelism**: The number of tasks that can execute in parallel, per worker.
* **replica_count:** The number of workers to provision that are able to accept tasks.
* **requests**
* **secret_request**
* **ttl_seconds** How long to keep the Actor alive while no tasks are being run.

## Examples

### Hello world

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/hello_world.py
:caption: hello_world.py

```

### Addition

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/plus_one.py
:caption: plus_one.py

```
