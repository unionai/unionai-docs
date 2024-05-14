# FlyteFile

## `FlyteFile` class

**Definition**

```{code-block} python
class FlyteFile(os.PathLike, typing.Generic[T])
```

**Import**

```{code-block} python
from flytekit.types.file import FlyteFile
```

**Constructor**

```{code-block} python
FlyteFile(path: typing.Union[str, os.PathLike],
          downloader: typing.Callable = noop,
          remote_path: typing.Optional[os.PathLike] = None)
```

**`path`**`: typing.Union[str, os.PathLike]` (_required_)\
The path to the source file from which to create the `FlyteFile`.
It may be a local path or a remote URI. In the vast majority of cases, this is the only parameter you need to initialize a `FlyteFile`.

**`downloader`**` : typing.Callable = noop` (_optional_)\
A custom download function (see below).

**`remote_path`**`: typing.Optional[os.PathLike] = None` (_optional_)\
A file path and name in a backing store. Used to override the default storage (see below).

**Attributes**

**`path`**`: typing.Union[str, os.PathLike]`\
The local (in-container) path to the file. If the `FlyteFile` was created in the current task from a local file, then this is simply the path to that file.
If the `FlyteFile` was passed in to the current task or was created in the current task from a remote file then this attribute will be `None` until `download`is successfully called on `FlyteFile`.
At that point, a random local path is generated for the downloaded file and that path is stored here.

**`remote_source`**`: str`\
If the `FlyteFile` was created from a remote source or passed into a task, the URI of the backing file is stored here.

**`remote_path`**`: typing.Optional[os.PathLike]`\
If a custom remote location was specified when the `FlyteFile` was created, it is stored here.

**`downloaded`**`: bool`\
If the `FlyteFile` was passed in to the current task or created in the current task from a remote source and downloaded then this attribute is `true`, otherwise it is `false`.

**Instance methods**

**`open`**`(mode: str, cache_type: typing.Optional[str] = None,`\
     `cache_options: typing.Optional[typing.Dict[str, typing.Any]]`\
     `= None) -> File`\
Opens the `FlyteFile` as a Python streaming `File` object. This method does not cause a download of a remote `FlyteFile` to occur.

**`download`**`() -> str`\
Triggers a download of a remote `FlyteFile`.

**`to_dict`**, **`to_json`**\
From `@dataclass_json`

**Class methods**

**`new_remote_file`**`(name: typing.Optional[str] = None) -> FlyteFile`\
Create a new `FlyteFile` with a remote source.

**`extension`**`()`\
Return the extension.

**`from_dict`**, **`from_json`**, **`schema`**\
From `@dataclass_json`

## Overview

In Flyte, each task runs in its own container.
One result is that a local file in one task will not automatically be available in other tasks, because it exists only inside the container where it was created.

