line = input()
x = any(i in line for i in '1234567890')
print('Цифр нет' if x == 0 else 'Цифра')
