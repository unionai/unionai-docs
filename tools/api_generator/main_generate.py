import argparse

import yaml

from generate.site import generate_site


def main():
    parser = argparse.ArgumentParser(
        description="Generate API documentation site from YAML"
    )
    parser.add_argument("yaml_file", help="Path to the API reference YAML file")
    parser.add_argument("output_dir", help="Path to the output directory")
    parser.add_argument("--title", help="Name of the API")
    parser.add_argument("--variants", nargs="+", help="List of variants to use")
    parser.add_argument("--include", nargs="+", help="List of files to include")
    args = parser.parse_args()

    # Read out.yaml file, parse and convert to ptypes.ParsedInfo
    with open(args.yaml_file, "r") as f:
        parsed_info = yaml.safe_load(f)

        generate_site(
            title=args.title,
            source=parsed_info,
            include=args.include,
            doc_level=3,
            output_folder=args.output_dir,
            variants=args.variants,
        )


if __name__ == "__main__":
    main()