To share a file across tasks it must be explicitly passed out of one task and into another within your workflow code.
To help with this, Flyte provides the [`FlyteFile`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.types.file.FlyteFile.html#flytekit-types-file-flytefile) Python class. Here is an example of how it works.

### Local file example

Let's say you have a local file in task `t1` that you want to make accessible in the next task, `t2`.
To do this, you create a `FlyteFile` object using the local path of the file you created, and then pass the `FlyteFile` object as part of your workflow, like this:

```{code-block} python
@task
def t1() -> FlyteFile:
    p = os.path.join(current_context().working_directory, "data.txt")
    f = open(p, mode="w")
    f.write("Here is some sample data.")
    f.close()
    return FlyteFile(p)

@task
def t2(ff: FlyteFile):
    ff.download()
    f = open(ff, mode="r")
    d = f.read()
    f.close()
    # do something with the data `d`

@workflow
def wf():
    ff = t1()
    t2(ff)
```

Recall that the code within a Flyte task function is real Python code (run in a Python interpreter inside the task container) while the code within a workflow function is actually a Python-like DSL, compiled by Flyte into a representation of the workflow.

This means that Flyte needs to handle the passing of the variable `ff` in `wf` from task `t1` to task `t2`. Of course, by design, the Flyte workflow engine knows how to handle values of type `FlyteFile`.
Here is what it does:

* The `FlyteFile` object was initialized with the local path of the file that you created.
* When the `FlyteFile` is passed out of `t1`, Flyte uploads the local file to a randomly generated location in your raw data store.
The URI of this location is used to initialize a Flyte object of type `Blob`.
* The `Blob` object is passed to `t2`.
Because the type of the input parameter is `FlyteFile`, Flyte converts the `Blob` back into a `FlyteFile` and sets the `remote_source` attribute of that `FlyteFile` to the URI of the `Blob` object.
* Inside `t2` you can now perform a `FlyteFile.download()` and then open the `FlyteFile`  as if it were a normal `file` object.

### Remote file example

In the example above we started with a local file.
To preserve that file across the task boundary, Flyte uploaded it to a remote location (in this case the system's dedicated blob store) before passing it to the next task, where it can be downloaded.

You can also _start with a remote file_, simply by initializing the `FlyteFile` object with a URI pointing to a remote source. For example:

```{code-block} python
@task
def t1() -> FlyteFile:
    p = "https://some/path/data.csv"
    return FlyteFile(p)

@task
def t2(ff: FlyteFile):
    ff.download()
    f = open(ff, mode="r")
    d = f.read()
    f.close()
    # do something with the data `d`

@workflow
def wf():
    ff = t1()
    t2(ff)@task
```

In this case, no uploading is needed. When the object is passed out of the task, it is simply converted into a `Blob` with the remote path as the URI.
After being passed to the next task, `FlyteFile.download()` can be called and the object opened as a file, just as before.

When initializing a `FlyteFile` with a remote file location, the URI schemes supported are: `http`, `https`, `gs`, `abfs`, `abfss`, and `file`.

### Specifying `remote_path`

When a `FlyteFile` based on a local file is passed out of a task, the file is uploaded, by default, to the default raw data store configured in your data plane.
In AWS-based systems, this is an S3 bucket, for example.

Within that bucket, the actual file location is, by default, a randomly generated path.
This path is guaranteed to be unique so that files are never over-written on subsequent runs of the task.

However,  the storage location used can be overridden by specifying the optional parameter `remote_path` when initializing the `FlyteFile` object.
The specified value must be the full URI of a writable location accessible from your Flyte cluster.
You can, for example, use the same S3 bucket that your cluster uses by default (the raw data store) but with a specified file name.

:::{note}

If you set`remote_path`then subsequent runs of the same task will overwrite the file.

:::

Here is an example

```{code-block} python
@task
def t1() -> FlyteFile:
    p = os.path.join(current_context().working_directory, "data.txt")
    f = open(p, mode="w")
    f.write("Here is some sample data.")
    f.close()
    return FlyteFile(p, remote_path="s3://union-contoso/foobar")

@task
def t2(ff: FlyteFile):
    # ff.remote_source == "s3://union-contoso/foobar"
    ff.download()
    f = open(ff, mode="r")
    d = f.read()
    f.close()
    # do something with the data `d`

@workflow
def wf():
    ff = t1()
    t2(ff)
```

:::{admonition} FlyteFile behavior triggered by different type hints

The examples above demonstrate the most common case:
**Both the output and input to tasks are declared as type`FlyteFile`and an actual`FlyteFile`object is, in fact, passed.**

Flyte also handles more convoluted cases (different return types, different parameter types, etc.).
These are described below.

:::

## Returning a file from a task

### The usual case: `FlyteFile` specified and `FlyteFile` returned

This is the case that we discussed above, where the task function signature specifies a `FlyteFile` return type and the task actually does return a `FlyteFile`.
There are two sub-cases:

#### Local file source

In this case, the returned `FlyteFile` is created from a local file.
For example:

```{code-block} python
@task
def t() -> FlyteFile
    # Create a file locally, write something to it, etc.
    local_path = "/some/path/data.csv"
    f = open(local_path, "w")
    ...

    # Return a FlyteFile initialized with the local path
    return FlyteFile(local_path)
```

When the `FlyteFile` object is returned from the task function:

* The contents of the file are uploaded to a randomly created location in your **raw data store**.
Each time the task is run a new randomly chosen location is generated.
* If the `FlyteFile` object was initialized with a `remote_path` parameter, then this location is used instead.
Note that (as opposed to the case where the raw data location is randomly generated) if this option is chosen, then each time the task is run with the same `remote_path`, the location will be overwritten.
* On the Flyte side (notionally, in the scope of the workflow function) a Flyte `Blob` object is created with its `uri` set to the raw data store location.

#### Remote file source

In this case, the returned `FlyteFile` is created from a remote file.
For example::

```{code-block} python
@task
def t() -> FlyteFile
    # Define a remote path
    remote_path = "https://some/path/data.csv"

    # Return a FlyteFile initialized with the remote path
    return FlyteFile(remote_path)
```

When the `FlyteFile` object is returned from the task function:

* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is returned with its `uri` set to the raw data store location.
* No uploading of data occurs.

### Edge cases

#### `FlyteFile` specified but `str` or `pathlib.Path` returned

This is the case where the task function signature specifies a `FlyteFile` return type but the task actually returns a `str` or `pathlib.Path`.
There are two sub-cases:

**Local file source**

In this case, the path is a local file path. For example:

```{code-block} python
@task
def t() -> FlyteFile
    # Create a file locally, write something to it, etc.
    local_path = "/some/path/data.csv"
    f = open(local_path, "w")
    ...

    # Return the plain string form of the path
    return local_path
```

When the value is returned from the task function:

* The contents of the file at the path are uploaded to a randomly created location in your **raw data store**.
Each time the task is run a new randomly chosen location is generated.
The raw data store is a blob store location in your Union dataplane (if you are on AWS, it is an S3 bucket, for example) configured during your onboarding.
The location can be overridden using the `raw_output_data_prefix` setting.
* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is returned with its `uri` set to the raw data store location.

**Remote file source**

In this case, the specified path is a remote path. For example:

```{code-block} python
@task
def t() -> FlyteFile
    # Define a remote path
    remote_path = "https://some/path/data.csv"

    # Return the plain string form of the path
    return remote_path
```

When the value is returned from the task function:

* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is created with its `uri` set to the given path.
* No uploading of data occurs.

#### `os.PathLike` specified but `FlyteFile` returned

This is the case where the task function signature specifies a `os.PathLike` return type but the task actually returns a `FlyteFile`. There are two sub-cases:

**Local file source**

In this case, the returned `FlyteFile` is created with a local path. For example:

```{code-block} python
@task
def t() -> os.PathLike
    # Create a file locally, write something to it, etc.
    local_path = "/some/path/data.csv"
    f = open(local_path, "w")
    ...

    # Return a FlyteFile initialized with the local path
    return FlyteFile(local_path)
```

When the object is returned from the task function:

* A warning is logged, since you are passing a more complex object (a `FlyteFile`) and expecting a simpler interface (`os.PathLike`).
* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is created with its `uri` set to the given path.
* No uploading occurs.

**Remote file source**

In this case, the returned `FlyteFile` is created with a remote path. we have something like this:

```{code-block} python
@task
def t() -> os.PathLike
    # Define a remote path
    remote_path = "https://some/path/data.csv"

    # Return a FlyteFile initialized with the remote path
    return FlyteFile(remote_path)
```

When the object is returned from the task function:

* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is returned with its `uri` set to the given path.
* No uploading of data occurs.

#### `os.PathLike` specified and `str` or `pathlib.Path` returned

This is the case where the task function signature specifies an `os.PathLike` return type and the task returns a `str` or `pathlib.Path`. There are two sub-cases:

**Local file source**

In this case, the path is a local path. For example:

```{code-block} python
@task
def t() -> os.PathLike
    # Create a file locally, write something to it, etc.
    local_path = "/some/path/data.csv"
    f = open(local_path, "w")
    ...

    # Return the plain string form of the path
    return local_path
```

When the value is returned from the task function:

* No warning is logged since only a string is being returned (as opposed to a `FlyteFile`).
* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is created with its `uri` set to the path.
* No uploading occurs.

**Remote file source**

In this case, the path is a remote path. For example:

```{code-block} python
@task
def t() -> os.PathLike
    # Define a remote path
    remote_path = "https://some/path/data.csv"

    # Return the plain string form of the path
    return remote_path
```

When the value is returned from the task function:

* On the Flyte side (notionally, in the scope of the workflow function) a Flyte object of type `Blob` object is returned with its `uri` set to the path.
* No uploading of data occurs.

## Passing a file to a task

This is the case where a Flyte object of type `Blob` is passed to a task function. This only occurs when a previous task has returned a value of type `FlyteFile` or `os.PathLike` (as described above) and that value is then passed on to the next task. For example:

```{code-block} python
@workflow
def wf1():
    ff = t1()
    t2(ff)

@task
def t1() -> FlyteFile
    return FlyteFile("https://some/path/data.csv")

@task
def t2(ff: FlyteFile)
    ...
```

### The usual case: `FlyteFile` parameter

This is the case where the type of the function parameter is `FlyteFile`. For example:

```{code-block} python
@task
def t(ff: FlyteFile)
    ...
```

There are two sub-cases:

#### Local file source

If the incoming `Blob` object has a `uri` that is a **local path**, then a `FlyteFile` is created as follows:

* `FlyteFile.path` is set to the local path from `Blob.uri`.
* `FlyteFile.remote_source` is set to `None`.
* `FlyteFile.remote_path` is set to `None`.
* The function `FlyteFile.downloader` is set top to the `noop` function.
* Any call to `FlyteFile.download()` will raise an exception.

The `FlyteFile` object can be used as a normal file within the task code.

**Remote file source**

If the incoming `Blob` object has a `uri` that is a **remote path**, then a `FlyteFile` is created as follows:

* `FlyteFile.path` is set to a randomly generated local path (but no file is written there until `FlyteFile.download()` is called).
* `FlyteFile.remote_source` is set to the remote path from `Blob.uri`.
* `FlyteFile.remote_path` is set to `None`.
* The function `FlyteFile.downloader`, if set, will be used upon a call to `FlyteFile.download()`, otherwise, the default download function will be used.
* A call to `FlyteFile.download()` download the remote file from `FlyteFile.remote_path` to the location at `FlyteFile.path`.

Once `FlyteFile.download()` has been called, the `FlyteFile` object can be used as a normal file within the task code.

### The edge case: `os.PathLike` parameter

This is the case where the type of the function parameter is of type `os.PathLike` (but not its subtype `FlyteFile`). For example:

```{code-block} python
@task
def t(ff: os.PathLike)
    ...
```

In this case, a `FlyteFile` object is still created, but regardless of whether the incoming `Blob` object has a `uri` that is a **local path** or a **remote path** it is initialized as follows:

* `FlyteFile.path` is set to the path from `Blob.uri`.
* `FlyteFile.remote_source` is set to `None`.
* `FlyteFile.remote_path` is set to `None`.
* The function `FlyteFile.downloader` is set to the `noop` function.

## Using FlyteFile

### Opening a file

To download and open a `FlyteFile`, you would do this:

```{code-block} python
@task
def t(ff: FlyteFile):
    if not ff.downloaded:
        ff.download()
    with open(ff) as f:
         data = f.read()
         ...
```

Alternatively, you can stream the file directly from its source location without needing to first download it, using either `FlyteFile.open()` or `fsspec.open()`.
For example:

```{code-block} python
@task
def copy_file(ff: FlyteFile) -> FlyteFile:
    new_file = FlyteFile.new_remote_file("target")
    with ff.open("rb", cache_type="readahead", cache={}) as r:
        with new_file.open("wb") as w:
            w.write(r.read())
    return new_file
```

Or, alternatively:

```{code-block} python
@task
def copy_file(ff: FlyteFile) -> FlyteFile:
    new_file = FlyteFile.new_remote_file(ff.name)
    with fsspec.open(f"readahead::{ff.remote_path}", "rb", readahead={}) as r:
        with new_file.open("wb") as w:
            w.write(r.read())
    return new_file
```
