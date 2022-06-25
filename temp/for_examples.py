# 5 day; 6 задача; total: 103
m = int(input())
n = int(input())

if m <= n:
    for i in range(m, n + 1):
        print(i)
if m > n:
    for i in range(m, n - 1, -1):
        print(i)
