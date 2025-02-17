"""
sphinx ext to automatically gen docs from Python modules using `pdoc`
"""

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging
from pathlib import Path
import os
from typing import Dict, Any, List

from pdoc.doc import Module
from gen import (
    build_rst_tree,
    create_directory,
    generate_rst_section,
    format_docstring,
    generate_class_rst,
    generate_function_rst,
    generate_variable_rst
)

logger = logging.getLogger(__name__)

def validate_config(app: Sphinx, config: Config) -> None:
    """Validate the extension configuration
    
    Args:
        app: Sphinx application instance
        config: Sphinx configuration object
    """
    if not hasattr(config, 'pdoc_modules'):
        logger.warning('No modules specified in pdoc_modules configuration')
        config.pdoc_modules = []
    
    if not isinstance(config.pdoc_modules, (list, tuple)):
        raise ValueError('pdoc_modules must be a list or tuple of module names')

def generate_pdoc_docs(app: Sphinx) -> None:
    """Generate RST documentation for configured modules
    
    Args:
        app: Sphinx application instance
    """
    # get output dir (relative to conf.py location)
    output_base = Path(app.confdir) / app.config.pdoc_output_dir
    
    # create output dir if it doesn't exist
    output_base.mkdir(parents=True, exist_ok=True)
    
    # process each configured module
    for module_name in app.config.pdoc_modules:
        try:
            logger.info(f'Generating documentation for module: {module_name}')
            
            # create module documentation
            module_dir = output_base / module_name
            if process_module(module_name, str(module_dir)):
                logger.info(f'Successfully processed {module_name}')
                
                # add to Sphinx's known documents
                doc_name = str(module_dir.relative_to(app.srcdir) / 'index')
                app.env.found_docs.add(doc_name)
            
        except Exception as e:
            logger.error(f'Error processing module {module_name}: {str(e)}')

def process_module(module_name: str, output_dir: str) -> bool:
    """Process a single module and create its documentation
    
    Args:
        module_name: Name of the module to process
        output_dir: Directory where documentation should be written
        
    Returns:
        bool: True if processing was successful, False otherwise
    """
    try:
        module = Module.from_name(module_name)
        build_rst_tree(module, output_dir)
        return True
    except Exception as e:
        logger.error(f"Error processing module {module_name}: {str(e)}")
        return False

def setup(app: Sphinx) -> Dict[str, Any]:
    """
    Setup the Sphinx extension
    
    Args:
        app: Sphinx application instance
        
    Returns:
        Dict containing extension metadata
    """
    # add extension configuration values
    app.add_config_value('pdoc_modules', [], 'env', [list, tuple])
    app.add_config_value('pdoc_output_dir', 'api-reference', 'env', str)
    
    # Connect extension functions to Sphinx events
    app.connect('config-inited', validate_config)
    app.connect('builder-inited', generate_pdoc_docs)
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }