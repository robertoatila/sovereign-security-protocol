# Quickstart Adoption Guide for SSP v13.4

This guide helps engineering teams, architects, and autonomous agent builders progressively adopt the **Sovereign Security Protocol (SSP)** across **any system**, using only this repository.

---

## 1. Core Principles

1. **Fail-Closed Behavior:** Missing configurations, invalid tokens, or network disconnects default strictly to `DENY`.
2. **Evidence Freshness:** An authorization or audit decision binds to an **exact git commit SHA**, **artifact digest**, and **environment**. Stale evidence from previous builds does not authorize current releases.
3. **Externalized Authority:** AI models, LLM prompts, and MCP servers never grant access authority; security boundaries and policy enforcement reside entirely in external deterministic runtimes.
4. **Governed Risk Exceptions:** `ACCEPTED RISK` requires an authenticated owner, rigorous technical rationale, compensating controls, and a strict expiration date.

---

## 2. 60-Second Adoption on Any System

With Python 3.10+ (standard library only, zero external packages), bootstrap and audit any local project:

```bash
# 1. Generate tailored .ssp/ scaffolding for the detected stack in your target project
python ssp.py init --target /path/to/your-system --lang en

# 2. Audit the 7 Security Layers on your target project
python ssp.py scan --target /path/to/your-system --lang en

# 3. Inspect stack hardening blueprints (api | database | docker | ai-mcp | cli)
python ssp.py blueprint --stack api --lang en

# 4. Enforce the SSP-12 Release Assurance Gate prior to production deployment
python ssp.py gate --file /path/to/your-system/.ssp/evidence-record.json --commit <git-sha>
```

To enforce SSP in GitHub Actions pipelines, add `robertoatila/sovereign-security-protocol@main` via [`action.yml`](../../action.yml). For side-by-side **❌ Vulnerable vs. ✅ Hardened** code patterns, read [`layers-by-system.md`](layers-by-system.md).

---

## 3. Three-Phase Adoption Roadmap

### Phase 1: Day 1 — Sovereign Baseline (L1)
*Goal: Establish system inventory, boundaries, and clear ownership.*

- [ ] **Scope and Asset Mapping (SSP-01):** Catalog repositories, services, databases, and accountable owners (`python ssp.py init`).
- [ ] **Dependency Pinning (SSP-07):** Commit reproducible lockfiles (`package-lock.json`, `poetry.lock`, `go.sum`, `Cargo.lock`).
- [ ] **Audit Insecure Defaults (SSP-05):** Eliminate default passwords, demo tokens, and test credentials (`python ssp.py scan`).
- [ ] **Compliance Baseline (SSP-13):** Document regulatory and contractual obligations (GDPR, LGPD, SOC 2).

### Phase 2: Week 1 — Secure Engineering & CI Gates (L2)
*Goal: Deterministic validation and automated negative tests.*

- [ ] **Trust Boundaries & Threat Modeling (SSP-02):** Map exposed endpoints, data flows, and untrusted inputs.
- [ ] **Granular Authorization (SSP-03):** Enforce principal/action/resource verification (prevent BOLA/IDOR).
- [ ] **Data Isolation & RLS (SSP-04):** Enable data encryption at rest and in transit; activate Row-Level Security.
- [ ] **Strict Input Validation (SSP-06):** Type-check and sanitize inputs at application and webhook boundaries.
- [ ] **Infrastructure Segregation (SSP-08):** Bind databases and management planes to `127.0.0.1` / private networks.
- [ ] **Redacted Audit Logging (SSP-11):** Implement structured audit logging without leaking PII or credentials.

### Phase 3: Month 1 — Contained AI, Disaster Recovery & Release Gates (L3)
*Goal: Agent containment and verifiable release decision.*

- [ ] **Agentic AI & MCP Containment (SSP-09):**
  - Scope tools, permissions, and egress using [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json).
  - Enforce human-in-the-loop approval bound to plan/action digests for destructive or high-cost actions.
  - Test agent timeouts, cost budgets, and immediate kill switches.
- [ ] **Disaster Recovery Exercise (SSP-10):** Execute and record empirical backup restore drills with verified RTO/RPO.
- [ ] **Formal Release Assurance Gate (SSP-12):** Execute `python ssp.py gate -f <evidence-record.json>` prior to production deployments.

---

## 4. Verifying Protocol Repository Integrity

```bash
# Full diagnostic (canonical SHA-256, links, Canvas, JSON Schema, and EN/PT parity)
python ssp.py --doctor

# View the 13-control matrix and minimum evidence thresholds
python ssp.py matrix --lang en
```

---

## 5. Operational Templates & Guides

- Practical Layers by System (❌ vs ✅): [`docs/en/layers-by-system.md`](layers-by-system.md)
- Ecosystem & 50k+★ Reference Map: [`docs/en/ecosystem-and-50k-references.md`](ecosystem-and-50k-references.md)
- Evidence Record Template: [`templates/EVIDENCE_RECORD.md`](../../templates/EVIDENCE_RECORD.md)
- Security Exception Request: [`templates/SECURITY_EXCEPTION.md`](../../templates/SECURITY_EXCEPTION.md)
- Agent & MCP Containment Manifest: [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json)
