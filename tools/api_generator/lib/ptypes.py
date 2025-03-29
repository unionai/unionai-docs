from types import ModuleType
from typing import Dict, List, MutableSequence, NotRequired, Optional, TypedDict

class PropertyInfo(TypedDict):
    name: str
    type: NotRequired[Optional[str]]
    doc: NotRequired[Optional[str]]

class VariableInfo(PropertyInfo):
    pass

type ParamDict = Dict[str, ParamInfo]


class ParamInfo(TypedDict):
    name: str
    default: NotRequired[Optional[str]]
    kind: NotRequired[Optional[str]]
    type: NotRequired[Optional[str]]
    doc: NotRequired[Optional[str]]


class MethodInfo(TypedDict):
    name: str
    doc: Optional[str]
    signature: str
    params: List[ParamInfo]
    params_doc: Optional[ParamDict]
    return_type: str




class ClassDetails(TypedDict):
    name: str
    path: str
    doc: Optional[str]
    module: str
    bases: List[str]
    is_exception: bool
    methods: List[MethodInfo]
    properties: List[PropertyInfo]
    class_variables: List[VariableInfo]


type ClassMap = dict[str, ClassDetails]
type ClassPackageMap = dict[str, ClassMap]


class PackageInfo(TypedDict):
    name: str
    doc: NotRequired[Optional[str]]
    methods: List[MethodInfo]
    variables: List[VariableInfo]


class ParsedInfo(TypedDict):
    version: str
    packages: List[PackageInfo]
    classes: ClassPackageMap
