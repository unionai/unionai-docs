.PHONY: update-examples
update-examples:
	git submodule update --remote

.PHONY: sync-examples
sync-examples:
	git submodule update --init

.PHONY: build-local
build-local: sync-examples
	UNION_SERVERLESS_ENDPOINT= python build.py

.PHONY: clean
clean:
	rm -rf build sphinx_source

.PHONY: serve-local
PORT ?= 8000
GREEN := \033[0;32m
NC := \033[0m # no color
serve-local:
	@echo "$(GREEN)Starting local server on port $(PORT) to serve the documentation...$(NC)"
	[ -x "$(shell command -v uv)" ] || pip install uv
	[ -d ".venv" ] || uv venv
	uv pip install -r docs-requirements.txt
	. .venv/bin/activate; UNION_SERVERLESS_ENDPOINT= python3 -m http.server --directory build/html ${PORT}
# check if a port is passed as an arg and override PORT var
ifdef port
override PORT := $(port)
endif

.PHONY: build
build: sync-examples
	[ -x "$(shell command -v uv)" ] || pip install uv
	[ -d ".venv" ] || uv venv
	uv pip install -r docs-requirements.txt
	. .venv/bin/activate; UNION_SERVERLESS_ENDPOINT= python build.py
