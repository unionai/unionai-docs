import inspect
from typing import Optional
from lib.parser.docstring import parse_docstring
from lib.ptypes import MethodInfo, PropertyInfo, VariableInfo


def parse_method(name: str, member: object) -> Optional[MethodInfo]:
    if not (inspect.isfunction(member) or inspect.ismethod(member)):
        return None

    doc_info = parse_docstring(inspect.getdoc(member), source=member)
    docstr = doc_info["docstring"] if doc_info else None
    params_docs = doc_info["params"] if doc_info else None
    sig = inspect.signature(member)
    param_types = {
        name: (
            param.annotation
            if str(param.annotation) != "<class 'inspect._empty'>"
            else ""
        )
        for name, param in sig.parameters.items()
    }
    return_type = (
        doc_info["return_type"]
        if doc_info != None and "return_type" in doc_info and doc_info["return_type"] != None
        else (
            sig.return_annotation
            if str(sig.return_annotation) != "<class 'inspect._empty'>"
            else "None"
        )
    )
    method_info = MethodInfo(
        name=name,
        doc=docstr,
        signature=str(sig),
        params=[
            {
                "name": param.name,
                "default": (
                    str(param.default)
                    if param.default != inspect.Parameter.empty
                    else None
                ),
                "kind": str(param.kind),
                "type": str(param_types[param.name]),
            }
            for param in inspect.signature(member).parameters.values()
        ],
        params_doc=params_docs,
        return_type=str(return_type),
    )
    return method_info


def parse_property(name: str, member: object) -> Optional[PropertyInfo]:
    if not isinstance(member, property):
        return None

    doc_info = parse_docstring(inspect.getdoc(member), source=member)
    docstr = doc_info["docstring"] if doc_info else None
    property_info = PropertyInfo(
        name=name,
        doc=docstr,
    )
    return property_info


def parse_variable(name: str, member: object) -> Optional[VariableInfo]:
    mtype = type(member).__name__
    if mtype == "module":
        return None

    var_info = VariableInfo(
        name=name,
        type=mtype,
    )

    return var_info
