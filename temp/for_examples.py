# 2 день; +57 задача; всего: 57

if (i := int(input())) not in range(0, 37):
    print('ошибка ввода')
elif (i in range(1, 11)) or (i in range(19, 29)):
    print('красный' if i % 2 != 0 else 'черный')
elif (i in range(11, 19)) or (i in range(29, 37)):
    print('черный' if i % 2 != 0 else 'красный')
elif i == 0:
    print('зеленый')
