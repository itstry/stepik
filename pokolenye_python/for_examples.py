num = int(input())

latest_digit = num % 10

counter_digit_3 = counter_latest_digit = counter_even = counter_digit_0_and_5 = 0
sum_digit_greater_5, multi_digit_greater_7 = 0, 1

while num > 0:
    last_digit = num % 10

    if last_digit == 3:
        counter_digit_3 += 1
    if last_digit == latest_digit:
        counter_latest_digit += 1
    if last_digit % 2 == 0:
        counter_even += 1
    if last_digit > 5:
        sum_digit_greater_5 += last_digit
    if last_digit > 7:
        multi_digit_greater_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        counter_digit_0_and_5 += 1

    num //= 10

print(counter_digit_3)
print(counter_latest_digit)
print(counter_even)
print(sum_digit_greater_5)
print(multi_digit_greater_7)
print(counter_digit_0_and_5)
