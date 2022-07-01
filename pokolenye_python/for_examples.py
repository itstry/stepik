from math import ceil

line = input()

len_line_2 = ceil(len(line) / 2)
print(line[len_line_2:] + line[:len_line_2])
