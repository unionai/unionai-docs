---
title: "Component gallery — internal preview (do not link)"
variants: -flyte +union
noindex: true
hidden: true
toc_max: 3
---

# Component gallery

An internal, un-indexed reference of every typographic element and content
component available on the Union.ai docs site, rendered in the live theme. It
exists so design can review the full component set in one place.

> [!NOTE] This page is internal
> It is excluded from the sitemap, marked `noindex,nofollow`, and is not linked
> from any navigation. It renders only in the `union` variant and is intended
> for preview builds only — it is never merged to production. Reach it by direct
> URL only.

For each component the raw markup is shown first, followed by its live
rendering.

---

## Typography

### Headings

The page title above is styled as an **h1**. Headings `h2`–`h6` render as
follows:

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

Hover any `h2`–`h6` to reveal its `#` anchor affordance.

### Body text and inline elements

A standard paragraph mixing **bold text**, *italic text*, ***bold italic***,
`inline code`, an [inline link](https://union.ai), and
~~strikethrough~~. Sentences wrap and flow at the site's default measure and
line height. Inline API identifiers such as `flyte.init()` and `flyte.io.File`
are auto-linked at runtime by the inline-code linker.

A hard line break can be forced with a trailing backslash or two spaces.\
This sentence sits on the line directly below the previous one.

### Unordered list

- First item
- Second item, with a longer line of text so you can see how list items wrap
  onto a second line and how the hanging indent behaves
  - Nested item one
  - Nested item two
    - Third-level item
- Third item

### Ordered list

1. Install the CLI
2. Authenticate against your endpoint
3. Submit your first run
   1. Define a `TaskEnvironment`
   2. Decorate a task with `@env.task`
   3. Call `flyte.run(...)`

### Blockquote

> This is a plain blockquote. Use it for pulled-out asides or quoted material.
> It can span multiple lines and continues with the same left border and
> padding treatment throughout.

### Table

| Component      | Type       | Container? | Typical use                       |
| -------------- | ---------- | ---------- | --------------------------------- |
| `note`         | Notice     | Yes        | Informational callouts            |
| `warning`      | Notice     | Yes        | Cautionary callouts               |
| `tabs` / `tab` | Layout     | Yes        | Alternate instructions            |
| `grid`         | Layout     | Yes        | Card layouts on landing pages     |
| `badge`        | Inline     | Yes        | Status labels inside tables       |
| `code`         | Code       | No         | Embed a runnable example file     |

### Horizontal rule

Content above the rule.

---

Content below the rule.

---

## Notices

Two mechanisms produce the same notice component: the markdown-native GitHub
alert blockquote (preferred house style) and the `note` / `warning` shortcodes.

### Native alert blockquotes

```text
> [!NOTE] Optional title
> Body of the note. Supports **markdown** and multiple lines.

> [!WARNING] Optional title
> Body of the warning.

> [!CAUTION] Optional title
> Body of the caution.
```

> [!NOTE] This is a note
> Body of the note. Supports **markdown**, `inline code`, and
> [links](https://union.ai). It can span multiple paragraphs.

> [!WARNING] This is a warning
> Use this for operations that need care — for example, an action that is
> **irreversible**.

> [!CAUTION] This is a caution
> The strongest emphasis level, for destructive or dangerous actions.

### Notice shortcodes

```text
{{</* note "Optional title" */>}}
Body of the note.
{{</* /note */>}}

{{</* warning "Optional title" */>}}
Body of the warning.
{{</* /warning */>}}
```

{{< note "Run the CLI without installing" >}}
If you have [`uv`](https://docs.astral.sh/uv/) installed, run
`uvx flyte --version` to invoke the CLI without a local install.
{{< /note >}}

{{< warning "Heads up" >}}
This operation is **irreversible**. Double-check the target before continuing.
{{< /warning >}}

---

## Code

### Fenced code block

Standard fenced blocks are rendered with syntax highlighting, a filename-less
header, and a copy button.

```python
import flyte

env = flyte.TaskEnvironment(name="hello_env")

@env.task
def main(x: int) -> int:
    return x * 2
```

```bash
uv run flyte run hello.py main --x 10
```

### `code` shortcode — whole file

Embeds a runnable example straight from the `unionai-examples` repo, with a
filename header, GitHub source link, and copy buttons.

```text
{{</* code file="/unionai-examples/v2/user-guide/getting-started/hello.py" lang="python" */>}}
```

{{< code file="/unionai-examples/v2/user-guide/getting-started/hello.py" lang="python" >}}

### `code` shortcode — fragment with highlight

Pulls only the lines between named `docs-fragment` markers, and emphasizes a
line range.

```text
{{</* code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" lang="python" fragment="task-env" highlight="2-3" */>}}
```

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" lang="python" fragment="task-env" highlight="2-3" >}}

---

## Tabs

Use tabs for alternate sets of instructions (for example, programmatic vs. CLI).
Fenced code inside a tab must be wrapped in a `{{</* markdown */>}}` container.

```text
{{</* tabs "gallery-demo" */>}}
{{</* tab "Programmatic" */>}}
{{</* markdown */>}}
​```python
flyte.init(endpoint="dns:///your-endpoint")
​```
{{</* /markdown */>}}
{{</* /tab */>}}
{{</* tab "CLI" */>}}
{{</* markdown */>}}
​```bash
flyte create config --endpoint https://your-endpoint
​```
{{</* /markdown */>}}
{{</* /tab */>}}
{{</* /tabs */>}}
```

{{< tabs "gallery-demo" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
import flyte

flyte.init(endpoint="dns:///your-endpoint")
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
```bash
flyte create config --endpoint https://your-endpoint
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

---

## Grid and link cards

`link-card`s are clickable cards, usually arranged in a `grid`. The `cols`
parameter sets the number of columns.

```text
{{</* grid cols="3" */>}}
{{</* link-card target="#" icon="rocket" title="Quickstart" */>}}
Get running fast.
{{</* /link-card */>}}
{{</* /grid */>}}
```

{{< grid cols="3" >}}
{{< link-card target="#typography" icon="fonts" title="Typography" >}}
Headings, body text, lists, tables.
{{< /link-card >}}
{{< link-card target="#notices" icon="info-circle" title="Notices" >}}
Notes, warnings, and cautions.
{{< /link-card >}}
{{< link-card target="#code" icon="code-slash" title="Code" >}}
Fenced blocks and the code shortcode.
{{< /link-card >}}
{{< /grid >}}

A two-column grid (the default when `cols` is omitted):

{{< grid >}}
{{< link-card target="#tabs" icon="segmented-nav" title="Tabs" >}}
Alternate instruction sets.
{{< /link-card >}}
{{< link-card target="#callouts-and-inline-components" icon="tags" title="Inline components" >}}
Badges, buttons, dropdowns, icons.
{{< /link-card >}}
{{< /grid >}}

---

## Callouts and inline components

### Badges

Status labels, most often used inside tables. The positional argument selects a
Shoelace variant.

```text
{{</* badge "primary" */>}}Primary{{</* /badge */>}}
{{</* badge "success" */>}}Success{{</* /badge */>}}
{{</* badge "neutral" */>}}Neutral{{</* /badge */>}}
{{</* badge "warning" */>}}Warning{{</* /badge */>}}
{{</* badge "danger" */>}}Danger{{</* /badge */>}}
```

{{< badge "primary" >}}Primary{{< /badge >}}
{{< badge "success" >}}Success{{< /badge >}}
{{< badge "neutral" >}}Neutral{{< /badge >}}
{{< badge "warning" >}}Warning{{< /badge >}}
{{< badge "danger" >}}Danger{{< /badge >}}

### Button link

An external call-to-action button (opens in a new tab).

```text
{{</* button-link text="Get started" variant="primary" target="https://union.ai" */>}}
```

{{< button-link text="Get started" variant="primary" target="https://union.ai" >}}
{{< button-link text="Learn more" variant="default" target="https://union.ai" >}}

### Dropdown

A collapsible `<sl-details>` disclosure. The `icon` is an emoji shortcode name.

```text
{{</* dropdown title="Show the full example" icon="bento" */>}}
{{</* markdown */>}}
Hidden content, revealed on click.
{{</* /markdown */>}}
{{</* /dropdown */>}}
```

{{< dropdown title="Show the full example" icon="bento" >}}
{{< markdown >}}
This content is hidden until the disclosure is expanded. It can hold any
markdown, including fenced code:

```python
print("revealed")
```
{{< /markdown >}}
{{< /dropdown >}}

### Icons

Any [Shoelace icon](https://shoelace.style/components/icon) by name.

```text
{{</* icon "book" */>}} {{</* icon "rocket" */>}} {{</* icon "gear" */>}}
```

{{< icon "book" >}} &nbsp; {{< icon "rocket" >}} &nbsp; {{< icon "gear" >}} &nbsp; {{< icon "cloud-download" >}} &nbsp; {{< icon "terminal" >}}

### Download link

A download affordance. The target must live under `/_static/public/` or a
Union.ai GitHub repository.

```text
{{</* download "https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/getting-started/hello.py" "hello.py" "A minimal runnable example" */>}}
```

{{< download "https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/getting-started/hello.py" "hello.py" "A minimal runnable example" >}}

---

## Layout helpers

### Right-aligned block

```text
{{</* right */>}}
[Next →](#)
{{</* /right */>}}
```

{{< right >}}
<a href="#component-gallery">Back to top →</a>
{{< /right >}}

### Multiline block

Forces `<br>`-separated lines — handy inside tight table cells.

```text
{{</* multiline */>}}
Line one
Line two
{{</* /multiline */>}}
```

{{< multiline >}}
Line one
Line two
Line three
{{< /multiline >}}

### Variant-conditional content

The `variant` shortcode shows its body only in the listed variants. This page
is built as `union`, so the `union` block renders and a `flyte`-only block would
be omitted.

```text
{{</* variant union */>}}
{{</* markdown */>}}
Union-only content.
{{</* /markdown */>}}
{{</* /variant */>}}
```

{{< variant union >}}
{{< markdown >}}
This paragraph appears only in the **union** build — which is what you are
viewing now.
{{< /markdown >}}
{{< /variant >}}

### Product-name keys

Inline `key` lookups resolve to variant-specific product terminology.

- Product name: **{{< key product_name >}}**
- CLI: **{{< key cli >}}**
- Docs home (root): {{< docs_home root v2 >}}

---

## Media

An audio player (the `src` below is a placeholder, so the transport controls
render but no audio loads).

```text
{{</* audio "/_static/public/example.mp3" */>}}
```

{{< audio "/_static/public/example.mp3" >}}

---

## Not rendered here

A few components are structural or side-effecting and are intentionally *not*
rendered on this page:

- **`redirect`** — performs a client-side redirect, so rendering it would
  navigate away from this page.
- **`llm-readable-list`** / **`llm-bundle-note`** — depend on section-bundle
  frontmatter (`llm_readable_bundle: true`) and are only meaningful on real
  section index pages.
- **`py_class_ref`** / **`py_func_ref`** — render an identifier as inline code,
  e.g. {{< py_class_ref flyte.TaskEnvironment "TaskEnvironment" >}}.
