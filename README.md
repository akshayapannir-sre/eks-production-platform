<div align="center">

# EKS Production Platform

**Production-grade Kubernetes platform on AWS EKS**

![CI/CD](https://img.shields.io/github/actions/workflow/status/akshayapannir-sre/eks-production-platform/deploy.yml?label=CI%2FCD&logo=github-actions&logoColor=white)
![EKS](https://img.shields.io/badge/EKS-v1.30-orange?logo=amazon-eks&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.13-purple?logo=terraform&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-3.18-blue?logo=helm&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

## Overview

A fully automated, production-ready Kubernetes platform built on AWS EKS. Includes end-to-end CI/CD with zero stored credentials, horizontal auto-scaling, and full observability — all provisioned as infrastructure as code using Terraform.

---

## Architecture

```
Developer
    |
    | git push
    v
GitHub Actions
    |-- OIDC Auth ---------> AWS STS (AssumeRole)
    |-- Build image -------> Amazon ECR
    |-- Helm deploy -------> EKS Cluster (us-west-1)
                                 |
                        +--------+--------+
                        |                 |
                   Private Subnet    Private Subnet
                   (us-west-1b)      (us-west-1c)
                        |                 |
                   Node: t3.medium   Node: t3.medium
                        |
                +-------+-------+
                |               |
           Flask App        Monitoring
           (HPA 2-6)    Prometheus + Grafana
```

---

## Stack

| Component | Technology |
|-----------|------------|
| Infrastructure | Terraform |
| Container Orchestration | AWS EKS v1.30 |
| CI/CD | GitHub Actions + OIDC |
| Container Registry | Amazon ECR |
| App Deployment | Helm |
| Autoscaling | HPA (CPU-based, 2 to 6 pods) |
| Monitoring | Prometheus + Grafana |
| Networking | VPC, private subnets, NAT GW |
| State Management | S3 + DynamoDB |

---

## Project Structure

```
.
+-- app/
|   +-- main.py                 # Flask application
|   +-- requirements.txt
|   +-- Dockerfile
+-- helm/
|   +-- app/
|       +-- Chart.yaml
|       +-- values.yaml
|       +-- templates/
|           +-- deployment.yaml
|           +-- service.yaml
|           +-- hpa.yaml
+-- terraform/
|   +-- modules/
|   |   +-- vpc/                # VPC, subnets, IGW, NAT GW, route tables
|   |   +-- eks/                # EKS cluster, node group, IAM roles
|   |   +-- ecr/                # Container registry
|   +-- environments/
|       +-- dev/
|           +-- main.tf
|           +-- variables.tf
|           +-- outputs.tf
|           +-- backend.tf
+-- .github/
|   +-- workflows/
|       +-- deploy.yml          # CI/CD pipeline
```

---

## CI/CD Pipeline

On every push to `main`:

1. **OIDC Authentication** — GitHub Actions assumes an AWS IAM role via OpenID Connect. No access keys stored anywhere.
2. **Build** — Docker image built from `app/` and pushed to Amazon ECR tagged with the commit SHA.
3. **Deploy** — Helm upgrades the release on EKS with the new image tag.
4. **Verify** — Pipeline confirms the rollout succeeds and all pods are running before completing.

---

## Infrastructure Setup

**Prerequisites:** AWS CLI, Terraform >= 1.0, kubectl, Helm

```bash
# Clone the repo
git clone https://github.com/akshayapannir-sre/eks-production-platform
cd eks-production-platform

# Deploy infrastructure
cd terraform/environments/dev
terraform init
terraform apply

# Configure kubectl
aws eks update-kubeconfig --name eks-platform-dev --region us-west-1

# Verify nodes
kubectl get nodes
```

---

## Observability

Deployed via `kube-prometheus-stack` Helm chart:

- **Prometheus** — scrapes metrics from all cluster components
- **Grafana** — pre-built dashboards for cluster, node, pod, and workload metrics
- **Alertmanager** — alert routing and notification
- **metrics-server** — enables HPA to scale based on CPU utilization

---

## Key Features

- **Zero static credentials** — GitHub Actions uses AWS OIDC federation. No IAM user or access keys required.
- **Auto-scaling** — HPA automatically scales pods from 2 to 6 based on CPU utilization.
- **Production networking** — Worker nodes run in private subnets. All outbound traffic routes through a NAT Gateway.
- **GitOps ready** — Every push to main triggers a full build, push, and Helm deploy in under 60 seconds.
- **Full observability** — Prometheus scrapes metrics cluster-wide. Grafana provides dashboards out of the box.
- **Infrastructure as code** — Every AWS resource defined in Terraform with S3 remote state and DynamoDB locking.

---

<div align="center">
Built by <a href="https://linkedin.com/in/akshayapanneerselvam">Akshaya P</a> &nbsp;·&nbsp; SRE Portfolio Project
</div>
