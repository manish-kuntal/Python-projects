#!/usr/bin/env python3
"""
System Resource Monitor
Show CPU, memory, and disk usage. Uses psutil when available, otherwise uses basic stdlib approximations.
"""

import shutil
import os
import sys

try:
    import psutil
except Exception:
    psutil = None


def main():
    if psutil:
        print('CPU percent:', psutil.cpu_percent(interval=1))
        mem = psutil.virtual_memory()
        print(f"Memory: {mem.percent}% ({mem.used//1024**2}MB/{mem.total//1024**2}MB)")
        disk = psutil.disk_usage('/')
        print(f"Disk: {disk.percent}% ({disk.used//1024**3}GB/{disk.total//1024**3}GB)")
    else:
        print('psutil not installed; showing basic info')
        # CPU approximation not available; show loadavg on Unix
        if hasattr(os, 'getloadavg'):
            loads = os.getloadavg()
            print('Load average (1,5,15 min):', loads)
        total, used, free = shutil.disk_usage('/')
        print(f"Disk: {(used/total)*100:.1f}% ({used//1024**3}GB/{total//1024**3}GB)")


if __name__ == '__main__':
    main()
