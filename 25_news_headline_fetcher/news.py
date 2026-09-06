#!/usr/bin/env python3
"""
News Headline Fetcher
Fetch headlines from an RSS feed (BBC top stories) and display titles.
No API key required.
"""

import sys
import xml.etree.ElementTree as ET

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)

RSS_BBC = 'http://feeds.bbci.co.uk/news/rss.xml'


def fetch_titles(rss_url=RSS_BBC, limit=10):
    r = requests.get(rss_url, timeout=10)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    titles = []
    for item in root.findall('.//item'):
        title = item.find('title')
        if title is not None:
            titles.append(title.text)
        if len(titles) >= limit:
            break
    return titles


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    try:
        titles = fetch_titles(limit=limit)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    for i, t in enumerate(titles, start=1):
        print(f"{i}. {t}")


if __name__ == '__main__':
    main()
