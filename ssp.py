#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ssp.py — Sovereign Security Protocol (SSP v13.4) Universal CLI & Layer Engine
Community Edition 0.3.0 | Pure Python 3.10+ Standard Library (Zero Dependencies)

Capabilities:
  --doctor      Full diagnostic of canonical SHA-256, schemas, links, canvas & parity
  init          Bootstrap SSP 7-Layer security scaffolding (.ssp/) in ANY project
  scan          Run 7-Layer Defense-in-Depth heuristic audit on ANY codebase
  blueprint     Display practical Defense-in-Depth layers & controls in terminal
  gate          Evaluate SSP-12 Release Assurance Gate (freshness + expiry + N/A rules)
  validate      Validate SSP repository links, assets, canvas, crosswalk & schemas
  check-parity  Verify PT-BR <-> EN bilingual documentation parity
  matrix        Print the 13 SSP controls matrix and minimum evidence levels
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
from typing import Any, Dict, List, Optional, Tuple

# Ensure UTF-8 output on Windows consoles (PowerShell / CMD)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

SSP_PROTOCOL_VERSION = "13.4.0"
COMMUNITY_EDITION_VERSION = "0.3.0"
CANONICAL_PT_SHA256_LF = "a83e8a27c02f5c57befc2cf0e9f0b7c8a020b2618a6f28ca55ce62b070f092f6"
CANONICAL_PT_BYTES_LF = 96328

REPO_ROOT = pathlib.Path(__file__).resolve().parent

BILINGUAL_DOC_PAIRS: List[Tuple[str, str]] = [
    ("protocolo.md", "protocol.md"),
    ("adocao-e-evidencias.md", "adoption-and-evidence.md"),
    ("agentes-jarvis-obsidian.md", "agentic-jarvis-obsidian.md"),
    ("guia-rapido-adocao.md", "quickstart-adoption.md"),
    ("camadas-por-sistema.md", "layers-by-system.md"),
    ("ecossistema-e-referencias-50k.md", "ecosystem-and-50k-references.md"),
]

SEVEN_LAYERS: List[Dict[str, Any]] = [
    {
        "layer": 1,
        "controls": ["SSP-01", "SSP-02", "SSP-05"],
        "title_pt": "Governança, Ativos, Fronteiras & Zero Segredos",
        "title_en": "Governance, Assets, Trust Boundaries & Zero Secrets",
        "goal_pt": "Mapear ativos/owners, tratar entradas externas como não confiáveis, proibir segredos hardcoded e falhar fechado.",
        "goal_en": "Map assets/owners, treat external inputs as untrusted, forbid hardcoded secrets, and fail closed.",
    },
    {
        "layer": 2,
        "controls": ["SSP-03", "SSP-05"],
        "title_pt": "Identidade, Sessão & Autorização Fina (Anti-BOLA)",
        "title_en": "Identity, Session & Fine-Grained Authorization (Anti-BOLA)",
        "goal_pt": "Exigir MFA administrativo, menor privilégio e validar Principal × Ação × Recurso × Tenant em toda rota.",
        "goal_en": "Enforce admin MFA, least privilege, and Principal × Action × Resource × Tenant checks on every route.",
    },
    {
        "layer": 3,
        "controls": ["SSP-06"],
        "title_pt": "Entradas, APIs & Invariantes de Negócio",
        "title_en": "Inputs, APIs & Business Invariants",
        "goal_pt": "Validar schemas no servidor, parametrizar queries, impor rate-limit, idempotência e proteção anti-replay.",
        "goal_en": "Validate schemas server-side, parameterize queries, enforce rate-limiting, idempotency, and anti-replay.",
    },
    {
        "layer": 4,
        "controls": ["SSP-04", "SSP-10", "SSP-11"],
        "title_pt": "Dados, Isolamento RLS, Recuperação & Logs Redigidos",
        "title_en": "Data, RLS Isolation, Recovery & Redacted Logs",
        "goal_pt": "Criptografar trânsito/repouso, ativar Row-Level Security multi-tenant, redigir PII nos logs e testar restore.",
        "goal_en": "Encrypt in transit/at rest, enable multi-tenant Row-Level Security, redact PII in logs, and exercise restores.",
    },
    {
        "layer": 5,
        "controls": ["SSP-08"],
        "title_pt": "Infraestrutura, Rede Privada & Isolamento de Containers",
        "title_en": "Infrastructure, Private Network & Container Isolation",
        "goal_pt": "Manter bancos/planos admin em loopback/rede privada (127.0.0.1), rodar containers non-root e filtrar egress.",
        "goal_en": "Keep DBs/admin planes on loopback/private nets (127.0.0.1), run non-root containers, and filter egress.",
    },
    {
        "layer": 6,
        "controls": ["SSP-07"],
        "title_pt": "Supply Chain, Dependências Fixadas & Proveniência",
        "title_en": "Supply Chain, Pinned Dependencies & Provenance",
        "goal_pt": "Exigir lockfiles determinísticos, SBOM, priorização CISA KEV + EPSS e verificação de proveniência SLSA.",
        "goal_en": "Require deterministic lockfiles, SBOM, CISA KEV + EPSS triage, and SLSA provenance verification.",
    },
    {
        "layer": 7,
        "controls": ["SSP-09", "SSP-12", "SSP-13"],
        "title_pt": "IA Agentiva, Contenção MCP & Portão de Release",
        "title_en": "Agentic AI, MCP Containment & Release Assurance Gate",
        "goal_pt": "Aplicar autoridade fora do LLM, vincular aprovação humana ao digest do plano, ter kill-switch e exigir evidência fresca por commit.",
        "goal_en": "Enforce authority outside the LLM, bind human approval to plan digest, keep a kill-switch, and require commit-fresh evidence.",
    },
]

PROFILES: Dict[str, Dict[str, Any]] = {
    "web-api": {
        "description_pt": "Aplicações Web, REST/GraphQL APIs e Backends",
        "description_en": "Web Applications, REST/GraphQL APIs, and Backends",
        "priority_controls": ["SSP-03", "SSP-05", "SSP-06", "SSP-07", "SSP-11", "SSP-12"],
    },
    "saas-multitenant": {
        "description_pt": "Plataformas SaaS Multi-Tenant com Dados Sensíveis",
        "description_en": "Multi-Tenant SaaS Platforms with Sensitive Data",
        "priority_controls": ["SSP-01", "SSP-02", "SSP-03", "SSP-04", "SSP-06", "SSP-08", "SSP-10", "SSP-12"],
    },
    "ai-agent-mcp": {
        "description_pt": "Agentes Autônomos de IA, Pipelines RAG e Servidores MCP",
        "description_en": "Autonomous AI Agents, RAG Pipelines, and MCP Servers",
        "priority_controls": ["SSP-02", "SSP-03", "SSP-04", "SSP-05", "SSP-08", "SSP-09", "SSP-11", "SSP-12"],
    },
    "microservice": {
        "description_pt": "Microsserviços, Workers de Fila e Containers Cloud",
        "description_en": "Microservices, Queue Workers, and Cloud Containers",
        "priority_controls": ["SSP-05", "SSP-06", "SSP-07", "SSP-08", "SSP-10", "SSP-11", "SSP-12"],
    },
    "cli-desktop": {
        "description_pt": "Ferramentas CLI, Apps Desktop/Mobile e Runtimes Locais",
        "description_en": "CLI Tools, Desktop/Mobile Apps, and Local-First Runtimes",
        "priority_controls": ["SSP-04", "SSP-05", "SSP-06", "SSP-07", "SSP-10", "SSP-12", "SSP-13"],
    },
}

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
    "target",
    "vendor",
    ".next",
    ".nuxt",
    ".system_generated",
}

CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".mjs", ".cjs",
    ".go", ".rs", ".java", ".kt", ".cs", ".php", ".rb",
}

CONFIG_EXTENSIONS = {
    ".json", ".yml", ".yaml", ".toml", ".ini", ".cfg", ".conf", ".env", ".properties",
}


# ============================================================================
# REPOSITORY SELF-VALIDATION FUNCTIONS
# ============================================================================

def verify_canonical_protocol_integrity(root: pathlib.Path) -> List[str]:
    errors: List[str] = []
    proto_pt = root / "protocol" / "v13.4" / "PROTOCOLO_INTEGRAL_v13.4_PT-BR.md"
    if not proto_pt.exists():
        return [f"Missing canonical protocol file: {proto_pt}"]
    raw = proto_pt.read_bytes()
    lf_bytes = raw.replace(b"\r\n", b"\n")
    digest = hashlib.sha256(lf_bytes).hexdigest()
    if len(lf_bytes) != CANONICAL_PT_BYTES_LF:
        errors.append(
            f"Canonical PT-BR byte length mismatch: expected {CANONICAL_PT_BYTES_LF} LF bytes, got {len(lf_bytes)}"
        )
    if digest != CANONICAL_PT_SHA256_LF:
        errors.append(
            f"Canonical PT-BR SHA-256 mismatch: expected {CANONICAL_PT_SHA256_LF}, got {digest}"
        )
    return errors


def find_markdown_files(root: pathlib.Path):
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def _strip_fenced_code_blocks(markdown_text: str) -> str:
    lines = []
    in_fence = False
    fence_marker = ""
    for line in markdown_text.splitlines():
        stripped = line.lstrip()
        if not in_fence:
            m = re.match(r"^(`{3,}|~{3,})", stripped)
            if m:
                in_fence = True
                fence_marker = m.group(1)
                continue
            lines.append(line)
        else:
            if stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = ""
    return "\n".join(lines)


def check_markdown_links(root: pathlib.Path) -> Tuple[int, int, List[str]]:
    errors: List[str] = []
    checked_count = 0
    link_count = 0

    md_link_pattern = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
    html_src_pattern = re.compile(r'(?:src|href)=["\']([^"\']+)["\']')

    for md_path in find_markdown_files(root):
        checked_count += 1
        raw_content = md_path.read_text(encoding="utf-8", errors="ignore")
        content = _strip_fenced_code_blocks(raw_content)

        candidates: List[Tuple[str, str]] = []
        for match in md_link_pattern.finditer(content):
            candidates.append((match.group(1), match.group(2).strip()))
        for match in html_src_pattern.finditer(content):
            candidates.append(("html-attr", match.group(1).strip()))

        for label, raw_link in candidates:
            if raw_link.startswith(("http://", "https://", "mailto:", "#", "data:", "conversation://", "file://")):
                continue
            link_count += 1
            clean_link = raw_link.split("#")[0].split("?")[0].replace("%20", " ").strip()
            if not clean_link:
                continue
            target = (md_path.parent / clean_link).resolve()
            if not target.exists():
                rel_source = md_path.relative_to(root)
                errors.append(f"Broken link in {rel_source}: [{label}]({raw_link}) -> '{target}' not found")

    return checked_count, link_count, errors


def check_canvas_nodes(root: pathlib.Path) -> Tuple[int, List[str]]:
    canvas_file = root / "SSP-13.4.canvas"
    errors: List[str] = []
    if not canvas_file.exists():
        return 0, [f"Canvas file {canvas_file} not found"]

    try:
        data = json.loads(canvas_file.read_text(encoding="utf-8"))
        nodes = data.get("nodes", [])
        node_ids = {n.get("id") for n in nodes}
        for node in nodes:
            if node.get("type") == "file":
                fpath = node.get("file")
                if fpath:
                    target = (root / fpath).resolve()
                    if not target.exists():
                        errors.append(f"Canvas node '{node.get('id')}' references missing file: {fpath}")
        for edge in data.get("edges", []):
            if edge.get("fromNode") not in node_ids or edge.get("toNode") not in node_ids:
                errors.append(f"Canvas edge '{edge.get('id')}' references unknown node")
        return len(nodes), errors
    except Exception as exc:
        return 0, [f"Failed to parse Canvas JSON: {exc}"]


def check_crosswalk(root: pathlib.Path) -> Tuple[int, List[str]]:
    csv_file = root / "control-crosswalk.csv"
    proto_pt = root / "protocol" / "v13.4" / "PROTOCOLO_INTEGRAL_v13.4_PT-BR.md"
    errors: List[str] = []

    if not csv_file.exists():
        return 0, [f"Missing {csv_file}"]
    if not proto_pt.exists():
        return 0, [f"Missing canonical protocol file: {proto_pt}"]

    proto_text = proto_pt.read_text(encoding="utf-8", errors="ignore")

    rows = []
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required_cols = {"control_id", "community_control", "source_sections", "source_domain", "evidence_focus"}
        if not required_cols.issubset(set(reader.fieldnames or [])):
            errors.append(f"CSV header missing required columns. Found: {reader.fieldnames}")
            return 0, errors
        for r in reader:
            rows.append(r)

    if len(rows) != 13:
        errors.append(f"Expected 13 controls (SSP-01 to SSP-13), found {len(rows)}")

    for r in rows:
        cid = r.get("control_id")
        sections = r.get("source_sections", "")
        raw_tokens = [tok.strip() for tok in re.split(r"[;,\s]+", sections) if tok.strip()]
        for token in raw_tokens:
            base_sec = token.split("-")[0].strip()
            if not base_sec:
                continue
            pattern = re.compile(rf"(?:^|\n)\s*{re.escape(base_sec)}(?:[\.\s\:\—\–\-]|$)", re.M)
            if not pattern.search(proto_text):
                errors.append(
                    f"Control {cid}: Section '{base_sec}' referenced from '{sections}' not located in canonical protocol"
                )

    return len(rows), errors


