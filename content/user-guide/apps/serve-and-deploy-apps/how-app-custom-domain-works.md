---
title: How app custom domains work
description: Set an app's subdomain with `flyte.app.Domain`.
icon: globe
weight: 2
variants: +flyte +union
---

# How app custom domains work

The snippet below sets the app's subdomain with `flyte.app.Domain(subdomain=...)`. It does not set a custom domain, which is the separate `custom_domain` field of `flyte.app.Domain`:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/create_custom_domain.py" fragment=custom-domain lang=python >}}

{{< variant flyte >}}
{{< markdown >}}
> [!NOTE]
> The Flyte backend ignores `subdomain` and `custom_domain`. It serves each app at `<name>-<project>-<domain>.<base domain>` (lower-cased, and shortened with a hash suffix if longer than 63 characters), where the base domain comes from the backend's app configuration. If no base domain is configured, the app gets no public URL.
{{< /markdown >}}
{{< /variant >}}
