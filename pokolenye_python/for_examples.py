print(*(list_num := [int(input()) for i in range(int(input()))]), sep='\n', end='\n\n')
print(*[k ** 2 + 2 * k + 1 for k in list_num], sep='\n')
