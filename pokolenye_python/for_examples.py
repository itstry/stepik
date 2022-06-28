# 8 day; 1 задача; total: 129
num = int(input())
last_num = num % 10
first_num = num
sum_num = 0
mult_num = 1
counter_len = 0
while num > 0:
    latest_num = num % 10
    if latest_num > 0:
        sum_num = latest_num + sum_num
        mult_num = latest_num * mult_num
        counter_len += 1
    num //= 10

print(sum_num)  # сумма цифр
print(counter_len)  # кол-во цифр
print(mult_num)  # произведение цифр
print(sum_num / counter_len)  # среднее арифметическое
print(first_num := first_num // (10 ** (counter_len - 1)))  # первая цифра
print(first_num + last_num)  # сумма 1 и последней цифр
