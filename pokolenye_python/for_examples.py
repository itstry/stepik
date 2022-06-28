# 8 day; 5 задача; total: 133
num = int(input())

for i in range(2, num + 1):
    if num % i == 0:
        break
print(i)
