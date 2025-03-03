---
title: "Installation Guide"
weight: 1
---

# Installation Guide

This guide covers the installation and initial setup of Union AI in various deployment environments.

## System Requirements

### Hardware Requirements

- CPU: 4+ cores
- RAM: 8GB minimum, 16GB recommended
- Storage: 20GB minimum free space

### Software Requirements

- Linux (Ubuntu 20.04+, CentOS 7+)
- Kubernetes 1.19+
- Docker 20.10+
- Helm 3.0+

## Installation Methods

### Using Helm Chart

1. Add the Union AI Helm repository:
```bash
helm repo add unionai https://charts.unionai.com
helm repo update
```

2. Install Union AI:
```bash
helm install unionai unionai/unionai-platform \
  --namespace unionai \
  --create-namespace
```

### Manual Installation

1. Download the installation script:
```bash
curl -O https://get.unionai.com/install.sh
chmod +x install.sh
```

2. Run the installer:
```bash
./install.sh
```

## Post-Installation

1. Verify the installation:
```bash
kubectl get pods -n unionai
```

2. Configure access:
```bash
unionai config init
```

## Next Steps

- Configure [Authentication](../authentication)
- Set up [High Availability](../high-availability)
- Review [Security Best Practices](../security)