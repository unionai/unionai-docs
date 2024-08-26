# FlyteDirectory



## Overview

In Flyte, each task runs in its own container.
One result is that a local directory in one task will not automatically be available in other tasks, because it exists only inside the container where it was created.

To share a directory across tasks it must be explicitly passed out of one task and into another within your workflow code.
To help with this, Flyte provides the [`FlyteDirectory`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.types.directory.FlyteDirectory.html) Python class. Here is an example of how it works.

### Local directory example

Let's say you have a directory local to a task `task1` that you want to make accessible in the next task, `task2`.
To do this, you create a `FlyteDirectory` object using the local path of the file you created, and then pass the `FlyteDirectory` object as part of your workflow, like this:

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

@task
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

@workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

Recall that the code within a Flyte task function is real Python code (run in a Python interpreter inside the task container) while the code within a workflow function is actually a Python-like DSL, compiled by Flyte into a representation of the workflow.

This means that Flyte needs to handle the passing of the variable `fd` in `workflow` from task `task1` to task `task2`. Of course, by design, the Flyte workflow engine knows how to handle values of type `FlyteDirectory`.
Here is what it does:

* The `FlyteDirectory` object was initialized with the local path of the directory that you created.
* When the `FlyteDirectory` is passed out of `task1`, Flyte uploads the local directory and its contained files to a randomly generated location in your raw data store.
The URI of this location is used to initialize a Flyte object of type `Blob`.
* The `Blob` object is passed to `task2`.
Because the type of the input parameter is `FlyteDirectory`, Flyte converts the `Blob` back into a `FlyteDirectory` and sets the `remote_source` attribute of that `FlyteDirectory` to the URI of the `Blob` object.
* Inside `ask` you can now inspect the directory using standard functionality from the `os` package or using helper `FlyteDirectory` methods which lazily download the returned `FlyteFile`s so we can inspect their contents.

### Remote file example

In the example above we started with a local directory.
To preserve that directory across the task boundary, Flyte uploaded it to a remote location (in this case the system's dedicated blob store) before passing it to the next task, where it can be downloaded.

You can also _start with a remote directory_, simply by initializing the `FlyteDirectory` object with a URI pointing to a remote source. For example:

```{code-block} python
@task
def task1() -> FlyteDirectory:
    p = "https://people.sc.fsu.edu/~jburkardt/data/csv/"
    return FlyteDirectory(p)

@task
def task2(fd: FlyteDirectory):
    # Get a list of the directory contents and display the first csv
    files = FlyteDirectory.listdir(fd)
    with open(files[0], mode="r") as f:
        d = f.read()
    print(f"The first csv is: \n{d}")


@workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

In this case, no uploading is needed. When the object is passed out of the task, it is simply converted into a `Blob` with the remote path as the URI.
After being passed to the next task, `FlyteDirectory.listdir(fd)` can be called to inspect the directory contents, just as before.

When initializing a `FlyteDirectory` with a remote file location, the URI schemes supported are: `http`, `https`, `gs`, `abfs`, `abfss`, and `file`.

### Specifying `remote_directory`

When a `FlyteDirectory` based on a local file is passed out of a task, the file is uploaded, by default, to the default raw data store configured in your data plane.
In AWS-based systems, this is an S3 bucket, for example.

Within that bucket, the actual directory location is, by default, a randomly generated path.
This path is guaranteed to be unique so that directories are never over-written on subsequent runs of the task.

However, the storage location used can be overridden by specifying the optional parameter `remote_directory` when initializing the `FlyteDirectory` object.
The specified value must be the full URI of a writable location accessible from your Flyte cluster.
You can, for example, use the same S3 bucket that your cluster uses by default (the raw data store) but with a specified directory name.

:::{note}

If you set `remote_directory` then subsequent runs of the same task will overwrite the files in the remote directory.

:::

Here is an example

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

    return FlyteDirectory(p, remote_directory="s3://union-contoso/foo/bar")

@task
def task2(fd: FlyteDirectory):
    # fd.remote_source == "s3://union-contoso/foo/bar"
    # file1.txt and file2.txt will now be found within s3://union-contoso/foo/bar

    # Use the FlyteDirectory
    ...

@workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

### Using `from_source`

You may have a remote directory that is already sitting in blog storage, say S3 for example. If you want to access
this directory, you can use the `from_source` class method. The resulting `FlyteDirectory` will have a `path` local to
the container and a `remote_source` equal to the URI used in `from_source`. Note that `from_source` does not download
the content of the directory unless the `download` method is explicitly called.

```{code-block} python
@task
def task1() -> FlyteDirectory:
    fd = FlyteDirectory.from_source("s3://union-contoso/foo/bar")
    # fd.path is a random path local to the task container
    # ff.remote_source == "s3://union-contoso/foo/bar"

    return fd
```
