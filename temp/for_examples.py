# 2 день; +62 задача; всего: 62

i = int(input())
roman_list = [None, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
if i not in range(1, 11):
    print('ошибка')
else:
    print(roman_list[i])
