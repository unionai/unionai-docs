---
title: Versions
description: How the docs version lines work, and how to cut and publish an archived version.
icon: clock-history
weight: 6
variants: +flyte +union
---

# Versions

In addition to the product variants, the docs site also supports multiple versions of the documentation.
The version selector is located at the top of the page, next to the variant selector.
Versions and variants are independent of each other, with the version being "above" the variant in the URL hierarchy.

The URL for version `v2` of the current page (the one you are one right now) in the Flyte variant is:

`{{< docs_home flyte v2 >}}/community/contributing-docs/versions`

while the URL for version `v1` of the same page is:

`{{< docs_home flyte v1 >}}/community/contributing-docs/versions`

## What a version contains (and what it does not)

A docs version is a snapshot of **content** — the pages, examples and generated API
reference as they stood against a given SDK release. The site's **look and
navigation** (the theme, built from the shared `unionai-docs-infra` submodule) is
*not* part of the snapshot: every published version, however old, is always served
with the **current** site UI. This is deliberate — the content you are reading has a
version; the reading experience should always be the best available.

Two practical consequences for contributors:

- **Theme or build-system changes never require a new docs version.** They reach
  every published version automatically when the infra submodule pointer is bumped
  on the docs branch.
- **Content changes reach `latest` immediately** on merge, and reach the stable
  version at the next cut.

## Lines are branches; versions are cuts

Each major line lives on its own long-lived branch in `unionai/unionai-docs`:

- `main` carries the current line, **v2**.
- `v1` carries the previous line. It is **active, not frozen**: new flytekit 1.x releases still
  produce new v1 versions.

Within a line, a **version** is a *cut*: an immutable snapshot of the content against an SDK
release, tagged `vN.x.y.z`. `N.x.y` is the SDK release the docs were built against, and `z` is a
docs patch counter for when a secondary component releases but the SDK triple has not moved.

### Which URL serves what

| URL | Serves | Indexed |
|---|---|---|
| `/docs/latest` | the tip of `main`, rebuilt on every merge | no |
| `/docs/v2` | the newest v2 cut, the canonical surface | **yes** |
| `/docs/v2.x.y.z` | an older, superseded cut | no |
| `/docs/v1` | the newest v1 cut | yes |
| `/docs/stable` | redirects to `/docs/v2` | n/a |

The newest cut is served **once**, at `/docs/<line>`. It only gets its own numbered URL when a
newer cut supersedes it, so there is never a duplicate copy of the same tree.

### What this means when you contribute

- **Your merged page appears on `/docs/latest` immediately**, and on `/docs/v2` at the next cut.
  If you are checking whether a change is live, look at `/docs/latest` first.
- **Theme and build changes need no cut.** They reach every version at once when the infra
  submodule pointer is bumped, as described above.

## Cutting a version

A cut is **one merge**, and it is normally automatic. When the SDK releases, CI regenerates the
API reference and opens a draft pull request that bumps `versions.toml`. Merging that PR is the
cut: the build materializes the tag and rebuilds.

You can also start one by hand from the Actions tab, by running **Regenerate API docs** (when the
SDK changed) or **Cut a docs version** (when only a secondary component moved). Both open a draft
PR rather than publishing directly.

**Nothing auto-merges.** Every path ends in a pull request that a maintainer reviews.

Maintainer detail, including how many pinned versions are retained and how a retired pin gets its
redirect, lives in `unionai-docs-infra/VERSIONING.md` and `CUTTING-A-DOCS-VERSION.md`.
