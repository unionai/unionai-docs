import sys
import importlib.util
from types import ModuleType
from os import path
from typing import TypedDict, List, Dict, NotRequired
import yaml

class Metadata(TypedDict, total=False):
    title: NotRequired[str]
    title_expanded: NotRequired[str]
    name: NotRequired[str]
    version: NotRequired[str]
    author: NotRequired[str]
    author_email: NotRequired[str]
    description: NotRequired[str]
    namespace_packages: NotRequired[List[str]]
    packages: NotRequired[List[str]]
    install_requires: NotRequired[List[str]]
    license: NotRequired[str]
    python_requires: NotRequired[str]
    classifiers: NotRequired[List[str]]
    entry_points: NotRequired[Dict[str, List[str]]]
    folder: NotRequired[str]

# Create a fake setuptools module with our custom setup function
class CaptureMetadata(ModuleType):
    def __init__(self):
        super().__init__("setuptools")
        self.result = Metadata()

    def setup(self, **kwargs):
        self.result = Metadata(**kwargs)

    def find_namespace_packages(self, **kwargs):
        ...

class NoOp(ModuleType):
    def __init__(self, name):
        super().__init__(name)
        
        # Create a develop class with a run method if this is the develop module
        if name == "setuptools.command.develop":
            class DevelopMock:
                def run(self):
                    pass
            self.develop = DevelopMock

def load(plugin_root: str) -> Metadata:
    # Replace the real setuptools with our fake one in sys.modules
    md = CaptureMetadata()
    sys.modules["setuptools"] = md
    sys.modules["setuptools.command"] = NoOp("setuptools.command")
    sys.modules["setuptools.command.develop"] = NoOp("setuptools.command.develop")

    # Now import the docs-builder module
    spec = importlib.util.spec_from_file_location("docs_builder", 
                                                  path.join(plugin_root, "setup.py"))
    if spec is None or spec.loader is None:
        raise ImportError("Failed to load docs-builder module")
    docs_builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(docs_builder)

    # # You can now access anything from the docs_builder module
    # print("Plugin name:", docs_builder.PLUGIN_NAME)
    # print("Microlib name:", docs_builder.microlib_name)

    # print("Plugin metadata:")
    # for key, value in md.result.items():
    #     print(f"  {key}: {value}")

    md.result["folder"] = path.basename(plugin_root)

    return md.result

def to_yaml(metadata: Metadata) -> str:
    # Configure the YAML dumper to produce clean output
    def represent_none(self, _):
        return self.represent_scalar('tag:yaml.org,2002:null', '')
    
    yaml.add_representer(type(None), represent_none)
    
    # Convert the TypedDict to YAML
    return yaml.dump(dict(metadata), default_flow_style=False, sort_keys=False)
    