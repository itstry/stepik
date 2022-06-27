# 7 day; 8 задача; total: 127
num = int(input())
while num != 0:
    print(last_num := num % 10, end='')
    num //= 10
