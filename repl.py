from decimal import Decimal, InvalidOperation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def get_number(prompt: str) -> Decimal:
    """
    Prompt the user for a number and return it as a Decimal.
    """
    while True:
        try:
            return Decimal(input(prompt))
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")

def display_history():
    """
    Display the calculation history.
    """
    history = Calculations.get_history()
    if not history:
        print("No history available.")
        return

    # Map operation names to symbols
    operation_symbols = {
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/"
    }

    print("\nCalculation History:")
    for i, calc in enumerate(history, 1):
        try:
            result = calc.perform()
            symbol = operation_symbols.get(calc.operation.__name__, "?")
            print(f"{i}. {calc.a} {symbol} {calc.b} = {result}")
        except ValueError as e:
            print(f"{i}. {calc.a} {calc.operation.__name__} {calc.b} = Error: {e}")

def display_menu():
    """
    Display the main menu options.
    """
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")

def start_repl():
    """
    Start the REPL (Read-Eval-Print Loop) for the calculator.
    """
    print("Welcome to the Calculator REPL. Choose an operation from the menu.")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            # Add
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            result = add(a, b)
            print(f"The result of {a} + {b} is: {result}")
            Calculations.add_calculation(Calculation.create(a, b, add))

        elif choice == "2":
            # Subtract
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            result = subtract(a, b)
            print(f"The result of {a} - {b} is: {result}")
            Calculations.add_calculation(Calculation.create(a, b, subtract))

        elif choice == "3":
            # Multiply
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            result = multiply(a, b)
            print(f"The result of {a} * {b} is: {result}")
            Calculations.add_calculation(Calculation.create(a, b, multiply))

        elif choice == "4":
            # Divide
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            try:
                result = divide(a, b)
                print(f"The result of {a} / {b} is: {result}")
                Calculations.add_calculation(Calculation.create(a, b, divide))
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            # View History
            display_history()

        elif choice == "6":
            # Clear History
            Calculations.clear_history()
            print("Calculation history cleared.")

        elif choice == "7":
            # Exit
            print("Exiting REPL. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    start_repl()