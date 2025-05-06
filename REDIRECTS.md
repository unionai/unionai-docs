# Redirecting Content

We use Cloudflare's Bulk Redirect to map URLs that moved to their new location,
so the user does not get a 404 using the old link.

The direct files are in CSV format, with the following structure:

    <incoming_redirect>,<target_url>,302,TRUE,FALSE,TRUE,TRUE

- `<incoming_redirect>`: the URL without `http://` or `https://`
- `<target_url>`: the URL to send the user to   

## `docs.union.ai` redirects

We control redirects of known links via the `redirects-ai-union-docs.csv` file.

docs.union.ai/administration,https://union.ai/docs/byoc/user-guide/administration,302,TRUE,FALSE,TRUE,TRUE

| | |
|-|-|
| Real URL | `https://docs.union.ai/administration` |
| Target URL | `https://union.ai/docs/byoc/user-guide/administration` | 
| Redirect Entry | `docs.union.ai/administration,https://union.ai/docs/byoc/user-guide/administration,302,TRUE,FALSE,TRUE,TRUE` |

## `docs.flyte.org` redirects

We control redirects of known links via the `redirects-org-flyte-docs.csv` file.

For the Flyte site, we have a special prefix to differentiate the incoming content: `www.union.ai/_r_/flyte`.
This allows us to isolate Flyte's redirects from Union's. For example, we can tell 
apart `docs.union.ai/administration` from `docs.flyte.org/administration`.

The process is the same as for `docs.union.ai`, only observing that the beginning of the file is _not_ `docs.flyte.org`.

Example:

| | |
|-|-|
| Real URL | `https://docs.flyte.org/projects/flytekit/en/latest/generated/flytekit.dynamic.html` |
| Target URL | `https://www.union.ai/docs/flyte/api-reference/flytekit-sdk/packages/flytekit.core.dynamic_workflow_task/` |
| Converted URL | `www.union.ai/_r_/flyte/projects/flytekit/en/latest/generated/flytekit.dynamic.html` | 
| Redirect Entry | `www.union.ai/_r_/flyte/projects/flytekit/en/latest/generated/flytekit.dynamic.html,https://www.union.ai/docs/flyte/api-reference/flytekit-sdk/packages/flytekit.core.dynamic_workflow_task/,302,TRUE,FALSE,TRUE,TRUE` |