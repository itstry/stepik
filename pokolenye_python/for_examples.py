# 5 day; 13 задача; total: 110
# ^-^ в профиле ссылка гитхаб
from math import log

i = int(input())
total = 0
for i in range(1, i + 1):
    total += 1 / i
print(total - log(i))
