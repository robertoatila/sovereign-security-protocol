# SSP Community Edition 0.1.0 — Protocolo (PT-BR)

**Base:** Protocolo de Segurança Soberana v13.4.0. **Estado desta edição:** proposta comunitária, não canônica.

Esta edição traduz e reorganiza a fonte em requisitos menores e rastreáveis. Os IDs abaixo pertencem a esta edição; não são IDs que a fonte v13.4 declara possuir. Consulte [proveniência](../research/provenance.md), [crosswalk](../../control-crosswalk.csv) e [revisão da v13.4](../research/revisao-v13.4.md).

## Linguagem normativa

- **MUST**: obrigatório quando o controle é aplicável.
- **SHOULD**: recomendado; uma exceção exige justificativa, responsável e prazo de revisão.
- **MAY**: opção permitida, sem alegação de equivalência ou certificação.
- `N/A` exige justificativa de escopo. Risco aceito é uma decisão governada, não um resultado de teste.

## Os 13 controles

### SSP-01 — Escopo, ativos e responsabilidade

O sistema MUST declarar escopo, limites, ativos importantes, tipos de dados, responsáveis e dependências externas. MUST haver um responsável pela decisão de risco e uma revisão quando a arquitetura, os dados ou os efeitos do sistema mudarem.

**Evidência mínima:** diagrama/inventário com data, owner, dependências e aprovação do escopo.

### SSP-02 — Modelagem de ameaças e fronteiras de confiança

O sistema MUST identificar atores, superfícies, fronteiras de confiança e cenários de abuso proporcionais ao impacto. Repositórios, prompts, resultados de ferramentas, documentos recuperados, memória e respostas externas MUST ser tratados como dados não confiáveis até validação.

**Evidência mínima:** modelo de ameaças versionado, caminhos de ataque e controles associados.

### SSP-03 — Identidade e autorização

O sistema MUST autenticar principals quando necessário e autorizar cada ação sobre o recurso e tenant corretos. Identidade, rede, UUID, JWT, sessão ou presença em um grupo MUST NOT ser tratados isoladamente como autorização suficiente. A permissão efetiva MUST seguir menor privilégio e expiração adequada.

**Evidência mínima:** matriz principal/ação/recurso, controles negativos de acesso e trilha de aprovação de privilégios.

### SSP-04 — Proteção de dados e privacidade

O sistema MUST minimizar coleta, retenção, cópia e exposição; proteger dados em trânsito e repouso conforme o risco; e definir acesso, uso, retenção, exclusão e resposta a incidentes. Requisitos legais e contratuais MUST ser identificados por jurisdição e caso de uso.

**Evidência mínima:** inventário/classificação, fluxo de dados e política de retenção/exclusão aprovada.

### SSP-05 — Configuração segura e falha fechada

Controles críticos MUST falhar de forma segura quando configuração, autenticação, integridade ou autorização estiverem ausentes ou inválidas. Credenciais padrão e exemplos MUST NOT permanecer ativos em produção. Proxy, WAF, rede privada, firewall, scanner ou configuração oculta não substituem autorização.

**Evidência mínima:** configuração efetiva e teste de ausência/erro de configuração crítica.

### SSP-06 — Entradas, APIs e lógica de negócio

O servidor MUST validar entradas, autorização, estados e invariantes de negócio. Valores fornecidos pelo cliente, cache, fila, webhook e modelo MUST NOT ser autoridade para pagamento, tenant, permissão ou estado privilegiado. Proteções MUST incluir limites de recurso, replay e abuso quando aplicáveis.

**Evidência mínima:** casos negativos e testes de abuso/regressão para as ações e regras críticas.

### SSP-07 — Dependências, origem e integridade de build

O sistema MUST manter inventário e origem de dependências e artefatos relevantes, usar resolução reproduzível quando disponível e revisar vulnerabilidades com contexto de exploração, exposição e impacto. Hash/Merkle identifica bytes frente a uma raiz confiável; não prova sozinho autor, produtor ou legitimidade. Alegações de SLSA MUST corresponder à versão, trilha e nível realmente verificados.

**Evidência mínima:** lockfiles, SBOM quando aplicável, provenance/assinatura verificadas e política de remediação.

### SSP-08 — Infraestrutura e isolamento

Serviços, bancos e planos administrativos MUST ser privados por padrão e expostos apenas por necessidade documentada. Regras de rede MUST ser testadas no caminho real; subnet, VLAN, VPN ou binding local não equivalem por si só a autorização ou isolamento.

**Evidência mínima:** diagrama de zonas, regras efetivas e prova de conectividade permitida e negada.

### SSP-09 — IA agentiva, memória e MCP

