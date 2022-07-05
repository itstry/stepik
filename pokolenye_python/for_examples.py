num_str = int(input().strip('#'))
list_str = ([input() for _ in range(num_str)])

for i in list_str:
    k = i
    while '#' in k:
        k = k[:-1]
    list_str[list_str.index(i)] = k.rstrip()

print(*list_str, sep='\n')
