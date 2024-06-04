# Union documentation

This repository contains the source for the Union documentation site.

The site is built using a combination of the [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
templating system and the [Sphinx](https://www.sphinx-doc.org) static site generator.

The site is hosted on Cloudflare Pages in the [docs-union-ai](https://dash.cloudflare.com/fcdf789dd2ac34464befdf8153c3b360/pages/view/docs-union-ai)
project:

## Set up your local Python environment

* Create a virtual Python environment with Python 3.11 installed
* Activate that virtual environment.
* Install the dependencies with `pip install -r requirements.txt`

## Build the site

* Run the build with `python build.py`

The resulting HTML files will be in the directory `build/html`.

## Publish the site

To publish a change to the site, create a pull request here in `unionai/docs` against the `main` branch.
Once the pull request is merged, the changes will be published to `docs.union.ai`.

PR builds are also automatically deployed to preview URLs on the [docs-union-ai](https://dash.cloudflare.com/fcdf789dd2ac34464befdf8153c3b360/pages/view/docs-union-ai)
project in Cloudflare Pages.

## How it works

The content in `source/` is written in [Sphinx](https://www.sphinx-doc.org)[Myst Markdown](https://mystmd.org/) format
augmented with [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templating syntax.

The site is engineered to present content for multiple **variants** of the Union product.
The current variants are: **Serverless** and **BYOC**. Other variants can be easily added.

The single source tree contains the content for all variants.
But which content is to be displayed for a specific variant can be controlled
at two levels: the whole-page level and the in-page block level.

### Controlling content at the whole-page level

The configuration file `sitemap.json` defines the hierarchical structure of the site
and specifies which pages are to be included in each variant using the `variants` key
in each page's entry.

For example, consider the following section of the `sitemap.json`:

```
{"name": "getting-started", "variants": ["byoc", "serverless"],
    "children": [
        {"name": "machine-learning-example", "variants": ["serverless"]},
        {"name": "adding-custom-dependencies", "variants": ["serverless"]},
        {"name": "managing-secrets", "variants": ["serverless"]},
        {"name": "managing-apps", "variants": ["serverless"]},
        {"name": "access-aws-s3", "variants": ["serverless"]},
        {"name": "installing-development-tools", "variants": ["byoc"]},
        {"name": "creating-the-project", "variants": ["byoc"]},
        {"name": "looking-at-the-dependencies", "variants": ["byoc"]},
        {"name": "looking-at-the-workflow-code", "variants": ["byoc"]},
        {"name": "running-in-a-local-python-environment", "variants": ["byoc"]},
        {"name": "running-in-a-local-cluster", "variants": ["byoc"]},
        {"name": "setting-up-the-project-on-union", "variants": ["byoc"]},
        {"name": "deploying-the-project-on-union", "variants": ["byoc"]},
        {"name": "more-resources", "variants": ["byoc"]}
    ]},
```

Here we see that the `getting-started` page is included in both the `byoc` and `serverless` variants.
But among its subpages the `machine-learning-example` page is only included in the `serverless` variant.
and the `installing-development-tools` page is only included in the `byoc` variant.
Other pages are similarly included in only one or the other variant.

Note that it a subpage cannot be included in variant in which its parent page is not included.
In other words, the scope of sub-pages is always either equicvalent to or a subset of the scope
of their parent page. A processing error will be raised by `build.py` if this rule is violated.

Note also that the `sitemap.json` file is used to automatically generate `toctree` entries
in the intermediate Sphinx markdown, so you must not add your own toctrees.
The `sitemap.json` defines the hierarchy of the pages.

### Controlling content at the block level

The content of a part of a page can be conditionally included
using Jinja templating syntax like this:

```
Content for all variants of the page as per its entry in the `sitemap.json`
{@@ if serverless @@}
Content only for serverless
{@@ elif  byoc @@}
Content only for BYOC
{@@ endif @@}
Content for all variants of the page as per its entry in the `sitemap.json`
```

### Variables

Variables can be used in the content of a page using Jinja templating syntax like this:

```
{@= my_variable =@}
```

The variable values are defined in the `build.py` file in the `SUBS` constant.

### Comments

Comments can be included using the Jinja templating syntax like this:

```
{@# This is a comment #@}
```

### Jinja2 syntax

Note that this system uses a cusomized version of the syntax for Jinja templating

* `{@@ ... @@}` for block statements
* `{@= ... =@}` for expressions.
* `{@# ... #@}` for comments.

This is done avoid conflict with documentation content that might include the standard Jinja syntax.

### The processing pipeline

The `build.py` script processes the content in the `source/` directory and applies the
Jinja2 templating logic as well as adding toctree directives to procduce proper Sphinx
markdopwn in the `sphinx_source` directory.

In that directory one entire self-contined sphinc project is created for each variant
(BYOC, Serverless, etc.).

These pseparate trees rojects are then built by Sphinx to produce the final HTML output in the `build/html` directory.

There the output for each variant is placed in a separate subdirectory.

A top level index page is then copied in at the very top that redirect to
the default variant's index page (currently Serverless).

## Redirects

When re-arranging the content of the site, it may be necessary to create redirects.
These are defined in the `cloudflare-redirects.json` file which is checked in at the
root of this repo.

However, that file's presence in this repo is not sufficient to iomplment the redirects

This file must be manually applied in Cloudflare under the **Bulk redirects** section
in order to take effect.

The file is present here in this repo simply for purposes of version control and storage.

## Contributing

Just like any other repository, you can create a pull request with your changes.

If you make changes that would move the URL-location of an exisitng page, you must
create the appropriate redirect.
