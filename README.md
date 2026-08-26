Project Title: End-to-End Dockerized Web Application

A production-oriented Flask web application built step by step to
demonstrate a complete DevOps workflow using Docker, Docker Compose,
PostgreSQL, Nginx, Gunicorn, GitHub Actions, GitHub Container Registry
(GHCR), Prometheus, Grafana, Loki, and alerting.


## Project Overview

The goal of this project is to demonstrate how a simple web application
can evolve into a containerized, observable, and automated application
stack.

The project covers:

-   Application containerization with Docker
-   Multi-container orchestration with Docker Compose
-   PostgreSQL database integration and persistent storage
-   Nginx reverse proxy
-   Gunicorn production application server
-   Automated testing
-   CI/CD with GitHub Actions
-   Docker image publishing with GHCR
-   Application monitoring with Prometheus
-   Grafana dashboards
-   Centralized logging with Loki
-   Application alerting
-   Docker networking and health checks


## Development Versions

### V1 --- Flask Application + Docker

Created the base Flask application and containerized it using Docker.

Key work:

-   Flask application structure
-   Dockerfile
-   Application container
-   Basic API endpoints

### V2 --- Docker Compose + PostgreSQL

Added PostgreSQL and Docker Compose to run the application and database
as separate services.

Key work:

-   PostgreSQL container
-   Flask-to-PostgreSQL communication
-   Docker Compose orchestration
-   Docker internal networking

### V3 --- Persistence + Health Checks

Improved reliability and configuration management.

Key work:

-   PostgreSQL persistent volume
-   Environment variables
-   `.env` configuration
-   Database health check
-   Application health endpoint
-   Service dependencies

### V4 --- Nginx Reverse Proxy

Added Nginx as the public entry point to the application.

Request flow:

``` text
Client -> Nginx :80 -> Flask/Gunicorn :5000 -> PostgreSQL
```

The Flask application no longer needs to be directly exposed to users.

### V5 --- Gunicorn + Container Hardening

Replaced the Flask development server with Gunicorn.

Key work:

-   Gunicorn WSGI server
-   Multiple worker processes
-   Non-root application user
-   Improved Docker image configuration
-   Production-oriented container execution

### V6 --- Automated Testing + GitHub Actions CI

Added automated testing and continuous integration.

Pipeline flow:

``` text
Git Push
   |
   v
GitHub Actions
   |
   +--> Install Dependencies
   +--> Run Tests
   +--> Validate Docker Compose
   +--> Build Containers
   +--> Start Application
   +--> Test Health Endpoint
```

This allows every code change to be automatically validated.

### V7 --- GHCR + Container Delivery

Extended the pipeline to build and publish the production Docker image
to GitHub Container Registry.

Flow:

Git Push
   |
   v
GitHub Actions
   |
   v
Tests
   |
   v
Docker Build
   |
   v
GHCR
   |
   v
Production Docker Compose

The deployment configuration can pull the published application image
instead of rebuilding it directly from source.

### V8 --- Prometheus + Grafana Monitoring

Added application observability using Prometheus and Grafana.

The Flask application exposes metrics through:

/metrics
```

Prometheus scrapes the application metrics and Grafana visualizes them.

Dashboard metrics include:

-   Application status
-   HTTP request count
-   HTTP request rate
-   Average response time

Example PromQL for application status:

 promql
up{job="web"}


Example PromQL for average response time:

 promql
(
  rate(flask_http_request_duration_seconds_sum[5m])
  /
  rate(flask_http_request_duration_seconds_count[5m])
) * 1000


### V9 --- Centralized Logging + Alerting

Added centralized logging and application alerting.

Logging flow:

Application / Container Logs
            |
            v
           Loki
            |
            v
         Grafana


Monitoring alerts can detect application failures using Prometheus
metrics.

Example application-down condition:

 promql
up{job="web"} == 0


This version demonstrates monitoring, troubleshooting, centralized log
analysis, and failure detection.

## Project Structure

end-to-end-dockerized-web-application/
|
|-- webapp/
|   |-- __init__.py
|   |-- main.py
|   `-- routes.py
|
|-- tests/
|
|-- nginx/
|   `-- nginx.conf
|
|-- monitoring/
|   |-- prometheus/
|   |   `-- prometheus.yml
|   |
|   `-- loki/
|       `-- loki-config.yml
|
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|
|-- screenshots/
|
|-- Dockerfile
|-- docker-compose.yml
|-- docker-compose.prod.yml
|-- requirements.txt
|-- .gitignore
`-- README.md


> The exact structure may vary depending on the current implementation.

## Running the Project

### Prerequisites

Install:

-   Docker
-   Docker Compose
-   Git

Verify:

``` bash
docker --version
docker compose version
git --version


### Clone the Repository


git clone <repository-url>
cd end-to-end-dockerized-web-application


### Configure Environment Variables

Create a local `.env` file based on the variables required by
`docker-compose.yml`.

Example variable names:

 env
DB_HOST=db
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password


### Validate Docker Compose


docker compose config
```

### Build and Start

docker compose up -d --build

### Check Containers


docker compose ps

### Test the Application

curl http://localhost/health


Test the API:

curl http://localhost/api/tasks

### View Application Metrics

curl http://localhost/metrics

## Monitoring

Prometheus:

http://localhost:9090


Grafana:


http://localhost:3000


Inside Docker networking, Grafana connects to Prometheus using:

http://prometheus:9090


## Useful Commands

View all service logs:


docker compose logs


Follow application logs:


docker compose logs -f web


Check Nginx logs:


docker compose logs nginx


Check Prometheus logs:


docker compose logs prometheus


Check Grafana logs:


docker compose logs grafana

Stop the stack:


docker compose down


Rebuild:


docker compose up -d --build


## CI/CD

The GitHub Actions workflow automatically performs validation when code
is pushed.

The pipeline includes:

1.  Source checkout
2.  Dependency installation
3.  Automated tests
4.  Docker Compose validation
5.  Docker image build
6.  Application health validation
7.  Authentication with GHCR
8.  Production image publishing

This creates a workflow similar to:

Developer -> GitHub -> GitHub Actions -> GHCR -> Deployment


## Screenshots

Recommended evidence included in the repository:

-   Docker containers running
-   Application health endpoint
-   Nginx reverse proxy verification
-   GitHub Actions CI/CD success
-   GHCR image/package
-   Prometheus target status
-   Flask `/metrics`
-   Grafana monitoring dashboard
-   Centralized logs
-   Grafana alert state



## Key Learning Outcomes

Through this project I gained practical experience with:

-   Building and containerizing Python applications
-   Docker image creation and troubleshooting
-   Multi-container application architecture
-   Docker networking and service discovery
-   Persistent database storage
-   Reverse proxy configuration
-   Production application serving with Gunicorn
-   CI/CD pipeline development
-   Container registry workflows
-   Debugging GitHub Actions pipelines
-   Prometheus metrics and PromQL
-   Grafana dashboards
-   Centralized logging
-   Alert configuration
-   Troubleshooting container connectivity and service failures

## Future Improvements

Potential future enhancements include:

-   HTTPS/TLS
-   Automated PostgreSQL backup and recovery
-   Improved secrets management
-   Container vulnerability scanning
-   Cloud deployment
-   Infrastructure as Code
-   Kubernetes deployment
-   Advanced alert notifications
-   Load balancing and high availability

## Project Status

The project demonstrates the evolution of a basic Flask application into
an end-to-end Dockerized application with CI/CD and observability.

## Author

Mr. Sayantan Kar

Interested in DevOps, Cloud, Linux, containerization, CI/CD, monitoring,
and infrastructure automation.
