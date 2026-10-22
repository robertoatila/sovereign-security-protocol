# Sovereign Security Protocol (SSP)

[![CI](https://github.com/robertoatila/sovereign-security-protocol/actions/workflows/ci.yml/badge.svg)](https://github.com/robertoatila/sovereign-security-protocol/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/SSP%20Base-v13.4.0-blue.svg)](protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md)
[![Edition](https://img.shields.io/badge/Community%20Edition-0.2.0-green.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

**Language:** [Português (PT-BR)](README.pt-BR.md) · 🇬🇧 English

---

## READ THE FULL PROTOCOL

**[Open the complete SSP v13.4.0 in Portuguese (Reference)](protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md)** — unabridged text, reproduced from the versioned source.

The source document declares canonical status. That status applies to the source repository and original commit; this repository provides a reading copy, audit tooling, and machine-readable specification without declaring new canonical authority.

---

## English Edition Contents

- **Full protocol translated into English:** [Community review draft](protocol/v13.4/SSP_v13.4_FULL_EN_COMMUNITY.md). An automated draft pending human technical review.
- [Three-Phase Quickstart Adoption Guide — English](docs/en/quickstart-adoption.md)
- [13-control community summary — English](docs/en/protocol.md)
- [Adoption and evidence — English](docs/en/adoption-and-evidence.md)
- [Agents, J.A.R.V.I.S., and Obsidian — English](docs/en/agentic-jarvis-obsidian.md)

The Portuguese source text remains the authoritative reference for resolving discrepancies.

---

## Start Here

- **[Three-Phase Quickstart Adoption Guide](docs/en/quickstart-adoption.md)** — Practical roadmap (Day 1, Week 1, Month 1).
- **[13 Controls Community Summary](docs/en/protocol.md)** — Normative control definitions SSP-01 through SSP-13.
- **[Adoption and Evidence](docs/en/adoption-and-evidence.md)** — Freshness principles and evidence levels L0 through L3.
- **[Agents, J.A.R.V.I.S., and Obsidian](docs/en/agentic-jarvis-obsidian.md)** — External authority, containment, and MCP boundary model.
- **[Machine-Readable Controls (JSON)](protocol/v13.4/ssp-controls.json)** · [JSON Schema](schema/ssp-control.schema.json).
- **[Traceability crosswalk to SSP v13.4 source chapters](control-crosswalk.csv)**.
- **[Obsidian Visual Index](00%20-%20SSP%20Home.md)** · **[Canvas](SSP-13.4.canvas)**.
- **Operational Templates:**
  - [Evidence Record](templates/EVIDENCE_RECORD.md)
  - [Security Exception Request](templates/SECURITY_EXCEPTION.md)
  - [Agent & MCP Containment Manifest](templates/AI_AGENT_MANIFEST.json)
- [Full protocol provenance and license](protocol/v13.4/NOTICE.md).
- [References and v13.4 review](docs/research/references.md) · [proposed enhancements](docs/research/revisao-v13.4.md).

---

## Tooling & Verification Engine (`scripts/ssp_tool.py`)

A sovereign, zero-external-dependency CLI (Python standard library only):

```bash
# 1. Validate markdown links, Canvas nodes, crosswalk, and JSON schemas
python scripts/ssp_tool.py validate

# 2. Display the 13 controls summary matrix and evidence thresholds
python scripts/ssp_tool.py matrix

# 3. Verify documentation parity across PT-BR and EN
python scripts/ssp_tool.py check-parity

# 4. Evaluate an SSP-12 Release Assurance Gate
python scripts/ssp_tool.py gate --file templates/sample_evidence_record.json
```

---

## What was improved in Community Edition `0.2.0`

- **Machine-Readable Specification:** All 13 controls structured in [`protocol/v13.4/ssp-controls.json`](protocol/v13.4/ssp-controls.json) and validated by [`schema/ssp-control.schema.json`](schema/ssp-control.schema.json), with mappings to OWASP ASVS, NIST SP 800-53, CIS Controls, ISO 27001, and OWASP LLM Top 10.
- **Deterministic CLI Tool (`ssp_tool.py`):** Link verification, crosswalk chapter resolution, Canvas node validation, and SSP-12 release gate evaluation.
- **Continuous Integration (CI):** GitHub Actions workflow across Python 3.10, 3.11, and 3.12.
- **Operational Templates:** Evidence Record (`EVIDENCE_RECORD.md`), Governed Security Exception (`SECURITY_EXCEPTION.md`), and AI Agent Manifest (`AI_AGENT_MANIFEST.json`).
- **Quickstart Adoption Guide:** Pragmatic 3-phase adoption path in Portuguese and English.
- **Obsidian Canvas Expansion:** Connected schema, templates, and guides directly into visual map.

---

## Contributing

Review [CONTRIBUTING.md](CONTRIBUTING.md), [VERSIONING.md](VERSIONING.md), and [SECURITY.md](SECURITY.md). Pull requests must pass `python scripts/ssp_tool.py validate`.
