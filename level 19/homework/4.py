#nimeri 4
numbers = []

for i in range(10):
    number = int(input(f"შეიყვანეთ რიცხვი ({i+1}/10): "))
    numbers.append(number)


reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])

print("სია საპირისპირო წესით:", reversed_numbers)
