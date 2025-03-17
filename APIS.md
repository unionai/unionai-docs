# Importing APIs

You can import Python APIs and host them on the site. To do that you will use
the `tools/api_generator` to parse and create the appropriate markdowns.

Please refer to [`api_generator/README`](tools/api_generator/README.md) for more
details.

## API naming convention

All the buildable APIs are at the root in the form:

    Makefile.api.<api_name>

To build it, run `make -f Makefile.api.<your_api>` and observe the setup
requirements in the readme above.
