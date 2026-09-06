# 06_unit_converter

A small unit conversion CLI supporting temperature, length, weight, and time.

Usage examples:
- Temperature: python unit_converter.py temp 100 C F
- Length: python unit_converter.py length 5 km m
- Weight: python unit_converter.py weight 2 lb kg
- Time: python unit_converter.py time 90 min h

Project architecture:
- Single script `unit_converter.py`.
- Conversion functions normalize to a base unit then convert to target.

Main functions:
- convert_temperature, convert_length, convert_weight, convert_time

Python concepts used:
- argparse, dictionaries for unit maps, error handling.

Possible improvement:
- Add more units and friendly unit synonyms (e.g., 'meters', 'kilograms').
