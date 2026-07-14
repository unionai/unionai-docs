---
title: Browser apps
weight: 6
variants: +flyte +union
---

# Browser apps

For browser-based apps (like Streamlit, Gradio, or custom HTML/JS dashboards), users interact directly through the web interface. The app URL is accessible in a browser, and users interact with the UI directly: no API calls needed from other services.

## Accessing browser-based apps

To access a browser-based app:

1. Deploy the app using `flyte deploy` or `flyte serve`
2. Navigate to the app URL in a browser
3. Interact with the UI directly

## Common browser-based app types

### Streamlit apps

Streamlit is ideal for data dashboards and ML prototypes. See [Streamlit app](../native-app-integrations/streamlit-app) for details.

### Gradio apps

Gradio is great for ML model demos and interactive interfaces. You can deploy a Gradio app by building a custom [`AppEnvironment`](./single-script-apps) with the `gradio` package installed in your image.

### Custom HTML/JS apps

You can also serve custom HTML/JS applications using FastAPI's static file serving or any other web framework.

## Best practices

1. **Authentication**: For sensitive apps, enable authentication with `requires_auth=True`.
2. **Responsive design**: Design UIs that work on various screen sizes.
3. **Loading states**: Show loading indicators for long-running operations.
4. **Error handling**: Display user-friendly error messages.
5. **Resource management**: Configure appropriate CPU/memory resources based on expected usage.
