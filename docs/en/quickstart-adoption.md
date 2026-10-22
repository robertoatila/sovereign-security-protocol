# Quickstart Adoption Guide for SSP v13.4

This guide assists engineering teams, architects, and autonomous agent builders in progressively adopting the **Sovereign Security Protocol (SSP)**.

---

## 1. Core Principles

1. **Fail-Closed Behavior:** Missing configurations, invalid tokens, or network disconnects default strictly to `DENY`.
2. **Evidence Freshness:** An authorization or audit decision binds to an **exact git commit SHA**, **artifact digest**, and **environment**. Stale evidence from previous builds does not authorize current releases.
3. **Externalized Authority:** AI models, LLM prompts, and MCP servers never grant access authority; security boundaries and policy enforcement reside entirely in external deterministic runtimes.
4. **Governed Risk Exceptions:** `ACCEPTED RISK` requires an authenticated owner, rigorous technical rationale, compensating controls, and a strict expiration date.

---

## 2. Three-Phase Adoption Roadmap

### Phase 1: Day 1 — Sovereign Baseline (L1)
*Goal: Establish system inventory, boundaries, and clear ownership.*

- [ ] **Scope and Asset Mapping (SSP-01):** Catalog repositories, services, databases, and accountable owners.
- [ ] **Dependency Pinning (SSP-07):** Commit reproducible lockfiles (`package-lock.json`, `poetry.lock`, etc.).
- [ ] **Audit Insecure Defaults (SSP-05):** Eliminate default passwords, demo tokens, and test credentials.
- [ ] **Compliance Baseline (SSP-13):** Document regulatory and contractual obligations (GDPR, LGPD, SOC 2).

### Phase 2: Week 1 — Secure Engineering & CI Gates (L2)
*Goal: Deterministic validation and automated negative tests.*

- [ ] **Trust Boundaries & Threat Modeling (SSP-02):** Map exposed endpoints, data flows, and untrusted inputs.
- [ ] **Granular Authorization (SSP-03):** Enforce principal/action/resource verification (prevent BOLA/IDOR).
- [ ] **Data Isolation & RLS (SSP-04):** Enable data encryption at rest and in transit; activate Row-Level Security.
- [ ] **Strict Input Validation (SSP-06):** Type-check and sanitize inputs at application and webhook boundaries.
- [ ] **Infrastructure Segregation (SSP-08):** Keep databases and management planes isolated from the public internet.
- [ ] **Redacted Audit Logging (SSP-11):** Implement structured audit logging without leaking PII or credentials.

### Phase 3: Month 1 — Contained AI, Disaster Recovery & Release Gates (L3)
*Goal: Agent containment and verifiable release decision.*

- [ ] **Agentic AI & MCP Containment (SSP-09):**
  - Scope tools, permissions, and egress using [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json).
  - Enforce human-in-the-loop approval bound to plan/action digests for destructive or high-cost actions.
  - Test agent timeouts, cost budgets, and immediate kill switches.
- [ ] **Disaster Recovery Exercise (SSP-10):** Execute and record empirical backup restore drills with verified RTO/RPO.
- [ ] **Formal Release Assurance Gate (SSP-12):** Execute `python scripts/ssp_tool.py gate -f <evidence-record.json>` prior to production deployments.

---

## 3. Local CLI Tooling

Verify repository integrity, crosswalk mapping, and evidence packages locally:

```bash
# Validate links, JSON schemas, and SSP crosswalk
python scripts/ssp_tool.py validate

# View control matrix and minimum evidence thresholds
python scripts/ssp_tool.py matrix

# Evaluate SSP-12 Release Assurance Gate
python scripts/ssp_tool.py gate --file templates/sample_evidence_record.json
```

---

## 4. Operational Templates

- Evidence Record Template: [`templates/EVIDENCE_RECORD.md`](../../templates/EVIDENCE_RECORD.md)
- Security Exception Request: [`templates/SECURITY_EXCEPTION.md`](../../templates/SECURITY_EXCEPTION.md)
- Agent & MCP Containment Manifest: [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json)
