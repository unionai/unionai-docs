from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging
from pathlib import Path
import os
import inspect
import re
import sys
import importlib
import importlib.util
import pkgutil
import traceback
from typing import Dict, Any, List, Optional, Set, Tuple

from pdoc.doc import Module, Class, Function, Variable

logger = logging.getLogger(__name__)

class ModuleProcessor:
    """
    processes python modules for doc generation using a hybrid approach that 
    combines pdoc's documentation generation with the module explorer's traversal abilities.
    """
    
    def __init__(self, max_depth: int = 10):
        """
        init the module processor.
        
        Args:
            max_depth: max depth to traverse when exploring submodules
        """
        self.max_depth = max_depth
        self.visited_modules: Set[str] = set()
        
    def explore_package(self, package_name: str) -> Dict[str, Any]:
        """
        Explore a package and all its submodules.
        
        Args:
            package_name: Name of the package to explore
            
        Returns:
            Dictionary containing the module structure
        """
        try:
            # import the package
            package = self._safe_import_module(package_name)
            if not package:
                logger.warning(f"Could not import package {package_name}")
                return {}
                
            result = self._explore_module(package, depth=0)
            return result
        except Exception as e:
            logger.error(f"Error exploring package {package_name}: {str(e)}")
            logger.error(traceback.format_exc())
            return {}
            
    def _safe_import_module(self, module_name: str) -> Any:
        """Safely import a module with multiple fallback methods."""
        # try multiple import strategies
        try:
            # std import
            return importlib.import_module(module_name)
        except ImportError:
            logger.debug(f"Standard import failed for {module_name}")
            
            try:
                # try with importlib.util
                spec = importlib.util.find_spec(module_name)
                if spec is not None:
                    return importlib.util.module_from_spec(spec)
            except (ImportError, AttributeError):
                logger.debug(f"Spec-based import failed for {module_name}")
            
            # try progressive import approach
            parts = module_name.split('.')
            for i in range(1, len(parts)):
                try:
                    # import parent modules one level at a time
                    parent = importlib.import_module('.'.join(parts[:i]))
                    if hasattr(parent, parts[i]):
                        # if the parent has the child as an attribute
                        child = getattr(parent, parts[i])
                        if inspect.ismodule(child):
                            return child
                except (ImportError, AttributeError):
                    pass
            
            logger.warning(f"All import strategies failed for {module_name}")
            return None
    
    def _is_importable_submodule(self, parent_module: Any, submodule_name: str) -> bool:
        """Check if a submodule is importable without actually importing it."""
        if not hasattr(parent_module, '__path__'):
            return False
            
        full_name = f"{parent_module.__name__}.{submodule_name}"
        try:
            return importlib.util.find_spec(full_name) is not None
        except (ModuleNotFoundError, ValueError):
            return False
    
    def _explore_module(self, module: Any, depth: int = 0) -> Dict[str, Any]:
        """
        Recursively explore a module and its submodules.
        
        Args:
            module: The module object to explore
            depth: Current recursion depth
            
        Returns:
            Dictionary containing the module structure
        """
        if depth > self.max_depth:
            return {"name": module.__name__, "type": "module", "truncated": True}
            
        # no revisiting modules
        if module.__name__ in self.visited_modules:
            return {"name": module.__name__, "type": "module", "visited": True}
            
        self.visited_modules.add(module.__name__)
        
        module_info = {
            "name": module.__name__,
            "type": "module" if not hasattr(module, "__path__") else "package",
            "file": getattr(module, "__file__", None),
            "doc": inspect.getdoc(module),
            "members": {},
            "submodules": []
        }
        
        # if this is a package, explore its submodules
        if hasattr(module, "__path__"):
            # Use pkgutil to find all submodules
            for finder, submodule_name, is_pkg in pkgutil.iter_modules(module.__path__, module.__name__ + '.'):
                # Extract the local name (without the parent prefix)
                local_name = submodule_name.split('.')[-1]
                
                try:
                    # Try to import the submodule
                    submodule = self._safe_import_module(submodule_name)
                    if submodule:
                        submodule_info = self._explore_module(submodule, depth + 1)
                        module_info["submodules"].append(submodule_info)
                    else:
                        # If import failed but the submodule exists
                        if self._is_importable_submodule(module, local_name):
                            module_info["submodules"].append({
                                "name": submodule_name,
                                "type": "package" if is_pkg else "module",
                                "import_error": True
                            })
                except Exception as e:
                    logger.debug(f"Error exploring submodule {submodule_name}: {str(e)}")
                    module_info["submodules"].append({
                        "name": submodule_name,
                        "error": str(e)
                    })
        
        # get module members (classes, functions, etc.)
        try:
            for name, obj in inspect.getmembers(module):
                # skip private members
                if name.startswith('_') and name != '__init__':
                    continue
                    
                # skip imported modules
                if inspect.ismodule(obj):
                    continue
                
                # skip objects from other modules
                if hasattr(obj, '__module__') and obj.__module__ != module.__name__:
                    continue
                    
                # get info about the member
                if inspect.isclass(obj):
                    member_type = "class"
                    member_doc = inspect.getdoc(obj)
                    member_info = self._get_class_info(obj)
                elif inspect.isfunction(obj):
                    member_type = "function"
                    member_doc = inspect.getdoc(obj)
                    member_info = self._get_function_info(obj)
                else:
                    member_type = type(obj).__name__
                    member_doc = None
                    member_info = {}
                    
                module_info["members"][name] = {
                    "type": member_type,
                    "doc": member_doc,
                    **member_info
                }
        except Exception as e:
            logger.warning(f"Error getting members from {module.__name__}: {str(e)}")
            
        return module_info
    
    def _get_class_info(self, cls: Any) -> Dict[str, Any]:
        """Extract information about a class."""
        methods = {}
        
        try:
            for name, method in inspect.getmembers(cls, inspect.isfunction):
                if not name.startswith('_') or name == '__init__':
                    methods[name] = {
                        "doc": inspect.getdoc(method),
                        "signature": str(inspect.signature(method))
                    }
                    
            return {
                "methods": methods,
                "bases": [base.__name__ for base in cls.__bases__ if base.__name__ != 'object']
            }
        except Exception as e:
            logger.debug(f"Error getting class info for {cls.__name__}: {str(e)}")
            return {"methods": {}, "bases": []}
    
    def _get_function_info(self, func: Any) -> Dict[str, Any]:
        """Extract information about a function."""
        try:
            return {
                "signature": str(inspect.signature(func))
            }
        except Exception:
            return {"signature": "()"}

