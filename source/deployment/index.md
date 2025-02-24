{@@ if flyte @@}

# Flyte deployment

```{admonition} Flyte
These docs are for [**Flyte**](./about-union.md#flyte).
Switch to another variant with the version selector above.
```

{@@ elif serverless @@}

# Union Serverless deployment

```{admonition} Union Serverless
These docs are for [**Union Serverless**](./about-union.md#union-serverless).
Switch to another variant with the version selector above.
```

{@@ elif byoc @@}

# Union BYOC deployment

```{admonition} Union BYOC
These docs are for [**Union BYOC**](./about-union.md#union-byoc).
Switch to another variant with the version selector above.
```

{@@ elif byok @@}

# Union BYOK deployment

```{admonition} Union BYOK
These docs are for [**Union BYOK**](./about-union.md#union-byok).
Switch to another variant with the version selector above.
```

{@@ endif @@}

Union uses a hybrid model cloud service: Union maintains the control plane of the application on its own cloud infrastructure in Amazon Web Services (AWS).
This is where all administration and management functionality resides.

Your data and the actual computation involved in executing your Flyte tasks and workflows takes place on the data plane, a virtual private cloud that you control but that is administered and managed by the Union control plane.
To enable the administration and management of your data plane, you grant Union the required permissions when you set up your data plane.

Union supports data planes on Amazon WebServices (AWS), Google Cloud Platform (GCP), and Microsoft Azure.
