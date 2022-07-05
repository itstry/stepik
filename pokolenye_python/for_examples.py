list_str = ([input() for _ in range(int(input().strip('#')))])
print(*((i[:i.index('#')].rstrip()) if '#' in i else i for i in list_str), sep='\n')