def get_source_code(obj):
    """Extract source code if available"""
    try:
        return inspect.getsource(obj.obj)
    except (TypeError, AttributeError, OSError):
        return None

def extract_signature(method_str):
    """Extract method signature from the string representation"""
    if '(' not in method_str:
        return {}
    
    try:
        sig_str = method_str[method_str.index('('):method_str.rindex(')')+1]
        params = sig_str.strip('()').split(',')
        param_dict = {}
        
        for p in params:
            p = p.strip()
            if not p:
                continue
            if ':' in p:
                name, type_hint = p.split(':', 1)
                param_dict[name.strip()] = type_hint.strip()
            else:
                param_dict[p] = None
                
        return param_dict
    except:
        return {}

def clean_docstring(docstring: str) -> str:
    """
    Cleans docstring for Sphinx compatibility:
    1. Markdown-style code fences (```python ... ```) become reST code blocks.
    2. Lines like 'param foo:' become ':param foo:' so Sphinx autodoc picks them up.
    3. Lines like 'returns:' or 'return:' become ':returns:'.
    """
    if not docstring:
        return ""

    # 1) convert markdown code fences -> reST code blocks
    def code_replacer(match):
        code = match.group(1)
        indented = "\n".join("    " + line for line in code.splitlines())
        return f"\n.. code-block:: python\n\n{indented}\n"

    docstring = re.sub(
        r"```(?:python)?\n(.*?)\n```",
        code_replacer,
        docstring,
        flags=re.DOTALL
    )

    # 2) convert lines like 'param foo:' -> ':param foo:'
    #    We look for the beginning of a line (possibly with some spaces) then "param <name>:"
    docstring = re.sub(
        r"(?m)^\s*param\s+([\w_]+):",
        r":param \1:",
        docstring
    )

    # also handle "type foo:" -> ":type foo:"
    docstring = re.sub(
        r"(?m)^\s*type\s+([\w_]+):",
        r":type \1:",
        docstring
    )

    # 3) convert "returns:" / "return:" -> ":returns:"
    docstring = re.sub(
        r"(?m)^\s*returns?:",
        ":returns:",
        docstring
    )

    return docstring

