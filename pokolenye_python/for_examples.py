line = input()
if line.count('f') == 0:
    print('NO')
    exit()
print(line.find('f'), end=' ')
if line.count('f') > 1:
    print(line.rfind('f'))
