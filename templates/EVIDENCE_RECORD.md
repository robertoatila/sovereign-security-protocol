# SSP-12 Evidence Record / Registro de Evidências

This document registers reproducible evidence required for an SSP-12 Release Assurance Gate (`READY`, `NOT READY`, or `READY WITH ACCEPTED RISK`).

---

## 1. Candidate Identification (Freshness Binding)

* **Repository / System:** `org/repo-name`
* **Commit SHA:** `[e.g. 7f3a8b2c1d4e5f60718293a4b5c6d7e8f9012345]`
* **Artifact Digest (SHA-256):** `sha256:[hash]`
* **Target Environment:** `[Staging / Production / sovereign-node]`
* **Evaluation Timestamp:** `YYYY-MM-DDTHH:MM:SSZ`
* **Evaluator / Responsible Identity:** `security-lead@domain.tld`

---

## 2. Controls Assessment Matrix

| Control ID | Minimum Level | Observed Status | Evaluated Method / Tool | Evidence Artifact / Link |
|---|---|---|---|---|
| **SSP-01** | L1 | `PASS` / `FAIL` / `N/A` | Architecture Review / Inventory | `docs/architecture.md#scope` |
| **SSP-02** | L2 | `PASS` / `FAIL` / `N/A` | Threat Model STRIDE / Abuse test | `threat-model.json` |
| **SSP-03** | L2 | `PASS` / `FAIL` / `N/A` | Automated Integration / AuthZ tests | `test-results/authz.xml` |
| **SSP-04** | L2 | `PASS` / `FAIL` / `N/A` | RLS inspection & Data classification | `schema/rls-audit.log` |
| **SSP-05** | L2 | `PASS` / `FAIL` / `N/A` | Fail-closed negative configuration test | `ci/fail-closed-test.log` |
| **SSP-06** | L2 | `PASS` / `FAIL` / `N/A` | API negative payloads & injection test | `ci/dast-zap-report.json` |
| **SSP-07** | L2 | `PASS` / `FAIL` / `N/A` | SBOM & Dependency audit (KEV/EPSS) | `build/sbom.spdx.json` |
| **SSP-08** | L2 | `PASS` / `FAIL` / `N/A` | Network firewall / Egress rules audit | `infra/network-audit.txt` |
| **SSP-09** | L3 | `PASS` / `FAIL` / `N/A` | Agent Manifest & Tool permission audit | `manifests/agent.manifest.json` |
| **SSP-10** | L2 | `PASS` / `FAIL` / `N/A` | Backup restore verification log | `reports/restore-drill-2026.log`|
| **SSP-11** | L2 | `PASS` / `FAIL` / `N/A` | Structured audit trail & redaction test| `logs/sample-redacted.json` |
| **SSP-12** | L3 | `PASS` / `FAIL` / `N/A` | Commit & Artifact hash verification | `build/provenance.attestation` |
| **SSP-13** | L1 | `PASS` / `FAIL` / `N/A` | Compliance register & A11y report | `docs/compliance-matrix.csv` |

---

## 3. Exceptions & Compensating Controls

*If any control is marked `ACCEPTED RISK`, document the formal exception reference:*

- **Control ID:** `SSP-XX`
- **Exception ID:** `EXC-2026-001` (Link: [`templates/SECURITY_EXCEPTION.md`](SECURITY_EXCEPTION.md))
- **Compensating Control:** `[Description of additional mitigations in place]`
- **Expiry Date:** `YYYY-MM-DD`

---

## 4. Final Release Decision

- [ ] **READY** (All applicable controls `PASS`, zero blockers)
- [ ] **READY WITH ACCEPTED RISK** (Blocker covered by approved, unexpired exception)
- [ ] **NOT READY** (Blocker present, missing evidence, or stale candidate)

**Authorized Approver Signature / Digest:**
`Signature: [Ed25519 / GPG / Approved PR Link]`
