"""
A simple calculator module for basic arithmetic operations.
"""

def subtract(num1: float, num2: float) -> float:
    """Return the result of subtraction: num1 - num2."""
    return num1 - num2

def add(num1: float, num2: float) -> float:
    """Return the result of addition: num1 + num2."""
    return num1 + num2

def multiply(num1: float, num2: float) -> float:
    """Return the result of multiplication: num1 * num2."""
    return num1 * num2

def divide(num1: float, num2: float):
    """Return the result of division: num1 / num2. Raises error if num2 is zero."""
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2


def main():
    """Demonstrate calculator functions with example values."""
    num1 = 10
    num2 = 5

    print("Subtraction:", subtract(num1, num2))
    print("Addition:", add(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))


if __name__ == "__main__":
    main()
