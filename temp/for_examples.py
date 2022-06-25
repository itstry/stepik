# 5 day; 7 задача; total: 104

m = int(input())
n = int(input())
m = ((((m - 1) // 2) * 2) + 1)
[print(i) for i in range(m, n - 1, -2)]
