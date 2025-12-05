{{- /*
Template for generating markdown versions of 404 pages.
This renders a simple 404 not found page for markdown output.
*/ -}}
{{- $title := .Title -}}

# {{ $title }}

The page you are looking for could not be found.

{{- if .RawContent }}

{{ .RawContent }}
{{- end }}

---
**Source**: {{ .File.Path }}
**URL**: {{ .Permalink }}
{{- if .Date }}
**Date**: {{ .Date.Format "2006-01-02" }}
{{- end }}