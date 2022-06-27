# 7 day; 7 задача; total: 126
num = int(input())
while num != 0:
    print(last_num := num % 10)
    num //= 10
