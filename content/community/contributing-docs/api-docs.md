---
title: API docs
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# API docs

You can import Python APIs and host them on the site. To do that you will use
the `tools/api_generator` to parse and create the appropriate markdown.

Please refer to [`api_generator/README`](https://github.com/unionai/docs/blob/main/tools/api_generator/README.md) for more details.

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

## Enabling auto-linking for plugins

When you generate API documentation for a plugin, the build process creates two data files that enable automatic linking from documentation to API references:

- `data/{name}.yaml` - Hugo data file for server-side code block linking
- `static/{name}-linkmap.json` - JSON file for client-side inline code linking

For plugins, use the `--short-names` flag when generating API docs (already enabled in `Makefile.api.plugins`). This generates both fully qualified names (`flyteplugins.wandb.wandb_init`) and short names (`wandb_init`) in the linkmap, allowing docs to reference APIs without the full package path.

To enable auto-linking for a new plugin, you need to register these files in two places:

### 1. Server-side code block linking

Edit `layouts/partials/autolink-python.html` and add your plugin's data file to the merge chain:

```go-html-template
{{- /* Load and merge all API data sources */ -}}
{{- $flyteapi := dict "identifiers" (dict) "methods" (dict) "packages" (dict) -}}
{{- with site.Data.flytesdk -}}
    {{- $flyteapi = merge $flyteapi (dict "identifiers" (.identifiers | default dict) "methods" (.methods | default dict) "packages" (.packages | default dict)) -}}
{{- end -}}
{{- with site.Data.wandb -}}
    {{- $flyteapi = merge $flyteapi (dict "identifiers" (merge $flyteapi.identifiers (.identifiers | default dict)) "methods" (merge $flyteapi.methods (.methods | default dict)) "packages" (merge $flyteapi.packages (.packages | default dict))) -}}
{{- end -}}
{{- /* Add your plugin here following the same pattern */ -}}
```

### 2. Client-side inline code linking

Edit `static/js/inline-code-linker.js` and add your plugin's linkmap file to the `linkmapFiles` array:

```javascript
const linkmapFiles = ['flytesdk-linkmap.json', 'wandb-linkmap.json'];
// Add your plugin's linkmap file here, e.g., 'myplugin-linkmap.json'
```

### How auto-linking works

Once configured, the following will be automatically linked:

- **Code blocks**: Python code in fenced code blocks will have API references linked. For example, `wandb_init()` in a Python code block will link to its API documentation.

- **Inline code**: Inline code like `` `wandb_init()` `` will be linked. The `@` prefix for decorators and `()` suffix for functions are automatically stripped for matching.

The linkmap files contain mappings from identifiers to their API documentation URLs. Both short names (e.g., `wandb_init`) and fully qualified names (e.g., `flyteplugins.wandb.wandb_init`) are supported if included in the linkmap.
