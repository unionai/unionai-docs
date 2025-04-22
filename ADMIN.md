# Docs Builder Administration Guide

## Variants

A variant is a term we use to identify a product or major section of the site.
Such variant has a dedicated token that identifies it, and all resources are
tagged to be either included or excluded when the variant is built.

> Adding new variants is a rare event and must be reserved when new products
> or major developments.
> 
> If you are thinking adding a new variant is the way
> to go, please double check with the infra admin to confirm before doing all
> the work below and waste your time.

### Location

When deploying, the variant takes a folder in the root

    https://<your-site-domain>/<variant>/<content>

For example, if we have a variant `acme`, then when built the content goes to:

    https://<your-site-domain>/acme/<content>

### Creating a new variant

To create a new variant a few steps are required:

| File                    | Changes                                                        |
| ----------------------- | -------------------------------------------------------------- |
| `hugo.site.toml`        | Add to `params.variant_weights` and all `params.key`           |
| `hugo.toml`             | Add to `params.search`                                         |
| `Makefile`              | Add a new `make variant` to `dist` target                      |
| `<content>.md`          | Add either `+<variant>` or `-<variant>` to all content pages   |
| `config.<variant>.toml` | Create a new file and configure `baseURL` and `params.variant` |

#### Testing the new variant

As you develop the new variant, it is recommended to have a `pre-release/<variant>` semi-stable
branch to confirm everything is working and the content looks good. It will also allow others
to collaborate by creating PRs against it (`base=pre-release/<variant>` instead of `main`)
without trampling on each other and allowing for parallel reviews.

Once the variant branch is correct, you merge that branch into main.

### Building (just) the variant

You can build the production version of the variant,
which will also trigger all the safety checks as well,
by invoking the variant build:

    make variant VARIANT=<variant>

Example:

    make variant VARIANT=serverless