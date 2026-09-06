#!/usr/bin/env python3
"""
Simple CLI Smart Calculator
Supports: addition, subtraction, multiplication, division, modulus
Also supports evaluating simple arithmetic expressions safely.
"""

import ast
import operator
import sys

# Allowed binary operators mapping
_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

# Allowed unary operators
_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def safe_eval(expr: str) -> float:
    """
    Safely evaluate a simple arithmetic expression using ast.
    Supports numbers, binary ops (+, -, *, /, %, **), and unary +/-
    Raises ValueError for unsupported expressions.
    """
    try:
        node = ast.parse(expr, mode="eval").body
    except SyntaxError as e:
        raise ValueError(f"Invalid expression: {e}")

    def _eval(node):
        if isinstance(node, ast.Constant):  # Python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numeric constants allowed")
        if isinstance(node, ast.Num):  # older ast compatibility
            return node.n
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in _BIN_OPS:
                raise ValueError(f"Operator {op_type.__name__} not supported")
            left = _eval(node.left)
            right = _eval(node.right)
            func = _BIN_OPS[op_type]
            try:
                return func(left, right)
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero")
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in _UNARY_OPS:
                raise ValueError(f"Unary operator {op_type.__name__} not supported")
            operand = _eval(node.operand)
            return _UNARY_OPS[op_type](operand)
        # Reject names, calls, attributes, etc.
        raise ValueError(f"Unsupported expression element: {type(node).__name__}")

    return _eval(node)


def get_number(prompt: str) -> float:
    """Prompt the user until a valid number is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def perform_operation(op_name: str):
    """Ask for operands and perform the requested operation."""
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    try:
        if op_name == "add":
            result = a + b
        elif op_name == "sub":
            result = a - b
        elif op_name == "mul":
            result = a * b
        elif op_name == "div":
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            result = a / b
        elif op_name == "mod":
            if b == 0:
                raise ZeroDivisionError("Modulus by zero")
            result = a % b
        else:
            raise ValueError("Unknown operation")
    except ZeroDivisionError as e:
        print("Error:", e)
        return

    # Display integer result without .0 when appropriate
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print("Result:", result)


def main():
    menu = """
Smart Calculator
Choose an option:
 1) Add
 2) Subtract
 3) Multiply
 4) Divide
 5) Modulus
 6) Evaluate expression (e.g. 3*(2+5)/4)
 0) Exit
"""
    while True:
        print(menu)
        choice = input("Select an option: ").strip()
        if choice == "1":
            perform_operation("add")
        elif choice == "2":
            perform_operation("sub")
        elif choice == "3":
            perform_operation("mul")
        elif choice == "4":
            perform_operation("div")
        elif choice == "5":
            perform_operation("mod")
        elif choice == "6":
            expr = input("Enter arithmetic expression: ").strip()
            try:
                result = safe_eval(expr)
            except ZeroDivisionError:
                print("Error: Division by zero")
                continue
            except ValueError as e:
                print("Error:", e)
                continue
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print("Result:", result)
        elif choice == "0":
            print("Goodbye.")
            return
        else:
            print("Invalid option. Please choose 0-6.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        sys.exit(0)
