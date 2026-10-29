---
name: "Stack Blueprint / Exemplo de Camada (PT-BR & EN)"
about: "Propose a hardened code/config example for a specific stack (Rust, Go, K8s, Java, Mobile, MCP)"
title: "[Blueprint] "
labels: ["enhancement", "blueprint"]
---

## Target Stack & Layer / Stack e Camada Alvo
- **Stack / Linguagem:** (e.g., Go + Gin, Rust + Axum, Kubernetes NetworkPolicy, Next.js, MCP Server)
- **SSP Layer (1–7) & Control IDs:** (e.g., Layer 2 / `SSP-03`, Layer 5 / `SSP-08`)

## Threat / Problema Real Evitado
Explain the common vulnerability or production misconfiguration this snippet prevents (PT-BR or EN).

## ❌ Vulnerable vs. ✅ Hardened Pattern
Provide a minimal, original, license-clean code/configuration snippet showing both the anti-pattern and the SSP-hardened defense.

## Verification Method / Como Testar
How can an adopter deterministically verify this layer (`pytest`, `curl`, `ssp.py scan`, SQL test)?
