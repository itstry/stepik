list_num = ([int(i) for i in input().split('.')])
flag = 'ДА'
for i in list_num:
    if i > 255:
        flag = 'НЕТ'
print(flag)
