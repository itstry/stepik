list_line = input().split()
print(*[list_line[i][0] + '.' for i in range(len(list_line))], sep='')
