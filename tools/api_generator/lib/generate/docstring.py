from typing import Optional


def docstring_summary(docstring: Optional[str]) -> str:
    return str(docstring).split(".")[0].split("\n")[0].strip("\n")