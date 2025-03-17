---
title: Image
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Image

**Package:** `flytekit.extend`

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
def Image(
    name: str,
    fqn: str,
    tag: Optional[str],
    digest: Optional[str],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `fqn` | `str` |
| `tag` | `Optional[str]` |
| `digest` | `Optional[str]` |
## Methods

### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |
### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |
### look_up_image_info()

```python
def look_up_image_info(
    name: str,
    image_identifier: str,
    allow_no_tag_or_digest: bool,
):
```
Creates an `Image` object from an image identifier string or a path to an ImageSpec yaml file.

This function is used when registering tasks/workflows with Admin. When using
the canonical Python-based development cycle, the version that is used to
register workflows and tasks with Admin should be the version of the image
itself, which should ideally be something unique like the git revision SHA1 of
the latest commit.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `image_identifier` | `str` |
| `allow_no_tag_or_digest` | `bool` |
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
):
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |
### to_dict()

```python
def to_dict(
    encode_json,
):
```
| Parameter | Type |
|-|-|
| `encode_json` |  |
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
):
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |
