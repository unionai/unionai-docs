---
title: FileSystem
description: "File access inside a sandbox (``sb.fs``)."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# FileSystem

**Package:** `flyteplugins.union.sandbox`

File access inside a sandbox (``sb.fs``). Relative paths are under ``/work``.


## Parameters

```python
class FileSystem(
    client: Callable[[], Awaitable[SandboxClient]],
    explain: Callable[[BaseException], Awaitable[BaseException]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` | `Callable[[], Awaitable[SandboxClient]]` | |
| `explain` | `Callable[[BaseException], Awaitable[BaseException]]` | |

## Methods

| Method | Description |
|-|-|
| [`download()`](#download) | Copies ``src`` from the sandbox to the local path ``dst``; returns ``dst``. |
| [`download_dir()`](#download_dir) | Copies the tree under ``src`` in the sandbox to the local directory ``dst``, several files at once; returns ``dst``. |
| [`exists()`](#exists) |  |
| [`ls()`](#ls) | Entries of one directory (default ``/work``), sorted by name; not recursive. |
| [`mkdir()`](#mkdir) | Creates the directory ``path`` and any missing parents; nothing if it exists (``mkdir -p``): an existing directory keeps its mode. |
| [`read_bytes()`](#read_bytes) | Raises ``FileNotFoundError`` if ``path`` doesn't exist. |
| [`read_text()`](#read_text) | ``path`` decoded as UTF-8. |
| [`rm()`](#rm) | Removes a file, symlink or empty directory; ``recursive=True`` for a directory and its contents. |
| [`stat()`](#stat) | Raises ``FileNotFoundError`` if ``path`` doesn't exist. |
| [`upload()`](#upload) | Copies the local file ``src`` to ``dst`` in the sandbox. |
| [`upload_dir()`](#upload_dir) | Copies the local directory ``src`` to ``dst`` in the sandbox (its contents go under ``dst``), several files at once. |
| [`write_bytes()`](#write_bytes) | Writes ``data`` to ``path``, replacing it, and creating its parent directories. |
| [`write_text()`](#write_text) | Writes ``text`` (UTF-8) to ``path``, replacing it, and creating its parent directories. |


### download()

```python
def download(
    src: str,
    dst: str | os.PathLike,
) -> Path
```
Copies ``src`` from the sandbox to the local path ``dst``; returns ``dst``.


| Parameter | Type | Description |
|-|-|-|
| `src` | `str` | |
| `dst` | `str \| os.PathLike` | |

### download_dir()

```python
def download_dir(
    src: str,
    dst: str | os.PathLike,
) -> Path
```
Copies the tree under ``src`` in the sandbox to the local directory
``dst``, several files at once; returns ``dst``. Only plain names from
the sandbox are written, all under ``dst``.


| Parameter | Type | Description |
|-|-|-|
| `src` | `str` | |
| `dst` | `str \| os.PathLike` | |

### exists()

```python
def exists(
    path: str,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### ls()

```python
def ls(
    path: str = '.',
) -> list[FileEntry]
```
Entries of one directory (default ``/work``), sorted by name; not recursive.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### mkdir()

```python
def mkdir(
    path: str,
    mode: int = 493,
)
```
Creates the directory ``path`` and any missing parents; nothing if it
exists (``mkdir -p``): an existing directory keeps its mode.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `mode` | `int` | |

### read_bytes()

```python
def read_bytes(
    path: str,
) -> bytes
```
Raises ``FileNotFoundError`` if ``path`` doesn't exist.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### read_text()

```python
def read_text(
    path: str,
) -> str
```
``path`` decoded as UTF-8. Raises ``FileNotFoundError`` if it doesn't exist.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### rm()

```python
def rm(
    path: str,
    recursive: bool = False,
)
```
Removes a file, symlink or empty directory; ``recursive=True`` for a directory and its contents.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `recursive` | `bool` | |

### stat()

```python
def stat(
    path: str,
) -> FileEntry
```
Raises ``FileNotFoundError`` if ``path`` doesn't exist.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### upload()

```python
def upload(
    src: str | os.PathLike,
    dst: str,
)
```
Copies the local file ``src`` to ``dst`` in the sandbox. A file over
512 MiB raises ``ValueError`` before it is read.


| Parameter | Type | Description |
|-|-|-|
| `src` | `str \| os.PathLike` | |
| `dst` | `str` | |

### upload_dir()

```python
def upload_dir(
    src: str | os.PathLike,
    dst: str,
)
```
Copies the local directory ``src`` to ``dst`` in the sandbox (its
contents go under ``dst``), several files at once. Each file is a call
of its own: for a tree of thousands, upload an archive and unpack it
with `Sandbox.run` instead.


| Parameter | Type | Description |
|-|-|-|
| `src` | `str \| os.PathLike` | |
| `dst` | `str` | |

### write_bytes()

```python
def write_bytes(
    path: str,
    data: bytes,
    mode: int = 420,
)
```
Writes ``data`` to ``path``, replacing it, and creating its parent
directories. At most `MAX_TRANSFER_BYTES`
(512 MiB) in one file: a larger one raises ``ValueError`` before it is sent.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `data` | `bytes` | |
| `mode` | `int` | |

### write_text()

```python
def write_text(
    path: str,
    text: str,
)
```
Writes ``text`` (UTF-8) to ``path``, replacing it, and creating its parent directories.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `text` | `str` | |