def check_controls_json(root: pathlib.Path) -> Tuple[int, List[str]]:
    json_path = root / "protocol" / "v13.4" / "ssp-controls.json"
    schema_path = root / "schema" / "ssp-control.schema.json"
    errors: List[str] = []

    if not json_path.exists():
        return 0, [f"Missing {json_path}"]
    if not schema_path.exists():
        return 0, [f"Missing schema: {schema_path}"]

    try:
        json.loads(schema_path.read_text(encoding="utf-8"))
        data = json.loads(json_path.read_text(encoding="utf-8"))
        controls = data.get("controls", [])
        if len(controls) != 13:
            errors.append(f"ssp-controls.json must contain exactly 13 controls, found {len(controls)}")

        seen_ids = set()
        for c in controls:
            cid = c.get("id")
            if not re.match(r"^SSP-(0[1-9]|1[0-3])$", cid or ""):
                errors.append(f"Invalid control ID format: {cid}")
            if cid in seen_ids:
                errors.append(f"Duplicate control ID: {cid}")
            seen_ids.add(cid)
            if not c.get("blocker_criteria"):
                errors.append(f"Control {cid} has no blocker_criteria defined")
            if c.get("minimum_evidence_level") not in {"L0", "L1", "L2", "L3"}:
                errors.append(f"Control {cid} has invalid minimum_evidence_level")

        return len(controls), errors
    except Exception as exc:
        return 0, [f"Error parsing ssp-controls.json or schema: {exc}"]


def check_bilingual_parity(root: pathlib.Path) -> Tuple[List[Tuple[str, str, bool]], List[str]]:
    pt_dir = root / "docs" / "pt-BR"
    en_dir = root / "docs" / "en"
    errors: List[str] = []
    report: List[Tuple[str, str, bool]] = []

    for pt_name, en_name in BILINGUAL_DOC_PAIRS:
        pt_file = pt_dir / pt_name
        en_file = en_dir / en_name
        ok = pt_file.exists() and en_file.exists()
        report.append((pt_name, en_name, ok))
        if not ok:
            errors.append(f"Missing bilingual pair: {pt_name} <-> {en_name}")
        elif pt_name == "protocolo.md":
            pt_ids = set(re.findall(r"\bSSP-(?:0[1-9]|1[0-3])\b", pt_file.read_text(encoding="utf-8")))
            en_ids = set(re.findall(r"\bSSP-(?:0[1-9]|1[0-3])\b", en_file.read_text(encoding="utf-8")))
            if len(pt_ids) != 13 or pt_ids != en_ids:
                errors.append(f"Control ID mismatch between protocolo.md ({len(pt_ids)}) and protocol.md ({len(en_ids)})")

    for readme_name in ("README.md", "README.pt-BR.md", "README.en.md"):
        if not (root / readme_name).exists():
            errors.append(f"Missing root entry README: {readme_name}")

    return report, errors


# ============================================================================
# UNIVERSAL TARGET SYSTEM SCANNER & BOOTSTRAPPER (ANY REPOSITORY)
# ============================================================================

