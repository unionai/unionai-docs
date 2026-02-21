# Thin delegator — forwards all targets to infra/Makefile.
# Version-specific variables live in makefile.inc (this directory).
# Shared build logic lives in infra/Makefile.

include makefile.inc

export REPO_ROOT := $(CURDIR)
export VERSION
export VARIANTS

PORT ?= 9000
export PORT

# Forward all known targets to infra/Makefile.
# These must be listed explicitly because Make's % pattern rule won't match
# targets that correspond to existing files/directories (e.g., dist/).
TARGETS := usage clean clean-generated base dist variant dev serve \
	update-examples init-examples check-jupyter check-images validate-urls \
	url-stats llm-docs update-redirects dry-run-redirects deploy-redirects \
	check-deleted-pages check-links check-generated-content check-api-docs \
	check-llm-bundle-notes update-api-docs

.PHONY: $(TARGETS)
$(TARGETS):
	@$(MAKE) --no-print-directory -f infra/Makefile $@

.DEFAULT_GOAL := usage
