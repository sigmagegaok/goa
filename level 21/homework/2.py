
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]


numbers.append(100)
numbers.insert(0, 5)
numbers.remove(30)
numbers.reverse()


index_of_50 = numbers.index(50)
count_of_20 = numbers.count(20)


print("Updated list:", numbers)
print("Index of 50:", index_of_50)
print("Count of 20:", count_of_20)