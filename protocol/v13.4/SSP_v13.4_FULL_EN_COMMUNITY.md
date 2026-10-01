# Security Protocol v13.4.0 — Complete English Community Translation

> **Translation status:** Community translation; not the canonical source text.
> **Reference:** The complete source is [Portuguese (PT-BR)](./PROTOCOLO_INTEGRAL_v13.4_PT-BR.md), preserved from J.A.R.V.I.S. source commit c263c2a2ffed5e7ddc50cc0584c04420df07ef5c.
> Use the Portuguese source to resolve wording or interpretation differences. The security requirements below are translated from the complete v13.4 source.

---
🔐 SECURITY PROTOCOL v13.4

Version: 13.4.0
Base date: 09/29/2026
Status: CANONICAL
Replaces: v7 v8 v9 v10 v11 v12 v13 v13.1 v13.2 v13.3
Model: Secure by Design + Production Engineering
Trigger: "SECURITY"

«A system is not ready for production just because it compiles.

A control doesn't exist just because there is related code.

PASS requires implementation + evidence + testing + verifiable result.”

---

0.0 DELTA v13 — IMPROVEMENTS OVER v12

v13 preserves the 9 domains and adds:

- RELEASE GATE separated into SECURITY + QUALITY + RELIABILITY + PRIVACY/COMPLIANCE;
- evidence freshness linked to commit, artifact and environment;
- SLSA 1.2 and explicit provenance verification;
- prioritization of vulnerabilities with KEV + EPSS + CVSS 4.0 + SSVC/context;
- release safety controls, migrations, queues and feature flags;
- expansion of AI/RAG/Agents/MCP with OWASP 2026 references;
- explicit protection against tool poisoning, rug pull, excessive agency and memory poisoning;
- budget and kill switch for loops/agents;
- authorization per tool and per resource in MCP;
- blocker criteria for cross-tenant RAG/MCP and artifact provenance mismatch;
- finding format with mapping to patterns and exploration context;
- audit of insecure defaults with Trail of Bits `insecure-defaults`;
- mandatory fail-closed for critical flags like `REQUIRE_AUTH`;
- private Docker databases by default, without port publishing to the host when not necessary;
- default/dev credentials prohibited in production and mandatory rotation after suspected exposure;
- explicit segmentation between client/guest network, application, administration and data;
- subnetting without ACL/firewall does not count as isolation;
- microsegmentation and service-specific connectivity for critical workloads;
- private management plane, without SSH/RDP/administrative panels exposed directly to the Internet;
- reverse proxy/WAF/CDN/DMZ can reduce exposure, but obfuscation does not replace AuthN/AuthZ;
- specific rules for Docker/firewall, including risk of published ports bypassing UFW policies;
- public source maps treated as exposure control;
- `.env`, environment files and public config dumps treated as blockers;
- price, discount, tax, total and payment status validated on the server;
- sensitive webhooks require verifiable signature and replay protection;
- security checks are now expressed as automatable gates, not just checklists;
- reinforced server-side validation as authority for inputs and business invariants;
- AI agents are now treated as principals capable of reading workspace/env/tools according to permissions;
- real credentials must not exist in the agent's workspace without explicit need and minimum scope;
- choice of package manager is not a security boundary: npm/pnpm/yarn/Bun require the same supply chain gates;
- continuous monitoring of CVEs/dependencies becomes an explicit operational requirement;
- accounts and administrative surfaces must be separated from common use; Isolated administrative plan is preferable at higher risk;
- password hashing requires single salt managed by trusted implementation; do not create a manual salt/crypto mechanism;
- WAF/CDN/Cloudflare-equivalent is optional edge defense and never replaces AuthN/AuthZ/validation.
- invalid evidence when produced by a commit/artifact other than the one that goes into production.

Rule:

EVIDENCE FROM OLD COMMIT
≠
PASS FOR CURRENT RELEASE

RELEASE
=
SECURITY PASS
+
QUALITY PASS
+
RELIABILITY PASS
+
PRIVACY/COMPLIANCE PASS WHEN APPLICABLE

---

0. OBJECTIVE

This protocol establishes the baseline for:

- web applications;
- SaaS;
- APIs;
- backends;
- multi-tenant systems;
- databases;
- storage;
- business systems;
- financial applications;
- systems with personal data;
- cloud;
- containers;
- CI/CD;
- supply chain;
- caches;
- queues;
- WebSockets;
- webhooks;
- OAuth/OIDC;
- Generative AI;
- RAG;
- agents;
- MCP;
- infrastructure;
- observability;
- disaster recovery;
- accessibility;
- architectural documentation.

The protected cycle becomes:

DESIGN
↓
IMPLEMENT
↓
REVIEW
↓
TEST
↓
BUILD
↓
DEPLOY
↓
PLEASE NOTE
↓
RESPOND
↓
RECOVER
↓
LEARN

---

0.1 CANONICAL REFERENCES

Application security

- OWASP Top 10:2025;
- OWASP ASVS 5.0.0;
- OWASP API Security Top 10:2023;
- OWASP Cheat Sheet Series;
- OWASP Automated Threats;
- OWASP Bot Management;
- OWASP Credential Stuffing Prevention.

OWASP Top 10:2025 is the current version and includes Broken Access Control, Security Misconfiguration, Software Supply Chain Failures, Cryptographic Failures, Injection, Insecure Design, Authentication Failures, Integrity Failures, Logging/Alerting Failures, and Mishandling of Exceptional Conditions.

For technical verification, ASVS 5.0.0 should take precedence over treating the Top 10 as a checklist, as OWASP itself recommends ASVS as a verifiable standard for design, code review and testing.

---

Identity

- NIST SP 800-63-4;
- NIST SP 800-63B-4;
- RFC 8725;
- RFC 9700;
- RFC 10017.

NIST SP 800-63B-4 is final as of July 2025.

RFC 10017, published in August 2026, formalizes OAuth 2.0 for browser applications. The BFF standard keeps access/refresh tokens outside of JavaScript and is strongly recommended for business, sensitive applications that process personal data.

---

Secure SDLC and supply chain

- NIST SP 800-218 SSDF 1.1;
- NIST SP 800-218A;
- CISA KEV;
- SBOM;
- provenance;
- artifact signing;
- SLSA 1.2;
- CVSS 4.0;
- EPSS;
- CISA SSVC.

SSDF 1.1 remains the final version; SP 800-218 Rev. 1 / SSDF 1.2 remains draft September 2026.

SLSA 1.2 is the current approved version and adds/structures Build and Source trails, provenance, and verified properties.

CVSS should not be used in isolation for prioritization. Match technical severity with actual exploitation, probability of exploitation, exposure, asset criticality and impact.

---

AI, agents and MCP

- OWASP GenAI LLM Top 10 2026;
- OWASP Top 10 for Agentic Applications 2026;
- OWASP MCP Top 10;
- OWASP Practical Guide for Secure MCP Server Development;
- NIST SP 800-218A.

Generative AI, agents and MCP are treated as explicit trust boundaries.

Model output, tool output, retrieved context, memory and external content remain untrusted until validation and authorization.

---

Incident Response and Continuity

- NIST CSF 2.0;
- NIST SP 800-61 Rev. 3;
- NIST SP 800-34 Rev. 1.

NIST SP 800-61 Rev. 3 is the current final recommendation for integrating incident response into risk management.

---

Accessibility

Baseline:

WCAG 2.2
LEVEL AA

WCAG 2.2 is W3C Recommendation and Level AA includes criteria A and AA.

---

Privacy and Compliance

According to applicability:

- LGPD;
- ANPD regulations;
- GDPR;
- HIPAA;
- PCI DSS 4.0.1.

PCI DSS 4.0.1 remains the current published version as of August 2026.

---

0.2 THE 9 DOMAINS

PART 1
Governance, Architecture and Secure SDLC

PART 2
Identity, AuthN, AuthZ, Sessions and Anti-Abuse

PART 3
Web, API, Injection and Business Logic

PART 4 ​​
Data, Database, RLS, Privacy and Compliance

PART 5
Cloud, Infrastructure, Secrets and Supply Chain

PART 6
Reliability, Resilience, Performance and DR

PART 7
Logging, Audit, Detection and Incident Response

PART 8
Testing, Quality Engineering and Accessibility

PART 9
AI, RAG, Agents and MCP

---

0.3 LEVELS

Level| Application
🟢 BASIC | any application with real user
🟡 INTERMEDIATE | production, SaaS, authentication, PII
🔴 ADVANCED| multi-tenant, financial, scale
⚫ MAXIMUM SAFE | high impact, regulated, critical

Flow:

COMPLETE BASIC
↓
INTERMEDIATE
↓
ADVANCED
↓
MAXIMUM SAFE

---

0.4 CONTROL STATUS

Only use:

PASS
FAIL
UNKNOWN
N/A
PENDING EXTERNAL ACTION
LEGAL PENDING
ACCEPTED RISK

PASS

It requires objective evidence.

UNKNOWN

Unable to verify.

N/A

There is a technical justification for non-applicability.

ACCEPTED RISK

Requires:

RISK
JUSTIFICATION
OWNER
COMPENSATORY CONTROL
EXPIRATION
APPROVAL

---

0.5 DEFINITION OF DONE

A critical control only receives PASS with:

- [ ] implementation;
- [ ] test;
- [ ] evidence;
- [ ] expected result;
- [ ] real result;
- [ ] owner;
- [ ] date;
- [ ] regression when possible.

For critical controls, evidence should record where applicable:

- CONTROL ID;
- standard mapping;
- commit SHA;
- artifact digestion;
- environment;
- command/test executed;
- timestamp;
- tool/version;
- raw result or verifiable reference.

Evidence from another commit, another artifact, or another environment does not prove the current release without explicit justification.

Example:

CONTROL:
Tenant isolation

IMPLEMENTATION:
TenantAuthorizationService

TEST:
Tenant A → resource B

EXPECTED:
403 / 404

CURRENT:
403

EVIDENCE:
integration test

OWNER:
Backend

REGRESSION:
CI

---

0.6 SECURITY / PRODUCTION BLOCKERS

Production must be blocked for:

- active secret exposed;
- credential leak;
- RCE;
- Exploitable SQL Injection;
- command injection;
- auth bypass;
- critical privilege escalation;
- cross-tenant access;
- IDOR/BALL critical;
- privileged mass assignment;
- insecure password storage;
- exposed sensitive seat;
- public sensitive storage;
- critical vulnerability actively exploited without mitigation;
- supply-chain compromise;
- build not validated;
- destructive migration without recovery plan;
- critical authorization failure;
- known data corruption;
- DR required without recoverable backup;
- release produced from an artifact other than the validated one;
- provenance/signature/digest incompatible with the approved artifact;
- cross-tenant leak in RAG, vector DB, agent memory or MCP;
- agent/MCP with broad destructive capacity without authorization and compensatory controls;
- mandatory restore failing or not verifiable;
- critical migration without testable rollback/roll-forward/recovery;
- applicable and exposed KEV vulnerability without formal fix or mitigation;
- critical auth/admin with no minimum telemetry to detect known abuse;
- fallback mechanism that transforms security failure into allow;
- sensitive database published on the public interface without architectural need and without compensatory controls;
- PostgreSQL/Redis/MySQL/MongoDB exposed to the Internet by `ports:`/host binding when it should be internal only;
- default credential, example, dev or known active in production;
- `POSTGRES_HOST_AUTH_METHOD=trust` or equivalent passwordless authentication on reachable surface;
- critical security flag missing resulting in permissive state (`REQUIRE_AUTH` missing → auth off);
- `.env`, dump, sensitive config or publicly accessible secret file;
- frontend authorized to unilaterally define payment amount/status;
- financial/privileged webhook processed without authenticity verification when signature is supported/required;
- public source map containing secrets or sensitive material;
- production relying exclusively on client-side validation for critical rules;
- production credential accessible to agent/workspace without need, scope or compensatory control;
- known vulnerable dependency/applicable KEV exposed without documented decision;
- shared administrative account or permanent administrative privileges without need on critical system.

---

PART 1 — GOVERNANCE, ARCHITECTURE AND SECURE SDLC

🟢 BASIC

1.1 Inventory

Map:

- frontend;
- backend;
- APIs;
- bank;
- cache;
- queues;
- storage;
- WebSockets;
- webhooks;
- domains;
- subdomains;
- cloud;
- CI/CD;
- integrations;
- third parties;
- repositories;
- environments;
- secrets;
- certificates;
- AI;
- MCP;
- owners.

---

1.2 Data Classification

PUBLIC
INTERNAL
CONFIDENTIAL
SENSITIVE
CRITICAL

Inventory:

- PII;
- credentials;
- tokens;
- financial data;
- documents;
- business data;
- fingerprints;
- telemetry;
- biometrics;
- logs.

---

1.3 Trust Boundaries

Produce diagram showing:

INTERNET
↓
EDGE
↓
FRONTEND
↓
BACKEND
↓
DATA LAYER
↓
THIRD PARTIES

Borders must be dealt with explicitly.

---

1.4 Secure Defaults

DEFAULT DENY

- private endpoints by default;
- debug turned off;
- minimum permissions;
- private storage;
- private experimental resources;
- protected administrative actions.

---

🟡 INTERMEDIATE

1.5 Threat Modeling

For critical features:

STRIDE
+
ABUSE CASES
+
BUSINESS LOGIC
+
TRUST BOUNDARIES

Analyze:

- spoofing;
- tampering;
- repudiation;
- disclosure;
- denial of service;
-elevation of privilege.

---

1.6 Abuse Cases

Ask:

What if I change the ID?

What if you change tenant?

What if I ignore the frontend?

What if you repeat the action?

What if you use 10,000 IPs?

What if I send two requests simultaneously?

What if the order of operations is reversed?

What if an account is compromised?

And if you compromise an admin?