def validate_config(app: Sphinx, config: Config) -> None:
    """Validate the extension configuration."""
    if not hasattr(config, "pdoc_modules"):
        logger.warning("No modules specified in pdoc_modules configuration")
        config.pdoc_modules = []

    if not isinstance(config.pdoc_modules, (list, tuple)):
        raise ValueError("pdoc_modules must be a list or tuple of module names")
        
    # attempt to preload the specified modules to identify potential issues early
    for module_name in config.pdoc_modules:
        try:
            if importlib.util.find_spec(module_name) is None:
                raise ImportError(f"Module {module_name} not found")
            logger.info(f"Module {module_name} can be found")
        except (ImportError, AttributeError, ModuleNotFoundError) as e:
            logger.warning(f"Module {module_name} may have import issues: {str(e)}")

def generate_pdoc_docs(app: Sphinx) -> None:
    """Generate API documentation with structured folders and sidebar navigation."""
    variants = ["serverless", "byoc"]

    output_base = Path(app.confdir) / app.config.pdoc_output_dir
    output_base.mkdir(parents=True, exist_ok=True)

    # det the variant dynamically from the folder structure
    current_variant = determine_variant(output_base, variants)
    
    # create the main index file (index.rst) for the doc set
    create_main_index(app, output_base)
    
    # process each module
    for module_name in app.config.pdoc_modules:
        try:
            logger.info(f"Generating documentation for module: {module_name}")

            module_root_dir = output_base / module_name
            module_root_dir.mkdir(parents=True, exist_ok=True)

            # use the ModuleProcessor to explore the module structure
            processor = ModuleProcessor()
            module_info = processor.explore_package(module_name)
            
            if not module_info:
                logger.warning(f"Could not explore module {module_name}, creating placeholder")
                create_placeholder_module_doc(
                    module_name,
                    module_root_dir,
                    output_base,
                    current_variant,
                    variants
                )
                continue
            
            # generate documentation from the module_info
            generate_docs_from_module_info(
                module_info, 
                module_root_dir, 
                output_base,
                current_variant,
                variants
            )
            
            logger.info(f"Successfully processed {module_name}")

        except Exception as e:
            logger.error(f"Error processing module {module_name}: {str(e)}")
            logger.error(traceback.format_exc())
            
            # create a placeholder for the failed module
            create_placeholder_module_doc(
                module_name,
                output_base / module_name,
                output_base,
                current_variant,
                variants
            )

def create_main_index(app: Sphinx, output_base: Path) -> None:
    """Create the main index.rst file for the API documentation."""
    index_path = output_base / "index.rst"
    with open(index_path, "w", encoding="utf-8") as f:
        title = "Union SDK"
        underline = "=" * len(title)
        f.write(f"{title}\n{underline}\n\n")
        f.write("This section contains the API reference documentation for the Union SDK.\n\n")
        f.write(".. toctree::\n")
        f.write("   :maxdepth: 3\n\n")
        for module_name in app.config.pdoc_modules:
            f.write(f"   {module_name}/index\n")
        f.write("\n")

def determine_variant(output_base: Path, variants: List[str]) -> str:
    """Determine the current variant dynamically based on the directory structure."""
    for variant in variants:
        if f"/{variant}/" in str(output_base) or output_base.name == variant:
            return variant
    return "serverless"  # default if no match is found

