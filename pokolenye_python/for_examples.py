numbers = [8, 9, 10, 11]

del numbers[1]  # 1
numbers.insert(1, 17)
numbers = numbers + [4, 5, 6]  # 2
del numbers[0]  # 3
numbers = numbers * 2  # 4
numbers.insert(3, 25)  # 5

print(numbers)  # 6
