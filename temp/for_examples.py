# 1 день; +47 задача; всего: 47
a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b:
    print('YES')
else:
    print('NO')
