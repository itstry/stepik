list_num = ([int(i) for i in input().split()])
print(*[n * '+' for n in list_num], sep='\n')
