# 7 day; 4 задача; total: 123
numbers_list = []
while True:
    w = int(input())
    if w >= 0:
        numbers_list.append(w)
    else:
        print(sum(numbers_list))
        break
