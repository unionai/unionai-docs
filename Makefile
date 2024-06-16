.PHONY: build
build:
	UNIONAI_SERVERLESS_ENDPOINT= python build.py

.PHONY: clean
clean:
	rm -rf build sphinx_source

.PHONY: update-examples
update-examples:
	git submodule update --init
