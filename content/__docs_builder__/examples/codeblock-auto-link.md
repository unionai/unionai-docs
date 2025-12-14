---
title: Hyperlinks to Docs
variants: -flyte -serverless -byoc -selfmanaged
---

# Automatic Code Documentation Linkage

## Code Blocks

```python
import flyte
from flyte import Trigger

env = flyte.TaskEnvironment(...)

t = Trigger("fofo")

try:
    do_something("mytrigger")
except flyte.errors.RuntimeDataValidationError as e:
    ...


def run():
    ...
```

### Rules

* Parse `import` and `from` to load valid types
* Match all direct matches of `fully.qualified.Type`
* Match any identifiers in the from clause `from flyte import Trigger` will make `flyte`, `Trigger`, and all references to `Trigger` in the code linked to the documentation
* Non-existing classes or methods will never be linked. They must exist in the SDK to be linked.

## Inline `backticks`

This is a test of inline code: `flyte.run()` and `flyte.TaskEnvironment` and `flyte.init()`.

You can match a function like `[[run()]]` (links to `flyte.run()`), but also not match for non-docs like `run()`.

### Rules

* We will not match random, non-qualified text, like `run()`.
* But we will match a fully qualified, and existing SDK match, like `flyte.Trigger`
* We can match a "best-effort" function if you add the magic markers `[[` and `]]`, like `[[run()]]`.
* Non-existing classes or methods will never be linked. They must exist in the SDK to be linked.

In other words, if you qualify `flyte.TaskEnvironment` it will match, but if you write `TaskEnvironment` will not. Unless you surround it with `[[` and `]]`, then it will match: `[[TaskEnvironment]]`.