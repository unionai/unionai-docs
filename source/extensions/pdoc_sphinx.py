from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging
from pathlib import Path
import os
import inspect
import re
import sys
import importlib
import traceback
from typing import Dict, Any, List, Optional, Set

from pdoc.doc import Module, Class, Function, Variable

logger = logging.getLogger(__name__)

def import_module_progressively(module_name: str, parent_module=None):
    """Import a module progressively by importing its parents first."""
    try:
        # First try direct import
        return importlib.import_module(module_name)
    except ImportError:
        # If direct import fails and we have a parent module
        if parent_module:
            try:
                # Try to access it as an attribute of the parent
                parts = module_name.split('.')
                local_name = parts[-1]
                if hasattr(parent_module, local_name):
                    return getattr(parent_module, local_name)
            except (ImportError, AttributeError):
                pass
                
        # Try progressive importing
        parts = module_name.split('.')
        for i in range(1, len(parts)):
            try:
                # Import parent modules one level at a time
                importlib.import_module('.'.join(parts[:i]))
            except ImportError:
                pass
                
        # Try again after importing parents
        try:
            return importlib.import_module(module_name)
        except ImportError as e:
            logger.warning(f"Progressive import failed for {module_name}: {str(e)}")
            return None

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

def format_docstring(docstring):
    """Format docstring for reST"""
    if not docstring:
        return ""
    formatted = docstring.replace('\n', '\n   ')
    return f"   {formatted}\n\n"

def clean_docstring(docstring: str) -> str:
    """
    Cleans docstring for Sphinx compatibility:
    1. Markdown-style code fences (```python ... ```) become reST code blocks.
    2. Lines like 'param foo:' become ':param foo:' so Sphinx autodoc picks them up.
    3. Lines like 'returns:' or 'return:' become ':returns:'.
    """
    if not docstring:
        return ""

    # 1) Convert markdown code fences -> reST code blocks
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

    # 2) Convert lines like 'param foo:' -> ':param foo:'
    #    We look for the beginning of a line (possibly with some spaces) then "param <name>:"
    docstring = re.sub(
        r"(?m)^\s*param\s+([\w_]+):",
        r":param \1:",
        docstring
    )

    # Also handle "type foo:" -> ":type foo:"
    docstring = re.sub(
        r"(?m)^\s*type\s+([\w_]+):",
        r":type \1:",
        docstring
    )

    # 3) Convert "returns:" / "return:" -> ":returns:"
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
        
    # Attempt to preload the specified modules to identify potential issues early
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

    # Determine the variant dynamically from the folder structure
    current_variant = determine_variant(output_base, variants)
    
    # Create the main index file (index.rst) for the doc set
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
    
    # Process each module
    for module_name in app.config.pdoc_modules:
        try:
            logger.info(f"Generating documentation for module: {module_name}")

            module_root_dir = output_base / module_name
            module_root_dir.mkdir(parents=True, exist_ok=True)

            # Track processed modules to avoid duplicates
            processed_modules = set()
            
            # Process the module documentation
            build_rst_tree(
                module_name,
                module_root_dir,
                output_base,
                current_variant,
                variants,
                processed_modules
            )
            
            logger.info(f"Successfully processed {module_name}")

        except Exception as e:
            logger.error(f"Error processing module {module_name}: {str(e)}")
            logger.error(traceback.format_exc())
            
            # Create a placeholder for the failed module
            create_placeholder_module_doc(
                module_name,
                output_base / module_name,
                output_base,
                current_variant,
                variants
            )

def determine_variant(output_base: Path, variants: List[str]) -> str:
    """Determine the current variant dynamically based on the directory structure."""
    for variant in variants:
        if f"/{variant}/" in str(output_base) or output_base.name == variant:
            return variant
    return "serverless"  # Default if no match is found

