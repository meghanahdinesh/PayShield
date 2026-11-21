# PayShield - Payment System on Kubernetes

## About the Project

PayShield is a small payment application I developed to understand how a backend application can be deployed and managed using DevOps tools.

The application is built using Python and Flask. It provides basic payment operations such as creating a payment, validating the amount, generating a transaction ID and checking transaction details.

I used Docker to create the application image and Kubernetes to deploy it. I also configured multiple replicas, health checks and automatic scaling based on CPU usage.

## Tools and Technologies

- Python and Flask
- Docker
- Kubernetes
- YAML
- Kubernetes Metrics Server
- Prometheus
- Grafana
- PowerShell

## Application Features

- Create a payment using a REST API.
- Generate a unique transaction ID.
- Validate payment amounts.
- Handle repeated requests using an idempotency key.
- Check payment details using the transaction ID.
- Provide a health check endpoint.

## Kubernetes Setup

The application is deployed using a Kubernetes Deployment and Service.

Some configurations I used:

- 3 application replicas initially.
- Minimum 3 and maximum 10 replicas through HPA.
- CPU utilization target of 50%.
- Readiness and liveness probes.
- CPU and memory requests and limits.

## Monitoring

I installed Prometheus and Grafana in a separate `monitoring` namespace.

Prometheus is used to collect Kubernetes metrics, and Grafana is used to view the monitoring data.

## Testing

I performed the following tests during development:

| Test | Result |
|---|---|
| API health check | Passed |
| Valid payment request | Passed |
| Missing amount | HTTP 400 |
| Negative amount | HTTP 400 |
| Invalid amount | HTTP 400 |
| Repeated idempotency key | Same transaction returned |
| Kubernetes deployment | 3/3 pods ready |
| Pod deletion test | Kubernetes created a replacement pod |
| HPA | Configured and tested under load |

## What I Learned

While working on this project, I learned how to build a Docker image, deploy an application in Kubernetes, configure services and probes, check resource usage and test automatic scaling.

I also understood how Kubernetes replaces failed pods and how Prometheus and Grafana can be used to monitor a cluster.

## Limitations

This is a simulated payment application. It does not connect to a real payment gateway.

Payment information and idempotency keys are stored in application memory. The data is lost when the application restarts and is not shared between replicas. A database and distributed idempotency mechanism would be needed for a production system.

## Future Improvements

- Add PostgreSQL for persistent payment storage.
- Integrate a real payment gateway.
- Add application logging and alerting.
- Configure a CI/CD pipeline using GitHub Actions.
- Improve the Grafana dashboards.

## Project Details

**Project:** PayShield  
**Category:** DevOps  
**Backend:** Python Flask  
**Deployment:** Docker and Kubernetes  
**Monitoring:** Prometheus and Grafana