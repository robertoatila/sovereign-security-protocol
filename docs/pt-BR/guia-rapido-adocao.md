# Guia Rápido de Adoção da SSP v13.4

Este guia orienta times de engenharia, arquitetos e desenvolvedores de agentes autônomos na implementação prática e progressiva do **Protocolo de Segurança Soberana (SSP)** em **qualquer sistema**, usando apenas este repositório.

---

## 1. Princípios Fundamentais

1. **Falha Fechada (Fail-Closed):** Ausência de configuração, token inválido ou falha de conexão bloqueiam acesso por padrão (`DENY`).
2. **Freshness da Evidência:** A aprovação pertence a um **commit SHA**, **digest do artefato** e **ambiente exatos**. Evidência de build anterior não valida o release atual.
3. **Autoridade Externa ao Modelo:** Modelos de IA e servidores MCP não concedem privilégios; a autorização reside no runtime externo e na verificação determinística de políticas.
4. **Governança de Exceção:** `ACCEPTED RISK` exige owner autenticado, justificativa técnica, controles compensatórios e data de expiração improrrogável.

---

## 2. Aplicação Imediata em Qualquer Sistema (60 Segundos)

Com Python 3.10+ (apenas biblioteca padrão, zero dependências externas), inicialize e audite qualquer projeto local:

```bash
# 1. Gerar artefatos .ssp/ customizados para a stack detectada no projeto alvo
python ssp.py init --target /caminho/do/seu-sistema --lang pt

# 2. Auditar as 7 Camadas de Segurança no projeto alvo
python ssp.py scan --target /caminho/do/seu-sistema --lang pt

# 3. Consultar guia prático por stack (api | database | docker | ai-mcp | cli)
python ssp.py blueprint --stack api --lang pt

# 4. Impor o Portão de Release SSP-12 antes de deploy em produção
python ssp.py gate --file /caminho/do/seu-sistema/.ssp/evidence-record.json --commit <git-sha>
```

Para integrar em pipelines GitHub Actions, adicione `robertoatila/sovereign-security-protocol@main` via [`action.yml`](../../action.yml). Para exemplos práticos de código **❌ Vulnerável vs. ✅ Blindado**, consulte [`camadas-por-sistema.md`](camadas-por-sistema.md).

---

## 3. Jornada de Adoção em 3 Fases

### Fase 1: Dia 1 — Baseline Soberano (L1)
*Objetivo: Estabelecer inventário, fronteiras e responsabilidades.*

- [ ] **Mapear Escopo e Ativos (SSP-01):** Identificar repositórios, serviços, bancos e owners (`python ssp.py init`).
- [ ] **Inventário de Dependências (SSP-07):** Versionar lockfiles (`package-lock.json`, `poetry.lock`, `go.sum`, `Cargo.lock`).
- [ ] **Auditar Credenciais Padrão (SSP-05):** Garantir ausência de senhas default ou tokens em repositórios (`python ssp.py scan`).
- [ ] **Declaração de Conformidade (SSP-13):** Registrar obrigações regulatórias (LGPD, GDPR, SOC 2).

### Fase 2: Semana 1 — Engenharia Segura & Portões CI (L2)
*Objetivo: Automação determinística e testes negativos.*

- [ ] **Fronteiras e Modelagem de Ameaças (SSP-02):** Documentar fluxos de dados e endpoints expostos.
- [ ] **Autorização Fina (SSP-03):** Implementar verificações no nível de recurso/tenant (prevenção a BOLA/IDOR).
- [ ] **Isolamento de Banco e RLS (SSP-04):** Ativar criptografia em trânsito/repouso e Row-Level Security.
- [ ] **Validação Estrita de Entrada (SSP-06):** Sanitização e tipagem em runtime em endpoints e webhooks.
- [ ] **Isolamento de Infraestrutura (SSP-08):** Portas de bancos e planos administrativos em `127.0.0.1` / rede privada.
- [ ] **Auditoria e Logs Redigidos (SSP-11):** Logs estruturados sem vazamento de PII ou credenciais.

### Fase 3: Mês 1 — IA Confinada, Recuperação & Decisão de Release (L3)
*Objetivo: Contenção de agentes e portão formal de release.*

- [ ] **Contenção Agentiva e MCP (SSP-09):**
  - Delimitar escopo de ferramentas e conexões MCP com [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json).
  - Exigir aprovação humana vinculada ao hash da ação/plano para efeitos destrutivos ou de alto custo.
  - Ativar kill switch operacional e timeout estrito.
- [ ] **Exercício de Restore (SSP-10):** Realizar e comprovar teste de restauração de backup com RTO/RPO documentados.
- [ ] **Portão Formal de Release (SSP-12):** Executar `python ssp.py gate -f <registro-evidencia.json>` antes de cada implantação crítica.

---

## 4. Verificação de Integridade do Próprio Repositório

```bash
# Diagnóstico completo (SHA-256 canônico, links, Canvas, JSON Schema e paridade PT/EN)
python ssp.py --doctor

# Visualizar a matriz de 13 controles e níveis mínimos
python ssp.py matrix --lang pt
```

---

## 5. Modelos e Artefatos Operacionais

- Manual Prático por Sistema (❌ vs ✅): [`docs/pt-BR/camadas-por-sistema.md`](camadas-por-sistema.md)
- Arquitetura & Referências 50k+★: [`docs/pt-BR/ecossistema-e-referencias-50k.md`](ecossistema-e-referencias-50k.md)
- Registro de Evidências: [`templates/EVIDENCE_RECORD.md`](../../templates/EVIDENCE_RECORD.md)
- Solicitação de Exceção de Segurança: [`templates/SECURITY_EXCEPTION.md`](../../templates/SECURITY_EXCEPTION.md)
- Manifesto de Contenção de Agentes/MCP: [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json)