def _get_git_head_sha(target_dir: pathlib.Path) -> str:
    try:
        res = subprocess.run(
            ["git", "-C", str(target_dir), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return "UNCOMMITTED_WORKSPACE"


def _is_git_tracked(target_dir: pathlib.Path, rel_path: str) -> bool:
    try:
        res = subprocess.run(
            ["git", "-C", str(target_dir), "ls-files", "--error-unmatch", rel_path],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return res.returncode == 0
    except Exception:
        return False


def _iter_project_files(target_dir: pathlib.Path):
    for p in target_dir.rglob("*"):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(target_dir).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        yield p


def _is_test_or_scanner_self_file(rel_posix: str) -> bool:
    lower = rel_posix.lower()
    base = lower.rsplit("/", 1)[-1]
    if base in {"ssp.py", "ssp_tool.py"}:
        return True
    if "/tests/" in f"/{lower}" or base.startswith("test_") or base.endswith(("_test.py", ".test.ts", ".test.js", ".spec.ts", ".spec.js")):
        return True
    return False


def scan_target_system(target_dir: pathlib.Path) -> Dict[str, Any]:
    """
    Deterministic, 100% offline 7-Layer Defense-in-Depth baseline scanner for ANY project.
    Returns structured results per layer without claiming certification or replacing human review.
    """
    target_dir = target_dir.resolve()
    files = list(_iter_project_files(target_dir))
    rel_map = {p.relative_to(target_dir).as_posix(): p for p in files}

    # Stack detection
    stacks: List[str] = []
    if any(k.endswith(("pyproject.toml", "requirements.txt", ".py")) for k in rel_map):
        stacks.append("Python")
    if any(k.endswith(("package.json", "tsconfig.json", ".ts", ".js")) for k in rel_map):
        stacks.append("Node.js/TypeScript")
    if any(k.endswith(("go.mod", ".go")) for k in rel_map):
        stacks.append("Go")
    if any(k.endswith(("Cargo.toml", ".rs")) for k in rel_map):
        stacks.append("Rust")
    if any(k.endswith(("pom.xml", "build.gradle", "build.gradle.kts", ".java")) for k in rel_map):
        stacks.append("Java/JVM")
    if any("dockerfile" in k.lower() or "docker-compose" in k.lower() or "compose.y" in k.lower() for k in rel_map):
        stacks.append("Docker/Containers")
    if any(k.startswith(".github/workflows/") for k in rel_map):
        stacks.append("GitHub Actions CI")
    if any("mcp" in k.lower() or "agent" in k.lower() for k in rel_map):
        stacks.append("AI Agents / MCP")
    if not stacks:
        stacks.append("Generic / Documentation")

    findings: Dict[int, List[Dict[str, str]]] = {i: [] for i in range(1, 8)}

    # Secret patterns (constructed safely to avoid self-matching)
    pk_header = "-----BEGIN " + r"(?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----"
    secret_patterns = [
        ("Private Key Block", re.compile(pk_header)),
        ("OpenAI API Key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b")),
        ("GitHub Personal/App Token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,})\b")),
        ("AWS Access Key ID", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
        ("Google API Key", re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b")),
        ("Slack Token", re.compile(r"\bxox[baprs]-[0-9A-Za-z\-]{24,}\b")),
    ]

    # --- Layer 1: Governance & Secrets (SSP-01, SSP-02, SSP-05) ---
    gitignore_path = target_dir / ".gitignore"
    gitignore_text = gitignore_path.read_text(encoding="utf-8", errors="ignore") if gitignore_path.exists() else ""
    if not gitignore_path.exists():
        findings[1].append({
            "severity": "WARN",
            "control": "SSP-05",
            "message": "Missing .gitignore file; local secrets or build artifacts risk accidental commit.",
            "location": ".gitignore",
        })

    for rel_posix, fpath in rel_map.items():
        base = fpath.name
        if base == ".env" or (base.startswith(".env.") and not base.endswith((".example", ".sample", ".template"))):
            env_ignored = (".env" in gitignore_text) and not _is_git_tracked(target_dir, rel_posix)
            if not env_ignored:
                findings[1].append({
                    "severity": "BLOCKER",
                    "control": "SSP-05",
                    "message": f"Active environment file '{rel_posix}' is not protected by .gitignore or is tracked in Git.",
                    "location": rel_posix,
                })

        if fpath.suffix.lower() in (CODE_EXTENSIONS | CONFIG_EXTENSIONS) and fpath.stat().st_size <= 1_000_000:
            if _is_test_or_scanner_self_file(rel_posix):
                continue
            text = fpath.read_text(encoding="utf-8", errors="ignore")
            for label, pat in secret_patterns:
                if pat.search(text):
                    findings[1].append({
                        "severity": "BLOCKER",
                        "control": "SSP-05",
                        "message": f"Potential hardcoded credential detected ({label}). Move to secret manager / runtime env.",
                        "location": rel_posix,
                    })

    if not (target_dir / "SECURITY.md").exists() and not (target_dir / ".github" / "SECURITY.md").exists():
        findings[1].append({
            "severity": "WARN",
            "control": "SSP-01",
            "message": "Missing SECURITY.md vulnerability disclosure & security ownership policy.",
            "location": "SECURITY.md",
        })

    # --- Layer 2: Identity, Session & Fail-Closed Config (SSP-03, SSP-05) ---
    fail_open_checks = [
        ("BLOCKER", "SSP-05", "Fail-open authentication flag detected (auth disabled).", re.compile(r"\b(?:REQUIRE_AUTH|AUTH_ENABLED)\s*[:=]\s*['\"]?(?:false|0|no)['\"]?", re.I)),
        ("BLOCKER", "SSP-03", "JWT 'none' algorithm permitted; enables signature bypass.", re.compile(r"""(?:algorithms\s*=\s*\[[^\]]*['"]none['"]|['"]alg['"]\s*:\s*['"]none['"])""", re.I)),
        ("WARN", "SSP-05", "TLS certificate verification explicitly disabled.", re.compile(r"(?:verify\s*=\s*False|rejectUnauthorized\s*:\s*false|InsecureSkipVerify\s*:\s*true|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*['\"]?0)", re.M)),
        ("WARN", "SSP-05", "Hardcoded DEBUG=True in source/config; ensure production fails closed.", re.compile(r"^\s*DEBUG\s*=\s*True\b", re.M)),
    ]

    for rel_posix, fpath in rel_map.items():
        if fpath.suffix.lower() not in (CODE_EXTENSIONS | CONFIG_EXTENSIONS) or _is_test_or_scanner_self_file(rel_posix):
            continue
        if fpath.stat().st_size > 1_000_000:
            continue
        text = fpath.read_text(encoding="utf-8", errors="ignore")
        for sev, ctrl, msg, pat in fail_open_checks:
            if pat.search(text):
                findings[2].append({"severity": sev, "control": ctrl, "message": msg, "location": rel_posix})

    # --- Layer 3: Inputs, APIs & Injection Sinks (SSP-06) ---
    sink_checks = [
        ("WARN", "SSP-06", "Subprocess invoked with shell=True; prefer argument list without shell.", re.compile(r"subprocess\.(?:run|Popen|call|check_output)\([^)]*shell\s*=\s*True")),
        ("BLOCKER", "SSP-06", "SQL query built via direct f-string/template interpolation (SQLi risk).", re.compile(r"""(?:f['"]|`)\s*(?:SELECT|INSERT|UPDATE|DELETE)\b[^'"`]*\{""", re.I)),
        ("WARN", "SSP-06", "Unsafe deserialization via pickle.loads or yaml.load without SafeLoader.", re.compile(r"(?:\bpickle\.loads\s*\(|\byaml\.load\s*\([^,)]+\))")),
        ("WARN", "SSP-06", "Raw HTML injection sink (dangerouslySetInnerHTML); verify strict sanitizer.", re.compile(r"\bdangerouslySetInnerHTML\b")),
    ]

    for rel_posix, fpath in rel_map.items():
        if fpath.suffix.lower() not in CODE_EXTENSIONS or _is_test_or_scanner_self_file(rel_posix):
            continue
        if fpath.stat().st_size > 1_000_000:
            continue
        text = fpath.read_text(encoding="utf-8", errors="ignore")
        for sev, ctrl, msg, pat in sink_checks:
            if pat.search(text):
                findings[3].append({"severity": sev, "control": ctrl, "message": msg, "location": rel_posix})

    # --- Layer 4: Data, Multi-Tenant RLS & Redacted Logs (SSP-04, SSP-10, SSP-11) ---
    log_secret_pat = re.compile(
        r"\b(?:logger|logging|console)\.(?:info|debug|log|warn|warning|error)\s*\([^)]*\b(?:password|passwd|api_key|client_secret|access_token|private_key)\s*[+,)\]}]",
        re.I,
    )
    for rel_posix, fpath in rel_map.items():
        if _is_test_or_scanner_self_file(rel_posix) or fpath.stat().st_size > 1_000_000:
            continue
        if fpath.suffix.lower() == ".sql":
            sql_text = fpath.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"\btenant_id\b", sql_text, re.I) and not re.search(r"ROW\s+LEVEL\s+SECURITY", sql_text, re.I):
                findings[4].append({
                    "severity": "WARN",
                    "control": "SSP-04",
                    "message": "Multi-tenant column 'tenant_id' found in SQL without 'ROW LEVEL SECURITY' declaration.",
                    "location": rel_posix,
                })
        elif fpath.suffix.lower() in CODE_EXTENSIONS:
            text = fpath.read_text(encoding="utf-8", errors="ignore")
            if log_secret_pat.search(text):
                findings[4].append({
                    "severity": "WARN",
                    "control": "SSP-11",
                    "message": "Potential credential/secret variable passed directly to logger output.",
                    "location": rel_posix,
                })

    # --- Layer 5: Infrastructure, Network & Containers (SSP-08) ---
    public_db_port_pat = re.compile(r"""['"]?(?:0\.0\.0\.0:)?(5432|3306|6379|27017|9200):\1['"]?""")
    for rel_posix, fpath in rel_map.items():
        lower_name = fpath.name.lower()
        if lower_name == "dockerfile" or lower_name.startswith("dockerfile."):
            dtext = fpath.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"^\s*FROM\s+\S+:latest\b", dtext, re.M | re.I):
                findings[5].append({
                    "severity": "WARN",
                    "control": "SSP-08",
                    "message": "Dockerfile uses mutable ':latest' base image tag; pin version and/or SHA-256 digest.",
                    "location": rel_posix,
                })
            if not re.search(r"^\s*USER\s+(?!root\b)\S+", dtext, re.M | re.I):
                findings[5].append({
                    "severity": "WARN",
                    "control": "SSP-08",
                    "message": "Dockerfile has no non-root USER instruction; container defaults to root.",
                    "location": rel_posix,
                })
        elif lower_name in {"docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml"}:
            ctext = fpath.read_text(encoding="utf-8", errors="ignore")
            for line in ctext.splitlines():
                if "127.0.0.1:" in line:
                    continue
                if public_db_port_pat.search(line):
                    findings[5].append({
                        "severity": "BLOCKER",
                        "control": "SSP-08",
                        "message": "Database/cache port published on 0.0.0.0 in Compose (bypasses host firewall); bind to 127.0.0.1.",
                        "location": rel_posix,
                    })
                    break

    # --- Layer 6: Supply Chain, Lockfiles & CI Pinning (SSP-07) ---
    if (target_dir / "package.json").exists():
        if not any((target_dir / lf).exists() for lf in ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb", "bun.lock")):
            findings[6].append({
                "severity": "WARN",
                "control": "SSP-07",
                "message": "package.json present without deterministic lockfile (package-lock.json / pnpm-lock.yaml / yarn.lock).",
                "location": "package.json",
            })
    if (target_dir / "Cargo.toml").exists() and not (target_dir / "Cargo.lock").exists():
        findings[6].append({
            "severity": "WARN",
            "control": "SSP-07",
            "message": "Cargo.toml present without Cargo.lock.",
            "location": "Cargo.toml",
        })
    if (target_dir / "go.mod").exists() and not (target_dir / "go.sum").exists():
        findings[6].append({
            "severity": "WARN",
            "control": "SSP-07",
            "message": "go.mod present without go.sum checksum database.",
            "location": "go.mod",
        })
    if (target_dir / "requirements.txt").exists():
        req_lines = [
            ln.strip() for ln in (target_dir / "requirements.txt").read_text(encoding="utf-8", errors="ignore").splitlines()
            if ln.strip() and not ln.strip().startswith(("#", "-"))
        ]
        unpinned = [ln for ln in req_lines if "==" not in ln and "@" not in ln]
        if unpinned:
            findings[6].append({
                "severity": "WARN",
                "control": "SSP-07",
                "message": f"requirements.txt has {len(unpinned)} unpinned dependency specifier(s) without '=='.",
                "location": "requirements.txt",
            })

    for rel_posix, fpath in rel_map.items():
        if rel_posix.startswith(".github/workflows/") and fpath.suffix.lower() in {".yml", ".yaml"}:
            wtext = fpath.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"uses:\s*[^@\s]+@(?:main|master|HEAD)\b", wtext):
                findings[6].append({
                    "severity": "WARN",
                    "control": "SSP-07",
                    "message": "GitHub Actions workflow references mutable '@main' or '@master' branch instead of tag/commit SHA.",
                    "location": rel_posix,
                })

    # --- Layer 7: Agentic AI, MCP Containment & Release Gate (SSP-09, SSP-12, SSP-13) ---
    mcp_files = [
        rel for rel in rel_map
        if pathlib.Path(rel).name.lower() in {"mcp.json", "claude_desktop_config.json", ".mcp.json"}
    ]
    has_agent_manifest = (
        (target_dir / ".ssp" / "AI_AGENT_MANIFEST.json").exists()
        or (target_dir / "AI_AGENT_MANIFEST.json").exists()
        or (target_dir / "templates" / "AI_AGENT_MANIFEST.json").exists()
    )
    for mcp_rel in mcp_files:
        mtext = rel_map[mcp_rel].read_text(encoding="utf-8", errors="ignore")
        if re.search(r'"(?:API_KEY|TOKEN|SECRET|PASSWORD)"\s*:\s*"(?![$\{<])[^"]{8,}"', mtext, re.I):
            findings[7].append({
                "severity": "BLOCKER",
                "control": "SSP-09",
                "message": "Plaintext credential literal inside MCP configuration file.",
                "location": mcp_rel,
            })
        if not has_agent_manifest:
            findings[7].append({
                "severity": "WARN",
                "control": "SSP-09",
                "message": "MCP server config detected without AI_AGENT_MANIFEST.json capability & kill-switch contract.",
                "location": mcp_rel,
            })

    head_sha = _get_git_head_sha(target_dir)
    ssp_evidence = target_dir / ".ssp" / "evidence.json"
    if ssp_evidence.exists():
        try:
            ev_data = json.loads(ssp_evidence.read_text(encoding="utf-8"))
            ev_sha = ev_data.get("candidate", {}).get("commit_sha", "")
            if head_sha != "UNCOMMITTED_WORKSPACE" and ev_sha and ev_sha != head_sha:
                findings[7].append({
                    "severity": "WARN",
                    "control": "SSP-12",
                    "message": f".ssp/evidence.json commit_sha ({ev_sha[:8]}) lags behind current HEAD ({head_sha[:8]}).",
                    "location": ".ssp/evidence.json",
                })
        except Exception:
            findings[7].append({
                "severity": "BLOCKER",
                "control": "SSP-12",
                "message": "Invalid JSON in .ssp/evidence.json.",
                "location": ".ssp/evidence.json",
            })

    layer_summaries = []
    total_blockers = 0
    total_warns = 0
    for layer_meta in SEVEN_LAYERS:
        lid = layer_meta["layer"]
        l_findings = findings[lid]
        b_cnt = sum(1 for f in l_findings if f["severity"] == "BLOCKER")
        w_cnt = sum(1 for f in l_findings if f["severity"] == "WARN")
        total_blockers += b_cnt
        total_warns += w_cnt
        status = "BLOCKER" if b_cnt > 0 else ("WARN" if w_cnt > 0 else "PASS")
        layer_summaries.append({
            "layer": lid,
            "controls": layer_meta["controls"],
            "title_pt": layer_meta["title_pt"],
            "title_en": layer_meta["title_en"],
            "status": status,
            "blockers": b_cnt,
            "warnings": w_cnt,
            "findings": l_findings,
        })

    return {
        "protocol_version": SSP_PROTOCOL_VERSION,
        "community_edition": COMMUNITY_EDITION_VERSION,
        "target": str(target_dir),
        "head_commit_sha": head_sha,
        "scanned_files": len(files),
        "detected_stacks": stacks,
        "total_blockers": total_blockers,
        "total_warnings": total_warns,
        "automated_baseline_status": "BLOCKED" if total_blockers > 0 else ("REVIEW_WARNINGS" if total_warns > 0 else "CLEAN_BASELINE"),
        "governance_notice": (
            "Automated scan checks deterministic configuration and secret hygiene only. "
            "Full SSP-12 READY decision requires fresh architectural, negative-test, and operational evidence."
        ),
        "layers": layer_summaries,
    }


# ============================================================================
# CLI COMMAND HANDLERS
# ============================================================================

def cmd_validate(args) -> int:
    print("================================================================================")
    print(f" Sovereign Security Protocol (SSP v{SSP_PROTOCOL_VERSION} · Community Edition {COMMUNITY_EDITION_VERSION})")
    print(" Repository Integrity & Cryptographic Provenance Validator")
    print("================================================================================")

    all_ok = True

    # 0. Canonical PT-BR SHA-256 verification
    canon_errs = verify_canonical_protocol_integrity(REPO_ROOT)
    print("[*] Canonical PT-BR source SHA-256 verification (6,678 lines / 96,328 LF bytes):")
    if canon_errs:
        all_ok = False
        for err in canon_errs:
            print(f"    [FAIL] {err}")
    else:
        print(f"    [PASS] Byte-for-byte match verified ({CANONICAL_PT_SHA256_LF[:16]}...).")

    # 1. Links & SVG/HTML assets
    num_md, num_links, link_errs = check_markdown_links(REPO_ROOT)
    print(f"[*] Markdown & asset link verification: {num_md} files scanned, {num_links} local refs checked.")
    if link_errs:
        all_ok = False
        print(f"    [FAIL] {len(link_errs)} broken link(s):")
        for err in link_errs:
            print(f"      - {err}")
    else:
        print("    [PASS] All relative markdown links and visual SVG assets resolve.")

    # 2. Canvas
    num_nodes, canvas_errs = check_canvas_nodes(REPO_ROOT)
    print(f"[*] Obsidian Canvas verification: {num_nodes} nodes inspected.")
    if canvas_errs:
        all_ok = False
        for err in canvas_errs:
            print(f"    [FAIL] {err}")
    else:
        print("    [PASS] All Canvas file nodes and edges resolve on disk.")

    # 3. Crosswalk
    num_ctrls, cross_errs = check_crosswalk(REPO_ROOT)
    print(f"[*] Control Crosswalk verification: {num_ctrls} controls evaluated.")
    if cross_errs:
        all_ok = False
        for err in cross_errs:
            print(f"    [FAIL] {err}")
    else:
        print("    [PASS] Crosswalk schema and canonical protocol mappings verified.")

    # 4. JSON controls
    num_json_ctrls, json_errs = check_controls_json(REPO_ROOT)
    print(f"[*] Machine-readable JSON specification: {num_json_ctrls} controls checked.")
    if json_errs:
        all_ok = False
        for err in json_errs:
            print(f"    [FAIL] {err}")
    else:
        print("    [PASS] JSON specification adheres to schema rules.")

    # 5. Bilingual Parity
    _, parity_errs = check_bilingual_parity(REPO_ROOT)
    print(f"[*] Bilingual PT-BR <-> EN parity check: {len(BILINGUAL_DOC_PAIRS)} document pairs + root READMEs.")
    if parity_errs:
        all_ok = False
        for err in parity_errs:
            print(f"    [FAIL] {err}")
    else:
        print("    [PASS] Bilingual documentation parity verified.")

    print("================================================================================")
    if all_ok:
        print("[RESULT] VERIFICATION PASSED: Repository integrity validated (Fail-Closed OK).")
        return 0
    print("[RESULT] VERIFICATION FAILED: Fail-closed state triggered.")
    return 1


def cmd_parity(args) -> int:
    print("================================================================================")
    print(" SSP Bilingual Documentation Parity Check (PT-BR <-> EN)")
    print("================================================================================")
    report, errors = check_bilingual_parity(REPO_ROOT)
    for pt_name, en_name, ok in report:
        status = "OK" if ok else "MISSING"
        print(f"  [{status:7}] docs/pt-BR/{pt_name:<34} <---> docs/en/{en_name}")
    if errors:
        print(f"\n[FAIL] {len(errors)} parity issue(s) detected:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\n[PASS] Complete PT-BR <-> EN documentation parity verified.")
    return 0


def cmd_matrix(args) -> int:
    json_path = REPO_ROOT / "protocol" / "v13.4" / "ssp-controls.json"
    if not json_path.exists():
        print("Missing protocol/v13.4/ssp-controls.json")
        return 1

    data = json.loads(json_path.read_text(encoding="utf-8"))
    controls = data.get("controls", [])
    lang = getattr(args, "lang", "pt")

    print(f"\nSOVEREIGN SECURITY PROTOCOL v{data.get('protocol_version')} (Community Edition {COMMUNITY_EDITION_VERSION})")
    header_name = "Control Name (EN)" if lang == "en" else "Nome do Controle (PT-BR)"
    print(f"{'ID':<8} | {'Min Lvl':<7} | {header_name:<44} | {'Source Sections':<22}")
    print("-" * 90)
    for c in controls:
        cname = c["name_en"] if lang == "en" else c["name_pt"]
        print(f"{c['id']:<8} | {c['minimum_evidence_level']:<7} | {cname[:44]:<44} | {c['source_sections'][:22]:<22}")
    print("-" * 90)
    return 0


def cmd_blueprint(args) -> int:
    lang = getattr(args, "lang", "pt")
    selected = getattr(args, "layer", "all")

    print("================================================================================")
    if lang == "en":
        print(" SSP v13.4 — Universal 7-Layer Defense-in-Depth Blueprint (Any System)")
    else:
        print(" SSP v13.4 — Arquitetura Universal de 7 Camadas de Defesa em Profundidade")
    print("================================================================================")

    for item in SEVEN_LAYERS:
        if selected != "all" and str(item["layer"]) != str(selected):
            continue
        title = item["title_en"] if lang == "en" else item["title_pt"]
        goal = item["goal_en"] if lang == "en" else item["goal_pt"]
        ctrls = ", ".join(item["controls"])
        label = "LAYER" if lang == "en" else "CAMADA"
        print(f"\n[{label} {item['layer']}] {title}")
        print(f"  Controls : {ctrls}")
        print(f"  Action   : {goal}")

    print("\n" + "=" * 80)
    if lang == "en":
        print("Full code examples: docs/en/layers-by-system.md | Bootstrap: python ssp.py init --target <dir>")
    else:
        print("Exemplos de código: docs/pt-BR/camadas-por-sistema.md | Instalar: python ssp.py init --target <dir>")
    return 0


def cmd_scan(args) -> int:
    target = pathlib.Path(args.target).resolve()
    if not target.exists() or not target.is_dir():
        print(f"[ERROR] Target directory does not exist: {target}")
        return 1

    result = scan_target_system(target)
    lang = getattr(args, "lang", "pt")

    if getattr(args, "output", None):
        out_path = pathlib.Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if getattr(args, "format", "text") == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("================================================================================")
        print(f" SSP v{SSP_PROTOCOL_VERSION} — 7-Layer Defense-in-Depth Baseline Scanner")
        print(f" Target        : {result['target']}")
        print(f" Commit SHA    : {result['head_commit_sha']}")
        print(f" Files Scanned : {result['scanned_files']} | Stacks: {', '.join(result['detected_stacks'])}")
        print("================================================================================")

        for lyr in result["layers"]:
            title = lyr["title_en"] if lang == "en" else lyr["title_pt"]
            badge = f"[{lyr['status']:7}]"
            ctrls = ",".join(lyr["controls"])
            print(f"{badge} L{lyr['layer']} ({ctrls:<20}) {title}")
            for f in lyr["findings"]:
                print(f"           -> ({f['severity']}) [{f['control']}] {f['location']}: {f['message']}")

        print("-" * 80)
        print(
            f"Summary: {result['total_blockers']} BLOCKER(s) | {result['total_warnings']} WARNING(s) | "
            f"Baseline: {result['automated_baseline_status']}"
        )
        if lang == "en":
            print("Note   : Automated heuristics do not replace threat modeling, AuthZ negative tests, or SSP-12 gate evidence.")
        else:
            print("Nota   : Heurísticas automáticas não substituem modelagem de ameaças, testes negativos de AuthZ ou o gate SSP-12.")
        print("================================================================================")

    if result["total_blockers"] > 0:
        return 2
    if getattr(args, "strict", False) and result["total_warnings"] > 0:
        return 1
    return 0


def cmd_init(args) -> int:
    target = pathlib.Path(args.target).resolve()
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)

    profile_key = args.profile
    profile = PROFILES[profile_key]
    lang = getattr(args, "lang", "pt")
    force = getattr(args, "force", False)

    ssp_dir = target / ".ssp"
    ssp_dir.mkdir(parents=True, exist_ok=True)

    head_sha = _get_git_head_sha(target)
    now_iso = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    json_spec_path = REPO_ROOT / "protocol" / "v13.4" / "ssp-controls.json"
    controls_spec = json.loads(json_spec_path.read_text(encoding="utf-8"))["controls"]

    created_files: List[str] = []

    # 1. .ssp/config.json
    cfg_path = ssp_dir / "config.json"
    if not cfg_path.exists() or force:
        cfg_payload = {
            "ssp_base_version": SSP_PROTOCOL_VERSION,
            "community_edition": COMMUNITY_EDITION_VERSION,
            "profile": profile_key,
            "profile_description": profile["description_en"] if lang == "en" else profile["description_pt"],
            "priority_controls": profile["priority_controls"],
            "initialized_at": now_iso,
            "fail_closed": True,
            "freshness_invalidation_triggers": [
                "auth_or_rbac_change",
                "database_schema_or_rls_change",
                "network_or_container_exposure_change",
                "dependency_lockfile_change",
                "agent_tool_or_mcp_policy_change",
            ],
        }
        cfg_path.write_text(json.dumps(cfg_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        created_files.append(str(cfg_path.relative_to(target)))

    # 2. .ssp/evidence.json (Fail-closed: initialized to UNKNOWN, bound to live git SHA)
    ev_path = ssp_dir / "evidence.json"
    if not ev_path.exists() or force:
        ctrl_results = {}
        for c in controls_spec:
            cid = c["id"]
            ctrl_results[cid] = {
                "status": "UNKNOWN",
                "minimum_level": c["minimum_evidence_level"],
                "priority": cid in profile["priority_controls"],
                "method": "",
                "evidence": "",
                "reason": "Pending project-specific verification and evidence binding.",
            }
        ev_payload = {
            "protocol_version": SSP_PROTOCOL_VERSION,
            "community_edition": COMMUNITY_EDITION_VERSION,
            "profile": profile_key,
            "candidate": {
                "repository": target.name,
                "commit_sha": head_sha,
                "artifact_digest": "sha256:PENDING_BUILD_ARTIFACT",
                "environment": "production-candidate",
            },
            "evaluator": "ASSIGN_OWNER@domain.tld",
            "evaluated_at": now_iso,
            "control_results": ctrl_results,
        }
        ev_path.write_text(json.dumps(ev_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        created_files.append(str(ev_path.relative_to(target)))

    # 3. .ssp/SECURITY_LAYERS_CHECKLIST.md
    chk_path = ssp_dir / "SECURITY_LAYERS_CHECKLIST.md"
    if not chk_path.exists() or force:
        lines = [
            f"# SSP v{SSP_PROTOCOL_VERSION} — Security Layers Checklist (`{profile_key}`)",
            "",
            f"- **Initialized:** `{now_iso}`",
            f"- **Candidate Commit SHA:** `{head_sha}`",
            f"- **Profile:** {profile['description_en'] if lang == 'en' else profile['description_pt']}",
            "",
            "> **Fail-Closed Rule:** Every applicable control starts as `UNKNOWN` in `.ssp/evidence.json`. Move to `PASS` only after binding direct test/review evidence to the current commit SHA.",
            "",
        ]
        for item in SEVEN_LAYERS:
            t = item["title_en"] if lang == "en" else item["title_pt"]
            g = item["goal_en"] if lang == "en" else item["goal_pt"]
            lines.append(f"## Layer {item['layer']} — {t}")
            lines.append(f"*{g}*")
            lines.append("")
            for cid in item["controls"]:
                c_meta = next(x for x in controls_spec if x["id"] == cid)
                cname = c_meta["name_en"] if lang == "en" else c_meta["name_pt"]
                prio = " **(PRIORITY)**" if cid in profile["priority_controls"] else ""
                lines.append(f"- [ ] **{cid}** ({c_meta['minimum_evidence_level']}): {cname}{prio} — *{c_meta['evidence_focus']}*")
            lines.append("")
        chk_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        created_files.append(str(chk_path.relative_to(target)))

    # 4. Optional AI Agent Manifest for ai-agent-mcp profile
    if profile_key == "ai-agent-mcp":
        manifest_src = REPO_ROOT / "templates" / "AI_AGENT_MANIFEST.json"
        manifest_dst = ssp_dir / "AI_AGENT_MANIFEST.json"
        if manifest_src.exists() and (not manifest_dst.exists() or force):
            manifest_dst.write_text(manifest_src.read_text(encoding="utf-8"), encoding="utf-8")
            created_files.append(str(manifest_dst.relative_to(target)))

    # 5. Optional GitHub Actions workflow
    if getattr(args, "ci", False):
        wf_path = target / ".github" / "workflows" / "ssp-security-gate.yml"
        if not wf_path.exists() or force:
            wf_path.parent.mkdir(parents=True, exist_ok=True)
            wf_content = (
                "name: SSP Security Layers Gate\n\n"
                "on:\n"
                "  push:\n"
                "    branches: [main, master]\n"
                "  pull_request:\n\n"
                "permissions:\n"
                "  contents: read\n\n"
                "jobs:\n"
                "  ssp-7-layer-scan:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - uses: actions/checkout@v4\n"
                "      - name: Run Sovereign Security Protocol 7-Layer Baseline Scan\n"
                "        uses: robertoatila/sovereign-security-protocol@main\n"
                "        with:\n"
                "          mode: scan\n"
                "          target: .\n"
            )
            wf_path.write_text(wf_content, encoding="utf-8")
            created_files.append(str(wf_path.relative_to(target)))

    print("================================================================================")
    print(f" SSP v{SSP_PROTOCOL_VERSION} Initialized Successfully in: {target}")
    print(f" Profile : {profile_key} ({profile['description_en'] if lang == 'en' else profile['description_pt']})")
    print(" Created : " + (", ".join(created_files) if created_files else "(files already existed; use --force to overwrite)"))
    print(" Next    :")
    print(f"   1. python ssp.py scan --target \"{target}\"")
    print(f"   2. Fill verifiable evidence in \"{ssp_dir / 'evidence.json'}\"")
    print(f"   3. python ssp.py gate --file \"{ssp_dir / 'evidence.json'}\"")
    print("================================================================================")
    return 0


def cmd_gate(args) -> int:
    evidence_path = pathlib.Path(args.file)
    if not evidence_path.exists():
        print(f"[ERROR] Evidence file not found: {evidence_path}")
        return 1

    try:
        record = json.loads(evidence_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[ERROR] Failed to parse evidence JSON: {exc}")
        return 1

    candidate = record.get("candidate", {})
    results = record.get("control_results", {})
    cand_sha = str(candidate.get("commit_sha", "UNKNOWN")).strip()

    expected_sha = getattr(args, "expected_sha", None)
    if not expected_sha and getattr(args, "target", None):
        live = _get_git_head_sha(pathlib.Path(args.target))
        if live != "UNCOMMITTED_WORKSPACE":
            expected_sha = live

    print("================================================================================")
    print(" SSP-12 Quadruple Release Assurance Gate Evaluation")
    print(f" Candidate Commit : {cand_sha}")
    print(f" Artifact Digest  : {candidate.get('artifact_digest', 'UNKNOWN')}")
    print(f" Evaluator        : {record.get('evaluator', 'UNKNOWN')}")
    print("================================================================================")

    blockers: List[Tuple[str, str, str]] = []
    accepted_risks: List[Tuple[str, str, str]] = []
    not_applicable: List[str] = []
    passed: List[str] = []

    if expected_sha and cand_sha != expected_sha:
        blockers.append((
            "SSP-12",
            "STALE_EVIDENCE",
            f"Evidence commit_sha ({cand_sha}) does not match expected commit ({expected_sha}).",
        ))

    json_path = REPO_ROOT / "protocol" / "v13.4" / "ssp-controls.json"
    spec = json.loads(json_path.read_text(encoding="utf-8"))
    ctrl_map = {c["id"]: c for c in spec["controls"]}

    today_str = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")

    for cid, spec_ctrl in ctrl_map.items():
        res = results.get(cid, {})
        status = res.get("status", "UNKNOWN")

        if status == "PASS":
            if not res.get("evidence") and not res.get("method"):
                blockers.append((cid, "UNVERIFIED_PASS", "PASS declared without 'method' or 'evidence' reference."))
            else:
                passed.append(cid)
        elif status == "N/A":
            if not res.get("rationale"):
                blockers.append((cid, "INVALID_NA", "N/A requires explicit scope 'rationale'."))
            else:
                not_applicable.append(cid)
        elif status == "ACCEPTED RISK":
            exc_ref = res.get("exception_ref", "")
            owner = res.get("owner", "")
            comp = res.get("compensating_control", "")
            expires = res.get("expires_at", "")
            if not (exc_ref and owner and comp and expires):
                blockers.append((
                    cid,
                    "UNGOVERNED_RISK",
                    "ACCEPTED RISK requires 'exception_ref', 'owner', 'compensating_control', and 'expires_at'.",
                ))
            elif expires < today_str:
                blockers.append((
                    cid,
                    "EXPIRED_EXCEPTION",
                    f"Exception {exc_ref} expired on {expires} (today: {today_str}).",
                ))
            else:
                accepted_risks.append((cid, exc_ref, expires))
        else:
            blockers.append((cid, status, res.get("reason", "Control not satisfied or unassessed.")))

    print(
        f"Controls: {len(ctrl_map)} | PASS: {len(passed)} | N/A: {len(not_applicable)} | "
        f"ACCEPTED RISK: {len(accepted_risks)} | BLOCKERS: {len(blockers)}"
    )
    print("-" * 80)

    if blockers:
        print("DECISION: NOT READY (Release Blocked — Fail-Closed)")
        for cid, st, r in blockers:
            cname = ctrl_map.get(cid, {}).get("name_en", cid)
            print(f"  - [{st}] {cid} ({cname}): {r}")
        return 2
    if accepted_risks:
        print("DECISION: READY WITH ACCEPTED RISK")
        for cid, ref, exp in accepted_risks:
            print(f"  - [ACCEPTED RISK] {cid}: Governed under {ref} (expires {exp})")
        return 0

    print("DECISION: READY (All Applicable Controls Verified)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ssp.py",
        description="Sovereign Security Protocol (SSP v13.4) — Universal 7-Layer Security CLI Engine",
    )
    parser.add_argument("--version", action="version", version=f"SSP v{SSP_PROTOCOL_VERSION} (Community Edition {COMMUNITY_EDITION_VERSION})")
    parser.add_argument("--doctor", action="store_true", help="Run full self-diagnostic of SSP repository & runtime")

    subparsers = parser.add_subparsers(dest="command")

    # init
    sub_init = subparsers.add_parser("init", help="Bootstrap SSP 7-Layer security scaffolding (.ssp/) in any project")
    sub_init.add_argument("--target", "-t", default=".", help="Target project directory (default: current dir)")
    sub_init.add_argument("--profile", "-p", choices=list(PROFILES.keys()), default="web-api", help="System security profile")
    sub_init.add_argument("--ci", action="store_true", help="Also generate .github/workflows/ssp-security-gate.yml")
    sub_init.add_argument("--lang", choices=["pt", "en"], default="pt", help="Checklist language (pt or en)")
    sub_init.add_argument("--force", action="store_true", help="Overwrite existing .ssp/ template files")
    sub_init.set_defaults(func=cmd_init)

    # scan
    sub_scan = subparsers.add_parser("scan", help="Run 7-Layer Defense-in-Depth baseline audit on any codebase")
    sub_scan.add_argument("--target", "-t", default=".", help="Target project directory to scan")
    sub_scan.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    sub_scan.add_argument("--output", "-o", help="Optional path to save JSON scan receipt")
    sub_scan.add_argument("--lang", choices=["pt", "en"], default="pt", help="Output language (pt or en)")
    sub_scan.add_argument("--strict", action="store_true", help="Return non-zero exit code on WARNINGS as well as BLOCKERS")
    sub_scan.set_defaults(func=cmd_scan)

    # blueprint
    sub_bp = subparsers.add_parser("blueprint", help="Display the 7 Universal Security Layers & controls")
    sub_bp.add_argument("--layer", "-l", default="all", help="Layer number (1-7) or 'all'")
    sub_bp.add_argument("--lang", choices=["pt", "en"], default="pt", help="Language (pt or en)")
    sub_bp.set_defaults(func=cmd_blueprint)

    # gate
    sub_gate = subparsers.add_parser("gate", help="Evaluate SSP-12 Release Assurance Gate on an evidence JSON file")
    sub_gate.add_argument("--file", "-f", required=True, help="Path to evidence record JSON")
    sub_gate.add_argument("--expected-sha", help="Expected git commit SHA for freshness enforcement")
    sub_gate.add_argument("--target", "-t", help="Optional target git repo directory to compare live HEAD SHA")
    sub_gate.set_defaults(func=cmd_gate)

    # validate
    sub_val = subparsers.add_parser("validate", help="Validate SSP repository integrity, SHA-256, links, canvas & schemas")
    sub_val.set_defaults(func=cmd_validate)

    # check-parity
    sub_par = subparsers.add_parser("check-parity", help="Verify PT-BR and EN documentation parity")
    sub_par.set_defaults(func=cmd_parity)

    # matrix
    sub_mat = subparsers.add_parser("matrix", help="Display 13 controls summary matrix")
    sub_mat.add_argument("--lang", choices=["pt", "en"], default="pt", help="Language (pt or en)")
    sub_mat.set_defaults(func=cmd_matrix)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "doctor", False):
        return cmd_validate(args)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
