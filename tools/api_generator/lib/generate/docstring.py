from typing import Optional

def docstring_summary(docstring: Optional[str]) -> str:
    if docstring is None:
        return ""
    import re
    # fix for hugo shortcodes
    def replace_shortcode_periods(match):
        return match.group(0).replace(".", "___PERIOD___")
    
    pattern = r'{{<.*?>}}'
    protected_docstring = re.sub(pattern, replace_shortcode_periods, str(docstring))
    first_sentence = protected_docstring.split(".")[0]
    first_sentence = first_sentence.replace("___PERIOD___", ".")    
    return first_sentence.split("\n")[0].strip("\n") + "."