# SSP Community Edition 0.1.0 — 13-Control Summary (English)

> **Need the complete protocol in English?** [Open the complete automatic English community translation](../../protocol/v13.4/SSP_v13.4_FULL_EN_COMMUNITY.md). It is a review draft, not canonical, and needs human technical review. The [Portuguese source (PT-BR)](../../protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md) is the reference for resolving wording differences. This page remains a separate 13-control community summary.

**Basis:** Sovereign Security Protocol v13.4.0. **Status of this edition:** community proposal, not canonical.

This edition translates and reorganizes the source into smaller, traceable requirements. The IDs below belong to this edition; they are not IDs claimed by source v13.4. See [provenance](../research/provenance.md), the [crosswalk](../../control-crosswalk.csv), and the [v13.4 review](../research/revisao-v13.4.md).

## Normative language

- **MUST**: required when the control applies.
- **SHOULD**: recommended; an exception needs a rationale, owner, and review date.
- **MAY**: permitted option, with no claim of equivalence or certification.
- `N/A` requires a scope rationale. Accepted risk is a governed decision, not a test result.

## The 13 controls

### SSP-01 — Scope, assets, and accountability

The system MUST declare scope, boundaries, important assets, data classes, owners, and external dependencies. A risk decision owner MUST be assigned, and the assessment MUST be reviewed when architecture, data, or system effects change.

**Minimum evidence:** dated scope/inventory or diagram, owner, dependencies, and scope approval.

### SSP-02 — Threat modeling and trust boundaries

The system MUST identify actors, attack surfaces, trust boundaries, and abuse cases proportionate to impact. Repositories, prompts, tool results, retrieved documents, memory, and external responses MUST be treated as untrusted data until validated.

**Minimum evidence:** versioned threat model, attack paths, and mapped controls.

### SSP-03 — Identity and authorization

The system MUST authenticate principals where needed and authorize each action against the correct resource and tenant. Identity, network location, UUID, JWT, session, or group membership MUST NOT alone be treated as sufficient authorization. Effective permissions MUST follow least privilege and appropriate expiry.

**Minimum evidence:** principal/action/resource matrix, negative access checks, and privilege approval records.

### SSP-04 — Data protection and privacy

The system MUST minimize collection, retention, copying, and exposure; protect data in transit and at rest according to risk; and define access, use, retention, deletion, and incident response. Legal and contractual requirements MUST be identified for the relevant jurisdiction and use case.

**Minimum evidence:** data inventory/classification, data-flow map, and approved retention/deletion policy.

### SSP-05 — Secure configuration and fail-closed behavior

Critical controls MUST fail safely when configuration, authentication, integrity, or authorization is missing or invalid. Default and example credentials MUST NOT remain active in production. A proxy, WAF, private network, firewall, scanner, or hidden configuration does not replace authorization.

**Minimum evidence:** effective configuration and a check for missing/invalid critical configuration.

### SSP-06 — Inputs, APIs, and business logic

The server MUST validate inputs, authorization, state, and business invariants. Client-provided values, caches, queues, webhooks, and model output MUST NOT be authoritative for payment, tenant, permission, or privileged state. Resource limits, replay protection, and abuse defenses MUST be applied where relevant.

**Minimum evidence:** negative and abuse/regression cases for critical actions and rules.

### SSP-07 — Dependencies, origin, and build integrity

The system MUST track the origin of relevant dependencies and artifacts, use reproducible resolution where available, and review vulnerabilities in the context of exploitation, exposure, and impact. A hash/Merkle tree identifies bytes against a trusted root; by itself it does not prove author, producer, or legitimacy. SLSA claims MUST match the version, track, and level actually verified.

**Minimum evidence:** lockfiles, SBOM where applicable, verified provenance/signatures, and a remediation policy.

### SSP-08 — Infrastructure and isolation

Services, databases, and administrative planes MUST be private by default and exposed only for documented need. Network rules MUST be tested on the actual path; a subnet, VLAN, VPN, or local bind alone is not authorization or proof of isolation.

**Minimum evidence:** zone diagram, effective rules, and proof of allowed and denied connectivity.

