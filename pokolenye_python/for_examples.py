num = int(input())
sum_num = 0
while num > 9:
    while num > 0:
        last_digit = num % 10
        sum_num += last_digit
        num //= 10
    num = sum_num
    sum_num = 0
print(num)
