---
title: Presigned URL data types
weight: 16
variants: -flyte +byoc +selfmanaged
---

# Presigned URL data types

| Data Type | Access Method | Direction |
| --- | --- | --- |
| Task inputs/outputs | Presign via ObjectStore service | Download (GET) |
| Code bundles (TGZ) | CreateDownloadLinkV2 | Download (GET) |
| Reports (HTML) | CreateDownloadLinkV2 | Download (GET) |
| Fast registration uploads | CreateUploadLocation | Upload (PUT) |
