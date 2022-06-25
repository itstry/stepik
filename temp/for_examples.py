# 4 день; +4 задача; всего: 92


from math import sqrt

a, b, c = float(input()), float(input()), float(input())
discriminant = b * b - 4 * a * c
if discriminant < 0:
    print('Нет корней')
elif discriminant == 0:
    print(-b / (2 * a))
elif discriminant > -0:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    quar_list = [x1, x2]
    print(f'{min(quar_list)}\n{max(quar_list)}')
