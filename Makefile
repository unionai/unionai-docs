PREFIX := docs
PORT := 9000

.PHONY: all dist variant dev

all: usage

usage:
	@./scripts/make_usage.sh

predist:
	@if ! scripts/pre-build-checks.sh; then exit 1; fi

base: predist
	@if ! ./scripts/pre-flight.sh; then exit 1; fi
	rm -rf dist
	mkdir -p dist
	mkdir -p dist/docs
	mkdir -p dist/_static
	cat index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/index.html
	cat index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/docs/index.html
	cp -R static/* dist/${PREFIX}/
	cp -R content/_static/* dist/_static/

dist: base
	make variant VARIANT=flyte
	make variant VARIANT=serverless
	make variant VARIANT=byoc
#	make variant VARIANT=byok

variant:
	@if [ -z ${VARIANT} ]; then echo "VARIANT is not set"; exit 1; fi
	@./scripts/run_hugo.sh --config hugo.toml,config.${VARIANT}.toml --destination dist/${VARIANT}
	@cat 404.html.tmpl | sed -e 's#@@BASE@@#/${PREFIX}#g' -e 's#@@VARIANT@@#${VARIANT}#g' > dist/docs/${VARIANT}/404.html

dev:
	@if ! ./scripts/pre-flight.sh; then exit 1; fi
	@if ! ./scripts/dev-pre-flight.sh; then exit 1; fi
	rm -rf public
	hugo server --config hugo.toml,hugo.dev.toml,hugo.local.toml

serve:
	@if [ ! -d dist ]; then "echo Run `make dist` first"; exit 1; fi
	echo "Open browser @ http://localhost:${PORT}"
	cd dist; python3 -m http.server ${PORT}
