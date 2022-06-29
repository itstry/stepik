num = int(input())

for i in range(1, num + 1):
    print(i, end='')
    for k in range(1, i + 1):
        if i % k == 0:
            print('+', end='')
    print()
