"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

import sys


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5 / 9


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C = {result:.2f}°F")
        elif unit == "F":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F = {result:.2f}°C")
        else:
            print("Invalid unit! Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid input! Please enter a numeric temperature value.")


if __name__ == "__main__":
    # Only run interactively when launched manually
    if sys.stdin.isatty():
        temperature_converter()
