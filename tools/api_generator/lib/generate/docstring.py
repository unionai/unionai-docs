from typing import Optional


def docstring_summary(docstring: Optional[str]) -> str:
    if docstring is None:
        return ""
    return str(docstring).strip("\n").split(".")[0].split("\n")[0].strip("\n") + "."
