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

# Steps to enable DNS
Deploy your application or service: Before setting up an ingress, you should have your application or service running in your Kubernetes cluster. Make sure that you have created a deployment or a statefulset and a service that expose your application.

Install an ingress controller: An ingress controller is a Kubernetes resource that manages ingress rules and traffic for your cluster. You can install an ingress controller by using a tool like Helm or by manually deploying the necessary resources.

There are several ingress controllers available for Kubernetes, such as Nginx, Traefik, and Istio. Choose one that suits your needs and install it according to its documentation.

Create an ingress resource: Once you have an ingress controller installed in your cluster, you can create an ingress resource to configure routing rules for incoming traffic. The ingress resource defines the hostname and paths that incoming traffic should match in order to be routed to your application or service.

Here's an example of an ingress resource:

yaml
Copy code
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /myapp
            pathType: Prefix
            backend:
              service:
                name: myapp-service
                port:
                  name: http
In this example, the ingress resource defines a rule that routes traffic with the hostname "example.com" and the path "/myapp" to a Kubernetes service called "myapp-service" on port 80.

Note that the nginx.ingress.kubernetes.io/rewrite-target annotation is used to rewrite the URL path so that it matches the path expected by the backend service.

Create a DNS record: Once you have created an ingress resource, you can create a DNS A record that points to the IP address of the ingress controller service.

To find the IP address of the ingress controller service, run the following command:

arduino
Copy code
kubectl get service -n <namespace> <ingress-controller-service-name>
Replace <namespace> with the namespace where your ingress controller is running, and <ingress-controller-service-name> with the name of the ingress controller service.

Once you have the IP address of the ingress controller service, create a DNS A record in your GoDaddy account that points to this IP address. The A record should use the hostname that you defined in your ingress resource.

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