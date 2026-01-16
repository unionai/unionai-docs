import inspect
import json
from typing import TypedDict, Optional

from lib.ptypes import ParamDict, ParamInfo


_returns = [
    "return",
    "rcode",
    "result",
    "rtype",
]

class DocstringInfo(TypedDict):
    docstring: str
    params: ParamDict
    return_doc: Optional[str]


def parse_docstring(docstring: str | None, source) -> Optional[DocstringInfo]:
    if not docstring:
        return None

    if "See help(type(self)) for accurate signature." in docstring:
        return None

    try:
        # Attempt to check if the signature matches. If yes, we have no docs.
        #if f"inspect.signature(source) == inspect.signature(eval(docstring)):
        #    return None
        method_decl = f"{source.__name__}{inspect.signature(source)}"
        if method_decl.startswith(docstring):
            return None
    except:
        pass

    # Removes the specicial !!!! notes
    docstring = format_three_exclamation_notes(docstring)

    lines = docstring.split("\n")
    # print(lines)

    result = DocstringInfo(docstring="", params={}, return_doc=None)

    current_param = None
    in_args = False
    leading_spaces = -1
    args_leading_spaces = -1
    args_continuation_spaces = -1

    # Enumerate lines
    for i, line in enumerate(lines):
        if leading_spaces == -1:
            # Wait for the first line
            if line.strip() == "":
                continue

            leading_spaces = len(line) - len(line.lstrip())
            # print(leading_spaces, file=stderr)

        line = line[leading_spaces:]
        # print(leading_spaces, ">", line, file=stderr)

        if not in_args and line.strip() == "Args:":
            in_args = True
            args_leading_spaces = -1
            continue

        if in_args:
            if args_leading_spaces == -1:
                args_leading_spaces = len(line) - len(line.lstrip())
            if args_leading_spaces != -1:
                line = line[args_leading_spaces:]

            # print(args_leading_spaces, ">>", line)

            if len(line.strip()) == 0:
                continue

            if line[0] != " ":
                # New parameter
                param_parts = line.split(":")
                if len(param_parts) != 2:
                    continue
                param_name_and_type = param_parts[0].strip()
                param_description = param_parts[1].strip()

                # Extract type information from format: param_name (type)
                param_type = None
                if "(" in param_name_and_type and param_name_and_type.endswith(")"):
                    # Find the last opening parenthesis to handle cases like "param_name (Dict[str, int])"
                    type_start = param_name_and_type.rfind("(")
                    current_param = param_name_and_type[:type_start].strip()
                    param_type = param_name_and_type[type_start+1:-1].strip()
                else:
                    current_param = param_name_and_type

                param = ParamInfo(
                    name=current_param,
                    doc=param_description,
                    type=param_type,
                    default=None,
                    kind=None,
                )
                result["params"][current_param] = param
                args_continuation_spaces = -1
            elif current_param:
                if args_continuation_spaces == -1:
                    args_continuation_spaces = len(line) - len(line.lstrip())
                if args_continuation_spaces != -1:
                    line = line[args_continuation_spaces:]

                # Param doc
                param = result["params"][current_param]
                # Ensure param["doc"] is initialized properly before concatenating
                if "doc" not in param or param["doc"] is None:
                    param["doc"] = line
                else:
                    param["doc"] = param["doc"] + "\n" + line
        else:
            line_params = line.strip()

            for r in _returns:
                if line_params.startswith(f":{r}:"):
                    result["return_doc"] = line_params[len(r):].strip()
                    continue

            if not current_param and not line_params.startswith(":param"):
                result["docstring"] += line + "\n"

            if current_param:
                if not line_params.startswith(":param"):
                    param = result["params"][current_param]
                    # Ensure param["doc"] is initialized properly before concatenating
                    if "doc" not in param or param["doc"] is None:
                        param["doc"] = line_params
                    else:
                        param["doc"] = param["doc"] + "\n" + line_params
                    continue

            if line_params.startswith(":param"):
                param_parts = line_params.split(":")
                param_name = param_parts[1].strip().replace("param ", "")
                param_doc = param_parts[2].strip() if len(param_parts) > 2 else ""
                current_param = param_name
                param = ParamInfo(
                    name=param_name,
                    doc=param_doc,
                    type=None,
                    default=None,
                    kind=None,
                )
                result["params"][current_param] = param
                # print("PARAM: ", param_name, param_doc)

        # if not current_param:
        #     print(f"DOC: {line}")

    return result


