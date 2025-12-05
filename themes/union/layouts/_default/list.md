{{- /*
Template for generating markdown versions of section/list pages.
This renders section content and lists child pages in markdown format.
*/ -}}
{{- $title := .Title -}}

# {{ $title }}

{{- if .Params.description }}

{{ .Params.description }}
{{- end }}

{{ .RawContent }}

{{- if .Pages }}

## Pages in this section

{{- range .Pages.ByWeight }}
{{- if (partial "page-allowed.html" .).allowed }}
- [{{ .Title }}]({{ .RelPermalink }}) {{- if .Params.description }} - {{ .Params.description }}{{ end }}
{{- end }}
{{- end }}
{{- end }}

---
**Source**: {{ .File.Path }}
**URL**: {{ .Permalink }}
{{- if .Date }}
**Date**: {{ .Date.Format "2006-01-02" }}
{{- end }}