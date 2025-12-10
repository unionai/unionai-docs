include makefile.inc

PREFIX := $(if $(VERSION),docs/$(VERSION),docs)
PORT := 9000
BUILD := $(shell date +%s)

.PHONY: all dist variant dev update-examples sync-examples llm-docs

all: usage

usage:
	@./scripts/make_usage.sh

base:
	@if ! ./scripts/pre-build-checks.sh; then exit 1; fi
	@if ! ./scripts/pre-flight.sh; then exit 1; fi
	rm -rf dist
	mkdir -p dist
	mkdir -p dist/docs
	cat index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/index.html
	cat index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/docs/index.html
	#cp -R static/* dist/${PREFIX}/

dist: base
	make variant VARIANT=flyte
	# make variant VARIANT=serverless
	make variant VARIANT=byoc
	make variant VARIANT=selfmanaged
	make llm-docs

variant:
	@if [ -z ${VARIANT} ]; then echo "VARIANT is not set"; exit 1; fi
	@VERSION=${VERSION} ./scripts/run_hugo.sh --config hugo.toml,hugo.site.toml,hugo.ver.toml,config.${VARIANT}.toml --destination dist/${VARIANT}
	@VERSION=${VERSION} VARIANT=${VARIANT} PREFIX=${PREFIX} BUILD=${BUILD} ./scripts/gen_404.sh
	@echo "Processing shortcodes in markdown files..."
	@if [ -d "dist/docs/${VERSION}/${VARIANT}/tmp-md" ]; then \
		if command -v uv >/dev/null 2>&1; then \
		uv run tools/llms_generator/process_shortcodes.py \
			--variant=${VARIANT} \
			--version=${VERSION} \
			--input-dir=dist/docs/${VERSION}/${VARIANT}/tmp-md \
			--output-dir=dist/docs/${VERSION}/${VARIANT}/md \
			--base-path=.; \
		else \
		python3 tools/llms_generator/process_shortcodes.py \
			--variant=${VARIANT} \
			--version=${VERSION} \
			--input-dir=dist/docs/${VERSION}/${VARIANT}/tmp-md \
			--output-dir=dist/docs/${VERSION}/${VARIANT}/md \
			--base-path=.; \
		fi \
	fi

dev:
	@if ! ./scripts/pre-flight.sh; then exit 1; fi
	@if ! ./scripts/dev-pre-flight.sh; then exit 1; fi
	rm -rf public
	hugo server --config hugo.toml,hugo.site.toml,hugo.ver.toml,hugo.dev.toml,hugo.local.toml

serve:
	@if [ ! -d dist ]; then "echo Run `make dist` first"; exit 1; fi
	@PORT=${PORT} LAUNCH=${LAUNCH} ./scripts/serve.sh

update-examples:
	git submodule update --remote

init-examples:
	git submodule update --init

check-jupyter:
	./tools/jupyter_generator/check_jupyter.sh

check-images:
	./scripts/check_images.sh

validate-urls:
	@echo "Validating URLs across all variants..."
	@for variant in flyte byoc serverless selfmanaged; do \
		echo "Checking $$variant..."; \
		if [ -d "dist/docs/${VERSION}/$$variant/md" ]; then \
			if command -v uv >/dev/null 2>&1; then \
				uv run python3 validate_urls.py dist/docs/${VERSION}/$$variant/md; \
			else \
				python3 validate_urls.py dist/docs/${VERSION}/$$variant/md; \
			fi; \
		else \
			echo "No processed markdown found for $$variant"; \
		fi \
	done

url-stats:
	@echo "URL statistics across all variants:"
	@for variant in flyte byoc serverless selfmanaged; do \
		echo "=== $$variant ==="; \
		if [ -d "dist/docs/${VERSION}/$$variant/md" ]; then \
			if command -v uv >/dev/null 2>&1; then \
				uv run python3 validate_urls.py dist/docs/${VERSION}/$$variant/md --stats; \
			else \
				python3 validate_urls.py dist/docs/${VERSION}/$$variant/md --stats; \
			fi; \
		else \
			echo "No processed markdown found for $$variant"; \
		fi \
	done

llm-docs:
	@echo "Building LLM-optimized documentation..."
	@if command -v uv >/dev/null 2>&1; then \
		VERSION=${VERSION} uv run tools/llms_generator/build_llm_docs.py --no-make-dist; \
	else \
		VERSION=${VERSION} python3 tools/llms_generator/build_llm_docs.py --no-make-dist; \
	fi
	@for variant in flyte byoc selfmanaged; do \
		mkdir -p dist/docs/${VERSION}/$$variant/_static/public; \
		cp dist/docs/${VERSION}/$$variant/llms-full.txt dist/docs/${VERSION}/$$variant/_static/public/llms-full.txt; \
	done
