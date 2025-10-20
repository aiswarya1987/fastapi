# Sample Python Service (FastAPI)

This file provides the required documentation for the pipeline flow, security check, and rollback strategy (conceptual).
# DevOps Challenge Submission: FastAPI CI/CD Pipeline

This repository implements a production-minded CI/CD pipeline for a containerized FastAPI microservice, using **GitHub Actions** and deploying to a **Kubernetes** staging environment.

### 1. The Pipeline Flow (CI/CD)

The pipeline is defined in `.github/workflows/build_and_test.yml` and is triggered on every push to the `main` / 'trunk' branch.

1. Test : Pytest - Runs unit and integration tests. Pipeline fails if tests fail.
2. Docker/GitHub Actions -Builds the container image using the secure multi-stage Dockerfile.  Container image tagged with Git SHA.
3.  Scan (Security/Quality Check) via Trivy - Scans the image for OS and dependency vulnerabilities. Fails pipeline if HIGH/CRITICAL vulnerabilities are found.
4.  Push GHCR - Pushes the security-vetted, tagged image to the registry.Image available for deployment.
5.  Deploy** `kubectl` Applies the deployment manifest, injecting the new image tag to the `staging` namespace.Updated deployment in staging. 

## 2. The Security/Compliance Check Implemented

The security check is enforced in the scan stage using Trivy

  Check Implemented:Vulnerability scanning of the container image.
  Compliance Rule: The pipeline is configured to explicitly fail (exit-code: 1) if Trivy identifies any vulnerabilities categorized as 
  CRITICAL or HIGH severity. This prevents high-risk images from ever reaching the registry or the staging environment.

### 3. Rollback Strategy 

The recovery plan leverages the immutability of containers and the features of Kubernetes.

  Deployment Failure Rollback (Immediate):
    Method:Kubernetes native rollout
    Action: An operator uses the command `kubectl rollout status deployment/fastapi-deployment -n staging`.
    Outcome:Kubernetes immediately reverts the deployment to the last known-good image tag saved in its history.


