# ============================================================
#  Simple Arithmetic Calculator
#  Operations: Addition, Subtraction, Multiplication, Division
# ============================================================

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises an error on division by zero."""
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b

def get_number(prompt):
    """Prompt the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value.\n")

def show_menu():
    """Display the operations menu."""
    print("\n" + "=" * 40)
    print("       SIMPLE ARITHMETIC CALCULATOR")
    print("=" * 40)
    print("  1.  Addition        ( + )")
    print("  2.  Subtraction     ( - )")
    print("  3.  Multiplication  ( × )")
    print("  4.  Division        ( ÷ )")
    print("  0.  Exit")
    print("-" * 40)

def main():
    print("\nWelcome to the Simple Calculator!")

    while True:
        show_menu()
        choice = input("  Select an operation (0-4): ").strip()

        if choice == "0":
            print("\n  Goodbye! 👋\n")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  ⚠  Invalid choice. Please select a number between 0 and 4.")
            continue

        # Get two numbers from the user
        print()
        a = get_number("  Enter first  number: ")
        b = get_number("  Enter second number: ")

        # Perform the chosen operation
        try:
            if choice == "1":
                result = add(a, b)
                symbol = "+"
            elif choice == "2":
                result = subtract(a, b)
                symbol = "-"
            elif choice == "3":
                result = multiply(a, b)
                symbol = "×"
            elif choice == "4":
                result = divide(a, b)
                symbol = "÷"

            # Format result: show as int if it's a whole number
            formatted = int(result) if result == int(result) else round(result, 10)
            print(f"\n  ✅  {a} {symbol} {b} = {formatted}")

        except ValueError as e:
            print(f"\n  ❌  {e}")

if __name__ == "__main__":
    main()
