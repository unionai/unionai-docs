.PHONY: update-examples
update-examples:
	git submodule update --remote

.PHONY: sync-examples
sync-examples:
	git submodule update --init

.PHONY: build
build: sync-examples
	UNION_SERVERLESS_API_KEY= python build.py

.PHONY: clean
clean:
	rm -rf build sphinx_source
