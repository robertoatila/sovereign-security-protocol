# SSP Security Exception Request / Solicitação de Exceção de Segurança

**Formulário Governança de Risco (SSP-01, SSP-05, SSP-12)**

---

## 1. Identificação da Exceção

* **ID da Exceção:** `EXC-YYYY-XXXX`
* **Controle SSP Afetado:** `[SSP-01 a SSP-13]`
* **Sistema / Repositório:** `[Nome do sistema / repo]`
* **Ambiente Aplicável:** `[Staging / Produção / Nó Soberano]`
* **Data da Solicitação:** `YYYY-MM-DD`
* **Data de Expiração Obrigatória (Max 90 dias):** `YYYY-MM-DD`

---

## 2. Contexto Técnico e Justificativa

* **Descrição do Bloqueador / Risco Encontrado:**
  *Explique detalhadamente por que o controle não pôde receber `PASS` no release atual.*
* **Impacto Operacional de Bloquear o Release:**
  *Justificativa de negócio ou contingência operacional que motive o aceite temporário do risco.*

---

## 3. Controles Compensatórios Ativos

> *Conforme a SSP v13.4, uma pendência nunca é tratada como aprovação. Um risco só pode ser aceito se houver salvaguardas compensatórias mensuráveis.*

1. **Mitigação Imediata:** `[ex: Restrição de tráfego a IP corporativo específico / Egress bloqueado]`
2. **Monitoramento Reforçado:** `[ex: Alertas de alta prioridade enviados ao SIEM a cada invocação]`
3. **Plano de Remediação Definitivo:** `[ex: PR #123 com refatoração agendada para o sprint 4]`

---

## 4. Aprovação e Assinatura

* **Responsável Técnico (Owner do Sistema):** `Nome / Cargo / ID`
* **Aprovador de Segurança Soberana (Security Lead):** `Nome / Cargo / ID`
* **Status da Decisão:** `[APROVADA / REJEITADA]`
* **Trilha Verificável:** `[Link da issue / commit / chave de assinatura]`
