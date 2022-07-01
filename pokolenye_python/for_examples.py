counter_11 = 0

for i in range(int(input())):
    counter_11 += 1 if (input().count('11')) >= 3 else 0
print(counter_11)