What if an external dependency lies?

---

1.7 Risk Register

Each risk:

ID
ASSET
THREAT
VULNERABILITY
LIKELIHOOD
IMPACT
OWNER
MITIGATION
RESIDUAL RISK
DEADLINE
STATUS

---

1.8 Code Review

Review must check:

- correctness;
- security;
- AuthN;
- AuthZ;
- tenant isolation;
- data access;
- validation;
- competition;
- errors;
- observability;
- performance;
- accessibility;
- tests.

OWASP also explicitly recommends server-side authorization, fail-safe defaults, and session/IDOR review in code review.

---

1.9 CODEOWNERS

Use for critical areas when possible:

- authentication;
- payment;
- authorization;
- migrations;
- CI/CD;
- cloud;
- crypto;
- security configuration.

---

🔴 ADVANCED

1.10 Architecture Review

Required for:

- auth;
- multi-tenancy;
- payment;
- storage;
- encryption;
- cache;
- queues;
- public APIs;
- AI/agents;
- MCP;
- network architecture.

---

1.11 Architecture Diagrams

Keep in repository:

System Context

USERS
↓
SYSTEM
↓
EXTERNAL SYSTEMS

Containers

BROWSER
↓
FRONTEND
↓
BACKEND
↓
DATABASE

↘ CACHE
↘ STORAGE
↘ QUEUE

Deployment

Show:

- cloud;
- regions;
- proxies;
- CDN;
- instances;
- database;
- storage;
- network boundaries.

Data Flow Diagram

Show sensitive data crossing systems.

Security Architecture

Show:

- AuthN;
- AuthZ;
- tenant;
- secrets;
- KMS;
- audit logs;
- WAF;
- bot defense;
- backups.

---

1.12 ADR — Architecture Decision Records

Recommended directory:

docs/adr/

Format:

# ADR-XXX — Decision

## Status

## Context

## Decision

## Alternatives

## Consequences

## Security Impact

## Reliability Impact

## Data/Privacy Impact

## Rollback

ADRs for important decisions:

- auth;
- sessions;
- JWT;
- BFF;
- multi-tenancy;
- database;
- RLS;
- cache;
- queue;
- storage;
- encryption;
- rate limiting;
- logging;
- backup;
- AI/MCP.


---

1.13 Control Mapping

Critical controls must, when applicable, map to stable references:

- OWASP ASVS `v5.0.0-x.y.z`;
- OWASP Top 10:2025;
- OWASP API Security Top 10:2023;
- NIST SSDF;
- NIST 800-63-4;
- PCI DSS;
- WCAG 2.2;
- OWASP GenAI / Agentic / MCP.

Do not use only a generic name when there is a verifiable versioned requirement.

---

1.14 Security Requirements as Code/Policy

When feasible:

REQUIREMENT
↓
CONTROL
↓
TEST
↓
CI GATE
↓
EVIDENCE

Repeatable critical policies must migrate from manual documentation to automated validation without eliminating human review.

---

1.15 Insecure Defaults Audit

Missing configuration should fail to safe state.

Examples prohibited in production:

`REQUIRE_AUTH` missing → authentication turned off

`DEBUG` missing → debug on

`TLS_VERIFY` missing → check off

`SECRET_KEY` missing → example secret

`ADMIN_PASSWORD` missing → known password

Rule:

MISSING SECURITY CONFIG
→ FAIL CLOSED / FAIL FAST

No:

MISSING SECURITY CONFIG
→ CONTINUE INSECURE

Audit:

- fallback secrets;
- default credentials;
- fail-open switches;
- weak crypto defaults;
- permissive ACL/CORS/file modes;
- debug leakage.

For real finding, try:

DEFAULT REACHABLE
+
INSECURE VALUE ACTIVE
+
SECURITY SINK
+
PRODUCTION REACHABILITY

---

1.16 Fail-Closed Configuration Contract

Each critical security configuration must declare:

- name;
- secure default;
- behavior when absent;
- behavior when invalid;
- environmental scope;
- owner;
- test;
- startup validation.

For production, prefer:

CONFIG INVALID / MISSING
→ STARTUP FAILURE

instead of silent fallback.

---

⚫ MAXIMUM SAFE

- formal AppSec;
- architecture board;
- security champion;
- formal risk acceptance;
- independent audits;
- vulnerability disclosure;
- supplier governance;
- executive metrics;
- table top exercises;
- separation of duties.

---

PART 2 — IDENTITY, AUTHENTICATION, AUTHORIZATION, SESSION AND ANTI-ABUSE

🟢 BASIC

2.1 Password Storage

Prefer:

ARGON2ID
↓
SCRYPT
↓
BCRYPT / PBKDF2 when justified

OWASP recommends Argon2id for new systems; a currently documented minimum profile is 19 MiB, two iterations, and 1 parallelism, although the configuration must be calibrated to the environment.

Salt:

- unique by password;
- random;
- generated by trusted library/implementation;
- stored next to the hash when the algorithm defines it;
- not treated as secret;
- never manually reused between users.

Argon2id, bcrypt and PBKDF2 usually already integrate/manage salt by proper implementation.

Do not implement:

CUSTOM SALT SCHEME
CUSTOM PASSWORD CRYPTO
FAST HASH + MANUAL SALT

as a replacement for dedicated password hashing.

Never:

PLAINTEXT
MD5
SHA-1
SHA-256(password)
REVERSIBLE PASSWORD ENCRYPTION

---

2.2 Password Policy

NIST SP 800-63B-4 states:

SINGLE FACTOR:
minimum 15 characters

MFA PART:
minimum 8

Also:

- allow 64+ characters;
- password manager;
- autofill;
- paste;
- blocklist of compromised passwords;
- no arbitrary composition;
- no mandatory periodic exchange without commitment.

---

2.3 Authentication

Server is authority.

REQUEST
↓
CREDENTIAL / SESSION
↓
VALIDATION
↓
IDENTITY
↓
ACCOUNT STATE

Frontend redirect:

if (!user) ...

it's UX.

Not enough security.

---

2.4 Recovery

- random token;
- single-use;
- TTL;
- store safely;
- rate limit;
- anti-enumeration response;
- invalidate after use;
- notify change;
- review sessions;
- do not rely on arbitrary "Host" to build link.

---

🟡 INTERMEDIATE

2.5 MFA

Mandatory according to risk for:

- owner;
- admin;
- infrastructure;
- cloud;
- secrets;
- critical functions.

Preference:

PASSKEY/WEBAUTHN
↓
TOTP
↓
SUITABLE FALLBACK

---

2.6 Biometrics

BIOMETRIC≠
SERVER-STORED PASSWORD

Prefer:

BIOMETRIC LOCATION
↓
UNLOCK PRIVATE KEY
↓
WEBAUTHN
↓
SERVER VERIFIES SIGNATURE

NIST does not consider isolated biometrics to be an authenticator and prefers local biometric verification associated with a physical authenticator.

---

2.7 Session Lifecycle

Every session has:

CREATE
↓
ROTATE
↓
USE
↓
REFRESH
↓
EXPIRE
↓
REVOKE
↓
DESTROY

Set:

- idle timeout;
- absolute timeout;
- renewal;
- recall;
- concurrent-session policy.

Do not use universal times for all systems.

---

2.8 Cookies

When applicable:

Cookie Set:
__Host-session=<random>;
Secure;
HttpOnly;
SameSite=Lax;
Path=/

"SameSite=Strict" when supported.

OWASP recommends session-wide TLS and "Secure" attribute for session cookies.

---

2.9 Session Fixation

Rotate handle after:

- login;
- increase in privilege;
- sensitive context changes.

---

2.10 Logout

Logout should actually revoke access when the mechanism supports it.

Don't just remove visual state.

---

2.11 OAuth/OIDC

Prefer:

AUTHORIZATION CODE
+
PKCE

Follow RFC 9700.

For highly demanding browsers:

BROWSER
↓ secure cookie
BFF
↓ token
RESOURCE SERVER

RFC 10017 describes BFF as a standard that keeps access/refresh tokens outside of JavaScript.

When BFF is applicable:

- secure session cookie;
- OAuth tokens maintained server-side;
- CSRF considered;
- Minimum CORS;
- session rotation;
- token revocation according to architecture;
- backend continues running AuthZ per resource/action.

Token-mediating backend is less secure than BFF because access token still reaches the browser.

Browser-only OAuth client must be architectural exception aware and follow Authorization Code + PKCE.


---

2.12 JWT

JWT is an architectural option.

No requirement.

If used:

- algorithm allow-list;
- mandatory signature;
- "iss";
- "aud";
- "exp";
- type/purpose;
- key validation;
- replay strategy;
- token separation.

Never:

JWT role=ADMIN
=
AUTOMATIC AUTHORIZATION

---

2.13 Authorization

IDENTITY
↓
ROLE / ATTRIBUTES
↓
PERMISSIONS
↓
TENANT
↓
RESOURCE
↓
ACTION

---

2.14 RBAC

Papers must be discovered in the application.

Example:

OWNER
ADMIN
MANAGER
EMPLOYEE
VIEWER

---

2.15 ABAC

When necessary consider:

- tenant;
-device;
- risk;
- time;
- location;
- state;
- sensitivity;
- transaction type.

---

2.16 Multi-Tenant Isolation

Every operation responds:

WHO?
TENANT?
RESOURCE?
ACTION?
PERMISSION?

Conceptually:

WHERE resource_id = :resource
AND tenant_id = :authenticatedTenant

Tenant received in the body is not a source of authority.

---

2.17 Tenant Isolation must achieve

Not just SQL.

Also:

- database;
- cache;
- object storage;
- search indexes;
- DB vector;
- queues;
- WebSockets;
- exports;
- logs;
- reports;
- background jobs;
- analytics.

---

2.18 UUID

UUID
≠
ACCESS CONTROL

---

2.19 Mass Assignment

Explicit allow-list.

Never save indiscriminately:

req.body

Protected fields include:

- scroll;
- permissions;
- tenant;
- owner;
- admin;
- verified;
- balance;
- internalPrice;
- privileged status.

---

2.20 Step-Up Authentication

Require according to risk for:

- change password;
- change email;
- change MFA;
- transfer owner;
- create admin;
- export data;
- exclude company;
- payment;
- secrets;
- impersonation.

---

2.20.1 Privileged Account / Admin Plane Separation

Daily Use Account
≠
Administrative account

For privileged roles:

- separate administrative identity when feasible;
- MFA/passkey;
- step-up;
- shorter session;
- reinforced logging/audit;
- no shared admin account;
- least privilege;
- JIT/JEA when available;
- network/device restriction according to risk.

In higher criticality, prefer:

PUBLIC USER APP
≠
ADMIN / MANAGEMENT INTERFACE

Admin plan ideally:

- separate host/subdomain;
- restricted network/VPN/ZTNA;
- own access policy;
- not indexed/publicized unnecessarily;
- AuthZ server-side independent of the UI.

It is not a universal requirement to create another entire product/application.

The requirement is to prevent common user credential/flow from implicitly turning into administration.

---

2.21 Impersonation

If support can impersonate user:

- explicit permission;
- reason;
- TTL;
- visible banner;
- audit log;
- never hide the operator's identity;
- critical operations optionally blocked.

---

2.22 Anti-Automation

OWASP recommends layered defense and emphasizes that distributed attacks cannot be resolved by IP alone.

Take on attacker with:

PROXY ROTATION
RESIDENTIAL BOTNET
HEADLESS BROWSER
CAPTCHA SOLVER
LOW-AND-SLOW

---

2.23 Distributed Rate Limiting

Rate:

REQ/IP
REQ/SUBNET
REQ/ASN
REQ/ACCOUNT
REQ/DEVICE
REQ/SESSION
REQ/TENANT
REQ/ROUTE
REQ/ACTION

Apply:

- burst;
- rolling windows;
- quotas;
- velocity;
- distributed counters;
- backoff.

---

2.24 Fingerprinting

Separate:

DEVICE
CONNECTION
SESSION
BEHAVIOR

Fingerprint:

≠ IDENTITY
≠ AUTH
≠ AUTHORIZATION

---

2.25 Risk Engine

Match:

NETWORK
DEVICE
CONNECTION
SESSION
ACCOUNT
BEHAVIOR
VELOCITY
RESOURCE

Output:

LOW
MEDIUM
HIGH
CRITICAL

---

2.26 Adaptive Response

LOW
→ ALLOW

MEDIUM
→ THROTTLE / CHALLENGE

HIGH
→ CAPTCHA + STEP-UP

CRITICAL
→ HOLD/DENY/REVOKE/ALERT

---

2.27 CAPTCHA

CAPTCHA:

≠ AUTHENTICATION
≠ AUTHORIZATION
≠ MFA

Prefer adaptive use.

OWASP highlights that CAPTCHA can be solved or outsourced and should not be the only control.

---

2.28 Credential Stuffing

Match:

- breached-password blocklist;
- account limits;
- MFA;
- passkeys;
- fingerprint;
- velocity;
- adaptive challenge;
- alerting.

---

2.29 Password Spraying

Detect:

SAME PASSWORD/PATTERN
→ MANY ACCOUNTS

---

2.30 ACT — Account Takeover

Signals:

- new device;
- new ASN;
- MFA removed;
- password reset;
- owner changed;
- admin granted;
- abnormal export;
- incompatible session.

Answer:

STEP-UP
ALERT
REVOKE
HOLD
REVIEW

---

2.31 Honeypots/Tarpits

They can increase risk score.

Never generate DoS against the system itself.

---

2.32 Fingerprint Privacy

- purpose;
- minimization;
- short retention;
- restricted access;
- pseudonymization;
- documentation.


---

2.33 Recovery Assurance

RECOVERY
≠
WEAKEST AUTH PATH

Account recovery must not bypass controls equivalent to normal authentication.

