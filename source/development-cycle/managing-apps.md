# Managing apps

You need to create an application to allow external systems to run compute
on Union, e.g. a Github action that registers or runs workflows.

## Creating an API key

To create an API key, run the following with the `union` CLI with any name.

```{code-block} shell
union create app custom_name

Client ID: my-custom-name
The following API key will only be shown once. Be sure to keep it safe!
Configure your headless CLI by setting the following environment variable:

export UNIONAI_SERVERLESS_API_KEY="<SECRET>"
```

Store the `<SECRET>` into a secure location. For `git` development, make sure to not check
in the `<SECRET>` into your repository. For GitHub actions, you can use
[Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
to store the secret.

For this example, copy the following workflow into a file called `hello.py`:

```{code-block} python
from flytekit import task, workflow

@task
def welcome(name: str) -> str:
    return f"Welcome to Union! {name}"

@workflow
def main(name: str) -> str:
    return welcome(name=name)
```

You can run this workflow from any machine by setting the `UNIONAI_SERVERLESS_API_KEY`
environment variable:

```{code-block} shell
export UNIONAI_SERVERLESS_API_KEY="<SECRET>"
union run --remote hello.py main --name "Union"
```

## Listing and deleting applications

You can list all your application by running:

```{code-block} shell
union get app
```

```{code-block} shell
┏━━━━━━━━━━━━━━━━┓
┃ client_id      ┃
┡━━━━━━━━━━━━━━━━┩
│ my-custom-name │
└────────────────┘
```

The `client_id` contains your custom application name and a prefix that contains your
user name.

Finally, you can delete your application by running:

```{code-block} shell
union delete app my-custom-name
```
