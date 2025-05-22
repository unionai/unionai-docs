---
title: Downloading with FlyteFile and FlyteDirectory
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Downloading with FlyteFile and FlyteDirectory

The basic idea behind `FlyteFile` and `FlyteDirectory` is that they represent files and directories in remote storage.
When you work with these objects in your tasks, you are working with references to the remote files and directories.

Of course, at some point you will need to access the actual contents of these files and directories,
which means that they have to be downloaded to the local file system of the task container.

The actual files and directories of a `FlyteFile` or `FlyteDirectory` are downloaded to the local file system of the task container in two ways:
* Explicitly, through a call to the `download` method.
* Implicitly, through automatic downloading.
  This occurs when an external function is called on the `FlyteFile` or `FlyteDirectory` that itself calls the `__fspath__` method.

To write efficient and performant task and workflow code, it is particularly important to have a solid understanding of when exactly downloading occurs.
Let's look at some examples showing when the content `FlyteFile` objects and `FlyteDirectory` objects are downloaded to the local task container file system.

## FlyteFile

**Calling `download` on a FlyteFile**

```python
@{{< key kit_as >}}.task
def my_task(ff: FlyteFile):
    print(os.path.isfile(ff.path))  # This will print False as nothing has been downloaded
    ff.download()
    print(os.path.isfile(ff.path))  # This will print True as the FlyteFile was downloaded
```

Note that we use `ff.path` which is of type `typing.Union[str, os.PathLike]` rather than using `ff` in `os.path.isfile` directly.
In the next example, we will see that using `os.path.isfile(ff)` invokes `__fspath__` which downloads the file.

**Implicit downloading by `__fspath__`**

In order to make use of some functions like `os.path.isfile` that you may be used to using with regular file paths, `FlyteFile`
implements a `__fspath__` method that downloads the remote contents to the `path` of `FlyteFile` local to the container.

```python
@{{< key kit_as >}}.task
def my_task(ff: FlyteFile):
    print(os.path.isfile(ff.path))  # This will print False as nothing has been downloaded
    print(os.path.isfile(ff))  # This will print True as os.path.isfile(ff) downloads via __fspath__
    print(os.path.isfile(ff.path))  # This will again print True as the file was downloaded
```

It is important to be aware of any operations on your `FlyteFile` that might call `__fspath__` and result in downloading.
Some examples include, calling `open(ff, mode="r")` directly on a `FlyteFile` (rather than on the `path` attribute) to get the contents of the path,
or similarly calling `shutil.copy` or `pathlib.Path` directly on a `FlyteFile`.

## FlyteDirectory

**Calling `download` on a FlyteDirectory**

```python
@{{< key kit_as >}}.task
def my_task(fd: FlyteDirectory):
    print(os.listdir(fd.path))  # This will print nothing as the directory has not been downloaded
    fd.download()
    print(os.listdir(fd.path))  # This will print the files present in the directory as it has been downloaded
```

Similar to how the `path` argument was used above for the `FlyteFile`, note that we use `fd.path` which is of type `typing.Union[str, os.PathLike]` rather than using `fd` in `os.listdir` directly.
Again, we will see that this is because of the invocation of `__fspath__` when `os.listdir(fd)` is called.

**Implicit downloading by `__fspath__`**

In order to make use of some functions like `os.listdir` that you may be used to using with directories, `FlyteDirectory`
implements a `__fspath__` method that downloads the remote contents to the `path` of `FlyteDirectory` local to the container.

```python
@{{< key kit_as >}}.task
def my_task(fd: FlyteDirectory):
    print(os.listdir(fd.path))  # This will print nothing as the directory has not been downloaded
    print(os.listdir(fd))  # This will print the files present in the directory as os.listdir(fd) downloads via __fspath__
    print(os.listdir(fd.path))  # This will again print the files present in the directory as it has been downloaded
```

It is important to be aware of any operations on your `FlyteDirectory` that might call `__fspath__` and result in downloading.
Some other examples include, calling `os.stat` directly on a `FlyteDirectory` (rather than on the `path` attribute) to get the status of the path,
or similarly calling `os.path.isdir` on a `FlyteDirectory` to check if a directory exists.

**Inspecting the contents of a directory without downloading using `crawl`**

As we saw above, using `os.listdir` on a `FlyteDirectory` to view the contents in remote blob storage
results in the contents being downloaded to the task container. If this should be avoided, the `crawl` method offers a means of inspecting
the contents of the directory without calling `__fspath__` and therefore downloading the directory contents.

```python
@{{< key kit_as >}}.task
def task1() -> FlyteDirectory:
    p = os.path.join(current_context().working_directory, "my_new_directory")
    os.makedirs(p)

    # Create and write to two files
    with open(os.path.join(p, "file_1.txt"), 'w') as file1:
        file1.write("This is file 1.")
    with open(os.path.join(p, "file_2.txt"), 'w') as file2:
        file2.write("This is file 2.")

    return FlyteDirectory(p)

@{{< key kit_as >}}.task
def task2(fd: FlyteDirectory):
    print(os.listdir(fd.path))  # This will print nothing as the directory has not been downloaded
    print(list(fd.crawl()))  # This will print the files present in the remote blob storage
    # e.g. [('s3://union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80', 'file_1.txt'), ('s3://union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80', 'file_2.txt')]
    print(list(fd.crawl(detail=True)))  # This will print the files present in the remote blob storage with details including type, the time it was created, and more
    # e.g. [('s3://union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80', {'file_1.txt': {'Key': 'union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80/file_1.txt', 'LastModified': datetime.datetime(2024, 7, 9, 16, 16, 21, tzinfo=tzlocal()), 'ETag': '"cfb2a3740155c041d2c3e13ad1d66644"', 'Size': 15, 'StorageClass': 'STANDARD', 'type': 'file', 'size': 15, 'name': 'union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80/file_1.txt'}}), ('s3://union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80', {'file_2.txt': {'Key': 'union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80/file_2.txt', 'LastModified': datetime.datetime(2024, 7, 9, 16, 16, 21, tzinfo=tzlocal()), 'ETag': '"500d703f270d4bc034e159480c83d329"', 'Size': 15, 'StorageClass': 'STANDARD', 'type': 'file', 'size': 15, 'name': 'union-contoso/ke/fe503def6ebe04fa7bba-n0-0/160e7266dcaffe79df85489771458d80/file_2.txt'}})]
    print(os.listdir(fd.path))  # This will again print nothing as the directory has not been downloaded
```