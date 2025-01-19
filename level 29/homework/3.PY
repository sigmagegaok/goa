#homework 3
numbers = list(range(1, 11))

first_half = numbers[:5]

second_half = numbers[5:]

squares = [num ** 2 for num in numbers]

print("First half of numbers:", first_half)
print("Second half of numbers:", second_half)
print("Squares of numbers:", squares)
