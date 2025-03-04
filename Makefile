.PHONY: all dist variant dev

all:
	@scripts/make_usage.sh

dist:
	rm -rf dist
	mkdir dist
	cp index.html dist/
	rsync -a --progress static/ dist/

	make variant VARIANT=serverless
	make variant VARIANT=byoc

variant:
	@if [ -z ${VARIANT} ]; then echo "VARIANT is not set"; exit 1; fi
	hugo --config hugo.toml,config.${VARIANT}.toml --destination dist/${VARIANT}

dev:
	rm -rf public
	if ! scripts/dev-pre-flight.sh; then exit 1; fi
	hugo server --config hugo.toml,hugo.local.toml