def generate_class_rst(cls, module_name: str, current_variant: str, variants: List[str]) -> str:
    """Generate reST content for a class."""
    content = []
    title = cls.name
    underline = "=" * len(title)
    content.append(f"{title}\n{underline}\n\n")
    
    content.append(f".. currentmodule:: {module_name}\n\n")
    content.append(f".. autoclass:: {cls.qualname}\n")
    content.append("   :members:\n")
    content.append("   :undoc-members:\n")
    content.append("   :show-inheritance:\n")
    content.append("   :special-members: __init__\n\n")
    
    if cls.docstring:
        clean_doc = clean_docstring(cls.docstring)
        content.append(f"{clean_doc}\n\n")
    
    # Base classes
    if cls.bases:
        bases = ", ".join(str(base) for base in cls.bases)
        content.append(f"**Bases:** {bases}\n\n")
    
    # Methods overview
    if cls.methods:
        content.append("**Methods:**\n\n")
        for method in sorted(cls.methods, key=lambda m: m.name):
            if method.name.startswith('_') and method.name != '__init__':
                continue
                
            method_str = str(method)
            signature = extract_signature(method_str)
            if hasattr(method, 'docstring') and method.docstring:
                method_doc = clean_docstring(method.docstring)
                if method_doc:
                    content.append(f"* **{method.name}** - {method_doc.split('.')[0]}.\n")
            else:
                content.append(f"* **{method.name}**\n")
        content.append("\n")
    
    # Source code
    source = get_source_code(cls)
    if source:
        content.append("Source Code\n-----------\n\n")
        content.append(".. code-block:: python\n\n")
        for line in source.splitlines():
            content.append(f"    {line}\n")
        content.append("\n")
    
    return "".join(content)

def generate_function_rst(func, module_name: str, current_variant: str, variants: List[str]) -> str:
    """Generate reST content for a function."""
    content = []
    title = func.name
    underline = "=" * len(title)
    content.append(f"{title}\n{underline}\n\n")
    
    content.append(f".. currentmodule:: {module_name}\n\n")
    content.append(f".. autofunction:: {func.qualname}\n\n")
    
    if func.docstring:
        clean_doc = clean_docstring(func.docstring)
        content.append(f"{clean_doc}\n\n")
    
    # Add parameters
    signature = extract_signature(str(func))
    if signature:
        content.append("**Parameters**\n\n")
        for param, type_hint in signature.items():
            if type_hint:
                content.append(f"* **{param}**: ``{type_hint}``\n")
            else:
                content.append(f"* **{param}**\n")
        content.append("\n")
    
    # Source code
    source = get_source_code(func)
    if source:
        content.append("Source Code\n-----------\n\n")
        content.append(".. code-block:: python\n\n")
        for line in source.splitlines():
            content.append(f"    {line}\n")
        content.append("\n")
    
    return "".join(content)

def generate_variable_rst(var, module_name: str, current_variant: str, variants: List[str]) -> str:
    """Generate reST content for a variable."""
    content = []
    title = var.name
    underline = "=" * len(title)
    content.append(f"{title}\n{underline}\n\n")
    
    content.append(f".. currentmodule:: {module_name}\n\n")
    content.append(f".. autodata:: {var.qualname}\n\n")
    
    if var.docstring:
        clean_doc = clean_docstring(var.docstring)
        content.append(f"{clean_doc}\n\n")
    
    if hasattr(var, 'type') and var.type:
        content.append(f"**Type:** ``{var.type}``\n\n")
    
    return "".join(content)

def is_significant_variable(var: Variable) -> bool:
    """Determine if a variable is significant enough to document."""
    try:
        if var.name.startswith('_'):
            return False
        
        if var.name in ('__all__', '__version__'):
            return True
            
        if var.docstring:
            return True
            
        value_str = str(var.obj)
        if value_str.startswith('<module ') or value_str.startswith('<function '):
            return False
            
        return True
    except Exception:
        return False

