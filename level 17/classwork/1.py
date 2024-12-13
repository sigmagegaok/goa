
my_list = [42, "Python", 3.14, True, None, [1, 2, 3], (4, 5), {'key': 'value'}, {1, 2, 3}, b"bytes"]


print("First element:", my_list[0])
print("Second element:", my_list[1])
print("Third element:", my_list[2])


my_list[3] = "Java"
my_list[4] = "C++"
my_list[5] = "JavaScript"


new_values = ["Ruby", 99, 3.14159, False, (10, 20)]
my_list.extend(new_values)
print("Updated list:", my_list)
print("First element:", my_list[0])
print("Second element:", my_list[1])
print("Third element:", my_list[2])

my_list[3] = "Java"
my_list[4] = "C++"
my_list[5] = "JavaScript"

new_values = ["Ruby", 99, 3.14159, False, (10, 20)]
my_list.extend(new_values)

print("Updated list:", my_list)