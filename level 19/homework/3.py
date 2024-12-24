# nimeri 3
numbers = []

for i in range(10):
    number = int(input(f"შეიყვანეთ რიცხვი ({i+1}/10): "))
    numbers.append(number)

delete_number = int(input("შეიყვანეთ რიცხვი, რომელიც უნდა წაშალოთ სიიდან: "))

if delete_number in numbers:
    numbers.remove(delete_number)
    print(f"რიცხვი {delete_number} წაშლილია სიიდან.")
else:
    print(f"რიცხვი {delete_number} სიაში არ არის.")

print("განახლებული სია:", numbers)