def generate_docs_from_module_info(
    module_info: Dict[str, Any],
    output_dir: Path,
    root_output: Path,
    current_variant: str,
    variants: List[str],
    parent_path: str = ""
) -> None:
    """Generate documentation files from the module_info dictionary."""
    module_name = module_info["name"]
    short_name = module_name.split(".")[-1]
    
    # create module directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # start building the index content
    index_content = []
    
    # add title and module docstring
    title = short_name
    underline = "=" * len(title)
    index_content.append(f"{title}\n{underline}\n\n")
    
    if module_info.get("doc"):
        clean_doc = clean_docstring(module_info["doc"])
        index_content.append(f"{clean_doc}\n\n")
    
    index_content.append(f".. module:: {module_name}\n\n")
    index_content.append(f".. automodule:: {module_name}\n")
    index_content.append("   :noindex:\n\n")
    
    # track all sections for the toctree
    all_sections = []
    
    # process submodules
    if module_info.get("submodules"):
        submodules_section = []
        submodules_section.append("Submodules\n----------\n\n")
        
        # write each submodule
        for submodule in sorted(module_info["submodules"], key=lambda m: m["name"]):
            submodule_name = submodule["name"].split(".")[-1]
            submodule_dir = output_dir / submodule_name
            
            if not submodule.get("error") and not submodule.get("import_error"):
                # process the submodule recursively
                generate_docs_from_module_info(
                    submodule,
                    submodule_dir,
                    root_output,
                    current_variant,
                    variants,
                    f"{parent_path}/{short_name}" if parent_path else short_name
                )
                all_sections.append(f"{submodule_name}/index")
                submodules_section.append(f"* :doc:`{submodule_name}/index`\n")
            else:
                # create placeholder for failed submodule
                create_placeholder_module_doc(
                    submodule["name"],
                    submodule_dir,
                    root_output,
                    current_variant,
                    variants
                )
                all_sections.append(f"{submodule_name}/index")
                submodules_section.append(f"* :doc:`{submodule_name}/index` (Import Failed)\n")
        
        if len(submodules_section) > 1:  # Only add if we have submodules
            submodules_section.append("\n")
            index_content.extend(submodules_section)
    
    # process members by category
    for category_name, category_title, member_filter in [
        ("classes", "Classes", lambda m: m["type"] == "class"),
        ("functions", "Functions", lambda m: m["type"] == "function"),
        ("variables", "Variables", lambda m: m["type"] not in ["class", "function", "module"])
    ]:
        members = [(name, member) for name, member in module_info.get("members", {}).items() 
                  if member_filter(member)]
        
        if members:
            # create category section
            category_section = []
            category_section.append(f"{category_title}\n{'-' * len(category_title)}\n\n")
            
            category_dir = output_dir / category_name
            category_dir.mkdir(exist_ok=True)
            
            # create category index
            category_index_content = []
            category_index_content.append(f"{module_name} {category_title}\n")
            category_index_content.append("=" * len(f"{module_name} {category_title}") + "\n\n")
            category_index_content.append(".. toctree::\n")
            category_index_content.append("   :maxdepth: 1\n\n")
            
            # process each member
            for member_name, member in sorted(members):
                filename = f"{member_name}.rst"
                filepath = category_dir / filename
                
                # generate appropriate content
                if member["type"] == "class":
                    content = generate_class_rst(member, module_name, member_name)
                elif member["type"] == "function":
                    content = generate_function_rst(member, module_name, member_name) 
                else:  # Variable
                    content = generate_variable_rst(member, module_name, member_name)
                
                # write member file
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                
                # add to category section in main index
                category_section.append(f"* :doc:`{category_name}/{member_name}`\n")
                
                # add to category index
                category_index_content.append(f"   {member_name}\n")
            
            # write category index
            with open(category_dir / "index.rst", "w", encoding="utf-8") as f:
                f.write("".join(category_index_content))
            
            category_section.append("\n")
            index_content.extend(category_section)
            all_sections.append(f"{category_name}/index")
    
    # add final toctree with all sections to make them available in navigation
    if all_sections:
        index_content.append(".. toctree::\n")
        index_content.append("   :maxdepth: 3\n")
        index_content.append("   :hidden:\n\n")
        
        for section in sorted(all_sections):
            index_content.append(f"   {section}\n")
    
    # write the module index file
    with open(output_dir / "index.rst", "w", encoding="utf-8") as f:
        f.write("".join(index_content))

