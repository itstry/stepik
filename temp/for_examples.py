# 2 день; +65 задача; всего: 65

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + x2 + y1 + y2) % 2 != 0 and x1 != x2 and y1 != y2:
    print('YES')
else:
    print('NO')
