# 4 day; 13 задача; total: 101
m, p, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    print(i, m)
    m = m + (m * (p / 100))
