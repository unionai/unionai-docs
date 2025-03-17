.PHONY: all
all: parser generate

.PHONY: parser
parser:
	python main_parser.py --package flytekit > /tmp/flytekit.api.yaml

.PHONY: generate
generate:
	python main_generate.py \
		/tmp/flytekit.api.yaml \
		../../content/api-reference/flytekit \
		--title "FlyteKit API" \
		--variants \
			+flyte \
			+byoc \
			+byok \
			+serverless \
		--include ../../include/api.flyte.md
