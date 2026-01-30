from typing import Dict, List, Literal, Optional, TypedDict

class PropertyInfo(TypedDict):
    name: str
    type: Optional[str]
    doc: Optional[str]


class VariableInfo(PropertyInfo):
    pass


class ParamInfo(TypedDict):
    name: str
    default: Optional[str]
    kind: Optional[str]
    type: Optional[str]
    doc: Optional[str]

ParamDict = Dict[str, ParamInfo]

FrameworkType = Literal["python", "syncify"]


class MethodInfo(TypedDict):
    name: str
    doc: Optional[str]
    signature: str
    params: List[ParamInfo]
    params_doc: Optional[ParamDict]
    return_type: str
    return_doc: Optional[str]
    framework: FrameworkType
    parent_name: Optional[str]


class ClassDetails(TypedDict):
    name: str
    path: str
    doc: Optional[str]
    module: str
    parent: Optional[str]
    bases: List[str]
    is_exception: bool
    methods: List[MethodInfo]
    properties: List[PropertyInfo]
    class_variables: List[VariableInfo]


ClassMap = dict[str, ClassDetails]
ClassPackageMap = dict[str, ClassMap]


class PackageInfo(TypedDict):
    name: str
    doc: Optional[str]
    methods: List[MethodInfo]
    variables: List[VariableInfo]


class ParsedInfo(TypedDict):
    version: str
    packages: List[PackageInfo]
    classes: ClassPackageMap