For critical accounts consider:

- reauthentication;
- proof-of-possession;
- cooldown;
- out-of-band notification;
- session recall;
- MFA recovery controls;
- helpdesk verification;
- audit trail.

---

2.34 Phishing-Resistant Authentication

For high impact, prioritize phishing-resistant authenticators:

PASSKEY/FIDO2/WEBAUTHN

SMS/voice should be treated as lower assurance mechanisms and used only when risk/compatibility warrants.

---

2.35 Authentication Must Fail Closed

Flags like:

- `REQUIRE_AUTH`;
- `AUTH_ENABLED`;
- `SECURITY_ENABLED`;
- `DISABLE_AUTH`;
- `ALLOW_ANONYMOUS`;

must have unambiguous semantics.

Production baseline:

`REQUIRE_AUTH` missing
→ AUTH REQUIRED / STARTUP FAIL

Never:

`REQUIRE_AUTH` missing
→ FALSE
→ anonymous access

Validate in test:

1. remove the variable;
2. start the application;
3. confirm startup failure or mandatory authentication;
4. try protected endpoint;
5. confirm `401/403`, never `2xx`.

---

PART 3 — WEB, API, INJECTION AND BUSINESS LOGIC

🟢 BASIC

3.1 Input Validation

All external input is hostile:

BODY
QUERY
PARAM
HEADER
COOKIE
FILE
WEBHOOK
QUEUE
API
LLM
MCP

Validate:

- type;
- size;
- creak;
- format;
- enum;
- cardinality;
- URL;
- date;
- amount;
- coin;
- business rules.

---

3.1.1 Server-Side Validation Gate

Client-side validation is UX.

Security requires server-side validation before:

- persist;
- calculate;
- authorize;
- charge;
- create session;
- change privilege;
- trigger job;
- consume integration;
- generate file;
- perform irreversible action.

CLIENT VALIDATION
≠
SECURITY CONTROL

Minimum Gate:

CLIENT BYPASS
→ SAME INVALID INPUT DIRECT TO API
→ SERVER REJECTS

Validate syntax and semantics.

Examples:

- correct type, but value outside the business rule;
- Valid ID, but resource from another tenant;
- numerically valid price, but not authorized;
- valid status, but prohibited state transition;
- valid role, but caller without permission.

Discrete validation failures against allow-list must be observable when they indicate client tampering.

---

3.2 Sanitization does not replace correct controls

VALIDATION
≠
PARAMETERIZATION
≠
OUTPUT ENCODING
≠
HTML SANITIZATION

---

3.3 SQL Injection

PREPARED STATEMENT
+
PARAMETERIZED ORM

Never concatenate input.

---

3.4 NoSQL Injection

- validate operators;
- reject unexpected objects;
- restrict expressions;
- control regex.

---

3.5 Command Injection

Avoid shell.

When unavoidable:

- structured args;
- allow-list;
- sandbox;
- least privilege;
- timeout.

---

3.6 Template Injection

Never treat external content as an executable template.

---

3.7 XSS

- escaping framework;
- contextual encoding;
- reliable sanitizer for rich HTML;
- CSP;
- avoid raw HTML.

---

3.8 Security Headers

Apply according to answer.

For browser:

X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin

Adequate CSP.

"frame-ancestors" is a modern mechanism for framing control; "X-Frame-Options" can be used as compatibility.

---

3.9 CORS

CORS
≠
AUTHORIZATION

Origin "*" is not automatically vulnerability.

It may be valid for a genuinely public resource without credentials.

For authenticated APIs:

- controlled origins;
- minimal methods;
- minimal headers;
- explicit credential policy.

---

3.10 CSRF

Evaluate when browser automatically sends credentials.

Controls:

- SameSite;
- CSRF token;
- Origin;
- Complementary referee.

GET should not cause mutation.

---

🟡 INTERMEDIATE

3.11 API Security Top 10

Cover:

API1 BALL
API2 Broken Authentication
API3 BOPLA
API4 Resource Consumption
API5 Broken Function Authorization
API6 Sensitive Business Flows
API7 SSRF
API8 Misconfiguration
API9 Inventory
API10 Unsafe Consumption

This is the current published edition of the OWASP API Security Top 10.

---

3.12 IDOR/BALL Regression

USER A → A = ALLOW
USER B → A = DENY

Test GET, PUT, PATCH, DELETE and custom actions.

---

3.13 API Output Minimization

Never serialize entire entity automatically.

Do not return:

- hash;
- reset token;
- MFA secret;
- internal flags;
- private metadata;
- secrets;
- Unnecessary PII.

---

3.14 Resource Consumption

Limit:

- payload;
- pagination;
- batch;
- files;
- CPU;
- memory;
- connections;
- reports;
- AI tokens.

---

3.15 Upload Security

Validate:

- extension;
- MIME;
- magic bytes;
- size;
- amount;
- name;
-path.

Apply:

- randomized server name;
- private storage;
- authorization;
- malware scanning when the risk is justified;
- never perform upload.

---

3.16 SSRF

Validate:

- scheme;
- hostname;
- DNS;
- IP resolved;
- redirects;
- port;
- IPv4;
- IPv6.

Block when unnecessary: ​​

- loopback;
- private networks;
- link-local;
- cloud metadata;
- internal services.

---

3.17 Path Traversal

Canonicalize and then validate.

---

3.18 XXE

When XML exists:

- DTD off;
- external entities off.

---

3.19 ReDoS

- input limits;
- regex review;
- timeout;
- avoid explosive backtracking.

---

3.20 Open Redirect

Prefer relative routes or allow-list.

---

3.21 Proxy Trust

Only trust:

Forwarded
X-Forwarded-For
X-Forwarded-Proto

when sent through a trusted proxy.

---

3.22 Header Bypass

When not used:

X-Original-URL
X-Rewrite-URL
X-Override-URL
X-HTTP-Method-Override

must be removed or rejected.

---

3.23 Host Header

Do not construct sensitive URLs using arbitrary "Host".

---

3.24 Request Smuggling

- updated edge/proxy/backend;
- consistent parsing;
- reject ambiguity;
- test CL/TE and TE/CL when relevant.

---

3.25 Cache Poisoning

Validate:

- cache key;
- "Vary";
- headers;
- query params;
- auth state;
- tenant.

---

3.26 Webhooks

- signature;
- timestamp;
- replay protection;
- schema;
- idempotency;
- timeout;
- logs.

---

3.27 WebSockets

- AuthN;
- AuthZ per event;
- tenant;
- payload schema;
- message size;
- rate limit;
- heartbeat;
- recall.

---

3.28 GraphQL — if applicable

- AuthZ to be resolved;
- depth/complexity;
- batch limits;
- introspection policy;
- pagination;
- field-level controls.

---

3.29 Replay Protection

Use according to protocol:

- nonce;
- timestamp;
- one-time token;
- replay cache;
- signature;
- idempotency key.

---

3.30 Business Logic

Test:

NEGATIVE
ZEROMAX
OVERFLOW
DUPLICATE
REPLAY
RACE
OUT-OF-ORDER
DOUBLE CLICK


---

3.31 Inventory API / Shadow APIs

Inventory:

- routes;
- versions;
- deprecated endpoints;
- internal APIs;
- admin APIs;
- webhooks;
- GraphQL;
- mobile APIs;
- experimental endpoints.

Forgotten endpoint remains an attack surface.

---

3.32 Background Jobs / Async Authorization

JOB
≠
TRUSTED BY DEFAULT

Job must load authorized context:

- actor;
- tenant;
- resources;
- action;
- permissions snapshot or revalidation;
- correlation ID.

Never rely solely on queued serialized IDs.

---

3.33 Content-Type / Parser Safety

Validate:

- Expected Content-Type;
- compatible parser;
- charset when relevant;
- size before parse;
- nesting/depth;
- decompression limits.

Avoid differential parser between edge and backend.

---

3.34 Exposed Environment/Configuration Files

Environment files, configuration, dumps, and build artifacts should never be served publicly.

Block:

- `.env`;
- `.env.*`;
- `.git`;
- `.svn`;
- `config.*` sensitive;
- backup files;
- swap files editor;
- build sensitive manifests;
- exported logs;
- SQL dumps;
- debug endpoints;
- framework diagnostic files.

Public HTTP GET for secret/sensitive configuration:

→ BLOCKER

Controls:

- deny rules on the web server;
- build packaging allow-list;
- minimal static root;
- secret scan;
- post-deploy probe;
- artifact inspection.

Rule:

FILE EXISTS IN REPO
≠
FILE MUST BE PUBLICLY SERVED

---

3.35 Source Map Exposure

Frontend source maps may expose:

- file names;
- paths;
- source code;
- comments;
- endpoints;
- feature flags;
- internal logic;
- class/function names;
- references to services.

Public source map is not automatically a critical vulnerability, but it increases reconnaissance and can reveal sensitive information.

Production must explicitly decide:

PUBLIC SOURCEMAP?
YES / NO

If not required:

- generate only for private observability;
- remove from public artifact;
- use private upload for Sentry/equivalent;
- test `*.map` URLs;
- prevent accidental publication.

Never allow secrets in source map or bundle.

---

3.36 Payment Integrity — Server Authority

Frontend is never authority for:

- unit price;
- subtotal;
- discount;
- tax;
- freight;
- total;
- payment status;
- coin;
- final quantity;
- product/plan ID;
- entitlement.

Customer can send intent or selection.

Server recalculates:

ITEMS
+
PRICE SOURCE OF TRUTH
+
DISCOUNT RULES
+
TAX RULES
+
TOTAL
+
PAYMENT STATE

Never accept:

```json
{
  "price": 1,
  "paid": true,
  "role": "premium"
}
```

as a business authority.

For payments:

FRONTEND SUCCESS SCREEN
≠
PAYMENT CONFIRMED

Confirm by:

- provider API;
- signed webhook;
- server-to-server verification;
- idempotency;
- transaction state machine.

---

3.37 Webhook Signature Enforcement

Sensitive webhook must have, when provider supports:

SIGNATURE
+
TIMESTAMP
+
BODY CANONICALIZATION
+
REPLAY WINDOW
+
SECRET/KEY ROTATION
+
IDEMPOTENCY

If subscription is expected:

MISSING / INVALID SIGNATURE
→ REJECT

Never:

MISSING SIGNATURE
→ PROCESS ANYWAY

Don't just rely on:

- source IP;
- User-Agent;
- obscurity of the URL;
- unauthenticated header.

---

3.38 Password Reset Security Gate

Password reset is authentication flow.

Validate:

- strong and random token;
- single use;
- TTL;
- secure storage;
- anti-enumeration;
- rate limit;
- invalidation after use;
- session review/revocation;
- notification;
- Host header safety;
- MFA/recovery interaction;
- no predictable IDs.

Mandatory test:

RESET TOKEN REPLAY
→ DENY

EXPIRED RESET TOKEN
→ DENY

OTHER USER TOKEN
→ DENY

---

3.39 Session Management Security Gate

Weak session includes:

- predictable session ID;
- absence of rotation;
- indefinite timeout;
- visual logout only;
- non-existent revocation;
- cookie without appropriate flags;
- session surviving critical credential change without justification.

Gate must prove:

LOGIN
→ SESSION CREATED

PRIVILEGE CHANGE
→ SESSION ROTATED / REEVALUATED

LOGOUT
→ ACCESS REVOKED

EXPIRY
→ ACCESS DENIED

---

3.40 JWT Secret/Key Exposure

JWT signing secret/private key is CRITICAL SECRET.

Never on:

- frontend;
- mobile bundle;
- source map;
- public repo;
- image layer;
- logs;
- example config with real value.

If exposed:

MAKE A COMMITMENT
→ ROTATE KEY
→ INVALIDATE AFFECTED TOKENS WHEN POSSIBLE
→ REVIEW ISSUANCE
→ REVIEW AUDIENCE/ISSUER
→ ADD REGRESSION

Cryptographically valid JWT:

≠
AUTHORIZED REQUEST

---

PART 4 ​​— DATA, DATABASE, RLS, PRIVACY AND COMPLIANCE

🟢 BASIC

4.1 Data Minimization

IF NOT NEEDED
DO NOT COLLECT

---

4.2 Database Access

Traditional bank:

CLIENT
↓
BACKEND
↓
DATABASE

No browser → administrative bank.

---

4.3 BaaS / Publishable Keys

If architecture supports explicitly publishable key:

CLIENT
→ PUBLISHABLE KEY

may be correct.

But:

PUBLIC KEY
≠ AUTH
≠ AUTHORIZATION
≠ RLS

Secret/service/admin keys never in the browser.

---

4.4 RLS

When supported and suitable:

- default deny;
- SELECT policy;
- INSERT;
- UPDATE;
- DELETE;
- tenant;
- ownership.

RLS is additional defense.

AuthZ backend remains necessary when there is a backend.

---

4.5 Cross-Tenant Tests

A → A = ALLOW
A → B = DENY
B → A = DENY
ANON → PRIVATE = DENY

---

4.6 Encryption

Passwords:

HASH

Recoverable data:

ENCRYPT

Don't build your own encryption.

---

4.7 Key Management

Separate:

DATE
KEY
MASTER KEY

- key IDs;
- versioning;
- rotation;
- access control;
- KMS where appropriate.

---

4.8 Test Data

Do not copy production to development without:

- need;
- authorization;
- masking;
- anonymization/pseudonymization;
- equivalent controls.

Prefer synthetic data.

---

🟡 INTERMEDIATE

4.9 Data Lifecycle

COLLECT
↓
PROCESS
↓
STORE
↓
SHARE
↓
ARCHIVE
↓
DELETE/ANONYMIZE

---

4.10 Retention

Policy by category:

DATA TYPE
PURPOSE
LEGAL BASIS
RETENTION
DELETION METHOD
BACKUP BEHAVIOR
OWNER

