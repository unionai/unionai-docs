from typing import Dict, List, Literal, NotRequired, Optional, TypedDict


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


type FrameworkType = Literal["python", "synchronicity"]


class MethodInfo(TypedDict):
    name: str
    doc: Optional[str]
    signature: str
    params: List[ParamInfo]
    params_doc: Optional[ParamDict]
    return_type: str
    return_doc: Optional[str]
    framework: FrameworkType


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
