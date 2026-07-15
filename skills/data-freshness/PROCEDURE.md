# Data Freshness

Verifies that ingestion pipelines are current and flags delays beyond the service-level agreement.

### Preconditions
- Required inputs must exist and pass data-trust verification.

### Steps
1. Parse input data and look for trends or threshold breaches.
2. Evaluate outcomes and document assumptions.
3. Output structured summary according to skill.yaml.
