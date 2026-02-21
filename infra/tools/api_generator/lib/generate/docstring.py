from typing import Optional
import re

def docstring_summary(docstring: Optional[str]) -> str:
    if docstring is None:
        return ""

    docstring = str(docstring).strip()

    # Skip alert/admonition lines at the start (GitHub alerts and MkDocs admonitions)
    lines = docstring.split("\n")
    content_lines = []
    in_alert = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(">") or stripped.startswith("!!!"):
            in_alert = True
            continue
        if in_alert and stripped == "":
            in_alert = False
            continue
        if not in_alert:
            content_lines.append(line)

    docstring = "\n".join(content_lines).strip()
    if not docstring:
        return ""

    def replace_shortcode_periods(match):
        return match.group(0).replace(".", "___PERIOD___")

    # non-greedy
    pattern = r"{{<.*?>}}"
    protected_docstring = re.sub(pattern, replace_shortcode_periods, docstring)
    first_sentence = protected_docstring.split(".")[0]
    first_sentence = first_sentence.replace("___PERIOD___", ".")
    first_line = first_sentence.split("\n")[0].strip()
    return first_line + "." if first_line else ""
