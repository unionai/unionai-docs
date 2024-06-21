# Managing secrets

We frequently use secrets for interacting with external services through API keys.
In this example, we learn how to manage secrets on Union.

Create a secret with the CLI:

```{code-block} shell
unionai create secret my_secret
```

You'll be prompted to enter a secret value in the terminal:

```
Enter secret value: ...
```

You can list existing secrets by running:

```{code-block} shell
unionai get secret
```

You can now use this secret in your workflow code. To run the following example, copy it to a new file and save it as `using_secrets.py`:

```{code-block} python
from flytekit import Secret, current_context, task, workflow

@task(secret_requests=[Secret(key="my_secret")])
def fn() -> str:
    secret_value = current_context().secrets.get(key="my_secret")
    # do something with the secret. For example, communication with an external API.
    # For this example, we'll just return it.
    return f"Hello: {secret_value}!"

@workflow
def main() -> str:
    return fn()
```

You can run the `using_secrets.py` script to see how it works:

```{code-block} shell
unionai run --remote using_secrets.py main
```

To update a secret, run the following and you will be prompted to enter a new value:

```{code-block} shell
unionai update secret my_secret
```

Lastly, to delete a secret run:

```{code-block} shell
unionai delete secret my_secret
```

