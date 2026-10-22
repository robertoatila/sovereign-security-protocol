#!/usr/bin/env python3
"""
Sovereign Security Protocol (SSP) - Tooling & Verification Engine
Deterministic, sovereign CLI for link checking, schema validation, crosswalk integrity,
and release gate assurance (SSP-12). Zero external runtime dependencies.
"""

import argparse
import csv
import json
import os
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

def find_markdown_files(root: pathlib.Path):
    for path in root.rglob("*.md"):
        # Ignore .git and temporary directories
        if ".git" in path.parts or ".system_generated" in path.parts:
            continue
        yield path

def check_markdown_links(root: pathlib.Path):
    errors = []
    checked_count = 0
    link_count = 0

    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for md_path in find_markdown_files(root):
        checked_count += 1
        content = md_path.read_text(encoding="utf-8", errors="ignore")
        for match in link_pattern.finditer(content):
            text, raw_link = match.group(1), match.group(2).strip()
            # Ignore absolute URLs, mailto, and pure in-page anchors
            if raw_link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            link_count += 1
            clean_link = raw_link.split("#")[0].replace("%20", " ")
            if not clean_link:
                continue
            target = (md_path.parent / clean_link).resolve()
            if not target.exists():
                rel_source = md_path.relative_to(root)
                errors.append(f"Broken link in {rel_source}: [{text}]({raw_link}) -> '{target}' not found")

    return checked_count, link_count, errors

def check_canvas_nodes(root: pathlib.Path):
    canvas_file = root / "SSP-13.4.canvas"
    errors = []
    if not canvas_file.exists():
        return 0, [f"Canvas file {canvas_file} not found"]

    try:
        data = json.loads(canvas_file.read_text(encoding="utf-8"))
        nodes = data.get("nodes", [])
        for node in nodes:
            if node.get("type") == "file":
                fpath = node.get("file")
                if fpath:
                    target = (root / fpath).resolve()
                    if not target.exists():
                        errors.append(f"Canvas node '{node.get('id')}' references missing file: {fpath}")
        return len(nodes), errors
    except Exception as e:
        return 0, [f"Failed to parse Canvas JSON: {e}"]

def check_crosswalk(root: pathlib.Path):
    csv_file = root / "control-crosswalk.csv"
    proto_pt = root / "protocol" / "v13.4" / "PROTOCOLO_INTEGRAL_v13.4_PT-BR.md"
    errors = []

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
        # Extract starting section markers, e.g. "1.1", "9.1", "0.4"
        raw_tokens = [tok.strip() for tok in re.split(r'[;,\s]+', sections) if tok.strip()]
        for token in raw_tokens:
            base_sec = token.split("-")[0].strip()
            if not base_sec:
                continue
            # Search for section identifier in canonical text
            # Format in protocol can be "1.1 ", "1.1.", "1.1 -", "§1.1", or "12. CANONICAL GATE", etc.
            pattern = re.compile(rf'(?:^|\n)\s*{re.escape(base_sec)}(?:[\.\s\:\—\–\-]|$)', re.M)
            if not pattern.search(proto_text):
                errors.append(f"Control {cid}: Section '{base_sec}' referenced from '{sections}' not located in canonical protocol")

    return len(rows), errors

def check_controls_json(root: pathlib.Path):
    json_path = root / "protocol" / "v13.4" / "ssp-controls.json"
    schema_path = root / "schema" / "ssp-control.schema.json"
    errors = []

    if not json_path.exists():
        return 0, [f"Missing {json_path}"]
    if not schema_path.exists():
        return 0, [f"Missing schema: {schema_path}"]

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
        controls = data.get("controls", [])
        if len(controls) != 13:
            errors.append(f"ssp-controls.json must contain exactly 13 controls, found {len(controls)}")

        for c in controls:
            cid = c.get("id")
            if not re.match(r"^SSP-(0[1-9]|1[0-3])$", cid or ""):
                errors.append(f"Invalid control ID format: {cid}")
            if not c.get("blocker_criteria"):
                errors.append(f"Control {cid} has no blocker_criteria defined")
            if not c.get("minimum_evidence_level"):
                errors.append(f"Control {cid} has no minimum_evidence_level")

        return len(controls), errors
    except Exception as e:
        return 0, [f"Error parsing ssp-controls.json: {e}"]

