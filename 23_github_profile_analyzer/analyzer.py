#!/usr/bin/env python3
"""
GitHub Profile Analyzer
Fetches public profile and repo stats for a GitHub username.
No auth: rate-limited — use a token for higher limits.
"""

import sys

try:
    import requests
except Exception:
    print('Install requests: pip install requests')
    sys.exit(1)

API_USER = 'https://api.github.com/users/'
API_REPOS = 'https://api.github.com/users/{user}/repos'


def get_user(user: str, token: str = None):
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'
    r = requests.get(API_USER + user, headers=headers)
    r.raise_for_status()
    return r.json()


def get_repos(user: str, token: str = None):
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'
    r = requests.get(API_REPOS.format(user=user), headers=headers, params={'per_page': 100})
    r.raise_for_status()
    return r.json()


def main():
    if len(sys.argv) < 2:
        print('Usage: python analyzer.py username [github_token]')
        sys.exit(2)
    user = sys.argv[1]
    token = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        profile = get_user(user, token)
        repos = get_repos(user, token)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    print('Name:', profile.get('name'))
    print('Public repos:', profile.get('public_repos'))
    print('Followers:', profile.get('followers'))
    print('\nTop repositories by stars:')
    sorted_repos = sorted(repos, key=lambda r: r.get('stargazers_count', 0), reverse=True)[:10]
    for r in sorted_repos:
        print(f" {r['name']}: ★{r.get('stargazers_count',0)} - {r.get('language')}")


if __name__ == '__main__':
    main()
