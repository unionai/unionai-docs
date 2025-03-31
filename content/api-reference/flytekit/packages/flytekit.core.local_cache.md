---
title: flytekit.core.local_cache
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.local_cache

## Directory

### Classes

| Class | Description |
|-|-|
| [`Cache`](.././flytekit.core.local_cache#flytekitcorelocal_cachecache) | Disk and file backed cache. |
| [`Literal`](.././flytekit.core.local_cache#flytekitcorelocal_cacheliteral) |  |
| [`LiteralCollection`](.././flytekit.core.local_cache#flytekitcorelocal_cacheliteralcollection) |  |
| [`LiteralMap`](.././flytekit.core.local_cache#flytekitcorelocal_cacheliteralmap) | A ProtocolMessage. |
| [`LocalTaskCache`](.././flytekit.core.local_cache#flytekitcorelocal_cachelocaltaskcache) | This class implements a persistent store able to cache the result of local task executions. |
| [`ModelLiteralMap`](.././flytekit.core.local_cache#flytekitcorelocal_cachemodelliteralmap) |  |

### Methods

| Method | Description |
|-|-|
| [`_calculate_cache_key()`](#_calculate_cache_key) |  |
| [`_recursive_hash_placement()`](#_recursive_hash_placement) |  |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CACHE_LOCATION` | `str` |  |

## Methods

#### _calculate_cache_key()

```python
def _calculate_cache_key(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
) -> str
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `cache_version` | `str` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |

#### _recursive_hash_placement()

```python
def _recursive_hash_placement(
    literal: flytekit.models.literals.Literal,
) -> flytekit.models.literals.Literal
```
| Parameter | Type |
|-|-|
| `literal` | `flytekit.models.literals.Literal` |

#### lazy_module()

```python
def lazy_module(
    fullname,
)
```
This function is used to lazily import modules.  It is used in the following way:
.. code-block:: python
from flytekit.lazy_import import lazy_module
sklearn = lazy_module("sklearn")
sklearn.svm.SVC()


| Parameter | Type |
|-|-|
| `fullname` |  |

## flytekit.core.local_cache.Cache

Disk and file backed cache.


```python
class Cache(
    directory,
    timeout,
    disk,
    settings,
)
```
Initialize cache instance.



| Parameter | Type |
|-|-|
| `directory` |  |
| `timeout` |  |
| `disk` |  |
| `settings` |  |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) | Add `key` and `value` item to cache. |
| [`check()`](#check) | Check database and file system consistency. |
| [`clear()`](#clear) | Remove all items from cache. |
| [`close()`](#close) | Close database connection. |
| [`create_tag_index()`](#create_tag_index) | Create tag index on cache database. |
| [`cull()`](#cull) | Cull items from cache until volume is less than size limit. |
| [`decr()`](#decr) | Decrement value by delta for item with key. |
| [`delete()`](#delete) | Delete corresponding item for `key` from cache. |
| [`drop_tag_index()`](#drop_tag_index) | Drop tag index on cache database. |
| [`evict()`](#evict) | Remove items with matching `tag` from cache. |
| [`expire()`](#expire) | Remove expired items from cache. |
| [`get()`](#get) | Retrieve value from cache. |
| [`incr()`](#incr) | Increment value by delta for item with key. |
| [`iterkeys()`](#iterkeys) | Iterate Cache keys in database sort order. |
| [`memoize()`](#memoize) | Memoizing cache decorator. |
| [`peek()`](#peek) | Peek at key and value item pair from `side` of queue in cache. |
| [`peekitem()`](#peekitem) | Peek at key and value item pair in cache based on iteration order. |
| [`pop()`](#pop) | Remove corresponding item for `key` from cache and return value. |
| [`pull()`](#pull) | Pull key and value item pair from `side` of queue in cache. |
| [`push()`](#push) | Push `value` onto `side` of queue identified by `prefix` in cache. |
| [`read()`](#read) | Return file handle value corresponding to `key` from cache. |
| [`reset()`](#reset) | Reset `key` and `value` item from Settings table. |
| [`set()`](#set) | Set `key` and `value` item in cache. |
| [`stats()`](#stats) | Return cache statistics hits and misses. |
| [`touch()`](#touch) | Touch `key` in cache and update `expire` time. |
| [`transact()`](#transact) | Context manager to perform a transaction by locking the cache. |
| [`volume()`](#volume) | Return estimated total size of cache on disk. |


#### add()

```python
def add(
    key,
    value,
    expire,
    read,
    tag,
    retry,
)
```
Add `key` and `value` item to cache.

Similar to `set`, but only add to cache if key not present.

Operation is atomic. Only one concurrent add operation for a given key
will succeed.

When `read` is `True`, `value` should be a file-like object opened
for reading in binary mode.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |
| `expire` |  |
| `read` |  |
| `tag` |  |
| `retry` |  |

#### check()

```python
def check(
    fix,
    retry,
)
```
Check database and file system consistency.

Intended for use in testing and post-mortem error analysis.

While checking the Cache table for consistency, a writer lock is held
on the database. The lock blocks other cache clients from writing to
the database. For caches with many file references, the lock may be
held for a long time. For example, local benchmarking shows that a
cache with 1,000 file references takes ~60ms to check.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `fix` |  |
| `retry` |  |

#### clear()

```python
def clear(
    retry,
)
```
Remove all items from cache.

Removing items is an iterative process. In each iteration, a subset of
items is removed. Concurrent writes may occur between iterations.

If a :exc:`Timeout` occurs, the first element of the exception's
`args` attribute will be the number of items removed before the
exception occurred.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `retry` |  |

#### close()

```python
def close()
```
Close database connection.


#### create_tag_index()

```python
def create_tag_index()
```
Create tag index on cache database.

It is better to initialize cache with `tag_index=True` than use this.

:raises Timeout: if database timeout occurs


#### cull()

```python
def cull(
    retry,
)
```
Cull items from cache until volume is less than size limit.

Removing items is an iterative process. In each iteration, a subset of
items is removed. Concurrent writes may occur between iterations.

If a :exc:`Timeout` occurs, the first element of the exception's
`args` attribute will be the number of items removed before the
exception occurred.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `retry` |  |

#### decr()

```python
def decr(
    key,
    delta,
    default,
    retry,
)
```
Decrement value by delta for item with key.

If key is missing and default is None then raise KeyError. Else if key
is missing and default is not None then use default for value.

Operation is atomic. All concurrent decrement operations will be
counted individually.

Unlike Memcached, negative values are supported. Value may be
decremented below zero.

Assumes value may be stored in a SQLite column. Most builds that target
machines with 64-bit pointer widths will support 64-bit signed
integers.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `delta` |  |
| `default` |  |
| `retry` |  |

#### delete()

```python
def delete(
    key,
    retry,
)
```
Delete corresponding item for `key` from cache.

Missing keys are ignored.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `retry` |  |

#### drop_tag_index()

```python
def drop_tag_index()
```
Drop tag index on cache database.

:raises Timeout: if database timeout occurs


#### evict()

```python
def evict(
    tag,
    retry,
)
```
Remove items with matching `tag` from cache.

Removing items is an iterative process. In each iteration, a subset of
items is removed. Concurrent writes may occur between iterations.

If a :exc:`Timeout` occurs, the first element of the exception's
`args` attribute will be the number of items removed before the
exception occurred.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `tag` |  |
| `retry` |  |

#### expire()

```python
def expire(
    now,
    retry,
)
```
Remove expired items from cache.

Removing items is an iterative process. In each iteration, a subset of
items is removed. Concurrent writes may occur between iterations.

If a :exc:`Timeout` occurs, the first element of the exception's
`args` attribute will be the number of items removed before the
exception occurred.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `now` |  |
| `retry` |  |

#### get()

```python
def get(
    key,
    default,
    read,
    expire_time,
    tag,
    retry,
)
```
Retrieve value from cache. If `key` is missing, return `default`.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |
| `read` |  |
| `expire_time` |  |
| `tag` |  |
| `retry` |  |

#### incr()

```python
def incr(
    key,
    delta,
    default,
    retry,
)
```
Increment value by delta for item with key.

If key is missing and default is None then raise KeyError. Else if key
is missing and default is not None then use default for value.

Operation is atomic. All concurrent increment operations will be
counted individually.

Assumes value may be stored in a SQLite column. Most builds that target
machines with 64-bit pointer widths will support 64-bit signed
integers.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `delta` |  |
| `default` |  |
| `retry` |  |

#### iterkeys()

```python
def iterkeys(
    reverse,
)
```
Iterate Cache keys in database sort order.

>>> cache = Cache()
>>> for key in [4, 1, 3, 0, 2]:
...     cache[key] = key
>>> list(cache.iterkeys())
[0, 1, 2, 3, 4]
>>> list(cache.iterkeys(reverse=True))
[4, 3, 2, 1, 0]



| Parameter | Type |
|-|-|
| `reverse` |  |

#### memoize()

```python
def memoize(
    name,
    typed,
    expire,
    tag,
    ignore,
)
```
Memoizing cache decorator.

Decorator to wrap callable with memoizing function using cache.
Repeated calls with the same arguments will lookup result in cache and
avoid function evaluation.

If name is set to None (default), the callable name will be determined
automatically.

When expire is set to zero, function results will not be set in the
cache. Cache lookups still occur, however. Read
:doc:`case-study-landing-page-caching` for example usage.

If typed is set to True, function arguments of different types will be
cached separately. For example, f(3) and f(3.0) will be treated as
distinct calls with distinct results.

The original underlying function is accessible through the __wrapped__
attribute. This is useful for introspection, for bypassing the cache,
or for rewrapping the function with a different cache.

>>> from diskcache import Cache
>>> cache = Cache()
>>> @cache.memoize(expire=1, tag='fib')
... def fibonacci(number):
...     if number == 0:
...         return 0
...     elif number == 1:
...         return 1
...     else:
...         return fibonacci(number - 1) + fibonacci(number - 2)
>>> print(fibonacci(100))
354224848179261915075

An additional `__cache_key__` attribute can be used to generate the
cache key used for the given arguments.

>>> key = fibonacci.__cache_key__(100)
>>> print(cache[key])
354224848179261915075

Remember to call memoize when decorating a callable. If you forget,
then a TypeError will occur. Note the lack of parenthenses after
memoize below:

>>> @cache.memoize
... def test():
...     pass
Traceback (most recent call last):
...
TypeError: name cannot be callable



| Parameter | Type |
|-|-|
| `name` |  |
| `typed` |  |
| `expire` |  |
| `tag` |  |
| `ignore` |  |

#### peek()

```python
def peek(
    prefix,
    default,
    side,
    expire_time,
    tag,
    retry,
)
```
Peek at key and value item pair from `side` of queue in cache.

When prefix is None, integer keys are used. Otherwise, string keys are
used in the format "prefix-integer". Integer starts at 500 trillion.

If queue is empty, return default.

Defaults to peeking at key and value item pairs from front of queue.
Set side to 'back' to pull from back of queue. Side must be one of
'front' or 'back'.

Expired items are deleted from cache. Operation is atomic. Concurrent
operations will be serialized.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).

See also `Cache.pull` and `Cache.push`.

>>> cache = Cache()
>>> for letter in 'abc':
...     print(cache.push(letter))
500000000000000
500000000000001
500000000000002
>>> key, value = cache.peek()
>>> print(key)
500000000000000
>>> value
'a'
>>> key, value = cache.peek(side='back')
>>> print(key)
500000000000002
>>> value
'c'



| Parameter | Type |
|-|-|
| `prefix` |  |
| `default` |  |
| `side` |  |
| `expire_time` |  |
| `tag` |  |
| `retry` |  |

#### peekitem()

```python
def peekitem(
    last,
    expire_time,
    tag,
    retry,
)
```
Peek at key and value item pair in cache based on iteration order.

Expired items are deleted from cache. Operation is atomic. Concurrent
operations will be serialized.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).

>>> cache = Cache()
>>> for num, letter in enumerate('abc'):
...     cache[letter] = num
>>> cache.peekitem()
('c', 2)
>>> cache.peekitem(last=False)
('a', 0)



| Parameter | Type |
|-|-|
| `last` |  |
| `expire_time` |  |
| `tag` |  |
| `retry` |  |

#### pop()

```python
def pop(
    key,
    default,
    expire_time,
    tag,
    retry,
)
```
Remove corresponding item for `key` from cache and return value.

If `key` is missing, return `default`.

Operation is atomic. Concurrent operations will be serialized.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |
| `expire_time` |  |
| `tag` |  |
| `retry` |  |

#### pull()

```python
def pull(
    prefix,
    default,
    side,
    expire_time,
    tag,
    retry,
)
```
Pull key and value item pair from `side` of queue in cache.

When prefix is None, integer keys are used. Otherwise, string keys are
used in the format "prefix-integer". Integer starts at 500 trillion.

If queue is empty, return default.

Defaults to pulling key and value item pairs from front of queue. Set
side to 'back' to pull from back of queue. Side must be one of 'front'
or 'back'.

Operation is atomic. Concurrent operations will be serialized.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).

See also `Cache.push` and `Cache.get`.

>>> cache = Cache()
>>> cache.pull()
(None, None)
>>> for letter in 'abc':
...     print(cache.push(letter))
500000000000000
500000000000001
500000000000002
>>> key, value = cache.pull()
>>> print(key)
500000000000000
>>> value
'a'
>>> _, value = cache.pull(side='back')
>>> value
'c'
>>> cache.push(1234, 'userids')
'userids-500000000000000'
>>> _, value = cache.pull('userids')
>>> value
1234



| Parameter | Type |
|-|-|
| `prefix` |  |
| `default` |  |
| `side` |  |
| `expire_time` |  |
| `tag` |  |
| `retry` |  |

#### push()

```python
def push(
    value,
    prefix,
    side,
    expire,
    read,
    tag,
    retry,
)
```
Push `value` onto `side` of queue identified by `prefix` in cache.

When prefix is None, integer keys are used. Otherwise, string keys are
used in the format "prefix-integer". Integer starts at 500 trillion.

Defaults to pushing value on back of queue. Set side to 'front' to push
value on front of queue. Side must be one of 'back' or 'front'.

Operation is atomic. Concurrent operations will be serialized.

When `read` is `True`, `value` should be a file-like object opened
for reading in binary mode.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).

See also `Cache.pull`.

>>> cache = Cache()
>>> print(cache.push('first value'))
500000000000000
>>> cache.get(500000000000000)
'first value'
>>> print(cache.push('second value'))
500000000000001
>>> print(cache.push('third value', side='front'))
499999999999999
>>> cache.push(1234, prefix='userids')
'userids-500000000000000'



| Parameter | Type |
|-|-|
| `value` |  |
| `prefix` |  |
| `side` |  |
| `expire` |  |
| `read` |  |
| `tag` |  |
| `retry` |  |

#### read()

```python
def read(
    key,
    retry,
)
```
Return file handle value corresponding to `key` from cache.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `retry` |  |

#### reset()

```python
def reset(
    key,
    value,
    update,
)
```
Reset `key` and `value` item from Settings table.

Use `reset` to update the value of Cache settings correctly. Cache
settings are stored in the Settings table of the SQLite database. If
`update` is ``False`` then no attempt is made to update the database.

If `value` is not given, it is reloaded from the Settings
table. Otherwise, the Settings table is updated.

Settings with the ``disk_`` prefix correspond to Disk
attributes. Updating the value will change the unprefixed attribute on
the associated Disk instance.

Settings with the ``sqlite_`` prefix correspond to SQLite
pragmas. Updating the value will execute the corresponding PRAGMA
statement.

SQLite PRAGMA statements may be executed before the Settings table
exists in the database by setting `update` to ``False``.



| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |
| `update` |  |

#### set()

```python
def set(
    key,
    value,
    expire,
    read,
    tag,
    retry,
)
```
Set `key` and `value` item in cache.

When `read` is `True`, `value` should be a file-like object opened
for reading in binary mode.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `value` |  |
| `expire` |  |
| `read` |  |
| `tag` |  |
| `retry` |  |

#### stats()

```python
def stats(
    enable,
    reset,
)
```
Return cache statistics hits and misses.



| Parameter | Type |
|-|-|
| `enable` |  |
| `reset` |  |

#### touch()

```python
def touch(
    key,
    expire,
    retry,
)
```
Touch `key` in cache and update `expire` time.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).



| Parameter | Type |
|-|-|
| `key` |  |
| `expire` |  |
| `retry` |  |

#### transact()

```python
def transact(
    retry,
)
```
Context manager to perform a transaction by locking the cache.

While the cache is locked, no other write operation is permitted.
Transactions should therefore be as short as possible. Read and write
operations performed in a transaction are atomic. Read operations may
occur concurrent to a transaction.

Transactions may be nested and may not be shared between threads.

Raises :exc:`Timeout` error when database timeout occurs and `retry` is
`False` (default).

>>> cache = Cache()
>>> with cache.transact():  # Atomically increment two keys.
...     _ = cache.incr('total', 123.4)
...     _ = cache.incr('count', 1)
>>> with cache.transact():  # Atomically calculate average.
...     average = cache['total'] / cache['count']
>>> average
123.4



| Parameter | Type |
|-|-|
| `retry` |  |

#### volume()

```python
def volume()
```
Return estimated total size of cache on disk.

:return: size in bytes


### Properties

| Property | Type | Description |
|-|-|-|
| `directory` |  | {{< multiline >}}Cache directory.
{{< /multiline >}} |
| `disk` |  | {{< multiline >}}Disk used for serialization.
{{< /multiline >}} |
| `timeout` |  | {{< multiline >}}SQLite connection timeout value in seconds.
{{< /multiline >}} |

## flytekit.core.local_cache.Literal

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type |
|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `hash` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type |
|-|-|
| `metadata` | `typing.Dict[str, str]` |

#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.core.local_cache.LiteralCollection

```python
class LiteralCollection(
    literals,
)
```
| Parameter | Type |
|-|-|
| `literals` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LiteralCollection
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `literals` |  |  |

## flytekit.core.local_cache.LiteralMap

A ProtocolMessage


## flytekit.core.local_cache.LocalTaskCache

This class implements a persistent store able to cache the result of local task executions.


### Methods

| Method | Description |
|-|-|
| [`clear()`](#clear) |  |
| [`get()`](#get) |  |
| [`initialize()`](#initialize) |  |
| [`set()`](#set) |  |


#### clear()

```python
def clear()
```
#### get()

```python
def get(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
) -> typing.Optional[flytekit.models.literals.LiteralMap]
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `cache_version` | `str` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |

#### initialize()

```python
def initialize()
```
#### set()

```python
def set(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
    value: flytekit.models.literals.LiteralMap,
)
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `cache_version` | `str` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |
| `value` | `flytekit.models.literals.LiteralMap` |

## flytekit.core.local_cache.ModelLiteralMap

```python
class ModelLiteralMap(
    literals,
)
```
| Parameter | Type |
|-|-|
| `literals` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> LiteralMap
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `literals` |  | {{< multiline >}}A dictionary mapping Text key names to Literal objects.
{{< /multiline >}} |

