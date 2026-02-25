---
title: Deploy an agent as a service
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
mermaid: true
---

# Deploy an agent as a service

Union makes it straightforward to deploy internal apps (chatbots, dashboards, API endpoints) behind a URL, with no separate infrastructure. This is how you turn an agent into a hosted service that your team (or other agents) can call.

Here's a FastAPI example (`app.py`):

```python
import flyte
from fastapi import FastAPI
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI(title="My App")

@app.get("/")
async def root():
    return {"message": "Hello from Union!"}

app_env = FastAPIAppEnvironment(
    name="my-app",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages("fastapi", "uvicorn"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

if __name__ == "__main__":
    flyte.init_from_config()
    deployment = flyte.serve(app_env)
    print(f"Live at: {deployment.url}")
```

```bash
python app.py
```

Union assigns a URL, handles TLS, and auto-scales. You can also serve vLLM and SGLang models this way, deploying open-weight LLMs on GPUs behind an OpenAI-compatible API endpoint with a few lines of config.

**Webhook pattern:** Need event-driven agent triggers? Deploy a FastAPI app that receives webhooks and calls `flyte.run()` to kick off agentic workflows programmatically.

> [!TIP]
> See [Configure Apps](https://www.union.ai/docs/v2/byoc/user-guide/configure-apps/), [Build Apps](https://www.union.ai/docs/v2/byoc/user-guide/build-apps/), and [FastAPI Apps](https://www.union.ai/docs/v2/byoc/user-guide/build-apps/fastapi-app/) for more details.
> For a hands-on example, see [solutions-engineering/hands_on/04_app](https://github.com/unionai/solutions-engineering/tree/main/hands_on/04_app).
