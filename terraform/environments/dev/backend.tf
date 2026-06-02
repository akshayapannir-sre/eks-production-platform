terraform {
  backend "s3" {
    bucket         = "eks-platform-tfstate-AWS_ACCOUNT_ID"
    key            = "dev/eks-platform/terraform.tfstate"
    region         = "us-west-1"
    encrypt        = true
    dynamodb_table = "eks-platform-tflock"
  }
}
