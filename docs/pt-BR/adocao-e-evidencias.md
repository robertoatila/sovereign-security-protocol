# Adoção e evidências

Este guia transforma os 13 controles em uma avaliação por candidato e ambiente. Ele não define um score universal nem converte um checklist em certificação.

## Fluxo de adoção

1. **Defina o candidato:** serviço, versão, funcionalidades, integrações, dados e ambientes no escopo.
2. **Desenhe as fronteiras:** usuários, tenants, serviços, provedores, ferramentas, agentes, stores e planos administrativos.
3. **Escolha o perfil:** base, produção, alto impacto ou crítico/regulado. Registre o motivo e os controles condicionais.
4. **Atribua responsáveis:** owner por controle, quem avalia, quem aprova exceção e quem decide release.
5. **Colete evidência direta:** execute o método adequado ao requisito e vincule o resultado ao candidato exato.
6. **Decida e registre:** bloqueadores, itens desconhecidos, risco aceito, controles compensatórios e validade.
7. **Monitore deriva:** mudanças no build, configuração, dependência, fronteira, modelo, prompt, MCP server ou autorização podem invalidar conclusões.

## Registro mínimo de evidência

Copie o modelo e remova campos que não se aplicam com justificativa. Use referências controladas para logs ou artefatos grandes; não publique credenciais, dados pessoais ou detalhes que criem risco.

```text
Assessment ID:
Control ID and edition:
Scope / asset / tenant:
Owner and assessor:
Commit SHA:
Artifact digest:
Environment and relevant configuration:
Method / command / tool and version:
Expected outcome:
Observed outcome:
Evidence reference / digest:
Timestamp and freshness rule:
Status: PASS | FAIL | UNKNOWN | N/A | ACCEPTED RISK
Limitations / residual risk:
Approver and approval reference, if applicable:
Expiry / next review:
```

**Hash não autentica a origem.** Um digest ajuda a identificar bytes quando comparado com um valor confiável; assinatura e provenance exigem identidade, chave, processo de emissão e verificação próprios.

## Validade e freshness

- Vincule cada resultado à revisão de código, digest do artefato, configuração e ambiente que foram avaliados.
- Defina previamente quais mudanças anulam cada tipo de evidência. Alteração de autorização, superfície de rede, dependência crítica ou versão de modelo geralmente exige reavaliação do controle afetado.
- Evidência antiga pode documentar histórico; não aprove automaticamente um release novo.
- Escolha periodicidade de revisão pelo risco e velocidade de mudança. Não existe prazo único adequado a todos os controles.
- Preserve origem, data e contexto; redija segredos e minimize dados pessoais.

## Decisão de release

| Gate | Pergunta de saída |
|---|---|
| Segurança | Os controles aplicáveis foram verificados? Existem bloqueadores sem mitigação? |
| Qualidade/correção | Os requisitos funcionais e de autorização passaram nos cenários relevantes? |
| Confiabilidade/recuperação | Falhas, migrações, filas, retries e restores foram avaliados? |
| Privacidade/compliance | Obrigações aplicáveis foram identificadas e revisadas pelos responsáveis competentes? |
| Artefato/proveniência | O artefato de release corresponde ao aprovado e tem origem verificável na medida exigida? |
| Acessibilidade | O alvo aplicável e a evidência de avaliação estão definidos? |

Use `READY` somente se os gates aplicáveis passarem e não houver bloqueador crítico. `READY WITH ACCEPTED RISK` exige autorização competente, owner, justificativa, controle compensatório, limite/expiração e revisão. Uma exceção não cancela obrigações legais, contratuais ou um bloqueador que a política da organização proíba aceitar. Caso falte prova, use `UNKNOWN` ou `NOT READY` conforme a política local.

## Priorização de vulnerabilidades

Considere severidade técnica, probabilidade de exploração, presença no [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), exposição real, criticidade do ativo, impacto e mitigação disponível. CVSS, EPSS e KEV respondem perguntas diferentes; não os some em uma fórmula arbitrária nem use a pontuação isolada como decisão.

## Exemplos de interpretação

- Um scanner sem finding não prova autorização correta em todas as rotas: complemente com testes negativos e revisão de desenho.
- Um teste de tenant que falha é `FAIL` para o controle avaliado, ainda que outras suítes passem.
- Um restore ainda não executado é `UNKNOWN` para o requisito de recuperação, não `PASS` porque existe um arquivo de backup.
- Uma nova versão de artefato exige evidência vinculada ao novo digest; resultados do anterior continuam como histórico.
- Um controle marcado `N/A` precisa de escopo e justificativa que outra pessoa consiga revisar.
