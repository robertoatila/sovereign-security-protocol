# Changelog

This changelog tracks this repository's community edition, not the canonical source protocol's release history.

## 0.3.0 — 2026-10-29 — Universal 7-Layer Engine, Multi-Stack Playbooks & Visual Architecture

- Added zero-dependency Universal Security CLI (`ssp.py`) allowing any external project to bootstrap SSP security scaffolding (`init`), run 7-Layer heuristic posture checks (`scan` across Python, Node/TS, Go, Rust, Java, SQL, Docker, GitHub Actions, and MCP), inspect stack remediation blueprints (`blueprint`), and enforce strict SSP-12 release gates (`gate` with commit SHA freshness, `N/A` rationale, and `ACCEPTED RISK` expiration verification).
- Created reusable Composite GitHub Action (`action.yml`) supporting `scan` and `gate` modes out-of-the-box in any CI/CD workflow.
- Authored side-by-side ❌ Vulnerable vs. ✅ Hardened multi-stack playbooks (`docs/pt-BR/camadas-por-sistema.md` and `docs/en/layers-by-system.md`) covering Web/API (FastAPI/Express), SaaS/PostgreSQL RLS, Docker/UFW loopback binding, Supply Chain pinning, and Agentic AI/MCP containment.
- Added ecosystem architecture and 50k+★ global open-source security benchmarks guide (`docs/pt-BR/ecossistema-e-referencias-50k.md` and `docs/en/ecosystem-and-50k-references.md`), detailing standalone SSP adoption vs. optional `jarvis-skill-registry` runtime integration.
- Designed sovereign SVG visual architecture banners and 7-Layer Defense-in-Depth diagrams (`.github/assets/ssp-hero-pt.svg`, `ssp-hero-en.svg`, `ssp-layers-pt.svg`, `ssp-layers-en.svg`).
- Added automated test battery (`run_tests.py` and `tests/test_ssp_engine.py`) and expanded `.github/workflows/ci.yml` to run unit/integration tests, `--doctor`, self-scan, and release gate evaluation across Python 3.10–3.12.
- Upgraded root `LICENSE` to standard SPDX-recognizable Apache License 2.0 text while preserving canonical `protocol/v13.4/LICENSE-APACHE-2.0.txt` and `NOTICE.md`.
- Added GitHub community issue templates (`.github/ISSUE_TEMPLATE/`) and updated `CITATION.cff`, `00 - SSP Home.md`, and `SSP-13.4.canvas`.

### PT-BR

- Adicionada CLI Universal de Segurança sem dependências externas (`ssp.py`), permitindo a qualquer sistema externo inicializar artefatos SSP (`init`), auditar heurísticas das 7 Camadas (`scan` em Python, Node/TS, Go, Rust, Java, SQL, Docker, GitHub Actions e MCP), consultar planos por stack (`blueprint`) e impor o portão formal SSP-12 (`gate` com verificação de commit SHA, justificativa de `N/A` e expiração de `ACCEPTED RISK`).
- Criada Composite GitHub Action reutilizável (`action.yml`) com modos `scan` e `gate` prontos para qualquer pipeline CI/CD.
- Elaborados manuais práticos lado a lado (❌ Vulnerável vs. ✅ Blindado) por sistema (`docs/pt-BR/camadas-por-sistema.md` e `docs/en/layers-by-system.md`) cobrindo Web/API, PostgreSQL RLS Multi-Tenant, Docker/UFW em loopback, Supply Chain e Agentes de IA/MCP.
- Adicionado guia de arquitetura do ecossistema e benchmarks globais 50k+★ (`docs/pt-BR/ecossistema-e-referencias-50k.md` e `docs/en/ecosystem-and-50k-references.md`), detalhando o uso 100% autônomo deste repositório e a integração opcional com `jarvis-skill-registry`.
- Criados banners visuais e diagramas de Defesa em Profundidade de 7 Camadas em SVG (`.github/assets/ssp-hero-pt.svg`, `ssp-hero-en.svg`, `ssp-layers-pt.svg`, `ssp-layers-en.svg`).
- Adicionada bateria automatizada de testes (`run_tests.py` e `tests/test_ssp_engine.py`) e expandido `.github/workflows/ci.yml` em Python 3.10–3.12.
- Atualizado o `LICENSE` raiz com o texto integral padrão Apache License 2.0 para detecção SPDX automática no GitHub, preservando intactos os arquivos canônicos da fonte.
- Adicionados templates comunitários de Issues (`.github/ISSUE_TEMPLATE/`) e atualizados `CITATION.cff`, `00 - SSP Home.md` e `SSP-13.4.canvas`.

## 0.2.0 — 2026-10-22 — Verification Engine & Machine-Readable Controls

