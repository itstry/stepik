# 1 день; +46 задача; всего: 46
z = int(input())

if 1000 <= z <= 9999:
    if z % 7 == 0 or z % 17 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
