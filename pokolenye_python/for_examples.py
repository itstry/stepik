list_num = input().split('-')
if list_num[0] == '7':
    del list_num[0]

if len(list_num[0]) == 3 and len(list_num[1]) == 3 and len(list_num[2]):
    if list_num[0].isdigit() and list_num[1].isdigit() and list_num[2].isdigit():
        print('YES')
    else:
        print('NO')
else:
    print('NO')