- Added machine-readable JSON control specification (`protocol/v13.4/ssp-controls.json`) and formal JSON Schema (`schema/ssp-control.schema.json`).
- Mapped all 13 controls to external standards: OWASP ASVS v4.0, NIST SP 800-53 r5, CIS Controls v8, ISO 27001:2022, and OWASP LLM Top 10 2025.
- Created sovereign, zero-dependency Python verification CLI (`scripts/ssp_tool.py`) with link validation, crosswalk checking, schema validation, bilingual parity checking, and SSP-12 release gate evaluation.
- Implemented GitHub Actions CI workflow (`.github/workflows/ci.yml`) validating repository integrity across Python 3.10, 3.11, and 3.12.
- Created operational templates: `templates/EVIDENCE_RECORD.md`, `templates/SECURITY_EXCEPTION.md`, and `templates/AI_AGENT_MANIFEST.json`.
- Authored pragmatic 3-Phase Quickstart Adoption Guides (`docs/pt-BR/guia-rapido-adocao.md` and `docs/en/quickstart-adoption.md`).
- Expanded Obsidian visual index (`00 - SSP Home.md`) and Canvas (`SSP-13.4.canvas`) linking new specifications and templates.

### PT-BR

- Adicionada especificação legível por máquina em JSON (`protocol/v13.4/ssp-controls.json`) e JSON Schema formal (`schema/ssp-control.schema.json`).
- Mapeamento dos 13 controles aos padrões externos: OWASP ASVS v4.0, NIST SP 800-53 r5, CIS Controls v8, ISO 27001:2022 e OWASP LLM Top 10 2025.
- Criada CLI soberana e sem dependências externas (`scripts/ssp_tool.py`) para checagem de links, consistência de crosswalk, validação de schema, paridade bilíngue e portão de release SSP-12.
- Implementado pipeline de CI com GitHub Actions (`.github/workflows/ci.yml`) testando Python 3.10, 3.11 e 3.12.
- Criados modelos operacionais: `templates/EVIDENCE_RECORD.md`, `templates/SECURITY_EXCEPTION.md` e `templates/AI_AGENT_MANIFEST.json`.
- Elaborado Guia Rápido de Adoção em 3 Fases (`docs/pt-BR/guia-rapido-adocao.md` e `docs/en/quickstart-adoption.md`).
- Expandido o índice visual do Obsidian (`00 - SSP Home.md`) e Canvas (`SSP-13.4.canvas`) com nós para schemas e templates.

## Unreleased — full English translation

- Added a complete machine-translated English draft of SSP v13.4.0; original PT-BR bytes remain unchanged and authoritative.
- Preserved Markdown line structure, fenced code, inline code, and link destinations during translation; marked the English draft as non-canonical and awaiting human technical review.
- Updated Portuguese and English entry pages, the source notice, provenance, and Obsidian navigation so each language opens its full text directly.

### PT-BR

- Adicionada uma tradução automática integral da SSP v13.4.0 para inglês; os bytes do original PT-BR seguem inalterados e são a referência normativa.
- Preservados a estrutura de linhas Markdown, blocos de código, trechos inline e destinos de links; a versão inglesa está marcada como não canônica e pendente de revisão técnica humana.
- Atualizadas as entradas PT-BR e English, o aviso de origem, a proveniência e a navegação do Obsidian para abrir diretamente o texto integral de cada idioma.

## Unreleased — publication and access correction

- Published the full 6,678-line SSP v13.4.0 source in Portuguese, extracted byte-for-byte from its pinned source commit and accompanied by its Apache-2.0 license and notice.
- Made PT-BR the default README, placed the full source as the first reading link, and separated the English and Portuguese entry pages.
- Renamed the 13-control guides as community summaries and added an explicit warning that they do not replace the full source.
- Updated the Obsidian home note and Canvas to open the complete PT-BR text first.
- Kept source content unchanged; source-review proposals remain separate.
- At that point, the English guide was a summary; a separate full translation draft was added in the later unreleased entry above.

### PT-BR

- Publicado o texto integral de 6.678 linhas da SSP v13.4.0 em português, extraído byte a byte do commit fixado e acompanhado pela licença e aviso Apache-2.0.
- PT-BR virou a página inicial padrão; o protocolo completo está no primeiro link de leitura e as entradas em inglês e português foram separadas.
- Os guias de 13 controles agora são chamados de resumos comunitários e avisam que não substituem o texto integral.
- A nota inicial e o Canvas do Obsidian agora abrem primeiro o texto integral em PT-BR.
- O conteúdo da fonte foi preservado; propostas da revisão continuam separadas.
- Naquele momento, o guia em inglês era um resumo; a entrada acima registra a tradução integral comunitária adicionada depois.

## 0.1.0 — draft — 2026-10-01

- Created a bilingual community edition based on the exact SSP v13.4.0 source commit recorded in `docs/research/provenance.md`.
- Mapped the source's nine domains to 13 stable community control IDs.
- Added adoption profiles, evidence freshness, release decisions, agent/MCP guidance, and a public Obsidian navigation view.
- Added official reference links with a dated review and a review of source ambiguities.
- No runtime implementation or conformance certification is included.

### PT-BR

- Criada edição comunitária bilíngue baseada no commit exato da SSP v13.4.0 em `docs/research/provenance.md`.
- Mapeados os nove domínios da fonte em 13 IDs de controle comunitários.
- Adicionados perfis de adoção, freshness de evidência, decisões de release, orientação para agentes/MCP e uma navegação pública para Obsidian.
- Incluídos links de fontes oficiais com data de revisão e análise de ambiguidades da fonte.
- Não inclui implementação de runtime nem certificação de conformidade.
