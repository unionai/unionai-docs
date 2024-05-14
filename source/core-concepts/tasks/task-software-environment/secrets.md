# Secrets

The `secret_requests` parameters is used to specify the keys used to retrieve secrets at task runtime.
Here is an example:

```{code-block} python
from flytekit import task, workflow, Secret

SECRET_KEY = "my_secret_key"
SECRET_GROUP = "my_secret_group"

@task(secret_requests=[Secret(group=SECRET_GROUP, key=SECRET_KEY)])
def secret_task() -> str:
    secret_val = flytekit.current_context().secrets.get(SECRET_GROUP, SECRET_KEY)
    // do something with secret_val
```
