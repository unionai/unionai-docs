from pdoc.doc import Class, Function, Variable, Module
from datetime import datetime
from pathlib import Path
import inspect
import os

def create_directory(path):
    """Create directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)

def get_source_code(obj):
    """Extract source code if available"""
    try:
        return inspect.getsource(obj.obj)
    except (TypeError, AttributeError, OSError):
        return None

def generate_rst_section(title, content, level=1):
    """Generate a reST section with proper underline"""
    underline_chars = ['=', '-', '~', '^', '"']
    underline_char = underline_chars[min(level - 1, len(underline_chars) - 1)]
    underline = underline_char * len(title)
    return f"{title}\n{underline}\n\n{content}\n\n"

# def format_docstring(docstring):
#     """Format docstring for reST"""
#     if not docstring:
#         return ""
#     return f"   {docstring.replace('\n', '\n   ')}\n\n"

def format_docstring(docstring):
    """Format docstring for reST"""
    if not docstring:
        return ""
    formatted = docstring.replace('\n', '\n   ')
    return f"   {formatted}\n\n"

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
            if ':' in p:
                name, type_hint = p.split(':', 1)
                param_dict[name.strip()] = type_hint.strip()
            else:
                param_dict[p] = None
                
        return param_dict
    except:
        return {}

def generate_class_rst(cls):
    """Generate reST content for a class"""
    content = [f".. py:class:: {cls.qualname}"]
    
    if cls.docstring:
        content.append(format_docstring(cls.docstring))
    
    # Base classes
    if cls.bases:
        content.append("   **Bases:** " + ", ".join(str(base) for base in cls.bases) + "\n")
    
    # methods
    if cls.methods:
        content.append("   **Methods:**\n")
        for method in cls.methods:
            method_str = str(method)
            signature = extract_signature(method_str)
            content.append(f"   .. py:method:: {method}")
            if hasattr(method, 'docstring') and method.docstring:
                content.append(format_docstring(method.docstring))
            if signature:
                content.append("      **Parameters:**\n")
                for param, type_hint in signature.items():
                    if type_hint:
                        content.append(f"      * {param}: {type_hint}\n")
                    else:
                        content.append(f"      * {param}\n")
                content.append("\n")
    
    # class variables
    if cls.class_variables:
        content.append("   **Class Variables:**\n")
        for var in cls.class_variables:
            content.append(f"   .. py:attribute:: {var}")
            if hasattr(var, 'docstring') and var.docstring:
                content.append(format_docstring(var.docstring))
    
    # instance variables
    if cls.instance_variables:
        content.append("   **Instance Variables:**\n")
        for var in cls.instance_variables:
            content.append(f"   .. py:attribute:: {var}")
            if hasattr(var, 'docstring') and var.docstring:
                content.append(format_docstring(var.docstring))
    
    # source code
    source = get_source_code(cls)
    if source:
        content.append("   **Source:**\n\n   .. code-block:: python\n")
        content.append(f"      {source.replace('\n', '\n      ')}\n")
    
    return "\n".join(content)

def generate_function_rst(func):
    """Generate reST content for a function"""
    content = [f".. py:function:: {func.qualname}"]
    
    if func.docstring:
        content.append(format_docstring(func.docstring))
    
    # add parameters
    signature = extract_signature(str(func))
    if signature:
        content.append("   **Parameters:**\n")
        for param, type_hint in signature.items():
            if type_hint:
                content.append(f"   * {param}: {type_hint}\n")
            else:
                content.append(f"   * {param}\n")
        content.append("\n")
    
    # source code
    source = get_source_code(func)
    if source:
        content.append("   **Source:**\n\n   .. code-block:: python\n")
        content.append(f"      {source.replace('\n', '\n      ')}\n")
    
    return "\n".join(content)

def generate_variable_rst(var):
    """Generate reST content for a variable"""
    content = [f".. py:attribute:: {var.qualname}"]
    
    if var.docstring:
        content.append(format_docstring(var.docstring))
    
    if hasattr(var, 'type') and var.type:
        content.append(f"   **Type:** {var.type}\n")
    
    return "\n".join(content)

def build_rst_tree(doc_obj, base_path, current_path=''):
    """Build reST documentation tree following module structure"""
    # Create directory for current module/submodule
    if current_path:
        full_path = os.path.join(base_path, current_path)
        create_directory(full_path)
    else:
        full_path = base_path
    
    # gen module documentation
    module_content = []
    
    # Module header
    module_name = doc_obj.name.split('.')[-1]
    module_content.append(generate_rst_section(module_name, doc_obj.docstring or ""))
    
    # Add module directive
    module_content.append(f".. py:module:: {doc_obj.name}\n")
    
    # Process members
    member_types = {
        'Classes': [],
        'Functions': [],
        'Variables': []
    }
    
    for member_name, member in doc_obj.members.items():
        member_path = os.path.join(current_path, member_name)
        
        if isinstance(member, Class):
            class_dir = os.path.join(full_path, 'classes')
            create_directory(class_dir)
            class_content = generate_class_rst(member)
            class_file = os.path.join(class_dir, f"{member_name}.rst")
            with open(class_file, 'w', encoding='utf-8') as f:
                f.write(class_content)
            member_types['Classes'].append(f"classes/{member_name}")
            
        elif isinstance(member, Function):
            func_dir = os.path.join(full_path, 'functions')
            create_directory(func_dir)
            function_content = generate_function_rst(member)
            function_file = os.path.join(func_dir, f"{member_name}.rst")
            with open(function_file, 'w', encoding='utf-8') as f:
                f.write(function_content)
            member_types['Functions'].append(f"functions/{member_name}")
            
        elif isinstance(member, Variable):
            var_dir = os.path.join(full_path, 'variables')
            create_directory(var_dir)
            variable_content = generate_variable_rst(member)
            variable_file = os.path.join(var_dir, f"{member_name}.rst")
            with open(variable_file, 'w', encoding='utf-8') as f:
                f.write(variable_content)
            member_types['Variables'].append(f"variables/{member_name}")
    
    # process submodules
    if hasattr(doc_obj, 'submodules'):
        submodule_paths = []
        for submodule in doc_obj.submodules:
            submodule_path = os.path.join(current_path, submodule.name.split('.')[-1])
            build_rst_tree(submodule, base_path, submodule_path)
            
            # Add submodule to list for toctree
            rel_path = os.path.relpath(
                os.path.join(base_path, submodule_path, 'index'),
                full_path
            )
            submodule_paths.append(rel_path)
        
        if submodule_paths:
            module_content.append("Submodules\n----------\n\n.. toctree::\n   :maxdepth: 2\n\n   ")
            module_content.append("\n   ".join(submodule_paths))
            module_content.append("\n\n")
    
    # add member entries to toctree
    for section, members in member_types.items():
        if members:
            module_content.append(f"{section}\n{'-' * len(section)}\n\n.. toctree::\n   :maxdepth: 1\n\n   ")
            module_content.append("\n   ".join(members))
            module_content.append("\n\n")
    
    # write module index file
    with open(os.path.join(full_path, 'index.rst'), 'w', encoding='utf-8') as f:
        f.write("\n".join(module_content))

def process_module(module_name, output_dir):
    """Process a single module and create its reST documentation"""
    print(f"Processing module: {module_name}")
    
    # create base directory for module
    module_dir = os.path.join(output_dir, module_name)
    create_directory(module_dir)
    
    try:
        module = Module.from_name(module_name)
        build_rst_tree(module, module_dir)
        return True
    except Exception as e:
        print(f"Error processing module {module_name}: {str(e)}")
        return False

if __name__ == '__main__':
    # list of modules to process
    modules = ['union', 'flytekit']
    
    # Create base output directory
    output_dir = 'sphinx_docs'
    create_directory(output_dir)
    
    # process each module
    for module_name in modules:
        if process_module(module_name, output_dir):
            print(f"Successfully processed {module_name}")
    
    print(f"\nDocumentation has been generated in the '{output_dir}' directory")