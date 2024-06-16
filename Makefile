
.PHONY: update-examples
update-examples:
	git submodule update --init

.PHONY: build
build: update-examples
	UNIONAI_SERVERLESS_ENDPOINT= python build.py

.PHONY: clean
clean:
	rm -rf build sphinx_source
