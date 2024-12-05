.PHONY: update-examples
update-examples:
	git submodule update --remote

.PHONY: sync-examples
sync-examples:
	git submodule update --init

.PHONY: build-local
build-local: sync-examples
	UNION_SERVERLESS_ENDPOINT= uv run build.py

.PHONY: clean
clean:
	rm -rf build sphinx_source


.PHONY: build
build: sync-examples
	[ -x "$(shell command -v uv)" ] || pip install uv
	uv sync
	UNION_SERVERLESS_ENDPOINT= uv run build.py