---

4.11 Deletion

Deletion should consider:

- active data;
- cache;
- search;
- storage;
- replicas;
- derived data;
- backups.

Backup may have separate documented cycle.

---

4.12 LGPD

Apply relevant principles and obligations of Law 13,709/2018.

---

4.13 Incident LGPD

When incident may cause relevant risk or damage:

ANPD / HOLDER
3 BUSINESS DAYS

except specific legislation.

Incident records must be kept for at least five years according to the regulation.

---

4.14 Rights of the Holder

Design mechanisms for when applicable:

- confirmation;
- access;
- correction;
- anonymization;
- blocking;
- elimination;
- portability;
- sharing information;
- revocation;
- review of automated decisions.

---

4.15 Privacy by Design

Evaluate privacy in design, not just in legal documents.

For advanced systems consider privacy threat modeling, including methodologies such as LINDDUN when useful.

---

4.16 Cookies

Inventory:

ESSENTIAL
AUTH
PREFERENCE
ANALYTICS
MARKETING

Don't create banners just out of habit.

Evaluate real obligation.

---

4.17 Terms / Privacy

Commercial system must have when applicable:

/terms
/privacy

Policy must reflect real behavior.

Do not invent company, DPO or subprocessors.

Placeholder:

[LEGAL INFORMATION TO BE DEFINED]

---

4.18 Legal Footer

© {ACTUAL_YEAR} Product.
All rights reserved.

With accessible links.

---

🔴 ADVANCED

4.19 GDPR

First:

IS GDPR APPLICABLE?

If yes, apply corresponding controls.

GDPR requires principles such as lawfulness, purpose limitation and data minimization.

---

4.20 HIPAA

First:

IS SYSTEM A
COVERED ENTITY
OR BUSINESS ASSOCIATE
PROCESSING ePHI?

HIPAA Security Rule is not a generic requirement for all SaaS; applies to regulated entities and ePHI.

The update proposal published in 2025 has not yet replaced the current Security Rule.

---

4.21 PCI DSS

First:

IS CARDHOLDER DATA ENVIRONMENT
IN SCOPE?

If yes, map PCI DSS 4.0.1.

Avoid storing card data when tokenization/PSP could remove the system from broader scope.


---

4.22 Data Export Security

Exports must apply:

- AuthN;
- AuthZ;
- tenant isolation;
- step-up according to sensitivity;
- minimization;
-audit;
- rate/volume limits;
- expiration of links;
- private storage;
- revocation when applicable.

EXPORT
≠
AUTHORIZATION BYPASS

---

4.23 Cryptographic Erasure

When architecturally appropriate, consider deletion by secure key destruction for cryptographically isolated data.

There must be proof of:

- scope;
- key ownership;
- dependencies;
- backups;
- expected irreversibility.

---

⚫ MAXIMUM SAFE

- KMS;
- HSM;
- envelope encryption;
- DLP;
- key ceremonies when necessary;
- separation of duties;
- dual control;
- crypto inventory;
- crypto agility;
- post-quantum migration planning according to data lifetime and risk.

---

PART 5 — CLOUD, INFRASTRUCTURE, SECRETS AND SUPPLY CHAIN ​​

🟢 BASIC

5.1 Secrets

Never on:

SOURCE CODE
GIT
README
SCREENSHOT
PUBLIC ISSUE
BUILD LOG
FRONTEND BUNDLE
DOCKER IMAGE
PUBLIC PROMPT

---

5.2 ".env"

.env
.env.*
!.env.example

".env.example" contains placeholders only.

---

5.3 Git History

Versioned secret:

COMMITTED

Flow:

REVOKE/ROTATE
↓
REMOVE CURRENT
↓
CLEAN HISTORY IF APPROPRIATE
↓
CHECK ARTIFACTS
↓
PREVENT RECURRENCE

Never show the value found.

---

5.4 History Rewrite

Don't automatically do destructive force-push on shared repo.

Rate:

- branches;
- tags;
- forks;
- collaborators;
- deploys.

---

5.5 Secret Inventory

NAME
PURPOSE
OWNER
ENVIRONMENT
LOCATION
ACCESS
ROTATION METHOD
EXPIRATION
LAST ROTATION

---

🟡 INTERMEDIATE

5.6 Secret Manager

Use appropriate mechanism:

- cloud secret manager;
- platform secrets;
- Vault;
- workload identity.

Secret manager does not necessarily mean “no env var”; the goal is to control exposure and life cycle.

---

5.7 Short-Lived Credentials

Prefer when available:

OIDC FEDERATION
WORKLOAD IDENTITY
SHORT-LIVED TOKEN

---

5.8 Secret Rotation

No:

ROTATE EVERYTHING EVERY 90 DAYS

as a universal rule.

Rotate according:

- compromise;
- exposure;
- life cycle;
- personnel change;
- provider requirements;
- risk;
- compliance.

---

5.9 TLS

Baseline:

TLS 1.3 DEFAULT
TLS 1.2 WHEN COMPATIBILITY REQUIRES
TLS 1.0/1.1 OFF

This corresponds to current OWASP guidance.

---

5.10 Certificate Lifecycle

Each certificate has:

ISSUE
↓
DEPLOY
↓
MONITOR
↓
RENEW
↓
ROTATE
↓
REVOKE

Control:

- expiration;
- private key access;
- SAN/domain;
- issuer;
- renewal automation;
- recall.

---

5.11 HSTS

Only after HTTPS is properly operational.

Preload is an additional decision, not a mandatory default.

---

5.12 IAM

LEAST PRIVILEGE

- specific functions;
- separate admin;
- MFA;
- workload identity;
-audit;
- recall.

---

5.13 Network

- minimum entry;
- egress control;
- private subnets;
- private DB;
- metadata protection;
- management restricted interfaces.

---

5.14 Cloud Metadata

Protection against SSRF.

On AWS, use IMDSv2 where applicable.

---

5.15 Containers

- trusted base;
- non-root;
- image scan;
- no secrets;
- read-only when supported;
- minimum capabilities;
- seccomp when appropriate;
- health checks.

"Alpine" or "distroless" do not automatically mean safe.

---

5.16 CI/CD

Base pipeline:

LINT
↓
TYPECHECK
↓
UNIT
↓
SECRET SCAN
↓
SAST
↓
SCA
↓
BUILD
↓
SBOM
↓
CONTAINER/IaC SCAN
↓
INTEGRATION
↓
STAGING
↓
DAST/API
↓
REGRESSION
↓
GATE
↓
PRODUCTION

---

5.17 Dependencies

Before adding package:

- need;
- registry;
- maintainer;
- repository;
- history;
- CVEs;
- license;
- typosquatting;
- slopsquatting.

---

5.18 Lockfiles

Mandatory when ecosystem supports it.

---

5.19 Vulnerability Management

Prioritize:

KEV / EXPLOITATION OBSERVED
+
EPSS / EXPLOIT LIKELIHOOD
+
EXPOSURE
+
REACHABILITY
+
IMPACT
+
ASSET CRITICALITY
+
COMPENSATING CONTROLS
+
CVSS 4.0
+
SSVC/DECISION CONTEXT

CISA KEV must be direct entry because it represents known exploited vulnerabilities.

EPSS estimates probability of exploration over a 30-day horizon and does not substitute for impact/context.

CVSS describes technical severity and should not be treated in isolation as a patch priority.

---

5.20 Patch Strategy

Each vulnerability:

CVE
AFFECTED?
REACHABLE?
EXPOSED?
EXPLOITABLE?
KEV?
EPSS?
CVSS 4.0?
SSVC/DECISION?
FIX AVAILABLE?
BREAKING CHANGE?
MITIGATION?
DEADLINE?
OWNER?

---

5.20.1 Continuous Dependency / CVE Monitoring

Deploy does not end supply-chain security.

Monitor continuously:

- direct dependencies;
- transitive dependencies;- container/base images;
- runtime/framework;
- OS packages;
- build tools;
- package registries;
- CI actions/plugins;
- MCP/plugins/agent extensions.

Prioritization inputs:

KEV
+
EPSS
+
CVSS 4.0
+
REACHABILITY
+
EXPOSURE
+
ASSET CRITICALITY

Recommended automation:

- dependency alerts;
- Dependabot/Renovate/equivalent;
- Recurrent SCA;
- Updated SBOM;
- image scanning;
- scheduled re-scan;
- release regression.

Rule:

UPDATE AVAILABLE
≠
AUTO-MERGE BLINDLY

PATCH
→ TEST
→ SECURITY REGRESSION
→ BUILD
→ VERIFY
→ RELEASE

---

5.20.2 Package Manager Neutrality

npm
pnpm
yarn
Bun

they are tooling/ecosystem choices.

None of them are security boundaries in and of themselves.

Manager independent baseline:

- versioned lockfile;
- deterministic install;
- reliable registry;
- integrity/hash when supported;
- evaluated lifecycle scripts;
- package provenance when available;
- typosquatting/slopsquatting review;
- dependency audit;
- pinning compatible with project strategy.

Change package manager only for generic security claim:

→ NOT ENOUGH CONTROL

---

🔴 ADVANCED

5.21 SBOM

Generate:

- components;
- version;
- origin;
- hash;
- license.

Formats:

CycloneDX
SPDX

---

5.22 Provenance

Production must know:

SOURCE COMMIT
BUILD
DEPENDENCIES
ARTIFACT HASH
DEPLOYMENT

---

5.23 Artifact Signing

Rate:

- Sigstore/cosign;
- signed container images;
- signed releases.

---

5.24 Build Once

BUILD
↓
TEST SAME ARTIFACT
↓
DEPLOY SAME ARTIFACT

---

5.25 GitHub Actions/CI

- explicit permissions;
- least privilege;
- trusted actions;
- adequate pinning;
- protected secrets;
- PR isolation;
- review "pull_request_target".

---

5.26 Branch Protection

- required PR;
- required CI;
- reviewers;
- no arbitrary force push;
- CODEOWNERS when necessary.


---

5.27 SLSA 1.2 / Provenance Verification

For critical artifacts, evaluate SLSA tracks:

SOURCE
+
BUILD
+
PROVENANCE
+
VERIFICATION

Before deploying, check when available:

- source repository;
- source revision;
- builder identity;
- build parameters;
- artifact digestion;
- provenance;
- signature/attestation;
- policy result.

ATTESTATION EXISTS
≠
ATTESTATION VERIFIED

---

5.28 IaC Drift

Declared and actual infrastructure must be compared.

Detect:

- manual changes;
- expanded permissions;
- public exposure;
- firewall drift;
- secret/config drift;
- unmanaged resources.

CRITICAL DRIFT
→ REVIEW / RECONCILE

---

5.29 Database Network Exposure — Docker / Compose

Application database must be PRIVATE BY DEFAULT.

In Docker Compose, communication between services uses the internal network and service name.

Safe example:

```yaml
services:
  app:
    environment:
      DB_HOST: db
      DB_PORT: 5432
    depends_on:
      - db

  db:
    image: postgres:18
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    networks:
      - backend

networks:
  backend:
    internal: true
```

For container-only traffic → container:

NOT NECESSARY:

```yaml
ports:
  - "5432:5432"
```

`ports:` publishes the port on the host.

If host access is really necessary in development:

```yaml
ports:
  - "127.0.0.1:5432:5432"
```

This is no substitute for firewall, auth or strong secret.

In production, external exposure of the bank requires explicit architectural justification, ACL/firewall, TLS according to the scenario, strong authentication, observability and ownership.

Never assume:

DB PASSWORD
=
NETWORK PERIMETER

Correct defense:

PRIVATE NETWORK
+
AUTH
+
LEAST PRIVILEGE
+
PATCHING
+
MONITORING

---

5.30 PostgreSQL Authentication Hardening

For the official PostgreSQL image:

- `POSTGRES_PASSWORD` must be strong and non-standard;
- do not use values ​​such as `postgres`, `password`, `admin`, `example`, product name or credential published in README;
- do not use `POSTGRES_HOST_AUTH_METHOD=trust` in a reachable environment;
- prefer supported modern authentication, such as `scram-sha-256`;
- app should not connect as superuser `postgres` when a limited role is sufficient;
- separate migration/admin role from runtime role when justified;
- restrict `pg_hba.conf` to the minimum necessary;
- rotate password after exposure/suspicion of compromise;
- remember that changing `POSTGRES_PASSWORD` in Compose does not necessarily change an already initialized instance.

INCIDENT RESPONSE:

PORT EXPOSED + CREDENTIAL WEAK/KNOWN
→ ASSUME CREDENTIAL COMMIT
→ CLOSE EXPOSURE
→ ROTATE CREDENTIAL
→ REVIEW LOGS
→ CHECK PERSISTENCE
→ PATCH
→ VERIFY FROM INTERNET
→ ADD REGRESSION

---

5.31 Database Exposure Regression

CI/review should look in manifests:

- `5432:5432`;
- `0.0.0.0:5432`;
- `3306:3306`;
- `6379:6379`;
- `27017:27017`;
- `network_mode: host`;
- security groups `0.0.0.0/0`;
- `POSTGRES_HOST_AUTH_METHOD=trust`;
- example/default credentials.

Finding depends on the context.

Port published in local dev may be valid.

Port published on VPS/production without the need for a blocker.

Recommended test:

EXTERNAL HOST
→ DB PORT
→ MUST BE CLOSED / FILTERED

when the bank is designated as internal.

---

5.32 Subnetting ≠ Security Boundary

Subnet mask organizes addressing and routing.

Alone, it does not prove isolation.

Example:

CLIENTS 10.10.10.0/24
SYSTEM 10.10.20.0/24

If the router allows it:

10.10.10.0/24
→
10.10.20.0/24
ALLOW ANY

so there is logical separation of addresses, but not security isolation.

To consider segmentation as control:

