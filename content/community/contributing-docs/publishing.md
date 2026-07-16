---
title: Production builds and troubleshooting
weight: 11
variants: +flyte +union
---

# Production builds and troubleshooting

This page covers building the site the way production does and troubleshooting what you see in the local preview.
To set up your machine and run the live preview for the first time, see [Set up a local docs dev environment](./quick-start).

## Build the production site

To build every variant the way the Cloudflare production pipeline does, run:

```bash
make dist
```

This builds all variants and writes the result to the `dist/` folder.

### Test the production build

Serve the `dist/` folder locally to confirm the site behaves as it would at its official URL:

```bash
make serve [PORT=<nnnnn>]
```

If you do not pass a port, it defaults to `9000`. For example:

```bash
make serve PORT=4444
```

Then open `http://localhost:<port>` in your browser. In the example above, that is `http://localhost:4444/`.

## Troubleshooting

### Missing content

Content may be hidden by `{{</* variant */>}}` blocks. To see what is hidden, adjust the show/hide settings in `hugo.local.toml` while running the dev server.

For a production-like view, set:

```toml
show_inactive = false
highlight_active = false
```

For a full developer view that reveals all variant content, set:

```toml
show_inactive = true
highlight_active = true
```

See [Set up a local docs dev environment > Development settings](./quick-start#development-settings) for what each setting does.

### Page visibility

The dev server marks in red any page that is missing from the current variant.
For a page to appear in a variant (or be deliberately excluded), that variant must be listed in the page's `variants` frontmatter field.
Click a red page to see the path you need to add and a link with guidance.

See [Author content > Page visibility](./authoring#page-visibility) for more details on the `variants` field.
