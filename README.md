# Union documentation

This repository contains the source for the Union documentation site [docs.union.ai](https://docs.union.ai).

The site is built using a combination of the [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
templating system and the [Sphinx](https://www.sphinx-doc.org) static site generator.

The site is hosted on Cloudflare Pages in the [docs-union-ai](https://dash.cloudflare.com/fcdf789dd2ac34464befdf8153c3b360/pages/view/docs-union-ai)
project.


## Set up your local Python environment

* Ensure you have Python 3.12 or later installed.
* Clone this repository.

```bash
git clone https://github.com/unionai/docs.git
```
* We use `uv`. See installation instructions for your platform [here](https://docs.astral.sh/uv/getting-started/installation/).


### Activate the virtual environment

```bash
cd docs
uv venv  # create a virtual environment
```
Or, if you have multiple Python versions installed, you can specify the Python version to use:

```bash
uv venv .venv --python 3.12  # create a virtual environment with the specific Python 3.12 version
```

### Install the dependencies

```bash
uv sync
```

**Note:** It's a good idea to regularly re-install dependencies, as documentation changes sometimes introduce new or updated dependencies.


## Build the site

* Run the build with `uv run make build-local`.

The resulting HTML files will be in the directory `build/html`.

```bash
open build/html/serverless/index.html  # serverless variant
open build/html/byoc/index.html  # byoc variant
```

The build process will generate two sets of Markdown files in the `sphinx_source` directory, one each for the Serverless and BYOC product versions. The final HTML output lives in the `build` directory.

To delete both the `sphinx_source` and `build` directories, run `uv run make clean`.


## Publish the site

To publish a change to the site, create a pull request here in `unionai/docs` against the `main` branch.
Once the pull request is merged, the changes will be published to `docs.union.ai`.

PR builds are also automatically deployed to preview URLs on the [docs-union-ai](https://dash.cloudflare.com/fcdf789dd2ac34464befdf8153c3b360/pages/view/docs-union-ai)
project in Cloudflare Pages.


## Build the site with Algolia DocSearch

To build the site with Algolia DocSearch, you need to provide the API keys associated with the
BYOC and Serverless DocSearch indexes. You can do this by creating a `secrets.txt`
file (which will be ignored by git), and putting the following content into it:

```
DOCSEARCH_API_KEY_BYOC=<DOCSEARCH_API_KEY_BYOC>
DOCSEARCH_API_KEY_SERVERLESS=<DOCSEARCH_API_KEY_SERVERLESS>
```

> [!NOTE]
> You can obtain the credentials from LastPass by contacting niels@union.ai.

Export the environment variables and run the docs build process:

```bash
export $(cat secrets.txt | xargs)
make build-local
```


> [!NOTE]
> When you view the local docs, the search bar will surface results that will
> redirect to the corresponding `docs.union.ai` page. This is because Algolia
> DocSearch does not index local pages.


## Variants

The Union docs website is built to differient content depending on which
"variant" of the product is selected in the variant switcher a the top of the page.

Currently we have two variants: "Serverless" and "BYOC".

The content for different variants is produced from a common single tree of source pages
with templating logic in individual pages and configuration in the `sitemap.json` controling which
content appears in which variant.

If you are on page and switch the variant to one where the current page also exists, you will go to
that specific page. If the current page does not exist, you will go to the root page of the site.


## How it works

The content in `source/` is written in [Sphinx](https://www.sphinx-doc.org) [Myst Markdown](https://mystmd.org/) format
augmented with [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templating syntax.

The site is engineered to present content for multiple **variants** of the Union product.
The current variants are **Serverless** and **BYOC**. Other variants can be easily added.

The single source tree contains the content for all variants.
Which content is to be displayed for a specific variant can be controlled
at two levels: the page level and the block level.


### Controlling content at the page level

The configuration file `sitemap.json` defines the hierarchical structure of the site
and specifies which pages are to be included in each variant using the `variants` key
in each page's entry.

For example, consider the following section of the `sitemap.json`:

``` json
{"name": "administration", "variants": ["byoc", "serverless"], "children": [
    {"name": "resources", "variants": ["byoc", "serverless"]},
    {"name": "cost-allocation", "variants": ["byoc"]},
    {"name": "user-management", "variants": ["byoc"]},
    {"name": "applications", "variants": ["byoc"]},
    {"name": "cli-authentication-types", "variants": ["byoc"]}
]},
```

Here we see that the `adminiistration` page is included in both the `byoc` and `serverless` variants.
Its subpage `resources` is also in both, but the other subpages are only in `byoc`.

Note that a subpage cannot be included in a variant in which its parent page is not included.
In other words, the scope of a sub-page is always either equivalent to, or a subset of, the scope
of its parent page. A processing error will be raised by `build.py` if this rule is violated.

Note also that the `sitemap.json` file is used to automatically generate `toctree` directives
in the intermediate Sphinx Markdown, so you must not add your own `toctree` directives.
The `sitemap.json` is the single source that defines the hierarchy of the pages.


### Correspondence between `sitemap.json`, website, and file tree

The hierarchy and ordering of pages in the `sitemap.json` correspond hierarchy and ordering of the navigation
elements in the website, as well as the URL structure of the website.

For example, the section shown above defines the following pages:

In Serverless:
* `https://docs.union.ai/serverless/user-guide/administration/`
* `https://docs.union.ai/serverless/user-guide/administration/resources`

In BYOC:
* `https://docs.union.ai/byoc/user-guide/administration/`
* `https://docs.union.ai/byoc/user-guide/administration/resources`
* `https://docs.union.ai/byoc/user-guide/administration/cost-allocation`
* `https://docs.union.ai/byoc/user-guide/administration/user-management`
* `https://docs.union.ai/byoc/user-guide/administration/applications`
* `https://docs.union.ai/byoc/user-guide/administration/cli-authentication-types`


### Controlling content at the block level

The content of part of a page can be conditionally included using Jinja templating syntax like this:

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

Variables can be used in the content of a page using Jinja2 templating syntax like this:

```
{@= my_variable =@}
```

The variable values are defined in the `build.py` file in the `SUBS` constant.


### Comments

Comments can be included using the Jinja2 templating syntax like this:

```
{@# This is a comment #@}
```

### Jinja2 syntax

Note that this system uses a customized version of the syntax for Jinja2 templating:

* `{@@ ... @@}` for block statements
* `{@= ... =@}` for expressions.
* `{@# ... #@}` for comments.

This is done to avoid conflict with documentation content that includes the standard Jinja syntax.


### Pulling in tutorial examples content

This repo uses the [unionai-examples](https://github.com/unionai/unionai-examples) repo as a git submodule
to pull in the content for the tutorial examples.

Calling `make build-local` automatically synchronizes the submodule to the current commit in the parent `docs` repo, but if you want to update it manually, you can
run `make sync-examples`.

If you've added a new example to the `union-examples` repo, you can update the submodule to the latest remote commit by running `make update-examples`.

To pull in a specific page from the examples repo, you can specify a `from_py_file`
key in the `sitemap.json` file. For example:

``` json
"children": [
    {
        "name": "sentiment-classifier",
        "variants": ["byoc", "serverless"],
        "from_py_file": "./unionai-examples/tutorials/sentiment_classifier/sentiment_classifier.py"
    }
]
```

When you run `make build-local`, `update-examples` will pull in the latest changes from the `unionai-examples` repo, then the `build.py` module converts the contents of the Python file to a Markdown file using `jupytext` before rendering the sphinx files using the `jinja` templating system.

It will also use the YAML file in the `./unionai-examples/run_commands.yaml` repo to
generate metadata about how to run that example.


### The processing pipeline

The `build.py` script processes the contents in the `source/` directory,
and builds a separate Sphinx project for each variant in the `sphinx_source/` directory.

It uses the `sitemap.json` to determine which files are copied into which variant's Sphinx project.
and also applies the Jinja2 templating logic to each page to determine it's content based on the variant.
Additionally, it adds toctree directives to each `index.md` page based on the hierarchy defined the `sitemap.json`.

The resulting Sphinx projects in the `sphinx_source` directory are then each proecessed by `sphinx-build` to produce the final HTML output in the `build/html` directory.
Again, each variant is placed in a separate subdirectory.


## Redirects

Redirects are handled in two places:

* `_redirects` (deployed automatically on merge to `main`)
* `docs_redirects.csv` (recorded here, but requires manual uploading to Cloudflare Bulk Redirects to take effect)

The `_redirects` file is used to redirect the top-level URLs to two opt-level pages:
* `docs.union.ai/` -> `docs.union.ai/byoc/user-guide`
* `docs.union.ai/byoc` -> `docs.union.ai/byoc/user-guide`
* `docs.union.ai/serverless` -> `docs.union.ai/serverless/user-guide`

These redirects are part of the functionality and design of the website itself.
The `_redirects` file is automatically deployed to Cloudflare Pages on merge to `main`.
For details on how the `_redirects` file works, see the [Cloudflare Docs > Pages > Configuration > Redirects](https://developers.cloudflare.com/pages/configuration/redirects/).

The `docs_redirects.csv` file is used to redirect specific URLs to other specific URLs
due to pages and content moving around over the lifecycle of the website.
This is done to avoid 404s in URLs that have made their way "out into the wild".

The file `docs_redirects.csv` is recorded here in the Git repo but only takes effect when uploaded to Cloudflare Bulk Redirects.
To register the `docs_redirects.csv`, go to the Cloudflare dashboard for the `docs-union-ai` project:

* Go to "Bulk Redirects"
* Select `docs_redirects` under "Bulk Redirect Lists"
* Upload the `docs_redirects.csv` file.

For details on how the redirects file works, see the [Cloudflare Docs > Rules > Redirects > Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/).


## PR builds

In Cloudflare pages, builds are automatically created for each PR. The PR builds are available at the following URL.
Because redirects happen at the Cloudflare Bulk Redirects level, they do not affect PR builds.
Consequently, IN PR builds the topmost page of the srte is not redirected to the BYOC index page (as it is on the production site).
Instead, a dummy index page is located there with links to the BYOC and Serverless index pages.


## Ordering in VS Code explorer

The file `.order` is included in the repo to control the order of files in the VS Code explorer when using the
[SortMyFile extension](https://marketplace.visualstudio.com/items?itemName=CanklotSoftware.SortMyFiles).
This extension allows the order of the files in the explorer to reflect the order of pages in the left navigation of the Union docs
(with one limitation: folders will always appear above files, whereas this is not the case in website navigation).


## Contributing

Just like any other repository, you can create a pull request with your changes.

If you make changes that would move the URL-location of an existing page, you must
create the appropriate redirect.
