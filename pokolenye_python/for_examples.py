list_num = ([int(input()) for i in range(int(input()))])
del list_num[list_num.index(max(list_num))], list_num[list_num.index(min(list_num))]
print(*list_num, sep='\n')
