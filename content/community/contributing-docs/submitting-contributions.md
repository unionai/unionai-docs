---
title: Submit a contribution
description: Fork, branch, sign off, and open a docs pull request against the right version branch.
icon: git
weight: 3
variants: +flyte +union
---

# Submit a contribution

This page walks through submitting a docs change as a pull request, from forking the repository to getting your change merged.
Both Flyte community members and Union customers are welcome to contribute.

Before you start, [set up a local docs dev environment](./quick-start) so you can preview your changes.

## Target the right branch

The docs repository keeps each version of the site on its own long-lived branch:

* **For Flyte or Union 2.x**, branch off `main` and open your pull request against `main`.
* **For Flyte or Union 1.x**, branch off `v1` and open your pull request against `v1`.

Most contributions target `main` (v2). See [Versions](./versions) for how versions map to branches.

## Fork and clone

If you have write access to the repository, you can branch directly. Otherwise, fork it first:

1. Fork [`unionai/unionai-docs`](https://github.com/unionai/unionai-docs) to your own GitHub account.
2. Clone your fork and initialize the submodules as described in [Set up a local docs dev environment](./quick-start):

   ```bash
   git clone https://github.com/<your-username>/unionai-docs.git
   cd unionai-docs
   make init-infra
   make init-examples
   ```

## Create a feature branch

Create a branch off the branch you are targeting (usually `main`):

```bash
git checkout main
git pull
git checkout -b my-docs-change
```

Give the branch a short, descriptive name.

## Make and preview your changes

Edit the Markdown files under `content/` and preview them locally with the live server:

```bash
make dev
```

See [Author content](./authoring) for how to write pages, and the [writing guidelines](./writing-guidelines) for the editorial conventions the site follows.

## Commit with a sign-off

Sign off each commit with the `-s` flag. This adds a `Signed-off-by` line that records that you agree your contribution can be included in the project:

```bash
git add content/...
git commit -s -m "Describe your change"
```

If you have several commits, sign off each of them.

## Open a pull request

Push your branch and open a pull request against the correct base branch (usually `main`):

```bash
git push -u origin my-docs-change
```

Then open the pull request on GitHub. In the description, explain what you changed and why.
If your change targets v1, make sure the base branch is `v1`.

## Check the preview build

Every pull request produces a preview build of the site on Cloudflare.
Look for the preview link in the pull request checks and open it to confirm your changes render as you expect, in the affected variants.

## Review and merge

A maintainer reviews your pull request, and continuous integration runs about sixteen checks on it.

Most **block the merge** and are worth reading the log for: internal and generated links, images,
redirects, icon names, subpage cards, generated content, Jupyter notebooks, build determinism, and
the developer certificate of origin sign-off described above.

Four are **advisory and do not block**, so a red mark on them is information rather than a stop:

| Advisory check | What it means |
|---|---|
| Check Markdown Lint | style nits in the Markdown source |
| Check Spelling | unknown words, which are often product names |
| API docs vs PyPI | the generated API reference has drifted from the released SDK |
| Helm docs vs helm-charts | the generated Helm reference has drifted |

Address review feedback or failing checks by pushing more commits to the same branch.

## When your change goes live

Once a maintainer merges it:

- it appears on **`/docs/latest`** with the next production deploy, within minutes;
- it appears on **`/docs/v2`**, the version most readers see, at the **next cut**, which may be
  days later.

That difference catches people out. If you are checking whether your merged change is live, look
at `/docs/latest` first. See [Versions](./versions) for why the two differ.
