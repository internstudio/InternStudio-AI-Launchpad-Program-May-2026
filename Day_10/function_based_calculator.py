# Function-Based Calculator
# This script defines separate functions for basic arithmetic operations and provides a simple
# menu-driven calculator. It also handles division by zero and includes optional power and
# modulus operations as a bonus.

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

# Bonus operations
def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def modulus(a, b):
    """Return the modulus of a divided by b. Handles division by zero."""
    if b == 0:
        return "Error: Modulus by zero is undefined."
    return a % b


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Please enter valid numeric values.")


def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
        "5": ("Power (Bonus)", power),
        "6": ("Modulus (Bonus)", modulus),
    }

    while True:
        print("\n--- Function-Based Calculator ---")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("7. Exit")
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid selection. Please try again.")
            continue

        a, b = get_numbers()
        op_name, func = operations[choice]
        result = func(a, b)
        print(f"Result of {op_name.lower()}: {result}")

if __name__ == "__main__":
    main()
