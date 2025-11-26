import io
from typing import List, Optional

from lib.ptypes import MethodInfo
from lib.generate.docstring import docstring_summary
from lib.generate.helper import generate_anchor_from_name


def generate_method_decl(
    name: str,
    method: MethodInfo,
    output: io.TextIOWrapper,
    is_class: bool = False,
    is_protocol: bool = False,
):
    # Filter out 'self' parameter
    filtered_params = [param for param in method["params"] if param["name"] != "self"]

    if method["framework"] == "syncify":
        qual_name = f"{method["parent_name"]}.{name}" if method["parent_name"] else name
        output.write(
            f"""
> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await {qual_name}.aio()`.
"""
        )

    output.write("```python\n")
    try:
        if len(filtered_params) == 0:
            output.write(f"def {name}()\n")
            return

        if is_protocol:
            output.write(f"protocol {name}()\n")
        elif is_class:
            output.write(f"class {name}(\n")
        else:
            output.write(f"def {name}(\n")

        if not is_protocol:
            for param in filtered_params:
                output.write(f"    {param['name']}")
                if "type" in param and param["type"]:
                    output.write(
                        f": {format_type(param['name'], param['type'], code=True)}"
                    )
                output.write(",\n")

            if not is_class and method["return_type"] and method["return_type"] != "None":
                output.write(
                    f") -> {format_type(None, method['return_type'], markdown=False)}\n"
                )
            else:
                output.write(")\n")
    finally:
        output.write("```\n")


def format_type(
    name: Optional[str], type: str | None, code=False, escape_or=False, markdown=True
) -> str:
    output = ""
    if name is not None:
        if name == "kwargs":
            output = "**kwargs"
        elif name == "args":
            output = "*args"

    if output == "":
        if type and type.startswith("<class '") and type.endswith("'>"):
            output = type[8:-2]
        else:
            output = type if type != "" else ""

    if output == "" or output is None:
        return ""

    if escape_or:
        output = output.replace("|", "\\|")

    if markdown:
        return f"`{output}`" if not code else str(output)
    else:
        return f"{output}" if not code else str(output)


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
        
        # Look for documentation in params_doc field first, then fallback to param doc
        doc = ""
        if "params_doc" in method and method["params_doc"] and param["name"] in method["params_doc"]:
            doc = method["params_doc"][param["name"]]["doc"] or ""
        elif "doc" in param:
            doc = param["doc"] or ""
            
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
