# 5 day; 18 задача; total: 115
# ^-^ в профиле ссылка гитхаб
j = int(input())
result_1 = 0
result_2 = 0
for i in range(1, j + 1, 2):
    result_1 += i
for i in range(2, j + 1, 2):
    result_2 += i
print(result_1-result_2)
