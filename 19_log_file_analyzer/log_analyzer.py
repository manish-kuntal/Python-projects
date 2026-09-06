#!/usr/bin/env python3
"""
Log File Analyzer
Parse a log file and summarize counts of ERROR/WARNING/INFO and show recent errors.
Assumes lines contain common level keywords.
"""

import sys
from collections import Counter, deque
from pathlib import Path
import re

LEVELS = ['ERROR', 'WARNING', 'WARN', 'INFO', 'DEBUG']
LEVEL_RE = re.compile(r'\b(ERROR|WARNING|WARN|INFO|DEBUG)\b')


def analyze(path: Path, recent=10):
    if not path.exists():
        print('File not found')
        return
    counts = Counter()
    recent_errors = deque(maxlen=recent)
    with path.open(encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = LEVEL_RE.search(line)
            if m:
                lvl = m.group(1)
                counts[lvl] += 1
                if lvl == 'ERROR':
                    recent_errors.append(line.strip())
    print('Log level counts:')
    for lvl in LEVELS:
        if counts[lvl]:
            print(f' {lvl}: {counts[lvl]}')
    if recent_errors:
        print('\nRecent errors:')
        for e in recent_errors:
            print(' -', e)


def main():
    if len(sys.argv) < 2:
        print('Usage: python log_analyzer.py path/to/log [recent_count]')
        sys.exit(2)
    recent = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    analyze(Path(sys.argv[1]), recent=recent)


if __name__ == '__main__':
    main()