SUBNET/VLAN/VRF
+
ROUTING CONTROL
+
ACL/FIREWALL
+
DEFAULT DENY
+
LOGGING
+
TEST

Rule:

DIFFERENT SUBNET
≠
DENIED CONNECTIVITY

---

5.33 Network Security Zones

Separate according to real architecture.

Model for gym/company:

INTERNET
↓
EDGE/CDN/WAF
↓
DMZ/REVERSE PROXY
↓
APPLICATION ZONE
↓
DATA ZONE

CLIENT/GUEST WIFI
↛ MANAGEMENT
↛ DATABASE
↛ INTERNAL SERVICES

STAFF / CORPORATE
→ only necessary services

MANAGEMENT ZONE
→ authorized administration

DATA ZONE
← only authorized application/migration paths

When applicable, also separate:

- IoT;
- turnstiles;
- cameras/CCTV;
- printers;
- payments;
- backups;
- observability;
- CI/CD runners;
- suppliers/third parties.

Do not place customers and critical infrastructure in the same trust domain.

---

5.34 Inter-Zone Policy

Principle:

DENY ALL
+
ALLOW REQUIRED FLOWS

Each allowed flow must declare:

SOURCE
DESTINATION
PROTOCOL
PORT
PURPOSE
OWNER

Example:

GUEST VLAN
→ INTERNET 443
ALLOW

GUEST VLAN
→ APP PUBLIC 443
ALLOW when necessary

GUEST VLAN
→ APP ADMIN
DENY

GUEST VLAN
→ POSTGRES 5432
DENY

GUEST VLAN
→ SSH 22
DENY

APP
→ POSTGRES 5432
ALLOW

ADMIN ZONE
→ MANAGEMENT
ALLOW as per identity/policy

Avoid:

ANY
→ ANY
ALLOW

---

5.35 Client/Guest Isolation

In customer/visitor networks:

- Own VLAN/SSID;
- client isolation when supported;
- private VLAN/PVLAN when appropriate;
- block unnecessary east-west;
- block access to RFC1918/internal ranges when applicable;
- only release Internet and services that are explicitly necessary;
- DNS and DHCP controlled;
- record relevant denials;
- prevent access to the management plane.

Purpose:

CLIENT A
↛
CLIENT B

when peer-to-peer communication is not necessary.

E:

CLIENT
↛
INTERNAL ADMIN / DB / INFRA

---

5.36 Management Plane Isolation

Administration should not depend on a public panel open to the Internet.

Prefer:

TRUSTED ADMIN DEVICE
↓
VPN / ZTNA / BASTION
↓
MANAGEMENT ZONE
↓
SSH / RDP / HYPERVISOR / DB ADMIN / CONTROL PANEL

Controls:

- MFA/passkey;
- device posture when available;
- source restriction;
- short-lived access;
- JIT/JEA when available;
-audit;
- session timeout;
- no shared admin accounts.

Do not manage infrastructure directly from the guest network.

Do not expose SSH/RDP/panel just because there is a strong password.

---

5.37 Reduce Origin Exposure

"Hide" is not primary control.

Cloudflare, Fastly, Akamai, AWS CloudFront/WAF, equivalent reverse proxies, or native provider controls can comprise the edge.

No specific vendor is a universal requirement.

EDGE/WAF/CDN
≠
AUTHENTICATION
≠
AUTHORIZATION
≠
PATCHING
≠
SERVER-SIDE VALIDATION

But reducing reachability is a valid defense.

For public applications consider:

INTERNET
↓
CDN / REVERSE PROXY / WAF
↓
ORIGIN RESTRICTED

Origin shall, where feasible:

- accept traffic only from proxy/CDN/LB;
- do not publish bank/cache/queues;
- do not expose admin endpoints;
- have a firewall/provider security group;
- apply TLS;
- rate limiting;
- observability;
- patching.

Other techniques:

- private endpoints;
- private DNS / split-horizon DNS;
- VPN/ZTNA for administration;
- bastion for operational access;
- egress filtering;
- mTLS between services when risk is justified;
- service identity;
- microsegmentation;
- separate management network.

Principle:

HIDDEN
≠
SECURE

But:

NOT REACHABLE
<
SMALLER ATTACK SURFACE

---

5.38 Zero Trust Beyond Network Location

Being on internal VLAN does not grant automatic trust.

Access decision must consider:

IDENTITY
+
DEVICE
+
RESOURCE
+
ACTION
+
CONTEXT
+
POLICY

Application continues running AuthN/AuthZ even when:

- source is LAN;
- origin is VPN;
- origin is internal subnet;
- service is in Docker/Kubernetes;
- communication occurs between workloads.

NETWORK LOCATION
≠
AUTHORIZATION

For cloud-native/microservices consider service identities and service-to-service authorization.

---

5.39 Docker Firewall Interaction

Docker can create its own iptables/nftables rules for bridge networks and published ports.

Port publishing:

```text
-p 8080:80
```

no host specific IP typically publishes on all host interfaces.

On Linux, do not assume that:

UFW DENY
=
DOCKER PORT DENIED

because traffic published by Docker can be processed before the chains used by UFW.

Baseline:

- avoid publishing what you don't need;
- bind in loopback when only local host is needed;
- use a firewall compatible with the Docker backend;
- review iptables/nftables/firewalld;
- externally test the real reachability;
- keep Docker updated;
- do not arbitrarily disable Docker firewall management without full replacement policy.

PASS requires testing from outside the VPS/network:

EXPECTED CLOSED
+
CURRENT CLOSED/FILTERED

---

5.40 Network Segmentation Regression Matrix

Explicitly test:

GUEST
→ INTERNET
ALLOW

GUEST
→ PUBLIC APP
ALLOW according to product

GUEST
→ ADMIN
DENY

GUEST
→ DB
DENY

GUEST
→ SSH/RDP
DENY

GUEST A
→ GUEST B
DENY when client isolation required

APP
→ DB
ALLOW only port/protocol required

DB
→ INTERNET
DENY or minimum egress as required

MANAGEMENT
→ ADMIN TARGETS
ALLOW authorized identity/device only

INTERNET
→ ORIGIN
DENY when origin must accept only proxy/CDN

INTERNET
→ DB/CACHE/QUEUE
DENY

Any unexpected path:

FAIL
→ FINDING
→ FIX
→ REGRESSION

---

⚫ MAXIMUM SAFE

- policy-as-code;
- admission control;
- immutable infrastructure;
- signed provenance;
- hardened runners;
- private registry;
- runtime detection;
- network segmentation;
- PAM;
- zero long-lived CI credentials when feasible.

---

PART 6 — RELIABILITY, RESILIENCE, PERFORMANCE AND DISASTER RECOVERY

🟢 BASIC

6.1 Timeouts

Every external call must have an explicit timeout:

- HTTP;
-DB;
- cache;
- queue;
- THERE;
- storage.

Never let calls wait indefinitely.

---

6.2 Error Classification

Separate:

VALIDATION ERROR
AUTH ERROR
BUSINESS ERROR
TRANSIENT ERROR
DEPENDENCY ERROR
INTERNAL ERROR

---

6.3 Graceful Failure

Optional failure should not necessarily bring down critical flow.

Example:

ANALYTICS DOWN
≠
LOGIN DOWN

---

🟡 INTERMEDIATE

6.4 Criticality Map

Sort dependencies:

CRITICAL
IMPORTANT
OPTIONAL

---

6.5 Retry

Retry only when semantically safe.

Use:

EXPONENTIAL BACKOFF
+
JITTER
+
MAX ATTEMPTS
+
RETRY BUDGET

---

6.6 Retry must not duplicate effects

Non-idempotent operations require protection before retry.

---

6.7 Idempotency

Apply when necessary: ​​

- payment;
- invoice;
- order;
- stock;
- webhook;
- import;
-financial action.

---

6.8 Circuit Breaker

States:

CLOSED
↓
OPEN
↓
HALF-OPEN
↓
CLOSED

Avoid cascade of failures.

---

6.9 Fallback

Fallback can never reduce security control.

Prohibited:

AUTH SERVICE DOWN
→ ALLOW USER

Correct:

AUTH SERVICE DOWN
→ FAIL CLOSED

for authorization decisions.

---

6.10 Bulkheads

Isolate resources to prevent a dependency from consuming all:

- thread pool;
- connection pool;
- queue;
- CPU;
- worker capacity.

---

6.11 Concurrency

Protect against:

- lost updates;
- duplicate submission;
- overselling;
- negative inventory;
- double billing;
- TOUCHED;
- simultaneous role changes.

Controls:

TRANSACTION
UNIQUE CONSTRAINT
OPTIMISTIC LOCK
PESSIMISTIC LOCK
ATOMIC UPDATE
IDEMPOTENCY KEY
VERSION

---

6.12 Cache Strategy

All cache documents:

WHAT?
KEY?
TTL?
INVALIDATION?
TENANT?
PII?
OWNER?

---

6.13 Cache Isolation

Specific cache must include appropriate context.

Example:

tenant:{tenantId}:invoice:{invoiceId}

when necessary.

---

6.14 Cache Invalidation

Set:

- write-through;
- write-behind;
- cache-aside;
- explicit purge;
-TTL.

Avoid eternal state.

---

6.15 Stampede Cache

Mitigate when applicable:

- locking;
- request coalescing;
- jittered TTL;
- stale-while-revalidate.

---

6.16 Health

Separate:

LIVENESS
READINESS
DEPENDENCY HEALTH

Public endpoint should not leak internal details.

---

6.17 SLI/SLO

Set for critical services:

- availability;
- latency;
- error rate;
- throughput;
- saturation.

Don't promise 100% uptime.

---

6.18 Load Testing

Test:

EXPECTED
PEAK
BURST
SUSTAINED

Measure:

- p50;
- p95;
- p99;
- error rate;
- throughput;
- CPU;
- RAM;
- DB pool;
- queue depth.

---
6.19 Stress Testing

Determine:

BREAKING POINT
+
FAILURE MODE
+
RECOVERY

---

6.20 Soak Testing

Evaluate long period to detect:

- leaks;
- connection exhaustion;
- queue growth;
- degradation.

---

6.21 RTO/RPO

For service.

RTO
=
maximum acceptable recovery time

RPO
=
maximum acceptable data loss

Don't make up numbers.

Derive from business impact.

---

6.22 BIA

Business Impact Analysis should identify:

- critical processes;
- dependencies;
- impact;
- recovery priority;
- RTO;
- RPO.

NIST SP 800-34 treats BIA, recovery strategies, plan, testing and maintenance as components of contingency planning.

---

6.23 Backups

- automatic;
- protected;
- encrypted when necessary;
- separate;
- monitored;
- defined retention.

---

6.24 Restore Testing

BACKUP EXISTS
≠
RECOVERY PROVEN

PASS in restore requires real testing.

---

🔴 ADVANCED

6.25 Disaster Recovery Plan

Document:

INCIDENT
↓
DECLARE DR
↓
FAILOVER/RESTORE
↓
VERIFY
↓
RESTORE TRAFFIC
↓
MONITOR

---

6.26 DR Plan

Include:

- owner;
- contacts;
- credentials;
- DNS;
- infrastructure;
- databases;
- storage;
- providers;
- recovery order;
- verification;
- rollback;
- communication.

---

6.27 Chaos Engineering

Only controlled.

Possible tests:

DB DOWN
CACHE DOWN
API DOWN
LATENCY
PACKET LOSS
QUEUE FAILURE
INSTANCE LOSS
DISK FULL
CERT FAILURE

Requires:

- blast radius;
- stop condition;
- monitoring;
- recovery plan.


---

6.28 Release Safety

For risk changes:

- canary;
- blue/green;
- staged rollout;
- feature flag;
- kill switch;
- automatic rollback criteria;
- observability before full rollout.

DEPLOY SUCCESS
≠
RELEASE HEALTHY

---

6.29 Database Migration Safety

Prefer:

EXPAND
↓
MIGRATE
↓
VERIFY
↓
CONTRACT

For critical migrations:

- backup/restore path;
- lock impact;
- execution time;
- rollback or roll-forward;
- backward compatibility;
- data validation;
- failure recovery.

---

6.30 Queue Safety

Queues should consider:

- idempotency;
- retrieval budget;
- DLQ;
- poison message;
- max attempts;
- ordering;
- deduplication;
- tenant context;
- message size;
- schema/version;
- replay safety.

---

6.31 Feature Flags

Critical flags must have:

- owner;
- safe default;
- environmental scope;
-audit;
- expiry/removal plan;
- fail-safe behavior.

Feature flag does not replace AuthZ.

---

6.32 Error Budget

For services with SLO:

ERROR BUDGET CONSUMED
→ REDUCE CHANGE RISK

Use error budget as a sign of reliability, not as a license to ignore security incidents.

---

⚫ MAXIMUM SAFE

- multi-region when business case requires it;
- automated failover;
- immutable/offline backups;
- DR exercises;
- dependency fault injection;
- capacity models;
- recovery automation.

---

PART 7 — LOGGING, AUDIT, DETECTION AND INCIDENT RESPONSE

🟢 BASIC

7.1 Security Logging

Register:

- login;
- logout;
-failure;
- reset;
- admin actions;
- critical errors.

Never log secrets.

---

7.2 Safe Errors

Client:

SAFE MESSAGE

Server:

DIAGNOSTIC CONTEXT

Never expose:

- stack;
- SQL;
- filesystem;
- credentials;
- internal URLs;
- tokens.

---

🟡 INTERMEDIATE

7.3 Structured Logs

Example:

{
"timestamp": "...",
"level": "WARN",
"requestId": "...",
"userId": "...",
"tenantId": "...",
"action": "...",
"resource": "...",
"result": "DENIED"
}

---

7.4 Correlation

Use:

- request ID;
- trace ID;
- span ID when tracing exists.