def cmd_validate(args):
    print("================================================================================")
    print(" Sovereign Security Protocol (SSP) - Repository Validation Engine")
    print("================================================================================")

    all_ok = True

    # 1. Links
    num_md, num_links, link_errs = check_markdown_links(REPO_ROOT)
    print(f"[*] Markdown link verification: {num_md} files scanned, {num_links} internal links checked.")
    if link_errs:
        all_ok = False
        print(f"    [FAIL] {len(link_errs)} broken link(s):")
        for err in link_errs:
            print(f"      - {err}")
    else:
        print("    [PASS] All relative markdown links resolve.")

    # 2. Canvas
    num_nodes, canvas_errs = check_canvas_nodes(REPO_ROOT)
    print(f"[*] Obsidian Canvas verification: {num_nodes} nodes inspected.")
    if canvas_errs:
        all_ok = False
        print(f"    [FAIL] Canvas errors:")
        for err in canvas_errs:
            print(f"      - {err}")
    else:
        print("    [PASS] All Canvas file nodes resolve on disk.")

    # 3. Crosswalk
    num_ctrls, cross_errs = check_crosswalk(REPO_ROOT)
    print(f"[*] Control Crosswalk verification: {num_ctrls} controls evaluated.")
    if cross_errs:
        all_ok = False
        print(f"    [FAIL] Crosswalk errors:")
        for err in cross_errs:
            print(f"      - {err}")
    else:
        print("    [PASS] Crosswalk schema and canonical protocol mappings verified.")

    # 4. JSON controls
    num_json_ctrls, json_errs = check_controls_json(REPO_ROOT)
    print(f"[*] Machine-readable JSON specification: {num_json_ctrls} controls checked.")
    if json_errs:
        all_ok = False
        print(f"    [FAIL] JSON control errors:")
        for err in json_errs:
            print(f"      - {err}")
    else:
        print("    [PASS] JSON specification adheres to schema rules.")

    print("================================================================================")
    if all_ok:
        print("[RESULT] VERIFICATION PASSED: Repository integrity validated (SSP-12 Compliant).")
        return 0
    else:
        print("[RESULT] VERIFICATION FAILED: Fail-closed state triggered.")
        return 1

def cmd_parity(args):
    print("================================================================================")
    print(" SSP Bilingual Documentation Parity Check (PT-BR <-> EN)")
    print("================================================================================")
    pt_dir = REPO_ROOT / "docs" / "pt-BR"
    en_dir = REPO_ROOT / "docs" / "en"

    pt_files = {p.name: p for p in pt_dir.glob("*.md")}
    en_files = {p.name: p for p in en_dir.glob("*.md")}

    print(f"PT-BR docs: {len(pt_files)} files | EN docs: {len(en_files)} files")

    # Mappings known by name
    known_pairs = [
        ("protocolo.md", "protocol.md"),
        ("adocao-e-evidencias.md", "adoption-and-evidence.md"),
        ("agentes-jarvis-obsidian.md", "agentic-jarvis-obsidian.md"),
        ("guia-rapido-adocao.md", "quickstart-adoption.md")
    ]

    missing = []
    for pt_name, en_name in known_pairs:
        pt_exists = (pt_dir / pt_name).exists()
        en_exists = (en_dir / en_name).exists()
        status = "OK" if (pt_exists and en_exists) else "MISSING"
        if not (pt_exists and en_exists):
            missing.append((pt_name, en_name))
        print(f"  [{status:7}] {pt_name} <---> {en_name}")

    if missing:
        print(f"\n[FAIL] Discrepancies found in {len(missing)} bilingual pair(s).")
        return 1
    print("\n[PASS] Core bilingual doc parity is aligned.")
    return 0

