# Sovereign Security Protocol

**A verifiable security baseline for software, infrastructure, and agentic AI systems.**

[English](README.md) · [Português (PT-BR)](README.pt-BR.md)

| Source basis | Edition in this repository | Reference review |
|---|---|---|
| SSP v13.4.0 | Community Edition 0.1.0 — proposal | 2026-10-01 |

This project turns **Sovereign Security Protocol v13.4.0** into a public, bilingual, traceable baseline. It keeps the source's nine domains and organizes requirements into 13 portable controls with applicability criteria, evidence expectations, and release decisions.

> The v13.4.0 source remains the origin reference. This community edition proposes an adoption structure; it does not claim canonical status, certification, a completed audit, or a security guarantee.

## Start here

- [Protocol and 13 controls — English](docs/en/protocol.md)
- [Protocolo e 13 controles — PT-BR](docs/pt-BR/protocolo.md)
- [Adoption and evidence — English](docs/en/adoption-and-evidence.md)
- [Adoção e evidências — PT-BR](docs/pt-BR/adocao-e-evidencias.md)
- [Agentic AI, J.A.R.V.I.S. and Obsidian profile — English](docs/en/agentic-jarvis-obsidian.md)
- [Perfil de IA agentiva, J.A.R.V.I.S. e Obsidian — PT-BR](docs/pt-BR/agentes-jarvis-obsidian.md)
- [Traceability to SSP v13.4](control-crosswalk.csv)
- [Obsidian vault and visual map](obsidian/README.md) · [Canvas](SSP-13.4.canvas)
- [Provenance and official references](docs/research/provenance.md) · [standards map](docs/research/references.md)
- [Review and proposed improvements](docs/research/revisao-v13.4.md) · [roadmap](ROADMAP.md)
- [Suggested public listing and launch criteria](PUBLICATION.md)

## What it provides

- Short requirements with stable IDs, aligned PT-BR and English versions, and links to source sections.
- Explicit states for `PASS`, `FAIL`, `UNKNOWN`, `N/A`, and accepted risk without treating missing evidence as approval.
- Evidence bound to the commit, artifact, environment, and run that were actually assessed.
- An agent and MCP profile covering authority boundaries, per-tool/resource permissions, untrusted content, and approvals bound to the exact action.
- Guidance for using the repository as an Obsidian vault without exporting a user's private vault or creating a second J.A.R.V.I.S. synchronizer.
- An official-source map with versions and review date. Standards and specification versions must be rechecked before adoption or publication.

## Mental model

```text
SCOPE → THREATS → CONTROLS → EVIDENCE → DECISION → OBSERVE → RECOVER → LEARN
```

A scanner, hash, passing build, Markdown file, or agent self-report is an input to an assessment; none alone proves that a system is secure.

## Adoption profiles

1. **Baseline:** any system that processes data or has users.
2. **Production:** authentication, availability, personal data, APIs, and real releases.
3. **High impact:** multi-tenant systems, payments, sensitive data, or automation with material effects.
4. **Critical/regulated:** legal, contractual, and sector requirements defined with the responsible specialists.

Higher profiles add rigor; they do not remove the baseline. Scope and applicability must be justified for each system.

## Limits

This document is not a full transcription or line-by-line coverage statement for source v13.4. It does not replace a professional assessment, sector standard, legal advice, penetration test, or operational controls. It does not certify the J.A.R.V.I.S. runtime, an Obsidian vault, an organization, or any deployment. Laws, deadlines, versions, and requirements depend on jurisdiction and context.

Star count measures adoption, not security evidence. The goal is to make the material useful, citable, translatable, and easy for the community to review; no star count is promised.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), [VERSIONING.md](VERSIONING.md), and [SECURITY.md](SECURITY.md). Normative changes must cite a source, explain risk, and keep translations and the crosswalk in sync.
