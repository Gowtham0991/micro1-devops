# Tradeoffs and Future Improvements

## Design Logic

The goal of this assessment was to demonstrate production oriented DevOps practices while keeping the solution realistic, maintainable, and aligned with the available implementation time. 
Several advanced capabilities were intentionally deferred in favor of delivering a complete, functional, and testable platform foundation within th deadline.

---

## Deployment Strategy

### Current Approach

GitHub Actions performs build validation, security scanning, image publication, and deployment orchestration (AWS disabled).

### Tradeoff

A traditional CI/CD workflow was selected over GitOps to reduce implementation complexity and focus on core delivery capabilities.

### Future Improvement

**GitOps with ArgoCD**

Introduce ArgoCD to make Git the authoritative source of deployment state, provide stronger deployment traceability, simplify rollback operations, and reduce configuration drift between repositories and running environments.

---

## Scaling Strategy

### Current Approach

The application runs with a fixed number of Kubernetes replicas.

### Tradeoff

Static replica counts provide predictable behavior and simplify demonstration of deployment and availability concepts for the assessment purpose.

### Future Improvement

**Horizontal Pod Autoscaling**

Implement Horizontal Pod Autoscalers (HPA) driven by CPU, memory, or custom application metrics to automatically adapt capacity to changing workload demands while improving resource efficiency.

---

## Observability Strategy

### Current Approach

The solution provides structured logging, health endpoints, and Prometheus-compatible metrics exposure.

### Tradeoff

A lightweight observability foundation was prioritized for assessment demonstratation of monitoring readiness without introducing additional operational components.

### Future Improvement

**Production Observability Platform**

Deploy Prometheus and Grafana to support centralized metrics collection, historical trend analysis, dashboarding, alerting, and service-level objective monitoring. There is scope for OpenTelemetery too.

---

## Secret Management

### Current Approach

Sensitive configuration is stored using Kubernetes Secrets.

### Tradeoff

Kubernetes Secrets provide a simple and portable solution suitable for local development and demonstration environments.

### Future Improvement

**Centralized Secret Management**

Integrate AWS Secrets Manager with the External Secrets Operator to enable centralized secret lifecycle management, automated rotation, improved auditability, and tighter cloud-native security controls.

---

## Distributed Observability

### Current Approach

Application visibility is provided through logs, metrics, and health checks.

### Tradeoff

The current implementation focuses on foundational operational telemetry while minimizing implementation complexity.

### Future Improvement

**OpenTelemetry Distributed Tracing**

Implement OpenTelemetry tracing to enable end-to-end request visibility across services, accelerate root cause analysis, and improve troubleshooting of complex application workflows.

---

## Security Controls

### Current Approach

The platform includes container hardening, non root execution, vulnerability scanning, and Kubernetes-based secret management.

### Tradeoff

Priority was placed on foundational security controls that could be implemented and validated within the assessment scope.

### Future Improvement

**Defense-in-Depth Enhancements**

Implement Kubernetes Network Policies to enforce workload isolation and adopt container image signing and verification to strengthen software supply chain security and deployment integrity.

---

## Conclusion

The implemented solution focuses on delivering a secure, observable, and automated platform foundation. 
Future enhancements would primarily target operational scalability, governance, observability maturity, and advanced security controls while preserving the simplicity and maintainability of the current design.
