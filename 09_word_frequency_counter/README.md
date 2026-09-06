# 09_word_frequency_counter

Count word frequencies in a text source (file or stdin) and show the top N words.

Usage:
- python freq_counter.py -f document.txt
- cat document.txt | python freq_counter.py -n 20

Project architecture:
- Single script `freq_counter.py` with `count_words` main helper.

Python concepts used:
- Regular expressions, Counter, stdin/file reading.

Possible improvement:
- Add options to normalize (remove punctuation) or ignore stopwords.
