# Roadmap / Roteiro

This roadmap is a proposal for the community edition. It does not commit the upstream protocol maintainers or promise a release date.

Este roteiro é uma proposta para a edição comunitária. Não compromete os mantenedores do protocolo upstream nem promete data de release.

## Edition 0.2.0 — Current / Atual (2026-10-22)

- [x] Machine-readable control specification (`protocol/v13.4/ssp-controls.json`).
- [x] Formal JSON Schema (`schema/ssp-control.schema.json`).
- [x] Zero-dependency Sovereign Verification CLI (`scripts/ssp_tool.py`).
- [x] Continuous Integration workflow in GitHub Actions (`.github/workflows/ci.yml`).
- [x] Pragmatic 3-Phase Adoption Quickstart guides in PT-BR and EN.
- [x] Operational templates for evidence records, security exceptions, and agent containment manifests.
- [x] Expanded Obsidian visual index and Canvas linking specifications and templates.

## Edition 0.1.0 — Initial draft / Rascunho inicial (2026-10-01)

- [x] Bilingual protocol, adoption and evidence guides.
- [x] 13-control crosswalk to the source v13.4 domains.
- [x] Agentic AI/MCP and J.A.R.V.I.S./Obsidian profile.
- [x] Provenance, official-source map, and community governance.
- [x] Static Obsidian navigation and Canvas; no private vault data.

## Candidate priorities / Prioridades candidatas

1. **Independent Review:** Invite independent security engineers to challenge control wording and applicability in real production scenarios.
2. **Adopter Evidence Portfolio:** Gather anonymized, non-sensitive implementation evidence records across common tech stacks (FastAPI, Spring Boot, Node.js, Go).
3. **Interactive Pre-commit Hook:** Provide a lightweight git hook integrating `ssp_tool.py validate` and `ssp_tool.py gate`.
4. **J.A.R.V.I.S. Gateway Sync:** Provide automated JSON exporter plugin for sovereign cognitive runtimes (`jarvis-sovereign-gateway` / `E:\.skill-registry`).
5. **English Human Review:** Progressively refine `SSP_v13.4_FULL_EN_COMMUNITY.md` with human technical review.

The project values verified usefulness and healthy maintenance over a star target. No number of adopters, certifications, or security outcomes is promised.
