# Actors

The Actors feature allows you to reuse containers between tasks that need to maintain state. You can create an actor by instantiating the `ActorEnvironment` class, then use the actor name as a decorator on functions that require that environment.

## Examples

### Hello world

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/hello_world.py
:caption: hello_world.py

```

### Addition

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/plus_one.py
:caption: plus_one.py

```

