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

.PHONY: build
build: sync-examples
	[ -x "$(shell command -v uv)" ] || pip install uv
	[ -d ".venv" ] || uv venv
	uv pip install -r docs-requirements.txt
	. .venv/bin/activate; UNION_SERVERLESS_ENDPOINT= python build.py
