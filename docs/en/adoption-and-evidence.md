# Adoption and evidence

This guide turns the 13 controls into an assessment for a specific candidate and environment. It does not define a universal score or turn a checklist into certification.

## Adoption flow

1. **Define the candidate:** services, version, features, integrations, data, and environments in scope.
2. **Draw boundaries:** users, tenants, services, providers, tools, agents, stores, and administrative planes.
3. **Choose a profile:** baseline, production, high impact, or critical/regulated. Record why and which conditional controls apply.
4. **Assign owners:** control owner, assessor, exception approver, and release decision owner.
5. **Collect direct evidence:** use a method suited to the requirement and bind results to the exact candidate.
6. **Decide and record:** blockers, unknowns, accepted risk, compensating controls, and validity.
7. **Monitor drift:** changes to build, configuration, dependency, boundary, model, prompt, MCP server, or authorization can invalidate conclusions.

## Minimum evidence record

Copy this template and remove fields that do not apply with a rationale. Use controlled references for large logs or artifacts; do not publish credentials, personal data, or details that create risk.

```text
Assessment ID:
Control ID and edition:
Scope / asset / tenant:
Owner and assessor:
Commit SHA:
Artifact digest:
Environment and relevant configuration:
Method / command / tool and version:
Expected outcome:
Observed outcome:
Evidence reference / digest:
Timestamp and freshness rule:
Status: PASS | FAIL | UNKNOWN | N/A | ACCEPTED RISK
Limitations / residual risk:
Approver and approval reference, if applicable:
Expiry / next review:
```

**A hash does not authenticate origin.** A digest helps identify bytes when compared with a trusted value; signatures and provenance require their own identity, key, issuance process, and verification.

## Validity and freshness

- Bind every result to the code revision, artifact digest, configuration, and environment assessed.
- Define in advance which changes invalidate each evidence type. Changes to authorization, network exposure, critical dependencies, or model version will usually require reassessing the affected control.
- Old evidence can document history; it does not automatically approve a new release.
- Set review frequency according to risk and rate of change. There is no single validity period suitable for every control.
- Preserve origin, date, and context; redact secrets and minimize personal data.

## Release decision

| Gate | Exit question |
|---|---|
| Security | Were applicable controls verified? Are any blockers unmitigated? |
| Quality/correctness | Did functional and authorization requirements pass relevant scenarios? |
| Reliability/recovery | Were failures, migrations, queues, retries, and restores assessed? |
| Privacy/compliance | Were applicable obligations identified and reviewed by the responsible specialists? |
| Artifact/provenance | Does the release artifact match the approved candidate, with origin verifiable to the required level? |
| Accessibility | Are the applicable target and assessment evidence defined? |

Use `READY` only when applicable gates pass and no critical blocker remains. `READY WITH ACCEPTED RISK` requires competent authorization, an owner, rationale, compensating control, limit/expiry, and review. An exception does not waive legal or contractual obligations or a blocker the organization's policy forbids accepting. If proof is missing, use `UNKNOWN` or `NOT READY` under local policy.

## Vulnerability prioritization

Consider technical severity, exploitation likelihood, presence in the [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), actual exposure, asset criticality, impact, and available mitigation. CVSS, EPSS, and KEV answer different questions; do not add them into an arbitrary formula or use a single score as the decision.

## Examples of interpretation

- A scanner with no findings does not prove correct authorization on every route; add negative tests and design review.
- A failing tenant-isolation check is `FAIL` for the assessed control even if other suites pass.
- A restore that has not been run is `UNKNOWN` for recovery; the existence of a backup file is not `PASS`.
- A new artifact version needs evidence bound to its new digest; results for the prior artifact remain historical.
- A control marked `N/A` needs scope and rationale that another reviewer can examine.
