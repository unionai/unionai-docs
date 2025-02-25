"""
sphinx ext to autogen API docs
"""

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging
from pathlib import Path
import os
from typing import Dict, Any, List

from pdoc.doc import Module

logger = logging.getLogger(__name__)


def validate_config(app: Sphinx, config: Config) -> None:
    """Validate the extension configuration."""
    if not hasattr(config, "pdoc_modules"):
        logger.warning("No modules specified in pdoc_modules configuration")
        config.pdoc_modules = []

    if not isinstance(config.pdoc_modules, (list, tuple)):
        raise ValueError("pdoc_modules must be a list or tuple of module names")


def generate_pdoc_docs(app: Sphinx) -> None:
    """Generate API documentation with structured folders, sidebar navigation, and dynamically determined variant metadata."""

    # def available variants
    variants = ["serverless", "byoc"]

    output_base = Path(app.confdir) / app.config.pdoc_output_dir
    output_base.mkdir(parents=True, exist_ok=True)

    # determine the variant dynamically from the folder structure
    current_variant = determine_variant(output_base, variants)

    # inject the variant directives
    api_index = [
        f"---\n"
        f"variant-display-names: {{'serverless': 'Serverless', 'byoc': 'BYOC'}}\n"
        f"available-variants: {variants}\n"
        f"current-variant: {current_variant}\n"
        f"---\n\n",
        "# Union SDK\n\n",
        "```{toctree}\n:maxdepth: 2\n\n",
    ]

    for module_name in app.config.pdoc_modules:
        try:
            logger.info(f"Generating documentation for module: {module_name}")

            module_root_dir = output_base / module_name
            module_root_dir.mkdir(parents=True, exist_ok=True)

            if process_module_recursive(
                module_name,
                module_root_dir,
                api_index,
                output_base,
                current_variant,
                variants,
            ):
                logger.info(f"Successfully processed {module_name}")

        except Exception as e:
            logger.error(f"Error processing module {module_name}: {str(e)}")

    api_index.append("```\n")
    with open(output_base / "index.md", "w") as f:
        f.writelines(api_index)


def determine_variant(output_base: Path, variants: List[str]) -> str:
    """
    Determine the current variant dynamically based on the directory structure.

    Args:
        output_base (Path): The base directory for the documentation output.
        variants (List[str]): The list of available variants.

    Returns:
        str: The dynamically determined current variant.
    """
    # Check if any known variant is present in the path
    for variant in variants:
        if f"/{variant}/" in str(output_base) or output_base.name == variant:
            return variant

    logger.warning(
        "Could not determine variant from directory structure, defaulting to 'serverless'."
    )
    return "serverless"  # Default if no match is found


def process_module_recursive(
    module_name: str,
    output_dir: Path,
    api_index: List[str],
    root_output: Path,
    current_variant: str,
    variants: List[str],
) -> bool:
    """Recursively process a module and its submodules, placing them into structured folders."""
    try:
        module = Module.from_name(module_name)

        # det where this module's documentation should be stored
        module_dir = root_output / module_name.replace(".", "/")
        module_dir.mkdir(parents=True, exist_ok=True)

        module_index_path = module_dir / "index.md"

        sidebar_entries = ["```{toctree}\n:maxdepth: 2\n\n"]

        with open(module_index_path, "w") as f:
            f.write(
                f"---\n"
                f"variant-display-names: {{'serverless': 'Serverless', 'byoc': 'BYOC'}}\n"
                f"available-variants: {variants}\n"
                f"current-variant: {current_variant}\n"
                f"---\n\n"
            )
            f.write(f"# {module_name}\n\n")
            f.write("```{eval-rst}\n")
            f.write(f".. currentmodule:: {module_name}\n\n")
            f.write(f".. automodule:: {module_name}\n")
            f.write("    :members:\n    :undoc-members:\n    :show-inheritance:\n")
            f.write("    :special-members: __init__\n")
            f.write("```\n\n")

        # document each class separately in its own file
        for cls in module.classes:
            class_dir = module_dir / cls.qualname
            class_dir.mkdir(parents=True, exist_ok=True)
            class_index_path = class_dir / "index.md"

            with open(class_index_path, "w") as f:
                f.write(
                    f"---\n"
                    f"variant-display-names: {{'serverless': 'Serverless', 'byoc': 'BYOC'}}\n"
                    f"available-variants: {variants}\n"
                    f"current-variant: {current_variant}\n"
                    f"---\n\n"
                )
                f.write(f"# {cls.qualname}\n\n")
                f.write("```{eval-rst}\n")
                f.write(f".. currentmodule:: {module_name}\n\n")
                f.write(f".. autoclass:: {cls.qualname}\n")
                f.write("    :members:\n    :undoc-members:\n    :show-inheritance:\n")
                f.write("    :special-members: __init__\n")
                f.write("```\n\n")

            sidebar_entries.append(f"{cls.qualname.replace('.', '/')}/index\n")

        # process submodules recursively and add them to the sidebar
        if module.submodules:
            for submodule in module.submodules:
                submodule_dir = root_output / submodule.qualname.replace(".", "/")
                submodule_dir.mkdir(parents=True, exist_ok=True)
                if process_module_recursive(
                    submodule.qualname,
                    submodule_dir,
                    sidebar_entries,
                    root_output,
                    current_variant,
                    variants,
                ):
                    sidebar_entries.append(
                        f"{submodule.qualname.replace('.', '/')}/index\n"
                    )

        sidebar_entries.append("```\n")

        # write the sidebar structure for the module
        with open(module_index_path, "a") as f:
            f.writelines(sidebar_entries)

        relative_path = module_dir.relative_to(root_output)
        api_index.append(f"{relative_path}/index\n")

        return True

    except Exception as e:
        logger.error(f"Error processing module {module_name}: {str(e)}")
        return False


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
