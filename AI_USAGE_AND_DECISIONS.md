# AI Tools Used

* ChatGPT (architecture design diagram, troubleshooting, documentation)
* Claude (reviewing CI/CD workflows and Kubernetes manifests)

---

# Prompts Used

### Prompt
Design a production style lightweight FastAPI application

#### WhyI used it
* To quickly establish a clean application foundation for the assessment.
* To identify the minimum components needed to demonstrate containerization, Kubernetes deployment, CI/CD, observability, and security practices.
* To accelerate initial project setup so I could focus more on infrastructure and platform engineering rather than application development.

#### What I Changed
* Selected a lightweight FastAPI service with health and metrics endpoints instead of a more complex application architecture because my own moviematch application required more complex adjustemnts that were not needed for this assignment).
* Added structured JSON logging to improve operational visibility.
* Integrated Prometheus metrics exposure for monitoring readiness.

---

### Prompt
Review this Dockerfile from a production security perspective. Identify risks related to privilege escalation, image size, dependency management, attack surface, and runtime security.

#### WhyI used it
* To identify scopes for container hardening.

### What I Changed
 * Added a non-root user.
 * Reduced unnecessary layers.
 * Kept the image intentionally simple to improve maintainability.

---

### Prompt
Assume this FastAPI service will run in a multi tenant Kubernetes cluster supporting customer facing workloads.
Perform a production readiness review and identify single points of failure, scaling bottlenecks, deployment risks, resource contention scenarios, and operational failure modes.
Recommend mitigations and explain the tradeoffs of each.

#### Why I used it
* To identify potential failure scenarios early and reduce deployment risk.
  
#### What I Changed
* Added multiple replicas.
* Implemented rolling update strategy.
* Added readiness and liveness probes.
* Established resource requests and limits.
* Added deployment validation checks.

---

### Prompt

Review my Kubernetes deployment architecture and evaluate whether it can support zero downtime deployments during node failures, pod crashes, application upgrades, and cluster maintenance events. 
Identify risks and recommend controls that improve service availability without introducing unnecessary operational complexity.

#### Why I used it
* To validate service availability during deployments and infrastructure failures.
* To ensure deployment patterns aligned with production reliability expectations.

#### What I Changed
* Added rolling deployment support.
* Balanced resiliency improvements against assessment scope and complexity.

---

### Prompt
Review my CI/CD pipeline as if it supports multiple engineering teams deploying to production daily. 
Identify potential release bottlenecks, unsafe deployment patterns, change management risks, rollback challenges, and areas where deployment velocity could negatively impact reliability.

#### Why I used it
* To evaluate the pipeline from a release engineering perspective.
* To ensure the pipeline balances delivery speed with production stability.

#### What I Changed
* Structured the pipeline into distinct validation and deployment stages.
* Added deployment verification steps before considering releases successful.
* Improved workflow organization to make failures easier to diagnose.
* Documented rollback and recovery considerations for future enhancements.

---

### Prompt
Assume I am the on call engineer responsible for this CI/CD platform. 
Analyze failure scenarios involving runner outages, registry failures, deployment interruptions, partial releases, and infrastructure instability. 
Recommend controls that improve recovery time and operational resilience.

#### Why I used it
* To evaluate the pipeline under real world failure conditions and identify weaknesses that may only appear during incidents.
* To improve reliability and troubleshooting capabilities before production use.
  
#### What I Changed
* Added explicit deployment status verification.
* Improved visibility into pipeline execution outcomes.
* Structured workflows to fail fast when validation checks fail.
* Added safeguards that prevent deployments from proceeding when prerequisite stages are unsuccessful.

---

#### Prompt
Assume this Terraform code is responsible for provisioning critical production infrastructure.
Analyze how infrastructure changes could impact service availability, deployment safety, rollback capabilities, and operational stability.
Recommend controls that reduce the risk of infrastructure related outages.

#### Why I used it
* To understand the operational impact of infrastructure changes before deployment.

#### What I Changed
* Validated infrastructure definitions before deployment.
* Incorporated infrastructure review checkpoints into the workflow.

---

#### Prompt
Review my Terraform architecture as if it will be managed by multiple engineers over several years.
Identify maintainability risks, module design issues, state management concerns, dependency coupling, and areas that may create operational debt as the infrastructure grows.

#### Why I used it
* To evaluate the long term maintainability of the infrastructure code.
* To identify design decisions that could become difficult to manage as the environment expands.

#### What I Changed
* Applied consistent naming and resource organization standards.

---

#### Prompt
Perform an infrastructure governance review of this Terraform implementation.
Evaluate resource standardization, tagging strategy, environment consistency, access control boundaries, and the ability to enforce organizational policies at scale.

#### Why I used it
* To assess whether the infrastructure could be managed consistently across environments.
* To identify governance gaps that often emerge as teams and cloud resources grow.

#### What I Changed
* Applied a consistent resource naming convention.
* Structured configurations to support future environment expansion.

---

