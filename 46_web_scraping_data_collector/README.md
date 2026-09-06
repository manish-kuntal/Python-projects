# 46_web_scraping_data_collector

Collect structured data from a public HTML table by CSS selector and save as CSV. Use responsibly and check site policies.

Usage:
- pip install -r requirements.txt
- python scraper.py "https://example.com/page" "table.stats" out.csv

Improvement suggestion:
- Add robots.txt check and rate limiting/backoff between requests.
