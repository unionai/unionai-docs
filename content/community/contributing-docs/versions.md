---
title: Versions
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Versions

> [!NOTE]
> The versions feature is **coming soon**!

In addition to the product variants, the docs site also supports multiple versions of the documentation.
The version selector is located at the top of the page, next to the variant selector.
Versions and variants are independent of each other, with the version being "above" the variant in the URL hierarchy.

For backward compatibility, the latest version of the content has no URL prefix, while all other versions do have a prefix.
For example, the URL for the latest version of the current page (the one you are one right now) in the Flyte variant is:

`https://www.union.ai/docs/flyte/community/contributing-docs/platform-overview`

while the URL for the `v1.0` version of the same page is:

`https://www.union.ai/docs/v1.0/flyte/community/contributing-docs/platform-overview`

### Versions are branches

The versioning system is based on long-lived Git branches in the `unionai/docs` GitHub repository:

- The `main` branch contains the latest version of the documentation. Currently, `v2.0`.
- Other versions of the docs are contained in branches named `vX.Y`, where `X` and `Y` are the major and minor version numbers, respectively. Currently, there is one other version, `v1.0`.

## How to create an archive version

An "archive version" is a static snapshot of the site at a given point in time.

It is meant to freeze a specific version of the site for historical purposes,
such as preserving the content and structure of the site at a specific point in time.

### How to create an archive version

1. Create a new branch from `main` named `v<major>.<minor>`, e.g. `v1.15`.
2. Add the version to the `VERSION` field in the `makefile.inc` file, e.g. `VERSION := v1.15`.
3. Add the version to the `versions` field in the `hugo.ver.toml` file, e.g. `versions = [ "v1.15" ]`.

> [!NOTE]
> **Important:** You must update the `versions` field in **ALL** published and archived versions of the site.

### Publishing an archive version

> [!NOTE]
> This step can only be done by a Union employee.

1. Update the `docs_archive_versions` in the `docs_archive_locals.tf` Terraform file
2. Create a PR for the changes
3. Once the PR is merged, run the production pipeline to activate the new version