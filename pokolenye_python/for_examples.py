# 7 day; 2 задача; total: 121
# ^-^ в профиле ссылка гитхаб
list_names = []
while True:
    w = input()
    if w == 'стоп' or w == 'хватит' or w == 'достаточно':
        print(len(list_names))
        break
    else:
        list_names.append(w)

