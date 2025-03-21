import os


def generate_anchor_from_name(name: str) -> str:
    return name.lower().replace("(", "").replace(")", "").replace(".", "")
