# API Generator

You must `uv sync` and activate your API environment.

## Building

    make -f Makefile.<yourapi>

It will build the `parser` and `generate` targets.

* **parser**: Introspects the package and produces a YAML with all the metadata
              for that version. This YAML is used in the **generate** step to
              create the site.

  > It is done this way so we can persist the metata and decouple from the site
  > generation business.

* **generate**: Produces all Hugo/Union compatible markdown files for a given
                library metadata (created by the **parser** target.)

## Documentation

All the documentation is interpreted as Markdown.

Example:

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

> **Do not include HTML entities in the file. It will fail the build.**

## Parameter Formats

The tool supports documentation in two flavors:

### `Args:` block

    Your documentation about the quick brown fox....
    .... and there it goes ...

    Args:
       name: documentation of name
       address: documentation of address
           if long you ident them the same level
           like this

### `:param:` block

    That fox keeps generating documentation.

    :param name:the documentation for the name goes here
    :param address: the documentation for address
    :rtype: the result type

## Special Tags

### Notes and Warnings

You can specify notes and warnings in your documentation:

    > [!NOTE] <optional note title>
    > your notes goes here. this is a
    > markdown block.

    > [!WARNING] <optional warning title>
    > your warning goes here. this is a
    > markdown block.

Example:

    > [!WARNING] Fox Detected
    > The fox is roaming around the farm. Watch out for
    > the lazy dog.
