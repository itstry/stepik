list_word = ([input() for i in range(int(input()))])
list_new = []
for k in list_word:
    if k not in list_new:
        list_new.append(k)
print(*list_new, sep='\n')
