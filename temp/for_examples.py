# хз какой день; +83 задача; всего: 83

len_names = sorted(len_names := [len(input()), len(input()), len(input())])

if len_names[2] - len_names[1] == len_names[1] - len_names[0]:
    print('YES')
else:
    print('NO')
