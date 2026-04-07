# Thin delegator — forwards all targets to unionai-docs-infra/Makefile.
# Version-specific variables live in makefile.inc (this directory).
# Shared build logic lives in unionai-docs-infra/Makefile.

include makefile.inc

export REPO_ROOT := $(CURDIR)
export VERSION
export VARIANTS
export DEFAULT_VARIANT

PORT ?= 9000
export PORT

# Forward all known targets to unionai-docs-infra/Makefile.
# These must be listed explicitly because Make's % pattern rule won't match
# targets that correspond to existing files/directories (e.g., dist/).
TARGETS := usage clean clean-generated base dist variant dev serve \
	update-examples init-examples check-jupyter check-images validate-urls \
	url-stats llm-docs update-redirects dry-run-redirects deploy-redirects \
	check-deleted-pages check-links check-generated-content check-api-docs \
	check-llm-bundle-notes update-api-docs check-helm-docs update-helm-docs

# Guard: fail fast if the infra submodule is not initialized.
.PHONY: _check-infra
_check-infra:
	@if [ ! -f unionai-docs-infra/Makefile ]; then \
		echo "ERROR: unionai-docs-infra/ submodule not initialized. Run: git submodule update --init"; \
		exit 1; \
	fi

.PHONY: $(TARGETS)
$(TARGETS): _check-infra
	@$(MAKE) --no-print-directory -f unionai-docs-infra/Makefile $@

# Submodule update helpers (not forwarded to unionai-docs-infra/Makefile).
.PHONY: update-infra
update-infra:
	git submodule update --remote unionai-docs-infra
	@echo "unionai-docs-infra/ updated to latest. Review and commit the change."

.DEFAULT_GOAL := usage
