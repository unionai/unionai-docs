---
title: Image
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Image

**Package:** `flytekit.configuration`

Image is a structured wrapper for task container images used in object serialization.

Attributes:
    name (str): A user-provided name to identify this image.
    fqn (str): Fully qualified image name. This consists of
        #. a registry location
        #. a username
        #. a repository name
        For example: `hostname/username/reponame`
    tag (str): Optional tag used to specify which version of an image to pull
    digest (str): Optional digest used to specify which version of an image to pull



```python
class Image(
    name: str,
    fqn: str,
    tag: Optional[str],
    digest: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `fqn` | `str` | |
| `tag` | `Optional[str]` | |
| `digest` | `Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `full` | `None` | " Return the full image name with tag or digest, whichever is available.  When using a tag the separator is `:` and when using a digest the separator is `@`. |
| `version` | `None` | Return the version of the image. This could be the tag or digest, whichever is available. |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`look_up_image_info()`](#look_up_image_info) | Creates an `Image` object from an image identifier string or a path to an ImageSpec yaml file. |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

### look_up_image_info()

```python
def look_up_image_info(
    name: str,
    image_identifier: str,
    allow_no_tag_or_digest: bool,
) -> Image
```
Creates an `Image` object from an image identifier string or a path to an ImageSpec yaml file.

This function is used when registering tasks/workflows with Admin. When using
the canonical Python-based development cycle, the version that is used to
register workflows and tasks with Admin should be the version of the image
itself, which should ideally be something unique like the git revision SHA1 of
the latest commit.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `image_identifier` | `str` | Either the full image identifier string e.g. somedocker.com/myimage or a path to a file containing a `ImageSpec`. |
| `allow_no_tag_or_digest` | `bool` | :rtype: Image |

### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

