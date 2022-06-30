from math import factorial

num = int(input())
sum_num = 0

for i in range(1, num + 1):
    sum_num = sum_num + factorial(i)

print(sum_num)
