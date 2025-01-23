import importlib
import pdoc
from pathlib import Path
from docutils import nodes
from pdoc_sphinx import convert_module_to_rst 

def generate_rst_doc(module_name: str, output_dir: Path) -> None:
    """
    Generate RST documentation for a module.
    
    Args:
        module_name: Name of the module to document
        output_dir: Directory where RST files should be saved
    """
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # import the module
    module = importlib.import_module(module_name)

    print(f"Generating documentation for module: {module_name}")
    # print("Module: ", module)
    print(type(module))

    doc = pdoc.doc.Module(module)
    mod = pdoc.doc.Module(pdoc.extract.load_module(module_name))
    print("Mod: ", mod)
    print("Doc: ", doc)

    node = nodes.literal_block()
    node += nodes.Text(doc)

    # print("Node: ", node)

    txt = node.astext()

    # print("Text: ", txt)
    
    # convert to RST
    rst_content = convert_module_to_rst(module)
    
    # create output filename
    output_file = output_dir / f"{module_name.replace('.', '_')}.md"
    
    # add a header with the module name
    full_content = f"""
{module_name}
{'=' * len(module_name)}

.. module:: {module_name}

{rst_content}
"""
    
    # Write to file
    output_file.write_text(full_content)
    print(f"Generated documentation at: {output_file}")

if __name__ == "__main__":
    
    module_names = ["union", "flytekit"]
    output_dir = Path("docs/api")

    [generate_rst_doc(module_name, output_dir) for module_name in module_names]