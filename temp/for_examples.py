# 1 день; +50 задача; всего: 50
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if ((y1 + 1 == y2 or y1 - 1 == y2) and (x1 - 1 == x2 or x1 == x2 or x1 + 1 == x2)) or (
        y2 == y1 and (x1 - 1 == x2 or x1 + 1 == x2)):
    print('YES')
else:
    print('NO')
