# FlyteFile and FlyteDirectory

In Union.ai, each task runs in its own container. This means that a file or directory created locally in one task will not automatically be available in other tasks.

The natural way to solve this problem is for the source task to to upload the file or directory to a common location (like the Union.ai object store) and then pass a reference to that location to the destination task, which then downloads or streams the data.

Since this is such a common use case, the Union.ai SDK provides the [`FlyteFile`](../../api-reference/union-sdk/custom-types/flytefile.md) and [`FlyteDirectory`](../../api-reference/union-sdk/custom-types/flytedirectory.md) classes, which automate this process.

## How the classes work

The classes work by wrapping a file or directory location path and, if necessary, maintaining the persistence of the referenced file or directory across task containers.

When you return a `FlyteFile` (or `FlyteDirectory`) object from a task, Union.ai checks to see if the underlying file or directory is local to the task container or if it already exists in a remote location.

If it is local to the source container, then Union.ai automatically uploads it to an object store so that it is not lost when the task container is discarded on task completion.
If the file or directory is already remote, then no upload is performed.

When the `FlyteFile` (or `FlyteDirectory`) is passed into the next task, the location of the source file (or directory) is available within the object and it can be downloaded or streamed.

## Local examples

:::{admonition} Local means local to the container
The terms _local file_ and _local_directory_ in this section refer to a file or directory local to the container running a task in Union.ai.
They do not refer to a file or directory on your local machine.
:::

### Local file example

Let's say you have a local file in the container running `task_1` that you want to make accessible in the next task, `task_2`.
To do this, you create a `FlyteFile` object using the local path of the file, and then pass the `FlyteFile` object as part of your workflow, like this:

```{code-block} python
@union.task
def task_1() -> FlyteFile:
    local_path = os.path.join(current_context().working_directory, "data.txt")
    with open(local_path, mode="w") as f:
        f.write("Here is some sample data.")
    return FlyteFile(path=local_path)


@union.task
def task_2(ff: FlyteFile):
    with ff.open(mode="r") as f
        file_contents = f.read()


@union.workflow
def wf():
    ff = task_1()
    task_2(ff=ff)
```

Union.ai handles the passing of the `FlyteFile` `ff` in the workflow `wf` from `task_1` to `task_2`:

