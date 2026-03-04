---
title: VPC Endpoints
variants: -flyte -serverless +byoc +selfmanaged
---

# VPC Endpoints

Ensure your VPC include these endpoints so when the Union stack needs to connect to the corresponding AWS services, it does so without leaving the AWS network:

| Endpoint                                      | Purpose                                                            |
| --------------------------------------------- | ------------------------------------------------------------------ |
| `com.amazonaws.<REGION>.autoscaling`          | Allows the Union stack to manage the autoscaling groups in the VPC |
| `com.amazonaws.<REGION>.xray`                 | Allows the Union stack to collect and store X-Ray traces           |
| `com.amazonaws.<REGION>.s3`                   | Allows the Union stack to store and retrieve data from S3          |
| `com.amazonaws.<REGION>.sts`                  | Allows the Union stack to assume IAM roles                         |
| `com.amazonaws.<REGION>.ecr.api`              | Allows the Union stack to interact with the ECR API                |
| `com.amazonaws.<REGION>.ssm`                  | Allows the Union stack to interact with SSM                        |
| `com.amazonaws.<REGION>.ec2messages`          | Allows the Union stack to interact with EC2 messages               |
| `com.amazonaws.<REGION>.ec2`                  | Allows the Union stack to interact with EC2                        |
| `com.amazonaws.<REGION>.ssmmessages`          | Allows the Union stack to interact with SSM messages               |
| `com.amazonaws.<REGION>.ecr.dkr`              | Allows the Union stack to interact with ECR                        |
| `com.amazonaws.<REGION>.logs`                 | Allows the Union stack to interact with CloudWatch Logs            |
| `com.amazonaws.<REGION>.eks-auth`             | Allows the Union stack to interact with EKS                        |
| `com.amazonaws.<REGION>.eks`                  | Allows the Union stack to interact with EKS                        |
| `com.amazonaws.<REGION>.elasticloadbalancing` | Allows the Union stack to interact with Elastic Load Balancing     |

Replace `<REGION>` with your AWS region, e.g., `us-east-2`.

Refer to [Data plane setup on AWS](../../../deployment/data-plane-setup-on-aws.md) for complete reference.
