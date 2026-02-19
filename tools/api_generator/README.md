# API Generator

To use this tool, you need to have the package for which you are generating API documentation installed in your active Python virtual environment.
The tool introspects the package and generates documentation based on the doc-strings and type hints in the code.
The examples below use the `uv` tool to manage the virtual environment, but you can use the tool you prefer.

## Example usage

For example, to generate the documentation for the `flyte` package, you can use either the automated setup or manual setup:

### Option 1: Automated Setup (Recommended)

1. From the root of your local checkout of this repository, run the setup script:

   ```bash
   $ ./setup-api-generator.sh
   ```

2. Activate the virtual environment and run the generator:

   ```bash
   $ source .venv/bin/activate
   $ make -f Makefile.api.sdk
   ```

### Option 2: Manual Setup

1. Go to the root of your local checkout of this repository.

2. Create a virtual environment:

   ```bash
   $ uv venv
   ```

3. Activate the virtual environment:

   ```bash
   $ source .venv/bin/activate
   ```

4. Install the package you want to generate documentation for, e.g., `flyte`:

   ```bash
   $ uv add flyte
   ```

5. Install additional dependencies:

   ```bash
   $ uv add pyyaml
   ```

5 Run the generator for `flytekit`:

   ```bash
   $ make -f Makefile.api.flytekit
   ```

The generator will introspect the `flytekit` package and produce the documentation in the form of Markdown files in the directory `content/api-reference/flytekirt-sdk/`.

Once the Markdown is generated, you should build the site locally to using `make dev` or `make dist` to check the results.

Once you are satisfied, you can push the changes and create a PR.
On merge to `main`, the result will be published to the public site

## Makefiles

The general command to build the API documentation for a specific package is:

```bash
$ make -f Makefile.<type>.<name>
```

There is a predefined `Makefile` for each API/CLI:

* `Makefile.api.sdk` — SDK and CLI docs (config-driven via `api-packages.toml`)
* `Makefile.api.plugins` — Plugin docs (config-driven via `api-packages.toml`)

## How it works

It will build the `parser` and `generate` targets.

The **parser** target introspects the package and produces a YAML.
This YAML is used in the **generate** step to create the Markdown.

> This is done in order to persist the intermediate data and decouple it from the site generation logic.

The **generate** target produces all the Union-Flyte-docs-compatible Markdown files.

## Docstrings

The docstrings are extracted and embedded as-is in the final Markdown file.
The docstring, therefoe, must itself be written in Union-Flyte-docs-compatible Markdown.

Example:

```python
async def async_put_raw_data(
    self,
    lpath: Uploadable,
    upload_prefix: Optional[str] = None,
    file_name: Optional[str] = None,
    read_chunk_size_bytes: int = 1024,
    encoding: str = "utf-8",
    skip_raw_data_prefix: bool = False,
    **kwargs,
) -> str:
    """
    This is a more flexible version of put that accepts a file-like object or a string path.
    Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
    file system directly.
    FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
         s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0
    If lpath is a folder, then recursive will be set.
    If lpath is a streamable, then it can only be a single file.
    Writes to:
        {raw output prefix}/{upload_prefix}/{file_name}
    :param lpath: A file-like object or a string path
    :param upload_prefix: A prefix to add to the path, see above for usage, can be an "". If None then a random
        string will be generated
    :param file_name: A file name to add to the path. If None, then the file name will be the tail of the path if
        lpath is a file, or a random string if lpath is a buffer
    :param read_chunk_size_bytes: If lpath is a buffer, this is the chunk size to read from it
    :param encoding: If lpath is a io.StringIO, this is the encoding to use to encode it to binary.
    :param skip_raw_data_prefix: If True, the raw data prefix will not be prepended to the upload_prefix
    :param kwargs: Additional kwargs are passed into the fsspec put() call or the open() call
    :return: Returns the final path data was written to.
    """
```

> **Do not include HTML in the docstring. The docs build will fail.**

## Parameter Formats

The tool supports documentation in two flavors:

### `Args:` block

```markdown
Your documentation about the quick brown fox....
.... and there it goes ...
Args:
   name: documentation of name
   address: documentation of address
       if long you ident them the same level
       like this
```

### `:param:` block

```markdown
That fox keeps generating documentation.

:param name:the documentation for the name goes here
:param address: the documentation for address
:rtype: the result type
```

## Special Tags

### Notes and Warnings

You can specify notes and warnings in your documentation:

```markdown
> [!NOTE] <optional note title>
> your notes goes here. this is a
> markdown block.

> [!WARNING] <optional warning title>
> your warning goes here. this is a
> markdown block.
```
