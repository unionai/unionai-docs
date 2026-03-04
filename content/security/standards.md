---
title: Security Standards
variants: -flyte -serverless +byoc -selfmanaged
weight: 2
---

# Security Standards

Security standards are guidelines and frameworks that establish requirements and best practices for protecting digital assets, systems, and data from threats like unauthorized access and cyberattacks.

By deploying [Private Data Planes](architecture.md), Union ensures that the data plane is isolated from the public internet.

Union complies with the following standard controls (non-inclusive list):

## ISO 27001

| Standard  | Control | Domain                                         | Description                                                                                                                                                                           |
| --------- | ------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ISO.27001 | A.5.15  | Access control                                 | Requires restricting access to network services and management interfaces. Exposing a management endpoint to the Internet, even if ACLed, is a broader attack surface than necessary. |
| ISO.27001 | A.8.20  | Network security                               | Requires segregation and protection of networks. Management interfaces should be kept on dedicated, private, controlled channels.                                                     |
| ISO.27001 | A.8.28  | Secure configuration of information systems    | Public management plane exposure violates the principle of secure configuration by default.                                                                                           |
| ISO.27001 | A.8.21  | Use of cryptography                            | Although TLS is used by EKS, the standard also expects minimization of exposure of sensitive channels to reduce reliance solely on cryptographic controls.                            |
| ISO.27001 | A.5.23  | Information security for use of cloud services | Requires ensuring that cloud services are configured securely and risks (like public exposure of management endpoints) are mitigated.                                                 |

## CIS 1.5/3.x

| Standard    | Control | Domain                                                     | Description                                                                                                              |
| ----------- | ------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| CIS.1.5/3.x | 3.1     | Amazon EKS public endpoint access is restricted            | Explicitly recommends disabling public access to the EKS cluster endpoint or restricting it to VPC/internal access only. |
| CIS.1.5/3.x | 3.2     | Restrict access to the EKS control plane to authorized IPs | ACLing helps, but the benchmark still prioritizes private-only endpoints.                                                |

## CIS v8

| Standard | Control | Domain                            | Description                                                                                                                                        |
| -------- | ------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| CIS.v8   | 4.4     | Restrict administrative access    | Administrative interfaces must not be exposed to the Internet unless absolutely necessary, and if so, with compensating safeguards (VPN, bastion). |
| CIS.v8   | 12.11   | Segment administration interfaces | Requires separation of administrative interfaces from public access.                                                                               |
| CIS.v8   | 13.2    | Deploy DMZ / boundary protections | Management plane endpoints should live behind strong network segmentation.                                                                         |
