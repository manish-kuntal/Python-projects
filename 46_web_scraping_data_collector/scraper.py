#!/usr/bin/env python3
"""
Web Scraping Data Collector
Scrape a table or list from a public page and save selected data as CSV. Use responsibly and obey robots.txt.
"""

import sys
import csv
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except Exception:
    print('Install: pip install requests beautifulsoup4')
    sys.exit(1)

HEADERS = {'User-Agent': 'python-projects-scraper/1.0'}


def fetch_table(url, selector, out):
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.select_one(selector)
    if table.name != 'table':
        raise ValueError('Selector did not select a table')
    rows = []
    for tr in table.find_all('tr'):
        cols = [td.get_text(strip=True) for td in tr.find_all(['td','th'])]
        if cols:
            rows.append(cols)
    if not rows:
        raise ValueError('No rows found')
    Path(out).write_text('\n'.join([','.join(r) for r in rows]), encoding='utf-8')
    print('Wrote', len(rows), 'rows to', out)


def main():
    if len(sys.argv) < 4:
        print('Usage: python scraper.py <url> <css_table_selector> <out_csv>')
        sys.exit(2)
    url = sys.argv[1]
    selector = sys.argv[2]
    out = sys.argv[3]
    fetch_table(url, selector, out)

if __name__ == '__main__':
    main()
