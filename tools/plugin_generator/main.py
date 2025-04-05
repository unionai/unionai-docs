import argparse
from os import mkdir, path, listdir

import metadata
import pages.landing as landing
import pages.index as index
import pages.api as api

def main():
    parser = argparse.ArgumentParser(
        description="Generate Plugin metadata from Python package"
    )
    parser.add_argument("--flytekit_root", help="Root for FlyteKit", required=True)
    parser.add_argument("--variants", nargs="+", help="List of variants to use")
    parser.add_argument("--output", help="Output directory", required=True)
    parser.add_argument("--generate_only", help="Generate only this plugin", default=False)
    args = parser.parse_args()
    
    if not path.exists(args.output):
        mkdir(args.output)

    # List all directories that are inside plugins/ and starts with flytekit-
    plugins_dir = path.join(args.flytekit_root, "plugins")
    
    plugin_dirs = []
    for d in listdir(plugins_dir):
        if path.isdir(path.join(plugins_dir, d)) and d.startswith("flytekit-"):
            plugin_dirs.append(d)

    plugin_dirs.sort()

    generated_plugins = {}

    for plugin_dir in plugin_dirs:
        print("-----------------")
        print(f"Plugin: {plugin_dir}")

        simple_folder_name = plugin_dir.replace("flytekit-", "")
        if args.generate_only:
            if simple_folder_name != args.generate_only:
                continue

        try:
            plugin_path = path.join(plugins_dir, plugin_dir)
            md = metadata.load(plugin_path)
            

            if "title" in md:
                title = md["title"]
            else:
                title = simple_folder_name
            title_expanded = title
            if "title_expanded" in md:
                title_expanded = md["title_expanded"]

            api.generate(
                metadata=md,
                plugin_source=plugin_path,
                output=path.join(args.output, simple_folder_name),
            )

            landing.generate(
                name=title,
                title_expanded=title_expanded,
                metadata=md,
                plugin_source=plugin_path,
                output=path.join(args.output, simple_folder_name),
                variants=args.variants,
            )

            generated_plugins[simple_folder_name] = md
        except Exception as e:
            print(f"Failed to load plugin: {e}")
            continue

    if not args.generate_only:
        index.generate(output=args.output, generated_plugins=generated_plugins, variants=args.variants)

if __name__ == "__main__":
    main()