Modelo, prompt, ferramenta, servidor MCP, repositório, memória e resultado remoto MUST ser tratados como fronteiras de confiança. O modelo não concede autoridade: políticas fora do modelo MUST validar principal, ferramenta, recurso, tenant, ação e efeito. Agentes MUST receber apenas capacidades, dados, credenciais, rede, tempo e orçamento necessários.

Aprovação humana para ação de risco MUST vincular identidade do aprovador, ação e alvos exatos, plano/digest, risco, orçamento, validade e identificador da operação. Mudança relevante exige nova aprovação. Memória persistente MUST manter origem, escopo/tenant quando aplicável, integridade, revisão e processo de exclusão. MUST existir contenção e parada operacional testável para automação de risco.

**Evidência mínima:** matriz de capacidades, testes de injeção/abuso, aprovação vinculada ao plano e exercícios de contenção.

### SSP-10 — Confiabilidade, mudança e recuperação

Mudanças, filas e retries MUST tratar efeitos duplicados, falhas parciais e migrações. Backups MUST ser protegidos e sua restauração MUST ser exercitada na frequência definida pelo impacto. RTO/RPO e estratégia de recuperação MUST ser explícitos para sistemas que dependam deles.

**Evidência mínima:** plano de mudança/recuperação, resultado de restore e reconciliação de efeitos.

### SSP-11 — Logs, detecção e resposta

Eventos relevantes MUST permitir investigação e correlação sem registrar segredos ou dados além do necessário. Alertas, severidade, contenção, comunicação, preservação de evidências e recuperação MUST ter owners e procedimentos praticáveis.

**Evidência mínima:** amostras redigidas, regras de detecção e exercício de resposta com resultado e lacunas.

### SSP-12 — Verificação e decisão de release

Um `PASS` MUST citar critério, método e evidência atual vinculada ao código, artefato, configuração e ambiente avaliados. Evidência de outro commit ou digest não aprova o candidato atual. Scanner e cobertura são sinais parciais; requisitos arquiteturais, humanos ou legais podem exigir revisão própria.

A decisão final MUST ser `READY`, `NOT READY` ou `READY WITH ACCEPTED RISK`. `READY` exige controles aplicáveis aprovados e ausência de bloqueadores críticos. Risco aceito exige owner autorizado, justificativa, controles compensatórios, expiração e registro da aprovação.

**Evidência mínima:** pacote com IDs de controle, commit SHA, digest do artefato, ambiente, versão de ferramenta, comando/método, timestamps, resultados esperado/observado e referência verificável.

### SSP-13 — Acessibilidade, obrigações e melhoria contínua

O projeto MUST declarar obrigações legais, contratuais e de acessibilidade aplicáveis; MUST registrar fonte, versão, jurisdição, owner e data de revisão. Padrões de conscientização não MUST ser apresentados como lista completa de verificação. Mudanças em norma, ameaça, incidente ou arquitetura MUST abrir revisão proporcional.

**Evidência mínima:** matriz de aplicabilidade e registro versionado das revisões e decisões. Quando há interface, adote um alvo de acessibilidade explícito — por exemplo, WCAG 2.2 AA — e registre o método de avaliação e exceções.

## Aplicabilidade e resultado

Use o baseline para qualquer sistema com dados ou usuários. Acrescente os perfis de produção, alto impacto e crítico/regulado conforme risco e obrigação. Perfil não é nota de segurança e `N/A` não é atalho: documente ativos, limite e justificativa.

| Estado | Uso |
|---|---|
| `PASS` | Critério satisfeito com evidência atual suficiente. |
| `FAIL` | Critério não satisfeito, ou evidência contradiz o requisito. |
| `UNKNOWN` | Escopo, mecanismo ou evidência não permitiu decidir. |
| `N/A` | Não aplicável com justificativa técnica e aprovação apropriada. |
| `ACCEPTED RISK` | Exceção aprovada, limitada no tempo, com owner e controle compensatório. |

`PENDING LEGAL` e `PENDING EXTERNAL ACTION` descrevem trabalho em aberto; não são resultados aprovados. Mudança no artefato, ambiente, configuração ou fronteira pode invalidar evidência anterior. Defina a regra de validade antes da avaliação.

## Nove domínios preservados da fonte

1. Governança, arquitetura e Secure SDLC.
2. Identidade, autenticação, autorização, sessões e antiabuso.
3. Web, API, injeção e lógica de negócio.
4. Dados, bancos, RLS, privacidade e compliance.
5. Cloud, infraestrutura, segredos e supply chain.
6. Confiabilidade, resiliência, desempenho e disaster recovery.
7. Logs, auditoria, detecção e resposta a incidentes.
8. Testes, engenharia de qualidade e acessibilidade.
9. IA, RAG, agentes e MCP.

Ver [crosswalk](../../control-crosswalk.csv) para o mapeamento aos capítulos da fonte.
