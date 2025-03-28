# Importing APIs

You can import Python APIs and host them on the site. To do that you will use
the `tools/api_generator` to parse and create the appropriate markdowns.

Please refer to [`api_generator/README`](tools/api_generator/README.md) for more
details.

## API naming convention

All the buildable APIs are at the root in the form:

    Makefile.api.<api_name>

To build it, run `make -f Makefile.api.<your_api>` and observe the setup
requirements in the readme above.

## Package Resource Resolution

When scanning the packages we need to know when to include or exclude an object
(class, function, variable) from the documentation. The parser will follow this
workflow to decide, in order, if the resource must be in or out:

1. `__all__: List[str]` package-level variable is present: Only resources
   listed will be exposed. All other resources are excluded.

   Example:

       from http import HTTPStatus, HTTPMethod

       __all__ = ["HTTPStatus", "LocalThingy"]

       class LocalThingy:
          ...

       class AnotherLocalThingy:
          ...

   In this example only `HTTPStatus` and `LocalThingy` will show in the docs.
   Both `HTTPMethod` and `AnotherLocalThingy` are ignored.

2. If `__all__` is not present, these rules are observed:

    - All imported packages are ignored
    - All objects starting with `_` are ignored

   Example:

       from http import HTTPStatus, HTTPMethod

       class _LocalThingy:
          ...

       class AnotherLocalThingy:
          ...

       def _a_func():
          ...

       def b_func():
          ...

    In this example only `AnotherLocalThingy` and `b_func` will show in the docs.
    Neither none of the imports nor `_LocalThingy` will show in the documention

> Note: if you either have no resources without a `_` nor an `__all__` to export
> blocked resources (imports or starting with `_`) the package will have no content
> and will not be generated.
