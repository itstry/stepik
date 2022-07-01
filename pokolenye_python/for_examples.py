line = input()
x = line.find('h')
y = line.rfind('h')
print(line[:x] + line[y + 1:])
