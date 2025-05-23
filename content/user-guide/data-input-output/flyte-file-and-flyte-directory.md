---
title: FlyteFile and FlyteDirectory
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---


<!-- TODO: CHeck for variant accuracy  remove mention of flytesnacks-->

# FlyteFile and FlyteDirectory

{{< variant flyte >}}
{{< markdown >}}

## FlyteFile

Files are one of the most fundamental entities that users of Python work with,
and they are fully supported by Flyte. In the IDL, they are known as
[Blob](https://github.com/flyteorg/flyteidl/blob/master/protos/flyteidl/core/literals.proto#L33)
literals which are backed by the
[blob type](https://github.com/flyteorg/flyteidl/blob/master/protos/flyteidl/core/types.proto#L47).

Let's assume our mission here is pretty simple. We download a few CSV file
links, read them with the python built-in `csv.DictReader` function,
normalize some pre-specified columns, and output the normalized columns to
another CSV file.

> [!NOTE]
> To clone and run the example code on this page, see the
> [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).

First, import the libraries:

```python
import csv
from collections import defaultdict
from pathlib import Path
from typing import List

import {{< key kit_import >}}
```

Define a task that accepts `FlyteFile` as an input.
The following is a task that accepts a `FlyteFile`, a list of column names,
and a list of column names to normalize. The task then outputs a CSV file
containing only the normalized columns. For this example, we use z-score normalization,
which involves mean-centering and standard-deviation-scaling.

> [!NOTE]
> The `FlyteFile` literal can be scoped with a string, which gets inserted
> into the format of the Blob type ("jpeg" is the string in
> `FlyteFile[typing.TypeVar("jpeg")]`). The format is entirely optional,
> and if not specified, defaults to `""`.
> Predefined aliases for commonly used flyte file formats are also available.
> You can find them [here](https://github.com/flyteorg/flytekit/blob/master/flytekit/types/file/__init__.py).

```python
@{{< key kit_as >}}.task
def normalize_columns(
    csv_url: {{< key kit_as >}}.FlyteFile,
    column_names: List[str],
    columns_to_normalize: List[str],
    output_location: str,
) -> {{< key kit_as >}}.FlyteFile:
    # read the data from the raw csv file
    parsed_data = defaultdict(list)
    with open(csv_url, newline="\n") as input_file:
        reader = csv.DictReader(input_file, fieldnames=column_names)
        next(reader)  # Skip header
        for row in reader:
            for column in columns_to_normalize:
                parsed_data[column].append(float(row[column].strip()))

    # normalize the data
    normalized_data = defaultdict(list)
    for colname, values in parsed_data.items():
        mean = sum(values) / len(values)
        std = (sum([(x - mean) ** 2 for x in values]) / len(values)) ** 0.5
        normalized_data[colname] = [(x - mean) / std for x in values]

    # write to local path
    out_path = str(Path({{< key kit_as >}}.current_context().working_directory) / f"normalized-{Path(csv_url.path).stem}.csv")
    with open(out_path, mode="w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns_to_normalize)
        writer.writeheader()
        for row in zip(*normalized_data.values()):
            writer.writerow({k: row[i] for i, k in enumerate(columns_to_normalize)})

    if output_location:
        return {{< key kit_as >}}.FlyteFile(path=str(out_path), remote_path=output_location)
    else:
        return {{< key kit_as >}}.FlyteFile(path=str(out_path))
```

When the image URL is sent to the task, the system translates it into a `FlyteFile` object on the local drive (but doesn't download it). The act of calling the `download()` method should trigger the download, and the `path` attribute enables to `open` the file.

If the `output_location` argument is specified, it will be passed to the `remote_path` argument of `FlyteFile`, which will use that path as the storage location instead of a random location (Flyte's object store).

When this task finishes, the system returns the `FlyteFile` instance, uploads the file to the location, and creates a blob literal pointing to it.

Lastly, define a workflow. The `normalize_csv_files` workflow has an `output_location` argument which is passed to the `location` input of the task. If it's not an empty string, the task attempts to upload its file to that location.

```python
@{{< key kit_as >}}.workflow
def normalize_csv_file(
    csv_url: {{< key kit_as >}}.FlyteFile,
    column_names: List[str],
    columns_to_normalize: List[str],
    output_location: str = "",
) -> {{< key kit_as >}}.FlyteFile:
    return normalize_columns(
        csv_url=csv_url,
        column_names=column_names,
        columns_to_normalize=columns_to_normalize,
        output_location=output_location,
    )
```

You can run the workflow locally as follows:

```python
if __name__ == "__main__":
    default_files = [
        (
            "https://raw.githubusercontent.com/flyteorg/flytesnacks/refs/heads/master/examples/data_types_and_io/test_data/biostats.csv",
            ["Name", "Sex", "Age", "Heights (in)", "Weight (lbs)"],
            ["Age"],
        ),
        (
            "https://raw.githubusercontent.com/flyteorg/flytesnacks/refs/heads/master/examples/data_types_and_io/test_data/faithful.csv",
            ["Index", "Eruption length (mins)", "Eruption wait (mins)"],
            ["Eruption length (mins)"],
        ),
    ]
    print(f"Running {__file__} main...")
    for index, (csv_url, column_names, columns_to_normalize) in enumerate(default_files):
        normalized_columns = normalize_csv_file(
            csv_url=csv_url,
            column_names=column_names,
            columns_to_normalize=columns_to_normalize,
        )
        print(f"Running normalize_csv_file workflow on {csv_url}: " f"{normalized_columns}")
```

You can enable type validation if you have the [python-magic](https://pypi.org/project/python-magic/) package installed.

{{< /markdown >}}

{{< tabs >}}
{{< tab "Mac OS" >}}
{{< markdown >}}

```shell
$  brew install libmagic
```

{{< /markdown >}}
{{< /tab>}}
{{< tab "Linux" >}}
{{< markdown >}}

```shell
$ sudo apt-get install libmagic1
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

{{< markdown >}}

> [!NOTE]
> Currently, type validation is only supported on the `Mac OS` and `Linux` platforms.

## Streaming support

Flyte `1.5` introduced support for streaming `FlyteFile` types via the `fsspec` library.
This integration enables efficient, on-demand access to remote files, eliminating the need for fully downloading them to local storage.


> [!NOTE]
> This feature is marked as experimental. We'd love feedback on the API! @Peeter we should provide a link here for people to give feedback, thoughts?

Here is a simple example of removing some columns from a CSV file and writing the result to a new file:

```python
@{{< key kit_as >}}.task()
def remove_some_rows(ff: {{< key kit_as >}}.FlyteFile) -> {{< key kit_as >}}.FlyteFile:
    """
    Remove the rows that the value of city is 'Seattle'.
    This is an example with streaming support.
    """
    new_file = {{< key kit_as >}}.FlyteFile.new_remote_file("data_without_seattle.csv")
    with ff.open("r") as r:
        with new_file.open("w") as w:
            df = pd.read_csv(r)
            df = df[df["City"] != "Seattle"]
            df.to_csv(w, index=False)
```

## FlyteDirectory

In addition to files, folders are another fundamental operating system primitive.
Flyte supports folders in the form of
[multi-part blobs](https://github.com/flyteorg/flyteidl/blob/master/protos/flyteidl/core/types.proto#L73).

> [!NOTE]
> To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).

To begin, import the libraries:

```python
import csv
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import List

import {{< key kit_import >}}
```

Building upon the previous example demonstrated in the [`FlyteFile` section](#flytefile),
let's continue by considering the normalization of columns in a CSV file.

The following task downloads a list of URLs pointing to CSV files
and returns the folder path in a `FlyteDirectory` object.

```python
@{{< key kit_as >}}.task
def download_files(csv_urls: List[str]) -> union.FlyteDirectory:
    working_dir = {{< key kit_as >}}.current_context().working_directory
    local_dir = Path(working_dir) / "csv_files"
    local_dir.mkdir(exist_ok=True)

    # get the number of digits needed to preserve the order of files in the local directory
    zfill_len = len(str(len(csv_urls)))
    for idx, remote_location in enumerate(csv_urls):
        # prefix the file name with the index location of the file in the original csv_urls list
        local_image = Path(local_dir) / f"{str(idx).zfill(zfill_len)}_{Path(remote_location).name}"
        urllib.request.urlretrieve(remote_location, local_image)
    return {{< key kit_as >}}.FlyteDirectory(path=str(local_dir))
```


> [!NOTE]
> You can annotate a `FlyteDirectory` when you want to download or upload the contents of the directory in batches.
> For example,
>
> ```python
> @{{< key kit_as >}}.task
> def t1(directory: Annotated[{{< key kit_as >}}.FlyteDirectory, BatchSize(10)]) -> Annotated[{{< key kit_as >}}.FlyteDirectory, BatchSize(100)]:
>     ...
>     return {{< key kit_as >}}.FlyteDirectory(...)
>
> {{< key kit_name >}} efficiently downloads files from the specified input directory in 10-file chunks.
> It then loads these chunks into memory before writing them to the local disk.
> The process repeats for subsequent sets of 10 files.
> Similarly, for outputs, {{< key kit_name >}} uploads the resulting directory in chunks of 100.

We define a helper function to normalize the columns in-place.

> [!NOTE]
> This is a plain Python function that will be called in a subsequent {{< key product_name >}} task. This example
> demonstrates how {{< key product_name >}} tasks are simply entrypoints of execution, which can themselves call
> other functions and routines that are written in pure Python.

```python
def normalize_columns(
    local_csv_file: str,
    column_names: List[str],
    columns_to_normalize: List[str],
):
    # read the data from the raw csv file
    parsed_data = defaultdict(list)
    with open(local_csv_file, newline="\n") as input_file:
        reader = csv.DictReader(input_file, fieldnames=column_names)
        for row in (x for i, x in enumerate(reader) if i > 0):
            for column in columns_to_normalize:
                parsed_data[column].append(float(row[column].strip()))

    # normalize the data
    normalized_data = defaultdict(list)
    for colname, values in parsed_data.items():
        mean = sum(values) / len(values)
        std = (sum([(x - mean) ** 2 for x in values]) / len(values)) ** 0.5
        normalized_data[colname] = [(x - mean) / std for x in values]

    # overwrite the csv file with the normalized columns
    with open(local_csv_file, mode="w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns_to_normalize)
        writer.writeheader()
        for row in zip(*normalized_data.values()):
            writer.writerow({k: row[i] for i, k in enumerate(columns_to_normalize)})
```

We then define a task that accepts the previously downloaded folder, along with some metadata about the
column names of each file in the directory and the column names that we want to normalize.

```python
@{{< key kit_as >}}.task
def normalize_all_files(
    csv_files_dir: {{< key kit_as >}}.FlyteDirectory,
    columns_metadata: List[List[str]],
    columns_to_normalize_metadata: List[List[str]],
) -> union.FlyteDirectory:
    for local_csv_file, column_names, columns_to_normalize in zip(
        # make sure we sort the files in the directory to preserve the original order of the csv urls
        list(sorted(Path(csv_files_dir).iterdir())),
        columns_metadata,
        columns_to_normalize_metadata,
    ):
        normalize_columns(local_csv_file, column_names, columns_to_normalize)
    return {{< key kit_as >}}.FlyteDirectory(path=csv_files_dir.path)
```

Compose all the above tasks into a workflow.
This workflow accepts a list of URL strings pointing to a remote location containing a CSV file,
a list of column names associated with each CSV file, and a list of columns that we want to normalize.

```python
@{{< key kit_as >}}.workflow
def download_and_normalize_csv_files(
    csv_urls: List[str],
    columns_metadata: List[List[str]],
    columns_to_normalize_metadata: List[List[str]],
) -> {{< key kit_as >}}.FlyteDirectory:
    directory = download_files(csv_urls=csv_urls)
    return normalize_all_files(
        csv_files_dir=directory,
        columns_metadata=columns_metadata,
        columns_to_normalize_metadata=columns_to_normalize_metadata,
    )
```

You can run the workflow locally as follows:

```python
if __name__ == "__main__":
    csv_urls = [
        "https://raw.githubusercontent.com/flyteorg/flytesnacks/refs/heads/master/examples/data_types_and_io/test_data/biostats.csv",
        "https://raw.githubusercontent.com/flyteorg/flytesnacks/refs/heads/master/examples/data_types_and_io/test_data/faithful.csv",
    ]
    columns_metadata = [
        ["Name", "Sex", "Age", "Heights (in)", "Weight (lbs)"],
        ["Index", "Eruption length (mins)", "Eruption wait (mins)"],
    ]
    columns_to_normalize_metadata = [
        ["Age"],
        ["Eruption length (mins)"],
    ]

    print(f"Running {__file__} main...")
    directory = download_and_normalize_csv_files(
        csv_urls=csv_urls,
        columns_metadata=columns_metadata,
        columns_to_normalize_metadata=columns_to_normalize_metadata,
    )
    print(f"Running download_and_normalize_csv_files on {csv_urls}: " f"{directory}")
```

{{< /markdown >}}
{{< /variant >}}

{{< variant byoc selfmanaged >}}
{{< markdown >}}

In {{< key product_name >}}, each task runs in its own container. This means that a file or directory created locally in one task will not automatically be available in other tasks.

The natural way to solve this problem is for the source task to upload the file or directory to a common location (like the {{< key product_name >}} object store) and then pass a reference to that location to the destination task, which then downloads or streams the data.

Since this is such a common use case, the {{< key kit_name >}} SDK provides the [`FlyteFile`](../../api-reference/flytekit-sdk/packages/flytekit.types.file.file) and [`FlyteDirectory`](../../api-reference/flytekit-sdk/packages/flytekit.types.directory.types#flytekittypesdirectorytypesflytedirectory) classes, which automate this process.

## How the classes work

The classes work by wrapping a file or directory location path and, if necessary, maintaining the persistence of the referenced file or directory across task containers.

When you return a `FlyteFile` (or `FlyteDirectory`) object from a task, {{< key product_name >}} checks to see if the underlying file or directory is local to the task container or if it already exists in a remote location.

If it is local to the source container, then {{< key product_name >}} automatically uploads it to an object store so that it is not lost when the task container is discarded on task completion.
If the file or directory is already remote, then no upload is performed.

When the `FlyteFile` (or `FlyteDirectory`) is passed into the next task, the location of the source file (or directory) is available within the object and it can be downloaded or streamed.

## Local examples

> [!NOTE] Local means local to the container
> The terms _local file_ and _local_directory_ in this section refer to a file or directory local to the container running a task in {{< key product_name >}}.
> They do not refer to a file or directory on your local machine.

### Local file example

Let's say you have a local file in the container running `task_1` that you want to make accessible in the next task, `task_2`.
To do this, you create a `FlyteFile` object using the local path of the file, and then pass the `FlyteFile` object as part of your workflow, like this:

```python
@{{< key kit_as >}}.task
def task_1() -> {{< key kit_as >}}.FlyteFile:
    local_path = os.path.join(current_context().working_directory, "data.txt")
    with open(local_path, mode="w") as f:
        f.write("Here is some sample data.")
    return {{< key kit_as >}}.FlyteFile(path=local_path)

@{{< key kit_as >}}.task
def task_2(ff: {{< key kit_as >}}.FlyteFile):
    with ff.open(mode="r") as f
    file_contents = f.read()

@{{< key kit_as >}}.workflow
def wf():
    ff = task_1()
    task_2(ff=ff)
```

{{< key product_name >}} handles the passing of the `FlyteFile` `ff` in the workflow `wf` from `task_1` to `task_2`:

* The `FlyteFile` object is initialized with the path (local to the `task_1` container) of the file you wish to share.
* When the `FlyteFile` is passed out of `task_1`, {{< key product_name >}} uploads the local file to a unique location in the {{< key product_name >}} object store. A randomly generated, universally unique location is used to ensure that subsequent uploads of other files never overwrite each other.
* The object store location is used to initialize the URI attribute of a Flyte `Blob` object. Note that Flyte objects are not Python objects. They exist at the workflow level and are used to pass data between task containers. For more details, see [Flyte Core Language Specification > Literals](../../api-reference/flyteidl#flyteidlcoretypesproto).
* The `Blob` object is passed to `task_2`.
* Because the type of the input parameter of `task_2` is `FlyteFile`, {{< key product_name >}} converts the `Blob` back into a `FlyteFile` and sets the `remote_source` attribute of that `FlyteFile` to the URI of the `Blob` object.
* Inside `task_2` you can now perform a [`FlyteFile.open()`](../../api-reference/flytekit-sdk/packages/flytekit.types.file.file#open) and read the file contents.

### Local directory example

Below is an equivalent local example for `FlyteDirectory`. The process of passing the `FlyteDirectory` between tasks is essentially identical to the `FlyteFile` example above.

```python
@{{< key kit_as >}}.task
def task1() -> {{< key kit_as >}}.FlyteDirectory: # Create new local directory
    p = os.path.join(current_context().working_directory, "my_new_directory")
    os.makedirs(p)

    # Create and write to two files
    with open(os.path.join(p, "file_1.txt"), 'w') as file1:
        file1.write("This is file 1.")
    with open(os.path.join(p, "file_2.txt"), 'w') as file2:
        file2.write("This is file 2.")

    return {{< key kit_as >}}.FlyteDirectory(p)

@{{< key kit_as >}}.task
def task2(fd: {{< key kit_as >}}.FlyteDirectory): # Get a list of the directory contents using os to return strings
    items = os.listdir(fd)
    print(type(items[0]))

    # Get a list of the directory contents using FlyteDirectory to return FlyteFiles
    files = {{< key kit_as >}}.FlyteDirectory.listdir(fd)
    print(type(files[0]))
    with open(files[0], mode="r") as f:
        d = f.read()
    print(f"The first line in the first file is: {d}")

@{{< key kit_as >}}.workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

{{< /markdown >}}
{{< /variant >}}

{{< variant serverless >}}
{{< markdown >}}

> [!NOTE] Upload location
> With {{< key product_name >}} Serverless, the remote location to which `FlyteFile` and `FlyteDirectory` upload container-local files is always a randomly generated (universally unique) location in {{< key product_name >}}'s internal object store. It cannot be changed.
>
> With {{< key product_name >}} BYOC, the upload location is configurable.
> See [FlyteFile and FlyteDirectory > Changing the data upload location](../data-input-output/flyte-file-and-flyte-directory#changing-the-data-upload-location).

{{< /markdown >}}
{{< /variant >}}

{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

## Changing the data upload location

> [!NOTE] Upload location
> With {{< key product_name >}} Serverless, the remote location to which `FlyteFile` and `FlyteDirectory` upload container-local
> files is always a randomly generated (universally unique) location in {{< key product_name >}}'s internal object store. It cannot be changed.
>
> With {{< key product_name >}} BYOC, the upload location is configurable.

By default, {{< key product_name >}} uploads local files or directories to the default **raw data store** ({{< key product_name >}}'s dedicated internal object store).
However, you can change the upload location by setting the raw data prefix to your own bucket or specifying the `remote_path` for a `FlyteFile` or `FlyteDirectory`.

> [!NOTE] Setting up your own object store bucket
> For details on how to set up your own object store bucket, consult the direction for your cloud provider:
>
> * [Enabling AWS S3](../integrations/enabling-aws-resources/enabling-aws-s3)
> * [Enabling Google Cloud Storage](../integrations/enabling-gcp-resources/enabling-google-cloud-storage)
> * [Enabling Azure Blob Storage](../integrations/enabling-azure-resources/enabling-azure-blob-storage)

### Changing the raw data prefix

If you would like files or directories to be uploaded to your own bucket, you can specify the AWS, GCS, or Azure bucket in the **raw data prefix** parameter at the workflow level on registration or per execution on the command line or in the UI.
This setting can be done at the workflow level on registration or per execution on the command line or in the UI.

<!-- TODO See [Raw data prefix]() for more information. -->

{{< key product_name >}} will create a directory with a unique, random name in your bucket for each `FlyteFile` or `FlyteDirectory` data write to guarantee that you never overwrite your data.

### Specifying `remote_path` for a `FlyteFile` or `FlyteDirectory`

If you specify the `remote_path` when initializing your `FlyteFile` (or `FlyteDirectory`), the underlying data is written to that precise location with no randomization.

> [!NOTE] Using remote_path will overwrite data
> If you set `remote_path` to a static string, subsequent runs of the same task will overwrite the file.
> If you want to use a dynamically generated path, you will have to generate it yourself.

{{< /markdown >}}
{{< /variant >}}

## Remote examples

### Remote file example

In the example above, we started with a local file.
To preserve that file across the task boundary, {{< key product_name >}} uploaded it to the {{< key product_name >}} object store before passing it to the next task.

You can also _start with a remote file_, simply by initializing the `FlyteFile` object with a URI pointing to a remote source. For example:

```python
@{{< key kit_as >}}.task
def task_1() -> {{< key kit_as >}}.FlyteFile:
    remote_path = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
    return {{< key kit_as >}}.FlyteFile(path=remote_path)
```

In this case, no uploading is needed because the source file is already in a remote location.
When the object is passed out of the task, it is converted into a `Blob` with the remote path as the URI.
After the `FlyteFile` is passed to the next task, you can call `FlyteFile.open()` on it, just as before.

If you don't intend on passing the `FlyteFile` to the next task, and rather intend to open the contents of the remote file within the task, you can use `from_source`.

```python
@{{< key kit_as >}}.task
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

```python
@{{< key kit_as >}}.task
def task1() -> {{< key kit_as >}}.FlyteDirectory:
    p = "https://people.sc.fsu.edu/~jburkardt/data/csv/"
    return {{< key kit_as >}}.FlyteDirectory(p)

@{{< key kit_as >}}.task
def task2(fd: {{< key kit_as >}}.FlyteDirectory): # Get a list of the directory contents and display the first csv
    files = {{< key kit_as >}}.FlyteDirectory.listdir(fd)
    with open(files[0], mode="r") as f:
    d = f.read()
    print(f"The first csv is: \n{d}")

@{{< key kit_as >}}.workflow
def workflow():
    fd = task1()
    task2(fd=fd)
```

## Streaming

In the above examples, we showed how to access the contents of `FlyteFile` by calling `FlyteFile.open()`.
The object returned by `FlyteFile.open()` is a stream. In the above examples, the files were small, so a simple `read()` was used.
But for large files, you can iterate through the contents of the stream:

```python
@{{< key kit_as >}}.task
def task_1() -> {{< key kit_as >}}.FlyteFile:
    remote_path = "https://sample-videos.com/csv/Sample-Spreadsheet-100000-rows.csv"
    return {{< key kit_as >}}.FlyteFile(path=remote_path)

@{{< key kit_as >}}.task
def task_2(ff: {{< key kit_as >}}.FlyteFile):
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

```python
@{{< key kit_as >}}.task
def task_2(ff: {{< key kit_as >}}.FlyteFile):
    with open(ff, mode="r") as f
    file_contents= f.read()
```

> [!NOTE] open() vs ff.open()
> Note the difference between
>
> `ff.open(mode="r")`
>
> and
>
> `open(ff, mode="r")`
>
> The former calls the `FlyteFile.open()` method and returns an iterator without downloading the file.
> The latter calls the built-in Python function `open()`, downloads the specified `FlyteFile` to the local container file system,
> and returns a handle to that file.
>
> Many other Python file operations (essentially, any that accept an `os.PathLike` object) can also be performed on a `FlyteFile`
> object and result in an automatic download.
>
> See [Downloading with FlyteFile and FlyteDirectory](./downloading-with-ff-and-fd) for more information.

### Explicit downloading

You can also explicitly download a `FlyteFile` to the local container file system by calling `FlyteFile.download()`:

```python
@{{< key kit_as >}}.task
def task_2(ff: {{< key kit_as >}}.FlyteFile):
    local_path = ff.download()
```

This method is typically used when you want to download the file without immediately reading it.

<!-- TODO: Explain:
classmethod FlyteFile.from_source()
classmethod FlyteFile.new_remote_file()

classmethod FlyteDirectory.from_source()
classmethod FlyteDirectory.listdir()
classmethod FlyteDirectory.new_remote()

FlyteDirectory.crawl()
FlyteDirectory.new_dir()
FlyteDirectory.new_file()
-->

## Typed aliases

The [{{< key kit_name >}} SDK](../../api-reference/union-sdk) defines some aliases of `FlyteFile` with specific type annotations.
Specifically, `FlyteFile` has the following [aliases for specific file types](../../api-reference/flytekit-sdk/packages/flytekit.types.file.file):

* `HDF5EncodedFile`
* `HTMLPage`
* `JoblibSerializedFile`
* `JPEGImageFile`
* `PDFFile`
* `PNGImageFile`
* `PythonPickledFile`
* `PythonNotebook`
* `SVGImageFile`

Similarly, `FlyteDirectory` has the following [aliases](../../api-reference/flytekit-sdk/packages/flytekit.types.directory.types):

* `TensorboardLogs`
* `TFRecordsDirectory`

These aliases can optionally be used when handling a file or directory of the specified type, although the object itself will still be a `FlyteFile` or `FlyteDirectory`.
The aliased versions of the classes are syntactic markers that enforce agreement between type annotations in the signatures of task functions, but they do not perform any checks on the actual contents of the file.