def generate_class_rst(member: Dict[str, Any], module_name: str, class_name: str) -> str:
    """Generate reST content for a class from the module_info member."""
    content = []
    title = class_name
    underline = "=" * len(title)
    content.append(f"{title}\n{underline}\n\n")
    
    content.append(f".. currentmodule:: {module_name}\n\n")
    content.append(f".. autoclass:: {class_name}\n")
    content.append("   :members:\n")
    content.append("   :undoc-members:\n")
    content.append("   :show-inheritance:\n")
    content.append("   :special-members: __init__\n\n")
    
    if member.get("doc"):
        clean_doc = clean_docstring(member["doc"])
        content.append(f"{clean_doc}\n\n")
    
    # base classes
    if "bases" in member and member["bases"]:
        bases = ", ".join(member["bases"])
        content.append(f"**Bases:** {bases}\n\n")
    
    # methods overview
    if "methods" in member and member["methods"]:
        content.append("**Methods:**\n\n")
        for method_name, method_info in sorted(member["methods"].items()):
            if method_info.get("doc"):
                method_doc = clean_docstring(method_info["doc"])
                if method_doc:
                    first_line = method_doc.split(".")[0]
                    content.append(f"* **{method_name}** - {first_line}.\n")
            else:
                content.append(f"* **{method_name}**\n")
        content.append("\n")
    
    return "".join(content)

def generate_function_rst(member: Dict[str, Any], module_name: str, function_name: str) -> str:
    """Generate reST content for a function from the module_info member."""
    content = []
    title = function_name
    underline = "=" * len(title)
    content.append(f"{title}\n{underline}\n\n")
    
    content.append(f".. currentmodule:: {module_name}\n\n")
    content.append(f".. autofunction:: {function_name}\n\n")
    
    if member.get("doc"):
        clean_doc = clean_docstring(member["doc"])
        content.append(f"{clean_doc}\n\n")
    
    # add parameters if available
    if "signature" in member:
        signature = extract_signature(member["signature"])
        if signature:
            content.append("**Parameters**\n\n")
            for param, type_hint in signature.items():
                if type_hint:
                    content.append(f"* **{param}**: ``{type_hint}``\n")
                else:
                    content.append(f"* **{param}**\n")
            content.append("\n")
    
    return "".join(content)

def generate_variable_rst(member: Dict[str, Any], module_name: str, variable_name: str) -> str:
    """Generate reST content for a variable from the module_info member."""
    content = []
    title = variable_name
    underline = "=" * len(title)
    content.append(f"{title}\n{underline}\n\n")
    
    content.append(f".. currentmodule:: {module_name}\n\n")
    content.append(f".. autodata:: {variable_name}\n\n")
    
    if member.get("doc"):
        clean_doc = clean_docstring(member["doc"])
        content.append(f"{clean_doc}\n\n")
    
    return "".join(content)

def create_placeholder_module_doc(
    module_name: str,
    output_dir: Path,
    root_output: Path,
    current_variant: str,
    variants: List[str],
) -> None:
    """Create a placeholder documentation for modules that can't be imported."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    module_index_path = output_dir / "index.rst"
    short_name = module_name.split('.')[-1]
    
    with open(module_index_path, "w", encoding="utf-8") as f:
        title = short_name
        underline = "=" * len(title)
        f.write(f"{title}\n{underline}\n\n")
        f.write(".. warning::\n")
        f.write("   This module could not be automatically documented because it couldn't be imported.\n")
        f.write("   This may be due to missing dependencies or an import error within the module.\n\n")
        f.write(f".. py:module:: {module_name}\n\n")
        f.write(f".. automodule:: {module_name}\n")
        f.write("   :noindex:\n\n")

def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup the Sphinx extension."""
    app.add_config_value("pdoc_modules", [], "env", [list, tuple])
    app.add_config_value("pdoc_output_dir", "api-reference", "env", str)

    app.connect("config-inited", validate_config)
    app.connect("builder-inited", generate_pdoc_docs)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }