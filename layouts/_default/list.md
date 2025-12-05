{{ define "main" }}
{{- /*
Template for generating markdown versions of section/list pages.
This renders section content and lists child pages in markdown format.
*/ -}}
{{- if .Params.description }}

{{ .Params.description }}
{{- end }}

{{ .RawContent }}

{{- if .Pages }}

## Subpages

{{- range .Pages.ByWeight }}
{{- if (partial "page-allowed.html" .).allowed }}
{{- $section := "" }}
{{- if eq .Kind "section" }}
{{- /* For section pages (directories), get the directory name from File.Dir */}}
{{- $section = strings.TrimSuffix "/" .File.Dir }}
{{- $section = path.Base $section }}
{{- else }}
{{- /* For regular pages (files), use the file's base name */}}
{{- $section = .File.BaseFileName }}
{{- end }}
- [{{ .Title }}]({{ $section }}/) {{- if .Params.description }} - {{ .Params.description }}{{ end }}
{{- end }}
{{- end }}
{{- end }}

---
**Source**: {{ .File.Path }}
**URL**: {{ .Permalink }}
{{- if .Date }}
**Date**: {{ .Date.Format "2006-01-02" }}
{{- end }}
{{ end }}