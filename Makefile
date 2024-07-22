.PHONY: update-examples
update-examples:
	git submodule update --remote

.PHONY: sync-examples
sync-examples:
	git submodule update --init

.PHONY: build
build: sync-examples
	UNION_SERVERLESS_ENDPOINT= python build.py

.PHONY: api
api:
	UNION_SERVERLESS_ENDPOINT= python build.py --api

.PHONY: clean
clean:
	rm -rf build sphinx_source
