import random

print("Think of a number between 1 and 100, and I'll try to guess it!")
print("I have 3 attempts to guess your number.")

low = 1
high = 100
attempts = 3

for attempt in range(1, attempts + 1):
    guess = random.randint(low, high)
    print(f"Attempt {attempt}: Is your number {guess}?")
    response = input("Type 'high' if my guess is too high, 'low' if it's too low, or 'correct' if I got it: ").lower()

    if response == "correct":
        print("Yay! I guessed your number!")
        break
    elif response == "high":
        high = guess - 1
    elif response == "low":
        low = guess + 1
    else:
        print("Invalid input. Please respond with 'high', 'low', or 'correct'.")

    if attempt == attempts:
        print("I'm out of attempts! Better luck next time!")