#### Prompt
Perform a security architecture review of this application and deployment model assuming the source code repository, CI/CD platform, container registry, and Kubernetes cluster are all potential attack surfaces.
Identify the most likely paths an attacker could use to reach production workloads and recommend controls that reduce risk while maintaining developer productivity.

#### Why I used it
* To identify risks across the software delivery lifecycle.

---

#### Prompt
Create a production architecture diagram showing the complete flow from source control through CI/CD, containerization, image registry, Kubernetes deployment, and application runtime.
Identify all major components, deployment boundaries, and operational touchpoints that should be represented for a technical design review.

#### Why I used it
* To validate that all major components of the solution were properly represented.
* To ensure the architecture could be easily understood by reviewer.
* To not waste time on manual image creation using native tools

#### What I Changed
* Tailored the diagram to reflect the implemented architecture rather than a theoretical production environment.

---

#### Prompt
Assume this service will eventually support business critical workloads with defined uptime and operational objectives.
Review the current monitoring and security controls and identify what information would be required to establish service level indicators, detect abnormal behavior, investigate incidents, and demonstrate operational compliance during audits.

#### Why I used it
* To evaluate the solution from both an operational excellence and governance perspective.

---

#### Prompt
The Kubernetes deployment completed successfully, but the application is not accessible through the expected endpoint.

#### Outcome
Claude helped me with the issue by validating each layer independently using kubectl logs, kubectl describe, pod health checks, service definitions, and port mappings. 
This confirmed that the application was running correctly and allowed traffic flow to be traced from the container through the Kubernetes service configuration until the root cause was identified.

---

#### Prompt
The /metrics endpoint expected for observability is returning HTTP 404.

#### Outcome
The application code and routing configuration were reviewed first, confirming that Prometheus metrics had not yet been exposed by the application. 
Metrics instrumentation was then added, the endpoint was registered correctly, and the updated container image was redeployed and validated successfully.

---

#### Prompt
(In my second appllication) GitHub Actions linting fails with a package export error even though the project dependencies appear to be installed correctly.

#### Outcome
The failure was traced to ESLint configuration compatibility rather than application code. 
The configuration was updated to align with the current ESLint version requirements, eliminating the package export error and restoring successful pipeline execution.

---

#### Prompt
A CI/CD workflow succeeds locally but fails when executed by the GitHub Actions runner.

#### Outcome
The workflow execution environment was analyzed for differences in installed dependencies, runner configuration, authentication context, and execution paths. 
This isolated the failure to environment specific configuration rather than application behavior and enabled the workflow to execute consistently across environments.

---

#### Prompt
Terraform validation succeeds, but Terraform plan fails during provider authentication.

#### Outcome
Terraform syntax and configuration were verified successfully through validation, narrowing the investigation to provider authentication. 
The failure was ultimately traced to invalid AWS credentials, confirming that the infrastructure code itself was not responsible for the plan failure.

---

#### Prompt
A newly deployed container image does not appear to contain the latest application changes.

#### Outcome
The image lifecycle was validated end-to-end by reviewing build outputs, image tags, registry artifacts, and deployment references. 
This ensured the correct image version was published, pulled, and deployed during rollout.

---

#### Prompt
The Kubernetes deployment reports success, but application changes are not reflected in running workloads.
How would you verify whether a rollout actually replaced the existing pods and deployed the intended application version?

#### Outcome
Rollout status, deployment revisions, and pod recreation events were reviewed to verify that Kubernetes had applied the new deployment. 
Explicit rollout verification was incorporated into the deployment process to ensure future releases could be validated automatically.

---

# Places my engineering judgement overrode AI suggestions

#### Infrastructure Scope

##### AI Suggested
* Multi region deployment
* Managed databases
* Full monitoring stack
* WAF integration
* GitOps tooling

##### What I Did

* Focused on infrastructure that could be realistically implemented, tested, and demonstrated within the assessment timeframe.
* Prioritized Kubernetes, CI/CD, security controls, observability, and Terraform foundations over advanced platform features.

---

#### CI/CD Design

##### AI Suggested

* Multiple deployment environments
* Canary deployments
* Automated rollback workflows

##### What I Did

* Implemented a streamlined pipeline focused on code quality, testing, container builds, security scanning, and deployment validation.
* Chose simplicity and reliability over additional deployment complexity.

---

#### Observability

##### AI Suggested

* Prometheus
* Grafana
* Alertmanager
* Distributed tracing

##### What I Did

* Implemented health checks, structured logging, and metrics exposure as a monitoring foundation.
* Deferred a full observability stack to keep the solution lightweight and maintainable for the assessment.

---

#### Secrets Management

##### AI Suggested

* AWS Secrets Manager integration

##### What I Did

* Used Kubernetes Secrets for implementation and testing.

---

Overall, AI was used for research, reviews, troubleshooting, and fixing grammatical mistakes on the documentation.
Final architecture decisions, security controls, infrastructure design, and implementation tradeoffs were based on my engineering judgment as needed for the goals of this assessment.



