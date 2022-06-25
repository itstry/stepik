# 5 день; +9 задача; всего: 157
x = 0
while i := input():
    if i.isnumeric():
        x = int(i) + x
    elif i == '' or i == '=':
        break
print(x)


