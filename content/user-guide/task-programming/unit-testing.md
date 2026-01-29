---
title: Unit Testing Tasks
weight: 14
variants: +flyte +serverless +byoc +selfmanaged
---

Unit testing is essential for ensuring your Flyte tasks work correctly. Flyte 2.0 provides flexible testing approaches that allow you to test both your business logic and Flyte-specific features like type transformations and caching.

## Understanding Task Invocation

When working with functions decorated with `@env.task`, there are two ways to invoke them, each with different behavior:

### Direct Function Invocation

When you call a task directly like a regular Python function:

```python
result = my_task(x=10, y=20)
```

**Flyte features are NOT invoked**, including:
- Type transformations and serialization
- Caching
- Data validation

This behaves exactly like calling a regular Python function, making it ideal for testing your business logic.

### Using `flyte.run()`

When you invoke a task using `flyte.run()`:

```python
run = flyte.run(my_task, x=10, y=20)
result = run.outputs()
```

**Flyte features ARE invoked**, including:
- Type transformations and serialization
- Data validation
- Type checking (raises `flyte.errors` if types are not supported or restricted)

This allows you to test Flyte-specific behavior like serialization and caching.

## Testing Business Logic

For most unit tests, you want to verify your business logic works correctly. Use **direct function invocation** for this:

```python
import flyte

env = flyte.TaskEnvironment("my_env")

@env.task
def add(a: int, b: int) -> int:
    return a + b

def test_add():
    result = add(a=3, b=5)
    assert result == 8
```

### Testing Async Tasks

Async tasks work the same way with direct invocation:

```python
import pytest

@env.task
async def subtract(a: int, b: int) -> int:
    return a - b

@pytest.mark.asyncio
async def test_subtract():
    result = await subtract(a=10, b=4)
    assert result == 6
```

### Testing Nested Tasks

When tasks call other tasks, direct invocation continues to work without any Flyte overhead:

```python
@env.task
def nested(a: int, b: int) -> int:
    return add(a, b)  # Calls the add task directly

def test_nested():
    result = nested(3, 5)
    assert result == 8
```

## Testing Type Transformations and Serialization

When you need to test how Flyte handles data types, serialization, or caching, use `flyte.run()`:

```python
@pytest.mark.asyncio
async def test_add_with_flyte_run():
    run = flyte.run(add, 3, 5)
    assert run.outputs() == 8
```

### Testing Type Restrictions

Some types may not be supported or may be restricted. Use `flyte.run()` to test that these restrictions are enforced:

```python
from typing import Tuple
import flyte.errors

@env.task
def not_supported_types(x: Tuple[str, str]) -> str:
    return x[0]

@pytest.mark.asyncio
async def test_not_supported_types():
    # Direct invocation works fine
    result = not_supported_types(x=("a", "b"))
    assert result == "a"

    # flyte.run enforces type restrictions
    with pytest.raises(flyte.errors.RestrictedTypeError):
        flyte.run(not_supported_types, x=("a", "b"))
```

### Testing Nested Tasks with Serialization

You can also test nested task execution with Flyte's full machinery:

```python
@pytest.mark.asyncio
async def test_nested_with_run():
    run = flyte.run(nested, 3, 5)
    assert run.outputs() == 8
```

## Testing Traced Functions

Functions decorated with `@flyte.trace` can be tested similarly to tasks:

```python
@flyte.trace
async def traced_multiply(a: int, b: int) -> int:
    return a * b

@pytest.mark.asyncio
async def test_traced_multiply():
    result = await traced_multiply(a=6, b=7)
    assert result == 42
```

## Best Practices

1. **Test logic with direct invocation**: For most unit tests, call tasks directly to test your business logic without Flyte overhead.

2. **Test serialization with `flyte.run()`**: Use `flyte.run()` when you need to verify:
   - Type transformations work correctly
   - Data serialization/deserialization
   - Caching behavior
   - Type restrictions are enforced

3. **Use standard testing frameworks**: Flyte tasks work with pytest, unittest, and other Python testing frameworks.

4. **Test async tasks properly**: Use `@pytest.mark.asyncio` for async tasks and await their results.

5. **Mock external dependencies**: Use standard Python mocking techniques for external services, databases, etc.

## Quick Reference

| Test Scenario | Method | Example |
|--------------|--------|---------|
| Business logic (sync) | Direct call | `result = task(x=10)` |
| Business logic (async) | Direct await | `result = await task(x=10)` |
| Type transformations | `flyte.run()` | `r = flyte.run(task, x=10)` |
| Data serialization | `flyte.run()` | `r = flyte.run(task, x=10)` |
| Caching behavior | `flyte.run()` | `r = flyte.run(task, x=10)` |
| Type restrictions | `flyte.run()` + pytest.raises | `pytest.raises(flyte.errors.RestrictedTypeError)` |

## Example Test Suite

Here's a complete example showing different testing approaches:

```python
import pytest
import flyte
import flyte.errors

env = flyte.TaskEnvironment("test_env")

@env.task
def add(a: int, b: int) -> int:
    return a + b

@env.task
async def subtract(a: int, b: int) -> int:
    return a - b

# Test business logic directly
def test_add_logic():
    result = add(a=3, b=5)
    assert result == 8

@pytest.mark.asyncio
async def test_subtract_logic():
    result = await subtract(a=10, b=4)
    assert result == 6

# Test with Flyte serialization
@pytest.mark.asyncio
async def test_add_serialization():
    run = flyte.run(add, 3, 5)
    assert run.outputs() == 8

@pytest.mark.asyncio
async def test_subtract_serialization():
    run = flyte.run(subtract, a=10, b=4)
    assert run.outputs() == 6
```

## Future Improvements

The Flyte SDK team is actively working on improvements for advanced unit testing scenarios, particularly around initialization and setup for complex test cases. Additional utilities and patterns may be introduced in future releases to make unit testing even more streamlined.

