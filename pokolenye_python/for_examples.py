# 5 day; 14 задача; total: 111
# ^-^ в профиле ссылка гитхаб
i = int(input())
total = 0
for i in range(1, i + 1):
    if (i**2)%10 == 2 or (i**2)%10 == 5 or (i**2)%10 == 8:
        total += i
print(total)
