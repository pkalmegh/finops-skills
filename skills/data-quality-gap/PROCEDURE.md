# Data Quality Gap

Evaluates datasets for billing anomalies, null values, or formatting inconsistencies before downstream ingestion.

### Preconditions
- Required inputs must exist and pass data-trust verification.

### Steps
1. Parse input data and look for trends or threshold breaches.
2. Evaluate outcomes and document assumptions.
3. Output structured summary according to skill.yaml.
