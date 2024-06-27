# Managing secrets

You can use secrets to interact with external services through API keys.

## Creating secrets

To create a secret, use the `unionai create secret` command:

```{code-block} shell
unionai create secret my_secret
```

You'll be prompted to enter a secret value in the terminal:

```
Enter secret value: ...
```

## Listing secrets

You can list existing secrets with the `unionai get secret` command:

```{code-block} shell
unionai get secret
```

## Using secrets in workflow code

See below for an example of using a secret in your workflow code. To run the following example, copy it to a new file and save it as `using_secrets.py`:

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

Use `unionai run` to run the `using_secrets.py` script:

```{code-block} shell
unionai run --remote using_secrets.py main
```

## Updating secrets

To update a secret, run the `unionai update secret` command. You will be prompted to enter a new value:

```{code-block} shell
unionai update secret my_secret
```

## Deleting secrets

To delete a secret, use the `unionai delete secret` command:

```{code-block} shell
unionai delete secret my_secret
```

