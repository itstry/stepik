# 8 day; 4 задача; total: 132
num = int(input())
temp_num = num % 10
flag = 'YES'
num //= 10
while num > 0:
    latest_num = num % 10
    if latest_num - 1 != temp_num:
        flag = 'NO'
        break
    temp_num = num % 10

    num //= 10

print(flag)