def test_parse_params():
    test = """
    Call this with any Encoder or Decoder to register it with the\
          flytekit type system. If your handler does not\nspecify a protocol (e.g.\
          s3, gs, etc.) field, then\n\n:param h: The StructuredDatasetEncoder or\
          StructuredDatasetDecoder you wish to register with this transformer.\n\
          :param default_for_type: If set, when a user returns from a task an instance\
          of the dataframe the handler\n  handles, e.g. ``return pd.DataFrame(...)``,\
          not wrapped around the ``StructuredDataset`` object, we will\n  use this\
          handler's protocol and format as the default, effectively saying that\
          this handler will be called.\n  Note that this shouldn't be set if your\
          handler's protocol is None, because that implies that your handler\n \
          is capable of handling all the different storage protocols that flytekit's\
          data persistence layer is aware of.\n  In these cases, the protocol is\
          determined by the raw output data prefix set in the active context.\n\
          :param override: Override any previous registrations. If default_for_type\
          is also set, this will also override\n  the default.\n:param default_format_for_type:\
          Unlike the default_for_type arg that will set this handler's format and\
          storage\n  as the default, this will only set the format. Error if already\
          set, unless override is specified.\n:param default_storage_for_type: Same\
          as above but only for the storage format. Error if already set,\n  unless\
          override is specified.
    """
    print(json.dumps(parse_docstring(test, source=None), indent=2))


def test_parse_args():
    doc_with_args = """
    This class is used to specify the docker image that will be used to run the task.

    Args:
        name: name of the image.
        python_version: python version of the image. Use default python in the base image if None.
        builder: Type of plugin to build the image. Use envd by default.
        source_root: source root of the image.
        env: environment variables of the image.
        registry: registry of the image.
        pip_secret_mounts: Specify a list of tuples to mount secret for pip install. Each tuple should contain the path to
            the secret file and the mount path. For example, [(".gitconfig", "/etc/gitconfig")]. This is experimental and
            the interface may change in the future. Configuring this should not change the built image.
        pip_extra_args: Specify one or more extra pip install arguments as a space-delimited string
        registry_config: Specify the path to a JSON registry config file
        source_copy_mode: This option allows the user to specify which source files to copy from the local host, into the image.
            Not setting this option means to use the default flytekit behavior. The default behavior is:
                - if fast register is used, source files are not copied into the image (because they're already copied
                  into the fast register tar layer).
                - if fast register is not used, then the LOADED_MODULES (aka 'auto') option is used to copy loaded
                  Python files into the image.

            If the option is set by the user, then that option is of course used.
        copy: List of files/directories to copy to /root. e.g. ["src/file1.txt", "src/file2.txt"]
        python_exec: Python executable to use for install packages
    """
    print(json.dumps(parse_docstring(doc_with_args, source=None), indent=2))

