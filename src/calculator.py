# calculator/calculations.py

def add(a, b):
    """Compute and return the sum of two numbers.

    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a, b):
    """Compute and return the difference of two numbers.

    Args:
        a (float): A number representing the first number in the subtraction.
        b (float): A number representing the second number in the subtraction.

    Returns:
        float: A number representing the arithmetic difference of `a` and `b`.
    """
    return float(a - b)

def multiply(a, b):
    """Compute and return the multiplication of two numbers.

    Args:
        a (float): A number representing the first number in the multiplication.
        b (float): A number representing the second number in the multiplication.

    Returns:
        float: A number representing the arithmetic multiplication of `a` and `b`.
    """
    return float(a * b)

def divide(a, b):
    """Compute and return the division of two numbers.

    Args:
        a (float): A number representing the first number in the division.
        b (float): A number representing the second number in the division.

    Returns:
        float: A number representing the arithmetic division of `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)