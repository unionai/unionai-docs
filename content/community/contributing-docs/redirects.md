---
title: Redirects
description: Map a moved URL to its new location through the Cloudflare redirect lists.
icon: signpost-split
weight: 10
variants: +flyte +union
---

# Redirects

We use Cloudflare's Bulk Redirect to map URLs that moved to their new location,
so the user does not get a 404 using the old link.

Redirects are recorded in `unionai-docs-infra/redirects.csv`, one per line, in CSV format:

`<source_url>,<target_url>,<status>,<include_subdomains>,<subpath_matching>,<preserve_query_string>,<preserve_path_suffix>`

| Column | Meaning |
|---|---|
| `source_url` | the incoming URL, **without** `https://` |
| `target_url` | the full URL to send the user to, **including** `https://` |
| `status` | `301` or `302`. Use `301` only when the target is certain, `302` otherwise. Rows written by the automatic detector (`make update-redirects`, which `make dist` runs) use `302` |
| `include_subdomains` | `TRUE` / `FALSE` |
| `subpath_matching` | `TRUE` matches everything beneath the source path |
| `preserve_query_string` | `TRUE` keeps `?a=b` on the target |
| `preserve_path_suffix` | `TRUE` appends the matched subpath to the target. Cloudflare rejects this unless `subpath_matching` is also `TRUE` |

A real row:

```
docs.union.ai/administration,https://www.union.ai/docs/v2/union/user-guide/user-management,301,TRUE,TRUE,TRUE,TRUE
```

**Merging a `redirects.csv` change deploys nothing by itself.** The CSV lives in
`unionai-docs-infra`. The `deploy-redirects.yml` workflow in `unionai-docs` runs on a push to
`main` or `v1` that touches the `unionai-docs-infra` pointer or `versions.toml`, and pushes the
whole list to Cloudflare only if `redirects.csv` differs between the old and new pointer commits
or `versions.toml` changed. To ship a CSV change, bump the `unionai-docs-infra` pointer in
`unionai-docs` after the infra PR merges. Running the workflow manually also deploys.

To add a redirect, open a pull request in `unionai-docs-infra` changing `redirects.csv`. Two rules save review time:

- **Point at the page that actually serves**, not at a URL you know will redirect again. Chains
  are trimmed periodically and a new one undoes that work.
- **Mind the trailing slash.** An exact-match row misses the other form and produces a soft 404.
  Either set `subpath_matching` to `TRUE` or add both `/x` and `/x/`.

**Do not add rows for retired version pins.** When a pinned version is retired its redirect is
derived automatically from the `retired` list in that line's `versions.toml`. A test fails if a
row for one appears in the CSV.

**This file cannot express patterns.** It becomes a Cloudflare Bulk Redirect List, which has no
regular expressions and no capture groups. A redirect that needs a pattern (for example, mapping
every `<path>/old.md` to `<path>.md`) is a dynamic redirect rule, edited in the Cloudflare
dashboard rather than here.

## `docs.union.ai` redirects

For redirects from the old `docs.union.ai` site to the new `www.union.ai/docs` site, we use the original request URL. For example:

| | |
|---|---|
| Request URL | `https://docs.union.ai/building-workflows/launch-plans/triggers` |
| Target URL | `https://www.union.ai/docs/v2/union/user-guide/triggers` |
| Redirect Entry | `docs.union.ai/building-workflows/launch-plans/triggers,https://www.union.ai/docs/v2/union/user-guide/triggers,301,TRUE,TRUE,TRUE,TRUE` |

## `docs.flyte.org` redirects

For redirects from the old `docs.flyte.org` to the new `www.union.ai/docs`, we replace the `docs.flyte.org` in the request URL with the special prefix `www.union.ai/_r_/flyte`, after Cloudflare's normalization rules collapse the version to `latest` and strip `.html`. For example:

| | |
|---|---|
| Request URL | `https://docs.flyte.org/en/latest/user_guide/development_lifecycle/caching.html` |
| Converted request URL | `www.union.ai/_r_/flyte/en/latest/user_guide/development_lifecycle/caching` |
| Target URL | `https://www.union.ai/docs/v2/flyte/user-guide/tasks/task-configuration/caching/` |
| Redirect Entry | `www.union.ai/_r_/flyte/en/latest/user_guide/development_lifecycle/caching,https://www.union.ai/docs/v2/flyte/user-guide/tasks/task-configuration/caching/,301,FALSE,TRUE,TRUE,FALSE` |

The special prefix is used so that we can include both `docs.union.ai` and `docs.flyte.org` redirects in the same file and apply them on the same domain (`www.union.ai`).