def convert_pydantic_links(text: str) -> str:
    """
    Convert pydantic documentation links to absolute URLs.

    Handles two formats:
    1. Relative path links: ../concepts/models.md#model-copy
    2. Reference-style links: [`text`][pydantic.BaseModel.something]
    """
    import re
    import sys

    def replace_inline_link(match):
        link_text = match.group(1)
        link_path = match.group(2)

        # Check if it's a relative pydantic docs link
        if link_path.startswith('../concepts/') or link_path.startswith('./concepts/'):
            # Convert ../concepts/models.md#model-copy to concepts/models/#model-copy
            path = link_path.lstrip('./')
            # Remove .md extension and adjust anchor
            path = re.sub(r'\.md(#|$)', r'/\1', path)
            return f'[{link_text}](https://docs.pydantic.dev/latest/{path})'

        return match.group(0)

    def replace_reference_link(match):
        link_text = match.group(1)
        reference = match.group(2)

        # Map pydantic references to their API doc pages
        if reference.startswith('pydantic_core.'):
            url = f'https://docs.pydantic.dev/latest/api/pydantic_core/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.main.BaseModel.') or reference.startswith('pydantic.BaseModel.'):
            url = f'https://docs.pydantic.dev/latest/api/base_model/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.config.ConfigDict.') or reference.startswith('pydantic.ConfigDict'):
            url = f'https://docs.pydantic.dev/latest/api/config/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.fields.'):
            url = f'https://docs.pydantic.dev/latest/api/fields/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.functional_serializers.'):
            url = f'https://docs.pydantic.dev/latest/api/functional_serializers/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.root_model.'):
            url = f'https://docs.pydantic.dev/latest/api/root_model/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.types.'):
            url = f'https://docs.pydantic.dev/latest/api/types/#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('pydantic.'):
            # Generic pydantic reference - try base_model as default
            url = f'https://docs.pydantic.dev/latest/api/base_model/#{reference}'
            return f'[{link_text}]({url})'

        # Map Python stdlib references to docs.python.org
        elif reference.startswith('object.'):
            url = f'https://docs.python.org/3/library/stdtypes.html#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('functools.'):
            url = f'https://docs.python.org/3/library/functools.html#{reference}'
            return f'[{link_text}]({url})'
        elif reference.startswith('inspect.'):
            url = f'https://docs.python.org/3/library/inspect.html#{reference}'
            return f'[{link_text}]({url})'
        elif reference == 'frame-objects':
            url = 'https://docs.python.org/3/reference/datamodel.html#frame-objects'
            return f'[{link_text}]({url})'

        # Log unhandled reference-style links
        print(f"WARNING: Unhandled reference-style link: [{link_text}][{reference}]", file=sys.stderr)
        return match.group(0)

    # Match inline markdown links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_inline_link, text)

    # Match reference-style markdown links: [text][reference]
    text = re.sub(r'\[([^\]]+)\]\[([^\]]+)\]', replace_reference_link, text)

    return text


def format_three_exclamation_notes(docstring: str) -> str:
    """
    Receives a docstring that contains lines like:

        !!! warning "Deprecated"
        This method is now deprecated; use `model_copy` instead.

    And converts them to:

        > [!WARNING] Deprecated
        > This method is now deprecated; use `model_copy` instead.

    Also handles !!! abstract and !!! note admonitions, and converts
    relative pydantic documentation links to absolute URLs.
    """
    # First convert any pydantic-relative links to absolute URLs
    docstring = convert_pydantic_links(docstring)

    lines = docstring.split("\n")
    result = []
    converting = False
    for line in lines:
        stripped = line.strip()  # Check stripped version to handle leading whitespace
        if stripped.startswith("!!! warning"):
            parts = stripped.split(" ")
            if len(parts) < 3:
                continue
            title = parts[2].replace('"', '')
            result.append(f"> [!WARNING] {title}")
            converting = True
        elif stripped.startswith("!!! note"):
            result.append("> [!NOTE]")
            converting = True
        elif stripped.startswith("!!! abstract"):
            # Extract title from !!! abstract "Title"
            parts = stripped.split('"')
            title = parts[1] if len(parts) >= 2 else "Note"
            # Add clarification for pydantic inherited method documentation
            if title == "Usage Documentation":
                title = "Usage Documentation (external docs for inhertied method)"
            result.append(f"> [!TIP] {title}")
            converting = True
        elif converting:
            if len(stripped) > 0:
                result.append(f"> {stripped}")
            else:
                result.append("")
                converting = False
        else:
            converting = False
            result.append(line)
    return "\n".join(result)


def main():
    test_parse_params()
    test_parse_args()


if __name__ == "__main__":
    main()