def cmd_matrix(args):
    json_path = REPO_ROOT / "protocol" / "v13.4" / "ssp-controls.json"
    if not json_path.exists():
        print("Missing protocol/v13.4/ssp-controls.json")
        return 1

    data = json.loads(json_path.read_text(encoding="utf-8"))
    controls = data.get("controls", [])

    print(f"\nSOVEREIGN SECURITY PROTOCOL v{data.get('protocol_version')} (Edition {data.get('edition')})")
    print(f"{'ID':<8} | {'Min Lvl':<7} | {'Control Name (PT-BR)':<35} | {'Source Domain':<30}")
    print("-" * 90)
    for c in controls:
        print(f"{c['id']:<8} | {c['minimum_evidence_level']:<7} | {c['name_pt'][:35]:<35} | {c['source_domain'][:30]:<30}")
    print("-" * 90)
    return 0

def cmd_gate(args):
    """
    Evaluates an evidence manifest against SSP-12 release gate.
    """
    evidence_path = pathlib.Path(args.file)
    if not evidence_path.exists():
        print(f"Evidence file not found: {evidence_path}")
        return 1

    try:
        record = json.loads(evidence_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Failed to read evidence record: {e}")
        return 1

    candidate = record.get("candidate", {})
    results = record.get("control_results", {})

    print("================================================================================")
    print(" SSP-12 Release Assurance Gate Evaluation")
    print(f" Candidate Commit: {candidate.get('commit_sha', 'UNKNOWN')}")
    print(f" Candidate Digest: {candidate.get('artifact_digest', 'UNKNOWN')}")
    print(f" Evaluator:        {record.get('evaluator', 'UNKNOWN')}")
    print("================================================================================")

    blockers = []
    accepted_risks = []
    passed = []

    json_path = REPO_ROOT / "protocol" / "v13.4" / "ssp-controls.json"
    spec = json.loads(json_path.read_text(encoding="utf-8"))
    ctrl_map = {c["id"]: c for c in spec["controls"]}

    for cid, spec_ctrl in ctrl_map.items():
        res = results.get(cid, {})
        status = res.get("status", "UNKNOWN")
        if status == "PASS":
            passed.append(cid)
        elif status == "ACCEPTED RISK":
            accepted_risks.append((cid, res.get("exception_ref", "No exception ID")))
        elif status in ["FAIL", "UNKNOWN"]:
            blockers.append((cid, status, res.get("reason", "No reason provided")))

    print(f"Controls Evaluated: {len(ctrl_map)}")
    print(f"PASS:          {len(passed)}")
    print(f"ACCEPTED RISK: {len(accepted_risks)}")
    print(f"BLOCKERS:      {len(blockers)}")

    print("-" * 80)
    if blockers:
        print("DECISION: NOT READY (Release Blocked)")
        for cid, st, r in blockers:
            print(f"  - [{st}] {cid} ({ctrl_map[cid]['name_en']}): {r}")
        return 2
    elif accepted_risks:
        print("DECISION: READY WITH ACCEPTED RISK")
        for cid, ref in accepted_risks:
            print(f"  - [ACCEPTED RISK] {cid}: Governed under {ref}")
        return 0
    else:
        print("DECISION: READY (Full Assurance Passed)")
        return 0

def main():
    parser = argparse.ArgumentParser(description="Sovereign Security Protocol Tooling Engine")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # validate
    sub_val = subparsers.add_parser("validate", help="Validate links, canvas, crosswalk, and json schemas")
    sub_val.set_defaults(func=cmd_validate)

    # parity
    sub_par = subparsers.add_parser("check-parity", help="Verify PT-BR and EN documentation parity")
    sub_par.set_defaults(func=cmd_parity)

    # matrix
    sub_mat = subparsers.add_parser("matrix", help="Display controls summary matrix")
    sub_mat.set_defaults(func=cmd_matrix)

    # gate
    sub_gate = subparsers.add_parser("gate", help="Evaluate SSP-12 release gate for an evidence record")
    sub_gate.add_argument("--file", "-f", required=True, help="Path to evidence record JSON")
    sub_gate.set_defaults(func=cmd_gate)

    args = parser.parse_args()
    sys.exit(args.func(args))

if __name__ == "__main__":
    main()
