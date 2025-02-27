.PHONY: update-examples
update-examples:
	git submodule update --remote

.PHONY: sync-examples
sync-examples:
	git submodule update --init

.PHONY: build-local
build-local: sync-examples
	rsync -a --info=progress2 source.public/ source/
	UNION_SERVERLESS_ENDPOINT= ENABLE_UNION_SERVING=1 uv run build.py

.PHONY: clean
clean:
	rm -rf build sphinx_source


.PHONY: build
build: sync-examples
	[ -x "$(shell command -v uv)" ] || pip install uv
	uv sync
	rsync -a --info=progress2 source.public/ source/
	UNION_SERVERLESS_ENDPOINT= ENABLE_UNION_SERVING=1 uv run build.py
