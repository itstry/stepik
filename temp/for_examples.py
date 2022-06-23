a1, b1, a2, b2, space = int(input()), int(input()), int(input()), int(input()), ' '
if (b1 < a2 and a1 < b2) or (b2 < a1 and a2 < b1):
    print('пустое множество')
elif b1 == a2 or a1 == b2:
    print(a1 if (a1 == b2) else a2)
elif a1 < a2 or a1 == a2:
    if b1 > b2 or b1 == b2:
        print(a2, b2)
    if b1 < b2:
        print(a2, b1)
elif a1 > a2 or a1 == a2:
    if b1 < b2 or b1 == b2:
        print(a1, b1)
    if b1 > b2:
        print(a1, b2)
