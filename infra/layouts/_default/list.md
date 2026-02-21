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

{{- $sortedPages := .Pages.ByWeight }}
{{- range $sortedPages }}
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
**Source**: https://github.com/unionai/unionai-docs/blob/main/content/{{ .File.Path }}
**HTML**: https://www.union.ai{{ .Permalink }}
{{ end }}