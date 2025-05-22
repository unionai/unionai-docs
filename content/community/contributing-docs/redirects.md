---
title: Redirects
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Redirects

We use Cloudflare's Bulk Redirect to map URLs that moved to their new location,
so the user does not get a 404 using the old link.

The direct files are in CSV format, with the following structure:

`<incoming_redirect>,<target_url>,302,TRUE,FALSE,TRUE,TRUE`

- `<incoming_redirect>`: the URL without `https://`
- `<target_url>`: the full URL (including `https://`) to send the user to

Redirects are recorded in `redirects.csv` file in the root of the repository.

To take effect, this file must be applied to the production environment on CloudFlare by a Union employee.

If you need to add a new redirect, please create a pull request with the change to `redirect.csv` and a note indicating that you would like to have it applied to production.

## `docs.union.ai` redirects

For redirects from the old `docs.union.ai` site to the new `www.union.ai/docs` site, we use the original request URL. For example:

|-|-|
| Request URL | `https://docs.union.ai/administration` |
| Target URL | `https://union.ai/docs/byoc/user-guide/administration` |
| Redirect Entry | `docs.union.ai/administration,https://union.ai/docs/byoc/user-guide/administration,302,TRUE,FALSE,TRUE,TRUE` |

## `docs.flyte.org` redirects

For directs from the old `docs.flyte.org` to the new `www.union.ai/docs`, we ureplace the `docs.flyte.org` in the request URL with the special prefix `www.union.ai/_r_/flyte`. For example:

|-|-|
| Request URL | `https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.dynamic.html` |
| Converted request URL | `www.union.ai/_r_/flyte/projects/flytekit/en/latest/generated/flytekit.dynamic.html` |
| Target URL | `https://www.union.ai/docs/flyte/api-reference/flytekit-sdk/packages/flytekit.core.dynamic_workflow_task/` |
| Redirect Entry | `www.union.ai/_r_/flyte/projects/flytekit/en/latest/generated/flytekit.dynamic.html,https://www.union.ai/docs/flyte/api-reference/flytekit-sdk/packages/flytekit.core.dynamic_workflow_task/,302,TRUE,FALSE,TRUE,TRUE` |

The special prefix is used so that we can include both `docs.union.ai` and `docs.flyte.org` redirects in the same file and apply them on the same domain (`www.union.ai`).
