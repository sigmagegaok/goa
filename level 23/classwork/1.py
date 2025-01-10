def calculate_operations(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    integer_division = x // y if y != 0 else "Division by zero error"
    
    print(f"Addition (+): {addition}")
    print(f"Subtraction (-): {subtraction}")
    print(f"Multiplication (*): {multiplication}")
    print(f"Integer Division (//): {integer_division}")

calculate_operations(10, 5)
