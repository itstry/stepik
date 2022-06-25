# 2 день; +58 задача; всего: 58

a1, b1, a2, b2, space = int(input()), int(input()), int(input()), int(input()), ' '
if (a2 > b1 and a1 < b2) or (a1 > b2 and a2 < b1):
    print('пустое множество')
elif b1 == a2 or a1 == b2:
    print(a1 if (a1 == b2) else a2)
elif a1 <= a2:
    print(str(a2) + space + str(b2) if (b1 >= b2) else str(a2) + space + str(b1))
elif a1 >= a2:
    print(str(a1) + space + str(b1) if (b1 <= b2) else str(a1) + space + str(b2))
