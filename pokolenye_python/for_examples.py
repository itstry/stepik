num = int(input())
multi_num = 1
while num > 0:
    digit = num % 10
    multi_num = multi_num * digit
    num //= 10
print(multi_num)