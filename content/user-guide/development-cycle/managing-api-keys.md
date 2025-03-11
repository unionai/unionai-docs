---
title: Managing API keys
weight: 14
variants: "+flyte +serverless +byoc +byok"
---

# Managing API keys

You need to create an API key to allow external systems to run compute
on Union, e.g. a GitHub action that registers or runs workflows.

## Creating an API key

To create an API key, run the following with the `union` CLI with any name.

```shell
union create api-key admin --name my-custom-name

Client ID: my-custom-name
The following API key will only be shown once. Be sure to keep it safe!
Configure your headless CLI by setting the following environment variable:

export UNION_API_KEY="<SECRET>"
```

Store the `<SECRET>` in a secure location. For `git` development, make sure to not check in the `<SECRET>` into your repository.
Within a GitHub action, you can use [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) to store the secret.

For this example, copy the following workflow into a file called `hello.py`:

```python
import union

@union.task
def welcome(name: str) -> str:
    return f"Welcome to Union! {name}"

@union.workflow
def main(name: str) -> str:
    return welcome(name=name)
```

You can run this workflow from any machine by setting the `UNION_API_KEY`
environment variable:

```shell
export UNION_API_KEY="<SECRET>"
union run --remote hello.py main --name "Union"
```

## Listing and deleting applications

You can list all your application by running:

```shell
union get api-key admin
```

```shell
┏━━━━━━━━━━━━━━━━┓
┃ client_id      ┃
┡━━━━━━━━━━━━━━━━┩
│ my-custom-name │
└────────────────┘
```

The `client_id` contains your custom application name and a prefix that contains your
user name.

Finally, you can delete your application by running:

```shell
union delete api-key admin --name my-custom-name
```
