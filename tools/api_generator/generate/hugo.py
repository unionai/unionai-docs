import io
from typing import List


version = "0.0.0"
variants = ""


def set_variants(v: List[str]):
    global variants
    variants = " ".join(v)


def set_version(v: str):
    global version
    version = v


def write_front_matter(title: str, output: io.TextIOWrapper):
    output.write(f"---\n")
    output.write(f"title: {title}\n")
    output.write(f"version: {version}\n")
    output.write(f"variants: {variants}\n")
    output.write(f"layout: api\n")
    output.write(f"---\n\n")
