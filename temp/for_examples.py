# 2 день; +60 задача; всего: 60

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + y1) % 2 == 0:
    z1 = 1
else:
    z1 = 2

if (x2 + y2) % 2 == 0:
    z2 = 1
else:
    z2 = 2

if z1 == z2:
    print('YES')
else:
    print('NO')
