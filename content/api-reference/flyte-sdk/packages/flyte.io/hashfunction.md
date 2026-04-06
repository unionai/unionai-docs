---
title: HashFunction
version: 2.1.2
variants: +flyte +union
layout: py_api
---

# HashFunction

**Package:** `flyte.io`

A hash method that wraps a user-provided function to compute hashes.

This class allows you to define custom hashing logic by providing a callable
that takes data and returns a hash string. It implements the HashMethod protocol,
making it compatible with Flyte's hashing infrastructure.



## Parameters

```python
class HashFunction(
    fn: Callable[[Any], str],
)
```
Initialize a HashFunction with a custom hash callable.



| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[[Any], str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_fn()`](#from_fn) | Create a HashFunction from a callable. |
| [`reset()`](#reset) |  |
| [`result()`](#result) | Return the most recently computed hash value. |
| [`update()`](#update) | Update the hash value by applying the hash function to the given data. |


### from_fn()

```python
def from_fn(
    fn: Callable[[Any], str],
) -> HashFunction
```
Create a HashFunction from a callable.

This is a convenience factory method for creating HashFunction instances.



| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[[Any], str]` | A callable that takes data of any type and returns a hash string. |

**Returns**

A new HashFunction instance wrapping the provided callable.


### reset()

```python
def reset()
```
### result()

```python
def result()
```
Return the most recently computed hash value.



**Returns:** The hash string from the last call to update().

### update()

```python
def update(
    data: Any,
)
```
Update the hash value by applying the hash function to the given data.



| Parameter | Type | Description |
|-|-|-|
| `data` | `Any` | The data to hash. The type depends on the hash function provided. |

