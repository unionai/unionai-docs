---
title: Redirects
weight: 7
variants: +flyte +union
---

# Redirects

We use Cloudflare's Bulk Redirect to map URLs that moved to their new location,
so the user does not get a 404 using the old link.

The direct files are in CSV format, with the following structure:

`<source_url>,<target_url>,<status>,<include_subdomains>,<subpath_matching>,<preserve_query_string>,<preserve_path_suffix>`

| Column | Meaning |
|---|---|
| `source_url` | the incoming URL, **without** `https://` |
| `target_url` | the full URL to send the user to, **including** `https://` |
| `status` | `301` for a permanent move, which is what new rows normally use |
| `include_subdomains` | `TRUE` / `FALSE` |
| `subpath_matching` | `TRUE` matches everything beneath the source path |
| `preserve_query_string` | `TRUE` keeps `?a=b` on the target |
| `preserve_path_suffix` | `TRUE` appends the matched subpath to the target. Cloudflare rejects this unless `subpath_matching` is also `TRUE` |

Redirects are recorded in the `unionai-docs-infra/redirects.csv` file.

**Deployment is automatic.** Merging your change is enough: the `deploy-redirects.yml` workflow
pushes the whole list to Cloudflare on any push to `main` or `v1` that touches the infra pointer
or `versions.toml`. Nobody applies it by hand.

Note that **one Cloudflare list serves both lines**, so a v1 deploy republishes the v2 rows too
and vice versa. That is why the workflow is serialized and why the list is always read from both
branches.

Two rules save review time:

- **Point at the page that actually serves**, not at a URL you know will redirect again.
- **Mind the trailing slash.** An exact-match row misses the other form and produces a soft 404;
  either set `subpath_matching` to `TRUE` or add both `/x` and `/x/`.

**Do not add rows for retired version pins.** Their redirects are derived automatically from the
`retired` list in each line's `versions.toml`, and a test fails if a row for one appears here.

**This file cannot express patterns.** It becomes a Cloudflare Bulk Redirect List, which has no
regular expressions and no capture groups. Pattern redirects are dynamic redirect rules, edited
in the Cloudflare dashboard rather than here.

If you need to add a new redirect, please create a pull request with the change to `redirect.csv` and a note indicating that you would like to have it applied to production.

## `docs.union.ai` redirects

For redirects from the old `docs.union.ai` site to the new `www.union.ai/docs` site, we use the original request URL. For example:

|
|-|-|
| Request URL | `https://docs.union.ai/administration` |
| Target URL | `{{< docs_home union v1 >}}/user-guide/administration` |
| Redirect Entry | `docs.union.ai/administration,{{< docs_home union v1 >}}/user-guide/administration,302,TRUE,FALSE,TRUE,TRUE` |

## `docs.flyte.org` redirects

For directs from the old `docs.flyte.org` to the new `www.union.ai/docs`, we replace the `docs.flyte.org` in the request URL with the special prefix `www.union.ai/_r_/flyte`. For example:

|
|-|-|
| Request URL | `https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.dynamic.html` |
| Converted request URL | `www.union.ai/_r_/flyte/projects/flytekit/en/latest/generated/flytekit.dynamic.html` |
| Target URL | `{{< docs_home flyte v1 >}}/api-reference/flytekit-sdk/flytekit.core.dynamic_workflow_task/` |
| Redirect Entry | `www.union.ai/_r_/flyte/projects/flytekit/en/latest/generated/flytekit.dynamic.html,{{< docs_home flyte v1 >}}/api-reference/flytekit-sdk/flytekit.core.dynamic_workflow_task/,302,TRUE,FALSE,TRUE,TRUE` |

The special prefix is used so that we can include both `docs.union.ai` and `docs.flyte.org` redirects in the same file and apply them on the same domain (`www.union.ai`).
