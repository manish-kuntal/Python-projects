#!/usr/bin/env python3
"""
Multithreaded File Downloader
Download multiple URLs concurrently with retries and basic progress.
"""

import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests


def download(url, dest_folder, timeout=15, retries=2):
    dest_folder = Path(dest_folder)
    dest_folder.mkdir(parents=True, exist_ok=True)
    local = dest_folder / Path(url).name
    attempt = 0
    while attempt <= retries:
        try:
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()
            local.write_bytes(r.content)
            return local
        except Exception as e:
            attempt += 1
            last_err = e
    raise last_err


def main():
    if len(sys.argv) < 3:
        print('Usage: python downloader.py dest_folder url1 url2 ...')
        sys.exit(2)
    dest = sys.argv[1]
    urls = sys.argv[2:]
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {ex.submit(download, u, dest): u for u in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                path = fut.result()
                print('Downloaded', url, '->', path)
            except Exception as e:
                print('Failed', url, e)

if __name__ == '__main__':
    main()
