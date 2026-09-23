---
paths:
  - "redirects.csv"
  - "unionai-docs-infra/redirects.csv"
  - "ROUTING-ARCHITECTURE.md"
  - "unionai-docs-infra/ROUTING-ARCHITECTURE.md"
  - "scripts/build_versions.sh"
  - "unionai-docs-infra/scripts/build_versions.sh"
  - "content/community/contributing-docs/redirects.md"
---

# Routing and redirects

`ROUTING-ARCHITECTURE.md` is the authority and carries its own "last verified" date. **Probe the
live URL first** (`curl -sI`), then reconcile — the Cloudflare rules are edited in the dashboard
and no repo file can know about it.

## `redirects.csv` cannot express patterns

It becomes a Cloudflare Bulk Redirect List: no regex, no capture groups. Anything needing a
pattern is a dynamic redirect rule, edited in the dashboard. The CSV shows what is
version-controlled, not what is possible.

- **Mind the trailing slash.** An exact-match row misses the other form and produces a soft 404.
  Set `subpath_matching`, or add both `/x` and `/x/`.
- **Never add a row for a retired version pin.** Its redirect is derived from the `retired` list
  in that line's `versions.toml`, and a test fails if a row appears here.

## The three fallbacks swallow more than 404s

`/docs/v1/*`, `/docs/v2/*` and `/docs/*` each redirect any unrecognised path to a user guide —
**302, not 404**. So a file added at a tree root is unreachable until it is added to that rule's
hand-maintained passthrough allowlist. `/docs/build-info.json` was lost exactly this way.

**A PR preview cannot detect this.** Previews are served from a `pages.dev` host where the
`www.union.ai` zone rules do not apply, so the file works on the preview and is invisible in
production. Verify on production after deploy.
