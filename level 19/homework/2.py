#nomeri 2
numbers = []

for i in range(10):
    number = int(input(f"შეიყვანეთ რიცხვი ({i+1}/10): "))
    numbers.append(number)

max_number = numbers[0]  
for num in numbers:
    if num > max_number:
        max_number = num

print("უდიდესი რიცხვი არის:", max_number)
