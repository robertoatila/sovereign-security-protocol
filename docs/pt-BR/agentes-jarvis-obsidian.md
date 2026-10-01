# Perfil de IA agentiva, J.A.R.V.I.S. e Obsidian

Este perfil aplica o SSP a agentes com memória, ferramentas, delegação, navegação de workspace ou conexões MCP. Ele descreve requisitos; não atesta que qualquer runtime J.A.R.V.I.S. os implemente.

## Modelo de autoridade

Um agente é um principal com capacidades limitadas. A autorização efetiva MUST ser aplicada fora do modelo e intersectar, no mínimo:

```text
missão autorizada ∩ identidade do principal ∩ perfil do agente
∩ política da ferramenta ∩ recursos/alvos ∩ ambiente ∩ política de risco
```

Uma camada inferior pode restringir uma permissão; não pode ampliá-la. Texto retornado por repositório, documento, busca, ferramenta, MCP, memória ou nó remoto pode informar uma decisão, mas não pode mudar sozinho a missão, políticas ou aprovação.

## Aprovação ligada à ação

Uma confirmação genérica, flag booleana, clique ou nome digitado não prova identidade nem autorização sobre um efeito. Para ação de risco, vincule o registro de aprovação a:

- identidade autenticada e papel do aprovador;
- principal/agente que executará;
- ação e conjunto completo de alvos/recursos;
- digest do plano/argumentos que será executado;
- risco, limites de custo/tempo e permissões;
- operação/tenant, validade e uso único ou política de repetição;
- registro verificável de decisão e resultado.

Qualquer alteração no conteúdo aprovado, alvo, escopo, ferramenta, digest ou ambiente relevante invalida a aprovação e exige nova decisão. Verifique novamente a permissão imediatamente antes do despacho, contra o adaptador e os efeitos reais.

## Limites para agentes e MCP

- Ferramentas, fontes MCP e versões precisam de owner, origem, capacidades, escopos, atualização, rede, filesystem, credenciais e processo de revogação conhecidos.
- Autorize cada chamada para o recurso e tenant pretendidos. Descrições e nomes de ferramentas não são uma fronteira de segurança.
- Shell e rede começam desabilitados quando não necessários. Quando habilitados, use sandbox, allow-list, timeout, limites de custo, filesystem e egress.
- Não exponha segredos no prompt, contexto, saída, telemetria ou vault. Materialize referências de segredo no consumidor de escopo mínimo; redação é defesa adicional, não autorização para persistir dados brutos.
- Dê aos agentes credenciais temporárias e limitadas, quando forem necessárias; defina revogação/rotação após exposição suspeita.
- Proteja delegação: subagente não pode herdar autoridade maior que a cadeia autorizada nem ampliar budget, escopo ou acesso.
- Registre fonte, autoria, tenant, escopo, integridade, revisão e exclusão da memória. Conteúdo externo nunca vira política confiável por ser lembrado.
- Teste cancelamento, limite e parada segura em operações que possam alterar dados, contas ou infraestrutura.

Para integração MCP, confira a revisão do protocolo vigente; a revisão pública indicada neste repositório foi publicada em **2026-07-28**. Compatibilidade de SDK, esquema, OAuth e extensões pode mudar independentemente deste perfil.

## Aplicação no J.A.R.V.I.S.

O repositório J.A.R.V.I.S. já possui uma `CognitiveVaultBridge.sync_registry` e um modelo de projeção gerenciada em Markdown/Canvas. Essa arquitetura é a referência de integração; este repositório não cria uma segunda bridge, seletor de skills, servidor ou autoridade de execução.

Os documentos de threat model e trust boundaries do J.A.R.V.I.S. informam as ameaças e o modelo de integração. Este projeto preserva a distinção entre controle desejado e mecanismo observado: uma descrição arquitetural é requisito e trilha de investigação, não prova de implementação ou certificação. Evidência deve ser coletada para o runtime e candidato específicos.

Para incorporar estes controles ao J.A.R.V.I.S., mantenedores devem mapear IDs SSP para a fonte canônica, planos, recibos e gates existentes; adicionar integração somente após revisão de ownership, escopo e evidências. A aprovação continua vinculada a um plano e digest exatos; a projeção Obsidian não decide nem executa missões.

## Aplicação no Obsidian

Abra a raiz deste repositório como vault. `SSP-13.4.canvas` e `00 - SSP Home.md` são índices de leitura para os arquivos versionados. Os arquivos Markdown são a fonte textual; Canvas e grafo não são fonte de autorização.

O cofre humano segue sendo conteúdo do usuário. Em uma integração real, atualize apenas regiões gerenciadas, preserve texto humano e nós/arestas que não pertencem à projeção, faça backup recuperável e gere recibo. Use um namespace de propriedade explícito. O prefixo `jarvis:projection:` pertence ao projetor J.A.R.V.I.S.; este Canvas público usa IDs próprios `ssp:` e não deve ser copiado para sobrescrever Canvas privado.

Não publique memória local, notas pessoais, histórico de execução, configs do Obsidian, estado do workspace, segredos ou cópias de vaults neste projeto.
