---
title: API docs
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# API docs

You can import Python APIs and host them on the site. To do that you will use
the `tools/api_generator` to parse and create the appropriate markdown.

Please refer to [`api_generator/README`](../../../tools/api_generator/README.md) for more details.

## API naming convention

All the buildable APIs are at the root in the form:

`Makefile.api.<api_name>`

To build it, run `make -f Makefile.api.<your_api>` and observe the setup
requirements in the `README.md` file above.

## Package Resource Resolution

When scanning the packages we need to know when to include or exclude an object
(class, function, variable) from the documentation. The parser will follow this
workflow to decide, in order, if the resource must be in or out:

1. `__all__: List[str]` package-level variable is present: Only resources
   listed will be exposed. All other resources are excluded.

   Example:

   ```python
   from http import HTTPStatus, HTTPMethod

   __all__ = ["HTTPStatus", "LocalThingy"]

   class LocalThingy:
      ...

   class AnotherLocalThingy:
      ...
   ```

   In this example only `HTTPStatus` and `LocalThingy` will show in the docs.
   Both `HTTPMethod` and `AnotherLocalThingy` are ignored.

2. If `__all__` is not present, these rules are observed:

    - All imported packages are ignored
    - All objects starting with `_` are ignored

   Example:

   ```python
   from http import HTTPStatus, HTTPMethod

   class _LocalThingy:
      ...

   class AnotherLocalThingy:
      ...

   def _a_func():
      ...

   def b_func():
      ...
   ```

   In this example only `AnotherLocalThingy` and `b_func` will show in the docs.
   Neither none of the imports nor `_LocalThingy` will show in the documentation.

## Tips and Tricks

1. If you either have no resources without a `_` nor an `__all__` to
   export blocked resources (imports or starting with `_`, the package will have no content and thus will not be generated.

2. If you want to export something you `from ___ import ____` you _must_
   use `__all__` to add the private import to the public list.

3. If all your methods follow the Python convention of everything private starts
   with `_` and everything you want public does not, you do not need to have a
   `__all__` allow list.
