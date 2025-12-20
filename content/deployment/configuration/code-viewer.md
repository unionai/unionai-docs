---
title: Code Viewer
weight: 1
variants: -flyte -serverless -byoc +selfmanaged
---

# Code Viewer
One of the powerful capabilities in the Union UI is the ability to view the exact code that ran a particular task. 
Union Union implements a secure mechanism to transfer the [code bundle](../../user-guide/run-scaling/life-of-a-run.md/#phase-2-image-building) to the browser without passing through the control plane.

![Code Viewer](../../_static/images/deployment/configuration/code-viewer/demo.png)

## Enable CORS policy on your fast registration bucket
In order to support this functionality securely, your bucket must allow CORS access for Union. Depending on which cloud the bucket is located in, these configurations vary.

{{< tabs "bucket-cors-policy" >}}
{{< tab "AWS S3 Console" >}}
1. Access AWS Console
2. Access S3 dashboard
3. Choose the fast registration bucket. Unless configured differently, this is the same as the metadata bucket configured when you first
    deployed.
4. Click on "Permissions" tab and scroll to "CORS Policy"
5. Click on Edit and enter the policy below
![Code Viewer](../../_static/images/deployment/configuration/code-viewer/s3.png)
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD",
        ],
        "AllowedOrigins": [
            "https://*.unionai.cloud"
        ],
        "ExposeHeaders": [
            "ETag"
        ],
        "MaxAgeSeconds": 3600
    }
]
```
Further reference: [AWS Guide on S3 CORS Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html)
{{< /tab >}}
{{< tab "Google GCS" >}}
Google GCS does not allow changing the bucket policy through the console.
1. Create a cors.json configuration file and paste the content below
    ```json
    [
        {
        "origin": ["https://*.unionai.cloud"],
        "method": ["HEAD", "GET"],
        "responseHeader": ["ETag"],
        "maxAgeSeconds": 3600
        }
    ]
    ```
2. Apply the cors configuration:
    ```bash
    gcloud storage buckets update gs://<fast_registration_bucket> --cors-file=cors.json
    ```
3. View configuration to confirm:
   ```bash
   gcloud storage buckets describe gs://<fast_registration_bucket> --format="default(cors_config)"

   cors_config:
   - maxAgeSeconds: 3600
     method:
     - GET
     - HEAD
     origin:
     - https://*.unionai.cloud
     responseHeader:
     - ETag
   ```
Further reference: [Google Guide on GCS CORS Policy](https://docs.cloud.google.com/storage/docs/using-cors#command-line)
{{< /tab >}}
{{< tab "Azure Storage" >}}
Further reference: [Azure Guide on Storage CORS Policy](https://learn.microsoft.com/en-us/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services)
{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

| Error Message | Cause | Fix |
|---------------|-------|-----|
| `Not available: No code available for this action.` | The underlying task doesn't have a code bundle, this could be because all code is already in the underlying docker image or the task isn't a code task. | Expected behavior for non-code-bundled tasks |
| `Not Found: The code bundle file could not be found. This may be due to your organization's data retention policy.` | The task does use a code bundle but the underlying bundle isn't found in the bucket. | Check fast registration bucket retention policy |
| `Error: Code download is blocked by your storage bucket's configuration. Please contact your administrator to enable access.` | CORS isn't properly configured on the bucket | Refer to the above guide to enable CORS. |