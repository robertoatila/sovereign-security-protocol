# Guia Rápido de Adoção da SSP v13.4

Este guia orienta times de engenharia, arquitetos e desenvolvedores de agentes autônomos na implementação prática e progressiva do **Protocolo de Segurança Soberana (SSP)**.

---

## 1. Princípios Fundamentais

1. **Falha Fechada (Fail-Closed):** Ausência de configuração, token inválido ou falha de conexão bloqueiam acesso por padrão (`DENY`).
2. **Freshness da Evidência:** A aprovação pertence a um **commit SHA**, **digest do artefato** e **ambiente exatos**. Evidência de build anterior não valida o release atual.
3. **Autoridade Externa ao Modelo:** Modelos de IA e servidores MCP não concedem privilégios; a autorização reside no runtime externo e na verificação determinística de políticas.
4. **Governança de Exceção:** `ACCEPTED RISK` exige owner autenticado, justificativa técnica, controles compensatórios e data de expiração improrrogável.

---

## 2. Jornada de Adoção em 3 Fases

### Fase 1: Dia 1 — Baseline Soberano (L1)
*Objetivo: Estabelecer inventário, fronteiras e responsabilidades.*

- [ ] **Mapear Escopo e Ativos (SSP-01):** Identificar repositórios, serviços, bancos e owners.
- [ ] **Inventário de Dependências (SSP-07):** Versionar lockfiles (`package-lock.json`, `poetry.lock`, etc.).
- [ ] **Auditar Credenciais Padrão (SSP-05):** Garantir ausência de senhas default ou tokens em repositórios.
- [ ] **Declaração de Conformidade (SSP-13):** Registrar obrigações regulatórias (LGPD, GDPR, SOC 2).

### Fase 2: Semana 1 — Engenharia Segura & Portões CI (L2)
*Objetivo: Automação determinística e testes negativos.*

- [ ] **Fronteiras e Modelagem de Ameaças (SSP-02):** Documentar fluxos de dados e endpoints expostos.
- [ ] **Autorização Fina (SSP-03):** Implementar verificações no nível de recurso/tenant (prevenção a BOLA/IDOR).
- [ ] **Isolamento de Banco e RLS (SSP-04):** Ativar criptografia em trânsito/repouso e Row-Level Security.
- [ ] **Validação Estrita de Entrada (SSP-06):** Sanitização e tipagem em runtime em endpoints e webhooks.
- [ ] **Isolamento de Infraestrutura (SSP-08):** Portas de bancos e planos administrativos fora da Internet pública.
- [ ] **Auditoria e Logs Redigidos (SSP-11):** Logs estruturados sem vazamento de PII ou credenciais.

### Fase 3: Mês 1 — IA Confinada, Recuperação & Decisão de Release (L3)
*Objetivo: Contenção de agentes e portão formal de release.*

- [ ] **Contenção Agentiva e MCP (SSP-09):**
  - Delimitar escopo de ferramentas e conexões MCP com [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json).
  - Exigir aprovação humana vinculada ao hash da ação/plano para efeitos destrutivos ou de alto custo.
  - Ativar kill switch operacional e timeout estrito.
- [ ] **Exercício de Restore (SSP-10):** Realizar e comprovar teste de restauração de backup com RTO/RPO documentados.
- [ ] **Portão Formal de Release (SSP-12):** Executar `python scripts/ssp_tool.py gate -f <registro-evidencia.json>` antes de cada implantação crítica.

---

## 3. Uso das Ferramentas Locais

Valide a integridade do protocolo e das evidências localmente:

```bash
# Validar links, esquemas JSON e crosswalk da SSP
python scripts/ssp_tool.py validate

# Visualizar a matriz de controles e níveis mínimos
python scripts/ssp_tool.py matrix

# Avaliar aprovação de release (Gate SSP-12)
python scripts/ssp_tool.py gate --file templates/sample_evidence_record.json
```

---

## 4. Modelos e Artefatos Operacionais

- Registro de Evidências: [`templates/EVIDENCE_RECORD.md`](../../templates/EVIDENCE_RECORD.md)
- Solicitação de Exceção de Segurança: [`templates/SECURITY_EXCEPTION.md`](../../templates/SECURITY_EXCEPTION.md)
- Manifesto de Contenção de Agentes/MCP: [`templates/AI_AGENT_MANIFEST.json`](../../templates/AI_AGENT_MANIFEST.json)
