list_line = input().split()
counter_pair = 0

for k in range(len(list_line)):
    for i in range(k+1, len(list_line)):
        if list_line[k] == list_line[i]:
            counter_pair += 1
print(counter_pair)
