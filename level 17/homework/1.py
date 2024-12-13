
user_input = input("Enter numbers separated by commas (e.g., 1, 2, 3, 4): ")


try:
    numbers = [float(num.strip()) for num in user_input.split(",")]

    total = sum(numbers)

    print("The sum of the numbers is:", total)
except ValueError:
    print("Please enter a valid list of numbers separated by commas.")