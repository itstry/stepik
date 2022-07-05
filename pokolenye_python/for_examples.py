list_in = input().split()
list_out = []
for i in list_in:
    i = i + i[0] + 'ки'
    list_out.append(i[1:])
print(*list_out)
