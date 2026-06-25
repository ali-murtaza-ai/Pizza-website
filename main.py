# ============================================================
#  Calculator  —  Arithmetic  +  2 Scientific Features
#  Basic:      +  -  x  /
#  Scientific: Factorial (n!), Absolute Value (|n|)
# ============================================================

import math

# ── Basic Arithmetic ────────────────────────────────────────
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# ── Scientific Features ──────────────────────────────────────
def factorial(a):
    """Return a! — only valid for non-negative integers."""
    if a < 0 or a != int(a):
        raise ValueError("Factorial is only defined for non-negative integers!")
    return math.factorial(int(a))

def absolute(a):
    """Return |a| — the absolute (non-negative) value of a."""
    return abs(a)

# ── Helpers ──────────────────────────────────────────────────
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.\n")

def fmt(n):
    """Show whole numbers without decimal point."""
    if n == int(n):
        return int(n)
    return round(n, 10)

# ── Menu ─────────────────────────────────────────────────────
def show_menu():
    print("\n" + "=" * 44)
    print("            CALCULATOR v2.0")
    print("=" * 44)
    print("  --- Basic Arithmetic ---")
    print("  [1]  Addition          (a + b)")
    print("  [2]  Subtraction       (a - b)")
    print("  [3]  Multiplication    (a x b)")
    print("  [4]  Division          (a / b)")
    print("  --- Scientific ---")
    print("  [5]  Factorial         (n!)")
    print("  [6]  Absolute Value    (|n|)")
    print("  [0]  Exit")
    print("-" * 44)

# ── Main ─────────────────────────────────────────────────────
def main():
    print("\n  Welcome to Calculator v2.0!")

    while True:
        show_menu()
        choice = input("  Select (0-6): ").strip()

        if choice == "0":
            print("\n  Goodbye!\n")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("  [!] Invalid choice. Enter a number between 0 and 6.")
            continue

        print()
        try:
            # Two-operand operations
            if choice in ("1", "2", "3", "4"):
                a = get_number("  Enter first  number: ")
                b = get_number("  Enter second number: ")
                if   choice == "1": result, expr = add(a, b),      f"{fmt(a)} + {fmt(b)}"
                elif choice == "2": result, expr = subtract(a, b), f"{fmt(a)} - {fmt(b)}"
                elif choice == "3": result, expr = multiply(a, b), f"{fmt(a)} x {fmt(b)}"
                elif choice == "4": result, expr = divide(a, b),   f"{fmt(a)} / {fmt(b)}"
                print(f"\n  [=]  {expr} = {fmt(result)}")

            # Single-operand scientific operations
            elif choice == "5":
                a = get_number("  Enter a non-negative integer: ")
                result = factorial(a)
                print(f"\n  [=]  {fmt(a)}! = {fmt(result)}")

            elif choice == "6":
                a = get_number("  Enter number: ")
                result = absolute(a)
                print(f"\n  [=]  |{fmt(a)}| = {fmt(result)}")

        except ValueError as e:
            print(f"\n  [!]  {e}")

if __name__ == "__main__":
    main()
