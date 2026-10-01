# Agentic AI, J.A.R.V.I.S., and Obsidian profile

This profile applies the SSP to agents with memory, tools, delegation, workspace access, or MCP connections. It states requirements; it does not attest that any J.A.R.V.I.S. runtime implements them.

## Authority model

An agent is a principal with limited capabilities. Effective authorization MUST be enforced outside the model and intersect at least:

```text
authorized mission ∩ principal identity ∩ agent profile
∩ tool policy ∩ resources/targets ∩ environment ∩ risk policy
```

A lower layer may restrict a permission; it must not expand it. Text returned by a repository, document, search, tool, MCP server, memory, or remote node may inform a decision but cannot by itself change the mission, policy, or approval.

## Approval bound to the action

A generic confirmation, boolean flag, click, or typed name does not prove identity or authorization for an effect. For risky actions, bind the approval record to:

- authenticated approver identity and role;
- principal/agent that will execute;
- action and complete set of targets/resources;
- digest of the plan/arguments to be executed;
- risk, cost/time limits, and permissions;
- operation/tenant, expiry, and single-use or retry policy;
- verifiable decision and result record.

Any change to approved content, target, scope, tool, digest, or relevant environment invalidates the approval and requires a new decision. Recheck permission immediately before dispatch against the actual adapter and effects.

## Boundaries for agents and MCP

- Tools, MCP sources, and versions need known owners, origins, capabilities, scopes, update paths, network, filesystem, credentials, and revocation processes.
- Authorize each call for the intended resource and tenant. Tool names and descriptions are not a security boundary.
- Shell and network start disabled when unnecessary. When enabled, use a sandbox, allow-list, timeout, cost limits, filesystem limits, and egress restrictions.
- Do not expose secrets to prompts, context, output, telemetry, or a vault. Materialize narrow secret references at the consumer; redaction is an added defense, not permission to persist raw data.
- Give agents short-lived, scoped credentials when needed; define revocation/rotation after suspected exposure.
- Protect delegation: a subagent cannot inherit more authority than the approved chain or expand budget, scope, or access.
- Track memory source, author, tenant, scope, integrity, review, and deletion. External content does not become trusted policy just because it is remembered.
- Test cancellation, limits, and safe stop for operations that can change data, accounts, or infrastructure.

For MCP integration, check the current protocol revision; the public revision referenced here was published on **2026-07-28**. SDK, schema, OAuth, and extension compatibility can change independently of this profile.

## Applying this to J.A.R.V.I.S.

The J.A.R.V.I.S. repository already has `CognitiveVaultBridge.sync_registry` and a managed Markdown/Canvas projection model. That architecture is the integration reference; this repository does not create a second bridge, skill selector, server, or execution authority.

J.A.R.V.I.S. threat-model and trust-boundary documents inform the threat and integration model. This project preserves the distinction between a desired control and an observed mechanism: an architectural description is a requirement and investigation lead, not proof of implementation or certification. Evidence must be collected for the specific runtime and candidate.

To bring these controls into J.A.R.V.I.S., maintainers should map SSP IDs to the existing canonical source, planner, receipts, and gates; add integration only after ownership, scope, and evidence review. Approval remains bound to an exact plan and digest; an Obsidian projection does not decide or execute missions.

## Applying this to Obsidian

Open the repository root as a vault. `SSP-13.4.canvas` and `00 - SSP Home.md` are read-only indexes into versioned files. Markdown is the textual source; the Canvas and graph are not authorization sources.

The human vault remains user-owned content. In a real integration, update only managed regions, preserve human text and non-projection nodes/edges, make a recoverable backup, and write a receipt. Use an explicit ownership namespace. `jarvis:projection:` belongs to the J.A.R.V.I.S. projector; this public Canvas uses its own `ssp:` IDs and must not be copied over a private Canvas.

Do not publish local memory, personal notes, execution history, Obsidian settings, workspace state, secrets, or copies of private vaults in this project.