---

7.5 Audit Trail

Relevant events:

- permission change;
- owner change;
- data export;
- financial action;
- impersonation;
- security settings;
- delete;
- admin actions.

---

7.6 Audit Event Schema

WHO
WHEN
TENANT
ACTION
RESOURCE
RESULT
SOURCE
REQUEST_ID

When necessary: ​​

BEFORE
AFTER

with editorial.

---

7.7 Tamper Evidence

"append-only JSON" alone does not guarantee integrity.

Most at risk:

- remote log sink;
- immutable storage;
- restricted delete;
- WORM;
- hash chaining;
- digital signature;
- independent retention controls.

---

7.8 Alerts

Alert:

- ACT;
- brute force;
- password spray;
- credential stuffing;
- privilege escalation;
- tenant violation;
- new admin;
- MFA removal;
- anomalous exports;
- secret leak;
- critical CVE;
- high 5xx;
- session anomalies.

---

🔴 ADVANCED

7.9 SIEM

When scale justify:

- Wazuh;
- Elastic Security;
- Splunk;
- equivalent.

---

7.10 Detection Engineering

THREAT
LOG SOURCE
DETECTION
ALERT
RUNBOOK
OWNER
TEST

---

7.11 Incident Response

Flow:

DETECT
↓
TRIAGE
↓
CONTAIN
↓
ERADICATE
↓
RECOVER
↓
LEARN

NIST SP 800-61 Rev. 3 integrates these capabilities into ongoing risk management.

---

7.12 Severity

SEV-1 CRITICAL
SEV-2 HIGH
SEV-3 MODERATE
SEV-4 INFORMATIONAL

---

7.13 SEV-1 Runbook

- declare;
- timestamp;
- incident commander;
- preserve evidence;
- contain;
- rotate credentials;
- identify vector;
- identify date;
- fix;
- recover;
- monitor;
- legal/privacy assessment;
- RCA.

---

7.14 Evidence Preservation

Preserve:

- logs;
- traces;
- requests;
- hashes;
- snapshots;
- commits;
- artifacts;
- configs;
- deploy IDs.

---

7.15 RCA

Ask:

WHAT HAPPENED?
WHY?
WHICH CONTROL FAILED?
WHY DID TESTING MISS IT?
WHY DID DETECTION MISS IT?
HOW DO WE PREVENT RECURRENCE?

Do not close in:

HUMAN ERROR

without systemic cause.

---

7.16 Pentest

Periodicity based on risk and relevant changes.

Trigger after:

- new auth;
- new tenant model;
- payments;
- great architecture;
- incident;
- relevant exposure.

---

7.17 DAST

Use where useful.

Example:

OWASP ZAP

It does not replace review or business logic testing.


---

7.18 Detection Validation

ALERT CONFIGURED
≠
DETECTION PROVEN

Test detections with controlled events.

Register:

- test case;
- expected alert;
- current alert;
- latency;
- routing;
- owner response.

---

7.19 Log Privacy / Redaction

Logs should minimize:

- passwords;
- tokens;
- reusable session IDs;
- authorization headers;
- card data;
- sensitive PII;
- prompt secrets;
- raw documents.

When personal identifiers are necessary, consider pseudonymization/tokenization.

---

7.20 Incident Communications

Runbook must define:

- technical channel;
- executive escalation;
- legal/privacy;
- customer communication;
- regulatory communication;
- cadence status;
- approval authority.

Do not speculate externally before minimal verified facts.

---

⚫ MAXIMUM SAFE

- SOC;
- EDR;
- UEBA;
- threat intelligence;
- immutable logs;
- forensic readiness;
- threat hunting;
- Red Team;
– Purple Team;
- bug bounty;
- crisis exercises.

---

PART 8 — TESTING, QUALITY ENGINEERING AND ACCESSIBILITY

🟢 BASIC

8.1 Test Pyramid

The project must match:

STATIC
+
UNIT
+
INTEGRATION
+
E2E
+
SECURITY

---

8.2 Unit Tests

Cover:

- business rules;
- validation;
- permission logic;
- calculations;
- edge cases.

---

8.3 Integration Tests

Cover:

-DB;
- cache;
- storage;
- queues;
- auth;
- third parties.

---

8.4 E2E

Critical Journeys:

REGISTER
LOGIN
RECOVERY
MAIN BUSINESS FLOW
ADMIN
LOGOUT

---

8.5 Negative Testing

Mandatory.

Examples:

UNAUTHORIZED
FORBIDDEN
INVALID
EXPIRED
CROSS-TENANT
DUPLICATE
OUT-OF-RANGE

---

🟡 INTERMEDIATE

8.6 Regression Tests

Bug or vulnerability fixed:

BUG
↓
FIX
↓
REGRESSION TEST
↓
CI

Whenever technically feasible.

---

8.7 Coverage Gates

Do not use:

80% = QUALITY

as dogma.

Define thresholds based on criticality.

Critical code:

- authentication;
- authorization;
- tenant isolation;
- payments;
- accounting;
- inventory integrity;

must have strong coverage.

---

8.8 Differential Coverage

New changes must not reduce quality without justification.

Evaluate coverage of changed lines.

---

8.9 Branch Coverage

For critical logic, branch coverage is often more informative than line coverage alone.

---

8.10 Contract Tests

When there are consumer services/API:

- request schemas;
- response schemes;
- compatibility;
- versioning.

---

8.11 Flaky Tests

Don't simply rerun until it passes.

Flaky testing is technical debt.

---

8.12 Static Gates

CI:

LINT
TYPECHECK
SAST
SECRET SCAN

---

8.13 Code Review Standard

Critical PR requires:

CORRECTNESS
SECURITY
DATE
COMPETITION
ERRORS
PERFORMANCE
TESTS
ACCESSIBILITY
OBSERVABILITY

---

8.14 Accessibility Baseline

WCAG 2.2 AA

W3C recommends WCAG 2.2 for greater future applicability.

---

8.15 Accessibility Tests

Test:

- keyboard navigation;
- focus;
- focus order;
- focus not obscured;
- contrast;
- semantic HTML;
- headings;
- labels;
- errors;
- accessible names;
- screen reader;
- responsive reflow;
- zoom;
- target size;
- reduced motion;
- status messages.

WCAG 2.2 also adds Focus Not Obscured, Target Size and Accessible Authentication.

---

8.16 Accessible Authentication

CAPTCHA or login should not create a cognitive barrier without an appropriate alternative.

This must be considered together with anti-bot.

---

8.17 Automation is not enough

Automated accessibility scanner:

≠
WCAG CONFORMANCE PROVEN

Combine automation with manual testing.

---

🔴 ADVANCED

8.18 Performance Regression

Add baseline for:

- Latency API;
- DB query latency;
- bundle size;
- memory;
- throughput.

---

8.19 Load Tests on CI/CD

They don't need to run on every commit.

Execute as:

- release;
- architecture;
- performance-sensitive change.

---

8.20 Security Regression Suite

Maintain testing for historical vulnerabilities.

---

8.21 Mutation Testing

Evaluate for critical logic.

Helps identify tests that execute code without actually checking behavior.

---

8.22 Property-Based Testing

Applicable for:

- parsers;
- calculations;
- business invariants;
- validation;
- serialization.

---

8.23 Fuzzing

Use for high-risk surfaces:

- parsers;
- file processing;
- protocol handlers;
- Complex APIs.


---

8.24 Control-to-Test Traceability

Critical control must point to verifiable testing.

CONTROL
→ TEST ID
→ CI RUN
→ RESULT
→ EVIDENCE

This prevents PASS based on documentation alone.

---

8.25 Test Environment Fidelity

Differences between staging and production must be known.

Map:

- auth provider;
- network;
- proxy;
- TLS;
- DB engine/version;
- storage;
- cache;
- queues;
- feature flags;
- secret mechanism.

STAGING PASS
≠
PRODUCTION PROVEN

when material differences alter control behavior.

---

8.26 Migration Tests

Test when relevant:

- forward migration;
- rollback/roll-forward;
- old app + new schema;
- new app + transitional schema;
- constraints;
- data conversion;
- large dataset behavior.

---

⚫ MAXIMUM SAFE

- continuous performance baselines;
- advanced fault injection;
- formal security regression suites;
- accessibility testing matrix;
- device/browser compatibility;
- adversarial testing;
- release qualification.

---

PART 9 — AI, RAG, AGENTS AND MCP

OWASP published the GenAI LLM Top 10 2026, Top 10 for Agentic Applications 2026, MCP Top 10, and practical guidance for secure MCP server development.

---

🟢 BASIC

9.1 AI-generated Code

Never:

AI GENERATED
→ DIRECT PRODUCTION

Required:

AI
↓
HUMAN REVIEW
↓
TEST
↓
SECURITY
↓
PR

---

9.2 Secrets

Never send external model:

- prod ".env";
- private keys;
- DB passwords;
- customer secrets;
- real tokens;
- sensitive dumps.

---

9.3 Dependency Hallucination

AI Suggested Package:

VERIFY REGISTRY
VERIFY OWNER
VERIFY REPO
VERIFY SECURITY

before installing.

---

🟡 INTERMEDIATE

9.4 Prompt Injection

All external content:
UNTRUSTED

Includes:

- user;
- page;
- PDF;
- mail;
- RAG;
- search;
- database;
- MCP;
- tool response.

---

9.5 Instruction Boundaries

Separate:

SYSTEM
DEVELOPER
TOOL
USER
EXTERNAL DATA

---

9.6 Output Validation

LLM output remains unreliable before:

- run shell;
- SQL;
- HTML;
- API call;
- email;
- DB change;
- file write.

---

9.7 Tool Least Privilege

Separate:

READ
WRITE
DELETE
RUN
ADMIN

---

9.8 Human Approval

Required for high impact:

- money;
- delete;
- admin;
- ownership;
- production deployment;
- secrets;
- mass communication;
- destructive command.

---

9.9 RAG Security

- source authorization;
- tenant filter;
- provenance;
- poisoning defenses;
- output validation;
- document ACLs.

Never retrieve documents from another tenant.

---

🔴 ADVANCED

9.10 Agent Identity

AGENT ID
+
SCOPED TOKEN
+
TENANT
+
SHORT TTL

Never:

AGENT = GLOBAL ADMIN

---

9.11 Delegation Chain

Register:

USER
↓
AGENT
↓
TOOL
↓
ACTION

---

9.12 Memory

Persistent memory must have:

- source;
-author;
- timestamp;
- tenant;
- scope;
- integrity;
- deletion.

---

9.13 Memory Poisoning

External content should never automatically become trusted policy.

---

9.14 MCP

MCP is trust boundary.

MCP Server:

- AuthN;
- AuthZ;
- schema;
- validation;
- output validation;
- rate limit;
- session isolation;
- logging;
- least privilege.

The 2026 OWASP guidance emphasizes authentication/authorization, strict validation, session isolation, and hardened deployment.

---

9.15 Third-Party MCP

Before connecting:

- owner;
- source;
- tools;
- scopes;
- filesystem;
- network;
- secrets;
- update mechanism;
- reputation/history.

---

9.16 MCP Filesystem

ALLOW-LIST

Do not release the entire root unnecessarily.

---

9.17 MCP Shell

OFF BY DEFAULT

When necessary: ​​

- sandbox;
- allow-list;
- approval;
- timeout;
- logging;
- limited network;
- limited filesystem.

---

9.18 MCP Network

Do not grant automatically:

- localhost;
- LAN;
- cloud metadata;
-DB;
- internal APIs;
- full internet.

---

9.19 Confused Deputy

Validate:

WHO REQUESTED?
WHO AUTHORIZED?
WHICH AGENT?
WHICH TENANT?
WHICH RESOURCE?
WHICH ACTION?

---

9.20 AI Inventory

Inventory:

- provider;
- model;
- version;
- prompt;
- embeddings;
- DB vector;
- tools;
- agents;
- MCP;
- datasets.

---

9.21 AI Red Team

Test:

- direct injection;
- indirect injection;
- data exfiltration;
- prompt leakage;
- tool abuse;
- cross-tenant RAG;
- memory poisoning;
- resource exhaustion;
- agent loops;
- privilege escalation.


---

9.22 OWASP GenAI 2026 Baseline

Threat model must consider according to applicability:

- prompt injection;
- sensitive information disclosure;
- supply-chain risk;
- data/model poisoning;
- improper output handling;
- excessive agency;
- vector/embedding weaknesses;
- misinformation/integrity impact;
- unbounded consumption;
- agent/tool ​​misuse.

Do not use Top 10 list as a substitute for threat modeling.

---

9.23 Agentic Threats

Explicitly test:

GOAL HIJACK
TOOL MISUSE
IDENTITY/PRIVILEGE ABUSE
MEMORY POISONING
INTER-AGENT TRUST FAILURE
RESOURCE EXHAUSTION
CASCADE FAILURE
UNEXPECTED AUTONOMY

Every high-impact decision must have an authorization boundary outside the LLM.

---

9.24 Tool Poisoning / Rug Pull

Tool metadata, descriptions and schemas are untrusted input.

Before trusting:

- source;
- publisher;
- version;
- hash/signature when available;
- permissions;
- behavior;
- update channel.

Silent change of tool/plugin/MCP requires reevaluation.

---

9.25 Authorization per Tool / Resource

AUTHORIZE AGENT
≠
AUTHORIZE ALL TOOL

Each call must consider:

WHO
AGENT
TENANT
TOOL
RESOURCE
ACTION
SCOPE
RISK

---

9.26 Agent Budgets

Set limits:

- steps;
- tokens;
- tool calls;
- money;
- wall-clock time;
- retries;
- recursion depth;
- spawned agents.

Loop without limit is reliability and security risk.

---

9.27 Kill Switch

High impact agent must have mechanism for:

