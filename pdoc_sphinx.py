from pathlib import Path
import pdoc
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from docutils import nodes
import importlib
import inspect
from typing import Any

logger = logging.getLogger(__name__)

def convert_module_to_rst(module_obj: Any) -> str:
    """Convert a pdoc Module object to RST format."""
    lines = []
    
    # get all members
    for name, member in inspect.getmembers(module_obj):
        # skip private members and modules
        if name.startswith('_'):
            continue
            
        if inspect.isclass(member):
            lines.extend(convert_class_to_rst(member))
        elif inspect.isfunction(member):
            lines.extend(convert_function_to_rst(member))
            
    return '\n'.join(lines)

def convert_class_to_rst(cls: type) -> list:
    """Convert a class to RST format."""
    lines = []
    
    # Class definition
    bases = [b.__name__ for b in cls.__bases__ if b != object]
    if bases:
        lines.append(f".. py:class:: {cls.__name__}({', '.join(bases)})")
    else:
        lines.append(f".. py:class:: {cls.__name__}")
        
    # Class docstring
    if cls.__doc__:
        lines.append("")
        lines.append(f"   {cls.__doc__.strip()}")
        
    lines.append("")
    
    # Get all members
    for name, member in inspect.getmembers(cls):
        # Skip private members
        if name.startswith('_') and not name == '__init__':
            continue
            
        if inspect.isfunction(member) or inspect.ismethod(member):
            lines.extend(["   " + line for line in convert_method_to_rst(member)])
        elif isinstance(member, property):
            lines.extend(["   " + line for line in convert_property_to_rst(name, member)])
            
    return lines

def convert_method_to_rst(method) -> list:
    """Convert a method to RST format."""
    lines = []
    
    # Get signature
    try:
        sig = inspect.signature(method)
        sig_str = str(sig).replace('(self, ', '(').replace('(self)', '()')
        lines.append(f".. py:method:: {method.__name__}{sig_str}")
    except ValueError:
        lines.append(f".. py:method:: {method.__name__}")
    
    # Method docstring
    if method.__doc__:
        lines.append("")
        lines.append(f"   {method.__doc__.strip()}")
        
    lines.append("")
    return lines

def convert_property_to_rst(name: str, prop: property) -> list:
    """Convert a property to RST format."""
    lines = []
    
    lines.append(f".. py:attribute:: {name}")
    
    if prop.__doc__:
        lines.append("")
        lines.append(f"   {prop.__doc__.strip()}")
        
    lines.append("")
    return lines

def convert_function_to_rst(func) -> list:
    """Convert a function to RST format."""
    lines = []
    
    # get signature
    try:
        sig = inspect.signature(func)
        lines.append(f".. py:function:: {func.__name__}{sig}")
    except ValueError:
        lines.append(f".. py:function:: {func.__name__}")
    
    # fn docstring
    if func.__doc__:
        lines.append("")
        lines.append(f"   {func.__doc__.strip()}")
        
    lines.append("")
    return lines


# Extracted from the pdoc-sphinx extension. 
# TODO: Clean this up and remove it
class PDocAutoDirective(SphinxDirective):
    """
    A directive that uses pdoc to generate RST documentation.
    Usage: .. pdoc-auto:: module_name
    """
    required_arguments = 1
    has_content = False

    def run(self):
        module_name = self.arguments[0]
        
        try:
            # import module
            module = importlib.import_module(module_name)
            
            # Generate RST content
            rst_content = convert_module_to_rst(module)
            
            # create a node with the RST content
            node = nodes.literal_block(rst_content, rst_content)
            
            return [node]
            
        except Exception as e:
            logger.error(f"Error processing module {module_name}: {e}")
            error_node = nodes.error()
            error_node += nodes.paragraph(text=str(e))
            return [error_node]

def setup(app):
    """
    Setup the extension
    """
    app.add_directive('pdoc-auto', PDocAutoDirective)
    
    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }