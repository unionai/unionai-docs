# Actors

Actors allow you to reuse containers between functions that need to maintain state. You can create an actor by instantiating the [`ActorEnvironment`](../api/sdk/actor.actorenvironment) class, then use `@actor` decorator on functions or classes that require that environment.

## Examples

### Hello world

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/hello_world.py
:caption: hello_world.py

```

### Addition

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/plus_one.py
:caption: plus_one.py

```
