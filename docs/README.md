<div align="center">

# EKS Production Platform

**Production-grade Kubernetes platform on AWS EKS**

![CI/CD](https://img.shields.io/github/actions/workflow/status/akshayapannir-sre/eks-production-platform/deploy.yml?label=CI%2FCD&logo=github-actions&logoColor=white)
![EKS](https://img.shields.io/badge/EKS-v1.30-orange?logo=amazon-eks&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.13-purple?logo=terraform&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-3.18-blue?logo=helm&logoColor=white)

</div>

---

## Overview

A fully automated, production-ready Kubernetes platform built on AWS EKS. Includes end-to-end CI/CD with zero stored credentials, auto-scaling, and full observability, all provisioned as code.

---

## Architecture

![Architecture Diagram](docs/architecture.png)

---

## CI/CD Pipeline

![Pipeline Success](docs/pipeline-success.png)

Every push to main triggers a full build and deploy:

| Step | Action |
|------|--------|
| 1 | Authenticate to AWS via GitHub OIDC - no static credentials |
| 2 | Build Docker image and push to Amazon ECR |
| 3 | Deploy to EKS using Helm |
| 4 | Verify rollout and pod health |

---

## Observability

![Grafana Dashboard](docs/grafana-dashboard.png)

Full cluster observability via kube-prometheus-stack:

- Kubernetes cluster, node, and pod metrics
- HPA scaling events
- Alertmanager for notifications
- Grafana exposed via AWS Load Balancer

---

## Live Cluster

![Pods Running](docs/pods-running.png)

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


.
+-- app/                        # Flask app + Dockerfile
+-- helm/
|   +-- app/                    # Helm chart
|       +-- templates/          # deployment, service, HPA
|       +-- values.yaml
+-- terraform/
|   +-- modules/
|   |   +-- vpc/                # VPC, subnets, NAT GW
|   |   +-- eks/                # EKS cluster + node group
|   |   +-- ecr/                # Container registry
|   +-- environments/
|       +-- dev/                # Dev environment config
+-- .github/
|   +-- workflows/
|       +-- deploy.yml          # CI/CD pipeline
+-- docs/                       # Screenshots and diagrams

---

## Infrastructure Setup

**Prerequisites:** AWS CLI, Terraform, kubectl, Helm

```bash
cd terraform/environments/dev
terraform init
terraform apply

aws eks update-kubeconfig --name eks-platform-dev --region us-west-1
```

---

## Key Features

- **Zero static credentials** - GitHub Actions authenticates via AWS OIDC. No access keys stored anywhere.
- **Auto-scaling** - HPA scales the app from 2 to 6 pods based on CPU utilization.
- **Production networking** - Nodes in private subnets, outbound traffic via NAT Gateway.
- **GitOps ready** - Every push to main triggers full build, push, and deploy in under 60 seconds.
- **Full observability** - Prometheus and Grafana with pre-built Kubernetes dashboards.
- **Infrastructure as code** - Every AWS resource managed by Terraform with remote state and locking.

---

<div align="center">
Built by <a href="https://linkedin.com/in/akshayapanneerselvam">Akshaya P</a> · SRE Portfolio Project
</div>