# Contributing / Como contribuir

Thank you for improving this baseline. Pull requests and issues should make a concrete security or usability improvement and keep the source trail visible.

## Before proposing a change

1. Search for an existing control or issue so the repository stays small and coherent.
2. Classify the proposal as editorial, normative, a reference update, or an example.
3. Link primary sources for normative claims. Record version, status, date checked, and affected control IDs.
4. State applicability, assumptions, threat addressed, evidence expected, and limitations.
5. Update English and PT-BR in the same change. Keep IDs and requirement strength aligned.
6. Update [`control-crosswalk.csv`](control-crosswalk.csv), [`CHANGELOG.md`](CHANGELOG.md), and version notes when relevant.

## Contribution boundaries

- Do not add secrets, live credentials, personal information, private vault exports, telemetry dumps, or local workspace settings.
- Do not copy full text, code, diagrams, or control catalogs from third-party standards without checking license and attribution requirements. Prefer links and original summaries.
- Do not present a local runtime, scanner, self-report, hash, or passing example as independent proof or certification.
- Keep tool names in examples optional unless a requirement truly depends on a specific implementation.
- An exception proposal must not silently downgrade a blocker, erase history, or remove an evidence limit.
- No GitHub Actions or other CI service is required by this repository. Reviewers may run their own local validation and must report the exact revision and limits of that evidence.

## Review checklist

- [ ] The proposal states the threat, asset, and scope.
- [ ] Normative strength and applicability are explicit.
- [ ] Evidence can be tied to the candidate actually assessed.
- [ ] Existing source references remain attributable and current for the stated review date.
- [ ] English and PT-BR versions agree in meaning.
- [ ] Local J.A.R.V.I.S. or Obsidian data has not been copied into the change.

All participants must follow the [Code of Conduct](CODE_OF_CONDUCT.md) and the [security reporting policy](SECURITY.md).

## Português

Obrigado por melhorar esta base. Issues e pull requests devem propor uma melhoria concreta de segurança ou usabilidade e manter a origem das afirmações visível.

### Antes da proposta

1. Procure controles e issues existentes para manter o repositório coeso.
2. Classifique a mudança como editorial, normativa, atualização de fonte ou exemplo.
3. Para afirmação normativa, ligue fonte primária e registre edição/estado, data de consulta e IDs afetados.
4. Explique aplicabilidade, premissas, ameaça, evidência esperada e limitações.
5. Atualize PT-BR e inglês na mesma alteração. Mantenha IDs e força normativa alinhados.
6. Atualize [`control-crosswalk.csv`](control-crosswalk.csv), [`CHANGELOG.md`](CHANGELOG.md) e versão quando aplicável.

### Limites

- Não inclua segredos, credenciais ativas, dados pessoais, exportações de vault privado, dumps de telemetria ou configurações de workspace.
- Não copie texto completo, código, diagramas ou catálogos de terceiros sem conferir licenças e atribuição; prefira links e síntese original.
- Não apresente runtime, scanner, auto-relato, hash ou exemplo aprovado como prova independente ou certificação.
- Deixe nomes de ferramentas opcionais, a menos que o requisito dependa de uma implementação específica.
- Uma proposta de exceção não pode reduzir silenciosamente um blocker, apagar histórico ou remover limite de evidência.
- Este repositório não exige GitHub Actions nem outro serviço de CI. Revisores podem validar localmente e devem registrar a revisão exata e os limites da evidência.

### Checklist de revisão

- [ ] A proposta informa ameaça, ativo e escopo.
- [ ] Força normativa e aplicabilidade estão explícitas.
- [ ] A evidência pode ser vinculada ao candidato avaliado.
- [ ] As fontes continuam atribuídas e atuais para a data declarada.
- [ ] As versões em inglês e PT-BR mantêm o mesmo significado.
- [ ] Nenhum dado local de J.A.R.V.I.S. ou Obsidian foi copiado.

Siga o [Código de Conduta](CODE_OF_CONDUCT.md) e a [política de relato de segurança](SECURITY.md).
