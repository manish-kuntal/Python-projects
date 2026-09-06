# 01_smart_calculator

Simple CLI Smart Calculator.

Features:
- Addition, subtraction, multiplication, division, modulus.
- Evaluate simple arithmetic expressions safely (uses ast).
- Input validation and basic error handling (including division by zero).
- No external dependencies; works with Python 3.8+.

How to run:
1. Open a terminal.
2. Run: python calculator.py
3. Follow the menu prompts.

Example usage:
- Choose option 1, enter 4 and 5 -> Result: 9
- Choose option 6, enter expression: 3*(2+5)/7 -> Result: 3

Project architecture:
- Single script `calculator.py`.
- `safe_eval(expr)` — safely parses and evaluates arithmetic expressions using the `ast` module.
- `get_number(prompt)` — robust user numeric input helper.
- `perform_operation(op_name)` — collects operands and performs operations with validation.
- `main()` — menu-driven CLI loop.

Python concepts used:
- Standard library: ast, operator, sys
- Function decomposition and mapping
- Exception handling (ValueError, ZeroDivisionError)
- Input validation and simple CLI I/O
- Recursion when evaluating AST nodes

How to run the project:
- Ensure Python 3.8+ is installed.
- From the folder, run: python calculator.py
- Use the menu to perform operations.

Possible improvements (one small task you can try):
- Add a history feature that stores the last N operations and allows the user to view them.
- Add unit tests for `safe_eval` to cover supported and unsupported expressions.
