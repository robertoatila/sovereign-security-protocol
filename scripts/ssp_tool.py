#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/ssp_tool.py — Backward-compatible CLI wrapper around root ssp.py engine.
"""

import pathlib
import sys

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from ssp import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
