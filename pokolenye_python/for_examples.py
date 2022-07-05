num_str = int(input().strip('#'))
list_str = ([input() for _ in range(num_str)])

for i in list_str:
    list_str[list_str.index(i)] = i[:i.index('#')].rstrip()
print(*list_str, sep='\n')
