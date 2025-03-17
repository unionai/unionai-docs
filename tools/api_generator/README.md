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
