---
title: flytekit.tools.fast_registration
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.fast_registration

## Directory

### Classes

| Class | Description |
|-|-|
| [`FastPackageOptions`](../flytekit.tools.fast_registration/fastpackageoptions) | FastPackageOptions is used to set configuration options when packaging files. |

### Methods

| Method | Description |
|-|-|
| [`compress_tarball()`](#compress_tarball) | Compress code tarball using pigz if available, otherwise gzip. |
| [`compute_digest()`](#compute_digest) | Walks the entirety of the source dir to compute a deterministic md5 hex digest of the dir contents. |
| [`download_distribution()`](#download_distribution) | Downloads a remote code distribution and overwrites any local files. |
| [`fast_package()`](#fast_package) | Takes a source directory and packages everything not covered by common ignores into a tarball. |
| [`get_additional_distribution_loc()`](#get_additional_distribution_loc) |  |
| [`print_ls_tree()`](#print_ls_tree) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `FAST_FILEENDING` | `str` |  |
| `FAST_PREFIX` | `str` |  |
| `PICKLE_FILE_PATH` | `str` |  |

## Methods

#### compress_tarball()

```python
def compress_tarball(
    source: os.PathLike,
    output: os.PathLike,
)
```
Compress code tarball using pigz if available, otherwise gzip


| Parameter | Type | Description |
|-|-|-|
| `source` | `os.PathLike` | |
| `output` | `os.PathLike` | |

#### compute_digest()

```python
def compute_digest(
    source: Union[os.PathLike, List[os.PathLike]],
    filter: Optional[callable],
) -> str
```
Walks the entirety of the source dir to compute a deterministic md5 hex digest of the dir contents.


| Parameter | Type | Description |
|-|-|-|
| `source` | `Union[os.PathLike, List[os.PathLike]]` | |
| `filter` | `Optional[callable]` | |

#### download_distribution()

```python
def download_distribution(
    additional_distribution: str,
    destination: str,
)
```
Downloads a remote code distribution and overwrites any local files.


| Parameter | Type | Description |
|-|-|-|
| `additional_distribution` | `str` | |
| `destination` | `str` | |

#### fast_package()

```python
def fast_package(
    source: os.PathLike,
    output_dir: os.PathLike,
    deref_symlinks: bool,
    options: Optional[FastPackageOptions],
) -> os.PathLike
```
Takes a source directory and packages everything not covered by common ignores into a tarball
named after a hexdigest of the included files.


| Parameter | Type | Description |
|-|-|-|
| `source` | `os.PathLike` | |
| `output_dir` | `os.PathLike` | |
| `deref_symlinks` | `bool` | |
| `options` | `Optional[FastPackageOptions]` | The CopyFileDetection option set to None :return os.PathLike: |

#### get_additional_distribution_loc()

```python
def get_additional_distribution_loc(
    remote_location: str,
    identifier: str,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `remote_location` | `str` | |
| `identifier` | `str` | |

#### print_ls_tree()

```python
def print_ls_tree(
    source: os.PathLike,
    ls: typing.List[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `source` | `os.PathLike` | |
| `ls` | `typing.List[str]` | |

