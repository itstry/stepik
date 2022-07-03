list_num = ([int(input()) for _ in range(int(input()))])
list_neg, list_zero, list_posit = [], [], []
for i in list_num:
    if i < 0:
        list_neg.append(i)
    elif i == 0:
        list_zero.append(i)
    else:
        list_posit.append(i)
print(*list_neg, sep='\n')
print(*list_zero, sep='\n')
print(*list_posit, sep='\n')
