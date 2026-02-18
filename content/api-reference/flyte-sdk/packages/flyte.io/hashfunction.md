---
title: HashFunction
version: 2.0.0b60
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# HashFunction

**Package:** `flyte.io`

A hash method that wraps a user-provided function to compute hashes.

This class allows you to define custom hashing logic by providing a callable
that takes data and returns a hash string. It implements the HashMethod protocol,
making it compatible with Flyte's hashing infrastructure.

Example:
    &gt;&gt;&gt; def my_hash(data: bytes) -&gt; str:
    ...     return hashlib.md5(data).hexdigest()
    &gt;&gt;&gt; hash_fn = HashFunction.from_fn(my_hash)
    &gt;&gt;&gt; hash_fn.update(b"hello")
    &gt;&gt;&gt; hash_fn.result()
    '5d41402abc4b2a76b9719d911017c592'

Attributes:
    _fn: The callable that computes the hash from input data.
    _value: The most recently computed hash value.



```python
class HashFunction(
    fn: Callable[[Any], str],
)
```
Initialize a HashFunction with a custom hash callable.



| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[[Any], str]` | A callable that takes data of any type and returns a hash string. |

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

### reset()

```python
def reset()
```
### result()

```python
def result()
```
Return the most recently computed hash value.

Returns:
    The hash string from the last call to update().


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

