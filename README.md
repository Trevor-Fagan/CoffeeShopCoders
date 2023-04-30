# CoffeeShopCoders
You know, for coffee shop coders

# The Plan
A website that is built to explain how it is built.
Potential to expand to articles and coding related content.
Perhaps guest videos and lecture from Google Student Developer Clubs leaders.

1. Configure GCS bucket to work as a helm chart repository
2. Create CI to work for building and publishing frontend/backend images
3. Figure out how to connect nginx/nginx ingress controller and allow frontend/backend communication
4. Configure DNS records to start serving content to coffeeshopcoders.com

# Frontend
- React
- Daisy UI
- Tailwind CSS

# Backend
- Python
- Flask

# CI/CD
- Github actions
- Helm
- Docker

# Metrics + Monitoring
- Prometheus
- Grafana

# Persistence
- AWS Elastic Container Registry
- AWS MySQL RDS
- Prometheus AWS DB
- Google Cloud buckets for Helm chart repository

# Other
- Hosting: Digital Ocean
- DNS Config + Domain: GoDaddy
- Search: Elasticsearch

# Potential
- Change logs
- DB migration tool (maybe AWS solution?)
- Load simulation
- CDN
- Self hosted linux runner for Github Actions (Ansible for Infrastructure as Code)
- Caching (Redis)