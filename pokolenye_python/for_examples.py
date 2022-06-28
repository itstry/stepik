# 8 day; 3 задача; total: 131
num = int(input())
temp_num = num % 10
flag = 'YES'
while num > 0:
    latest_num = num % 10
    if latest_num != temp_num:
        flag = 'NO'
    num //= 10
print(flag)