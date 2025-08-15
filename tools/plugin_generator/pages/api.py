from metadata import Metadata
import os
import subprocess


def generate(metadata: Metadata, plugin_source: str, output: str) -> None:
    install_package(plugin_source)
    run_makefile(
        title=metadata["title"] if "title" in metadata else plugin_source,
        name=metadata["name"] if "name" in metadata else plugin_source,
        pkg=metadata["packages"][0] if "packages" in metadata else plugin_source,
        plugin_source=plugin_source,
        output=output
    )

def run_makefile(title: str, pkg: str, name: str, plugin_source: str, output: str):
    try:
        env = os.environ.copy()
        env.update({
            "TITLE": title,
            "PLUGIN": pkg,
            "PLUGIN_NAME": name,
            "OUTPUT": output,
            "PLUGIN_SOURCE": plugin_source
        })
        
        subprocess.run(["make", "-f", "Makefile.api.plugins", "parser", "generate"], env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running make: {e}")


def install_package(plugin_source: str):
    original_dir = os.getcwd() # Save the current directory
    try:
        os.chdir(plugin_source)
        subprocess.run(["uv", "pip", "install", "-e", "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing package: {e}")
    finally:
        os.chdir(original_dir) # Return to original directory
