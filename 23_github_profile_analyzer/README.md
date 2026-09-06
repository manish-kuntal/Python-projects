# 23_github_profile_analyzer

Retrieve public GitHub profile info and list top repositories by stars.

Usage:
- pip install -r requirements.txt
- python analyzer.py username [github_token]

Notes:
- Without a token, GitHub API is rate-limited to 60 requests/hour per IP.

Possible improvement:
- Add per-repo analysis (issues, languages breakdown) and cache results.
