# Reference map / Mapa de referências

**Reviewed/revisado:** 2026-10-01. This is a dated snapshot, not an evergreen claim. Recheck official sources before adopting a control or publishing a release.

| Area / Área | Primary source / Fonte primária | Status recorded / Estado registrado | Use in this edition / Uso nesta edição |
|---|---|---|---|
| Source SSP | [SSP v13.4.0 at commit `c263c2a`](https://github.com/robertoatila/jarvis-skill-registry/blob/c263c2a2ffed5e7ddc50cc0584c04420df07ef5c/docs/security/PROTOCOLO_SEGURANCA_v13.4_CANONICO.md) | Source declares `CANÔNICO` | Basis and traceability |
| Application security | [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | 5.0.0 identified as the stable release on the project page | Verifiable application-security requirements |
| Awareness | [OWASP Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 2025 edition | Awareness and risk vocabulary; not a complete control checklist |
| Secure development | [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST publication list](https://csrc.nist.gov/projects/ssdf/publications) | SSDF 1.1 final; SP 800-218 Rev. 1 / SSDF 1.2 listed as draft | Secure SDLC outcomes and provenance practices |
| GenAI development | [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) · [NIST AI RMF GenAI Profile, AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | Published profile documents | AI lifecycle risk and secure development context |
| Agentic applications | [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 2026 project resource, published 2025-12-09 | Agentic threat vocabulary and assessment prompts |
| Supply-chain assurance | [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/) · [Provenance](https://slsa.dev/spec/v1.2/provenance) | v1.2 marked Approved | Provenance and verified-property terminology |
| Vulnerability priority | [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST CVSS](https://www.first.org/cvss/) · [FIRST EPSS](https://www.first.org/epss/) | Living resources | Combine known exploitation, severity, likelihood, exposure, and asset impact without a universal formula |
| Identity | [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [RFC 10017](https://www.rfc-editor.org/rfc/rfc10017.html) | Both RFC Editor pages classify these as Best Current Practice | OAuth security and browser-based application architecture |
| MCP | [MCP specification, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | Official revision page available; referenced version as of this review date | Version-pinned MCP example; verify current auth and transport rules before adoption |
| Incident response | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Final, published 2025-04-03 | Preparation, response, and recovery lifecycle |
| Accessibility | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | W3C Recommendation, updated publication 2024-12-12 | Accessibility target for user interfaces; not a security certification |
| Normative terms | [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) · [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html) | RFCs define interpretation of capitalized requirement terms | Interpret `MUST`, `SHOULD`, and `MAY` |

## Regulatory and contractual requirements

The source references LGPD, GDPR, HIPAA, and PCI DSS. This community edition does not reproduce legal deadlines or claim that one mapping satisfies a regulation. Identify applicable law, sector rules, contracts, regulator guidance, and data-residency requirements for the system's jurisdiction, then have qualified owners review them. Record the authoritative version and review date in the project's own applicability matrix.

## Reference maintenance

- Each update records the exact edition/revision, status, primary URL, and date checked.
- A draft, proposal, preview, SDK implementation, or marketing page is not silently substituted for an approved specification.
- When a source changes, identify affected control IDs and explain whether the update changes a requirement, its example, or only its citation.
- Keep a dated snapshot in pull requests so reviewers can tell what was current when the change was made.