* The `FlyteFile` object is initialized with the path (local to the `task_1` container) of the file you wish to share.
* When the `FlyteFile` is passed out of `task_1`, Union.ai uploads the local file to a unique location in the Union.ai object store. A randomly generated, universally unique location is used to ensure that subsequent uploads of other files never overwrite each other.
* The object store location is used to initialize the URI attribute of a Flyte `Blob` object. Note that Flyte objects are not Python objects. They exist at the workflow level and are used to pass data between task containers. For more details, see [Flyte Core Language Specification > Literals](https://docs.flyte.org/en/latest/api/flyteidl/docs/core/core.html#flyteidl-core-types-proto).
* The `Blob` object is passed to `task_2`.
* Because the type of the input parameter of `task_2` is `FlyteFile`, Union.ai converts the `Blob` back into a `FlyteFile` and sets the `remote_source` attribute of that `FlyteFile` to the URI of the `Blob` object.
* Inside `task_2` you can now perform a [`FlyteFile.open()`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.types.file.FlyteFile.html#flytekit.types.file.FlyteFile.open) and read the file contents.

### Local directory example

Below is an equivalent local example for `FlyteDirectory`. The process of passing the `FlyteDirectory` between tasks is essentially identical to the `FlyteFile` example above.

```{code-block} python
def task1() -> FlyteDirectory:
    # Create new local directory
    p = os.path.join(current_context().working_directory, "my_new_directory")
    os.makedirs(p)

    # Create and write to two files
    with open(os.path.join(p, "file_1.txt"), 'w') as file1:
        file1.write("This is file 1.")
    with open(os.path.join(p, "file_2.txt"), 'w') as file2:
        file2.write("This is file 2.")

    return FlyteDirectory(p)

@union.task
def task2(fd: FlyteDirectory):
    # Get a list of the directory contents using os to return strings
    items = os.listdir(fd)
    print(type(items[0]))

    # Get a list of the directory contents using FlyteDirectory to return FlyteFiles
    files = FlyteDirectory.listdir(fd)
    print(type(files[0]))
    with open(files[0], mode="r") as f:
        d = f.read()
    print(f"The first line in the first file is: {d}")

@union.workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

{@@ if serverless @@}

:::{admonition} Upload location
With Union.ai Serverless, the remote location to which FlyteFile and FlyteDirectory upload container-local files is always a randomly generated (universally unique) location in Union.ai's internal object store. It cannot be changed.

With Union.ai BYOC, the upload location is configurable. See [FlyteFile and FLyteDirectory > Changing the data upload location](https://docs.union.ai/byoc/data-input-output/flyte-file-and-flyte-directory.md#changing-the-data-upload-location).
:::

{@@ elif byoc @@}

## Changing the data upload location

:::{admonition} Upload location
With Union.ai Serverless, the remote location to which FlyteFile and FlyteDirectory upload container-local files is always a randomly generated (universally unique) location in Union.ai's internal object store. It cannot be changed.

With Union.ai BYOC, the upload location is configurable.
:::

By default, Union.ai uploads local files or directories to the default **raw data store** (Union.ai's dedicated internal object store).
However, you can change the upload location by setting the raw data prefix to your own bucket or specifying the `remote_path` for a `FlyteFile` or `FlyteDirectory`.

:::{admonition} Setting up your own object store bucket
For details on how to set up your own object store bucket, consult the direction for your cloud provider:

* [Enabling AWS S3](../integrations/enabling-aws-resources/enabling-aws-s3.md)
* [Enabling Google Cloud Storage](../integrations/enabling-gcp-resources/enabling-google-cloud-storage.md)
* [Enabling Azure Blob Storage](../integrations/enabling-azure-resources/enabling-azure-blob-storage.md)
:::

### Changing the raw data prefix

If you would like files or directories to be uploaded to your own bucket, you can specify the AWS, GCS, or Azure bucket in the **raw data prefix** parameter at the workflow level on registration or per execution on the command line or in the UI.
This setting can be done at the workflow level on registration or per execution on the command line or in the UI.

{@# TODO See [Raw data prefix]() for more information. #@}

Union.ai will create a directory with a unique, random name in your bucket for each `FlyteFile` or `FlyteDirectory` data write to guarantee that you never overwrite your data.

### Specifying `remote_path` for a `FlyteFile` or `FlyteDirectory`

If you specify the `remote_path` when initializing your `FlyteFile` (or `FlyteDirectory`), the underlying data is written to that precise location with no randomization.

:::{admonition} Using `remote_path` will overwrite data
If you set `remote_path` to a static string, subsequent runs of the same task will overwrite the file.
If you want to use a dynamically generated path, you will have to generate it yourself.
:::

{@@ endif @@}

## Remote examples

### Remote file example

In the example above, we started with a local file.
To preserve that file across the task boundary, Union.ai uploaded it to the Union.ai object store before passing it to the next task.

You can also _start with a remote file_, simply by initializing the `FlyteFile` object with a URI pointing to a remote source. For example:

```{code-block} python
@union.task
def task_1() -> FlyteFile:
    remote_path = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
    return FlyteFile(path=remote_path)
```

In this case, no uploading is needed because the source file is already in a remote location.
When the object is passed out of the task, it is converted into a `Blob` with the remote path as the URI.
After the FlyteFile is passed to the next task,  you can call `FlyteFile.open()` on it, just as before.

If you don't intend on passing the `FlyteFile` to the next task, and rather intend to open the contents of the remote file within the task, you can use `from_source`.

```{code-block} python
@union.task
def load_json():
    uri = "gs://my-bucket/my-directory/example.json"
    my_json = FlyteFile.from_source(uri)

    # Load the JSON file into a dictionary and print it
    with open(my_json, "r") as json_file:
        data = json.load(json_file)
    print(data)
```

When initializing a `FlyteFile` with a remote file location, all URI schemes supported by `fsspec` are supported, including `http`, `https`(Web), `gs` (Google Cloud Storage), `s3` (AWS S3), `abfs`, and `abfss` (Azure Blob Filesystem).

### Remote directory example

Below is an equivalent remote example for `FlyteDirectory`. The process of passing the `FlyteDirectory` between tasks is essentially identical to the `FlyteFile` example above.

```{code-block} python
@union.task
def task1() -> FlyteDirectory:
    p = "https://people.sc.fsu.edu/~jburkardt/data/csv/"
    return FlyteDirectory(p)

@union.task
def task2(fd: FlyteDirectory):
    # Get a list of the directory contents and display the first csv
    files = FlyteDirectory.listdir(fd)
    with open(files[0], mode="r") as f:
        d = f.read()
    print(f"The first csv is: \n{d}")


@union.workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

## Streaming

In the above examples, we showed how to access the contents of `FlyteFile` by calling `FlyteFile.open()`.
The object returned by `FlyteFile.open()` is a stream. In the above examples, the files were small, so a simple `read()` was used.
But for large files, you can iterate through the contents of the stream:

```{code-block} python
@union.task
def task_1() -> FlyteFile:
    remote_path = "https://sample-videos.com/csv/Sample-Spreadsheet-100000-rows.csv"
    return FlyteFile(path=remote_path)

@union.task
def task_2(ff: FlyteFile):
    with ff.open(mode="r") as f
        for row in f:
            do_something(row)
```

## Downloading

Alternative, you can download the contents of a `FlyteFile` object to a local file in the task container.
There are two ways to do this: **implicitly** and **explicitly**.

### Implicit downloading

The source file of a `FlyteFile` object is downloaded to the local container file system automatically whenever a function is called that takes the `FlyteFile` object and then calls `FlyteFile`'s `__fspath__()` method.

`FlyteFile` implements the `os.PathLike` interface and therefore the `__fspath__()` method.
`FlyteFile`'s implementation of `__fspath__()` performs a download of the source file to the local container storage and returns the path to that local file.
This enables many common file-related operations in Python to be performed on the `FlyteFile` object.

The most prominent example of such an operation is calling Python's built-in `open()` method with a `FlyteFile`:

```{code-block} python
@union.task
def task_2(ff: FlyteFile):
    with open(ff, mode="r") as f
       file_contents= f.read()
```

:::{admonition} `open()` vs `ff.open()`
Note the difference between

`ff.open(mode="r")`

and

`open(ff, mode="r")`

The former calls the `FlyteFile.open()` method and returns an iterator without downloading the file.
The latter calls the built-in Python function `open()`, downloads the specified `FlyteFile` to the local container file system, and returns a handle to that file.
:::

Many other Python file operations (essentially, any that accept an `os.PathLike` object) can also be performed on a `FlyteFile` object and result in an automatic download.

See [Downloading with FlyteFile and FlyteDirectory](./downloading-with-ff-and-fd.md) for more information.

### Explicit downloading

You can also explicitly download a `FlyteFile` to the local container file system by calling `FlyteFile.download()`:

```{code-block} python
@union.task
def task_2(ff: FlyteFile):
    local_path = ff.download()
```

This method is typically used when you want to download the file without immediately reading it.

{@# TODO: Explain:
classmethod FlyteFile.from_source()
classmethod FlyteFile.new_remote_file()

classmethod FlyteDirectory.from_source()
classmethod FlyteDirectory.listdir()
classmethod FlyteDirectory.new_remote()

FlyteDirectory.crawl()
FlyteDirectory.new_dir()
FlyteDirectory.new_file()
#@}

## Typed aliases

The [Union.ai SDK](../../api-reference/union-sdk/index.md) defines some aliases of `FlyteFile` with specific type annotations.
Specifically, `FlyteFile` has the following [aliases for specific file types](../../api-reference/union-sdk/custom-types/index.md#file-type):

* `HDF5EncodedFile`
* `HTMLPage`
* `JoblibSerializedFile`
* `JPEGImageFile`
* `PDFFile`
* `PNGImageFile`
* `PythonPickledFile`
* `PythonNotebook`
* `SVGImageFile`

Similarly, `FlyteDirectory` has the following [aliases](../../api-reference/union-sdk/custom-types/index.md#directory-type):

* `TensorboardLogs`
* `TFRecordsDirectory`

These aliases can optionally be used when handling a file or directory of the specified type, although the object itself will still be a `FlyteFile` or `FlyteDirectory`.
The aliased versions of the classes are syntactic markers that enforce agreement between type annotations in the signatures of task functions, but they do not perform any checks on the actual contents of the file.