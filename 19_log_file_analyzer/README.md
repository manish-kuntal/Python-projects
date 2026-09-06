# 19_log_file_analyzer

Analyze a plain text log file to count common log levels (ERROR/WARNING/INFO) and show recent error lines.

Usage:
- python log_analyzer.py /var/log/myapp.log
- python log_analyzer.py my.log 20  (show 20 recent errors)

Improvement suggestion:
- Add parsing for timestamped logs and aggregate errors over time windows.
