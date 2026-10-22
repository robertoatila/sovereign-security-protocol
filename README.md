# Protocolo de Segurança Soberana (SSP)

[![CI](https://github.com/robertoatila/sovereign-security-protocol/actions/workflows/ci.yml/badge.svg)](https://github.com/robertoatila/sovereign-security-protocol/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/SSP%20Base-v13.4.0-blue.svg)](protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md)
[![Edition](https://img.shields.io/badge/Community%20Edition-0.2.0-green.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

**Idioma / Language:** 🇧🇷 Português (PT-BR) · [English](README.en.md)

---

## LEIA O PROTOCOLO INTEGRAL

**[Abrir a SSP v13.4.0 completa em português](protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md)** — texto integral, reproduzido da fonte versionada.

O documento de origem declara o estado `CANÔNICO`. Esse estado se refere à fonte e ao commit original; este repositório oferece uma cópia para leitura, ferramental de auditoria e especificação legível por máquina, sem declarar uma nova autoridade canônica.

---

## O que há em inglês

- **Protocolo integral traduzido para inglês:** [versão comunitária em revisão](protocol/v13.4/SSP_v13.4_FULL_EN_COMMUNITY.md). É uma tradução automática não canônica e ainda precisa de revisão técnica humana.
- [Guia rápido de adoção em 3 fases — English](docs/en/quickstart-adoption.md)
- [Resumo comunitário dos 13 controles — English](docs/en/protocol.md)
- [Adoção e evidências — English](docs/en/adoption-and-evidence.md)
- [Agentes, J.A.R.V.I.S. e Obsidian — English](docs/en/agentic-jarvis-obsidian.md)

O texto integral em PT-BR é a referência para resolver divergências. A tradução inglesa está identificada como rascunho automático, não como versão normativa revisada. Os dois idiomas ficam em documentos separados; este README é a entrada em PT-BR.

---

## Comece aqui

- **[Guia Rápido de Adoção em 3 Fases](docs/pt-BR/guia-rapido-adocao.md)** — Roteiro prático (Dia 1, Semana 1, Mês 1).
- **[Resumo dos 13 controles — PT-BR](docs/pt-BR/protocolo.md)** — Definição normativa dos controles SSP-01 a SSP-13.
- **[Adoção e evidências — PT-BR](docs/pt-BR/adocao-e-evidencias.md)** — Princípio de freshness e níveis de prova L0 a L3.
- **[Agentes, J.A.R.V.I.S. e Obsidian — PT-BR](docs/pt-BR/agentes-jarvis-obsidian.md)** — Modelo de autoridade externa, contenção e MCP.
- **[Especificação Legível por Máquina (JSON)](protocol/v13.4/ssp-controls.json)** · [JSON Schema](schema/ssp-control.schema.json).
- **[Mapa de rastreabilidade para os capítulos da SSP v13.4](control-crosswalk.csv)**.
- **[Índice visual do Obsidian](00%20-%20SSP%20Home.md)** · **[Canvas](SSP-13.4.canvas)**.
- **Modelos Operacionais:**
  - [Registro de Evidências](templates/EVIDENCE_RECORD.md)
  - [Solicitação de Exceção de Segurança](templates/SECURITY_EXCEPTION.md)
  - [Manifesto de Contenção de Agentes/MCP](templates/AI_AGENT_MANIFEST.json)
- [Proveniência e licença do protocolo integral](protocol/v13.4/NOTICE.md).
- [Referências e revisão da v13.4](docs/research/references.md) · [melhorias propostas](docs/research/revisao-v13.4.md).

---

## Motor de Ferramental e Validação Soberana (`scripts/ssp_tool.py`)

O repositório inclui um motor de verificação autônomo, determinístico e sem dependências externas (Python standard library):

```bash
# 1. Validar links, nós do Canvas, crosswalk e schemas do repositório
python scripts/ssp_tool.py validate

# 2. Exibir a matriz dos 13 controles e níveis mínimos de evidência
python scripts/ssp_tool.py matrix

# 3. Verificar paridade da documentação bilíngue (PT-BR <-> EN)
python scripts/ssp_tool.py check-parity

# 4. Avaliar portão de release SSP-12 contra manifesto de evidência
python scripts/ssp_tool.py gate --file templates/sample_evidence_record.json
```

---

## O que foi melhorado na Edição Comunitária `0.2.0`

- **Especificação em JSON & Schema:** Todos os 13 controles agora possuem representação estruturada em [`protocol/v13.4/ssp-controls.json`](protocol/v13.4/ssp-controls.json), validada pelo [`schema/ssp-control.schema.json`](schema/ssp-control.schema.json), com mapeamentos para OWASP ASVS, NIST SP 800-53 r5, CIS Controls v8, ISO 27001 e OWASP LLM Top 10.
- **CLI Determinística (`ssp_tool.py`):** Validação de links relativos, consistência do crosswalk com os capítulos do protocolo, integridade do Canvas e avaliação do portão de release SSP-12.
- **Pipeline de Integração Contínua (CI):** Workflow no GitHub Actions testando Python 3.10, 3.11 e 3.12 em cada push e pull request.
- **Modelos Operacionais:** Templates de registro de evidências (`EVIDENCE_RECORD.md`), exceções governadas (`SECURITY_EXCEPTION.md`) e manifesto de contenção agentiva (`AI_AGENT_MANIFEST.json`).
- **Guia Rápido de Adoção:** Roteiro prático em 3 fases em PT-BR e EN.
- **Expansão do Obsidian Canvas:** Novos nós integrando schemas, templates e guias de adoção.

---

## Escopo e limites

A cópia integral preserva o texto da SSP v13.4.0. Este projeto não a renomeia como v13.5 nem declara certificação, conformidade, auditoria concluída ou cobertura de implementação. A edição comunitária `0.2.0` organiza orientação complementar, ferramental de verificação e permanece independente da governança da fonte.

Estrelas medem adoção, não segurança. Nenhuma contagem de estrelas é prometida.

---

## Contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md), [VERSIONING.md](VERSIONING.md) e [SECURITY.md](SECURITY.md). Mudanças no texto da fonte exigem nova versão aprovada pelos mantenedores autorizados. Pull requests devem passar pelo validador local (`python scripts/ssp_tool.py validate`).
