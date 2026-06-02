# EKS Production Platform

A production-grade Kubernetes platform on AWS EKS with full CI/CD, observability, and autoscaling.

## Stack

| Component | Technology |
|-----------|------------|
| Infrastructure | Terraform |
| Container Orchestration | AWS EKS v1.30 |
| CI/CD | GitHub Actions + OIDC |
| Container Registry | Amazon ECR |
| App Deployment | Helm |
| Autoscaling | HPA (CPU-based) |
| Monitoring | Prometheus + Grafana |
| Networking | VPC, NAT GW, ALB |

## Project Structure

`
.
+-- app/                    # Flask application + Dockerfile
+-- helm/app/               # Helm chart (deployment, service, HPA)
+-- terraform/
|   +-- modules/            # vpc, eks, ecr modules
|   +-- environments/dev/   # dev environment config
+-- .github/workflows/      # GitHub Actions CI/CD pipeline
`

## CI/CD Pipeline

On every push to main:
1. Authenticate to AWS via OIDC (no stored credentials)
2. Build Docker image and push to ECR
3. Deploy to EKS using Helm
4. Verify rollout and pod health

## Infrastructure Setup

`ash
cd terraform/environments/dev
terraform init
terraform apply
`

## Monitoring

Grafana deployed via kube-prometheus-stack with dashboards for:
- Kubernetes cluster resources
- Node metrics
- Pod and workload monitoring
- Alertmanager

## Key Features

- **Zero static credentials** - GitHub Actions uses AWS OIDC federation
- **Auto-scaling** - HPA scales pods 2 to 6 based on CPU utilization
- **Production networking** - private subnets for nodes, NAT GW for egress
- **GitOps ready** - every push triggers full build and deploy pipeline
- **Full observability** - Prometheus metrics, Grafana dashboards out of the box
