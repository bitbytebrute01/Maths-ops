#!/usr/bin/env python3
"""
Simple Calculator for Basic Math Operations
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter 1-5.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"\n{num1} × {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"\n{num1} ÷ {num2} = {result}")
        
        except ValueError:
            print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
