from typing import Dict, List, NotRequired, Optional, TypedDict


class VariableInfo(TypedDict):
    name: str
    type: str
    value: str


type ParamDict = Dict[str, ParamInfo]


class ParamInfo(TypedDict):
    name: str
    default: NotRequired[Optional[str]]
    kind: NotRequired[Optional[str]]
    type: NotRequired[Optional[str]]
    doc: NotRequired[Optional[str]]


class MethodInfo(TypedDict):
    name: str
    docstring: Optional[str]
    signature: str
    params: List[ParamInfo]
    params_doc: Optional[ParamDict]
    return_type: str


class PropertyInfo(TypedDict):
    name: str
    docstring: Optional[str]


class ClassDetails(TypedDict):
    name: str
    path: str
    docstring: Optional[str]
    module: str
    bases: List[str]
    is_exception: bool
    methods: List[MethodInfo]
    properties: List[PropertyInfo]
    class_variables: List[VariableInfo]


type ClassMap = dict[str, ClassDetails]
type ClassPackageMap = dict[str, ClassMap]


class ParsedInfo(TypedDict):
    version: str
    packages: list[str]
    classes: ClassPackageMap
