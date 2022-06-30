line = input()
counter_double = 0
for i in range(len(line)-1):
    if line[i] == line[i + 1]:
        counter_double += 1
print(counter_double)
