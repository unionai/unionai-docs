import io
from typing import List, TypedDict, Optional


version = "0.0.0"
variants = ""


def set_variants(v: List[str]):
    global variants
    variants = " ".join(v)


def set_version(v: str):
    global version
    version = v

class FrontMatterExtra(TypedDict):
    weight: Optional[int]
    expand_sidebar: Optional[bool]

def write_front_matter(title: str, output: io.TextIOWrapper, extra: Optional[FrontMatterExtra] = None):
    output.write("---\n")
    output.write(f"title: {title}\n")
    output.write(f"version: {version}\n")
    output.write(f"variants: {variants}\n")
    output.write("layout: py_api\n")
    if extra:
        if extra['weight']:
            output.write(f"weight: {extra['weight']}\n")
        if extra['expand_sidebar']:
            output.write("sidebar_expanded: true\n")
    output.write("---\n\n")
