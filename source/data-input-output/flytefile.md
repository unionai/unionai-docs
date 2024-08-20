# FlyteFile

In Union, because each task runs in its own container, a file created locally in one task will not automatically be available in other tasks.

The natural way to solve this problem is for the source task to upload the file to a common location (like the Union object store) and then pass a reference to that location to the destination task, which then downloads the file.

Since this is such a common case, Union provides the [`FlyteFile`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.types.file.FlyteFile.html#flytekit-types-file-flytefile) class, which automates this process, making it nearly transparent to the user.

Here is how it works.

## Local file example

Let's say you have a local file in task `task_1` that you want to make accessible in the next task, `task_2`.
To do this, you create a `FlyteFile` object using the local path of the file you created, and then pass the `FlyteFile` object as part of your workflow, like this:

```{code-block} python
@task
def task_1() -> FlyteFile:
    local_path = os.path.join(current_context().working_directory, "data.txt")
    with open(local_path, mode="w") as f:
        f.write("Here is some sample data.")
    return FlyteFile(path=local_path)


@task
def task_2(ff: FlyteFile):
    with ff.open(mode="r") as f
        file_contents = f.read()


@workflow
def wf():
    ff = task_1()
    task_2(ff=ff)
```

Union handles the passing of the `FlyteFile` `ff` in `wf` from `task1` to `task2`:

* The `FlyteFile` object was initialized in `task_1` with the local path of the file that you created.
* When the `FlyteFile` is passed out of `task_1`, Union uploads the local file to a randomly generated location in the Union object store.
* This location is used to initialize the URI attribute of a Flyte `Blob` object (Note that Flyte objects are not Python objects. They exists at the workflow level and are used to pass data between task containers.
  See [Flyte objects]() for more details).
* The `Blob` object is passed to `task_2`.
* Because the type of the input parameter of `task_2` is `FlyteFile`, Union converts the `Blob` back into a `FlyteFile` and sets the `remote_source` attribute of that `FlyteFile` to the URI of the `Blob` object.
* Inside `task_2` you can now perform a `FlyteFile.open()` and read the file contents.

## Remote file example

In the example above we started with a local file.
To preserve that file across the task boundary, Union uploaded it to the Union object store before passing it to the next task.

You can also _start with a remote file_, simply by initializing the `FlyteFile` object with a URI pointing to a remote source. For example:

```{code-block} python
@task
def task_1() -> FlyteFile:
    remote_path = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
    return FlyteFile(path=remote_path)
```

In this case, no uploading is needed because the source file is already in a remote location.
When the object is passed out of the task, it is simply converted into a `Blob` with the remote path as the URI.
After being passed to the next task, `FlyteFile.open()` can be called, just as before.

When initializing a `FlyteFile` with a remote file location, all URI schemes supported by `fsspec` are supported, the most common being: `http`, `https`, `gs` and `s3`.

{@@ if byoc @@}

## Specifying `remote_path`

When a `FlyteFile` based on a local file is passed out of a task, the file is uploaded, by default, to the Union object store.
For example, in AWS-based Union BYOC systems, this is an S3 bucket, while in Google Cloud-based Union BYOC systems, this is a GCS bucket.

Within that bucket, the actual file location is, by default, a randomly generated path.
This path is guaranteed to be unique so that files are never over-written on subsequent runs of the task.

However, the storage location used can be overridden by specifying the optional parameter `remote_path` when initializing the `FlyteFile` object.
The specified value must be the full URI of a writable location accessible from your Union cluster.
You can, for example, use the same bucket that your cluster uses by default, but with a specified file name.
Alternatively, you can use an entirely different bucket.

:::{note}

If you set `remote_path` to a static string, subsequent runs of the same task will overwrite the file.
If you want to use a dynamically generated path, you will have to generate it yourself.

:::

Here is an example

```{code-block} python
@task
def task1() -> FlyteFile:
    local_path = os.path.join(current_context().working_directory, "data.txt")
    with open(local_path, mode="w") as f:
        f.write("Here is some sample data.")
    return FlyteFile(path=local_path, remote_path="s3://union-contoso/foobar")
```

## Specifying the raw data prefix

Note that the above use of `remote_path` in `FlyteFile` is different from the higher level configuration of `raw_data_prefix` parameter.
The `raw_data_prefix` parameter can be set at the workflow execution level and effectively changes the default location for all writes to object store.
For example, if the `raw_data_prefix` is set then a `FlyteFile` (without a `remote_path` override) will still perform the automatic random path generation,
but it will simply be relative to the new `raw_data_prefix` instead of the default location.
See [Raw data prefix](raw-data-prefix) for more information.

{@@ endif @@}

## Streaming

In the above examples, we showed how to access the contents of `FlyteFile` by calling `open` on the `FlyteFile` object.
The object returned by `FlyteFile.open` is a stream. In the above examples, the files were small, so a simple `read` was used.
But, for large files you can iterate through the contents of the stream:

```{code-block} python
@task
def task_1() -> FlyteFile:
    remote_path = "https://sample-videos.com/csv/Sample-Spreadsheet-100000-rows.csv"
    return FlyteFile(path=remote_path)

@task
def task_2(ff: FlyteFile):
    with ff.open(mode="r") as f
        for row in f:
            do_something(row)
```

## Downloading

Alternative, you can download the contents of a `FlyteFile` object to a local file in the task container.
There are two ways to do this: **implicitly** and **explicitly**.

### Implicit downloading

The source file of a `FlyteFile` object is downloaded to the local container file system automatically whenever an external function is called that takes the `FlyteFile` object and then itself calls `FlyteFile`'s `__fspath__()` method.

`FlyteFile` implements the `os.PathLike` interface and therefore the `__fspath__()` method.
`FlyteFile`'s implementation of `__fspath__()` performs a download of the source file to the local container storage and return the path to that local file.
This enables many common file-related operations in Python to be performed on the `FlyteFile` object.

The most prominent example of such an operation is calling Python's built-in `open()` method with a `FlyteFile`:

```{code-block} python
@task
def task_2(ff: FlyteFile):
    with open(ff, mode="r") as f
       file_contents= f.read()
```

:::{admonition}

Note the difference between

`ff.open(mode="r")`

and

`open(ff, mode="r")`

The former calls `FlyteFile`'s `open` method and returns a stream to the file without downloading it.
The latter calls the built-in Python function `open` passing a `FlyteFile`, downloads the file to the local container file system, and returns a handle to that file.

:::

Many other Python file operations (essentially, any that accept an `os.PathLike`) can also be performed on a `FlyteFile` object and result in an automatic download.

See [Downloading with FlyteFile and FlyteDirectory](./downloading-with-ff-and-fd) for more information.

### Explicit downloading

You can also explicitly download a `FlyteFile` to the local container file system by calling `FlyteFile.download()`:

```{code-block} python
@task
def task_2(ff: FlyteFile):
    local_path = ff.download()
```

This method typically used when you want to download the file without immediately reading it.
