#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_tests.py — Sovereign Security Protocol Executable Test Runner
Discovers and executes all deterministic verification suites under tests/.
"""

import pathlib
import sys
import time
import unittest

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REPO_ROOT = pathlib.Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def main() -> int:
    start = time.perf_counter()
    print("================================================================================")
    print(" Sovereign Security Protocol (SSP v13.4) — Master Executable Test Battery")
    print("================================================================================")

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(REPO_ROOT / "tests"), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    elapsed = time.perf_counter() - start
    print("================================================================================")
    print(
        f" Executed: {result.testsRun} tests in {elapsed:.2f}s | "
        f"Failures: {len(result.failures)} | Errors: {len(result.errors)}"
    )
    print("================================================================================")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
