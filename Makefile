include makefile.inc

PREFIX := $(if $(VERSION),docs/$(VERSION),docs)
PORT := 9000
BUILD := $(shell date +%s)

.PHONY: all base dist variant dev serve usage update-examples sync-examples llm-docs check-api-docs update-api-docs update-redirects dry-run-redirects deploy-redirects check-deleted-pages check-links check-generated-content clean clean-generated

all: usage

usage:
	@./scripts/make_usage.sh

clean:
	rm -rf dist public

# WARNING: clean-generated removes all generated content (API docs, CLI docs,
# notebooks, YAML data, linkmaps). Do NOT commit after running this without
# regenerating via 'make dist'. CI will block the merge (check-generated-content).
clean-generated: clean
	rm -rf content/_static/notebooks
	rm -rf content/api-reference/flyte-sdk/packages content/api-reference/flyte-sdk/classes
	rm -f content/api-reference/flyte-cli.md
	rm -rf content/api-reference/integrations/*/
	rm -f data/*.yaml
	rm -f static/*-linkmap.json

base:
	@if ! ./scripts/pre-build-checks.sh; then exit 1; fi
	@if ! ./scripts/pre-flight.sh; then exit 1; fi
	@echo "Converting Jupyter notebooks..."
	@./tools/jupyter_generator/gen_jupyter.sh
	rm -rf dist
	mkdir -p dist
	mkdir -p dist/docs
	cat index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/index.html
	cat index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/docs/index.html

dist: base
	make update-redirects
	-make check-deleted-pages
	make update-api-docs
	-make check-links
	make variant VARIANT=flyte
	# Serverless variant build is currently disabled
	make variant VARIANT=byoc
	make variant VARIANT=selfmanaged
	make llm-docs

variant:
	@if [ -z ${VARIANT} ]; then echo "VARIANT is not set"; exit 1; fi
	@VERSION=${VERSION} ./scripts/run_hugo.sh
	@VERSION=${VERSION} VARIANT=${VARIANT} PREFIX=${PREFIX} BUILD=${BUILD} ./scripts/gen_404.sh
	@if [ -d "dist/docs/${VERSION}/${VARIANT}/tmp-md" ]; then \
		if command -v uv >/dev/null 2>&1; then \
		uv run tools/llms_generator/process_shortcodes.py \
			--variant=${VARIANT} \
			--version=${VERSION} \
			--input-dir=dist/docs/${VERSION}/${VARIANT}/tmp-md \
			--output-dir=dist/docs/${VERSION}/${VARIANT} \
			--base-path=. \
			--quiet; \
		else \
		python3 tools/llms_generator/process_shortcodes.py \
			--variant=${VARIANT} \
			--version=${VERSION} \
			--input-dir=dist/docs/${VERSION}/${VARIANT}/tmp-md \
			--output-dir=dist/docs/${VERSION}/${VARIANT} \
			--base-path=. \
			--quiet; \
		fi; \
		rm -rf dist/docs/${VERSION}/${VARIANT}/tmp-md; \
	fi

dev:
	@if ! ./scripts/pre-flight.sh; then exit 1; fi
	@if ! ./scripts/dev-pre-flight.sh; then exit 1; fi
	rm -rf public
	hugo server --config hugo.toml,hugo.site.toml,hugo.ver.toml,hugo.dev.toml,hugo.local.toml

serve:
	@if [ ! -d dist ]; then echo "Run 'make dist' first"; exit 1; fi
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
		if [ -d "dist/docs/${VERSION}/$$variant" ]; then \
			if command -v uv >/dev/null 2>&1; then \
				uv run python3 tools/validate_urls.py dist/docs/${VERSION}/$$variant; \
			else \
				python3 tools/validate_urls.py dist/docs/${VERSION}/$$variant; \
			fi; \
		else \
			echo "No processed markdown found for $$variant"; \
		fi \
	done

url-stats:
	@echo "URL statistics across all variants:"
	@for variant in flyte byoc serverless selfmanaged; do \
		echo "=== $$variant ==="; \
		if [ -d "dist/docs/${VERSION}/$$variant" ]; then \
			if command -v uv >/dev/null 2>&1; then \
				uv run python3 tools/validate_urls.py dist/docs/${VERSION}/$$variant --stats; \
			else \
				python3 tools/validate_urls.py dist/docs/${VERSION}/$$variant --stats; \
			fi; \
		else \
			echo "No processed markdown found for $$variant"; \
		fi \
	done

llm-docs:
	@if command -v uv >/dev/null 2>&1; then \
		VERSION=${VERSION} uv run tools/llms_generator/build_llm_docs.py --no-make-dist --quiet; \
	else \
		VERSION=${VERSION} python3 tools/llms_generator/build_llm_docs.py --no-make-dist --quiet; \
	fi

update-redirects:
	@echo "Detecting moved pages and appending to redirects.csv..."
	@if command -v uv >/dev/null 2>&1; then \
		uv run tools/redirect_generator/detect_moved_pages.py; \
	else \
		python3 tools/redirect_generator/detect_moved_pages.py; \
	fi

dry-run-redirects:
	@echo "Dry run: detecting moved pages from git history..."
	@if command -v uv >/dev/null 2>&1; then \
		uv run tools/redirect_generator/detect_moved_pages.py --dry-run; \
	else \
		python3 tools/redirect_generator/detect_moved_pages.py --dry-run; \
	fi

deploy-redirects:
	@python3 tools/redirect_generator/deploy_redirects.py

check-deleted-pages:
	@if command -v uv >/dev/null 2>&1; then \
		uv run tools/redirect_generator/check_deleted_pages.py; \
	else \
		python3 tools/redirect_generator/check_deleted_pages.py; \
	fi

check-links:
	@if command -v uv >/dev/null 2>&1; then \
		uv run tools/link_checker/check_internal_links.py; \
	else \
		python3 tools/link_checker/check_internal_links.py; \
	fi

check-generated-content:
	@uv run tools/check_generated_content.py

check-api-docs:
	@uv run tools/api_generator/check_versions.py --check

check-llm-bundle-notes:
	@uv run python tools/llms_generator/check_llm_bundle_notes.py

update-api-docs:
	@if command -v uv >/dev/null 2>&1; then \
		uv run tools/api_generator/check_versions.py --update; \
	else \
		echo "uv not available, skipping API docs update (using committed docs)"; \
	fi
