---
title: Versions
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Versions

In addition to the product variants, the docs site also supports multiple versions of the documentation.
The version selector is located at the top of the page, next to the variant selector.
Versions and variants are independent of each other, with the version being "above" the variant in the URL hierarchy.

The URL for version `v1` of the current page (the one you are one right now) in the Flyte variant is:

`{{< docs_home flyte v1 >}}/community/contributing-docs/versions`

while the URL for version `v2` of the same page is:

`{{< docs_home flyte v2 >}}/community/contributing-docs/versions`

### Versions are branches

The versioning system is based on long-lived Git branches in the `unionai/unionai-docs` GitHub repository:

- The `main` branch contains the latest version of the documentation. Currently, `v2`.
- Other versions of the docs are contained in branches named `vX`, where `X` is the major version number. Currently, there is one other version, `v1`.

## How to create an archive version

An "archive version" is a static snapshot of the site at a given point in time.

It is meant to freeze a specific version of the site for historical purposes,
such as preserving the content and structure of the site at a specific point in time.

### How to create an archive version

1. Create a new branch from `main` named `vX`, e.g. `v3`.
2. Add the version to the `VERSION` field in the `makefile.inc` file, e.g. `VERSION := v3`.
3. Add the version to the `versions` field in the `hugo.ver.toml` file, e.g. `versions = [ "v1", "v2", "v3" ]`.

> [!NOTE]
> **Important:** You must update the `versions` field in **ALL** published and archived versions of the site.

### Publishing an archive version

> [!NOTE]
> This step can only be done by a Union employee.

1. Update the `docs_archive_versions` in the `docs_archive_locals.tf` Terraform file
2. Create a PR for the changes
3. Once the PR is merged, run the production pipeline to activate the new version