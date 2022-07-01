line = input()
new_line = ''

for ch in range(len(line)):
    if ch % 3 == 0:
        pass
    else:
        new_line += line[ch]
print(new_line)
