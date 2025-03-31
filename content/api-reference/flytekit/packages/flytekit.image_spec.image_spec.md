---
title: flytekit.image_spec.image_spec
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.image_spec.image_spec

## Directory

### Classes

| Class | Description |
|-|-|
| [`CopyFileDetection`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_speccopyfiledetection) | Create a collection of name/value pairs. |
| [`ImageBuildEngine`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_specimagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`ImageSpec`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`ImageSpecBuilder`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_specimagespecbuilder) |  |
| [`Version`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_specversion) | This class abstracts handling of a project's versions. |
| [`cached_property`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_speccached_property) |  |

### Errors

| Exception | Description |
|-|-|
| [`FlyteAssertion`](.././flytekit.image_spec.image_spec#flytekitimage_specimage_specflyteassertion) | Assertion failed. |

### Methods

| Method | Description |
|-|-|
| [`abstractmethod()`](#abstractmethod) | A decorator indicating abstract methods. |
| [`asdict()`](#asdict) | Return the fields of a dataclass instance as a new dictionary mapping. |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`lru_cache()`](#lru_cache) | Least-recently-used cache decorator. |
| [`validate_container_registry_name()`](#validate_container_registry_name) | Validate Docker container registry name. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DOCKER_HUB` | `str` |  |
| `FLYTE_FORCE_PUSH_IMAGE_SPEC` | `str` |  |

## Methods

#### abstractmethod()

```python
def abstractmethod(
    funcobj,
)
```
A decorator indicating abstract methods.

Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.  abstractmethod() may be used to declare
abstract methods for properties and descriptors.

Usage:

class C(metaclass=ABCMeta):
@abstractmethod
def my_abstract_method(self, arg1, arg2, argN):
...


| Parameter | Type |
|-|-|
| `funcobj` |  |

#### asdict()

```python
def asdict(
    obj,
    dict_factory,
)
```
Return the fields of a dataclass instance as a new dictionary mapping
field names to field values.

Example usage::

@dataclass
class C:
x: int
y: int

c = C(1, 2)
assert asdict(c) == {'x': 1, 'y': 2}

If given, 'dict_factory' will be used instead of built-in dict.
The function applies recursively to field values that are
dataclass instances. This will also look into built-in containers:
tuples, lists, and dicts. Other objects are copied with 'copy.deepcopy()'.


| Parameter | Type |
|-|-|
| `obj` |  |
| `dict_factory` |  |

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

#### lru_cache()

```python
def lru_cache(
    maxsize,
    typed,
)
```
Least-recently-used cache decorator.

If *maxsize* is set to None, the LRU features are disabled and the cache
can grow without bound.

If *typed* is True, arguments of different types will be cached separately.
For example, f(decimal.Decimal("3.0")) and f(3.0) will be treated as
distinct calls with distinct results. Some types such as str and int may
be cached separately even when typed is false.

Arguments to the cached function must be hashable.

View the cache statistics named tuple (hits, misses, maxsize, currsize)
with f.cache_info().  Clear the cache and statistics with f.cache_clear().
Access the underlying function with f.__wrapped__.

See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)


| Parameter | Type |
|-|-|
| `maxsize` |  |
| `typed` |  |

#### validate_container_registry_name()

```python
def validate_container_registry_name(
    name: str,
) -> bool
```
Validate Docker container registry name.


| Parameter | Type |
|-|-|
| `name` | `str` |

## flytekit.image_spec.image_spec.CopyFileDetection

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.image_spec.image_spec.FlyteAssertion

Assertion failed.


```python
class FlyteAssertion(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.image_spec.image_spec.ImageBuildEngine

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


### Methods

| Method | Description |
|-|-|
| [`build()`](#build) |  |
| [`get_registry()`](#get_registry) |  |
| [`register()`](#register) |  |


#### build()

```python
def build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
)
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### get_registry()

```python
def get_registry()
```
#### register()

```python
def register(
    builder_type: str,
    image_spec_builder: flytekit.image_spec.image_spec.ImageSpecBuilder,
    priority: int,
)
```
| Parameter | Type |
|-|-|
| `builder_type` | `str` |
| `image_spec_builder` | `flytekit.image_spec.image_spec.ImageSpecBuilder` |
| `priority` | `int` |

## flytekit.image_spec.image_spec.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
class ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry. |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled. |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment. |
| [`image_name()`](#image_name) | Full image name with tag. |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec. |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process. |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process. |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory. |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process. |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
) -> ImageSpec
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `tag` |  | {{< multiline >}}Calculate a hash from the image spec. The hash will be the tag of the image.
We will also read the content of the requirement file and the source root to calculate the hash.
Therefore, it will generate different hash if new dependencies are added or the source code is changed.

Keep in mind the fields source_root and copy may be changed by update_image_spec_copy_handling, so when
you call this property in relation to that function matter will change the output.
{{< /multiline >}} |

## flytekit.image_spec.image_spec.ImageSpecBuilder

### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec. |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> typing.Optional[str]
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

## flytekit.image_spec.image_spec.Version

This class abstracts handling of a project's versions.

A :class:`Version` instance is comparison aware and can be compared and
sorted using the standard Python interfaces.

>>> v1 = Version("1.0a5")
>>> v2 = Version("1.0")
>>> v1
<Version('1.0a5')>
>>> v2
<Version('1.0')>
>>> v1 < v2
True
>>> v1 == v2
False
>>> v1 > v2
False
>>> v1 >= v2
False
>>> v1 <= v2
True


```python
class Version(
    version: str,
)
```
Initialize a Version object.



| Parameter | Type |
|-|-|
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `base_version` |  | {{< multiline >}}The "base version" of the version.

>>> Version("1.2.3").base_version
'1.2.3'
>>> Version("1.2.3+abc").base_version
'1.2.3'
>>> Version("1!1.2.3dev1+abc").base_version
'1!1.2.3'

The "base version" is the public version of the project without any pre or post
release markers.
{{< /multiline >}} |
| `dev` |  | {{< multiline >}}The development number of the version.

>>> print(Version("1.2.3").dev)
None
>>> Version("1.2.3.dev1").dev
1
{{< /multiline >}} |
| `epoch` |  | {{< multiline >}}The epoch of the version.

>>> Version("2.0.0").epoch
0
>>> Version("1!2.0.0").epoch
1
{{< /multiline >}} |
| `is_devrelease` |  | {{< multiline >}}Whether this version is a development release.

>>> Version("1.2.3").is_devrelease
False
>>> Version("1.2.3.dev1").is_devrelease
True
{{< /multiline >}} |
| `is_postrelease` |  | {{< multiline >}}Whether this version is a post-release.

>>> Version("1.2.3").is_postrelease
False
>>> Version("1.2.3.post1").is_postrelease
True
{{< /multiline >}} |
| `is_prerelease` |  | {{< multiline >}}Whether this version is a pre-release.

>>> Version("1.2.3").is_prerelease
False
>>> Version("1.2.3a1").is_prerelease
True
>>> Version("1.2.3b1").is_prerelease
True
>>> Version("1.2.3rc1").is_prerelease
True
>>> Version("1.2.3dev1").is_prerelease
True
{{< /multiline >}} |
| `local` |  | {{< multiline >}}The local version segment of the version.

>>> print(Version("1.2.3").local)
None
>>> Version("1.2.3+abc").local
'abc'
{{< /multiline >}} |
| `major` |  | {{< multiline >}}The first item of :attr:`release` or ``0`` if unavailable.

>>> Version("1.2.3").major
1
{{< /multiline >}} |
| `micro` |  | {{< multiline >}}The third item of :attr:`release` or ``0`` if unavailable.

>>> Version("1.2.3").micro
3
>>> Version("1").micro
0
{{< /multiline >}} |
| `minor` |  | {{< multiline >}}The second item of :attr:`release` or ``0`` if unavailable.

>>> Version("1.2.3").minor
2
>>> Version("1").minor
0
{{< /multiline >}} |
| `post` |  | {{< multiline >}}The post-release number of the version.

>>> print(Version("1.2.3").post)
None
>>> Version("1.2.3.post1").post
1
{{< /multiline >}} |
| `pre` |  | {{< multiline >}}The pre-release segment of the version.

>>> print(Version("1.2.3").pre)
None
>>> Version("1.2.3a1").pre
('a', 1)
>>> Version("1.2.3b1").pre
('b', 1)
>>> Version("1.2.3rc1").pre
('rc', 1)
{{< /multiline >}} |
| `public` |  | {{< multiline >}}The public portion of the version.

>>> Version("1.2.3").public
'1.2.3'
>>> Version("1.2.3+abc").public
'1.2.3'
>>> Version("1!1.2.3dev1+abc").public
'1!1.2.3.dev1'
{{< /multiline >}} |
| `release` |  | {{< multiline >}}The components of the "release" segment of the version.

>>> Version("1.2.3").release
(1, 2, 3)
>>> Version("2.0.0").release
(2, 0, 0)
>>> Version("1!2.0.0.post0").release
(2, 0, 0)

Includes trailing zeroes but not the epoch or any pre-release / development /
post-release suffixes.
{{< /multiline >}} |

## flytekit.image_spec.image_spec.cached_property

```python
class cached_property(
    func,
)
```
| Parameter | Type |
|-|-|
| `func` |  |

