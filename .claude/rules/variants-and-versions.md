---
paths:
  - "content/**/*.md"
  - "versions.toml"
  - "makefile.inc"
  - "config.union.toml"
  - "config.flyte.toml"
  - "unionai-docs-infra/config.union.toml"
  - "unionai-docs-infra/config.flyte.toml"
---

# Variant gating and version lines

## Every page declares its variants, with both signs

```yaml
variants: +flyte +union      # both
variants: -flyte +union      # Union only
```

State a `+` **and** a `-` for each variant. A page that is neither allowed nor excluded warns at
build time; silence is not the default.

## Block-level gating uses different syntax from front matter

Front matter uses `+`/`-` prefixes. The shortcode takes a bare space-separated list of the
variants that *may* see the block:

```
{{< variant union >}}{{< markdown >}}Union-only text.{{< /markdown >}}{{< /variant >}}
```

Two traps that have both bitten:

- **Naming every variant guards nothing.** `{{< variant flyte union >}}` is equivalent to plain
  top-level markdown. Delete the wrapper rather than working around it.
- **Variant blocks do not nest.** An inner gated block is a build error, and the message names
  whatever construct sits at the failure point rather than the enclosing wrapper.

The whole `content/deployment/` tree is Union-only (`-flyte +union`) and does not exist on the
Flyte variant.

## `/docs/v2` lags `main` by design

A merged page is live on **`/docs/latest`**, not `/docs/v2`. `/docs/v2` is the newest *cut*.
A 404 on the stable URL right after merging is expected, not a failed deploy.

Content is versioned; **chrome is promoted**. A cut snapshots content only — theme and build
changes reach every version at once via the infra submodule pointer, and need no cut.
