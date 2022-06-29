# 9 day; 3 задача; total: 139
num = int(input())
max_digit = -1
while num > 0:
    last_digit = num % 10
    if last_digit % 3 == 0 and last_digit > max_digit:
        max_digit = last_digit
    num //= 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