STOP
REVOKE
ISOLATE
DISABLE TOOL
DISABLE EGRESS

Kill switch must be tested.

---

9.28 MCP Session/Context Isolation

Never share state between users/tenants without explicit design.

Insulate:

- session;
- auth context;
- tool results;
- filesystem;
- memory;
- caches;
- temporary files.

---

9.29 MCP OAuth/Scope Discipline

When MCP uses OAuth/OIDC:

- authorization code + PKCE when applicable;
- audience/resource validation;
- minimum scopes;
- expiry token;
- recall;
- no indiscriminate token forwarding;
- per-tool/per-resource authorization.

---

9.30 AI Data Egress

Before sending data to provider/model/tool:

CLASSIFY
↓
MINIMIZE
↓
AUTHORIZE
↓
REDACT
↓
SEND

Control:

- prompt;
- attachments;
- RAG context;
- tool output;
- memory;
- logs.

---

9.31 Model / Provider Change Management

Changing model/provider may change:

- security behavior;
- tool calling;
- output format;
- latency;
- refusal behavior;
- data handling;
- retention;
- region;
- compliance.

Material change requires regression and revalidation.

---

9.32 Agent Workspace / Environment Secret Exposure

Agent with access to:

- workspace;
- shell;
- environment variables;
- filesystem;
- MCP;
- CI setup;
- local tools;

should be treated as principal capable of observing data accessible to these surfaces.

Rule:

NOT PASTED IN CHAT
≠
NOT ACCESSIBLE TO AGENT

Do not put production credential in:

- `.env` available in the agent's workspace;
- agent shell environment;
- local file accessible without need;
- logs;
- fixtures;
- screenshots;
- prompt;
- test dumps.

Prefer:

SECRET MANAGER / VAULT
+
SCOPED CREDENTIAL
+
SHORT TTL
+
APPROVED DESTINATION
+
BROKER / PROXY WHEN AVAILABLE

If real secret needs to be given to agent:

- minimum scope;
- non-prod environment when possible;
- short duration;
- restricted egress;
- logging;
- explicit authorization.

---

9.33 Credential Rotation After Agent / Workspace Exposure

Deploy by itself:

≠
ROTATION EVENT

Rotate/revoke when:

- secret has been committed;
- `.env` has been exposed;
- agent/tool ​​received secret beyond what was necessary;
- logs/output can contain secret;
- environment was compromised;
- credential scope is uncertain;
- third-party/MCP access has become unreliable.

If it is not possible to prove that the credential remained protected:

TREAT AS EXPOSED
→ REVOKE/ROTATE
→ AUDIT
→ REGRESSION

---

9.34 AI-Assisted Development Security Gate

AI-altered code requires the same or more gates:

AI CHANGE
→ DIFF REVIEW
→ SERVER-SIDE VALIDATION CHECK
→ AUTHZ REGRESSION
→ SECRET SCAN
→ SAST/SCA
→ TEST
→ BUILD
→ SECURITY GATE

Do not accept:

"AI GENERATED IT"
or
"TESTS PASSED"

as isolated proof of security.

---

⚫ MAXIMUM SAFE

- strong sandbox;
- policy engine;
- agent kill switch;
- egress control;
- per-tool AuthZ;
- signed/verified components when possible;
- anomaly detection;
- adversarial testing;
- AI incident response;
- AI governance.

---

10. TEST MATRIX

Authentication

- [ ] server-side validation bypass attempt;
- [ ] nonexistent user;
- [ ] wrong password;
- [ ] expired session;
- [ ] invalid token;
- [ ] logout;
- [ ] reset replay;
- [ ] MFA bypass.

Authorization

- [ ] horizontal scaling;
- [ ] vertical escalation;
- [ ] IDOR/BALL;
- [ ] tenant escape;
- [ ] property authorization.

Injection

- [ ] SQLi;
- [ ] NoSQLi;
- [ ] XSS;
- [ ] command injection;
- [ ] template injection.

Protocol

- [ ] CSRF;
- [ ] SSRF;
- [ ] traversal;
- [ ] redirect;
- [ ] upload bypass;
- [ ] unsigned/invalid webhook;
- [ ] exposed `.env`/config;
- [ ] exposed source maps;
- [ ] header attacks.

Anti-Abuse

- [ ] IP rotation;
- [ ] ASN rotation;
- [ ] low-and-slow;
- [ ] password spraying;
- [ ] credential stuffing;
- [ ] challenge replay;
- [ ] bot automation.

Business

- [ ] negative;
- [ ] zero;
- [ ] max;
- [ ] overflow;
- [ ] duplicate;
- [ ] replay;
- [ ] race;
- [ ] client-side price tampering;
- [ ] client-side discount/tax tampering;
- [ ] forged payment success;
- [ ] server-side total recomputation.

Reliability

- [ ] dependency timeout;
- [ ] retry;
- [ ] circuit breaker;
- [ ] cache failure;
- [ ] DB failure;
- [ ] recovery.

Accessibility

- [ ] keyboard;
- [ ] focus;
- [ ] screen reader;
- [ ] forms;
- [ ] contrast;
- [ ] authentication.

AI/MCP

- [ ] prompt injection;
- [ ] indirect injection;
- [ ] tool abuse;
- [ ] tool poisoning;
- [ ] rug pull/update change;
- [ ] excessive agency;
- [ ] tenant leak;
- [ ] cross-tenant RAG;
- [ ] filesystem;
- [ ] network;
- [ ] memory poisoning;
- [ ] session/context isolation;
- [ ] agent budget exhaustion;
- [ ] kill switch;
- [ ] per-tool/per-resource AuthZ;
- [ ] agent reads unintended `.env`/env vars;
- [ ] agent secret scope/TTL;
- [ ] secret leakage in tool/log output.

---

11. CANONICAL CI/CD PIPELINE

LOCAL / PRE-COMMIT
│
SECRET SCAN
│
ENV/CONFIG EXPOSURE CHECK
│
SOURCE MAP POLICY CHECK
│
COMMIT
│
▼
LINT
│
TYPECHECK
│
UNIT TESTS
│
SECRET SCAN
│
SAST
│
SCA
│
BUILD
│
SBOM
│
PROVENANCE / ATTESTATION
│
SIGN / VERIFY WHEN APPLICABLE
│
CONTAINER / IaC SCAN
│
INTEGRATION TESTS
│
CONTRACT TESTS
│
STAGING
│
E2E
│
DAST/API SECURITY
│
AUTHORIZATION REGRESSION
│
ACCESSIBILITY
│
PERFORMANCE CHECK
│
SECURITY GATE
│
QUALITY GATE
│
RELIABILITY GATE
│
PRIVACY / COMPLIANCE GATE WHEN APPLICABLE
│
ARTIFACT/PROVENANCE VERIFY
│
PRODUCTION
│
POST-DEPLOY VERIFY

Not all expensive tests need to run on every commit.

They must be positioned according to cost and risk.

---

11.1 Security Checks as Gates

Checklist informs.

Gate prevents progress.

For automatable controls:

CHECK
→ EXPECTED RESULT
→ FAIL CONDITION
→ CI/PRE-COMMIT
→ EVIDENCE

Examples:

SECRET FOUND
→ FAIL

PUBLIC `.env`
→ FAIL

UNSIGNED REQUIRED WEBHOOK
→ FAIL

SOURCE MAP PUBLIC WHEN POLICY=PRIVATE
→ FAIL

AUTHZ REGRESSION
→ FAIL

CROSS-TENANT ACCESS
→ FAIL

PAYMENT TOTAL TRUSTS CLIENT
→ FAIL

DEFAULT CREDENTIAL
→ FAIL

UNKNOWN in critical control:
→ FAIL RELEASE / REQUIRE REVIEW

Automation does not replace human analysis of business logic, AuthZ and architecture.

---

12. CANONICAL GATE v13.4

GOVERNANCE PASS/FAIL/UNKNOWN
ARCHITECTURE PASS/FAIL
THREAT MODEL PASS/FAIL
ADRs PASS/FAIL/N/A

INPUT VALIDATION PASS/FAIL
INJECTION PASS/FAIL
AUTHENTICATION PASS/FAIL
SERVER-SIDE VALIDATION PASS/FAIL
AUTHORIZATION PASS/FAIL
ROLES/PERMISSIONS PASS/FAIL
TENANT ISOLATION PASS/FAIL/N/A
RLS PASS/FAIL/N/A

SESSION LIFECYCLE PASS/FAIL
MFA PASS/FAIL/N/A
ANTI-ABUSE PASS/FAIL
CAPTCHA/CHALLENGE PASS/FAIL/N/A
ATO PASS/FAIL/N/A

SECRETS PASS/FAIL
GIT HISTORY PASS/FAIL
TLS PASS/FAIL
CERT LIFECYCLE PASS/FAIL
ENCRYPTION PASS/FAIL/N/A

API MINIMIZATION PASS/FAIL
CORS PASS/FAIL
CSRF PASS/FAIL/N/A
UPLOAD PASS/FAIL/N/A
SSRF PASS/FAIL/N/A
WEBHOOK PASS/FAIL/N/A
WEBHOOK SIGNATURE PASS/FAIL/N/A
WEBSOCKET PASS/FAIL/N/A
SOURCE MAP EXPOSURE PASS/FAIL/N/A
ENV/CONFIG EXPOSURE PASS/FAIL
PAYMENT SERVER AUTHORITY PASS/FAIL/N/A

PASS/FAIL DEPENDENCIES
CONTINUOUS CVE MONITOR PASS/FAIL
PACKAGE MANAGER HYGIENE PASS/FAIL
SBOM PASS/FAIL/N/A
SUPPLY CHAIN ​​PASS/FAIL
CI/CD PASS/FAIL

ERROR HANDLING PASS/FAIL
RETRY PASS/FAIL/N/A
IDEMPOTENCY PASS/FAIL/N/A
CIRCUIT BREAKER PASS/FAIL/N/A
COMPETITION PASS/FAIL
CACHE PASS/FAIL/N/A

LOAD/STRESS PASS/FAIL/N/A
RTO/RPO PASS/FAIL
BACKUP PASS/FAIL
RESTORE PASS/FAIL/UNKNOWN
DR PLAN PASS/FAIL
CHAOS PASS/FAIL/N/A

LOGGING PASS/FAIL
AUDIT TRAIL PASS/FAIL
TAMPER EVIDENCE PASS/FAIL/N/A
PASS/FAIL ALERTING
INCIDENT RESPONSE PASS/FAIL

UNIT TESTS PASS/FAIL
INTEGRATION TESTS PASS/FAIL
E2E PASS/FAIL
REGRESSION PASS/FAIL
COVERAGE GATE PASS/FAIL
CODE REVIEW PASS/FAIL

ACCESSIBILITY PASS/FAIL

LGPD PASS/FAIL/N/A
GDPR PASS/FAIL/N/A
HIPAA PASS/FAIL/N/A
PCI DSS PASS/FAIL/N/A

TERMS PASS/FAIL/PENDING LEGAL
PRIVACY POLICY PASS/FAIL/PENDING LEGAL

AI/RAG PASS/FAIL/N/A
AGENTS PASS/FAIL/N/A
AGENT SECRET EXPOSURE PASS/FAIL/N/A
MCP PASS/FAIL/N/A

LINT PASS/FAIL
TYPECHECK PASS/FAIL
TEST PASS/FAIL
BUILD PASS/FAIL


---

12.1 RELEASE GATE v13.4

A release does not receive READY just because the SECURITY GATE has passed.

SECURITY GATE
- access control;
- AuthN/AuthZ;
- tenant isolation;
- injection;
- secrets;
- supply chain;
- critical vulnerabilities;
- AI/MCP when applicable.

QUALITY GATE
- lint/typecheck;
- tests;
- regression;
- code review;
- build;
- accessibility baseline.

RELIABILITY GATE
- timeouts;
- retries/idempotency;
- migrations;
- backup/restore;
- health;
- SLO impact;
- rollback;
- critical dependency behavior.

PRIVACY / COMPLIANCE GATE
- LGPD/privacy;
- retention;
- data minimization;
- cool artifacts;
- PCI/GDPR/HIPAA when applicable.

FINAL:

READY
=
ALL APPLICABLE GATES PASS
+
NO BLOCKER
+
ARTIFACT VERIFIED
+
RESIDUAL RISK ACCEPTED WHEN NECESSARY

UNKNOWN in critical control prevents READY.

---

13. EVIDENCE RULES

AUTHORIZATION PASS
=
SERVER CONTROL
+
NEGATIVE TEST

TENANT PASS
=
ISOLATION IMPLEMENTATION
+
CROSS-TENANT TEST

RLS PASS
=
POLICY
+
MIGRATION
+
TEST

RATE LIMIT PASS
=
IMPLEMENTATION
+
OBSERVED ENFORCEMENT

BUILD PASS
=
COMMAND EXECUTED
+
EXIT CODE 0

RESTORE PASS
=
RESTORE ACTUALLY PERFORMED

ACCESSIBILITY PASS
≠
ONLY AX/LIGHTHOUSE PASSED


EVIDENCE FRESHNESS

PASS requires evidence applicable to the release evaluated.

Prefer link to:

COMMIT SHA
+
ARTIFACT DIGEST
+
ENVIRONMENT
+
TEST RUN
+
TIMESTAMP

STALE EVIDENCE
→ UNKNOWN / REVALIDATE


---

14. SECURITY_AUDIT.md

Every full audit must produce:

SECURITY_AUDIT.md

