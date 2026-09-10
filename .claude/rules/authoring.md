---
paths:
  - "content/**/*.md"
  - "linkmap/**"
  - "layouts/partials/**"
  - "unionai-docs-infra/layouts/partials/**"
---

# Authoring content

## API-reference autolinking

Inline `` `code` `` and Python code blocks are linked to their API reference **at runtime in the
browser**, by `inline-code-linker.js` and `codeblock-linker.js`, resolving against
`linkmap/*-linkmap.json`. The linkers load on every page.

**Do not write explicit Markdown links for identifiers the autolinker already handles.** Write
the bare backticked identifier and let the linker wrap it.

```markdown
✅  A `flyte.io.File` is a reference to an offloaded file.
✅  Call `flyte.init()` before submitting a run.

❌  A [`flyte.io.File`](../../api-reference/flyte-sdk/packages/flyte.io/file) is a reference …
❌  Call [`flyte.init()`](../../api-reference/flyte-sdk/packages/flyte/_index#init) …
```

## What the linker matches

In inline code, against the exact `<code>` text:

- Fully-qualified identifiers from any loaded linkmap — `flyte.io.File`, `flyte.report.log()`,
  `flyte.errors.OOMError`, `flyteplugins.bigquery.BigQueryConfig`.
- A trailing `()` is stripped before lookup, so `` `flyte.init()` `` and `` `flyte.init` `` both link.
- A leading `@` is stripped, so the decorator form works.
- `ClassName.method` falls back to `<class-url>#method` when the class is in the linkmap.

## What it does not match — keep an explicit link

- Link text that isn't a single pure backticked identifier: `` [`Resources` API reference](…) ``,
  `` [`Trigger` and `Cron`](…) ``.
- Bare short names such as `` `Trigger` `` or `` `Resources` `` — the **SDK** linkmap emits only
  fully-qualified keys, so prefer `` `flyte.Trigger` ``. (Plugin linkmaps do emit both forms.)
- Anchors that aren't `#methodname`.
- Cross-page links (`./other-page`) and non-API-ref URLs.

**To check whether an identifier is autolinkable, grep `linkmap/*.json` for it.** If it is there,
drop the explicit `[...](…)` wrapper.

## Other authoring patterns

### Notices

```markdown
> [!NOTE] Title
> Content here

> [!WARNING] Title
> Warning content
```

### Python example pages

```yaml
---
layout: py_example
example_file: /path/to/file.py
run_command: union run --remote path/to/file.py main
source_location: https://github.com/unionai/unionai-examples/tree/main/path
---
```

### Jupyter notebooks

```yaml
---
jupyter_notebook: /path/to/notebook.ipynb
---
```
