import inspect
from typing import Optional, Any
from lib.parser.docstring import parse_docstring
from lib.ptypes import MethodInfo, PropertyInfo, VariableInfo, FrameworkType, ParamInfo


def parse_method(name: str, member: object) -> Optional[MethodInfo]:
    if not (inspect.isfunction(member) or inspect.ismethod(member)):
        return None

    return do_parse_method(name, member, "python")


def do_parse_method(name: str, member: Any, framework: FrameworkType) -> Optional[MethodInfo]:
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
        sig.return_annotation
        if str(sig.return_annotation) != "<class 'inspect._empty'>"
        else "None"
    )
    return_doc = doc_info["return_doc"] \
        if doc_info is not None and "return_doc" in doc_info and doc_info["return_doc"] is not None \
        else None

    method_info = MethodInfo(
        name=name,
        doc=docstr,
        signature=str(sig),
        params=[
            ParamInfo(
                name=param.name,
                default=(
                    str(param.default)
                    if param.default != inspect.Parameter.empty
                    else None
                ),
                kind=str(param.kind),
                type=str(param_types[param.name]),
                doc=None
            )
            for param in inspect.signature(member).parameters.values()
        ],
        params_doc=params_docs,
        return_type=str(return_type),
        return_doc=return_doc,
        framework=framework,
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
        type=None
    )
    return property_info


def parse_variable(name: str, member: object) -> Optional[VariableInfo]:
    mtype = type(member).__name__
    if mtype == "module":
        return None

    var_info = VariableInfo(
        name=name,
        type=mtype,
        doc=None
    )

    return var_info
