# хз какой день; +76 задача; всего: 76

i = input()
numbers = [int(i[0]), int(i[1]), int(i[2])]
sorted(numbers)
if max(numbers) - min(numbers) == (sum(numbers) - max(numbers) - min(numbers)):
    print('Число интересное')
else:
    print('Число неинтересное')
