---
title: Versions
weight: 3
variants: +flyte +union
---

# Versions

In addition to the product variants, the docs site also supports multiple versions of the documentation.
The version selector is located at the top of the page, next to the variant selector.
Versions and variants are independent of each other, with the version being "above" the variant in the URL hierarchy.

The URL for version `v1` of the current page (the one you are one right now) in the Flyte variant is:

`{{< docs_home flyte v1 >}}/community/contributing-docs/versions`

while the URL for version `v2` of the same page is:

`{{< docs_home flyte v2 >}}/community/contributing-docs/versions`

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
- **Content changes reach the stable version at the next cut.**

### Lines are branches; versions are cuts

Each major line lives on its own long-lived branch in `unionai/unionai-docs`:

- `main` carries the current line, **v2**, built against the `flyte` 2.x SDK.
- `v1` carries **this** line, built against `flytekit` 1.x. It is **active, not frozen**: new
  flytekit 1.x releases still produce new v1 versions.

Within a line, a **version** is a *cut*: an immutable snapshot of the content against an SDK
release, tagged `vN.x.y.z`. `N.x.y` is the SDK release the docs were built against, and `z` is a
docs patch counter for when a secondary component releases but the SDK triple has not moved.

### Which URL serves what

v1 is a **secondary** line, which changes what you see here:

| URL | Serves | Indexed |
|---|---|---|
| `/docs/v1` | the newest v1 cut, this line's canonical surface | yes |
| `/docs/v1.x.y.z` | an older, superseded v1 cut | no |
| `/docs/latest` | **the v2 line's tip, not v1's.** There is only one `/docs/latest`, and the primary line owns it | no |

So there is no bleeding-edge URL for v1. **A merged v1 page is not visible anywhere until the
next v1 cut**, which is the main practical difference from contributing on `main`. If you need
to see a change before then, check the pull request's preview build.

## Cutting a v1 version

A cut is **one merge**. Running **Cut a docs version** or **Regenerate API docs** from the
Actions tab, with the branch set to `v1`, opens a draft pull request that bumps `versions.toml`.
Merging that PR is the cut: the build materializes the tag and rebuilds.

> [!NOTE]
> **v1 cuts are started by hand.** GitHub fires scheduled and repository-dispatch events only
> from the default branch, so the automatic release signals run for the v2 line. A v1 bump uses
> a manual workflow dispatch against the `v1` branch.

**Nothing auto-merges.** Every path ends in a pull request a maintainer reviews.

Maintainer detail, including how many pinned versions are retained and how a retired pin gets its
redirect, lives in `unionai-docs-infra/VERSIONING.md` and `CUTTING-A-DOCS-VERSION.md`.
