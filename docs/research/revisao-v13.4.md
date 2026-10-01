# Revisão da fonte v13.4 / Review of source v13.4

Esta revisão usa a fonte integral SSP v13.4.0 identificada em [`provenance.md`](provenance.md). Ela preserva os pontos fortes e registra melhorias editoriais propostas; não altera nem substitui a fonte canônica.

## Pontos fortes preservados

- Nove domínios cobrem o ciclo de desenho, implementação, verificação, operação, resposta e recuperação.
- A fonte separa gates de segurança, qualidade, confiabilidade e privacidade/compliance.
- O princípio de freshness liga evidência ao commit, artefato e ambiente.
- A fonte inclui isolamento multi-tenant, supply chain, recuperação, redes, abuso, logs, IA/RAG/agentes/MCP e fronteiras de confiança.
- `UNKNOWN`, justificativa de `N/A` e risco aceito reconhecem que ausência de informação não é aprovação.

## Ajustes editoriais desta edição

| Observação sobre a fonte | Ajuste nesta edição |
|---|---|
| O cabeçalho identifica v13.4.0, enquanto o check de consistência §27 pede `versão = v13`. | A decisão de release desta edição se vincula explicitamente a `13.4.0` e ao digest do candidato avaliado. |
| A seção §0.0 se chama “Delta v13”; não fornece um changelog completo e específico de v13.4. | Esta revisão lista suas próprias mudanças e preserva o link à fonte, sem inventar histórico intermediário. |
| A fonte é extensa e requisitos parecidos aparecem em capítulos distintos. | IDs SSP-01 a SSP-13, linguagem normativa comum e crosswalk tornam localização e revisão mais fáceis; não substituem os detalhes da fonte. |
| Estados operacionais como pendência externa/legal aparecem perto de resultados de controle. | Pendência é trabalho em aberto; `PASS`, `FAIL`, `UNKNOWN`, `N/A` e risco aceito são decisões de controle separadas. |
| Integridade por hash, proveniência, autenticidade de identidade e autorização podem ser confundidas. | O novo texto trata essas propriedades separadamente e não eleva hash/Merkle a prova de origem ou autoridade. |
| Ferramentas concretas são citadas ao lado de requisitos universais. | Esta edição especifica o resultado de segurança; ferramentas são opções e não condição de conformidade. |
| Referências regulatórias e técnicas têm ciclos de vida diferentes e podem mudar após a data da fonte. | [`references.md`](references.md) registra fontes oficiais, versões/estados e a data desta revisão; requisitos legais continuam dependentes de jurisdição. |
| Um `PASS` precisa demonstrar o controle, mas diferentes controles pedem métodos de prova distintos. | A evidência mínima é proporcional: teste, revisão, configuração, exercício, registro de aprovação ou referência normativa conforme o controle. |

## Propostas explícitas além da fonte

1. **IDs estáveis e bilíngues:** manter controle ID mesmo quando título ou texto mudam; alinhar EN/PT-BR na mesma revisão.
2. **Aprovação vinculada a payload:** autenticar aprovador e limitar concessão a ação, alvos, digest/plano, budget, validade e operação exatos; mudança material requer novo consentimento.
3. **Freshness orientada à mudança:** cada controle define quais alterações invalidam sua evidência, sem prazo universal arbitrário.
4. **Exceções governadas:** owner autorizado, risco, rationale, compensação, prazo de expiração, revisão e trilha verificável; pendência nunca é `PASS`.
5. **Perfis incrementais:** baseline comum; maior risco adiciona exigência sem desativar controle básico.
6. **Projeção de conhecimento:** Obsidian facilita navegação e revisão humana; notas e Canvas não concedem autoridade de execução.
7. **Separação entre intenção e prova:** J.A.R.V.I.S. e qualquer outro runtime precisam de evidência específica antes de um mecanismo documentado receber `PASS`.

## Não alegado

Esta edição não afirma auditoria completa linha a linha da fonte, certificação legal/setorial, implementação dos controles no J.A.R.V.I.S., cobertura exaustiva dos padrões citados, segurança por passar um scanner, nem aceitação pela governança da origem. O dono canônico da fonte decide mudanças nela.