### SSP-09 — Agentic AI, memory, and MCP

Models, prompts, tools, MCP servers, repositories, memory, and remote results MUST be treated as trust boundaries. A model does not grant authority: policy outside the model MUST validate principal, tool, resource, tenant, action, and effect. Agents MUST receive only the capabilities, data, credentials, network access, time, and budget they need.

Human approval for a risky action MUST bind approver identity, exact action and targets, plan/digest, risk, budget, expiry, and operation ID. Material changes require fresh approval. Persistent memory MUST retain source, scope/tenant where applicable, integrity, review, and deletion handling. Risky automation MUST have a testable containment and stop procedure.

**Minimum evidence:** capability matrix, injection/abuse checks, plan-bound approval, and containment exercises.

### SSP-10 — Reliability, change, and recovery

Changes, queues, and retries MUST account for duplicate effects, partial failure, and migrations. Backups MUST be protected and restores MUST be exercised at a frequency set by impact. RTO/RPO and recovery strategy MUST be explicit for systems that depend on them.

**Minimum evidence:** change/recovery plan, restore result, and effects reconciliation.

### SSP-11 — Logs, detection, and response

Relevant events MUST support investigation and correlation without recording secrets or unnecessary data. Alerts, severity, containment, communication, evidence preservation, and recovery MUST have owners and workable procedures.

**Minimum evidence:** redacted samples, detection rules, and a response exercise with results and gaps.

### SSP-12 — Verification and release decision

A `PASS` MUST cite criteria, method, and current evidence bound to the code, artifact, configuration, and environment assessed. Evidence from another commit or digest does not approve the current candidate. Scanners and coverage are partial signals; architectural, human, or legal requirements may need their own review.

The final decision MUST be `READY`, `NOT READY`, or `READY WITH ACCEPTED RISK`. `READY` requires applicable controls to pass and no critical blockers. Accepted risk requires an authorized owner, rationale, compensating controls, expiry, and recorded approval.

**Minimum evidence:** a package with control IDs, commit SHA, artifact digest, environment, tool version, command/method, timestamps, expected/observed outcomes, and a verifiable reference.

### SSP-13 — Accessibility, obligations, and continuous improvement

The project MUST declare applicable legal, contractual, and accessibility obligations; MUST record source, version, jurisdiction, owner, and review date. Awareness documents MUST NOT be presented as exhaustive verification lists. A standards change, threat, incident, or architecture change MUST trigger a proportionate review.

**Minimum evidence:** applicability matrix and a versioned record of reviews and decisions. For user interfaces, select an explicit accessibility target—for example WCAG 2.2 AA—and record the assessment method and exceptions.

## Applicability and result

Use the baseline for any system with data or users. Add production, high-impact, and critical/regulated profiles as risk and obligations require. A profile is not a security score, and `N/A` is not a shortcut: document the asset, boundary, and rationale.

| State | Meaning |
|---|---|
| `PASS` | The criterion is satisfied with sufficient current evidence. |
| `FAIL` | The criterion is not satisfied or evidence contradicts it. |
| `UNKNOWN` | Scope, mechanism, or evidence is insufficient to decide. |
| `N/A` | Not applicable with technical rationale and suitable approval. |
| `ACCEPTED RISK` | Time-limited exception with an owner and compensating control. |

`PENDING LEGAL` and `PENDING EXTERNAL ACTION` describe open work; they are not passing results. A change to the artifact, environment, configuration, or boundary can invalidate earlier evidence. Set the validity rule before assessment.

## The nine source domains

1. Governance, architecture, and secure SDLC.
2. Identity, authentication, authorization, sessions, and anti-abuse.
3. Web, API, injection, and business logic.
4. Data, databases, RLS, privacy, and compliance.
5. Cloud, infrastructure, secrets, and supply chain.
6. Reliability, resilience, performance, and disaster recovery.
7. Logging, audit, detection, and incident response.
8. Testing, quality engineering, and accessibility.
9. AI, RAG, agents, and MCP.

See the [crosswalk](../../control-crosswalk.csv) for mappings to source chapters.
