---
title: flytekit.remote.remote_fs
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.remote_fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteFS`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytefs) | Want this to behave mostly just like the HTTP file system. |
| [`FlytePathResolver`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) | None. |
| [`HTTPFileSystem`](.././flytekit.remote.remote_fs#flytekitremoteremote_fshttpfilesystem) | Simple File-System for fetching data via HTTP(S). |
| [`HttpFileWriter`](.././flytekit.remote.remote_fs#flytekitremoteremote_fshttpfilewriter) | Convenient class to derive from to provide buffering. |
| [`NoOpCallback`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsnoopcallback) | This implementation of Callback does exactly nothing. |
| [`UUID`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsuuid) | Instances of the UUID class represent UUIDs as specified in RFC 4122. |

## flytekit.remote.remote_fs.FlytePathResolver

### Methods

| Method | Description |
|-|-|
| [`add_mapping()`](#add_mapping) | Thread safe method to dd a mapping from a flyte uri to a remote path |
| [`resolve_remote_path()`](#resolve_remote_path) | Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None |


#### add_mapping()

```python
def add_mapping(
    flyte_uri: str,
    remote_path: str,
):
```
Thread safe method to dd a mapping from a flyte uri to a remote path


| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |
| `remote_path` | `str` |

#### resolve_remote_path()

```python
def resolve_remote_path(
    flyte_uri: str,
):
```
Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None


| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |

## flytekit.remote.remote_fs.NoOpCallback

This implementation of Callback does exactly nothing


```python
def NoOpCallback(
    size,
    value,
    hooks,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `size` |  |
| `value` |  |
| `hooks` |  |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute_update()`](#absolute_update) | Set the internal value state |
| [`as_callback()`](#as_callback) | Transform callback= |
| [`branch()`](#branch) | Set callbacks for child transfers |
| [`branch_coro()`](#branch_coro) | Wraps a coroutine, and pass a new child callback to it |
| [`branched()`](#branched) | Return callback for child transfers |
| [`call()`](#call) | Execute hook(s) with current state |
| [`close()`](#close) | Close callback |
| [`no_op()`](#no_op) | None |
| [`relative_update()`](#relative_update) | Delta increment the internal counter |
| [`set_size()`](#set_size) | Set the internal maximum size attribute |
| [`wrap()`](#wrap) | Wrap an iterable to call ``relative_update`` on each iterations |


#### absolute_update()

```python
def absolute_update(
    value,
):
```
Set the internal value state

Triggers ``call()``

Parameters
----------
value: int


| Parameter | Type |
|-|-|
| `value` |  |

#### as_callback()

```python
def as_callback(
    maybe_callback,
):
```
Transform callback=... into Callback instance

For the special value of ``None``, return the global instance of
``NoOpCallback``. This is an alternative to including
``callback=DEFAULT_CALLBACK`` directly in a method signature.


| Parameter | Type |
|-|-|
| `maybe_callback` |  |

#### branch()

```python
def branch(
    path_1,
    path_2,
    kwargs,
):
```
Set callbacks for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The passed kwargs are
to be *mutated* to add ``callback=``, if this class supports branching
to children.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
kwargs: dict
arguments passed to child method, e.g., put_file.

Returns
-------


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### branch_coro()

```python
def branch_coro(
    fn,
):
```
Wraps a coroutine, and pass a new child callback to it.


| Parameter | Type |
|-|-|
| `fn` |  |

#### branched()

```python
def branched(
    path_1,
    path_2,
    kwargs,
):
```
Return callback for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The function returns a callback
that has to be passed to the child method, e.g., put_file,
as `callback=` argument.

The implementation uses `callback.branch` for compatibility.
When implementing callbacks, it is recommended to override this function instead
of `branch` and avoid calling `super().branched(...)`.

Prefer using this function over `branch`.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
**kwargs:
Arbitrary keyword arguments

Returns
-------
callback: Callback
A callback instance to be passed to the child method


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### call()

```python
def call(
    args,
    kwargs,
):
```
Execute hook(s) with current state

Each function is passed the internal size and current value

Parameters
----------
hook_name: str or None
If given, execute on this hook
kwargs: passed on to (all) hook(s)


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### close()

```python
def close()
```
Close callback.


#### no_op()

```python
def no_op(
    _,
    __,
):
```
| Parameter | Type |
|-|-|
| `_` |  |
| `__` |  |

#### relative_update()

```python
def relative_update(
    inc,
):
```
Delta increment the internal counter

Triggers ``call()``

Parameters
----------
inc: int


| Parameter | Type |
|-|-|
| `inc` |  |

#### set_size()

```python
def set_size(
    size,
):
```
Set the internal maximum size attribute

Usually called if not initially set at instantiation. Note that this
triggers a ``call()``.

Parameters
----------
size: int


| Parameter | Type |
|-|-|
| `size` |  |

#### wrap()

```python
def wrap(
    iterable,
):
```
Wrap an iterable to call ``relative_update`` on each iterations

Parameters
----------
iterable: Iterable
The iterable that is being wrapped


| Parameter | Type |
|-|-|
| `iterable` |  |

## flytekit.remote.remote_fs.UUID

Instances of the UUID class represent UUIDs as specified in RFC 4122.
UUID objects are immutable, hashable, and usable as dictionary keys.
Converting a UUID to a string with str() yields something in the form
'12345678-1234-1234-1234-123456789abc'.  The UUID constructor accepts
five possible forms: a similar string of hexadecimal digits, or a tuple
of six integer fields (with 32-bit, 16-bit, 16-bit, 8-bit, 8-bit, and
48-bit values respectively) as an argument named 'fields', or a string
of 16 bytes (with all the integer fields in big-endian order) as an
argument named 'bytes', or a string of 16 bytes (with the first three
fields in little-endian order) as an argument named 'bytes_le', or a
single 128-bit integer as an argument named 'int'.

UUIDs have these read-only attributes:

bytes       the UUID as a 16-byte string (containing the six
integer fields in big-endian byte order)

bytes_le    the UUID as a 16-byte string (with time_low, time_mid,
and time_hi_version in little-endian byte order)

fields      a tuple of the six integer fields of the UUID,
which are also available as six individual attributes
and two derived attributes:

time_low                the first 32 bits of the UUID
time_mid                the next 16 bits of the UUID
time_hi_version         the next 16 bits of the UUID
clock_seq_hi_variant    the next 8 bits of the UUID
clock_seq_low           the next 8 bits of the UUID
node                    the last 48 bits of the UUID

time                    the 60-bit timestamp
clock_seq               the 14-bit sequence number

hex         the UUID as a 32-character hexadecimal string

int         the UUID as a 128-bit integer

urn         the UUID as a URN as specified in RFC 4122

variant     the UUID variant (one of the constants RESERVED_NCS,
RFC_4122, RESERVED_MICROSOFT, or RESERVED_FUTURE)

version     the UUID version number (1 through 5, meaningful only
when the variant is RFC_4122)

is_safe     An enum indicating whether the UUID has been generated in
a way that is safe for multiprocessing applications, via
uuid_generate_time_safe(3).


```python
def UUID(
    hex,
    bytes,
    bytes_le,
    fields,
    int,
    version,
    is_safe,
):
```
Create a UUID from either a string of 32 hexadecimal digits,
a string of 16 bytes as the 'bytes' argument, a string of 16 bytes
in little-endian order as the 'bytes_le' argument, a tuple of six
integers (32-bit time_low, 16-bit time_mid, 16-bit time_hi_version,
8-bit clock_seq_hi_variant, 8-bit clock_seq_low, 48-bit node) as
the 'fields' argument, or a single 128-bit integer as the 'int'
argument.  When a string of hex digits is given, curly braces,
hyphens, and a URN prefix are all optional.  For example, these
expressions all yield the same UUID:

UUID('{12345678-1234-5678-1234-567812345678}')
UUID('12345678123456781234567812345678')
UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
UUID(bytes='\x12\x34\x56\x78'*4)
UUID(bytes_le='\x78\x56\x34\x12\x34\x12\x78\x56' +
'\x12\x34\x56\x78\x12\x34\x56\x78')
UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
UUID(int=0x12345678123456781234567812345678)

Exactly one of 'hex', 'bytes', 'bytes_le', 'fields', or 'int' must
be given.  The 'version' argument is optional; if given, the resulting
UUID will have its variant and version set according to RFC 4122,
overriding the given 'hex', 'bytes', 'bytes_le', 'fields', or 'int'.

is_safe is an enum exposed as an attribute on the instance.  It
indicates whether the UUID has been generated in a way that is safe
for multiprocessing applications, via uuid_generate_time_safe(3).


| Parameter | Type |
|-|-|
| `hex` |  |
| `bytes` |  |
| `bytes_le` |  |
| `fields` |  |
| `int` |  |
| `version` |  |
| `is_safe` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| bytes |  |  |
| bytes_le |  |  |
| clock_seq |  |  |
| clock_seq_hi_variant |  |  |
| clock_seq_low |  |  |
| fields |  |  |
| hex |  |  |
| node |  |  |
| time |  |  |
| time_hi_version |  |  |
| time_low |  |  |
| time_mid |  |  |
| urn |  |  |
| variant |  |  |
| version |  |  |

