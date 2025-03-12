.PHONY: all dist variant dev

all: usage

usage:
	@./scripts/make_usage.sh

base:
	rm -rf dist
	mkdir dist
	cp index.html dist/
	cp -R static/* dist/

dist: base
	make variant VARIANT=serverless
	make variant VARIANT=byoc

variant:
	@if [ -z ${VARIANT} ]; then echo "VARIANT is not set"; exit 1; fi
	@./scripts/run_hugo.sh --config hugo.toml,config.${VARIANT}.toml --destination dist/${VARIANT}

dev:
	rm -rf public
	if ! ./scripts/dev-pre-flight.sh; then exit 1; fi
	hugo server --config hugo.toml,hugo.local.toml

serve:
	@if [ ! -d dist ]; then "echo Run `make dist` first"; exit 1; fi
	@if [ -z ${PORT} ]; then make usage; echo "FATAL: Port missing"; exit 1; fi
	@echo "Open browser @ http://localhost:${PORT}"
	cd dist; python3 -m http.server ${PORT}
