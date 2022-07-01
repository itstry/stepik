line = input()
index_1_h = line.find('h')
index_2_h = line.rfind('h')

print(line[:index_1_h + 1] + line[index_2_h - 1:index_1_h:-1] + line[index_2_h:])
