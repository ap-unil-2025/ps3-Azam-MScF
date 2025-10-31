"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def temperature_converter():
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
    # Exécuter uniquement quand lancé manuellement
    if sys.stdin.isatty():
        temperature_converter()

