# Versioning / Versionamento

## Separate version tracks

| Track | Current value | Meaning |
|---|---|---|
| Origin protocol | SSP `13.4.0` | The exact upstream source used as the baseline; it is governed in its originating repository. |
| This repository | Community Edition `0.1.0` — draft | An independent, bilingual adaptation and control structure; it is not an upstream successor. |

Do not label a community release `SSP 13.5`, `canonical`, `certified`, or `compliant` without a formal decision by the source protocol's authorized maintainers. A future proposal for the origin must go through that project's governance.

## Community edition version rules

- **Patch:** editorial fixes, broken links, translation corrections, and clarifications that do not change a MUST/SHOULD, scope, applicability, or evidence meaning.
- **Minor:** additive controls, profiles, mappings, or guidance that preserve existing control IDs and do not weaken requirements.
- **Major:** incompatible or weakening changes, retired IDs, changed status meanings, or restructured applicability.
- A version change updates both languages, the crosswalk, changelog, provenance/reference dates, and any Obsidian navigation that points to changed files.
- Control IDs are never reused. Retired controls remain mapped to their successor or are marked withdrawn with rationale.
- A release is not tagged until maintainers explicitly approve the proposed content and source references.

## Evidence versioning

Evidence records state the control edition and candidate identity. A protocol update does not retroactively change evidence; it may make prior evidence insufficient for the new edition. Reassess only the affected controls and document the transition.

## Português

### Trilhas de versão separadas

| Trilha | Valor atual | Significado |
|---|---|---|
| Protocolo de origem | SSP `13.4.0` | Fonte exata usada como base; governada no repositório de origem. |
| Este repositório | Community Edition `0.1.0` — draft | Adaptação bilíngue independente; não é sucessora do upstream. |

Não rotule uma edição comunitária como `SSP 13.5`, `canônica`, `certificada` ou `compliant` sem decisão formal dos mantenedores autorizados do protocolo de origem.

### Regras da edição comunitária

- **Patch:** correções editoriais, de tradução e de links, sem mudar força normativa, escopo, aplicabilidade ou sentido de evidência.
- **Minor:** controles, perfis, mapeamentos ou orientação adicionais sem enfraquecer requisitos ou reutilizar IDs.
- **Major:** mudança incompatível/enfraquecedora, retirada de IDs, mudança nos estados ou reorganização de aplicabilidade.
- Toda versão atualiza PT-BR, inglês, crosswalk, changelog, proveniência/fontes e navegação Obsidian afetada.
- IDs não são reutilizados. Controle retirado fica mapeado ao sucessor ou marcado como retirado com justificativa.
- Uma release só recebe tag após aprovação explícita dos mantenedores.

### Versionamento de evidências

Registros citam a edição do controle e a identidade do candidato. Uma atualização de protocolo não altera evidência passada; pode torná-la insuficiente. Reavalie os controles afetados e documente a transição.
