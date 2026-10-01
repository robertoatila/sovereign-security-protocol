# Protocolo de Segurança Soberana

**Uma base de segurança verificável para software, infraestrutura e sistemas de IA com agentes.**

[English](README.md) · [Português (PT-BR)](README.pt-BR.md)

| Base de origem | Edição neste repositório | Revisão das referências |
|---|---|---|
| SSP v13.4.0 | Community Edition 0.1.0 — proposta | 2026-10-01 |

Este projeto transforma o **Protocolo de Segurança Soberana v13.4.0** em uma base pública, bilíngue e rastreável. Mantém os nove domínios da fonte e organiza requisitos em 13 controles portáveis, com critérios de aplicabilidade, evidências e decisões de release.

> A fonte v13.4.0 continua sendo a referência de origem. Esta edição comunitária propõe uma estrutura de adoção; ela não se declara versão canônica, certificação, auditoria concluída ou garantia de segurança.

## Comece aqui

- [Protocolo e 13 controles — PT-BR](docs/pt-BR/protocolo.md)
- [Protocol and 13 controls — English](docs/en/protocol.md)
- [Adoção e evidências — PT-BR](docs/pt-BR/adocao-e-evidencias.md)
- [Adoption and evidence — English](docs/en/adoption-and-evidence.md)
- [Perfil de IA agentiva, J.A.R.V.I.S. e Obsidian — PT-BR](docs/pt-BR/agentes-jarvis-obsidian.md)
- [Agentic AI, J.A.R.V.I.S. and Obsidian profile — English](docs/en/agentic-jarvis-obsidian.md)
- [Rastreabilidade para a SSP v13.4](control-crosswalk.csv)
- [Vault e mapa visual do Obsidian](obsidian/README.md) · [Canvas](SSP-13.4.canvas)
- [Proveniência e referências oficiais](docs/research/provenance.md) · [fontes normativas](docs/research/references.md)
- [Revisão e melhorias propostas](docs/research/revisao-v13.4.md) · [roteiro](ROADMAP.md)
- [Metadados sugeridos para publicação](PUBLICATION.md)

## O que entrega

- Requisitos curtos com IDs estáveis, versões PT-BR e EN alinhadas e ligações às seções da fonte.
- Uma forma explícita de registrar `PASS`, `FAIL`, `UNKNOWN`, `N/A` e risco aceito sem transformar ausência de evidência em aprovação.
- Evidências vinculadas ao commit, artefato, ambiente e execução que realmente foram avaliados.
- Um perfil específico para agentes e MCP: limites de autoridade, permissões por ferramenta/recurso, conteúdo não confiável e aprovações vinculadas à ação exata.
- Orientação para usar o repositório como vault Obsidian sem exportar o cofre privado do usuário nem criar um segundo sincronizador J.A.R.V.I.S.
- Um mapa de fontes oficiais com versão e data de revisão. As versões de normas e especificações precisam ser rechecadas antes de cada adoção ou publicação.

## Modelo mental

```text
ESCOPO → AMEAÇAS → CONTROLES → EVIDÊNCIAS → DECISÃO → OBSERVAR → RECUPERAR → APRENDER
```

Um scanner, hash, build aprovado, arquivo Markdown ou declaração de agente é uma entrada para a avaliação; nenhum deles, isoladamente, prova que o sistema está seguro.

## Perfis de adoção

1. **Base:** qualquer sistema que processe dados ou tenha usuários.
2. **Produção:** autenticação, disponibilidade, dados pessoais, APIs e releases reais.
3. **Alto impacto:** multi-tenant, pagamento, dados sensíveis ou automação com efeitos relevantes.
4. **Crítico/regulado:** requisitos legais, contratuais e setoriais definidos com os responsáveis competentes.

Os perfis superiores acrescentam rigor; não removem o baseline. O escopo e os controles aplicáveis precisam ser justificados para cada sistema.

## Limites

Este documento não é uma transcrição integral nem uma declaração de cobertura linha a linha da fonte v13.4. Ele não substitui uma avaliação profissional, uma norma setorial, aconselhamento jurídico, teste de invasão ou controles operacionais. Não certifica o runtime J.A.R.V.I.S., o conteúdo de um vault Obsidian, uma organização ou qualquer implantação. Leis, prazos, versões e requisitos dependem de jurisdição e contexto.

O número de estrelas é uma medida de adoção, não uma evidência de segurança. O objetivo é tornar o material útil, citável, traduzível e fácil de revisar pela comunidade; nenhuma contagem de estrelas é prometida.

## Contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md), [VERSIONING.md](VERSIONING.md) e [SECURITY.md](SECURITY.md). Mudanças normativas devem citar fonte, explicar risco e manter as traduções e o crosswalk sincronizados.
