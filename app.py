#!/usr/bin/env python3
"""
Simple Python application for CI/CD demo
"""


def greet(name="World"):
    """
    Returns a greeting message
    
    Args:
        name (str): Name to greet
        
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"


def add_numbers(a, b):
    """
    Adds two numbers together
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of the two numbers
    """
    return a + b


def main():
    """
    Main function to demonstrate the application
    """
    print("=" * 50)
    print("CI/CD Demo Application")
    print("=" * 50)
    
    # Greeting example
    message = greet("DevOps Team")
    print(f"\n{message}")
    
    # Addition example
    num1, num2 = 10, 20
    result = add_numbers(num1, num2)
    print(f"\nAddition example: {num1} + {num2} = {result}")
    
    print("\n" + "=" * 50)
    print("Application executed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
