# 5 day; 19 задача; total: 116
# ^-^ в профиле ссылка гитхаб

numbers_count = int(input())
numbers_list = []

for i in range(1, numbers_count+1):
    numbers_list.append(int(input()))
k = sorted(numbers_list)
print(k[numbers_count-1])
print(k[numbers_count-2])