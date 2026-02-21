{{ define "main" }}
{{- /*
Template for generating markdown versions of individual pages.
This renders the content with shortcodes processed for markdown output.
*/ -}}
{{- if .Params.description }}

{{ .Params.description }}
{{- end }}

{{ .RawContent }}

---
**Source**: https://github.com/unionai/unionai-docs/blob/main/content/{{ .File.Path }}
**HTML**: https://www.union.ai{{ .Permalink }}
{{ end }}