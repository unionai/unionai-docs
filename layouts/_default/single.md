{{ define "main" }}
{{- /*
Template for generating markdown versions of individual pages.
This renders the content with shortcodes processed for markdown output.
*/ -}}
{{- $title := .Title -}}

# {{ $title }}

{{- if .Params.description }}

{{ .Params.description }}
{{- end }}

{{ .RawContent }}

---
**Source**: {{ .File.Path }}
**URL**: {{ .Permalink }}
{{- if .Date }}
**Date**: {{ .Date.Format "2006-01-02" }}
{{- end }}
{{- if .Params.weight }}
**Weight**: {{ .Params.weight }}
{{- end }}
{{ end }}