# Simple calculator program

# Take input from the user
num1 = 10
num2 = 5

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
product = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {product}")
print(f"Division: {division}")