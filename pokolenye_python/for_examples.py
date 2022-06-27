# 7 day; 9 задача; total: 128
num = int(input())
max_num = 0
min_num = num % 10
while num != 0:
    last_num = num % 10
    if last_num > max_num:
        max_num = last_num
    if last_num < min_num:
        min_num = last_num

    num //= 10
print(f'Максимальная цифра равна {max_num}')
print(f'Минимальная цифра равна {min_num}')
