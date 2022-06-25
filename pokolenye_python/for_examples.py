# 5 day; 17 задача; total: 114
# ^-^ в профиле ссылка гитхаб
j = int(input())
result = 0
for i in range(1, j + 1):
    if j % i == 0:
        result += i
print(result)
