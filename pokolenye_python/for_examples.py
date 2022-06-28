# 8 day; 2 задача; total: 130
num = int(input())
first_2_num = num
counter_len = 0
while num > 0:
    latest_num = num % 10
    if latest_num > -1:
        counter_len += 1
    num //= 10
print((first_2_num//(10**(counter_len-2)))%10)
