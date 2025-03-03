# Installation guide

In the BYOK model, the customer deploys the data plane themselves. Union data plane runs on a standard Kubernetes cluster.

Union data plane is distributed as standard Helm Charts, with overridable values.

```{admonition} Other distribution mechanisms
Although Helm Chart is a popular and well-established standard Kubernetes distribution mechanism,
our Engineering team is investigating other installation and distribution mechanisms, such as Terraform,
to more easily integrate with the customers’ deployment systems.
```
