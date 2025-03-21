import io
from typing import List

from lib.ptypes import MethodInfo
from lib.generate.docstring import docstring_summary
from lib.generate.helper import generate_anchor_from_name


def generate_method_decl(name: str, method: MethodInfo, output: io.TextIOWrapper):
    # Filter out 'self' parameter
    filtered_params = [param for param in method["params"] if param["name"] != "self"]

    output.write("```python\n")
    try:
        if len(filtered_params) == 0:
            output.write(f"def {name}()\n")
            return

        output.write(f"def {name}(\n")
        for param in filtered_params:
            output.write(f"    {param['name']}")
            if "type" in param and param["type"]:
                output.write(
                    f": {format_type(param["name"], param['type'], code=True)}"
                )
            output.write(",\n")
        output.write("):\n")
    finally:
        output.write("```\n")


def format_type(name: str, type: str | None, code=False, escape_or=False) -> str:
    output = ""
    if name == "kwargs":
        output = "`**kwargs`"
    elif name == "args":
        output = "`*args`"
    elif type and type.startswith("<class '") and type.endswith("'>"):
        output = type[8:-2]
    else:
        output = type if type != "" else ""

    if output == "":
        return ""

    if escape_or:
        output = output.replace("|", "\\|")

    return f"`{output}`" if not code else str(output)


def generate_params(method: MethodInfo, output: io.TextIOWrapper):
    # Filter out 'self' parameter
    filtered_params = [param for param in method["params"] if param["name"] != "self"]

    # Check if there are any parameters left after filtering
    if not filtered_params:
        # output.write("No parameters\n")
        return

    multiline_start = "{{< multiline >}}"
    multiline_end = "{{< /multiline >}}"

    output.write("| Parameter | Type |\n")
    output.write("|-|-|\n")
    for param in filtered_params:
        typeOutput = format_type(
            param["name"], param["type"] if "type" in param else "", escape_or=True
        )
        doc = param["doc"] if "doc" in param else ""
        if doc:
            output.write(
                f"| `{param['name']}` | {multiline_start}{typeOutput}\ndoc: {doc}\n{multiline_end} |\n"
            )
        else:
            output.write(f"| `{param['name']}` | {typeOutput} |\n")
    output.write("\n")


def generate_signature(method: MethodInfo):
    params = []
    for param in method["params"]:
        param_str = param["name"]
        if "type" in param and param["type"]:
            param_str += f": {param['type']}"
        params.append(param_str)

    return f"{method['name']}({', '.join(params)}) -> {method['return_type']}"


def generate_signature_simple(method: MethodInfo, name: str = ""):
    result = "".join(
        [
            name if name else method["name"],
            "(",
            ", ".join([param["name"] for param in method["params"]]),
            ")",
            " -> ",
            method["return_type"],
        ]
    )
    return result


def generate_method_list(
    methods: List[MethodInfo], output: io.TextIOWrapper, doc_level: int
):
    output.write(f"{'#' * (doc_level)} Methods\n\n")

    output.write("| Method | Description |\n")
    output.write("|-|-|\n")

    for method in methods:
        output.write(
            f"| [`{method['name']}()`]({generate_method_link(method['name'])}) | {docstring_summary(method['doc'])} |\n"
        )

    output.write("\n\n")


def generate_method_link(name: str) -> str:
    anchor = generate_anchor_from_name(name)
    return f"#{anchor}"


def generate_method(method: MethodInfo, output: io.TextIOWrapper, doc_level: int):
    output.write(f"{'#' * (doc_level+1)} {method['name']}()\n\n")
    generate_method_decl(method["name"], method, output)
    if method["doc"]:
        output.write(f"{method['doc']}\n\n")
    generate_params(method, output)
