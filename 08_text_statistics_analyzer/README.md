# 08_text_statistics_analyzer

Analyze text for basic statistics: characters, words, sentences, average word length, and most common words.

Usage:
- From file: python stats.py -f document.txt
- From stdin: cat document.txt | python stats.py

Project architecture:
- `stats.py` exposes `analyze_text` which returns a dictionary of metrics.

Python concepts used:
- Regular expressions, collections.Counter, file and stdin handling.

Possible improvement:
- Provide an option to exclude stopwords when computing most common words.