def build_rst_tree(
    module_name: str,
    output_dir: Path,
    root_output: Path,
    current_variant: str,
    variants: List[str],
    processed_modules: Set[str] = None,
    parent_module = None
) -> bool:
    """Build reST documentation tree following module structure."""
    if processed_modules is None:
        processed_modules = set()
        
    # Skip if already processed
    if module_name in processed_modules:
        return True
        
    processed_modules.add(module_name)
    
    try:
        # Try progressive importing first
        module_obj = import_module_progressively(module_name, parent_module)
        
        try:
            module = Module.from_name(module_name)
            logger.info(f"Successfully loaded module: {module_name}")
        except (ImportError, RuntimeError) as e:
            logger.warning(f"Could not import module {module_name}: {str(e)}")
            create_placeholder_module_doc(
                module_name, 
                output_dir, 
                root_output, 
                current_variant, 
                variants
            )
            return True
        
        # Create module directory
        module_dir = output_dir
        module_dir.mkdir(parents=True, exist_ok=True)
        
        # Start building the index content
        index_content = []
        
        # Add title and module docstring
        title = module.name.split('.')[-1]
        underline = "=" * len(title)
        index_content.append(f"{title}\n{underline}\n\n")
        
        if module.docstring:
            clean_doc = clean_docstring(module.docstring)
            index_content.append(f"{clean_doc}\n\n")
        
        index_content.append(f".. module:: {module.name}\n\n")
        index_content.append(f".. automodule:: {module.name}\n")
        index_content.append("   :noindex:\n\n")
        
        # Track all sections for the toctree
        all_sections = []
        
        # Process submodules first
        if hasattr(module, "submodules") and module.submodules:
            submodules_section = []
            submodules_section.append("Submodules\n----------\n\n")
            
            # Store the actual module object for use with submodules
            try:
                actual_module_obj = importlib.import_module(module.name)
            except ImportError:
                actual_module_obj = module_obj
            
            # Write each submodule
            for submodule in sorted(module.submodules, key=lambda m: m.name):
                submodule_name = submodule.name.split('.')[-1]
                submodule_dir = output_dir / submodule_name
                
                if submodule.name in processed_modules:
                    logger.warning(f"Skipping already processed submodule: {submodule.name}")
                    continue
                    
                try:
                    build_rst_tree(
                        submodule.name,
                        submodule_dir,
                        root_output,
                        current_variant,
                        variants,
                        processed_modules,
                        actual_module_obj
                    )
                    all_sections.append(f"{submodule_name}/index")
                    submodules_section.append(f"* :doc:`{submodule_name}/index`\n")
                except Exception as e:
                    logger.error(f"Error processing submodule {submodule.name}: {str(e)}")
                    logger.error(traceback.format_exc())
            
            if len(submodules_section) > 1:  # Only add if we have submodules
                submodules_section.append("\n")
                index_content.extend(submodules_section)
        
        # Process members by category
        for category_name, category_title, member_filter in [
            ("classes", "Classes", lambda m: isinstance(m, Class)),
            ("functions", "Functions", lambda m: isinstance(m, Function)),
            ("variables", "Variables", lambda m: isinstance(m, Variable) and is_significant_variable(m))
        ]:
            members = [(name, member) for name, member in module.members.items() 
                      if member_filter(member) and not (name.startswith('_') and name != '__init__')]
            
            if members:
                # Create category section
                category_section = []
                category_section.append(f"{category_title}\n{'-' * len(category_title)}\n\n")
                
                category_dir = output_dir / category_name
                category_dir.mkdir(exist_ok=True)
                
                # Create category index
                category_index_content = []
                category_index_content.append(f"{module.name} {category_title}\n")
                category_index_content.append("=" * len(f"{module.name} {category_title}") + "\n\n")
                category_index_content.append(".. toctree::\n")
                category_index_content.append("   :maxdepth: 1\n\n")
                
                # Process each member
                for member_name, member in sorted(members):
                    filename = f"{member_name}.rst"
                    filepath = category_dir / filename
                    
                    # Generate appropriate content
                    if isinstance(member, Class):
                        content = generate_class_rst(member, module.name, current_variant, variants)
                    elif isinstance(member, Function):
                        content = generate_function_rst(member, module.name, current_variant, variants)
                    else:  # Variable
                        content = generate_variable_rst(member, module.name, current_variant, variants)
                    
                    # Write member file
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    
                    # Add to category section in main index
                    category_section.append(f"* :doc:`{category_name}/{member_name}`\n")
                    
                    # Add to category index
                    category_index_content.append(f"   {member_name}\n")
                
                # Write category index
                with open(category_dir / "index.rst", "w", encoding="utf-8") as f:
                    f.write("".join(category_index_content))
                
                category_section.append("\n")
                index_content.extend(category_section)
                all_sections.append(f"{category_name}/index")
        
        # Add final toctree with all sections to make them available in navigation
        index_content.append(".. toctree::\n")
        index_content.append("   :maxdepth: 3\n")
        index_content.append("   :hidden:\n\n")
        
        for section in sorted(all_sections):
            index_content.append(f"   {section}\n")
        
        # Write the module index file
        with open(module_dir / "index.rst", "w", encoding="utf-8") as f:
            f.write("".join(index_content))
        
        return True
        
    except Exception as e:
        logger.error(f"Error processing module {module_name}: {str(e)}")
        logger.error(traceback.format_exc())
        return False

def create_placeholder_module_doc(
    module_name: str,
    output_dir: Path,
    root_output: Path,
    current_variant: str,
    variants: List[str],
) -> None:
    """Create a placeholder documentation for modules that can't be imported."""
    module_dir = output_dir
    module_dir.mkdir(parents=True, exist_ok=True)
    
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