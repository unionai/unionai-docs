"""A simple Union.ai app using Streamlit"""

import union
import os

# The `ImageSpec` for the container that will run the `App`.
# `union-runtime` must be declared as a dependency,
# in addition to any other dependencies needed by the app code.
# Use Union remote Image builder to build the app container image
image = union.ImageSpec(
    name="streamlit-app",
    packages=["union-runtime>=0.1.18", "streamlit==1.51.0"],
    builder="union",
)

# The `App` declaration.
# Uses the `ImageSpec` declared above.
# In this case we do not need to supply any app code
# as we are using the built-in Streamlit `hello` app.
app = union.app.App(
    name="streamlit-hello",
    container_image=image,
    args="streamlit hello --server.port 8080",
    port=8080,
    limits=union.Resources(cpu="1", mem="1Gi"),
)
