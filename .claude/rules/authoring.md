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
- Short **class** names — `` `Trigger` ``, `` `TaskEnvironment` ``, `` `BigQueryConfig` ``. Every
  linkmap, SDK and plugin alike, keys classes under both the full and the short name.
- A trailing `()` is stripped before lookup, so `` `flyte.init()` `` and `` `flyte.init` `` both link.
- A leading `@` is stripped, so the decorator form works.
- `ClassName.method` falls back to `<class-url>#method` when the class is in the linkmap.

The split is by kind, not by linkmap: **functions are keyed only by their fully-qualified name**,
in every linkmap. The generator leaves short function names out on purpose, because names like
`init`, `run` and `log` are too generic to link safely.

## What it does not match

- Short **function** names, bare or module-qualified — `` `nsys_profile` ``, `` `nsys.range` ``,
  `` `nvtx.mark()` ``. The `ClassName.method` fallback does not cover `module.function`.
- Link text that isn't a single pure backticked identifier: `` [`Resources` API reference](…) ``,
  `` [`Trigger` and `Cron`](…) ``.
- Anchors that aren't `#methodname`.
- Cross-page links (`./other-page`) and non-API-ref URLs.

A short class name that two linkmaps both define (`Agent`, `FlyteModel`) resolves to whichever
loads last. Use the fully-qualified name when the short one is ambiguous.

## Sigils

When the text you want to show isn't a linkmap key, use a sigil instead of an explicit link. The
whole backticked span must be the sigil:

- `` `[[target|display]]` `` — link to `target` (a linkmap key, or matched by its last segment)
  and render `display`. Use it to keep a short name in prose:
  `` `[[flyteplugins.nsight.nsys.range|nsys.range]]` ``, `` `[[flyte.Trigger|Trigger]]` ``.
- `` `[[X]]` `` — force a link by last-segment lookup and render `X`.
- `` `{{X}}` `` — render `X` with no link, even if it is in the linkmap.

**Not inside a table cell:** the `|` in `[[target|display]]` splits the cell. Link the first
mention in the prose above the table, or link the API reference page.

**To check whether an identifier is autolinkable, grep `linkmap/*.json` for it** — fully-qualified
for functions, either form for classes. If it is there, drop the explicit `[...](…)` wrapper.

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
