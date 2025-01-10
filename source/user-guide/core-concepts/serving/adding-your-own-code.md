# Adding your own code

In the introductory section we saw how to define and deploy a simple Streamlit app.
The app deployed was the default hello world Streamlit example app.
In this section we will expand on this by adding our own custom code to the app.

## Example app

We will initialize the app in `app.py` as before, but now we will add two files containing our own code, `main.py` and `utils.py`.

In a local directory, create the following files:

```{code-block} shell
├── app.py
├── main.py
└── utils.py
```

## App declaration

The file `app.py` contains the app declaration:

```{code-block} python
:caption: app.py

"""A Union app with custom code"""

from union import Resources
from union.app import App

app = App(
     name="streamlit-custom-code",
    container_image="ghcr.io/thomasjpfan/streamlit-app:0.1.30",
    command=["streamlit", "run", "main.py", "--server.port", "8080"],
    port=8080,
    limits=Resources(cpu="2", mem="3Gi"),
    include=[
        "./main.py",
        "./utils.py",
    ],
)
```

Compared to the first example we have added one more parameter:

* `include`: A list of files to be added to the container at deployment time, containing the custom code that defines the specific functionality of your app.

## Custom code

In this example we include two files containing custom logic: `main.py` and `utils.py`.

The file `main.py` contains the bulk of our custom code:

```{code-block} python
:caption: main.py

"""Custom Streamlit app code"""

import streamlit as st
from utils import process_user_input

st.title("Custom code demo")

user_input = st.text_input("Enter some text:")

if user_input:
    st.write("You entered:", process_user_input(user_input))
```

The file `utils.py` contains a supporting function that is imported into the file above.

```{code-block} python
:caption: utils.py

"""Custom Streamlit app supporting code"""

def process_user_input(value):
    return f"Processing {value}"
```

## Deploy the app

Deploy the app with:

```{code-block} shell
$ union deploy apps app.py streamlit-custom-code
```

## App deployment with included files

When a new app is deployed for the first time (i.e., there is no app registered with the specified `name`),
a container is spun up using the specified `container_image` and the files specified in `include` are
copied into the container. The `command` is the then executed in the container, starting the app.

If you alter the `include` code you need to re-deploy your app.
When `union deploy apps` is called using an app name that corresponds to an already existing app,
the app code is updated in the container and the app is restarted.

You can iterate on your app easily by changing your `include` code and re-deploying.

Because there is a slight performance penalty involved in copying the `include` files into the container,
you may wish to consolidate you code directly into custom-built image once you have successfully iterated to production quality.
