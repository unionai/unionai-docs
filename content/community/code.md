---
title: "{{< code >}} examples"
variants: +flyte +serverless +byoc +selfmanaged
---

# `{{</* code */>}}` Examples

## Including a section of a file: `{{docs-fragment}}`

    {{</* code file="/_static/__docs_builder__/sample.py" fragment="entrypoint" */>}}

Link to [/_static/__docs_builder__/sample.py](/_static/__docs_builder__/sample.py)

Effect:

{{< code file="/_static/__docs_builder__/sample.py" fragment="entrypoint" >}}

## Including a file with a specific line range: `from` and `to`

    {{</* code file="/_static/public/public-key.txt" from="1" to="3" */>}}

Link to [/_static/public/public-key.txt](/_static/public/public-key.txt)

Effect:

{{< code file="/_static/public/public-key.txt" from="1" to="3" >}}

## Including a whole file

Simply specify no filters, just the `file` attribute:

    {{</* code file="/_static/public/public-key.txt" */>}}

Link to [/_static/public/public-key.txt](/_static/public/public-key.txt)

Effect:

{{< code file="/_static/public/public-key.txt" >}}
