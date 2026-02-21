# infra/Makefile — Shared build logic.
# Invoked from the thin top-level Makefile via: make -f infra/Makefile <target>
# Working directory is always the repo root (not infra/).
# VERSION, VARIANTS, REPO_ROOT, PORT are exported by the top-level Makefile.

PREFIX := $(if $(VERSION),docs/$(VERSION),docs)
PORT ?= 9000
BUILD := $(shell date +%s)

.PHONY: all base dist variant dev serve usage update-examples sync-examples llm-docs check-api-docs update-api-docs update-redirects dry-run-redirects deploy-redirects check-deleted-pages check-links check-generated-content clean clean-generated

all: usage

usage:
	@infra/scripts/make_usage.sh

clean:
	rm -rf dist public

# WARNING: clean-generated removes all generated content (API docs, CLI docs,
# notebooks, YAML data, linkmaps). Do NOT commit after running this without
# regenerating via 'make dist'. CI will block the merge (check-generated-content).
clean-generated: clean
	rm -rf content/_static/notebooks
	@uv run infra/tools/clean_generated.py

base:
	@if ! infra/scripts/pre-build-checks.sh; then exit 1; fi
	@if ! infra/scripts/pre-flight.sh; then exit 1; fi
	@echo "Converting Jupyter notebooks..."
	@infra/tools/jupyter_generator/gen_jupyter.sh
	rm -rf dist
	mkdir -p dist
	mkdir -p dist/docs
	cat infra/index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/index.html
	cat infra/index.html.tmpl | sed 's#@@BASE@@#/${PREFIX}#g' > dist/docs/index.html

dist:
	@VARIANTS="$(VARIANTS)" PARALLEL_HUGO="$(PARALLEL_HUGO)" infra/scripts/build_dist.sh

variant:
	@if [ -z ${VARIANT} ]; then echo "VARIANT is not set"; exit 1; fi
	@VERSION=${VERSION} infra/scripts/run_hugo.sh
	@VERSION=${VERSION} VARIANT=${VARIANT} PREFIX=${PREFIX} BUILD=${BUILD} infra/scripts/gen_404.sh
	@if [ -d "dist/docs/${VERSION}/${VARIANT}/tmp-md" ]; then \
		uv run infra/tools/llms_generator/process_shortcodes.py \
			--variant=${VARIANT} \
			--version=${VERSION} \
			--input-dir=dist/docs/${VERSION}/${VARIANT}/tmp-md \
			--output-dir=dist/docs/${VERSION}/${VARIANT} \
			--base-path=. \
			--quiet; \
		rm -rf dist/docs/${VERSION}/${VARIANT}/tmp-md; \
	fi

dev:
	@if ! infra/scripts/pre-flight.sh; then exit 1; fi
	@if ! infra/scripts/dev-pre-flight.sh; then exit 1; fi
	rm -rf public
	hugo server --config infra/hugo.toml,hugo.site.toml,infra/hugo.ver.toml,infra/hugo.dev.toml,hugo.local.toml

serve:
	@if [ ! -d dist ]; then echo "Run 'make dist' first"; exit 1; fi
	@PORT=${PORT} LAUNCH=${LAUNCH} infra/scripts/serve.sh

update-examples:
	git submodule update --remote

init-examples:
	git submodule update --init

check-jupyter:
	infra/tools/jupyter_generator/check_jupyter.sh

check-images:
	infra/scripts/check_images.sh

validate-urls:
	@echo "Validating URLs across all variants..."
	@for variant in flyte byoc serverless selfmanaged; do \
		echo "Checking $$variant..."; \
		if [ -d "dist/docs/${VERSION}/$$variant" ]; then \
			uv run python3 infra/tools/validate_urls.py dist/docs/${VERSION}/$$variant; \
		else \
			echo "No processed markdown found for $$variant"; \
		fi \
	done

url-stats:
	@echo "URL statistics across all variants:"
	@for variant in flyte byoc serverless selfmanaged; do \
		echo "=== $$variant ==="; \
		if [ -d "dist/docs/${VERSION}/$$variant" ]; then \
			uv run python3 infra/tools/validate_urls.py dist/docs/${VERSION}/$$variant --stats; \
		else \
			echo "No processed markdown found for $$variant"; \
		fi \
	done

llm-docs:
	@VERSION=${VERSION} uv run infra/tools/llms_generator/build_llm_docs.py --no-make-dist --quiet

update-redirects:
	@echo "Detecting moved pages and appending to redirects.csv..."
	@uv run infra/tools/redirect_generator/detect_moved_pages.py

dry-run-redirects:
	@echo "Dry run: detecting moved pages from git history..."
	@uv run infra/tools/redirect_generator/detect_moved_pages.py --dry-run

deploy-redirects:
	@uv run infra/tools/redirect_generator/deploy_redirects.py

check-deleted-pages:
	@uv run infra/tools/redirect_generator/check_deleted_pages.py

check-links:
	@uv run infra/tools/link_checker/check_internal_links.py

check-generated-content:
	@uv run infra/tools/check_generated_content.py

check-api-docs:
	@uv run infra/tools/api_generator/check_versions.py --check

check-llm-bundle-notes:
	@uv run python infra/tools/llms_generator/check_llm_bundle_notes.py

update-api-docs:
	@uv run infra/tools/api_generator/check_versions.py --update
