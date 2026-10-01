# Provenance and use of source material

## Primary basis

| Field | Value |
|---|---|
| Source | Sovereign Security Protocol v13.4.0 |
| Source status | The source document declares `CANÔNICO` |
| Source date | 2026-09-29, as stated in the document |
| Public repository | [robertoatila/jarvis-skill-registry](https://github.com/robertoatila/jarvis-skill-registry) |
| Exact source commit | [`c263c2a2ffed5e7ddc50cc0584c04420df07ef5c`](https://github.com/robertoatila/jarvis-skill-registry/blob/c263c2a2ffed5e7ddc50cc0584c04420df07ef5c/docs/security/PROTOCOLO_SEGURANCA_v13.4_CANONICO.md) |
| Source path | `docs/security/PROTOCOLO_SEGURANCA_v13.4_CANONICO.md` |
| Git blob | `ede03fb9c6d5c744249e2bc8a4016d52a438c715` |
| SHA-256 of source bytes | `a83e8a27c02f5c57befc2cf0e9f0b7c8a020b2618a6f28ca55ce62b070f092f6` |
| Size / lines | 96,328 bytes / 6,678 lines |
| Repository copy | [`protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md`](../../protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md) |
| Source license | Apache-2.0; full text included at [`protocol/v13.4/LICENSE-APACHE-2.0.txt`](../../protocol/v13.4/LICENSE-APACHE-2.0.txt) |
| Content check | The repository copy was extracted directly from the named Git blob; its bytes and SHA-256 match |

The exact commit link is the provenance anchor. The source's declared canonical status describes that originating protocol; it does not make this independent community edition canonical.

## What this edition carries forward

- The nine domains and their broad control scope.
- The source's emphasis on risk, fail-closed behavior, least authority, current evidence, recovery, and continuous review.
- The source's agent, RAG, memory, tool, and MCP trust-boundary coverage.
- Traceability from each community control ID to ranges in the v13.4 source in [`control-crosswalk.csv`](../../control-crosswalk.csv).

## What this edition adds

- Stable community control IDs and equivalent English/PT-BR normative text.
- Explicit applicability, evidence, status, exception, and release-decision semantics.
- A provenance distinction between content hashes, signatures, authenticated identity, and verifiable build provenance.
- Exact-plan approval guidance for agent actions and a non-authoritative Obsidian projection contract.
- A dated reference map and an explicit review of source ambiguities in [`revisao-v13.4.md`](revisao-v13.4.md).

The full 6,678-line Portuguese source is now reproduced byte-for-byte at [`protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md`](../../protocol/v13.4/PROTOCOLO_INTEGRAL_v13.4_PT-BR.md). The root README links to it before the shorter community summary. Its canonical status remains the status declared by the originating file; the community edition is not a successor. This repository contains no local J.A.R.V.I.S. state or private Obsidian content.

## J.A.R.V.I.S. and Obsidian research boundary

The synthesis used the J.A.R.V.I.S. threat-model and trust-boundary material, the existing `CognitiveVaultBridge.sync_registry` ownership model, and the managed Markdown/Canvas projection design. The key lesson is to distinguish a documented target control from a mechanism demonstrated in a particular runtime. This repository carries that lesson forward as a normative requirement; it does not publish private vault content, telemetry, workspace settings, credentials, or a runtime audit report.

The Obsidian files in this repository are a public documentation view authored for this project. They do not sync into the user's existing vault and do not become runtime policy. Any future J.A.R.V.I.S. integration belongs in its existing canonical bridge, subject to that project's review and preservation rules.

## Attribution and license

The v13.4 source copy is redistributed under the source repository's Apache-2.0 license, with its exact source commit and license included. Original explanatory material authored specifically for this community edition is licensed as described in [`LICENSE`](../../LICENSE). Any future English translation of the source must be marked unofficial, linked to the same source commit, and preserve its license. Referenced standards and third-party materials keep their own licenses and terms.
