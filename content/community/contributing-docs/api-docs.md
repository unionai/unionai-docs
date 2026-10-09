---
title: API docs
description: Generate API reference pages from Python docstrings, and control how inline identifiers become links.
icon: braces
weight: 8
variants: +flyte +union
---

# API docs

You can import Python APIs and host them on the site. To do that you will use
the `unionai-docs-infra/tools/api_generator` to parse and create the appropriate markdown.

Please refer to [`api_generator/README`](https://github.com/unionai/unionai-docs-infra/blob/main/tools/api_generator/README.md) for more details.

## API naming convention

All the buildable APIs are defined in Makefiles of the form:

`unionai-docs-infra/Makefile.api.<api_name>`

To build it, run `make -f unionai-docs-infra/Makefile.api.<your_api>` and observe the setup
requirements in the `README.md` file above. Alternatively, `make update-api-docs` will regenerate all API docs.

## Package resource resolution

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

## Tips and tricks

1. If you either have no resources without a `_` nor an `__all__` to
   export blocked resources (imports or starting with `_`, the package will have no content and thus will not be generated.

2. If you want to export something you `from ___ import ____` you _must_
   use `__all__` to add the private import to the public list.

3. If all your methods follow the Python convention of everything private starts
   with `_` and everything you want public does not, you do not need to have a
   `__all__` allow list.

## Auto-linking

Every package that the API generator processes, the SDK and all plugins, emits a linkmap file (`linkmap/<name>-linkmap.json`) that maps identifiers to their API reference URLs. Two scripts in the shared infra consume those linkmaps at runtime to turn mentions of those identifiers in docs prose and code samples into links to the API reference:

- `assets/js/inline-code-linker.js`: wraps inline `` `code` `` whose text matches a linkmap key.
- `assets/js/codeblock-linker.js`: wraps matching identifiers inside Python code blocks based on the block's `import` statements.

**Registration is automatic.** At build time, `layouts/_default/baseof.html` scans `linkmap/` and exposes every `*-linkmap.json` file as `window.__LINKMAP_SOURCES`. Both linker scripts read that variable and fetch the linkmaps on page load. There is no per-package wiring step: adding an entry to `api-packages.toml` is enough; the generator produces its linkmap and the linkers pick it up.

### Short vs. fully-qualified names

The generator runs with `--short-names` for the SDK (`tools/api_sdk_generate.py`) and for plugins (`Makefile.api.plugins`), so every linkmap follows the same rule. Whether a short name links depends on whether the identifier is a class or a function, not on which linkmap it is in:

- **Classes** are keyed under both the fully-qualified and the short name, so `` `flyte.Trigger` `` and `` `Trigger` `` both link.
- **Functions** are keyed only by their fully-qualified name, in every linkmap. `` `flyte.init()` `` links; a bare `` `init()` `` does not. The generator leaves short function names out on purpose, because names like `init`, `run`, and `log` are too generic to link safely.

A short class name that two linkmaps both define, such as `Agent`, resolves to whichever linkmap loads last. Use the fully-qualified name when the short one is ambiguous.

To check whether an identifier autolinks, search `linkmap/*.json` for it: fully-qualified for functions, either form for classes.

### How auto-linking works

- **Inline code**: `` `flyte.io.File` `` (or the short class name `` `File` ``) is wrapped with a link to its API reference. A trailing `()` and a leading `@` (for decorators) are stripped before lookup. `ClassName.method` syntax falls back to `<class-url>#method` when the class is in the linkmap. That fallback does not cover `module.function`: a module-qualified short function name such as `nsys.range` does not link.
- **Code blocks**: identifiers inside Python code blocks are linked based on the block's `from … import …` and `import …` statements: only names that resolve through one of those imports get wrapped.

### Sigils for inline code

When the text you want to show is not a linkmap key, use a sigil inside the backticks instead of writing an explicit link. The whole backticked span must be the sigil:

```markdown
`[[flyteplugins.nsight.nsys.range|nsys.range]]`   links to the target, renders "nsys.range"
`[[Trigger]]`                                     links by last-segment lookup, renders "Trigger"
`{{Trigger}}`                                     renders "Trigger" with no link
```

- **Target and display** (double brackets with a `|`): links to the target, either a linkmap key or a match on its last segment, and renders the display text. Use it to keep a short function name in prose.
- **Double brackets**: forces a link by last-segment lookup and renders the text inside the brackets.
- **Double braces**: renders the text inside the braces with no link, even if it is in a linkmap.

Don't use the target-and-display form inside a Markdown table cell: its `|` splits the cell. Link the first mention in the prose above the table instead.
