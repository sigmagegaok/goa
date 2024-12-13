user_numbers = []


print("Enter numbers one by one (press Enter on an empty line to finish):")
while True:
    user_input = input()  
    if user_input == "":  
        break
    try:
        number = float(user_input) 
        user_numbers.append(number)
    except ValueError:
        print("Please enter a valid number or press Enter to finish.")


if any(num > 10 for num in user_numbers):
    print("There is a number greater than 10 in the list.")
else:
    print("There is no number greater than 10 in the list.")


print("Created list:", user_numbers)
print("Sum of the list elements:", sum(user_numbers))