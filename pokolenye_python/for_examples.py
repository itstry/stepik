a_num = int(input())
b_num = int(input())

max_div_now = max_div_out = 0  # делитель, внутренний и максимальный
sum_div_now = sum_div_out = 0  # сумматор, внутренний и максимальный

for i in range(a_num, b_num + 1):
    for k in range(1, i + 1):
        max_div_now = i  # записываем делитель внутренний
        if i % k == 0:
            sum_div_now += k
    if sum_div_now >= sum_div_out and max_div_now > max_div_out:
        max_div_out, sum_div_out = max_div_now, sum_div_now  # обмен переменными

    max_div_now = counter_now = sum_div_now = 0  # обнуление внутренних переменных

print(max_div_out, sum_div_out)
