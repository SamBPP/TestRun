import math
from datetime import datetime

# hello.py

# 1. Importing modules

# 2. Defining a constant
PI = math.pi

# 3. Defining a function
def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

# 4. Using a class
class Calculator:
    """A simple calculator class."""
    
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# 5. Using a decorator
def log_time(func):
    """Logs the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"{func.__name__} executed in {end_time - start_time}")
        return result
    return wrapper

@log_time
def compute_circle_area(radius: float) -> float:
    """Computes the area of a circle given its radius."""
    return PI * radius ** 2

# 6. Using a generator
def fibonacci_sequence(n: int):
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 7. Main execution block
if __name__ == "__main__":
    # Greeting
    print(greet("World"))

    # Calculator usage
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")

    # Compute circle area
    print(f"Area of circle with radius 5: {compute_circle_area(5)}")

    # Fibonacci sequence
    print("First 10 Fibonacci numbers:")
    for num in fibonacci_sequence(10):
        print(num)