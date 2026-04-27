"""
Selfmanaged GCP E2E test.

**This module is being rewritten to the Flyte 2 function style used by
``selfmanaged_aws_e2e.py``.** It is intentionally empty on this branch; the
GCP mirror is a follow-up PR.

The previous synchronous/uctl-driven version lives in git history:
    git show main:scripts/selfmanaged_gcp_e2e.py

To port: copy the structure of ``selfmanaged_aws_e2e.py`` and replace each
AWS-specific task with its GCP equivalent:

    AWS                         GCP
    ──────────────────────────  ───────────────────────────────
    resolve_aws_account_id      (use cfg.project_id — already set)
    create_eks                  create_gke
    create_s3_bucket            create_gcs_bucket
    create_ecr                  create_ar_repo
    create_iam_role             create_workload_identity
    patch_values_yaml           patch_values_yaml (GCP patches)
    teardown                    teardown_gcp

The shared pieces (provision_dataplane, helm_install, cluster_wait_healthy,
verify_*, smoke_test) come straight from ``selfmanaged_common.py`` and work
against any cloud.
"""

raise NotImplementedError(
    "selfmanaged_gcp_e2e is being rewritten; see the module docstring and "
    "selfmanaged_aws_e2e.py for the current Flyte 2 pattern."
)
