# FlyteFile

In Union, because each task runs in its own container, a file created locally in one task will not automatically be available in other tasks.

The natural way to solve this problem is for the source task to to upload the file to a common location (like the Union object store) and then pass a reference to that location to the destination task, which then downloads the file.

Since this is such a common case, Union provides the [`FlyteFile`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.types.file.FlyteFile.html#flytekit-types-file-flytefile) class, which automates this process, making it nearly transparent to the user.

## Local file example

:::{note}
The term _local file_ in this section refers to a file local to the container running a task in Union.
It does not refer to a file on your local machine.
:::

Let's say you have a local file in the container running `task_1` that you want to make accessible in the next task, `task_2`.
To do this, you create a `FlyteFile` object using the local path of the file, and then pass the `FlyteFile` object as part of your workflow, like this:

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

Union handles the passing of the `FlyteFile` `ff` in `wf` from `task_1` to `task_2`:

* The `FlyteFile` object is initialized with the path (local to the `task_1` container) of the file you wish to share.
* When the `FlyteFile` is passed out of `task_1`, Union uploads the local file to a randomly generated location in the Union object store.
* This location is used to initialize the URI attribute of a Flyte `Blob` object. (Note that Flyte objects are not Python objects. They exists at the workflow level and are used to pass data between task containers. See [Flyte Core Language Specification > Literals](https://docs.flyte.org/en/latest/protos/docs/core/core.html#flyteidl-core-literals-proto) for more details.)
* The `Blob` object is passed to `task_2`.
* Because the type of the input parameter of `task_2` is `FlyteFile`, Union converts the `Blob` back into a `FlyteFile` and sets the `remote_source` attribute of that `FlyteFile` to the URI of the `Blob` object.
* Inside `task_2` you can now perform a [`FlyteFile.open()`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.types.file.FlyteFile.html#flytekit.types.file.FlyteFile.open) and read the file contents.

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

## Where dos FlyteFile and Flyte Directory store the actual data?

{@@ if serverless @@}



{@@ elif byoc @@}

`FlyteFile` and `FlyteDirectory` are two Python classes provided by Flyte to make it easy to pass files from one task to the next within a workflow.
They do this by wrapping a file or directory location path and, if necessary, maintaining the persistence of the referenced file or directory across task containers.

When you return a `FlyteFile` (or `FlyteDirectory`) object from a task, Flyte checks to see if the underlying file or directory is local to the task container or is already remotely located.
If it is local then Flyte automatically uploads it to an object store so that it is not lost when the task container is discarded on task completion.
If the file is already remote then no upload is performed.

When the `FlyteFile` (or `FlyteDirectory`) is passed into the next task, the location of the source file (or directory) is available within the object and it can be downloaded and opened.

By default, when Flyte uploads a local file or directory (as opposed to the case where the source data is already remote), it is stored in the default **raw data store** (an S3 or GCS bucket) configured in your data plane during setup.

Optionally, you can set up your own bucket and set the **raw data prefix** parameter to point to it.
In that case, Flyte will use this bucket for `FlyteFile`/`FlyteDirectory` storage.
This setting can be done on registration or per execution on the command line or in the UI.

In either case, the data stored in the bucket is placed in a randomly-named directory with a different random name generated for each `FlyteFile` (`FlyteDirectory`) data write.
This guarantees that you never overwrite your data.

A further variation is to specify `remote_path` when initializing your `FlyteFile` (or `FlyteDirectory`), in which case the underlying data is written to that precise location with no randomization.
In this case, subsequent runs using the same `remote_path` _will_ overwrite data.

See also:

* [FlyteFile](./data-input-output/flytefile)
* [Understand How Flyte Handles Data](https://docs.flyte.org/en/latest/concepts/data_management.html)

### Can I accidentally overwrite FlyteFile data?

In general, no.
When a task returns a `FlyteFile` or `FlyteDirectory` whose source is local to the origin container, Flyte automatically uploads it to a location with a randomized path in the raw data store.
This ensures that subsequent runs will not overwrite earlier data.

The only exception is if you explicitly initialize the `FlyteFile` or `FlyteDirectory` with a `remote_path`.
In that case, the storage location used is precisely that specified.
No randomization occurs so successive runs using the same `remote_path` will overwrite the same location.

See also:

* In this FAQ section, **Where do FlyteFile and FlyteDirectory store their data?**
* [FlyteFile](./data-input-output/flytefile)

### Can I use my own blob store for FlyteFile and FlyteDirectory data storage?

Yes.
If you do not want to use the default raw output store that is provided with your data plane you can configure your own storage.
If you do this, you must ensure that your task code has access to this custom storage (see [Enabling AWS S3](./integrations/enabling-aws-resources/enabling-aws-s3) or [Enabling Google Cloud Storage](./integrations/enabling-gcp-resources/enabling-google-cloud-storage)).

You then have two options for using that storage for `FlyteFile` and `FlyteDirectory`:

* Specify the custom storage location in the output location prefix parameter either on workflow registration or per execution.
Your custom storage will be used instead of the default pre-configured raw data store, but the file data will be managed in the same way, using a randomized location within that store for each run, ensuring no overwrites.
* Specify the `remote_path` when initializing your `FlyteFile` or `FlyteDirectory` object in your task code.
The precise location specified will be used with no randomization so avoiding overwrites is up to you.

See also:

* In this FAQ section, **Where do `FlyteFile` and `FlyteDirectory` store their data?**

* [FlyteFile](./data-input-output/flytefile)







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

{@# See [Raw data prefix](raw-data-prefix) for more information. #@}

{@@ endif @@}

## Streaming

In the above examples, we showed how to access the contents of `FlyteFile` by calling `open` on the `FlyteFile` object.
The object returned by `FlyteFile.open` is a stream. In the above examples, the files were small, so a simple `read` was used.
But for large files, you can iterate through the contents of the stream:

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
`FlyteFile`'s implementation of `__fspath__()` performs a download of the source file to the local container storage and returns the path to that local file.
This enables many common file-related operations in Python to be performed on the `FlyteFile` object.

The most prominent example of such an operation is calling Python's built-in `open()` method with a `FlyteFile`:

```{code-block} python
@task
def task_2(ff: FlyteFile):
    with open(ff, mode="r") as f
       file_contents= f.read()
```

:::{note}

Note the difference between

`ff.open(mode="r")`

and

`open(ff, mode="r")`

The former calls `FlyteFile`'s `open` method and returns a stream to the file without downloading it.
The latter calls the built-in Python function `open()`, downloads the specified `FlyteFile` to the local container file system, and returns a handle to that file.

:::

Many other Python file operations (essentially, any that accept an `os.PathLike` object) can also be performed on a `FlyteFile` object and result in an automatic download.

See [Downloading with FlyteFile and FlyteDirectory](./downloading-with-ff-and-fd) for more information.

### Explicit downloading

You can also explicitly download a `FlyteFile` to the local container file system by calling `FlyteFile.download()`:

```{code-block} python
@task
def task_2(ff: FlyteFile):
    local_path = ff.download()
```

This method is typically used when you want to download the file without immediately reading it.









### Where do `FlyteFile` and `FlyteDirectory` store their data?



### How do the typed aliases of `FlyteFile` and `FlyteDirectory` work?

You may notice that `flytekit` defines some aliases of `FlyteFile` with specific type annotations.
Specifically, `FlyteFile` has the following [aliases for specific file types](https://github.com/flyteorg/flytekit/blob/edfa76739d1064822af44e0addc924e381d3a5ad/flytekit/types/file/__init__.py):

* `HDF5EncodedFile`
* `HTMLPage`
* `JoblibSerializedFile`
* `JPEGImageFile`
* `PDFFile`
* `PNGImageFile`
* `PythonPickledFile`
* `PythonNotebook`
* `SVGImageFile`

Similarly, `FlyteDirectory` has the following [aliases](https://github.com/flyteorg/flytekit/blob/edfa76739d1064822af44e0addc924e381d3a5ad/flytekit/types/directory/__init__.py):

* `TensorboardLogs`
* `TFRecordsDirectory`

These aliases can be used when handling a file or directory of the specified type, however, doing so is entirely optional.
Under the covers, the object itself will still be a simple `FlyteFile` or `FlyteDirectory`.
The aliased version of the classes do not perform any checks on the actual content of the file, they are simply syntactic markers that enforce agreement between type annotations in the signatures of task functions.