Structure:
1. Executive Summary;
2. Scope;
3. Detected Stack;
4. Architecture;
5. Threat Model;
6. Data Classification;
7. Findings;
8. Severity Matrix;
9. AuthN;
10. AuthZ;
11. Multi-Tenancy;
12. Anti-Abuse;
13. Web/API;
14. Database/RLS;
15. Privacy;
16. Secrets;
17. Git History;
18.Cloud;
19. Supply Chain;
20. Reliability;
21. Cache;
22. Performance;
23.DR;
24. Logging;
25. Incident Response;
26. Testing;
27. Accessibility;
28. AI/MCP;
29. Cool;
30. Gate;
31. Commands;
32. Evidence;
33. External Actions;
34. Residual Risks;
35. Standard Mappings;
36. Artifact/Provenance;
37. Release Gate Decision;
38. Limitations / Unknowns.

---

15. FINDING FORMAT

ID:
SEC-XXX

SEVERITY:
CRITICAL / HIGH / MEDIUM / LOW / INFO

PRIORITY:
P0/P1/P2/P3

DOMAIN:
...


STANDARD_MAPPING:
ASVS / OWASP / NIST / PCI / WCAG / GENAI / MCP / OTHER

ASSET:
...

ATTACK_PATH:
...

CWE/CVE:
...

CVSS:
...

KEV:
YES / NO / N/A

EPSS:
...

CONTROL_ID:
...


FILE:
...

LINE:
...

PROBLEM:
...

IMPACT:
...

EVIDENCE:
...

EXPLOITABILITY:
...

FIX:
...

TEST:
...

OWNER:
...

STATUS:
OPEN / FIXED / MITIGATED / ACCEPTED

---

16. EXTERNAL ACTIONS

Never mark as completed without execution.

Examples:

[ ] ROTATE PROVIDER SECRET

[ ] ENABLE BRANCH PROTECTION

[ ] CONFIGURE DNS

[ ] ENABLE TLS

[ ] RUN REAL RESTORE

[ ] LEGAL REVIEW

[ ] ENABLE MFA IN CLOUD CONSOLE

---

17. REPOSITORY EXECUTION ORDER

1. INSPECT
2. DETECT STACK
3. MAP ARCHITECTURE
4. MAP DATA
5. MAP TRUST BOUNDARIES
6. THREAT MODEL
7. SECRET SCAN
8. GIT HISTORY SCAN
9. FINDINGS
10. CLASSIFY
11. FIX P0
12. FIX P1
13. FIX P2
14. FIX RELEVANT P3
15. ADD TESTS
16. ADD REGRESSIONS
17. RUN STATIC ANALYSIS
18. RUN SECURITY SCANS
19. RUN LINT
20. RUN TYPECHECK
21. RUN UNIT
22. RUN INTEGRATION
23. RUN E2E
24. BUILD
25. PERFORMANCE/RESILIENCE CHECKS
26. ACCESSIBILITY CHECKS
27. REVIEW DIFF
28. VERIFY ARTIFACT/PROVENANCE
29. SECURITY GATE
30. QUALITY GATE
31. RELIABILITY GATE
32. PRIVACY/COMPLIANCE GATE WHEN APPLICABLE
33. POST-DEPLOY / RELEASE CHECK PLAN
34. SECURITY_AUDIT.md
35. FINAL AUDIT

---

18. AGENT RULES

Agent running this protocol must:

- discover stack before changing;
- preserve architecture when appropriate;
- change the minimum necessary;
- test later;
- do not falsify results;
- do not reveal secrets;
- do not invent compliance;
- do not destroy Git history automatically;
- do not attack third parties;
- do not carry out destructive pen testing in production;
- do not weaken control to make the test pass;
- do not mark PASS with evidence of a different release;
- do not install dependencies suggested by AI without verification;
- do not expand scope/token/tool ​​permission to circumvent failure;
- do not carry out destructive action without appropriate authorization;
- preserve traceability between source, build, artifact and deploy.

---

19. NEW THREAT WORKFLOW

All new vulnerability or defense:

DISCOVER
↓
VERIFY SOURCE / REPRODUCIBILITY
↓
CLASSIFY
↓
MAP DOMAIN
↓
DESIGN CONTROL
↓
IMPLEMENT
↓
CREATE TEST
↓
ADD REGRESSION
↓
UPDATE PROTOCOL

---

20. EXCEPTION PROCESS

CONTROL:
...

REASON:
...

RISK:
...

COMPENSATING CONTROL:
...

OWNER:
...

EXPIRY:
...

APPROVAL:
...

Exception without expiration becomes permanent debt.

---

21. CANONICAL PRINCIPLES

DEFAULT DENY

LEAST PRIVILEGE

DEFENSE IN DEPTH

SECURE BY DESIGN

SECURE BY DEFAULT

FAIL SECURE

ASSUME BREACH

VERIFY EXPLICITLY

MINIMIZE DATE

MINIMIZE ATTACK SURFACE

SERVER IS AUTHORITY

CLIENT INPUT IS UNTRUSTED

TENANT INPUT IS UNTRUSTED

EXTERNAL DATA IS UNTRUSTED

AI OUTPUT IS UNTRUSTED

IDENTITY ≠ AUTHORIZATION

UUID ≠ ACCESS CONTROL

JWT ≠ AUTHORIZATION

FINGERPRINT ≠ IDENTITY

CAPTCHA ≠ AUTHENTICATION

IP ≠ USER

CORS ≠ AUTHORIZATION

WAF ≠ FIX

CACHE ≠ SOURCE OF TRUTH

RETRY ≠ ALWAYS SAFE

BACKUP ≠ RECOVERY UNTIL TESTED

COVERAGE ≠ QUALITY

SCANNER PASS ≠ SECURE

CODE ≠ CONTROL UNTIL VERIFIED

DOCUMENTATION ≠ IMPLEMENTATION

COMPLIANCE ≠ SECURITY

CVSS ≠ PRIORITY

ATTESTATION ≠ VERIFICATION

STAGING PASS ≠ PRODUCTION PROVEN

DEPLOY SUCCESS ≠ RELEASE HEALTHY

AGENT ≠ AUTHORITY

TOOL DESCRIPTION ≠ TRUST

MISSING CONFIG ≠ PERMISSION TO FAIL OPEN

DB PASSWORD ≠ NETWORK PERIMETER

PUBLISHED PORT ≠ REQUIRED CONNECTIVITY

FRONTEND VALUE ≠ BUSINESS AUTHORITY

PAYMENT UI ≠ PAYMENT CONFIRMATION

WEBHOOK URL ≠ WEBHOOK AUTHENTICATION

SOURCE MAP ≠ HARMLESS BY DEFAULT

DEFAULT CREDENTIAL ≠ SAFE DEVELOPMENT SHORTCUT

SUBNET ≠ SECURITY BOUNDARY

VLAN ≠ AUTHORIZATION

VPN ≠ TRUST

HIDDEN ≠ SECURE

PRIVATE NETWORK ≠ AUTHORIZATION

MEMORY ≠ POLICY

SECURITY ≠ RELIABILITY

BUT PRODUCTION REQUIRES BOTH

---

22. TRIGGER

Upon receipt:

SECURITY

Apply:

SECURITY PROTOCOL v13

and, with access to the repository:

INSPECT
→ FIND
→ FIX
→ TEST
→ VERIFY
→ DOCUMENT

Don't just stop at recommendations when corrections can be made.

---

23. FINAL MATURITY

🟢 BASIC

NO OBVIOUS FAILURES

🟡 INTERMEDIATE

PRODUCTION DEFENSIBLE

🔴 ADVANCED

RESILIENT AGAINST
REAL ATTACKS
AND REAL FAILURES

⚫ MAXIMUM SAFE

PREVENT
DETECT
CONTAIN
RECOVER
PROVE
ADAPT

---

24. FINAL EQUATION

PRODUCTION READINESS
=
SECURITY
+
CORRECTNESS
+
RELIABILITY
+
RESILIENCE
+
PERFORMANCE
+
PRIVACY
+
ACCESSIBILITY
+
OBSERVABILITY
+
TESTABILITY
+
RECOVERABILITY
+
DOCUMENTATION
+
SUPPLY CHAIN ​​INTEGRITY
+
GOVERNANCE
+
CONTINUOUS IMPROVEMENT


---

25. TOOLING — INSECURE DEFAULTS / TRAIL OF BITS

Requirement:

- Codex CLI;
- own or explicitly authorized repository.

Marketplace:

```bash
codex plugin marketplace add trailofbits/skills
codex plugin list
codex plugin add insecure-defaults@trailofbits
```

Run in chat Codex:

```text
/insecure-defaults:audit
```

Specific scope:

```text
/insecure-defaults:audit src/
```

Or file:

```text
/insecure-defaults:audit src/config/app.py
```

Expected result by finding:

- category;
- file/line;
- achievable default;
- actually active insecure value;
- security sink;
- reachability;
- severity;
- correction;
- coverage gap when applicable.

Validation rule for authentication:

WITHOUT `REQUIRE_AUTH`
→ APPLICATION MUST FAIL CLOSED

Acceptable:

STARTUP FAIL

or

AUTH CONTINUES REQUIRED

Not acceptable:

AUTH DISABLED BY DEFAULT

The plugin should complement, not replace:

- secret scan;
- Semgrep;
- SAST;
- ACS;
- manual review;
- negative tests.

---

26. VERIFIED REFERENCES — 09/09/2026

Application:
- OWASP Top 10:2025 — current version;
- OWASP ASVS 5.0.0 — latest stable;
- OWASP API Security Top 10:2023.

Identity:
- NIST SP 800-63-4 — final, July 2025;
- NIST SP 800-63B-4 — final, July 2025;
- RFC 9700;
- RFC 10017 — Best Current Practice, August 2026.

Secure SDLC / Supply Chain:
- Trail of Bits Skills — `insecure-defaults`;
- Docker Compose Networking — service-to-service via internal/default network;
- Docker Official Image — PostgreSQL (`POSTGRES_PASSWORD`, `POSTGRES_HOST_AUTH_METHOD`);
- Docker Engine Networking / Port Publishing / Packet Filtering;
- NIST SP 800-207 — Zero Trust Architecture;
- NIST SP 800-207A — Zero Trust for Cloud-Native Applications;
- CISA Zero Trust Maturity Model v2;
- CISA network segmentation/hardening guidance;
- NIST SP 800-218 SSDF 1.1 — final;
- SP 800-218 Rev. 1 / SSDF 1.2 — draft;
- NIST SP 800-218A — final;
- SLSA 1.2 — Approved;
- CISA KEV;
- CISA SSVC;
- FIRST CVSS 4.0;
- FIRST EPSS.

Incident Response:
- NIST CSF 2.0;
- NIST SP 800-61 Rev. 3 — final, April 2025;
- NIST SP 800-34 Rev. 1.

Privacy:
- LGPD;
- CD/ANPD Resolution No. 15/2024 — Security Incident Communication;
- communication to the ANPD/holder according to applicability: 3 working days;
- incident record: minimum of 5 years.

Accessibility:
- WCAG 2.2;
- recommended baseline: level AA.

Payments:
- PCI DSS 4.0.1 — current published version.

IA / Agents / MCP:
- OpenAI sandbox/environment security — keep application credentials outside the agent environment when possible; secrets injected into the environment can be read by the agent's code;
- OWASP GenAI LLM Top 10 2026;
- OWASP Top 10 for Agentic Applications 2026;
- OWASP MCP Top 10;
- OWASP Practical Guide for Secure MCP Server Development.

---

27. CONSISTENCY CHECK v13.4

Before declaring audit complete:

[ ] protocol version = v13
[ ] stack detected
[ ] documented scope
[ ] trust boundaries mapped
[ ] verified blockers
[ ] P0/P1 treated
[ ] negative tests performed
[ ] tenant tests run when applicable
[ ] secrets/history checked
[ ] insecure defaults audited
[ ] critical flags fail closed when missing
[ ] private database ports by default
[ ] guest/client network isolated from management/data zone
[ ] subnet/VLAN has explicit ACL/firewall when used as boundary
[ ] management plane is not directly exposed to the Internet
[ ] Docker published ports have been externally tested
[ ] no default/dev credentials active in production
[ ] PostgreSQL `trust` missing in reachable surface
[ ] `.env`/config/dumps are not publicly reachable
[ ] source map policy validated
[ ] payments recalculated/confirmed on server
[ ] sensitive authenticated and replay-protected webhooks
[ ] proven server-side validation for critical rules
[ ] accounts/admin plan segregated according to risk
[ ] agents do not receive real secrets beyond what is necessary
[ ] `.env`/env exposure to agent has been reviewed
[ ] dependencies/CVEs have continuous monitoring
[ ] package manager uses deterministic lockfile/install/gates
[ ] KEV/EPSS/context considered
[ ] build reproduced
[ ] artifact digest registered
[ ] provenance verified when available
[ ] restore actually tested when required
[ ] accessibility not based on scanner only
[ ] AI/MCP tested where applicable
[ ] security gate PASS
[ ] quality gate PASS
[ ] reliability gate PASS
[ ] privacy/compliance gate PASS/N/A/PENDING LEGAL suitable
[ ] explicit unknowns
[ ] explicit residual risks
[ ] SECURITY_AUDIT.md produced

---

28. FINAL DECISION

Use only:

READY
NOT READY
READY WITH ACCEPTED RISK

READY requires:

NO CRITICAL BLOCKER
+
ALL APPLICABLE GATES PASS
+
ARTIFACT VERIFIED
+
EVIDENCE CURRENT

READY WITH ACCEPTED RISK requires:

RISK
+
OWNER
+
JUSTIFICATION
+
COMPENSATING CONTROL
+
EXPIRY
+
APPROVAL

Do not use:

"PROBABLY SAFE"
"LOOKS SECURE"
"SCANNER PASSED"
"BUILD PASSED"

as a production decision.


---

END — SECURITY PROTOCOL v13.4

BUILD SECURE.

BUILD RELIABLE.

CHECK EVERYTHING.

FAIL SAFELY.

RECOVER BY DESIGN.

TRY CRITICAL CONTROLS.

ADAPT CONTINUOUSLY.