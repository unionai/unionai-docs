---
title: flyteplugins.papermill
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# flyteplugins.papermill

## Directory

### Classes

| Class | Description |
|-|-|
| [`NotebookTask`](../flyteplugins.papermill/notebooktask) | A Flyte task that executes a Jupyter notebook via Papermill. |

### Methods

| Method | Description |
|-|-|
| [`load_dataframe()`](#load_dataframe) | Load a ``flyte. |
| [`load_dir()`](#load_dir) | Load a ``flyte. |
| [`load_file()`](#load_file) | Load a ``flyte. |
| [`record_outputs()`](#record_outputs) | Record output values from a notebook for use by downstream Flyte tasks. |


## Methods

#### load_dataframe()

```python
def load_dataframe(
    uri: str,
    fmt: str,
)
```
Load a ``flyte.io.DataFrame`` from a serialized URI inside a notebook.

When a ``DataFrame`` is passed as an input to a ``NotebookTask``, it is
serialized to its remote URI for papermill injection.  Use this helper
to reconstruct it::

    from flyteplugins.papermill import load_dataframe

    df = load_dataframe(my_df_uri)
    pandas_df = df.all()  # materializes as pandas DataFrame



| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | The remote URI string (injected as a papermill parameter). |
| `fmt` | `str` | The storage format (default ``"parquet"``). |

**Returns:** A ``flyte.io.DataFrame`` instance pointing at the remote URI.

#### load_dir()

```python
def load_dir(
    path: str,
)
```
Load a ``flyte.io.Dir`` from a serialized path inside a notebook.

When a ``Dir`` is passed as an input to a ``NotebookTask``, it is
serialized to its remote path string.  Use this helper to
reconstruct it::

    from flyteplugins.papermill import load_dir

    d = load_dir(my_dir_path)



| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | The remote path string (injected as a papermill parameter). |

**Returns:** A ``flyte.io.Dir`` instance pointing at the remote path.

#### load_file()

```python
def load_file(
    path: str,
)
```
Load a ``flyte.io.File`` from a serialized path inside a notebook.

When a ``File`` is passed as an input to a ``NotebookTask``, it is
serialized to its remote path string for papermill injection.  Use
this helper to reconstruct the ``File`` object inside the notebook::

    from flyteplugins.papermill import load_file

    f = load_file(my_file_path)  # my_file_path injected by papermill
    with f.open_sync() as fh:
        data = fh.read()



| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | The remote path string (injected as a papermill parameter). |

**Returns:** A ``flyte.io.File`` instance pointing at the remote path.

#### record_outputs()

```python
def record_outputs(
    kwargs: **kwargs,
) -> str
```
Record output values from a notebook for use by downstream Flyte tasks.

Call this as the **last expression** in a cell tagged ``"outputs"``.
The returned protobuf text is captured by Jupyter as the cell output
and later extracted by ``NotebookTask``.

Values are serialized as Flyte Literals, so any type supported by
Flyte's type system works — primitives, ``File``, ``Dir``,
``DataFrame``, dataclasses, etc.

Example (cell tagged ``"outputs"``)::

    from flyteplugins.papermill import record_outputs

    record_outputs(result=42, summary="done")



| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

**Returns**

Protobuf text representation of a ``LiteralMap``. Jupyter captures
this as the cell's text/plain output.

