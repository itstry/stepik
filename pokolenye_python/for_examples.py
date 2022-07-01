line = input()

if line.count('f') == 1:
    print('-1')
elif line.count('f') == 0:
    print('-2')
else:
    index_f = line.find('f')
    line = line[:index_f] + line[index_f + 1:]
    if len(line) == 1:
        print(1)
        exit()
    print(line.find('f') + 1)
