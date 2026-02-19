---
title: HttpFileWriter
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# HttpFileWriter

**Package:** `flytekit.remote.remote_fs`

```python
class HttpFileWriter(
    remote: FlyteRemote,
    filename: str,
    kwargs,
)
```
Template for files with buffered reading and writing

Parameters
----------
fs: instance of FileSystem
path: str
    location in file-system
mode: str
    Normal file modes. Currently only 'wb', 'ab' or 'rb'. Some file
    systems may be read-only, and some may not support append.
block_size: int
    Buffer size for reading or writing, 'default' for class default
autocommit: bool
    Whether to write to final destination; may only impact what
    happens when file is being closed.
cache_type: {"readahead", "none", "mmap", "bytes"}, default "readahead"
    Caching policy in read mode. See the definitions in ``core``.
cache_options : dict
    Additional options passed to the constructor for the cache specified
    by `cache_type`.
size: int
    If given and in read mode, suppressed having to look up the file size
kwargs:
    Gets stored as self.kwargs


| Parameter | Type | Description |
|-|-|-|
| `remote` | `FlyteRemote` | |
| `filename` | `str` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `closed` | `None` |  |
| `details` | `None` |  |
| `full_name` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`close()`](#close) | Close file. |
| [`commit()`](#commit) | Move from temp to final destination. |
| [`discard()`](#discard) | Throw away temporary file. |
| [`flush()`](#flush) | Write buffered data to backend store. |
| [`info()`](#info) | File information about this path. |
| [`read()`](#read) | Return data from cache, or fetch pieces as necessary. |
| [`readable()`](#readable) | Whether opened for reading. |
| [`readinto()`](#readinto) | mirrors builtin file's readinto method. |
| [`readinto1()`](#readinto1) |  |
| [`readline()`](#readline) | Read until and including the first occurrence of newline character. |
| [`readlines()`](#readlines) | Return all data, split by the newline character, including the newline character. |
| [`readuntil()`](#readuntil) | Return data between current position and first occurrence of char. |
| [`seek()`](#seek) | Set current file location. |
| [`seekable()`](#seekable) | Whether is seekable (only in read mode). |
| [`tell()`](#tell) | Current file location. |
| [`writable()`](#writable) | Whether opened for writing. |
| [`write()`](#write) | Write data to buffer. |


### close()

```python
def close()
```
Close file

Finalizes writes, discards cache


### commit()

```python
def commit()
```
Move from temp to final destination


### discard()

```python
def discard()
```
Throw away temporary file


### flush()

```python
def flush(
    force,
)
```
Write buffered data to backend store.

Writes the current buffer, if it is larger than the block-size, or if
the file is being closed.

Parameters
----------
force: bool
    When closing, write the last block even if it is smaller than
    blocks are allowed to be. Disallows further writing to this file.


| Parameter | Type | Description |
|-|-|-|
| `force` |  | |

### info()

```python
def info()
```
File information about this path


### read()

```python
def read(
    length,
)
```
Return data from cache, or fetch pieces as necessary

Parameters
----------
length: int (-1)
    Number of bytes to read; if &lt;0, all remaining bytes.


| Parameter | Type | Description |
|-|-|-|
| `length` |  | |

### readable()

```python
def readable()
```
Whether opened for reading


### readinto()

```python
def readinto(
    b,
)
```
mirrors builtin file's readinto method

https://docs.python.org/3/library/io.html#io.RawIOBase.readinto


| Parameter | Type | Description |
|-|-|-|
| `b` |  | |

### readinto1()

```python
def readinto1(
    b,
)
```
| Parameter | Type | Description |
|-|-|-|
| `b` |  | |

### readline()

```python
def readline()
```
Read until and including the first occurrence of newline character

Note that, because of character encoding, this is not necessarily a
true line ending.


### readlines()

```python
def readlines()
```
Return all data, split by the newline character, including the newline character


### readuntil()

```python
def readuntil(
    char,
    blocks,
)
```
Return data between current position and first occurrence of char

char is included in the output, except if the end of the tile is
encountered first.

Parameters
----------
char: bytes
    Thing to find
blocks: None or int
    How much to read in each go. Defaults to file blocksize - which may
    mean a new read on every call.


| Parameter | Type | Description |
|-|-|-|
| `char` |  | |
| `blocks` |  | |

### seek()

```python
def seek(
    loc,
    whence,
)
```
Set current file location

Parameters
----------
loc: int
    byte location
whence: {0, 1, 2}
    from start of file, current location or end of file, resp.


| Parameter | Type | Description |
|-|-|-|
| `loc` |  | |
| `whence` |  | |

### seekable()

```python
def seekable()
```
Whether is seekable (only in read mode)


### tell()

```python
def tell()
```
Current file location


### writable()

```python
def writable()
```
Whether opened for writing


### write()

```python
def write(
    data,
)
```
Write data to buffer.

Buffer only sent on flush() or if buffer is greater than
or equal to blocksize.

Parameters
----------
data: bytes
    Set of bytes to be written.


| Parameter | Type | Description |
|-|-|-|
| `data` |  | |

