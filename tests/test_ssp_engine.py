#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests/test_ssp_engine.py — Comprehensive Verification Suite for SSP v13.4 Engine
Tests canonical SHA-256 immutability, link & canvas integrity, bilingual parity,
7-layer universal target scanning (vulnerable vs hardened), init scaffolding,
and SSP-12 Release Assurance Gate enforcement.
"""

import json
import pathlib
import tempfile
import unittest

import ssp

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


class TestSSPRepositoryIntegrity(unittest.TestCase):
    def test_canonical_pt_protocol_sha256_immutable(self):
        errs = ssp.verify_canonical_protocol_integrity(REPO_ROOT)
        self.assertEqual(errs, [], f"Canonical PT-BR protocol was altered: {errs}")

    def test_markdown_and_svg_links_resolve(self):
        checked_md, checked_links, errs = ssp.check_markdown_links(REPO_ROOT)
        self.assertGreaterEqual(checked_md, 20)
        self.assertGreaterEqual(checked_links, 80)
        self.assertEqual(errs, [], f"Broken markdown/asset links found: {errs}")

    def test_obsidian_canvas_nodes_and_edges_valid(self):
        node_count, errs = ssp.check_canvas_nodes(REPO_ROOT)
        self.assertGreaterEqual(node_count, 15)
        self.assertEqual(errs, [], f"Canvas validation errors: {errs}")

    def test_crosswalk_resolves_against_canonical_source(self):
        ctrl_count, errs = ssp.check_crosswalk(REPO_ROOT)
        self.assertEqual(ctrl_count, 13)
        self.assertEqual(errs, [], f"Crosswalk errors: {errs}")

    def test_controls_json_matches_schema_invariants(self):
        ctrl_count, errs = ssp.check_controls_json(REPO_ROOT)
        self.assertEqual(ctrl_count, 13)
        self.assertEqual(errs, [], f"Controls JSON errors: {errs}")

    def test_bilingual_documentation_parity(self):
        report, errs = ssp.check_bilingual_parity(REPO_ROOT)
        self.assertEqual(len(report), len(ssp.BILINGUAL_DOC_PAIRS))
        self.assertEqual(errs, [], f"Bilingual parity discrepancies: {errs}")

    def test_self_repository_scan_has_zero_blockers(self):
        res = ssp.scan_target_system(REPO_ROOT)
        self.assertEqual(res["total_blockers"], 0, f"Self-scan had blockers: {res}")


class TestUniversalSystemApplication(unittest.TestCase):
    def test_init_scaffolds_fail_closed_unknown_state_and_ci(self):
        with tempfile.TemporaryDirectory() as tmp:
            tpath = pathlib.Path(tmp)
            rc = ssp.main(["init", "--target", str(tpath), "--profile", "ai-agent-mcp", "--ci", "--lang", "en"])
            self.assertEqual(rc, 0)

            cfg = json.loads((tpath / ".ssp" / "config.json").read_text(encoding="utf-8"))
            self.assertEqual(cfg["profile"], "ai-agent-mcp")
            self.assertTrue(cfg["fail_closed"])

            ev = json.loads((tpath / ".ssp" / "evidence.json").read_text(encoding="utf-8"))
            self.assertEqual(len(ev["control_results"]), 13)
            for cid, cstate in ev["control_results"].items():
                self.assertEqual(cstate["status"], "UNKNOWN", f"{cid} must start UNKNOWN (fail-closed)")

            self.assertTrue((tpath / ".ssp" / "AI_AGENT_MANIFEST.json").exists())
            self.assertTrue((tpath / ".ssp" / "SECURITY_LAYERS_CHECKLIST.md").exists())
            self.assertTrue((tpath / ".github" / "workflows" / "ssp-security-gate.yml").exists())

            # Gate MUST block immediately on freshly initialized UNKNOWN controls
            gate_rc = ssp.main(["gate", "--file", str(tpath / ".ssp" / "evidence.json")])
            self.assertEqual(gate_rc, 2)

    def test_scanner_catches_multi_layer_vulnerabilities(self):
        with tempfile.TemporaryDirectory() as tmp:
            tpath = pathlib.Path(tmp)
            # Layer 1: unignored .env + AWS key
            (tpath / ".env").write_text("DATABASE_URL=postgres://u:p@localhost/db\n", encoding="utf-8")
            fake_aws = "AKIA" + "1234567890ABCDEF"
            # Layer 2 & 3: fail-open REQUIRE_AUTH=false + SQL f-string interpolation
            (tpath / "app.py").write_text(
                f'KEY = "{fake_aws}"\n'
                'REQUIRE_AUTH = "false"\n'
                'def q(uid):\n'
                '    return f"SELECT * FROM users WHERE id = {uid}"\n',
                encoding="utf-8",
            )
            # Layer 5: Docker compose exposing Postgres on 0.0.0.0:5432
            (tpath / "docker-compose.yml").write_text(
                "services:\n  db:\n    image: postgres:latest\n    ports:\n      - '5432:5432'\n",
                encoding="utf-8",
            )
            # Layer 7: Plaintext token in mcp.json
            (tpath / "mcp.json").write_text(
                '{"mcpServers":{"demo":{"env":{"API_KEY":"supersecretliteral12345"}}}}',
                encoding="utf-8",
            )

            report = ssp.scan_target_system(tpath)
            self.assertGreaterEqual(report["total_blockers"], 4)
            self.assertEqual(report["automated_baseline_status"], "BLOCKED")
            layer_statuses = {lyr["layer"]: lyr["status"] for lyr in report["layers"]}
            self.assertEqual(layer_statuses[1], "BLOCKER")
            self.assertEqual(layer_statuses[2], "BLOCKER")
            self.assertEqual(layer_statuses[3], "BLOCKER")
            self.assertEqual(layer_statuses[5], "BLOCKER")
            self.assertEqual(layer_statuses[7], "BLOCKER")

    def test_scanner_passes_hardened_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            tpath = pathlib.Path(tmp)
            (tpath / ".gitignore").write_text(".env\n__pycache__/\n", encoding="utf-8")
            (tpath / "SECURITY.md").write_text("# Security Policy\nReport privately.\n", encoding="utf-8")
            (tpath / "requirements.txt").write_text("fastapi==0.115.0\nuvicorn==0.30.6\n", encoding="utf-8")
            (tpath / "Dockerfile").write_text(
                "FROM python:3.12.6-slim\nUSER appuser\nCMD [\"python\", \"main.py\"]\n",
                encoding="utf-8",
            )
            (tpath / "docker-compose.yml").write_text(
                "services:\n  db:\n    image: postgres:16.4-alpine\n    ports:\n      - '127.0.0.1:5432:5432'\n",
                encoding="utf-8",
            )
            (tpath / "main.py").write_text(
                "def get_item(db, item_id: str, tenant_id: str):\n"
                "    return db.execute('SELECT id FROM items WHERE id = ? AND tenant_id = ?', (item_id, tenant_id))\n",
                encoding="utf-8",
            )

            report = ssp.scan_target_system(tpath)
            self.assertEqual(report["total_blockers"], 0)
            self.assertEqual(report["total_warnings"], 0)
            self.assertEqual(report["automated_baseline_status"], "CLEAN_BASELINE")


class TestReleaseAssuranceGate(unittest.TestCase):
    def test_sample_evidence_record_passes_gate(self):
        sample = REPO_ROOT / "templates" / "sample_evidence_record.json"
        rc = ssp.main(["gate", "--file", str(sample)])
        self.assertEqual(rc, 0)

    def test_gate_blocks_stale_commit_sha(self):
        sample = REPO_ROOT / "templates" / "sample_evidence_record.json"
        rc = ssp.main(["gate", "--file", str(sample), "--expected-sha", "0000000000000000000000000000000000000000"])
        self.assertEqual(rc, 2)

    def test_gate_blocks_expired_exception_and_allows_valid_future_exception(self):
        sample_data = json.loads((REPO_ROOT / "templates" / "sample_evidence_record.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            ev_file = pathlib.Path(tmp) / "ev.json"

            # Expired exception -> MUST block
            sample_data["control_results"]["SSP-10"] = {
                "status": "ACCEPTED RISK",
                "exception_ref": "EXC-2020-001",
                "owner": "sec-lead@example.com",
                "compensating_control": "Read-only replica snapshot",
                "expires_at": "2020-01-01",
            }
            ev_file.write_text(json.dumps(sample_data), encoding="utf-8")
            self.assertEqual(ssp.main(["gate", "--file", str(ev_file)]), 2)

            # Future valid governed exception -> READY WITH ACCEPTED RISK (exit 0)
            sample_data["control_results"]["SSP-10"]["expires_at"] = "2099-12-31"
            ev_file.write_text(json.dumps(sample_data), encoding="utf-8")
            self.assertEqual(ssp.main(["gate", "--file", str(ev_file)]), 0)


if __name__ == "__main__":
    unittest.main()
