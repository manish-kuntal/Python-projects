#!/usr/bin/env python3
"""
Command Line Assistant
A tiny modular CLI assistant that can call some local utilities (notes, tasks, calculator).
It executes the corresponding script in the repo using the Python interpreter.
"""

import argparse
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent
SCRIPTS = {
    'calc': '01_smart_calculator/calculator.py',
    'notes': '15_notes_manager/notes.py',
    'tasks': '41_cli_task_management_system/task_manager.py',
}


def run_tool(name, args):
    script = SCRIPTS.get(name)
    if not script:
        print('Unknown tool:', name)
        return
    path = BASE / script
    if not path.exists():
        print('Script not found:', path)
        return
    cmd = [sys.executable, str(path)] + args
    subprocess.run(cmd)


def main():
    p = argparse.ArgumentParser(description='Command Line Assistant')
    p.add_argument('tool', choices=SCRIPTS.keys())
    p.add_argument('args', nargs='*')
    args = p.parse_args()
    run_tool(args.tool, args.args)

if __name__ == '__main__':
    main()
