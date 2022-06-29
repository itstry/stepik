num = int(input())
num2 = num // 2

for j in range(1, num2 + 1):
    print('*' * j)
for j in range(num2 + 1, 0, -1):
    print('*' * j)
